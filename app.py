import streamlit as st

def fetch_book_info(isbn):
    # Placeholder function - replace with actual API calls or data fetching logic
    return {
        "title": "Example Book Title",
        "author": "John Doe",
        "publisher": "Example Publisher"
    }

st.title('Book Information by ISBN')
st.write('Enter an ISBN to get the title, author, and publisher of the book.')

isbn = st.text_input('Enter ISBN', '')

if isbn:
    st.write(f'ISBN entered: {isbn}')
    
    book_info = fetch_book_info(isbn)

    st.subheader('Book Information')
    st.write(f"**Title:** {book_info['title']}")
    st.write(f"**Author:** {book_info['author']}")
    st.write(f"**Publisher:** {book_info['publisher']}")
