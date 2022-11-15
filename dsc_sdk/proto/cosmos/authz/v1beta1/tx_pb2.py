# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/tx.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/authz/v1beta1/tx.proto',
  package='cosmos.authz.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\030com.cosmos.authz.v1beta1B\007TxProtoP\001Z$github.com/cosmos/cosmos-sdk/x/authz\242\002\003CAX\252\002\024Cosmos.Authz.V1beta1\312\002\024Cosmos\\Authz\\V1beta1\342\002 Cosmos\\Authz\\V1beta1\\GPBMetadata\352\002\026Cosmos::Authz::V1beta1\310\341\036\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x63osmos/authz/v1beta1/tx.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a cosmos/authz/v1beta1/authz.proto\"w\n\x08MsgGrant\x12\x18\n\x07granter\x18\x01 \x01(\tR\x07granter\x12\x18\n\x07grantee\x18\x02 \x01(\tR\x07grantee\x12\x37\n\x05grant\x18\x03 \x01(\x0b\x32\x1b.cosmos.authz.v1beta1.GrantB\x04\xc8\xde\x1f\x00R\x05grant\"+\n\x0fMsgExecResponse\x12\x18\n\x07results\x18\x01 \x03(\x0cR\x07results\"o\n\x07MsgExec\x12\x18\n\x07grantee\x18\x01 \x01(\tR\x07grantee\x12J\n\x04msgs\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB \xca\xb4-\x1csdk.Msg, authz.AuthorizationR\x04msgs\"\x12\n\x10MsgGrantResponse\"a\n\tMsgRevoke\x12\x18\n\x07granter\x18\x01 \x01(\tR\x07granter\x12\x18\n\x07grantee\x18\x02 \x01(\tR\x07grantee\x12 \n\x0cmsg_type_url\x18\x03 \x01(\tR\nmsgTypeUrl\"\x13\n\x11MsgRevokeResponse2\xf8\x01\n\x03Msg\x12O\n\x05Grant\x12\x1e.cosmos.authz.v1beta1.MsgGrant\x1a&.cosmos.authz.v1beta1.MsgGrantResponse\x12L\n\x04\x45xec\x12\x1d.cosmos.authz.v1beta1.MsgExec\x1a%.cosmos.authz.v1beta1.MsgExecResponse\x12R\n\x06Revoke\x12\x1f.cosmos.authz.v1beta1.MsgRevoke\x1a\'.cosmos.authz.v1beta1.MsgRevokeResponseB\xbf\x01\n\x18\x63om.cosmos.authz.v1beta1B\x07TxProtoP\x01Z$github.com/cosmos/cosmos-sdk/x/authz\xa2\x02\x03\x43\x41X\xaa\x02\x14\x43osmos.Authz.V1beta1\xca\x02\x14\x43osmos\\Authz\\V1beta1\xe2\x02 Cosmos\\Authz\\V1beta1\\GPBMetadata\xea\x02\x16\x43osmos::Authz::V1beta1\xc8\xe1\x1e\x00\x62\x06proto3'
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos_dot_authz_dot_v1beta1_dot_authz__pb2.DESCRIPTOR,])




_MSGGRANT = _descriptor.Descriptor(
  name='MsgGrant',
  full_name='cosmos.authz.v1beta1.MsgGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.authz.v1beta1.MsgGrant.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='granter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgGrant.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='grantee', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grant', full_name='cosmos.authz.v1beta1.MsgGrant.grant', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='grant', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=165,
  serialized_end=284,
)


_MSGEXECRESPONSE = _descriptor.Descriptor(
  name='MsgExecResponse',
  full_name='cosmos.authz.v1beta1.MsgExecResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='cosmos.authz.v1beta1.MsgExecResponse.results', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=286,
  serialized_end=329,
)


_MSGEXEC = _descriptor.Descriptor(
  name='MsgExec',
  full_name='cosmos.authz.v1beta1.MsgExec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgExec.grantee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='grantee', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgs', full_name='cosmos.authz.v1beta1.MsgExec.msgs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\034sdk.Msg, authz.Authorization', json_name='msgs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=331,
  serialized_end=442,
)


