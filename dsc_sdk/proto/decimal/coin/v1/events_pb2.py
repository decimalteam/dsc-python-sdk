# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/coin/v1/events.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/coin/v1/events.proto',
  package='decimal.coin.v1',
  syntax='proto3',
  serialized_options=b'\n\023com.decimal.coin.v1B\013EventsProtoP\001Z4bitbucket.org/decimalteam/go-smart-node/x/coin/types\242\002\003DCX\252\002\017Decimal.Coin.V1\312\002\017Decimal\\Coin\\V1\342\002\033Decimal\\Coin\\V1\\GPBMetadata\352\002\021Decimal::Coin::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x64\x65\x63imal/coin/v1/events.proto\x12\x0f\x64\x65\x63imal.coin.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xcf\x02\n\x0f\x45ventCreateCoin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\x12\x19\n\x03\x63rr\x18\x04 \x01(\rB\x07\xe2\xde\x1f\x03\x43RRR\x03\x63rr\x12%\n\x0einitial_volume\x18\x05 \x01(\tR\rinitialVolume\x12\'\n\x0finitial_reserve\x18\x06 \x01(\tR\x0einitialReserve\x12!\n\x0climit_volume\x18\x07 \x01(\tR\x0blimitVolume\x12\x1a\n\x08identity\x18\x08 \x01(\tR\x08identity\x12\x34\n\x16\x63ommission_create_coin\x18\t \x01(\tR\x14\x63ommissionCreateCoin\"\x98\x01\n\x0f\x45ventUpdateCoin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom\x12!\n\x0climit_volume\x18\x03 \x01(\tR\x0blimitVolume\x12\x1a\n\x08identity\x18\x04 \x01(\tR\x08identity\"[\n\x11\x45ventUpdateCoinVR\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06volume\x18\x02 \x01(\tR\x06volume\x12\x18\n\x07reserve\x18\x03 \x01(\tR\x07reserve\"\x8d\x01\n\rEventSendCoin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x36\n\trecipient\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\trecipient\x12\x12\n\x04\x63oin\x18\x03 \x01(\tR\x04\x63oin\"\xb5\x01\n\x10\x45ventBuySellCoin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x1e\n\x0b\x63oin_to_buy\x18\x02 \x01(\tR\tcoinToBuy\x12 \n\x0c\x63oin_to_sell\x18\x03 \x01(\tR\ncoinToSell\x12-\n\x13\x61mount_in_base_coin\x18\x04 \x01(\tR\x10\x61mountInBaseCoin\"U\n\rEventBurnCoin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x12\n\x04\x63oin\x18\x02 \x01(\tR\x04\x63oin\"\xf5\x01\n\x10\x45ventRedeemCheck\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x30\n\x06issuer\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06issuer\x12\x12\n\x04\x63oin\x18\x03 \x01(\tR\x04\x63oin\x12\x14\n\x05nonce\x18\x04 \x01(\tR\x05nonce\x12\x1b\n\tdue_block\x18\x05 \x01(\tR\x08\x64ueBlock\x12\x36\n\x17\x63ommission_redeem_check\x18\x06 \x01(\tR\x15\x63ommissionRedeemCheckB\xb6\x01\n\x13\x63om.decimal.coin.v1B\x0b\x45ventsProtoP\x01Z4bitbucket.org/decimalteam/go-smart-node/x/coin/types\xa2\x02\x03\x44\x43X\xaa\x02\x0f\x44\x65\x63imal.Coin.V1\xca\x02\x0f\x44\x65\x63imal\\Coin\\V1\xe2\x02\x1b\x44\x65\x63imal\\Coin\\V1\\GPBMetadata\xea\x02\x11\x44\x65\x63imal::Coin::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_EVENTCREATECOIN = _descriptor.Descriptor(
  name='EventCreateCoin',
  full_name='decimal.coin.v1.EventCreateCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventCreateCoin.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.coin.v1.EventCreateCoin.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='decimal.coin.v1.EventCreateCoin.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='title', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crr', full_name='decimal.coin.v1.EventCreateCoin.crr', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\003CRR', json_name='crr', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_volume', full_name='decimal.coin.v1.EventCreateCoin.initial_volume', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='initialVolume', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_reserve', full_name='decimal.coin.v1.EventCreateCoin.initial_reserve', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='initialReserve', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit_volume', full_name='decimal.coin.v1.EventCreateCoin.limit_volume', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='limitVolume', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identity', full_name='decimal.coin.v1.EventCreateCoin.identity', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='identity', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commission_create_coin', full_name='decimal.coin.v1.EventCreateCoin.commission_create_coin', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commissionCreateCoin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=99,
  serialized_end=434,
)


_EVENTUPDATECOIN = _descriptor.Descriptor(
  name='EventUpdateCoin',
  full_name='decimal.coin.v1.EventUpdateCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventUpdateCoin.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.coin.v1.EventUpdateCoin.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit_volume', full_name='decimal.coin.v1.EventUpdateCoin.limit_volume', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='limitVolume', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identity', full_name='decimal.coin.v1.EventUpdateCoin.identity', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='identity', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=437,
  serialized_end=589,
)


_EVENTUPDATECOINVR = _descriptor.Descriptor(
  name='EventUpdateCoinVR',
  full_name='decimal.coin.v1.EventUpdateCoinVR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='decimal.coin.v1.EventUpdateCoinVR.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='decimal.coin.v1.EventUpdateCoinVR.volume', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='volume', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='decimal.coin.v1.EventUpdateCoinVR.reserve', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='reserve', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=591,
  serialized_end=682,
)


