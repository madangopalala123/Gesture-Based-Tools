# # import cv2
# # import streamlit as st
# # import time
# # import threading
# # from scripts.keyboard import run_virtual_keyboard  # Import your actual function from scripts/keyboard.py
# # from scripts.mouse import runvirtualmouse  # Import your actual function from scripts/mouse.py
# #
# # # Initialize session state variables if they don't exist
# # st.title("Gest Tool kit")
# # st.write("Click 'Run' to start the Project")
# #
# # # Initialize session state
# # if 'is_running' not in st.session_state:
# #     st.session_state.is_running = False
# #     st.session_state.stop_event = threading.Event()  # Event to stop the loop
# #     st.session_state.virtual_keyboard_thread = None  # To store the background thread
# #
# # # Run or stop the virtual keyboard based on the button click
# # if st.button("Run Keyboard") and not st.session_state.is_running:
# #     st.session_state.is_running = True
# #     st.session_state.stop_event.clear()  # Ensure stop event is clear when running
# #
# #     # Start the virtual keyboard in a new thread to prevent blocking Streamlit's UI
# #     thread = threading.Thread(target=run_virtual_keyboard, args=(st.session_state.stop_event,), daemon=True)
# #     st.session_state.virtual_keyboard_thread = thread  # Store the thread reference
# #     thread.start()
# #
# # # Show the Stop button only when the project is running
# # if st.session_state.is_running:
# #     if st.button("Stop Keyboard"):
# #         st.session_state.is_running = False
# #         st.session_state.stop_event.set()  # Signal the loop to stop
# #
# #         # Wait for the thread to finish, ensuring resources are cleaned up
# #         st.session_state.virtual_keyboard_thread.join()
# #
# #         st.write("The virtual keyboard has been stopped.")
# #         cv2.destroyAllWindows()  # Close OpenCV window if it's open
# #
# import cv2
# import streamlit as st
# import time
# import threading
# from scripts.keyboard import run_virtual_keyboard  # Import your actual function from scripts/keyboard.py
# from scripts.mouse import runvirtualmouse  # Import your actual function from scripts/mouse.py
#
# # Initialize session state variables if they don't exist
# st.title("Gest Tool Kit")
# st.write("Click 'Run' to start the project.")
#
# # Initialize session state for all projects
# if 'is_running' not in st.session_state:
#     st.session_state.is_running = None  # None means no task is running
#     st.session_state.stop_event = threading.Event()  # Event to stop the loop
#     st.session_state.keyboard_thread = None  # To store the keyboard thread
#     st.session_state.mouse_thread = None  # To store the mouse thread
#     st.session_state.progress = ""  # For task progress messages
#
# # Function to manage stopping and cleaning up a thread
# def stop_task(task_name):
#     if task_name == "keyboard":
#         st.session_state.stop_event.set()
#         if st.session_state.keyboard_thread:
#             st.session_state.keyboard_thread.join()
#         cv2.destroyAllWindows()
#     elif task_name == "mouse":
#         st.session_state.stop_event.set()
#         if st.session_state.mouse_thread:
#             st.session_state.mouse_thread.join()
#
#     # Reset the session state
#     st.session_state.is_running = None
#     st.session_state.progress = f"{task_name.capitalize()} task has been stopped."
#
# # Project 1 - Keyboard
# st.header("Project 1: Virtual Keyboard")
#
# # Disable the 'Run' button if any task is running
# if st.session_state.is_running is None:
#     run_button_disabled = False
# else:
#     run_button_disabled = True
#
# # Run the virtual keyboard
# if st.button("Run Keyboard") and st.session_state.is_running is None:
#     st.session_state.is_running = "keyboard"  # Set the current running task to "keyboard"
#     st.session_state.stop_event.clear()  # Clear any existing stop event
#
#     # Start the virtual keyboard in a new thread
#     thread = threading.Thread(target=run_virtual_keyboard, args=(st.session_state.stop_event,), daemon=True)
#     st.session_state.keyboard_thread = thread
#     thread.start()
#
#     st.write("Virtual Keyboard task started...")
#
# # Stop the virtual keyboard
# if st.session_state.is_running == "keyboard":
#     if st.button("Stop Keyboard"):
#         stop_task("keyboard")
#
# # Project 2 - Mouse
# st.header("Project 2: Virtual Mouse")
#
# # Run the virtual mouse (same logic as keyboard)
# if st.button("Run Mouse") and st.session_state.is_running is None:
#     st.session_state.is_running = "mouse"  # Set the current running task to "mouse"
#     st.session_state.stop_event.clear()  # Clear any existing stop event
#
#     # Start the virtual mouse in a new thread
#     thread = threading.Thread(target=runvirtualmouse, args=(st.session_state.stop_event,), daemon=True)
#     st.session_state.mouse_thread = thread
#     thread.start()
#
#     st.write("Virtual Mouse task started...")
#
# # Stop the virtual mouse
# if st.session_state.is_running == "mouse":
#     if st.button("Stop Mouse"):
#         stop_task("mouse")
#
# # Display progress messages
# if st.session_state.progress:
#     st.write(st.session_state.progress)


