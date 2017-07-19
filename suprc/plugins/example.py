""" 
Example super reboot checks module
"""

from helper import run_command
from logger import log


PLUGIN_INFO = {
    'name': 'example_plugin', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

def _run(facts):
    log.pInfo("Ran the example module. This uses the \"processes\" datasource.")
    log.pInfo("Example of getting data from sources - number of running processes: %s" % len(facts.processes))
    log.pError("Example of an error message")
    log.pWarning("Example of a warning message")
    log.pDebug("Example of a debug message")

    # Example of running a shell command
    o = run_command([ "uname", "-r" ])
    log.pInfo("Example command output - kernel version is: %s" % o[0])
