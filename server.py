from peerstore import peerstore_pb2_grpc as pstore_grpc
from peerstore import peerstore_pb2 as pstore_pb2

import argparse
import grpc
import time

from concurrent import futures
from datetime import timedelta
from loguru import logger
from timeloop import Timeloop

class Peerstore(pstore_grpc.PeerstoreServicer):

    def __init__(self, config):
        logger.info('init peerstore servicer')
        self.config = config
        self.peers = {}
        self.last_subscribe = {}

    def clean(self):
        logger.info('removing stale entries ')
        num_deleted = 0
        for key, value in enumerate(self.peers):
            last = self.last_subscribe[key]
            now = time.time()
            if (now - last) > self.config.time_to_live:
                num_deleted += 1 
                del self.peers[key]
                del self.last_subscribe[key]
        logger.info('deleted {} entries', num_deleted)

    def Subscribe(self, request, context):
        logger.info('subscribe {}', str(request))
        self.peers[request.peer.publickey] = request.peer
        self.last_subscribe[request.peer.publickey] = time.time()
        response = pstore_pb2.SubscribeResponse()
        return response

    def Unsubscribe(self, request, context):
        logger.info('unsubscribe {}', str(request))
        del self.peers[request.peer.publickey]
        del self.last_subscribe[request.peer.publickey]
        response = pstore_pb2.UnsubscribeResponse()
        return response
    
    def GetPeers(self, request, context):
        logger.info('getpeers {}', str(request))
        response = pstore_pb2.GetPeersResponse(peers=self.peers.values())
        return response

def set_timed_loops(tl, config, server):

    @tl.job(interval=timedelta(seconds=config.wait_clean))
    def clean():
        server.clean()

def main(config):
    address = "[::]:8888"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peerstore = Peerstore(config)
    pstore_grpc.add_PeerstoreServicer_to_server(peerstore, server)
    server.add_insecure_port(address)
    
    tl = Timeloop()
    set_timed_loops(tl, config, peerstore)
    tl.start(block=False)
    logger.info('started timers')

    server.start()
    logger.info('peerstore server {} ...', address)
    server.wait_for_termination()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--wait_clean',
        default=100,
        type=int,
        help="Time between stale entry cleaning. Default=100")
    hparams = parser.parse_args()
    main(hparams)

