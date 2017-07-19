PLUGIN_INFO = {
    'name': 'f', # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module', # Required
    'maintainer': 'Joe Bloggs', # Required
    'description': 'Optional longer text with description - as of yet unimplemented', # Optional
    'version': '1.0', # Required
    'short_arg': '-E', # Optional
}

def gather_f(facts):
    return

def provides():
    return (['f'])

def requires():
    return (['a'])
