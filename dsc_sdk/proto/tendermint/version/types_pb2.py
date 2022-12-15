# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/version/types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tendermint/version/types.proto',
  package='tendermint.version',
  syntax='proto3',
  serialized_options=b'\n\026com.tendermint.versionB\nTypesProtoP\001Z9github.com/tendermint/tendermint/proto/tendermint/version\242\002\003TVX\252\002\022Tendermint.Version\312\002\022Tendermint\\Version\342\002\036Tendermint\\Version\\GPBMetadata\352\002\023Tendermint::Version',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1etendermint/version/types.proto\x12\x12tendermint.version\x1a\x14gogoproto/gogo.proto\"=\n\x03\x41pp\x12\x1a\n\x08protocol\x18\x01 \x01(\x04R\x08protocol\x12\x1a\n\x08software\x18\x02 \x01(\tR\x08software\"9\n\tConsensus\x12\x14\n\x05\x62lock\x18\x01 \x01(\x04R\x05\x62lock\x12\x10\n\x03\x61pp\x18\x02 \x01(\x04R\x03\x61pp:\x04\xe8\xa0\x1f\x01\x42\xc8\x01\n\x16\x63om.tendermint.versionB\nTypesProtoP\x01Z9github.com/tendermint/tendermint/proto/tendermint/version\xa2\x02\x03TVX\xaa\x02\x12Tendermint.Version\xca\x02\x12Tendermint\\Version\xe2\x02\x1eTendermint\\Version\\GPBMetadata\xea\x02\x13Tendermint::Versionb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_APP = _descriptor.Descriptor(
  name='App',
  full_name='tendermint.version.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='tendermint.version.App.protocol', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='protocol', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='software', full_name='tendermint.version.App.software', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='software', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=76,
  serialized_end=137,
)


_CONSENSUS = _descriptor.Descriptor(
  name='Consensus',
  full_name='tendermint.version.Consensus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='tendermint.version.Consensus.block', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app', full_name='tendermint.version.Consensus.app', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='app', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['App'] = _APP
DESCRIPTOR.message_types_by_name['Consensus'] = _CONSENSUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), {
  'DESCRIPTOR' : _APP,
  '__module__' : 'tendermint.version.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.version.App)
  })
_sym_db.RegisterMessage(App)

Consensus = _reflection.GeneratedProtocolMessageType('Consensus', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUS,
  '__module__' : 'tendermint.version.types_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.version.Consensus)
  })
_sym_db.RegisterMessage(Consensus)


DESCRIPTOR._options = None
_CONSENSUS._options = None
# @@protoc_insertion_point(module_scope)
