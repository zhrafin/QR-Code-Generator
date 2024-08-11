import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

def generate_qr(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image with specified colors
    img_qr = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGBA')

    return img_qr

def main():
    st.title("Custom QR Code Generator")

    # Input text
    data = st.text_input("Enter the text or URL for the QR code")

    # Color selection
    fill_color = st.color_picker("Pick a color for the QR code", "#000000")
    back_color = st.color_picker("Pick a background color for the QR code", "#ffffff")

    # Generate QR code
    if st.button("Generate Now"):
        if data:
            img_qr = generate_qr(data, fill_color, back_color)

            # Display QR code
            st.image(img_qr, caption="Your QR code", use_column_width=True)

            # Prepare for download
            buf = BytesIO()
            img_qr.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="Download QR code",
                data=byte_im,
                file_name="custom_qr_code.png",
                mime="image/png"
            )
        else:
            st.error("Please enter the text or URL for the QR code.")

if __name__ == "__main__":
    main()
