#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
"""
Script to deploy a static website
"""


def do_pack():
    """
    Pack file into a .tgz archive
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}".format(date)
    local("mkdir -p versions")
    new = local("tar -czvf {} web_static".format(filename))
    if new.succeeded:
        return(filename)
    else:
        return(None)
