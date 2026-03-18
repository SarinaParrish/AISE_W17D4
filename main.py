from transformers import pipeline
from PIL import Image
import os

def load_model():
    print("🔄 Loading model...")
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
def run_on_images(folder="images"):
    captioner = load_model()

    if not os.path.exists(folder):
        print("❌ No 'images' folder found")
        return

    files = os.listdir(folder)

    if not files:
        print("❌ No images found in folder")
        return

    for filename in files:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(folder, filename)
            image = Image.open(path)

            result = captioner(image)
            caption = result[0]['generated_text']

            print("\n-------------------------")
            print(f"🖼️ Image: {filename}")
            print(f"📝 Caption: {caption}")

if __name__ == "__main__":
    run_on_images()