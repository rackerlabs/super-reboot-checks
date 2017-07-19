import modules
from facts import Facts
from logger import init_logging, log
from helper import order_dependencies
import sys


def main():
    if not sys.version_info >= (2, 7):
        print 'Super reboot checks requires Python version 2.7'
        sys.exit(1)

    init_logging(10)
    log.pError("Testing perror")
    log.pWarning("Testing pwarning")
    log.pInfo("Testing pinfo")

    # Load all of our datasources. This will also validate that all required
    # properties are present.
    datasources = modules.load_modules('datasources')

    # Order the datasources to make sure their dependencies are satisfied.
    datasource_load_ordered = order_dependencies(datasources)

    # Build our facts object using all of our loaded datasources
    facts = Facts(datasource_load_ordered)

    # Run modules which will consume the data from our datasources
    modules.run_modules(modules.load_modules('plugins'), facts)

if __name__ == '__main__':
    main()