# import cv2
# import streamlit as st
# import threading
# from scripts.keyboard import run_virtual_keyboard  # Import your actual function from scripts/keyboard.py
# from scripts.mouse import runvirtualmouse  # Import your actual function from scripts/mouse.py
#
# # Set the page title and icon
# st.set_page_config(page_title="Gest Tool Kit", page_icon="🎮", layout="centered")
#
# # Title and Introduction Section
# st.title("🎮 Gesture Tool Kit")
# st.markdown("""
#     Welcome to the Gesture Tool Kit! Use gestures to control your keyboard and mouse.
#
#     - **Run Keyboard** to start controlling the keyboard using gestures.
#     - **Run Mouse** to start controlling the mouse with gestures.
#     - **Stop** to stop any ongoing task.
# """)
#
# # Initialize session state variables if they don't exist
# if 'is_running' not in st.session_state:
#     st.session_state.is_running = None  # None means no task is running
#     st.session_state.stop_event = threading.Event()  # Event to stop the loop
#     st.session_state.keyboard_thread = None  # To store the keyboard thread
#     st.session_state.mouse_thread = None  # To store the mouse thread
#     st.session_state.progress = ""  # For task progress messages
#
#
# # Function to manage stopping and cleaning up a thread
# def stop_task(task_name):
#     if task_name == "keyboard":
#         st.session_state.stop_event.set()
#         if st.session_state.keyboard_thread:
#             st.session_state.keyboard_thread.join()
#         cv2.destroyAllWindows()
#     elif task_name == "mouse":
#         st.session_state.stop_event.set()
#         if st.session_state.mouse_thread:
#             st.session_state.mouse_thread.join()
#
#     # Reset the session state
#     st.session_state.is_running = None
#     st.session_state.progress = f"{task_name.capitalize()} task has been stopped."
#
#
# # **Improved UI Design**: Using containers, better alignment, and buttons.
# # Project 1 - Virtual Keyboard
# with st.container():
#     st.header("🖥️ Virtual Keyboard")
#     st.subheader("Control your keyboard using gestures")
#
#     # Disable the 'Run' button if any task is running
#     run_button_disabled = st.session_state.is_running is not None
#
#     # Run the virtual keyboard
#     if st.button("Run Keyboard", disabled=run_button_disabled, use_container_width=True):
#         st.session_state.is_running = "keyboard"  # Set the current running task to "keyboard"
#         st.session_state.stop_event.clear()  # Clear any existing stop event
#
#         # Start the virtual keyboard in a new thread
#         thread = threading.Thread(target=run_virtual_keyboard, args=(st.session_state.stop_event,), daemon=True)
#         st.session_state.keyboard_thread = thread
#         thread.start()
#
#         st.session_state.progress = "Virtual Keyboard task started..."
#
#     # Stop the virtual keyboard
#     if st.session_state.is_running == "keyboard":
#         if st.button("Stop Keyboard", use_container_width=True, key="stop_keyboard"):
#             stop_task("keyboard")
#
# # Project 2 - Virtual Mouse
# with st.container():
#     st.header("🖱️ Virtual Mouse")
#     st.subheader("Control your mouse using gestures")
#
#     # Run the virtual mouse (same logic as keyboard)
#     if st.button("Run Mouse", disabled=run_button_disabled, use_container_width=True):
#         st.session_state.is_running = "mouse"  # Set the current running task to "mouse"
#         st.session_state.stop_event.clear()  # Clear any existing stop event
#
#         # Start the virtual mouse in a new thread
#         thread = threading.Thread(target=runvirtualmouse, args=(st.session_state.stop_event,), daemon=True)
#         st.session_state.mouse_thread = thread
#         thread.start()
#
#         st.session_state.progress = "Virtual Mouse task started..."
#
#     # Stop the virtual mouse
#     if st.session_state.is_running == "mouse":
#         if st.button("Stop Mouse", use_container_width=True, key="stop_mouse"):
#             stop_task("mouse")
#
# # **Progress Display**: Show task progress or status
# if st.session_state.progress:
#     st.markdown(f"#### **Progress:** {st.session_state.progress}")
#
# # Sidebar for showing current task status
# with st.sidebar:
#     st.markdown("### Current Task Status")
#     if st.session_state.is_running == "keyboard":
#         st.write("🖥️ **Virtual Keyboard** is currently running.")
#     elif st.session_state.is_running == "mouse":
#         st.write("🖱️ **Virtual Mouse** is currently running.")
#     else:
#         st.write("🔴 No task is currently running.")


