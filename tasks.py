# -*- coding: utf-8 -*-

from subprocess import run
import os
import shutil
import sys
import datetime

from invoke import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer


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
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        ("", CONFIG["port"]),
        ComplexHTTPRequestHandler)

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


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
    git("subtree", "push", "--prefix", "output", "origin", "master")
