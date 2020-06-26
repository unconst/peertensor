from peerstore import peerstore_pb2
from peerstore import peerstore_pb2_grpc
import grpc
from loguru import logger
import argparse

def main(hparams):
    
    # Build stub.
    address = hparams.address
    channel = grpc.insecure_channel(address)
    stub = peerstore_pb2_grpc.PeerstoreStub(channel)
    logger.info('Connect to {}', address)

    # Create peer info.
    info = peerstore_pb2.PeerInfo(
            version=1.0,
            publickey='abcdefghijk',
            address='192.0.0.0',
            port='12345'
    )

    # subscribe.
    logger.info('subscribe')
    request = peerstore_pb2.SubscribeRequest(version=1.0, peer=info)
    response = stub.Subscribe(request)
    logger.info('{}', str(response))

    # getpeers
    logger.info('get peers')
    request = peerstore_pb2.GetPeersRequest(version=1.0)
    response = stub.GetPeers(request)
    logger.info('{}', str(response))

    # unsubscribe
    logger.info('unsubscribe')
    request = peerstore_pb2.UnsubscribeRequest(version=1.0)
    response = stub.Unsubscribe(request)
    logger.info('{}', str(response))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Server parameters.
    parser.add_argument(
        '--address',
        default='localhost:8888',
        type=str,
        help="server address. Default address=localhost:8888")

    hparams = parser.parse_args()
    main(hparams)


