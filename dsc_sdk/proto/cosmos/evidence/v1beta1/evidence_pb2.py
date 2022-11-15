# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/evidence.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/evidence/v1beta1/evidence.proto',
  package='cosmos.evidence.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\033com.cosmos.evidence.v1beta1B\rEvidenceProtoP\001Z-github.com/cosmos/cosmos-sdk/x/evidence/types\242\002\003CEX\252\002\027Cosmos.Evidence.V1beta1\312\002\027Cosmos\\Evidence\\V1beta1\342\002#Cosmos\\Evidence\\V1beta1\\GPBMetadata\352\002\031Cosmos::Evidence::V1beta1\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&cosmos/evidence/v1beta1/evidence.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x01\n\x0c\x45quivocation\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\x12\x38\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01R\x04time\x12\x14\n\x05power\x18\x03 \x01(\x03R\x05power\x12I\n\x11\x63onsensus_address\x18\x04 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"consensus_address\"R\x10\x63onsensusAddress:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x42\xdd\x01\n\x1b\x63om.cosmos.evidence.v1beta1B\rEvidenceProtoP\x01Z-github.com/cosmos/cosmos-sdk/x/evidence/types\xa2\x02\x03\x43\x45X\xaa\x02\x17\x43osmos.Evidence.V1beta1\xca\x02\x17\x43osmos\\Evidence\\V1beta1\xe2\x02#Cosmos\\Evidence\\V1beta1\\GPBMetadata\xea\x02\x19\x43osmos::Evidence::V1beta1\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_EQUIVOCATION = _descriptor.Descriptor(
  name='Equivocation',
  full_name='cosmos.evidence.v1beta1.Equivocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.evidence.v1beta1.Equivocation.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='height', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='cosmos.evidence.v1beta1.Equivocation.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\220\337\037\001', json_name='time', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='power', full_name='cosmos.evidence.v1beta1.Equivocation.power', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='power', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consensus_address', full_name='cosmos.evidence.v1beta1.Equivocation.consensus_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\030yaml:\"consensus_address\"', json_name='consensusAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=330,
)

_EQUIVOCATION.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Equivocation'] = _EQUIVOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Equivocation = _reflection.GeneratedProtocolMessageType('Equivocation', (_message.Message,), {
  'DESCRIPTOR' : _EQUIVOCATION,
  '__module__' : 'cosmos.evidence.v1beta1.evidence_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.evidence.v1beta1.Equivocation)
  })
_sym_db.RegisterMessage(Equivocation)


DESCRIPTOR._options = None
_EQUIVOCATION.fields_by_name['time']._options = None
_EQUIVOCATION.fields_by_name['consensus_address']._options = None
_EQUIVOCATION._options = None
# @@protoc_insertion_point(module_scope)
