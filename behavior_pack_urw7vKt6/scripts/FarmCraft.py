from mod.common.mod import  Mod
import mod.server.extraMasterApi;
import mod.server.extraMasterApi
@Mod.Binding("FarmCraft","0.1 alpha")
class FarmCraft(object):
    def __init__(self):
        pass
    @Mod.InitServer
    def serverInit(self):
        print "Initing Server"
        pass;
    @Mod.InitClient
    def clientInit(self):
        print "Initing Client"
    pass;


