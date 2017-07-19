# Class to return data

from helper import run_command as run_command

PLUGIN_INFO = {
    'name': 'processes',  # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Gather process list',  # Required
    'maintainer': 'Piers Cornwell',  # Required
    'description': 'Optional longer text with description - as of yet unimplemented',  # Optional
    'version': '1.0',  # Required
    'short_arg': '',  # Optional
}


def gather_processes(facts):
    #processes = run_command(['ps', '-eo', 'cmd'])
    processes = ['top', 'bash', 'kthreadd']
    return processes


def provides():
    return (['processes'])


def requires():
    return ([])
