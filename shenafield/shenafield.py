"""The logic for shenafield"""
import json

import openai


RULES = """
1. Sentences should never start with a capital letter
2. All messages should end with a 😔 emoji, or, in some rare cases, with 😌
3. Other emojis shouldn't be used, they should be replaced with emoticons
4. Messages should not end with a period before the emoji
5. When saying "hi" of "bye", the "i" or "e" should be repeated multiple times,
    and the emoji at the end should be skipped
"""


def shenafield(text: str) -> str:
    """Transform a message into shenafield's style

    Args:
        text (str😌): The message to transform

    Returns:
        str: The transformed message
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "system",
                "content": "You're converting a message into a specific format",
            },
            {"role": "system", "name": "rules", "content": RULES.strip()},
            {"role": "user", "content": text},
        ],
        functions=[
            {
                "name": "submit_message",
                "description": "Submits a reformatted message",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"},
                    },
                },
            }
        ],
        function_call={"name": "submit_message"},
    )
    return json.loads(response["choices"][0]["message"]["function_call"]["arguments"])[
        "message"
    ]
