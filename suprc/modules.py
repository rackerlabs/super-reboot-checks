import sys
import os
import string
from logger import log

def get_modules_27(module_files, mod_type):
    import imp
    modules = []
    for module_file in module_files:
    # Uncomment the nice error handling here for live
        try:
            mod = imp.load_source(module_file['name'], module_file['path'])
        except Exception as ex:
            log.debug("Error loading module at {0}: {1}".format(module_file['path'], str(ex)))
            continue
        if validate_module(mod, mod_type, module_file['path']):
            log.debug("Loaded module %s" % mod.PLUGIN_INFO['name'])
            modules.append(mod)

    return modules

def validate_module(module, mod_type, path):
    """ This is where we check that the attributes of the module are set correctly """

    required_keys = ['name', 'short_description', 'version', 'maintainer']
    try:
        for k in required_keys:
            module.PLUGIN_INFO[k]
    except KeyError as ex:
        log.debug("Plugin at {0} is invalid. {1} key missing from PLUGIN_INFO".format(path, ex))
        return False

    name = module.PLUGIN_INFO['name']
    allowed_chars = string.ascii_letters + '-' + '_'
    for char in name:
        if char not in allowed_chars:
            log.debug("Plugin name {0} is invalid. Plugin names may only contain ascii letters, underscores and unrepeated dashes".format(name))
            return False

    # Datasource / plugin specific checks go here
    if mod_type == "datasources":
        # First check that we list what each datasource requires, and what it provides
        required_methods = ["provides", "requires"]
        for method in required_methods:
            if not hasattr(module, method):
                log.debug("Datasource %s has failed to provide the required method %s(). Skipping loading of this datasource." % (module.PLUGIN_INFO['name'], method))
                return False

        # Next, lets make sure that it has a gather_ method for each thing it provides
        required_methods = []
        for method in module.provides():
            if not hasattr(module, "gather_%s" % method):
                log.debug("Datasource %s has failed to provide the required method gather_%s(). Skipping loading this datasource." % (module.PLUGIN_INFO['name'], method))
                return False
        return True

    elif mod_type == "plugins":
        # still to write
        return True
    else:
        return True

def get_files(module_dirs):
    modules = []
    module_names = []
    for module_dir in module_dirs:
        try:
            module_files = [f for f in os.listdir(module_dir) if is_module(f, module_dir)]
        except OSError as ex:
            log.debug("Error scanning directory {0}: {1}".format(module_dir, str(ex)))
            continue

        for module_file in module_files:
            full_path = os.path.join(module_dir, module_file)
            name = os.path.splitext(module_file)[0]
            if name in module_names:
                log.critical("Plugin with file name {0} already loaded. Please rename {1}.".format(
                    name, full_path))
                raise HtExit(1)
            else:
                module_names.append(name)
            module = {
                'path': full_path,
                'name': name
            }
            modules.append(module)

    return modules

def is_module(file_name, module_dir):
    full_path = os.path.join(module_dir, file_name)
    return os.path.isfile(full_path) and file_name.endswith('.py') and file_name != '__init__.py'

def get_default_module_dirs(path):
    default_module_dirs = []
    module_dir = os.path.dirname(os.path.abspath(__file__))
    default_module_dirs.append(os.path.join(module_dir, path))

    return default_module_dirs

def handle_error(plugin, error=None):
    log.critical("An error occurred during the execution of plugin '{name}'".format(**plugin.PLUGIN_INFO))
    log.critical("Error is: %s" % error)

def load_modules(mod_type):
    """ Entrypoint."""

    module_dirs = get_default_module_dirs(mod_type)
    modules = []
    module_files = get_files(module_dirs)

    if sys.version_info >= (2, 7):
        modules = get_modules_27(module_files, mod_type)
    else:
        log.critical("Super Reboot Checks is not supported on python != 2.7")

    return modules

def run_modules(mymodules, facts):
    for module in mymodules:
        try:
            module._run(facts)
        except Exception as ex:
            handle_error(module, error=ex)
