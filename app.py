import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np

st.title('ISBN Reviews and Ratings')
st.write('Enter or scan an ISBN to get reviews and ratings from Amazon and Goodreads.')

isbn = st.text_input('Enter ISBN', '')

st.write("Or scan ISBN using your camera:")

class BarcodeScanner(VideoTransformerBase):
    def transform(self, frame):
        image = frame.to_image()
        image = image.convert('RGB')  # Ensure the image is in RGB format

        # Decode the barcodes in the image
        barcodes = decode(image)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            (x, y, w, h) = barcode.rect
            # Draw rectangle around the barcode
            image = np.array(image)
            image = Image.fromarray(image)
            draw = ImageDraw.Draw(image)
            draw.rectangle([(x, y), (x + w, y + h)], outline="green", width=2)
            draw.text((x, y - 10), barcode_data, fill="green")

            # Update the scanned ISBN
            st.session_state.scanned_isbn = barcode_data

        return np.array(image)

webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=BarcodeScanner)

if 'scanned_isbn' not in st.session_state:
    st.session_state.scanned_isbn = ''

if webrtc_ctx.video_receiver:
    st.write(f'Scanned ISBN: {st.session_state.scanned_isbn}')

if st.session_state.scanned_isbn:
    isbn = st.session_state.scanned_isbn

if isbn:
    st.write(f'ISBN entered: {isbn}')
    
    def fetch_amazon_reviews(isbn):
        # Placeholder function - replace with actual API calls or scraping logic
        return {
            "rating": 4.5,
            "reviews": ["Great book!", "Loved it!", "Highly recommended."]
        }

    def fetch_goodreads_reviews(isbn):
        # Placeholder function - replace with actual API calls or scraping logic
        return {
            "rating": 4.2,
            "reviews": ["Informative read.", "Engaging and well-written."]
        }

    amazon_data = fetch_amazon_reviews(isbn)
    goodreads_data = fetch_goodreads_reviews(isbn)

    st.subheader('Amazon Reviews')
    st.write(f"Rating: {amazon_data['rating']}")
    for review in amazon_data['reviews']:
        st.write(f"- {review}")

    st.subheader('Goodreads Reviews')
    st.write(f"Rating: {goodreads_data['rating']}")
    for review in goodreads_data['reviews']:
        st.write(f"- {review}")
