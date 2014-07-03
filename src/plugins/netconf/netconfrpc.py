import amsoil.core.pluginmanager as pm
from amsoil.core import serviceinterface

from amsoil.config import (netconfrpc_server_ip, netconfrpc_server_port)
from SocketServer import ThreadingMixIn
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class NETCONF_Handler(object):
    def __init__(self):
        self._delegate = None

    @serviceinterface
    def setDelegate(self, adelegate):
        """
        Set this object's delegate.
        """
        self._delegate = adelegate

    @serviceinterface
    def getDelegate(self):
        """
        Get this object's delegate.
        """
        return self._delegate

    @serviceinterface
    def list_interfaces(self):
        return self._delegate.list_interfaces()


