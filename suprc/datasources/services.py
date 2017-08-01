# Class to return data

from helper import run_command as run_command

PLUGIN_INFO = {
    'name': 'services',  # May only contain ascii letters and single, non-leading dashes (eg. not --test)
    'short_description': 'Gather process list',  # Required
    'maintainer': 'Piers Cornwell',  # Required
    'description': 'Optional longer text with description - as of yet unimplemented',  # Optional
    'version': '1.0',  # Required
    'short_arg': '',  # Optional
}


def gather_starts_in_runlevel(facts):
    # Produce a dict containing the list of sysv services that start on each runlevel

    output = run_command(['chkconfig', '--list'])

    sysvservices = {}

    # Convert output to dict with key on service
    for i in output:
        il = i.split("0:off")
        sysvservices[il[0].strip()] = il[1].strip()

    starts_in_runlevel = {"runlevel2": [], "runlevel3": [], "runlevel4": [], "runlevel5": []}

    for i in sysvservices:
        if '2:on' in sysvservices[i]:
             starts_in_runlevel['runlevel2'].append(i)
        if '3:on' in sysvservices[i]:
             starts_in_runlevel['runlevel3'].append(i)
        if '4:on' in sysvservices[i]:
             starts_in_runlevel['runlevel4'].append(i)
        if '5:on' in sysvservices[i]:
             starts_in_runlevel['runlevel5'].append(i)

    return starts_in_runlevel


def provides():
    return (['starts_in_runlevel'])


def requires():
    return ([])
