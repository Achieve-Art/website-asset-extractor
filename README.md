# Website Assets Extractor

This project extracts images and videos from a specified website and saves them into a zip file. It ensures that all assets are downloaded without any quality loss.

## Features

- Extracts images and videos from a given website URL.
- Saves extracted assets into a specified folder.
- Compresses the assets into a zip file for easy distribution.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Achieve-Art/website-assets-extractor.git
    cd website-assets-extractor
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python extract_assets.py
    ```

2. Enter the website URL when prompted.

3. The extracted assets will be saved in a folder named `assets`, and a zip file named `website_assets.zip` will be created in the current directory.

## Example

Here's an example of how to run the script:

```bash
$ python extract_assets.py
Enter the website URL: https://example.com
Assets have been zipped into website_assets.zip
