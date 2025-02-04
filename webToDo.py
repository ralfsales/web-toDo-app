import streamlit as st
import functions

if "todos" not in st.session_state:
    st.session_state["todos"] = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()  # Avoid empty lines
    if todo:  # Only add if not empty
        st.session_state["todos"].append(todo + "\n")
        functions.write_todos(st.session_state["todos"])
    st.session_state["new_todo"] = ""  # Clear input

st.title("To-Do App")
st.subheader("This is my To Do list.")
st.write("This app is to increase your productivity.")

# Display todos with checkboxes
for index, todo in enumerate(st.session_state["todos"]):
    if st.checkbox(todo, key=f"todo_{index}"):
        st.session_state["todos"].pop(index)
        functions.write_todos(st.session_state["todos"])
        st.rerun()  # Force rerun to update UI

# Input field to add new todos
st.text_input("Type a to-do:", on_change=add_todo, key='new_todo', placeholder="Enter a task")
