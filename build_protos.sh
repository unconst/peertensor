# Build protos.
	python3 -m grpc.tools.protoc peerstore/peerstore.proto  -I. --python_out=. --grpc_python_out=.
