PLUGIN_INFO = {
    'name': 'c', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

def gather_c(facts):
    return

def provides():
    return (['c'])

def requires():
    return (['e'])
