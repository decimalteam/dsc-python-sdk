# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/nft/v1/nft.proto

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
  name='decimal/nft/v1/nft.proto',
  package='decimal.nft.v1',
  syntax='proto3',
  serialized_options=b'\n\022com.decimal.nft.v1B\010NftProtoP\001Z3bitbucket.org/decimalteam/go-smart-node/x/nft/types\242\002\003DNX\252\002\016Decimal.Nft.V1\312\002\016Decimal\\Nft\\V1\342\002\032Decimal\\Nft\\V1\\GPBMetadata\352\002\020Decimal::Nft::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x64\x65\x63imal/nft/v1/nft.proto\x12\x0e\x64\x65\x63imal.nft.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xb7\x01\n\nCollection\x12\x32\n\x07\x63reator\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x63reator\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06supply\x18\x03 \x01(\rR\x06supply\x12\x39\n\x06tokens\x18\x04 \x03(\x0b\x32\x15.decimal.nft.v1.TokenB\n\xaa\xdf\x1f\x06TokensR\x06tokens:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\"9\n\x11\x43ollectionCounter\x12\x16\n\x06supply\x18\x01 \x01(\rR\x06supply:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\"\xe2\x02\n\x05Token\x12\x32\n\x07\x63reator\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x63reator\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12\x16\n\x02id\x18\x03 \x01(\tB\x06\xe2\xde\x1f\x02IDR\x02id\x12\x19\n\x03uri\x18\x04 \x01(\tB\x07\xe2\xde\x1f\x03URIR\x03uri\x12\x39\n\x07reserve\x18\x05 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x07reserve\x12\x1d\n\nallow_mint\x18\x06 \x01(\x08R\tallowMint\x12\x16\n\x06minted\x18\x07 \x01(\rR\x06minted\x12\x14\n\x05\x62urnt\x18\x08 \x01(\rR\x05\x62urnt\x12\x46\n\nsub_tokens\x18\t \x03(\x0b\x32\x18.decimal.nft.v1.SubTokenB\r\xaa\xdf\x1f\tSubTokensR\tsubTokens:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\"J\n\x0cTokenCounter\x12\x16\n\x06minted\x18\x01 \x01(\rR\x06minted\x12\x14\n\x05\x62urnt\x18\x02 \x01(\rR\x05\x62urnt:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\"\x95\x01\n\x08SubToken\x12\x16\n\x02id\x18\x01 \x01(\rB\x06\xe2\xde\x1f\x02IDR\x02id\x12.\n\x05owner\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05owner\x12\x33\n\x07reserve\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07reserve:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\x42\xad\x01\n\x12\x63om.decimal.nft.v1B\x08NftProtoP\x01Z3bitbucket.org/decimalteam/go-smart-node/x/nft/types\xa2\x02\x03\x44NX\xaa\x02\x0e\x44\x65\x63imal.Nft.V1\xca\x02\x0e\x44\x65\x63imal\\Nft\\V1\xe2\x02\x1a\x44\x65\x63imal\\Nft\\V1\\GPBMetadata\xea\x02\x10\x44\x65\x63imal::Nft::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_COLLECTION = _descriptor.Descriptor(
  name='Collection',
  full_name='decimal.nft.v1.Collection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='decimal.nft.v1.Collection.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='creator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.nft.v1.Collection.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supply', full_name='decimal.nft.v1.Collection.supply', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='supply', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='decimal.nft.v1.Collection.tokens', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\006Tokens', json_name='tokens', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=126,
  serialized_end=309,
)


_COLLECTIONCOUNTER = _descriptor.Descriptor(
  name='CollectionCounter',
  full_name='decimal.nft.v1.CollectionCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supply', full_name='decimal.nft.v1.CollectionCounter.supply', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='supply', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=311,
  serialized_end=368,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='decimal.nft.v1.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='decimal.nft.v1.Token.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='creator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.nft.v1.Token.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='decimal.nft.v1.Token.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='decimal.nft.v1.Token.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\003URI', json_name='uri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='decimal.nft.v1.Token.reserve', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='reserve', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_mint', full_name='decimal.nft.v1.Token.allow_mint', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='allowMint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minted', full_name='decimal.nft.v1.Token.minted', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='minted', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='burnt', full_name='decimal.nft.v1.Token.burnt', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='burnt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_tokens', full_name='decimal.nft.v1.Token.sub_tokens', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\tSubTokens', json_name='subTokens', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=371,
  serialized_end=725,
)


