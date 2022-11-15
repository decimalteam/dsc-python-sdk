# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/legacy/v1/events.proto

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
  name='decimal/legacy/v1/events.proto',
  package='decimal.legacy.v1',
  syntax='proto3',
  serialized_options=b'\n\025com.decimal.legacy.v1B\013EventsProtoP\001Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\242\002\003DLX\252\002\021Decimal.Legacy.V1\312\002\021Decimal\\Legacy\\V1\342\002\035Decimal\\Legacy\\V1\\GPBMetadata\352\002\023Decimal::Legacy::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x64\x65\x63imal/legacy/v1/events.proto\x12\x11\x64\x65\x63imal.legacy.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xe8\x01\n\x16\x45ventReturnLegacyCoins\x12;\n\x0clegacy_owner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0blegacyOwner\x12.\n\x05owner\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05owner\x12\x61\n\x05\x63oins\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x05\x63oins\"\xeb\x01\n\x19\x45ventReturnLegacySubToken\x12;\n\x0clegacy_owner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0blegacyOwner\x12.\n\x05owner\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05owner\x12\x14\n\x05\x64\x65nom\x18\x03 \x01(\tR\x05\x64\x65nom\x12\x16\n\x02id\x18\x04 \x01(\tB\x06\xe2\xde\x1f\x02IDR\x02id\x12\x33\n\rsub_token_ids\x18\x05 \x03(\rB\x0f\xe2\xde\x1f\x0bSubTokenIDsR\x0bsubTokenIds\"\xba\x01\n\x19\x45ventReturnMultisigWallet\x12;\n\x0clegacy_owner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0blegacyOwner\x12.\n\x05owner\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05owner\x12\x30\n\x06wallet\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06wallet\"\xbb\x01\n\x14\x45ventReturnValidator\x12;\n\x0clegacy_owner\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0blegacyOwner\x12.\n\x05owner\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05owner\x12\x36\n\tvalidator\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tvalidatorB\xc2\x01\n\x15\x63om.decimal.legacy.v1B\x0b\x45ventsProtoP\x01Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\xa2\x02\x03\x44LX\xaa\x02\x11\x44\x65\x63imal.Legacy.V1\xca\x02\x11\x44\x65\x63imal\\Legacy\\V1\xe2\x02\x1d\x44\x65\x63imal\\Legacy\\V1\\GPBMetadata\xea\x02\x13\x44\x65\x63imal::Legacy::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_EVENTRETURNLEGACYCOINS = _descriptor.Descriptor(
  name='EventReturnLegacyCoins',
  full_name='decimal.legacy.v1.EventReturnLegacyCoins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_owner', full_name='decimal.legacy.v1.EventReturnLegacyCoins.legacy_owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyOwner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='decimal.legacy.v1.EventReturnLegacyCoins.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coins', full_name='decimal.legacy.v1.EventReturnLegacyCoins.coins', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', json_name='coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=135,
  serialized_end=367,
)


_EVENTRETURNLEGACYSUBTOKEN = _descriptor.Descriptor(
  name='EventReturnLegacySubToken',
  full_name='decimal.legacy.v1.EventReturnLegacySubToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_owner', full_name='decimal.legacy.v1.EventReturnLegacySubToken.legacy_owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyOwner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='decimal.legacy.v1.EventReturnLegacySubToken.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.legacy.v1.EventReturnLegacySubToken.denom', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='decimal.legacy.v1.EventReturnLegacySubToken.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\002ID', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_token_ids', full_name='decimal.legacy.v1.EventReturnLegacySubToken.sub_token_ids', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\013SubTokenIDs', json_name='subTokenIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=370,
  serialized_end=605,
)


_EVENTRETURNMULTISIGWALLET = _descriptor.Descriptor(
  name='EventReturnMultisigWallet',
  full_name='decimal.legacy.v1.EventReturnMultisigWallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_owner', full_name='decimal.legacy.v1.EventReturnMultisigWallet.legacy_owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyOwner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='decimal.legacy.v1.EventReturnMultisigWallet.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wallet', full_name='decimal.legacy.v1.EventReturnMultisigWallet.wallet', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='wallet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=608,
  serialized_end=794,
)


_EVENTRETURNVALIDATOR = _descriptor.Descriptor(
  name='EventReturnValidator',
  full_name='decimal.legacy.v1.EventReturnValidator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_owner', full_name='decimal.legacy.v1.EventReturnValidator.legacy_owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyOwner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='decimal.legacy.v1.EventReturnValidator.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='owner', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator', full_name='decimal.legacy.v1.EventReturnValidator.validator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='validator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=797,
  serialized_end=984,
)

_EVENTRETURNLEGACYCOINS.fields_by_name['coins'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['EventReturnLegacyCoins'] = _EVENTRETURNLEGACYCOINS
DESCRIPTOR.message_types_by_name['EventReturnLegacySubToken'] = _EVENTRETURNLEGACYSUBTOKEN
DESCRIPTOR.message_types_by_name['EventReturnMultisigWallet'] = _EVENTRETURNMULTISIGWALLET
DESCRIPTOR.message_types_by_name['EventReturnValidator'] = _EVENTRETURNVALIDATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventReturnLegacyCoins = _reflection.GeneratedProtocolMessageType('EventReturnLegacyCoins', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRETURNLEGACYCOINS,
  '__module__' : 'decimal.legacy.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.EventReturnLegacyCoins)
  })
_sym_db.RegisterMessage(EventReturnLegacyCoins)

EventReturnLegacySubToken = _reflection.GeneratedProtocolMessageType('EventReturnLegacySubToken', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRETURNLEGACYSUBTOKEN,
  '__module__' : 'decimal.legacy.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.EventReturnLegacySubToken)
  })
_sym_db.RegisterMessage(EventReturnLegacySubToken)

EventReturnMultisigWallet = _reflection.GeneratedProtocolMessageType('EventReturnMultisigWallet', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRETURNMULTISIGWALLET,
  '__module__' : 'decimal.legacy.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.EventReturnMultisigWallet)
  })
_sym_db.RegisterMessage(EventReturnMultisigWallet)

EventReturnValidator = _reflection.GeneratedProtocolMessageType('EventReturnValidator', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRETURNVALIDATOR,
  '__module__' : 'decimal.legacy.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.EventReturnValidator)
  })
_sym_db.RegisterMessage(EventReturnValidator)


DESCRIPTOR._options = None
_EVENTRETURNLEGACYCOINS.fields_by_name['legacy_owner']._options = None
_EVENTRETURNLEGACYCOINS.fields_by_name['owner']._options = None
_EVENTRETURNLEGACYCOINS.fields_by_name['coins']._options = None
_EVENTRETURNLEGACYSUBTOKEN.fields_by_name['legacy_owner']._options = None
_EVENTRETURNLEGACYSUBTOKEN.fields_by_name['owner']._options = None
_EVENTRETURNLEGACYSUBTOKEN.fields_by_name['id']._options = None
_EVENTRETURNLEGACYSUBTOKEN.fields_by_name['sub_token_ids']._options = None
_EVENTRETURNMULTISIGWALLET.fields_by_name['legacy_owner']._options = None
_EVENTRETURNMULTISIGWALLET.fields_by_name['owner']._options = None
_EVENTRETURNMULTISIGWALLET.fields_by_name['wallet']._options = None
_EVENTRETURNVALIDATOR.fields_by_name['legacy_owner']._options = None
_EVENTRETURNVALIDATOR.fields_by_name['owner']._options = None
_EVENTRETURNVALIDATOR.fields_by_name['validator']._options = None
# @@protoc_insertion_point(module_scope)