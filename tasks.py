# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer


# CONFIG = {
#     # Local path configuration (can be absolute or relative to tasks.py)
#     "deploy_path": "output",
#     # Github Pages configuration
#     "github_pages_branch": "master",
#     "commit_message": "'Publish site on {}'".format(datetime.date.today().isoformat()),
# }


@task
def clean(context):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(context):
    """Build local version of site"""
    context.run("pelican -s pelicanconf.py")


@task
def rebuild(context):
    """`build` with the delete switch"""
    context.run("pelican -d -s pelicanconf.py")


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
    """`build`, then `serve`"""
    build(context)
    serve(context)


@task
def preview(context):
    """Build production version of site"""
    context.run("pelican -s publishconf.py")


@task
def gh_pages(context):
    """Publish to GitHub Pages"""
    preview(context)
    context.run(
        [
            "ghp-import",
            "-b", github_pages_branch,
            "-m", commit_message,
            deploy_path,
            "-p",
        ],
    )
