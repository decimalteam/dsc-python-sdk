# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/feemarket/v1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ethermint.feemarket.v1 import feemarket_pb2 as ethermint_dot_feemarket_dot_v1_dot_feemarket__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethermint/feemarket/v1/genesis.proto',
  package='ethermint.feemarket.v1',
  syntax='proto3',
  serialized_options=b'\n\032com.ethermint.feemarket.v1B\014GenesisProtoP\001Z,github.com/evmos/ethermint/x/feemarket/types\242\002\003EFX\252\002\026Ethermint.Feemarket.V1\312\002\026Ethermint\\Feemarket\\V1\342\002\"Ethermint\\Feemarket\\V1\\GPBMetadata\352\002\030Ethermint::Feemarket::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$ethermint/feemarket/v1/genesis.proto\x12\x16\x65thermint.feemarket.v1\x1a\x14gogoproto/gogo.proto\x1a&ethermint/feemarket/v1/feemarket.proto\"y\n\x0cGenesisState\x12<\n\x06params\x18\x01 \x01(\x0b\x32\x1e.ethermint.feemarket.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12\x1b\n\tblock_gas\x18\x03 \x01(\x04R\x08\x62lockGasJ\x04\x08\x02\x10\x03R\x08\x62\x61se_feeB\xd2\x01\n\x1a\x63om.ethermint.feemarket.v1B\x0cGenesisProtoP\x01Z,github.com/evmos/ethermint/x/feemarket/types\xa2\x02\x03\x45\x46X\xaa\x02\x16\x45thermint.Feemarket.V1\xca\x02\x16\x45thermint\\Feemarket\\V1\xe2\x02\"Ethermint\\Feemarket\\V1\\GPBMetadata\xea\x02\x18\x45thermint::Feemarket::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,ethermint_dot_feemarket_dot_v1_dot_feemarket__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='ethermint.feemarket.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='ethermint.feemarket.v1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_gas', full_name='ethermint.feemarket.v1.GenesisState.block_gas', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='blockGas', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=126,
  serialized_end=247,
)

_GENESISSTATE.fields_by_name['params'].message_type = ethermint_dot_feemarket_dot_v1_dot_feemarket__pb2._PARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'ethermint.feemarket.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ethermint.feemarket.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['params']._options = None
# @@protoc_insertion_point(module_scope)
