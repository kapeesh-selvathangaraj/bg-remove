import streamlit as st
from PIL import Image
import subprocess
import sys

try:
    # Install rembg using the user flag and without using the system site-packages
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "--no-binary", ":all:", "rembg"])

    # Now you can import rembg
    from rembg import remove

except subprocess.CalledProcessError as e:
    print(f"Error while installing rembg: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


from rembg import remove
from io import BytesIO

def removebg(img):
    # Convert the uploaded file to bytes
    img_bytes = img.read()

    # Process the image using removebg
    output_bytes = remove(img_bytes)

    # Return the result as a PIL Image
    return Image.open(BytesIO(output_bytes))

def main():
    st.title("Background Remover App")
    uploaded_file = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Remove Background"):
            result = removebg(uploaded_file)
            st.image(result, caption="Image with Background Removed", use_column_width=True)

if __name__ == "__main__":
    main()
