# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/genesis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/staking/v1beta1/genesis.proto',
  package='cosmos.staking.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\032com.cosmos.staking.v1beta1B\014GenesisProtoP\001Z,github.com/cosmos/cosmos-sdk/x/staking/types\242\002\003CSX\252\002\026Cosmos.Staking.V1beta1\312\002\026Cosmos\\Staking\\V1beta1\342\002\"Cosmos\\Staking\\V1beta1\\GPBMetadata\352\002\030Cosmos::Staking::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$cosmos/staking/v1beta1/genesis.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$cosmos/staking/v1beta1/staking.proto\"\xd4\x05\n\x0cGenesisState\x12<\n\x06params\x18\x01 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\x12s\n\x10last_total_power\x18\x02 \x01(\x0c\x42I\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:\"last_total_power\"R\x0elastTotalPower\x12\x84\x01\n\x15last_validator_powers\x18\x03 \x03(\x0b\x32*.cosmos.staking.v1beta1.LastValidatorPowerB$\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:\"last_validator_powers\"R\x13lastValidatorPowers\x12G\n\nvalidators\x18\x04 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00R\nvalidators\x12J\n\x0b\x64\x65legations\x18\x05 \x03(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00R\x0b\x64\x65legations\x12\x86\x01\n\x15unbonding_delegations\x18\x06 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB$\xc8\xde\x1f\x00\xf2\xde\x1f\x1cyaml:\"unbonding_delegations\"R\x14unbondingDelegations\x12P\n\rredelegations\x18\x07 \x03(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00R\rredelegations\x12\x1a\n\x08\x65xported\x18\x08 \x01(\x08R\x08\x65xported\"N\n\x12LastValidatorPower\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05power\x18\x02 \x01(\x03R\x05power:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x42\xd2\x01\n\x1a\x63om.cosmos.staking.v1beta1B\x0cGenesisProtoP\x01Z,github.com/cosmos/cosmos-sdk/x/staking/types\xa2\x02\x03\x43SX\xaa\x02\x16\x43osmos.Staking.V1beta1\xca\x02\x16\x43osmos\\Staking\\V1beta1\xe2\x02\"Cosmos\\Staking\\V1beta1\\GPBMetadata\xea\x02\x18\x43osmos::Staking::V1beta1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_staking_dot_v1beta1_dot_staking__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.staking.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.staking.v1beta1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_total_power', full_name='cosmos.staking.v1beta1.GenesisState.last_total_power', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\027yaml:\"last_total_power\"', json_name='lastTotalPower', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_validator_powers', full_name='cosmos.staking.v1beta1.GenesisState.last_validator_powers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\034yaml:\"last_validator_powers\"', json_name='lastValidatorPowers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validators', full_name='cosmos.staking.v1beta1.GenesisState.validators', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='validators', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegations', full_name='cosmos.staking.v1beta1.GenesisState.delegations', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='delegations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unbonding_delegations', full_name='cosmos.staking.v1beta1.GenesisState.unbonding_delegations', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\034yaml:\"unbonding_delegations\"', json_name='unbondingDelegations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redelegations', full_name='cosmos.staking.v1beta1.GenesisState.redelegations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='redelegations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exported', full_name='cosmos.staking.v1beta1.GenesisState.exported', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exported', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=125,
  serialized_end=849,
)


_LASTVALIDATORPOWER = _descriptor.Descriptor(
  name='LastValidatorPower',
  full_name='cosmos.staking.v1beta1.LastValidatorPower',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.staking.v1beta1.LastValidatorPower.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='power', full_name='cosmos.staking.v1beta1.LastValidatorPower.power', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='power', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=929,
)

_GENESISSTATE.fields_by_name['params'].message_type = cosmos_dot_staking_dot_v1beta1_dot_staking__pb2._PARAMS
_GENESISSTATE.fields_by_name['last_validator_powers'].message_type = _LASTVALIDATORPOWER
_GENESISSTATE.fields_by_name['validators'].message_type = cosmos_dot_staking_dot_v1beta1_dot_staking__pb2._VALIDATOR
_GENESISSTATE.fields_by_name['delegations'].message_type = cosmos_dot_staking_dot_v1beta1_dot_staking__pb2._DELEGATION
_GENESISSTATE.fields_by_name['unbonding_delegations'].message_type = cosmos_dot_staking_dot_v1beta1_dot_staking__pb2._UNBONDINGDELEGATION
_GENESISSTATE.fields_by_name['redelegations'].message_type = cosmos_dot_staking_dot_v1beta1_dot_staking__pb2._REDELEGATION
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
DESCRIPTOR.message_types_by_name['LastValidatorPower'] = _LASTVALIDATORPOWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.staking.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

LastValidatorPower = _reflection.GeneratedProtocolMessageType('LastValidatorPower', (_message.Message,), {
  'DESCRIPTOR' : _LASTVALIDATORPOWER,
  '__module__' : 'cosmos.staking.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.LastValidatorPower)
  })
_sym_db.RegisterMessage(LastValidatorPower)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['params']._options = None
_GENESISSTATE.fields_by_name['last_total_power']._options = None
_GENESISSTATE.fields_by_name['last_validator_powers']._options = None
_GENESISSTATE.fields_by_name['validators']._options = None
_GENESISSTATE.fields_by_name['delegations']._options = None
_GENESISSTATE.fields_by_name['unbonding_delegations']._options = None
_GENESISSTATE.fields_by_name['redelegations']._options = None
_LASTVALIDATORPOWER._options = None
# @@protoc_insertion_point(module_scope)