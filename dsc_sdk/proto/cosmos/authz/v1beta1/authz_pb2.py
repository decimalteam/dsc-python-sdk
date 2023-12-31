# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/authz.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/authz/v1beta1/authz.proto',
  package='cosmos.authz.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\030com.cosmos.authz.v1beta1B\nAuthzProtoP\001Z$github.com/cosmos/cosmos-sdk/x/authz\242\002\003CAX\252\002\024Cosmos.Authz.V1beta1\312\002\024Cosmos\\Authz\\V1beta1\342\002 Cosmos\\Authz\\V1beta1\\GPBMetadata\352\002\026Cosmos::Authz::V1beta1\310\341\036\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cosmos/authz/v1beta1/authz.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\";\n\x14GenericAuthorization\x12\x10\n\x03msg\x18\x01 \x01(\tR\x03msg:\x11\xca\xb4-\rAuthorization\"\x9c\x01\n\x05Grant\x12M\n\rauthorization\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rAuthorizationR\rauthorization\x12\x44\n\nexpiration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\nexpirationB\xc2\x01\n\x18\x63om.cosmos.authz.v1beta1B\nAuthzProtoP\x01Z$github.com/cosmos/cosmos-sdk/x/authz\xa2\x02\x03\x43\x41X\xaa\x02\x14\x43osmos.Authz.V1beta1\xca\x02\x14\x43osmos\\Authz\\V1beta1\xe2\x02 Cosmos\\Authz\\V1beta1\\GPBMetadata\xea\x02\x16\x43osmos::Authz::V1beta1\xc8\xe1\x1e\x00\x62\x06proto3'
  ,
  dependencies=[cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_GENERICAUTHORIZATION = _descriptor.Descriptor(
  name='GenericAuthorization',
  full_name='cosmos.authz.v1beta1.GenericAuthorization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='cosmos.authz.v1beta1.GenericAuthorization.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\312\264-\rAuthorization',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=226,
)


_GRANT = _descriptor.Descriptor(
  name='Grant',
  full_name='cosmos.authz.v1beta1.Grant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorization', full_name='cosmos.authz.v1beta1.Grant.authorization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\rAuthorization', json_name='authorization', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='cosmos.authz.v1beta1.Grant.expiration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\220\337\037\001', json_name='expiration', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=229,
  serialized_end=385,
)

_GRANT.fields_by_name['authorization'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_GRANT.fields_by_name['expiration'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['GenericAuthorization'] = _GENERICAUTHORIZATION
DESCRIPTOR.message_types_by_name['Grant'] = _GRANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericAuthorization = _reflection.GeneratedProtocolMessageType('GenericAuthorization', (_message.Message,), {
  'DESCRIPTOR' : _GENERICAUTHORIZATION,
  '__module__' : 'cosmos.authz.v1beta1.authz_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.GenericAuthorization)
  })
_sym_db.RegisterMessage(GenericAuthorization)

Grant = _reflection.GeneratedProtocolMessageType('Grant', (_message.Message,), {
  'DESCRIPTOR' : _GRANT,
  '__module__' : 'cosmos.authz.v1beta1.authz_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.Grant)
  })
_sym_db.RegisterMessage(Grant)


DESCRIPTOR._options = None
_GENERICAUTHORIZATION._options = None
_GRANT.fields_by_name['authorization']._options = None
_GRANT.fields_by_name['expiration']._options = None
# @@protoc_insertion_point(module_scope)
