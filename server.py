from peerstore import peerstore_pb2_grpc as pstore_grpc
from peerstore import peerstore_pb2 as pstore_pb2

import grpc
import time

from concurrent import futures
from loguru import logger

class Peerstore(pstore_grpc.PeerstoreServicer):

    def __init__(self):
        logger.info('init peerstore servicer')
        self.peers = {}

    def Subscribe(self, request, context):
        logger.info('subscribe {}', str(request))
        self.peers[request.peer.publickey] = request.peer
        response = pstore_pb2.SubscribeResponse()
        return response

    def Unsubscribe(self, request, context):
        logger.info('unsubscribe {}', str(request))
        response = pstore_pb2.UnsubscribeResponse()
        return response
    
    def GetPeers(self, request, context):
        logger.info('getpeers {}', str(request))
        response = pstore_pb2.GetPeersResponse(peers=self.peers.values())
        return response

def main():
    address = "[::]:8888"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = Peerstore()
    pstore_grpc.add_PeerstoreServicer_to_server(servicer, server)
    server.add_insecure_port(address)
    server.start()
    logger.info('peerstore server {} ...', address)
    server.wait_for_termination()

if __name__ == '__main__':
    main()
