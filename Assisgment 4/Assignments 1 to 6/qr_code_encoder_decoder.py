import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def qr_code_encoder(filename,data):
    img = qrcode.make(data)
    img.save(f"{filename}.png")
    return f"{filename}.png is created"

def qr_code_decoder(filename,extension):
    img = Image.open(f"{filename}.{extension}")
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(obj.data)

def main():
    
    while True:
        print("\n1. QR Code Encoder")
        print("2. QR Code Decoder")
        print("3. Exit")

        user_input = int(input("Enter the method number: "))

        try:
            if user_input == 1:
                filename = input("Enter the filename: ")
                data = input("Enter the data to encode: ")
                print(qr_code_encoder(filename,data))
            elif user_input == 2:
                filename = input("Enter the filename: ")
                extension = input("Enter the file extension: ")
                qr_code_decoder(filename,extension)
            elif user_input == 3:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter Valid number")

if __name__ == "__main__":
    main()