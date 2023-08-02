# shenafield

shenafield is a Python library that replicates the unique typing style of shenafield. This library allows users to transform their text into the distinctive style in which shenafield talks.

## Installation

To install shenafield, you can use `pipx` by running the following command:

```bash
pipx install shenafield
```

Note: shenafield requires an OpenAI API key to function properly. Please make sure you have obtained an API key from [OpenAI](https://platform.openai.com/account/api-keys) and set it as the `OPENAI_API_KEY` environment variable or in a `.env` file. Alternatively, you can pass your API key through the `--api-key` option.

## Usage

To transform a message into the shenafield style, use the following command:

```bash
shenafield transform [message]
```

Replace `[message]` with the text you want to convert. The result will be printed to the console.

Alternatively, you can launch the interactive shell by running:

```bash
shenafield shell
```

The interactive shell allows you to input multiple messages, and shenafield will transform each one into the unique typing style.
