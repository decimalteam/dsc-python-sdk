# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/multisig/v1/params.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/multisig/v1/params.proto',
  package='decimal.multisig.v1',
  syntax='proto3',
  serialized_options=b'\n\027com.decimal.multisig.v1B\013ParamsProtoP\001Z8bitbucket.org/decimalteam/go-smart-node/x/multisig/types\242\002\003DMX\252\002\023Decimal.Multisig.V1\312\002\023Decimal\\Multisig\\V1\342\002\037Decimal\\Multisig\\V1\\GPBMetadata\352\002\025Decimal::Multisig::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n decimal/multisig/v1/params.proto\x12\x13\x64\x65\x63imal.multisig.v1\x1a\x14gogoproto/gogo.proto\"\x16\n\x06Params:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x01\xe8\xa0\x1f\x01\x42\xce\x01\n\x17\x63om.decimal.multisig.v1B\x0bParamsProtoP\x01Z8bitbucket.org/decimalteam/go-smart-node/x/multisig/types\xa2\x02\x03\x44MX\xaa\x02\x13\x44\x65\x63imal.Multisig.V1\xca\x02\x13\x44\x65\x63imal\\Multisig\\V1\xe2\x02\x1f\x44\x65\x63imal\\Multisig\\V1\\GPBMetadata\xea\x02\x15\x44\x65\x63imal::Multisig::V1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='decimal.multisig.v1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=79,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'decimal.multisig.v1.params_pb2'
  # @@protoc_insertion_point(class_scope:decimal.multisig.v1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_PARAMS._options = None
# @@protoc_insertion_point(module_scope)
