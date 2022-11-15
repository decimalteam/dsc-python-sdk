# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/fee/v1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from decimal.fee.v1 import fee_pb2 as decimal_dot_fee_dot_v1_dot_fee__pb2
from decimal.fee.v1 import params_pb2 as decimal_dot_fee_dot_v1_dot_params__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/fee/v1/genesis.proto',
  package='decimal.fee.v1',
  syntax='proto3',
  serialized_options=b'\n\022com.decimal.fee.v1B\014GenesisProtoP\001Z3bitbucket.org/decimalteam/go-smart-node/x/fee/types\242\002\003DFX\252\002\016Decimal.Fee.V1\312\002\016Decimal\\Fee\\V1\342\002\032Decimal\\Fee\\V1\\GPBMetadata\352\002\020Decimal::Fee::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x64\x65\x63imal/fee/v1/genesis.proto\x12\x0e\x64\x65\x63imal.fee.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x18\x64\x65\x63imal/fee/v1/fee.proto\x1a\x1b\x64\x65\x63imal/fee/v1/params.proto\"}\n\x0cGenesisState\x12\x37\n\x06prices\x18\x01 \x03(\x0b\x32\x19.decimal.fee.v1.CoinPriceB\x04\xc8\xde\x1f\x00R\x06prices\x12\x34\n\x06params\x18\x02 \x01(\x0b\x32\x16.decimal.fee.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06paramsB\xb1\x01\n\x12\x63om.decimal.fee.v1B\x0cGenesisProtoP\x01Z3bitbucket.org/decimalteam/go-smart-node/x/fee/types\xa2\x02\x03\x44\x46X\xaa\x02\x0e\x44\x65\x63imal.Fee.V1\xca\x02\x0e\x44\x65\x63imal\\Fee\\V1\xe2\x02\x1a\x44\x65\x63imal\\Fee\\V1\\GPBMetadata\xea\x02\x10\x44\x65\x63imal::Fee::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,decimal_dot_fee_dot_v1_dot_fee__pb2.DESCRIPTOR,decimal_dot_fee_dot_v1_dot_params__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='decimal.fee.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prices', full_name='decimal.fee.v1.GenesisState.prices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='prices', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='decimal.fee.v1.GenesisState.params', index=1,
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
  serialized_start=152,
  serialized_end=277,
)

_GENESISSTATE.fields_by_name['prices'].message_type = decimal_dot_fee_dot_v1_dot_fee__pb2._COINPRICE
_GENESISSTATE.fields_by_name['params'].message_type = decimal_dot_fee_dot_v1_dot_params__pb2._PARAMS
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'decimal.fee.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:decimal.fee.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['prices']._options = None
_GENESISSTATE.fields_by_name['params']._options = None
# @@protoc_insertion_point(module_scope)
