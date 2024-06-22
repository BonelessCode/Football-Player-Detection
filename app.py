import streamlit as st
import subprocess
from PIL import Image
import os

# Streamlit app
def main():
    st.title("YOLOv8 Football Player/Ball Detection with Streamlit")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Perform inference when the user clicks the button
        if st.button("Run Football Player/Ball Detection"):
            # Save the uploaded image temporarily
            image_path = "temp_image.jpg"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Use subprocess to run the YOLO prediction command and capture the output
            command = f"yolo task=detect mode=predict model=best.pt conf=0.55 source={image_path}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Get the latest prediction directory
            dir = os.listdir(os.getcwd()+"/runs/detect")
            # Extract the numeric part from each string and convert to integers
            numeric_parts = [int(folder.lstrip('predict')) if folder.lstrip('predict').isdigit() else 0 for folder in dir]  
            
            prediction_image_path = os.path.join(os.getcwd()+"/runs/detect/predict"+str(max(numeric_parts))+"/temp_image.jpg")

            print("prediction_image_path")
            print(prediction_image_path)

            # Display the saved prediction image
            prediction_image = Image.open(prediction_image_path)
            st.image(prediction_image, caption="Prediction Image", use_column_width=True)

            # Remove the temporary and prediction image files
            #os.remove(image_path)
            #os.remove(prediction_image_path)

if __name__ == "__main__":
    main()
