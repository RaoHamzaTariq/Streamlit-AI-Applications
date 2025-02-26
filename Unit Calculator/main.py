import streamlit as st
from agent_with_tools.agent import graph
from langchain_core.messages import HumanMessage, AIMessage

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Unit Conversion Chatbot")

# Display chat messages from history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Accept user input
if prompt := st.chat_input("Ask me to convert units (e.g., 'Convert 10 kg to pounds')"):
    # Add user message to chat history
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response from the agent
    result = graph.invoke({"messages": [HumanMessage(content=prompt)]})
    assistant_response = result["messages"][-1]
    
    # Add assistant response to chat history
    st.session_state.messages.append(assistant_response)
    with st.chat_message("assistant"):
        st.markdown(assistant_response.content)


# from langchain_core.messages import HumanMessage, AIMessage
# import streamlit as st
# from agent_with_tools.agent import graph

# st.title("Unit Convertor with LLM Model")

# prompt = st.chat_input("Ask me to convert units (e.g., 'Convert 10 kg to pounds')")

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# for messages in st.session_state.messages:
#     if isinstance(messages, HumanMessage):
#         with st.chat_message("user"):
#             st.markdown(messages.content)
#     elif isinstance(messages, AIMessage):
#         with st.chat_message("assistant"):
#             st.markdown(messages.content)
    

# if prompt:
#     # Add user message to chat history
#     st.session_state.messages.append(HumanMessage(content=prompt))
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     result =  graph.invoke({"messages":[HumanMessage(content=prompt)]})
#     agent_response = result['messages'][-1]
#     st.session_state.message.append(agent_response)
#     with st.chat_message("assistant"):
#         st.markdown(agent_response.content)