"""The cli for interacting with shenafield"""
import os
import sys

import click
from dotenv import load_dotenv
import openai
import openai.error

from .shenafield import shenafield

load_dotenv()


@click.group()
def cli():
    """A library that replicates how shenafield talks"""


@cli.command()
@click.argument("message", type=str)
@click.option(
    "--api-key", "-a", type=str, help="The OpenAI api key to use", default=None
)
def transform(message: str, api_key: str | None = None) -> None:
    """Transform a message into shenafield's style"""
    if api_key is not None:
        openai.api_key = api_key
    elif "OPENAI_API_KEY" in os.environ:
        openai.api_key = os.environ["OPENAI_API_KEY"]

    try:
        click.echo(shenafield(message))
    except openai.error.AuthenticationError:
        click.echo(
            "Invalid api key. Make sure to provide the correct one. "
            "You can do so by either using the --api-key parameter "
            "or the OPENAI_API_KEY environment variable (or in .env).",
            err=True,
        )
        sys.exit(1)
    except openai.error.OpenAIError as error:
        click.echo(error, err=True)
        sys.exit(1)


@cli.command()
@click.option(
    "--api-key", "-a", type=str, help="The OpenAI api key to use", default=None
)
def shell(api_key: str | None = None) -> None:
    """Interactively transform multiple messages into shenafield's style"""
    if api_key is not None:
        openai.api_key = api_key
    elif "OPENAI_API_KEY" in os.environ:
        openai.api_key = os.environ["OPENAI_API_KEY"]

    try:
        while True:
            message = click.prompt("Message")
            click.echo(shenafield(message))
    except openai.error.AuthenticationError:
        click.echo(
            "Invalid api key. Make sure to provide the correct one. "
            "You can do so by either using the --api-key parameter "
            "or the OPENAI_API_KEY environment variable (or in .env).",
            err=True,
        )
        sys.exit(1)
    except openai.error.OpenAIError as error:
        click.echo(error, err=True)
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        click.echo()
        sys.exit(0)


if __name__ == "__main__":
    cli()