# import cv2
# import streamlit as st
# import threading
# import time
# from scripts.keyboard import run_virtual_keyboard  # Import your actual function from scripts/keyboard.py
# from scripts.mouse import runvirtualmouse  # Import your actual function from scripts/mouse.py
#
#
# # Set the page title and icon
# st.set_page_config(page_title="Gest Tool Kit", page_icon="🎮", layout="centered")
#
# # Title and Introduction Section
# st.title("🎮 Gesture Tool Kit")
# st.markdown("""
#     Welcome to the Gesture Tool Kit! Use gestures to control your keyboard and mouse.
#
#     - **Run Keyboard** to start controlling the keyboard using gestures.
#     - **Run Mouse** to start controlling the mouse with gestures.
#     - **Stop** to stop any ongoing task.
# """)
#
# # Initialize session state variables if they don't exist
# if 'is_running' not in st.session_state:
#     st.session_state.is_running = None  # None means no task is running
#     st.session_state.stop_event = threading.Event()  # Event to stop the loop
#     st.session_state.keyboard_thread = None  # To store the keyboard thread
#     st.session_state.mouse_thread = None  # To store the mouse thread
#     st.session_state.keyboard_progress = ""  # For keyboard task progress messages
#     st.session_state.mouse_progress = ""  # For mouse task progress messages
#
#
# # Function to manage stopping and cleaning up a thread
# def stop_task(task_name):
#     if task_name == "keyboard":
#         st.session_state.stop_event.set()
#         if st.session_state.keyboard_thread:
#             st.session_state.keyboard_thread.join()
#         cv2.destroyAllWindows()
#     elif task_name == "mouse":
#         st.session_state.stop_event.set()
#         if st.session_state.mouse_thread:
#             st.session_state.mouse_thread.join()
#
#     # Reset the session state
#     st.session_state.is_running = None
#
#
# # **Card Layout for Projects**: Using columns and custom styling.
# col1, col2 = st.columns(2)
#
# with col1:
#     # Project 1 - Virtual Keyboard
#     st.markdown("""
#         <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
#             <h3 style="color: #333;">🖥️ Virtual Keyboard</h3>
#             <p style="color: #666;">Control your keyboard using gestures</p>
#     """, unsafe_allow_html=True)
#
#     # Create a container for progress messages
#     keyboard_progress_container = st.empty()
#
#     # Run the virtual keyboard
#     if st.button("Run Keyboard", disabled=st.session_state.is_running is not None, use_container_width=True):
#         st.session_state.is_running = "keyboard"  # Set the current running task to "keyboard"
#         st.session_state.stop_event.clear()  # Clear any existing stop event
#
#         # Start the virtual keyboard in a new thread
#         thread = threading.Thread(target=run_virtual_keyboard, args=(st.session_state.stop_event,), daemon=True)
#         st.session_state.keyboard_thread = thread
#         thread.start()
#
#         st.session_state.keyboard_progress = "keyboard started..."
#         keyboard_progress_container.markdown(
#             f"<p style='color: green; font-weight: bold;'>{st.session_state.keyboard_progress}</p>",
#             unsafe_allow_html=True)
#         time.sleep(2)  # Display for 2 seconds
#         keyboard_progress_container.empty()  # Clear the progress message
#
#     # Stop the virtual keyboard
#     if st.session_state.is_running == "keyboard":
#         if st.button("Stop Keyboard", use_container_width=True, key="stop_keyboard"):
#             stop_task("keyboard")
#             st.session_state.keyboard_progress = "keyboard stopped."
#             keyboard_progress_container.markdown(
#                 f"<p style='color: red; font-weight: bold;'>{st.session_state.keyboard_progress}</p>",
#                 unsafe_allow_html=True)
#             time.sleep(2)  # Display for 2 seconds
#             keyboard_progress_container.empty()  # Clear the progress message
#
#     st.markdown("</div>", unsafe_allow_html=True)
#
# with col2:
#     # Project 2 - Virtual Mouse
#     st.markdown("""
#         <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
#             <h3 style="color: #333;">🖱️ Virtual Mouse</h3>
#             <p style="color: #666;">Control your mouse using gestures</p>
#     """, unsafe_allow_html=True)
#
#     # Create a container for progress messages
#     mouse_progress_container = st.empty()
#
#     # Run the virtual mouse (same logic as keyboard)
#     if st.button("Run Mouse", disabled=st.session_state.is_running is not None, use_container_width=True):
#         st.session_state.is_running = "mouse"  # Set the current running task to "mouse"
#         st.session_state.stop_event.clear()  # Clear any existing stop event
#
#         # Start the virtual mouse in a new thread
#         thread = threading.Thread(target=runvirtualmouse, args=(st.session_state.stop_event,), daemon=True)
#         st.session_state.mouse_thread = thread
#         thread.start()
#
#         st.session_state.mouse_progress = "Mouse started..."
#         mouse_progress_container.markdown(
#             f"<p style='color: green; font-weight: bold;'>{st.session_state.mouse_progress}</p>",
#             unsafe_allow_html=True)
#         time.sleep(2)  # Display for 2 seconds
#         mouse_progress_container.empty()  # Clear the progress message
#
#     # Stop the virtual mouse
#     if st.session_state.is_running == "mouse":
#         if st.button("Stop Mouse", use_container_width=True, key="stop_mouse"):
#             stop_task("mouse")
#             st.session_state.mouse_progress = "Mouse stopped."
#             mouse_progress_container.markdown(
#                 f"<p style='color: red; font-weight: bold;'>{st.session_state.mouse_progress}</p>",
#                 unsafe_allow_html=True)
#             time.sleep(2)  # Display for 2 seconds
#             mouse_progress_container.empty()  # Clear the progress message
#
#     st.markdown("</div>", unsafe_allow_html=True)
#
# # Sidebar for showing current task status
# with st.sidebar:
#     st.markdown("### Current Task Status")
#     if st.session_state.is_running == "keyboard":
#         st.write("🖥️ **Virtual Keyboard** is currently running.")
#     elif st.session_state.is_running == "mouse":
#         st.write("🖱️ **Virtual Mouse** is currently running.")
#     else:
#         st.write("🔴 No task is currently running.")


