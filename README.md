# NLP Text Generator

This project provides a Python-based tool for generating human-like text using advanced NLP techniques. The tool leverages state-of-the-art language models to create coherent and contextually relevant text.

## Features

- Generate text based on user-provided prompts.
- Supports multiple text generation models.
- Configurable parameters to fine-tune the generated text.
- Easy-to-use command-line interface.

## Requirements

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/aditya-kamatt/NLP-Text-Generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd NLP-Text-Generator
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To generate text, use the provided command-line interface or run the `generate_text.py` script directly.

### Command-Line Interface

Run the script with the following command:

```bash
python generate_text.py --prompt "Your prompt here" --model "model_name" --length 100
```
- `--prompt`: The initial text to start the generation from.
- `--model`: The name of the pre-trained model to use (e.g., "gpt-2", "gpt-neo").
- `--length`: The length of the generated text (number of tokens).

## Example
```bash
python generate_text.py --prompt "Once upon a time" --model "gpt-2" --length 50
```
This command will generate 50 tokens of text starting with "Once upon a time" using the GPT-2 model.

## Configuration
Adjust the configuration settings in the `config.py` file to change default parameters such as model paths and text generation settings.

