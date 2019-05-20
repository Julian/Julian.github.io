# -*- coding: utf-8 -*-

from pathlib import Path
from subprocess import run

from invoke import task


OUTPUT_DIR = Path(__file__).parent / "output"


def git(*args):
    return run(["git"] + list(args))


def pelican(*args):
    return run(["pelican"] + list(args))


@task
def develop(context):
    """Build local version of the site."""
    pelican("--delete-output-directory", "--settings", "pelicanconf.py")


@task
def regenerate(context):
    """Automatically regenerate site upon file modification"""
    context.run("pelican -r -s pelicanconf.py")


@task
def serve(context):
    """Serve the site."""
    run(["twist", "web", "--path", str(OUTPUT_DIR)])


@task
def reserve(context):
    """`develop`, then `serve`"""
    develop(context)
    serve(context)


@task
def build(context):
    """Build production version of the site."""
    pelican("--delete-output-directory", "--settings", "publishconf.py")


@task
def publish(context):
    """Publish to GitHub Pages"""
    git("commit", "-m", "Regenerate output.")
    git("subtree", "push", "--prefix", OUTPUT_DIR.name, "origin", "master")
