import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pynote - Simple Notes", page_icon="📝", layout="wide")

# --- INITIALIZE SESSION STATE ---
if "notes" not in st.session_state:
    st.session_state.notes = []
if "selected_note_index" not in st.session_state:
    st.session_state.selected_note_index = None

# --- SIDEBAR: VIEW SAVED NOTES ---
with st.sidebar:
    st.header("My Notes")

    # Button to reset the view to "Create New Note"
    if st.button("➕ Create New Note", use_container_width=True):
        st.session_state.selected_note_index = None
        st.rerun()

    st.divider()

    search_query = st.text_input("Search Notes", placeholder="Type to search...")

    if not st.session_state.notes:
        st.write("No notes saved yet.")
    else:
        for i, note in enumerate(st.session_state.notes):
            # Filter based on search
            if search_query.lower() in note['title'].lower():
                # GUI improvement: Grouping info and button in a container
                with st.container(border=True):
                    st.markdown(f"**{note['title']}**")
                    st.caption(f"🕒 {note['date']}")
                    # The fix: Setting the index tells the main area which note to load
                    if st.button(f"View Note {i + 1}", key=f"view_{i}", use_container_width=True):
                        st.session_state.selected_note_index = i
                        st.rerun()

# --- MAIN INTERFACE: DYNAMIC VIEW ---
st.title("📝 Pynote App")

# Check if we are viewing an existing note or creating a new one
if st.session_state.selected_note_index is not None:
    # VIEW/EDIT MODE
    idx = st.session_state.selected_note_index
    note = st.session_state.notes[idx]

    st.subheader(f"Viewing: {note['title']}")

    edit_title = st.text_input("Title", value=note['title'])
    edit_content = st.text_area("Content", value=note['content'], height=300)

    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("Save Changes", type="primary"):
            st.session_state.notes[idx]['title'] = edit_title
            st.session_state.notes[idx]['content'] = edit_content
            st.session_state.notes[idx]['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success("Note updated!")
            st.rerun()
    with col2:
        if st.button("Delete Note", type="secondary"):
            st.session_state.notes.pop(idx)
            st.session_state.selected_note_index = None
            st.rerun()
else:
    # CREATE MODE
    st.subheader("Create a new Python-powered note")
    with st.container(border=True):
        title = st.text_input("Note Title", placeholder="e.g., Grocery List")
        content = st.text_area("Write your note here...", height=200)

        if st.button("Save Note", type="primary"):
            if title and content:
                new_note = {
                    "title": title,
                    "content": content,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.notes.append(new_note)
                st.success("Note saved successfully!")
                st.rerun()
            else:
                st.error("Please provide both a title and content.")

# --- DISPLAY ALL ENTRIES AT BOTTOM (Optional) ---
st.divider()
if st.session_state.notes:
    st.write("### All Recent Entries")
    for note in reversed(st.session_state.notes):
        with st.expander(f"{note['title']} - {note['date']}"):
            st.markdown(note['content'])


# import streamlit as st
# import datetime
#
# # --- PAGE CONFIG ---
# st.set_page_config(page_title="Pynote - Simple Notes", page_icon="📝")
#
# # --- APP TITLE ---
# st.title("📝 Pynote App")
# st.subheader("Your personal Python-powered notepad")
#
# # --- INITIALIZE SESSION STATE ---
# # This keeps your notes from disappearing when the app refreshes
# if "notes" not in st.session_state:
#     st.session_state.notes = []
#
# # --- SIDEBAR: VIEW SAVED NOTES ---
# with st.sidebar:
#     st.header("My Notes")
#     st.text_input("Search Notes", key="search_query", placeholder="Type to search...")
#     if not st.session_state.notes:
#         st.write("No notes saved yet.")
#     else:
#         for i, note in enumerate(st.session_state.notes):
#             # Show a snippet of the note as a button/label
#             st.info(f"**{note['title']}**\n\n{note['date']}")
#             if st.button(f"View Note {i+1}"):
#                 st.session_state.selected_note = note
#
#
# # --- MAIN INTERFACE: CREATE NOTE ---
# with st.container():
#     title = st.text_input("Note Title", placeholder="e.g., Grocery List")
#     content = st.text_area("Write your note here...", height=200)
#
#     col1, col2 = st.columns([1, 5])
#     with col1:
#         if st.button("Save Note"):
#             if title and content:
#                 new_note = {
#                     "title": title,
#                     "content": content,
#                     "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 }
#                 st.session_state.notes.append(new_note)
#                 st.success("Note saved successfully!")
#             else:
#                 st.error("Please provide both a title and content.")
#
# # --- DISPLAY CURRENT NOTES ---
# st.divider()
# if st.session_state.notes:
#     st.subheader("Recent Entries")
#     # Display the latest note first
#     for note in reversed(st.session_state.notes):
#         with st.expander(f"{note['title']} - {note['date']}"):
#             st.write(note['content'])

# git add app.py
# git commit -m "fixed notes"
# git push origin main