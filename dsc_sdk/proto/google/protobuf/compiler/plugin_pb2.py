# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/compiler/plugin.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/compiler/plugin.proto',
  package='google.protobuf.compiler',
  syntax='proto2',
  serialized_options=b'\n\034com.google.protobuf.compilerB\014PluginProtosZ\tplugin_go',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%google/protobuf/compiler/plugin.proto\x12\x18google.protobuf.compiler\x1a google/protobuf/descriptor.proto\"c\n\x07Version\x12\x14\n\x05major\x18\x01 \x01(\x05R\x05major\x12\x14\n\x05minor\x18\x02 \x01(\x05R\x05minor\x12\x14\n\x05patch\x18\x03 \x01(\x05R\x05patch\x12\x16\n\x06suffix\x18\x04 \x01(\tR\x06suffix\"\xf1\x01\n\x14\x43odeGeneratorRequest\x12(\n\x10\x66ile_to_generate\x18\x01 \x03(\tR\x0e\x66ileToGenerate\x12\x1c\n\tparameter\x18\x02 \x01(\tR\tparameter\x12\x43\n\nproto_file\x18\x0f \x03(\x0b\x32$.google.protobuf.FileDescriptorProtoR\tprotoFile\x12L\n\x10\x63ompiler_version\x18\x03 \x01(\x0b\x32!.google.protobuf.compiler.VersionR\x0f\x63ompilerVersion\"\xd6\x01\n\x15\x43odeGeneratorResponse\x12\x14\n\x05\x65rror\x18\x01 \x01(\tR\x05\x65rror\x12H\n\x04\x66ile\x18\x0f \x03(\x0b\x32\x34.google.protobuf.compiler.CodeGeneratorResponse.FileR\x04\x66ile\x1a]\n\x04\x46ile\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0finsertion_point\x18\x02 \x01(\tR\x0einsertionPoint\x12\x18\n\x07\x63ontent\x18\x0f \x01(\tR\x07\x63ontentB7\n\x1c\x63om.google.protobuf.compilerB\x0cPluginProtosZ\tplugin_go'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])




_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='google.protobuf.compiler.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='google.protobuf.compiler.Version.major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='major', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor', full_name='google.protobuf.compiler.Version.minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='minor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patch', full_name='google.protobuf.compiler.Version.patch', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='patch', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='google.protobuf.compiler.Version.suffix', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='suffix', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=200,
)


_CODEGENERATORREQUEST = _descriptor.Descriptor(
  name='CodeGeneratorRequest',
  full_name='google.protobuf.compiler.CodeGeneratorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_to_generate', full_name='google.protobuf.compiler.CodeGeneratorRequest.file_to_generate', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fileToGenerate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='google.protobuf.compiler.CodeGeneratorRequest.parameter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parameter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proto_file', full_name='google.protobuf.compiler.CodeGeneratorRequest.proto_file', index=2,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='protoFile', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compiler_version', full_name='google.protobuf.compiler.CodeGeneratorRequest.compiler_version', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='compilerVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=444,
)


_CODEGENERATORRESPONSE_FILE = _descriptor.Descriptor(
  name='File',
  full_name='google.protobuf.compiler.CodeGeneratorResponse.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='insertion_point', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.insertion_point', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='insertionPoint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.content', index=2,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='content', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=661,
)

_CODEGENERATORRESPONSE = _descriptor.Descriptor(
  name='CodeGeneratorResponse',
  full_name='google.protobuf.compiler.CodeGeneratorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='google.protobuf.compiler.CodeGeneratorResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='error', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='google.protobuf.compiler.CodeGeneratorResponse.file', index=1,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='file', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CODEGENERATORRESPONSE_FILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=661,
)

_CODEGENERATORREQUEST.fields_by_name['proto_file'].message_type = google_dot_protobuf_dot_descriptor__pb2._FILEDESCRIPTORPROTO
_CODEGENERATORREQUEST.fields_by_name['compiler_version'].message_type = _VERSION
_CODEGENERATORRESPONSE_FILE.containing_type = _CODEGENERATORRESPONSE
_CODEGENERATORRESPONSE.fields_by_name['file'].message_type = _CODEGENERATORRESPONSE_FILE
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['CodeGeneratorRequest'] = _CODEGENERATORREQUEST
DESCRIPTOR.message_types_by_name['CodeGeneratorResponse'] = _CODEGENERATORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'google.protobuf.compiler.plugin_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.compiler.Version)
  })
_sym_db.RegisterMessage(Version)

CodeGeneratorRequest = _reflection.GeneratedProtocolMessageType('CodeGeneratorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CODEGENERATORREQUEST,
  '__module__' : 'google.protobuf.compiler.plugin_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorRequest)
  })
_sym_db.RegisterMessage(CodeGeneratorRequest)

CodeGeneratorResponse = _reflection.GeneratedProtocolMessageType('CodeGeneratorResponse', (_message.Message,), {

  'File' : _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
    'DESCRIPTOR' : _CODEGENERATORRESPONSE_FILE,
    '__module__' : 'google.protobuf.compiler.plugin_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorResponse.File)
    })
  ,
  'DESCRIPTOR' : _CODEGENERATORRESPONSE,
  '__module__' : 'google.protobuf.compiler.plugin_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorResponse)
  })
_sym_db.RegisterMessage(CodeGeneratorResponse)
_sym_db.RegisterMessage(CodeGeneratorResponse.File)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)