import cv2
import streamlit as st
import threading
import time
from scripts.keyboard import run_virtual_keyboard  # Import your actual function from scripts/keyboard.py
from scripts.mouse import runvirtualmouse  # Import your actual function from scripts/mouse.py
from scripts.painter import run_painter  # Import your actual function from scripts/painter.py
from scripts.ppt_controller import run_ppt

# Set the page title and icon
# st.set_page_config(page_title="Gest Tool Kit", page_icon="🎮", layout="centered")
st.set_page_config(page_title="Gest Tools", layout="centered")
# Title and Introduction Section
st.title(" Gesture Based Tools")
st.markdown("""
    Welcome to the Gesture Tool Kit! Use gestures to control your keyboard, mouse, and painter.

    - **Run Keyboard** to start controlling the keyboard using gestures.
    - **Run Mouse** to start controlling the mouse with gestures.
    - **Run Painter** to start drawing using gestures.
    - **Stop** to stop any ongoing task.
""")

# Initialize session state variables if they don't exist
if 'is_running' not in st.session_state:
    st.session_state.is_running = None  # None means no task is running
    st.session_state.stop_event = threading.Event()  # Event to stop the loop
    st.session_state.keyboard_thread = None  # To store the keyboard thread
    st.session_state.mouse_thread = None  # To store the mouse thread
    st.session_state.painter_thread = None  # To store the painter thread
    st.session_state.ppt_thread = None
    st.session_state.keyboard_progress = ""  # For keyboard task progress messages
    st.session_state.mouse_progress = ""  # For mouse task progress messages
    st.session_state.painter_progress = ""  # For painter task progress messages
    st.session_state.ppt_progress = ""


