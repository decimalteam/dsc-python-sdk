# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/legacy/v1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from decimal.legacy.v1 import legacy_pb2 as decimal_dot_legacy_dot_v1_dot_legacy__pb2
from decimal.legacy.v1 import params_pb2 as decimal_dot_legacy_dot_v1_dot_params__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/legacy/v1/genesis.proto',
  package='decimal.legacy.v1',
  syntax='proto3',
  serialized_options=b'\n\025com.decimal.legacy.v1B\014GenesisProtoP\001Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\242\002\003DLX\252\002\021Decimal.Legacy.V1\312\002\021Decimal\\Legacy\\V1\342\002\035Decimal\\Legacy\\V1\\GPBMetadata\352\002\023Decimal::Legacy::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x64\x65\x63imal/legacy/v1/genesis.proto\x12\x11\x64\x65\x63imal.legacy.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x64\x65\x63imal/legacy/v1/legacy.proto\x1a\x1e\x64\x65\x63imal/legacy/v1/params.proto\"\x82\x01\n\x0cGenesisState\x12\x39\n\x07records\x18\x01 \x03(\x0b\x32\x19.decimal.legacy.v1.RecordB\x04\xc8\xde\x1f\x00R\x07records\x12\x37\n\x06params\x18\x02 \x01(\x0b\x32\x19.decimal.legacy.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06paramsB\xc3\x01\n\x15\x63om.decimal.legacy.v1B\x0cGenesisProtoP\x01Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\xa2\x02\x03\x44LX\xaa\x02\x11\x44\x65\x63imal.Legacy.V1\xca\x02\x11\x44\x65\x63imal\\Legacy\\V1\xe2\x02\x1d\x44\x65\x63imal\\Legacy\\V1\\GPBMetadata\xea\x02\x13\x44\x65\x63imal::Legacy::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,decimal_dot_legacy_dot_v1_dot_legacy__pb2.DESCRIPTOR,decimal_dot_legacy_dot_v1_dot_params__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='decimal.legacy.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='decimal.legacy.v1.GenesisState.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='records', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='decimal.legacy.v1.GenesisState.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=141,
  serialized_end=271,
)

_GENESISSTATE.fields_by_name['records'].message_type = decimal_dot_legacy_dot_v1_dot_legacy__pb2._RECORD
_GENESISSTATE.fields_by_name['params'].message_type = decimal_dot_legacy_dot_v1_dot_params__pb2._PARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'decimal.legacy.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['records']._options = None
_GENESISSTATE.fields_by_name['params']._options = None
# @@protoc_insertion_point(module_scope)