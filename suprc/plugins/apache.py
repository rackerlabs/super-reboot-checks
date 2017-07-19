"""
Apache configuration check
"""

from helper import run_command
from logger import log


PLUGIN_INFO = {
    'name': 'apache', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Check Apache syntx', # Required
    'maintainer': 'Piers Cornwell', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '', # Optional
}

def _run(facts):
    log.pDebug("Running Apache plugin")

    if 'httpd' in facts.processes:
        run_command(['httpd', '-S'])
    else:
        log.pDebug("Apache not in running processes list")