_TOKENCOUNTER = _descriptor.Descriptor(
  name='TokenCounter',
  full_name='decimal.nft.v1.TokenCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='minted', full_name='decimal.nft.v1.TokenCounter.minted', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='minted', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='burnt', full_name='decimal.nft.v1.TokenCounter.burnt', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='burnt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=727,
  serialized_end=801,
)


_SUBTOKEN = _descriptor.Descriptor(
  name='SubToken',
  full_name='decimal.nft.v1.SubToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='decimal.nft.v1.SubToken.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='decimal.nft.v1.SubToken.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='decimal.nft.v1.SubToken.reserve', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='reserve', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=804,
  serialized_end=953,
)

_COLLECTION.fields_by_name['tokens'].message_type = _TOKEN
_TOKEN.fields_by_name['reserve'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_TOKEN.fields_by_name['sub_tokens'].message_type = _SUBTOKEN
_SUBTOKEN.fields_by_name['reserve'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['Collection'] = _COLLECTION
DESCRIPTOR.message_types_by_name['CollectionCounter'] = _COLLECTIONCOUNTER
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['TokenCounter'] = _TOKENCOUNTER
DESCRIPTOR.message_types_by_name['SubToken'] = _SUBTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Collection = _reflection.GeneratedProtocolMessageType('Collection', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTION,
  '__module__' : 'decimal.nft.v1.nft_pb2'
  # @@protoc_insertion_point(class_scope:decimal.nft.v1.Collection)
  })
_sym_db.RegisterMessage(Collection)

CollectionCounter = _reflection.GeneratedProtocolMessageType('CollectionCounter', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONCOUNTER,
  '__module__' : 'decimal.nft.v1.nft_pb2'
  # @@protoc_insertion_point(class_scope:decimal.nft.v1.CollectionCounter)
  })
_sym_db.RegisterMessage(CollectionCounter)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'decimal.nft.v1.nft_pb2'
  # @@protoc_insertion_point(class_scope:decimal.nft.v1.Token)
  })
_sym_db.RegisterMessage(Token)

TokenCounter = _reflection.GeneratedProtocolMessageType('TokenCounter', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCOUNTER,
  '__module__' : 'decimal.nft.v1.nft_pb2'
  # @@protoc_insertion_point(class_scope:decimal.nft.v1.TokenCounter)
  })
_sym_db.RegisterMessage(TokenCounter)

SubToken = _reflection.GeneratedProtocolMessageType('SubToken', (_message.Message,), {
  'DESCRIPTOR' : _SUBTOKEN,
  '__module__' : 'decimal.nft.v1.nft_pb2'
  # @@protoc_insertion_point(class_scope:decimal.nft.v1.SubToken)
  })
_sym_db.RegisterMessage(SubToken)


DESCRIPTOR._options = None
_COLLECTION.fields_by_name['creator']._options = None
_COLLECTION.fields_by_name['tokens']._options = None
_COLLECTION._options = None
_COLLECTIONCOUNTER._options = None
_TOKEN.fields_by_name['creator']._options = None
_TOKEN.fields_by_name['id']._options = None
_TOKEN.fields_by_name['uri']._options = None
_TOKEN.fields_by_name['reserve']._options = None
_TOKEN.fields_by_name['sub_tokens']._options = None
_TOKEN._options = None
_TOKENCOUNTER._options = None
_SUBTOKEN.fields_by_name['id']._options = None
_SUBTOKEN.fields_by_name['owner']._options = None
_SUBTOKEN._options = None
# @@protoc_insertion_point(module_scope)
