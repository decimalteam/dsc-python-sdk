# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/slashing.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/slashing/v1beta1/slashing.proto',
  package='cosmos.slashing.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\033com.cosmos.slashing.v1beta1B\rSlashingProtoP\001Z-github.com/cosmos/cosmos-sdk/x/slashing/types\242\002\003CSX\252\002\027Cosmos.Slashing.V1beta1\312\002\027Cosmos\\Slashing\\V1beta1\342\002#Cosmos\\Slashing\\V1beta1\\GPBMetadata\352\002\031Cosmos::Slashing::V1beta1\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&cosmos/slashing/v1beta1/slashing.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x03\n\x14ValidatorSigningInfo\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12:\n\x0cstart_height\x18\x02 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"start_height\"R\x0bstartHeight\x12:\n\x0cindex_offset\x18\x03 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"index_offset\"R\x0bindexOffset\x12^\n\x0cjailed_until\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1f\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"jailed_until\"\x90\xdf\x1f\x01R\x0bjailedUntil\x12\x1e\n\ntombstoned\x18\x05 \x01(\x08R\ntombstoned\x12T\n\x15missed_blocks_counter\x18\x06 \x01(\x03\x42 \xf2\xde\x1f\x1cyaml:\"missed_blocks_counter\"R\x13missedBlocksCounter:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"\xf9\x04\n\x06Params\x12Q\n\x14signed_blocks_window\x18\x01 \x01(\x03\x42\x1f\xf2\xde\x1f\x1byaml:\"signed_blocks_window\"R\x12signedBlocksWindow\x12\x81\x01\n\x15min_signed_per_window\x18\x02 \x01(\x0c\x42N\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1cyaml:\"min_signed_per_window\"R\x12minSignedPerWindow\x12z\n\x16\x64owntime_jail_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB)\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:\"downtime_jail_duration\"\x98\xdf\x1f\x01R\x14\x64owntimeJailDuration\x12\x90\x01\n\x1aslash_fraction_double_sign\x18\x04 \x01(\x0c\x42S\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f!yaml:\"slash_fraction_double_sign\"R\x17slashFractionDoubleSign\x12\x88\x01\n\x17slash_fraction_downtime\x18\x05 \x01(\x0c\x42P\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1eyaml:\"slash_fraction_downtime\"R\x15slashFractionDowntimeB\xdd\x01\n\x1b\x63om.cosmos.slashing.v1beta1B\rSlashingProtoP\x01Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa2\x02\x03\x43SX\xaa\x02\x17\x43osmos.Slashing.V1beta1\xca\x02\x17\x43osmos\\Slashing\\V1beta1\xe2\x02#Cosmos\\Slashing\\V1beta1\\GPBMetadata\xea\x02\x19\x43osmos::Slashing::V1beta1\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VALIDATORSIGNINGINFO = _descriptor.Descriptor(
  name='ValidatorSigningInfo',
  full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_height', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.start_height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"start_height\"', json_name='startHeight', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_offset', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.index_offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"index_offset\"', json_name='indexOffset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jailed_until', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.jailed_until', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\023yaml:\"jailed_until\"\220\337\037\001', json_name='jailedUntil', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tombstoned', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.tombstoned', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tombstoned', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missed_blocks_counter', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.missed_blocks_counter', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"missed_blocks_counter\"', json_name='missedBlocksCounter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=547,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.slashing.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_blocks_window', full_name='cosmos.slashing.v1beta1.Params.signed_blocks_window', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"signed_blocks_window\"', json_name='signedBlocksWindow', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_signed_per_window', full_name='cosmos.slashing.v1beta1.Params.min_signed_per_window', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\034yaml:\"min_signed_per_window\"', json_name='minSignedPerWindow', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downtime_jail_duration', full_name='cosmos.slashing.v1beta1.Params.downtime_jail_duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\362\336\037\035yaml:\"downtime_jail_duration\"\230\337\037\001', json_name='downtimeJailDuration', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slash_fraction_double_sign', full_name='cosmos.slashing.v1beta1.Params.slash_fraction_double_sign', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037!yaml:\"slash_fraction_double_sign\"', json_name='slashFractionDoubleSign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slash_fraction_downtime', full_name='cosmos.slashing.v1beta1.Params.slash_fraction_downtime', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\036yaml:\"slash_fraction_downtime\"', json_name='slashFractionDowntime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=550,
  serialized_end=1183,
)

_VALIDATORSIGNINGINFO.fields_by_name['jailed_until'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PARAMS.fields_by_name['downtime_jail_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ValidatorSigningInfo'] = _VALIDATORSIGNINGINFO
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidatorSigningInfo = _reflection.GeneratedProtocolMessageType('ValidatorSigningInfo', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSIGNINGINFO,
  '__module__' : 'cosmos.slashing.v1beta1.slashing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.ValidatorSigningInfo)
  })
_sym_db.RegisterMessage(ValidatorSigningInfo)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.slashing.v1beta1.slashing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_VALIDATORSIGNINGINFO.fields_by_name['start_height']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['index_offset']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['missed_blocks_counter']._options = None
_VALIDATORSIGNINGINFO._options = None
_PARAMS.fields_by_name['signed_blocks_window']._options = None
_PARAMS.fields_by_name['min_signed_per_window']._options = None
_PARAMS.fields_by_name['downtime_jail_duration']._options = None
_PARAMS.fields_by_name['slash_fraction_double_sign']._options = None
_PARAMS.fields_by_name['slash_fraction_downtime']._options = None
# @@protoc_insertion_point(module_scope)
