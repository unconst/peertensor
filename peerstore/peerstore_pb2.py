# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peerstore/peerstore.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='peerstore/peerstore.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x19peerstore/peerstore.proto\"<\n\x10SubscribeRequest\x12\x0f\n\x07version\x18\x01 \x01(\x02\x12\x17\n\x04peer\x18\x02 \x01(\x0b\x32\t.PeerInfo\"$\n\x11SubscribeResponse\x12\x0f\n\x07version\x18\x01 \x01(\x02\"%\n\x12UnsubscribeRequest\x12\x0f\n\x07version\x18\x01 \x01(\x02\"&\n\x13UnsubscribeResponse\x12\x0f\n\x07version\x18\x01 \x01(\x02\"\"\n\x0fGetPeersRequest\x12\x0f\n\x07version\x18\x01 \x01(\x02\"=\n\x10GetPeersResponse\x12\x0f\n\x07version\x18\x01 \x01(\x02\x12\x18\n\x05peers\x18\x02 \x03(\x0b\x32\t.PeerInfo\"M\n\x08PeerInfo\x12\x0f\n\x07version\x18\x01 \x01(\x02\x12\x11\n\tpublickey\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\t2\xb0\x01\n\tPeerstore\x12\x34\n\tSubscribe\x12\x11.SubscribeRequest\x1a\x12.SubscribeResponse\"\x00\x12:\n\x0bUnsubscribe\x12\x13.UnsubscribeRequest\x1a\x14.UnsubscribeResponse\"\x00\x12\x31\n\x08GetPeers\x12\x10.GetPeersRequest\x1a\x11.GetPeersResponse\"\x00\x62\x06proto3'
)




_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='SubscribeRequest.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer', full_name='SubscribeRequest.peer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=89,
)


_SUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='SubscribeResponse',
  full_name='SubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='SubscribeResponse.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=127,
)


_UNSUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='UnsubscribeRequest',
  full_name='UnsubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='UnsubscribeRequest.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=166,
)


_UNSUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='UnsubscribeResponse',
  full_name='UnsubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='UnsubscribeResponse.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=206,
)


_GETPEERSREQUEST = _descriptor.Descriptor(
  name='GetPeersRequest',
  full_name='GetPeersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='GetPeersRequest.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=242,
)


_GETPEERSRESPONSE = _descriptor.Descriptor(
  name='GetPeersResponse',
  full_name='GetPeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='GetPeersResponse.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peers', full_name='GetPeersResponse.peers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=305,
)


_PEERINFO = _descriptor.Descriptor(
  name='PeerInfo',
  full_name='PeerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='PeerInfo.version', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publickey', full_name='PeerInfo.publickey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='PeerInfo.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='PeerInfo.port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=384,
)

_SUBSCRIBEREQUEST.fields_by_name['peer'].message_type = _PEERINFO
_GETPEERSRESPONSE.fields_by_name['peers'].message_type = _PEERINFO
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeResponse'] = _SUBSCRIBERESPONSE
DESCRIPTOR.message_types_by_name['UnsubscribeRequest'] = _UNSUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['UnsubscribeResponse'] = _UNSUBSCRIBERESPONSE
DESCRIPTOR.message_types_by_name['GetPeersRequest'] = _GETPEERSREQUEST
DESCRIPTOR.message_types_by_name['GetPeersResponse'] = _GETPEERSRESPONSE
DESCRIPTOR.message_types_by_name['PeerInfo'] = _PEERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType('SubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERESPONSE,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:SubscribeResponse)
  })
_sym_db.RegisterMessage(SubscribeResponse)

UnsubscribeRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNSUBSCRIBEREQUEST,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:UnsubscribeRequest)
  })
_sym_db.RegisterMessage(UnsubscribeRequest)

UnsubscribeResponse = _reflection.GeneratedProtocolMessageType('UnsubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNSUBSCRIBERESPONSE,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:UnsubscribeResponse)
  })
_sym_db.RegisterMessage(UnsubscribeResponse)

GetPeersRequest = _reflection.GeneratedProtocolMessageType('GetPeersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPEERSREQUEST,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:GetPeersRequest)
  })
_sym_db.RegisterMessage(GetPeersRequest)

GetPeersResponse = _reflection.GeneratedProtocolMessageType('GetPeersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPEERSRESPONSE,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:GetPeersResponse)
  })
_sym_db.RegisterMessage(GetPeersResponse)

PeerInfo = _reflection.GeneratedProtocolMessageType('PeerInfo', (_message.Message,), {
  'DESCRIPTOR' : _PEERINFO,
  '__module__' : 'peerstore.peerstore_pb2'
  # @@protoc_insertion_point(class_scope:PeerInfo)
  })
_sym_db.RegisterMessage(PeerInfo)



_PEERSTORE = _descriptor.ServiceDescriptor(
  name='Peerstore',
  full_name='Peerstore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=387,
  serialized_end=563,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='Peerstore.Subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIBERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Unsubscribe',
    full_name='Peerstore.Unsubscribe',
    index=1,
    containing_service=None,
    input_type=_UNSUBSCRIBEREQUEST,
    output_type=_UNSUBSCRIBERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPeers',
    full_name='Peerstore.GetPeers',
    index=2,
    containing_service=None,
    input_type=_GETPEERSREQUEST,
    output_type=_GETPEERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PEERSTORE)

DESCRIPTOR.services_by_name['Peerstore'] = _PEERSTORE

# @@protoc_insertion_point(module_scope)
