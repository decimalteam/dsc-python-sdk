# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/reflection/v1beta1/reflection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/reflection/v1beta1/reflection.proto',
  package='cosmos.base.reflection.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\"com.cosmos.base.reflection.v1beta1B\017ReflectionProtoP\001Z3github.com/cosmos/cosmos-sdk/client/grpc/reflection\242\002\003CBR\252\002\036Cosmos.Base.Reflection.V1beta1\312\002\036Cosmos\\Base\\Reflection\\V1beta1\342\002*Cosmos\\Base\\Reflection\\V1beta1\\GPBMetadata\352\002!Cosmos::Base::Reflection::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/cosmos/base/reflection/v1beta1/reflection.proto\x12\x1e\x63osmos.base.reflection.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\x1a\n\x18ListAllInterfacesRequest\"D\n\x19ListAllInterfacesResponse\x12\'\n\x0finterface_names\x18\x01 \x03(\tR\x0einterfaceNames\"C\n\x1aListImplementationsRequest\x12%\n\x0einterface_name\x18\x01 \x01(\tR\rinterfaceName\"_\n\x1bListImplementationsResponse\x12@\n\x1cimplementation_message_names\x18\x01 \x03(\tR\x1aimplementationMessageNames2\xb8\x03\n\x11ReflectionService\x12\xbc\x01\n\x11ListAllInterfaces\x12\x38.cosmos.base.reflection.v1beta1.ListAllInterfacesRequest\x1a\x39.cosmos.base.reflection.v1beta1.ListAllInterfacesResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/reflection/v1beta1/interfaces\x12\xe3\x01\n\x13ListImplementations\x12:.cosmos.base.reflection.v1beta1.ListImplementationsRequest\x1a;.cosmos.base.reflection.v1beta1.ListImplementationsResponse\"S\x82\xd3\xe4\x93\x02M\x12K/cosmos/base/reflection/v1beta1/interfaces/{interface_name}/implementationsB\x85\x02\n\"com.cosmos.base.reflection.v1beta1B\x0fReflectionProtoP\x01Z3github.com/cosmos/cosmos-sdk/client/grpc/reflection\xa2\x02\x03\x43\x42R\xaa\x02\x1e\x43osmos.Base.Reflection.V1beta1\xca\x02\x1e\x43osmos\\Base\\Reflection\\V1beta1\xe2\x02*Cosmos\\Base\\Reflection\\V1beta1\\GPBMetadata\xea\x02!Cosmos::Base::Reflection::V1beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LISTALLINTERFACESREQUEST = _descriptor.Descriptor(
  name='ListAllInterfacesRequest',
  full_name='cosmos.base.reflection.v1beta1.ListAllInterfacesRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=139,
)


_LISTALLINTERFACESRESPONSE = _descriptor.Descriptor(
  name='ListAllInterfacesResponse',
  full_name='cosmos.base.reflection.v1beta1.ListAllInterfacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_names', full_name='cosmos.base.reflection.v1beta1.ListAllInterfacesResponse.interface_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='interfaceNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=141,
  serialized_end=209,
)


_LISTIMPLEMENTATIONSREQUEST = _descriptor.Descriptor(
  name='ListImplementationsRequest',
  full_name='cosmos.base.reflection.v1beta1.ListImplementationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cosmos.base.reflection.v1beta1.ListImplementationsRequest.interface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='interfaceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=278,
)


_LISTIMPLEMENTATIONSRESPONSE = _descriptor.Descriptor(
  name='ListImplementationsResponse',
  full_name='cosmos.base.reflection.v1beta1.ListImplementationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='implementation_message_names', full_name='cosmos.base.reflection.v1beta1.ListImplementationsResponse.implementation_message_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='implementationMessageNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=280,
  serialized_end=375,
)

DESCRIPTOR.message_types_by_name['ListAllInterfacesRequest'] = _LISTALLINTERFACESREQUEST
DESCRIPTOR.message_types_by_name['ListAllInterfacesResponse'] = _LISTALLINTERFACESRESPONSE
DESCRIPTOR.message_types_by_name['ListImplementationsRequest'] = _LISTIMPLEMENTATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListImplementationsResponse'] = _LISTIMPLEMENTATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAllInterfacesRequest = _reflection.GeneratedProtocolMessageType('ListAllInterfacesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALLINTERFACESREQUEST,
  '__module__' : 'cosmos.base.reflection.v1beta1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.reflection.v1beta1.ListAllInterfacesRequest)
  })
_sym_db.RegisterMessage(ListAllInterfacesRequest)

ListAllInterfacesResponse = _reflection.GeneratedProtocolMessageType('ListAllInterfacesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTALLINTERFACESRESPONSE,
  '__module__' : 'cosmos.base.reflection.v1beta1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.reflection.v1beta1.ListAllInterfacesResponse)
  })
_sym_db.RegisterMessage(ListAllInterfacesResponse)

ListImplementationsRequest = _reflection.GeneratedProtocolMessageType('ListImplementationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMPLEMENTATIONSREQUEST,
  '__module__' : 'cosmos.base.reflection.v1beta1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.reflection.v1beta1.ListImplementationsRequest)
  })
_sym_db.RegisterMessage(ListImplementationsRequest)

ListImplementationsResponse = _reflection.GeneratedProtocolMessageType('ListImplementationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMPLEMENTATIONSRESPONSE,
  '__module__' : 'cosmos.base.reflection.v1beta1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.reflection.v1beta1.ListImplementationsResponse)
  })
_sym_db.RegisterMessage(ListImplementationsResponse)


DESCRIPTOR._options = None

_REFLECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ReflectionService',
  full_name='cosmos.base.reflection.v1beta1.ReflectionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=378,
  serialized_end=818,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAllInterfaces',
    full_name='cosmos.base.reflection.v1beta1.ReflectionService.ListAllInterfaces',
    index=0,
    containing_service=None,
    input_type=_LISTALLINTERFACESREQUEST,
    output_type=_LISTALLINTERFACESRESPONSE,
    serialized_options=b'\202\323\344\223\002,\022*/cosmos/base/reflection/v1beta1/interfaces',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListImplementations',
    full_name='cosmos.base.reflection.v1beta1.ReflectionService.ListImplementations',
    index=1,
    containing_service=None,
    input_type=_LISTIMPLEMENTATIONSREQUEST,
    output_type=_LISTIMPLEMENTATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002M\022K/cosmos/base/reflection/v1beta1/interfaces/{interface_name}/implementations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REFLECTIONSERVICE)

DESCRIPTOR.services_by_name['ReflectionService'] = _REFLECTIONSERVICE

# @@protoc_insertion_point(module_scope)
