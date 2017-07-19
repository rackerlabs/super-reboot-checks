# Class to return data

from helper import run_command as run_command

PLUGIN_INFO = {
    'name': 'distro', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

class Distro():
    def __init__(self):
        self.name = "redhat"
        self.version = 6

def gather_distro(facts):
    return Distro()

def gather_cameron(facts):
    return "Cameron"

def provides():
    return (['distro'])

def requires():
    return ([])
