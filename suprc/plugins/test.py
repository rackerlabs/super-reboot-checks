""" 
Example super reboot checks module
"""

PLUGIN_INFO = {
    'name': 'test_plugin', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

def _run(facts):
    print "Ran the test module"
    print "Gathering data"
    print "The Cameron is " + facts.cameron
    print "The operating system is %s" % facts.distro.name
