# Helper

import subprocess
from logger import log

def run_command(command, fail_ok=False,
                sort=False, stdout=False, shell=False):
    try:
        command_proc = subprocess.Popen(
            command, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=shell)
    except OSError, e:
        if not fail_ok:
            log.error("Error running %s: %s" % (command[0], e.strerror))
            return None
        else:
            return None

    output = command_proc.stdout.readlines()
    returncode = command_proc.wait()

    if not fail_ok and returncode != 0:
        log.error("%s failed\nPlease troubleshoot manually" % (' '.join(command), ))
        return None

    if len(output) == 0:
        return True

    if sort:
        output.sort()

    return output

# Credit https://www.electricmonk.nl/docs/dependency_resolving_algorithm/dependency_resolving_algorithm.html
def order_dependencies(datasources):
    class Node:
        def __init__(self, datasource):
            self.edges = []
            self.datasource = datasource

        def addEdge(self, node):
            self.edges.append(node)

    def _dep_resolve(node, resolved, unresolved):
        unresolved.append(node)
        for edge in node.edges:
            if edge not in resolved:
                if edge in unresolved:
                    raise Exception('Circular reference detected: %s <-> %s' % (node.datasource.PLUGIN_INFO["name"], edge.datasource.PLUGIN_INFO["name"]))
                _dep_resolve(edge, resolved, unresolved)
        resolved.append(node)
        unresolved.remove(node)

    def _build_provides(node, provides):
        this_datasource_provides = {}
        for string in node.datasource.provides():
            log.debug("Datasource '%s' provides: %s" % (node.datasource.PLUGIN_INFO['name'], string))
            if string not in provides:
                this_datasource_provides[string] = node
            else:
                log.debug("Duplicate fact detected.  Datasource '%s' provides %s which is already provided by datasource %s. Not loading datasource %s" %
                    (node.datasource.PLUGIN_INFO['name'],
                    string,
                    provides.get(string).datasource.PLUGIN_INFO['name'],
                    node.datasource.PLUGIN_INFO['name']))
                return {}
        return this_datasource_provides 

    nodes = []
    provides = {}

    for datasource in datasources:
        node = Node(datasource)
        a = _build_provides(node, provides)
        if a:
            provides.update(a)
            nodes.append(node)

    for node in nodes[:]:
        try:
            log.debug("Datasource '%s' requires: %s" % (node.datasource.PLUGIN_INFO["name"], node.datasource.requires()))
            [node.addEdge(provides[dependency]) for dependency in node.datasource.requires()]
        except KeyError as e:
            log.debug("Could not find dependency for datasource %s. Skipping loading this datasource." % node.datasource.PLUGIN_INFO['name'])
            nodes.remove(node)

    resolved = []
    for node in nodes:
        if node in resolved:
            continue
        else:
            try:
                _dep_resolve(node, resolved, [])
            except Exception as e:
                print e
                sys.exit(0)
    order = []
    for node in resolved:
        order.append(node.datasource)
    log.debug("Building facts using datasources in this order: %s" % order)
    return order
