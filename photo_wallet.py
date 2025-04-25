#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
import os
from datetime import datetime
import uuid

# Set app config
st.set_page_config(page_title="📸 Photo Wallet", layout="wide")

# Directory to store uploaded photos
UPLOAD_DIR = "photo_storage"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# App title
st.title("📸 My Photo Wallet")

# Upload section
st.subheader("Upload a Photo")
uploaded_file = st.file_uploader("Choose a photo from your phone or computer", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded image with a unique name
    ext = uploaded_file.name.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Photo uploaded successfully!")

# Gallery
st.subheader("🖼 Your Photo Gallery")

image_files = [file for file in os.listdir(UPLOAD_DIR) if file.lower().endswith(("png", "jpg", "jpeg"))]

if image_files:
    cols = st.columns(3)
    for index, image_file in enumerate(sorted(image_files, reverse=True)):
        image_path = os.path.join(UPLOAD_DIR, image_file)
        img = Image.open(image_path)
        cols[index % 3].image(img, use_column_width=True, caption=image_file)
else:
    st.info("No photos uploaded yet.")

