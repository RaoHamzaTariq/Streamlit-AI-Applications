import numpy as np
import png

class Image:
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        """
        Initializes an Image object.

        Args:
            x_pixels (int, optional): Number of pixels in the x-dimension. Defaults to 0.
            y_pixels (int, optional): Number of pixels in the y-dimension. Defaults to 0.
            num_channels (int, optional): Number of color channels (e.g., 3 for RGB). Defaults to 0.
            filename (str, optional): Name of the PNG file to read. Defaults to ''.
        """
        if x_pixels and y_pixels and num_channels:
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = num_channels
            self.array = np.zeros((y_pixels, x_pixels, num_channels))  # Corrected shape order to (y, x, c)
        elif filename:
            self.array = self.read_image(filename)
            self.y_pixels, self.x_pixels, self.num_channels = self.array.shape # Corrected order
        else:
            raise ValueError("You need to input either a filename OR specify the dimensions of the image")

    def read_image(self, filename, gamma=2.2):
        """
        Reads a PNG RGB image, returning a 3D numpy array organized along Y, X, channel.
        Values are float, gamma is decoded.

        Args:
            filename (str): Name of the PNG file to read.
            gamma (float, optional): Gamma value for decoding. Defaults to 2.2.

        Returns:
            numpy.ndarray: A 3D numpy array (Y, X, channel) representing the image.
        """
        try:
            reader = png.Reader(filename)
            width, height, pixels, metadata = reader.read()
            pixels_array = np.array(list(pixels), dtype=np.uint8)  # Convert iterator to numpy array
            if metadata['planes'] == 3:
                pixels_array = pixels_array.reshape(height, width, 3)  # Corrected shape order to (h, w, c)
            elif metadata['planes'] == 4:
                pixels_array = pixels_array[:, : , :3]
                pixels_array = pixels_array.reshape(height, width, 3)
            else:
                raise ValueError(f"Unsupported number of planes: {metadata['planes']}")

            # Convert to float and then apply gamma correction
            float_array = pixels_array.astype(np.float32) / 255.0
            float_array = float_array ** gamma
            return float_array
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")
        except png.Error as e:
            raise png.Error(f"Error reading PNG file: {e}")
        except ValueError as e:
            raise ValueError(f"Error processing PNG data: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def write_image(self, output_file_name, gamma=2.2):
        """
        3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png.

        Args:
            output_file_name (str): Name of the PNG file to write.
            gamma (float, optional): Gamma value for encoding. Defaults to 2.2.
        """
        try:
            im = np.clip(self.array, 0, 1)
            y, x, c = im.shape  # Get dimensions
            im = im**(1/gamma) # Apply inverse gamma
            im = (im * 255).round().astype(np.uint8)  # Scale to 0-255 and convert to uint8
            im = im.reshape(y, x * c)  # Reshape for png writer

            writer = png.Writer(x, y, greyscale=False, bitdepth=8) #initialize the writer
            with open(output_file_name, 'wb') as f:
                writer.write(f, im)
        except png.Error as e:
            raise png.Error(f"Error writing PNG file: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!

    # # this is the non vectorized version
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor

    # faster version that leverages numpy
    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[y, x, c] = (image.array[y, x, c] - mid) * factor + mid # changed the order to y,x

    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    neighbor_range = kernel_size // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a kernel of 3, this value should be 1)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # we are going to use a naive implementation of iterating through each neighbor and summing
                # there are faster implementations where you can use memoization, but this is the most straightforward for a beginner to understand
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(new_im.x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(new_im.y_pixels - 1, y + neighbor_range) + 1):
                        total += image.array[y_i, x_i, c] # changed the order to y_i, x_i
                new_im.array[y, x, c] = total / (kernel_size ** 2) # changed the order to y, x
    return new_im

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    neighbor_range = kernel.shape[0] // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a 3x3 kernel, this value should be 1)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(new_im.x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(new_im.y_pixels - 1, y + neighbor_range) + 1):
                        x_k = x_i - (x - neighbor_range)
                        y_k = y_i - (y - neighbor_range)
                        kernel_val = kernel[y_k, x_k]
                        total += image.array[y_i, x_i, c] * kernel_val # changed the order to y_i, x_i
                new_im.array[y, x, c] = total # changed the order to y, x
    return new_im

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[y, x, c] = (image1.array[y, x, c] ** 2 + image2.array[y, x, c] ** 2) ** 0.5 # changed the order to y, x
    return new_im

if __name__ == '__main__':
    try:
        lake = Image(filename='lake.png')
        city = Image(filename='city.png')

        # brightening
        brightened_im = brighten(lake, 1.7)
        brightened_im.write_image('brightened.png')

        # darkening
        darkened_im = brighten(lake, 0.3)
        darkened_im.write_image('darkened.png')

        # increase contrast
        incr_contrast = adjust_contrast(lake, 2, 0.5)
        incr_contrast.write_image('increased_contrast.png')

        # decrease contrast
        decr_contrast = adjust_contrast(lake, 0.5, 0.5)
        decr_contrast.write_image('decreased_contrast.png')

        # blur using kernel 3
        blur_3 = blur(city, 3)
        blur_3.write_image('blur_k3.png')

        # blur using kernel size of 15
        blur_15 = blur(city, 15)
        blur_15.write_image('blur_k15.png')

        # let's apply a sobel edge detection kernel on the x and y axis
        sobel_x = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
        sobel_x.write_image('edge_x.png')
        sobel_y = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
        sobel_y.write_image('edge_y.png')

        # let's combine these and make an edge detector!
        sobel_xy = combine_images(sobel_x, sobel_y)
        sobel_xy.write_image('edge_xy.png')
        print("All operations completed successfully. Check the output images.")

    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure that the 'lake.png' and 'city.png' files exist in the same directory as the script, and that you have the 'pypng' library installed (pip install pypng).")