_MSGGRANTRESPONSE = _descriptor.Descriptor(
  name='MsgGrantResponse',
  full_name='cosmos.authz.v1beta1.MsgGrantResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=444,
  serialized_end=462,
)


_MSGREVOKE = _descriptor.Descriptor(
  name='MsgRevoke',
  full_name='cosmos.authz.v1beta1.MsgRevoke',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.authz.v1beta1.MsgRevoke.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='granter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.MsgRevoke.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='grantee', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_type_url', full_name='cosmos.authz.v1beta1.MsgRevoke.msg_type_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msgTypeUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=464,
  serialized_end=561,
)


_MSGREVOKERESPONSE = _descriptor.Descriptor(
  name='MsgRevokeResponse',
  full_name='cosmos.authz.v1beta1.MsgRevokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=563,
  serialized_end=582,
)

_MSGGRANT.fields_by_name['grant'].message_type = cosmos_dot_authz_dot_v1beta1_dot_authz__pb2._GRANT
_MSGEXEC.fields_by_name['msgs'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['MsgGrant'] = _MSGGRANT
DESCRIPTOR.message_types_by_name['MsgExecResponse'] = _MSGEXECRESPONSE
DESCRIPTOR.message_types_by_name['MsgExec'] = _MSGEXEC
DESCRIPTOR.message_types_by_name['MsgGrantResponse'] = _MSGGRANTRESPONSE
DESCRIPTOR.message_types_by_name['MsgRevoke'] = _MSGREVOKE
DESCRIPTOR.message_types_by_name['MsgRevokeResponse'] = _MSGREVOKERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgGrant = _reflection.GeneratedProtocolMessageType('MsgGrant', (_message.Message,), {
  'DESCRIPTOR' : _MSGGRANT,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgGrant)
  })
_sym_db.RegisterMessage(MsgGrant)

MsgExecResponse = _reflection.GeneratedProtocolMessageType('MsgExecResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGEXECRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgExecResponse)
  })
_sym_db.RegisterMessage(MsgExecResponse)

MsgExec = _reflection.GeneratedProtocolMessageType('MsgExec', (_message.Message,), {
  'DESCRIPTOR' : _MSGEXEC,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgExec)
  })
_sym_db.RegisterMessage(MsgExec)

MsgGrantResponse = _reflection.GeneratedProtocolMessageType('MsgGrantResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGGRANTRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgGrantResponse)
  })
_sym_db.RegisterMessage(MsgGrantResponse)

MsgRevoke = _reflection.GeneratedProtocolMessageType('MsgRevoke', (_message.Message,), {
  'DESCRIPTOR' : _MSGREVOKE,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgRevoke)
  })
_sym_db.RegisterMessage(MsgRevoke)

MsgRevokeResponse = _reflection.GeneratedProtocolMessageType('MsgRevokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREVOKERESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.MsgRevokeResponse)
  })
_sym_db.RegisterMessage(MsgRevokeResponse)


DESCRIPTOR._options = None
_MSGGRANT.fields_by_name['grant']._options = None
_MSGEXEC.fields_by_name['msgs']._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.authz.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=585,
  serialized_end=833,
  methods=[
  _descriptor.MethodDescriptor(
    name='Grant',
    full_name='cosmos.authz.v1beta1.Msg.Grant',
    index=0,
    containing_service=None,
    input_type=_MSGGRANT,
    output_type=_MSGGRANTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Exec',
    full_name='cosmos.authz.v1beta1.Msg.Exec',
    index=1,
    containing_service=None,
    input_type=_MSGEXEC,
    output_type=_MSGEXECRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Revoke',
    full_name='cosmos.authz.v1beta1.Msg.Revoke',
    index=2,
    containing_service=None,
    input_type=_MSGREVOKE,
    output_type=_MSGREVOKERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