# Function to manage stopping and cleaning up a thread
def stop_task(task_name):
    if task_name == "keyboard":
        st.session_state.stop_event.set()
        if st.session_state.keyboard_thread:
            st.session_state.keyboard_thread.join()
        cv2.destroyAllWindows()
    elif task_name == "mouse":
        st.session_state.stop_event.set()
        if st.session_state.mouse_thread:
            st.session_state.mouse_thread.join()
    elif task_name == "painter":
        st.session_state.stop_event.set()
        if st.session_state.painter_thread:
            st.session_state.painter_thread.join()
        cv2.destroyAllWindows()
    elif task_name == "ppt":
        st.session_state.stop_event.set()
        if st.session_state.ppt_thread:
            st.session_state.ppt_thread.join()
        cv2.destroyAllWindows()

    # Reset the session state
    st.session_state.is_running = None


# **Card Layout for Projects**: Using columns and custom styling.
col1, col2= st.columns(2)

with col1:
    # Project 1 - Virtual Keyboard
    st.markdown("""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #333;">🖥️ Virtual Keyboard</h3>
            <p style="color: #666;">Control your keyboard using gestures</p>
    """, unsafe_allow_html=True)

    # Create a container for progress messages
    keyboard_progress_container = st.empty()

    # Run the virtual keyboard
    if st.button("Run Keyboard", disabled=st.session_state.is_running is not None, use_container_width=True):
        st.session_state.is_running = "keyboard"  # Set the current running task to "keyboard"
        st.session_state.stop_event.clear()  # Clear any existing stop event

        # Start the virtual keyboard in a new thread
        thread = threading.Thread(target=run_virtual_keyboard, args=(st.session_state.stop_event,), daemon=True)
        st.session_state.keyboard_thread = thread
        thread.start()

        st.session_state.keyboard_progress = "Keyboard started..."
        keyboard_progress_container.markdown(
            f"<p style='color: green; font-weight: bold;'>{st.session_state.keyboard_progress}</p>",
            unsafe_allow_html=True)
        time.sleep(2)  # Display for 2 seconds
        keyboard_progress_container.empty()  # Clear the progress message

    # Stop the virtual keyboard
    if st.session_state.is_running == "keyboard":
        if st.button("Stop Keyboard", use_container_width=True, key="stop_keyboard"):
            stop_task("keyboard")
            st.session_state.keyboard_progress = "Keyboard stopped."
            keyboard_progress_container.markdown(
                f"<p style='color: red; font-weight: bold;'>{st.session_state.keyboard_progress}</p>",
                unsafe_allow_html=True)
            time.sleep(2)  # Display for 2 seconds
            keyboard_progress_container.empty()  # Clear the progress message

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Project 2 - Virtual Mouse
    st.markdown("""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #333;">🖱️ Virtual Mouse</h3>
            <p style="color: #666;">Control your mouse using gestures</p>
    """, unsafe_allow_html=True)

    # Create a container for progress messages
    mouse_progress_container = st.empty()

    # Run the virtual mouse (same logic as keyboard)
    if st.button("Run Mouse", disabled=st.session_state.is_running is not None, use_container_width=True):
        st.session_state.is_running = "mouse"  # Set the current running task to "mouse"
        st.session_state.stop_event.clear()  # Clear any existing stop event

        # Start the virtual mouse in a new thread
        thread = threading.Thread(target=runvirtualmouse, args=(st.session_state.stop_event,), daemon=True)
        st.session_state.mouse_thread = thread
        thread.start()

        st.session_state.mouse_progress = "Mouse started..."
        mouse_progress_container.markdown(
            f"<p style='color: green; font-weight: bold;'>{st.session_state.mouse_progress}</p>",
            unsafe_allow_html=True)
        time.sleep(2)  # Display for 2 seconds
        mouse_progress_container.empty()  # Clear the progress message

    # Stop the virtual mouse
    if st.session_state.is_running == "mouse":
        if st.button("Stop Mouse", use_container_width=True, key="stop_mouse"):
            stop_task("mouse")
            st.session_state.mouse_progress = "Mouse stopped."
            mouse_progress_container.markdown(
                f"<p style='color: red; font-weight: bold;'>{st.session_state.mouse_progress}</p>",
                unsafe_allow_html=True)
            time.sleep(2)  # Display for 2 seconds
            mouse_progress_container.empty()  # Clear the progress message

    st.markdown("</div>", unsafe_allow_html=True)
