import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from zipfile import ZipFile

def extract_images(url, output_folder="images"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_urls = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            full_url = urljoin(url, img_url)
            image_urls.append(full_url)

    for i, img_url in enumerate(image_urls):
        img_data = requests.get(img_url).content
        img_name = os.path.join(output_folder, f'image_{i+1}.jpg')
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

    return output_folder

def create_zip(folder_path, zip_name='website_assets.zip'):
    with ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

    print(f"Assets have been zipped into {zip_name}")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    output_folder = extract_images(website_url)
    create_zip(output_folder)
