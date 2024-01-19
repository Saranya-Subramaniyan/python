import streamlit as st
import if_else

todos = if_else.get_todos()

def add_todo():
  todo =st.session_state["new todo"]
  print(todo)
  todos.append(todo)
  if_else.write_todos(todos)

st.title("My welcome app")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    print(checkbox)


st.text_input(label="", placeholder=" add new todo ..",on_change=add_todo, key='new_todo')

print("Hello")

st.session_state