_EVENTSENDCOIN = _descriptor.Descriptor(
  name='EventSendCoin',
  full_name='decimal.coin.v1.EventSendCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventSendCoin.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='decimal.coin.v1.EventSendCoin.recipient', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='recipient', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin', full_name='decimal.coin.v1.EventSendCoin.coin', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='coin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=685,
  serialized_end=826,
)


_EVENTBUYSELLCOIN = _descriptor.Descriptor(
  name='EventBuySellCoin',
  full_name='decimal.coin.v1.EventBuySellCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventBuySellCoin.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_to_buy', full_name='decimal.coin.v1.EventBuySellCoin.coin_to_buy', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='coinToBuy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin_to_sell', full_name='decimal.coin.v1.EventBuySellCoin.coin_to_sell', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='coinToSell', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount_in_base_coin', full_name='decimal.coin.v1.EventBuySellCoin.amount_in_base_coin', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amountInBaseCoin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=829,
  serialized_end=1010,
)


_EVENTBURNCOIN = _descriptor.Descriptor(
  name='EventBurnCoin',
  full_name='decimal.coin.v1.EventBurnCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventBurnCoin.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin', full_name='decimal.coin.v1.EventBurnCoin.coin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='coin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1012,
  serialized_end=1097,
)


_EVENTREDEEMCHECK = _descriptor.Descriptor(
  name='EventRedeemCheck',
  full_name='decimal.coin.v1.EventRedeemCheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='decimal.coin.v1.EventRedeemCheck.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='sender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='decimal.coin.v1.EventRedeemCheck.issuer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='issuer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin', full_name='decimal.coin.v1.EventRedeemCheck.coin', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='coin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='decimal.coin.v1.EventRedeemCheck.nonce', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nonce', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='due_block', full_name='decimal.coin.v1.EventRedeemCheck.due_block', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dueBlock', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commission_redeem_check', full_name='decimal.coin.v1.EventRedeemCheck.commission_redeem_check', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commissionRedeemCheck', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1100,
  serialized_end=1345,
)

DESCRIPTOR.message_types_by_name['EventCreateCoin'] = _EVENTCREATECOIN
DESCRIPTOR.message_types_by_name['EventUpdateCoin'] = _EVENTUPDATECOIN
DESCRIPTOR.message_types_by_name['EventUpdateCoinVR'] = _EVENTUPDATECOINVR
DESCRIPTOR.message_types_by_name['EventSendCoin'] = _EVENTSENDCOIN
DESCRIPTOR.message_types_by_name['EventBuySellCoin'] = _EVENTBUYSELLCOIN
DESCRIPTOR.message_types_by_name['EventBurnCoin'] = _EVENTBURNCOIN
DESCRIPTOR.message_types_by_name['EventRedeemCheck'] = _EVENTREDEEMCHECK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventCreateCoin = _reflection.GeneratedProtocolMessageType('EventCreateCoin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTCREATECOIN,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventCreateCoin)
  })
_sym_db.RegisterMessage(EventCreateCoin)

EventUpdateCoin = _reflection.GeneratedProtocolMessageType('EventUpdateCoin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTUPDATECOIN,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventUpdateCoin)
  })
_sym_db.RegisterMessage(EventUpdateCoin)

EventUpdateCoinVR = _reflection.GeneratedProtocolMessageType('EventUpdateCoinVR', (_message.Message,), {
  'DESCRIPTOR' : _EVENTUPDATECOINVR,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventUpdateCoinVR)
  })
_sym_db.RegisterMessage(EventUpdateCoinVR)

EventSendCoin = _reflection.GeneratedProtocolMessageType('EventSendCoin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSENDCOIN,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventSendCoin)
  })
_sym_db.RegisterMessage(EventSendCoin)

EventBuySellCoin = _reflection.GeneratedProtocolMessageType('EventBuySellCoin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBUYSELLCOIN,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventBuySellCoin)
  })
_sym_db.RegisterMessage(EventBuySellCoin)

EventBurnCoin = _reflection.GeneratedProtocolMessageType('EventBurnCoin', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBURNCOIN,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventBurnCoin)
  })
_sym_db.RegisterMessage(EventBurnCoin)

EventRedeemCheck = _reflection.GeneratedProtocolMessageType('EventRedeemCheck', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREDEEMCHECK,
  '__module__' : 'decimal.coin.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:decimal.coin.v1.EventRedeemCheck)
  })
_sym_db.RegisterMessage(EventRedeemCheck)


DESCRIPTOR._options = None
_EVENTCREATECOIN.fields_by_name['sender']._options = None
_EVENTCREATECOIN.fields_by_name['crr']._options = None
_EVENTUPDATECOIN.fields_by_name['sender']._options = None
_EVENTSENDCOIN.fields_by_name['sender']._options = None
_EVENTSENDCOIN.fields_by_name['recipient']._options = None
_EVENTBUYSELLCOIN.fields_by_name['sender']._options = None
_EVENTBURNCOIN.fields_by_name['sender']._options = None
_EVENTREDEEMCHECK.fields_by_name['sender']._options = None
_EVENTREDEEMCHECK.fields_by_name['issuer']._options = None
# @@protoc_insertion_point(module_scope)