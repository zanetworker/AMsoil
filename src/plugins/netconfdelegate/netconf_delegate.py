import amsoil.core.pluginmanager as pm
from amsoil.core import serviceinterface



class NETCONF_Delegate(object):
    def __init__(self):
        self.rm = pm.getService('netconfrm')


    def list_interfaces(self):
        #return self.rm.get_config()
        return self.rm.list_capabilities()