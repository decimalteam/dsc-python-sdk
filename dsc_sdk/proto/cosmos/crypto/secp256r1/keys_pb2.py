# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/secp256r1/keys.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crypto/secp256r1/keys.proto',
  package='cosmos.crypto.secp256r1',
  syntax='proto3',
  serialized_options=b'\n\033com.cosmos.crypto.secp256r1B\tKeysProtoP\001Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\242\002\003CCS\252\002\027Cosmos.Crypto.Secp256r1\312\002\027Cosmos\\Crypto\\Secp256r1\342\002#Cosmos\\Crypto\\Secp256r1\\GPBMetadata\352\002\031Cosmos::Crypto::Secp256r1\310\341\036\000\330\341\036\000\310\343\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"cosmos/crypto/secp256r1/keys.proto\x12\x17\x63osmos.crypto.secp256r1\x1a\x14gogoproto/gogo.proto\"\'\n\x06PubKey\x12\x1d\n\x03key\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saPKR\x03key\".\n\x07PrivKey\x12#\n\x06secret\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saSKR\x06secretB\xe6\x01\n\x1b\x63om.cosmos.crypto.secp256r1B\tKeysProtoP\x01Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xa2\x02\x03\x43\x43S\xaa\x02\x17\x43osmos.Crypto.Secp256r1\xca\x02\x17\x43osmos\\Crypto\\Secp256r1\xe2\x02#Cosmos\\Crypto\\Secp256r1\\GPBMetadata\xea\x02\x19\x43osmos::Crypto::Secp256r1\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xc8\xe3\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PUBKEY = _descriptor.Descriptor(
  name='PubKey',
  full_name='cosmos.crypto.secp256r1.PubKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.crypto.secp256r1.PubKey.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\007ecdsaPK', json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=85,
  serialized_end=124,
)


_PRIVKEY = _descriptor.Descriptor(
  name='PrivKey',
  full_name='cosmos.crypto.secp256r1.PrivKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret', full_name='cosmos.crypto.secp256r1.PrivKey.secret', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\007ecdsaSK', json_name='secret', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=126,
  serialized_end=172,
)

DESCRIPTOR.message_types_by_name['PubKey'] = _PUBKEY
DESCRIPTOR.message_types_by_name['PrivKey'] = _PRIVKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), {
  'DESCRIPTOR' : _PUBKEY,
  '__module__' : 'cosmos.crypto.secp256r1.keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.secp256r1.PubKey)
  })
_sym_db.RegisterMessage(PubKey)

PrivKey = _reflection.GeneratedProtocolMessageType('PrivKey', (_message.Message,), {
  'DESCRIPTOR' : _PRIVKEY,
  '__module__' : 'cosmos.crypto.secp256r1.keys_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.secp256r1.PrivKey)
  })
_sym_db.RegisterMessage(PrivKey)


DESCRIPTOR._options = None
_PUBKEY.fields_by_name['key']._options = None
_PRIVKEY.fields_by_name['secret']._options = None
# @@protoc_insertion_point(module_scope)