col3,col4=st.columns(2)
with col3:
    # Project 3 - Painter (Drawing with Gestures)
    st.markdown("""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #333;">🎨 Gesture Painter</h3>
            <p style="color: #666;">Draw pictures using gesture control.</p>
    """, unsafe_allow_html=True)

    # Create a container for progress messages
    painter_progress_container = st.empty()

    # Run the painter
    if st.button("Run Painter", disabled=st.session_state.is_running is not None, use_container_width=True):
        st.session_state.is_running = "painter"  # Set the current running task to "painter"
        st.session_state.stop_event.clear()  # Clear any existing stop event

        # Start the painter in a new thread
        thread = threading.Thread(target=run_painter, args=(st.session_state.stop_event,), daemon=True)
        st.session_state.painter_thread = thread
        thread.start()

        st.session_state.painter_progress = "Painter started..."
        painter_progress_container.markdown(
            f"<p style='color: green; font-weight: bold;'>{st.session_state.painter_progress}</p>",
            unsafe_allow_html=True)
        time.sleep(2)  # Display for 2 seconds
        painter_progress_container.empty()  # Clear the progress message

    # Stop the painter
    if st.session_state.is_running == "painter":
        if st.button("Stop Painter", use_container_width=True, key="stop_painter"):
            stop_task("painter")
            st.session_state.painter_progress = "Painter stopped."
            painter_progress_container.markdown(
                f"<p style='color: red; font-weight: bold;'>{st.session_state.painter_progress}</p>",
                unsafe_allow_html=True)
            time.sleep(2)  # Display for 2 seconds
            painter_progress_container.empty()  # Clear the progress message

    st.markdown("</div>", unsafe_allow_html=True)
with col4:
    # Project 2 - Virtual Mouse
    st.markdown("""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #333;">📊 ppt Controller</h3>
            <p style="color: #666;">Control your ppt using gestures</p>
    """, unsafe_allow_html=True)

    # Create a container for progress messages
    ppt_progress_container = st.empty()

    # Run the virtual mouse (same logic as keyboard)
    if st.button("Run ppt Controller", disabled=st.session_state.is_running is not None, use_container_width=True):
        st.session_state.is_running = "ppt"  # Set the current running task to "mouse"
        st.session_state.stop_event.clear()  # Clear any existing stop event

        # Start the virtual mouse in a new thread
        thread = threading.Thread(target=run_ppt, args=(st.session_state.stop_event,), daemon=True)
        st.session_state.ppt_thread = thread
        thread.start()

        st.session_state.mouse_progress = "ppt controller started..."
        ppt_progress_container.markdown(
            f"<p style='color: green; font-weight: bold;'>{st.session_state.ppt_progress}</p>",
            unsafe_allow_html=True)
        time.sleep(2)  # Display for 2 seconds
        ppt_progress_container.empty()  # Clear the progress message

    # Stop the virtual mouse
    if st.session_state.is_running == "ppt":
        if st.button("Stop ppt controller", use_container_width=True, key="stop_ppt_controller"):
            stop_task("ppt")
            st.session_state.ppt_progress = "ppt controller stopped."
            ppt_progress_container.markdown(
                f"<p style='color: red; font-weight: bold;'>{st.session_state.ppt_progress}</p>",
                unsafe_allow_html=True)
            time.sleep(2)  # Display for 2 seconds
            ppt_progress_container.empty()  # Clear the progress message

    st.markdown("</div>", unsafe_allow_html=True)


# Sidebar for showing current task status
with st.sidebar:
    st.markdown("### Current Task Status")
    if st.session_state.is_running == "keyboard":
        st.write("🖥️ **Virtual Keyboard** is currently running.")
    elif st.session_state.is_running == "mouse":
        st.write("🖱️ **Virtual Mouse** is currently running.")
    elif st.session_state.is_running == "painter":
        st.write("🎨 **Gesture Painter** is currently running.")
    elif st.session_state.is_running == "ppt":
        st.write("📊 **ppt controller** is currently running.")
    else:
        st.write("🔴 No task is currently running.")




