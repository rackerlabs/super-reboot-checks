PLUGIN_INFO = {
    'name': 'a', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

#def gather_a(facts):
#    return

def provides():
    return (['a'])

def requires():
    return (['d', 'b'])
