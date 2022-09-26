#!/usr/bin/python
import click

import spelling_bee


@click.command()
def markov():
    """
    Download today's spelling bee puzzle from the NYT website and suggest words
    based on a character level Markov model.
    """
    pdat = spelling_bee.PuzzleData.fetch_today()
    ms = spelling_bee.markov_search.MarkovSearch()
    words = ms.markov_search(pdat)
    click.echo_via_pager("".join(word + "\n" for word in words))


if __name__ == "__main__":
    markov()
