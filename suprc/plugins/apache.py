""" 
Apache configuration check
"""

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
    print "Ran the apache module"
    print "First item in ps output is: " 
    print facts.processes[0]
    log.debug("Testing Apache")
