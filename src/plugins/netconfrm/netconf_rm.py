from ncclient import manager

class NETCONFResourceManager(object):

    def __init__(self):
        pass


    def get_config(self, filter=None):
        with manager.connect(host='127.0.0.1', port=830, username='adel', password='zanetworker_89', hostkey_verify=False) as m:
            c = m.get_config(source='running').data_xml
            return c


    def list_capabilities (self):
        with manager.connect(host='127.0.0.1', port=830, username='adel', password='zanetworker_89', hostkey_verify=False) as m:
            for c in m.server_capabilities:
                print c

    def edit_config(self, configuration):
        pass


