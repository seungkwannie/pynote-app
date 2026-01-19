import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pynote - Simple Notes", page_icon="📝")

# --- APP TITLE ---
st.title("📝 Pynote App")
st.subheader("Your personal Python-powered notepad")

# --- INITIALIZE SESSION STATE ---
# This keeps your notes from disappearing when the app refreshes
if "notes" not in st.session_state:
    st.session_state.notes = []

# --- SIDEBAR: VIEW SAVED NOTES ---
with st.sidebar:
    st.header("My Notes")
    st.text_input("Search Notes", key="search_query", placeholder="Type to search...")
    if not st.session_state.notes:
        st.write("No notes saved yet.")
    else:
        for i, note in enumerate(st.session_state.notes):
            # Show a snippet of the note as a button/label
            st.info(f"**{note['title']}**\n\n{note['date']}")
            if st.button(f"View Note {i+1}"):
                st.session_state.selected_note = note
                # Display selected note details

                for notes in reversed(st.session_state.notes):
                    with st.subheader(f"{notes['title']} - {notes['date']}"):
                        st.write(notes['content'])

                # if "selected_note" in st.session_state:
                #     note = st.session_state.selected_note
                #     st.subheader(note['title'])
                #     st.write(f"*Date: {note['date']}*")
                #     st.write(note['content'])
                # # Divider
                # st.divider()




# --- MAIN INTERFACE: CREATE NOTE ---
with st.container():
    title = st.text_input("Note Title", placeholder="e.g., Grocery List")
    content = st.text_area("Write your note here...", height=200)

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Save Note"):
            if title and content:
                new_note = {
                    "title": title,
                    "content": content,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.notes.append(new_note)
                st.success("Note saved successfully!")
            else:
                st.error("Please provide both a title and content.")

# --- DISPLAY CURRENT NOTES ---
st.divider()
if st.session_state.notes:
    st.subheader("Recent Entries")
    # Display the latest note first
    for note in reversed(st.session_state.notes):
        with st.expander(f"{note['title']} - {note['date']}"):
            st.write(note['content'])

# git add app.py
# git commit -m "fixed notes"
# git push origin main