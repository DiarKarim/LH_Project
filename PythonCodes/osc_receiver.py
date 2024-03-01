from oscpy.server import OSCThreadServer
from time import sleep

osc = OSCThreadServer()
sock = osc.listen(address='127.0.0.1', port=8008, default=True)

@osc.address(b'/address')
def callback(*values):
    print("got values: {}".format(values))

sleep(1000)
osc.stop()


# from oscpy.server import OSCThreadServer

# with OSCAsyncServer(port=8008) as OSC:
#     for address, values in OSC.listen():
#        if address == b'/example':
#             print("got {} on /example".format(values))
#        else:
#             print("unknown address {}".format(address))