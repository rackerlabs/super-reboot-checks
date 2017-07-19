# Class to return data

from helper import run_command as run_command

PLUGIN_INFO = {
    'name': 'packages',  # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Test/example module',  # Required
    'maintainer': 'Joe Bloggs',  # Required
    'description': 'Optional longer text with description - as of yet unimplemented',  # Optional
    'version': '1.0',  # Required
    'short_arg': '-E',  # Optional
}


def gather_packages(facts):
    if facts.distro.name in ('redhat', 'centos', 'fedora'):
#        packages = run_command(['rpm', '-qa'])
        packages = "testing_packages_list"
    elif facts.distro.name in ('ubuntu', 'debian'):
 #       packages = run_command(['dpkg-query' '-f' '${binary:Package}\n' '-W'])
        packages = "testing packages list"
    else:
        raise Exception
    return packages


def gather_cameron(facts):
    return "Cameron"


def provides():
    return (['packages', 'cameron'])


def requires():
    return (['distro'])
