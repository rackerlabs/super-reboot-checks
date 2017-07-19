from logger import log


class Facts:
    def __init__(self, datasources):
        self.build(datasources)

    def set(self, fact_name, value):
        #log.debug("FACTS: setting name %s to %s" % (fact_name, value))
        if not self.get(fact_name):
            setattr(self, fact_name, value)
        else:
            log.debug("FACTS: The fact %s has already been set to %s. Skipping"
                      % (fact_name, value))

    def get(self, keyword):
        try:
            return getattr(self, keyword)
        except AttributeError:
            return False

    def build(self, datasources):
        for datasource in datasources:
            for method in datasource.provides():
                run = getattr(datasource, "gather_%s" % method)
                self.set(method, run(self))
