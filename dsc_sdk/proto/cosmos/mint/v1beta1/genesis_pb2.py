# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.mint.v1beta1 import mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/mint/v1beta1/genesis.proto',
  package='cosmos.mint.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\027com.cosmos.mint.v1beta1B\014GenesisProtoP\001Z)github.com/cosmos/cosmos-sdk/x/mint/types\242\002\003CMX\252\002\023Cosmos.Mint.V1beta1\312\002\023Cosmos\\Mint\\V1beta1\342\002\037Cosmos\\Mint\\V1beta1\\GPBMetadata\352\002\025Cosmos::Mint::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!cosmos/mint/v1beta1/genesis.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/mint/v1beta1/mint.proto\"\x84\x01\n\x0cGenesisState\x12\x39\n\x06minter\x18\x01 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.MinterB\x04\xc8\xde\x1f\x00R\x06minter\x12\x39\n\x06params\x18\x02 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06paramsB\xc0\x01\n\x17\x63om.cosmos.mint.v1beta1B\x0cGenesisProtoP\x01Z)github.com/cosmos/cosmos-sdk/x/mint/types\xa2\x02\x03\x43MX\xaa\x02\x13\x43osmos.Mint.V1beta1\xca\x02\x13\x43osmos\\Mint\\V1beta1\xe2\x02\x1f\x43osmos\\Mint\\V1beta1\\GPBMetadata\xea\x02\x15\x43osmos::Mint::V1beta1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_mint_dot_v1beta1_dot_mint__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.mint.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='minter', full_name='cosmos.mint.v1beta1.GenesisState.minter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='minter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.mint.v1beta1.GenesisState.params', index=1,
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
  serialized_start=113,
  serialized_end=245,
)

_GENESISSTATE.fields_by_name['minter'].message_type = cosmos_dot_mint_dot_v1beta1_dot_mint__pb2._MINTER
_GENESISSTATE.fields_by_name['params'].message_type = cosmos_dot_mint_dot_v1beta1_dot_mint__pb2._PARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.mint.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['minter']._options = None
_GENESISSTATE.fields_by_name['params']._options = None
# @@protoc_insertion_point(module_scope)
