# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/legacy/v1/legacy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/legacy/v1/legacy.proto',
  package='decimal.legacy.v1',
  syntax='proto3',
  serialized_options=b'\n\025com.decimal.legacy.v1B\013LegacyProtoP\001Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\242\002\003DLX\252\002\021Decimal.Legacy.V1\312\002\021Decimal\\Legacy\\V1\342\002\035Decimal\\Legacy\\V1\\GPBMetadata\352\002\023Decimal::Legacy::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x64\x65\x63imal/legacy/v1/legacy.proto\x12\x11\x64\x65\x63imal.legacy.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x92\x02\n\x06Record\x12?\n\x0elegacy_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\rlegacyAddress\x12\x61\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x05\x63oins\x12\x18\n\x07wallets\x18\x03 \x03(\tR\x07wallets\x12\x1c\n\x04nfts\x18\x04 \x03(\tB\x08\xe2\xde\x1f\x04NFTsR\x04nfts\x12\x1e\n\nvalidators\x18\x05 \x03(\tR\nvalidators:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\x42\xc2\x01\n\x15\x63om.decimal.legacy.v1B\x0bLegacyProtoP\x01Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\xa2\x02\x03\x44LX\xaa\x02\x11\x44\x65\x63imal.Legacy.V1\xca\x02\x11\x44\x65\x63imal\\Legacy\\V1\xe2\x02\x1d\x44\x65\x63imal\\Legacy\\V1\\GPBMetadata\xea\x02\x13\x44\x65\x63imal::Legacy::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='decimal.legacy.v1.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_address', full_name='decimal.legacy.v1.Record.legacy_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coins', full_name='decimal.legacy.v1.Record.coins', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', json_name='coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wallets', full_name='decimal.legacy.v1.Record.wallets', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='wallets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nfts', full_name='decimal.legacy.v1.Record.nfts', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\004NFTs', json_name='nfts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validators', full_name='decimal.legacy.v1.Record.validators', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validators', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\001\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=409,
)

_RECORD.fields_by_name['coins'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'decimal.legacy.v1.legacy_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.Record)
  })
_sym_db.RegisterMessage(Record)


DESCRIPTOR._options = None
_RECORD.fields_by_name['legacy_address']._options = None
_RECORD.fields_by_name['coins']._options = None
_RECORD.fields_by_name['nfts']._options = None
_RECORD._options = None
# @@protoc_insertion_point(module_scope)