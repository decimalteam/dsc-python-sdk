# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/query.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/bank/v1beta1/query.proto',
  package='cosmos.bank.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\027com.cosmos.bank.v1beta1B\nQueryProtoP\001Z)github.com/cosmos/cosmos-sdk/x/bank/types\242\002\003CBX\252\002\023Cosmos.Bank.V1beta1\312\002\023Cosmos\\Bank\\V1beta1\342\002\037Cosmos\\Bank\\V1beta1\\GPBMetadata\352\002\025Cosmos::Bank::V1beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"O\n\x13QueryBalanceRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"K\n\x14QueryBalanceResponse\x12\x33\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinR\x07\x62\x61lance\"\x85\x01\n\x17QueryAllBalancesRequest\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xcc\x01\n\x18QueryAllBalancesResponse\x12g\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x08\x62\x61lances\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"k\n\x17QueryTotalSupplyRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xc8\x01\n\x18QueryTotalSupplyResponse\x12\x63\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x06supply\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\",\n\x14QuerySupplyOfRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"P\n\x15QuerySupplyOfResponse\x12\x37\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount\"\x14\n\x12QueryParamsRequest\"P\n\x13QueryParamsResponse\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params\"d\n\x1aQueryDenomsMetadataRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa9\x01\n\x1bQueryDenomsMetadataResponse\x12\x41\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00R\tmetadatas\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"1\n\x19QueryDenomMetadataRequest\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\"]\n\x1aQueryDenomMetadataResponse\x12?\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00R\x08metadata2\xb2\x08\n\x05Query\x12\x97\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//cosmos/bank/v1beta1/balances/{address}/{denom}\x12\x9b\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\x8f\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x8e\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/bank/v1beta1/supply/{denom}\x12\x80\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xa6\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xa1\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadataB\xbe\x01\n\x17\x63om.cosmos.bank.v1beta1B\nQueryProtoP\x01Z)github.com/cosmos/cosmos-sdk/x/bank/types\xa2\x02\x03\x43\x42X\xaa\x02\x13\x43osmos.Bank.V1beta1\xca\x02\x13\x43osmos\\Bank\\V1beta1\xe2\x02\x1f\x43osmos\\Bank\\V1beta1\\GPBMetadata\xea\x02\x15\x43osmos::Bank::V1beta1b\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_bank_dot_v1beta1_dot_bank__pb2.DESCRIPTOR,])




_QUERYBALANCEREQUEST = _descriptor.Descriptor(
  name='QueryBalanceRequest',
  full_name='cosmos.bank.v1beta1.QueryBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.bank.v1beta1.QueryBalanceRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='cosmos.bank.v1beta1.QueryBalanceRequest.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=295,
)


_QUERYBALANCERESPONSE = _descriptor.Descriptor(
  name='QueryBalanceResponse',
  full_name='cosmos.bank.v1beta1.QueryBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='cosmos.bank.v1beta1.QueryBalanceResponse.balance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='balance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=297,
  serialized_end=372,
)


_QUERYALLBALANCESREQUEST = _descriptor.Descriptor(
  name='QueryAllBalancesRequest',
  full_name='cosmos.bank.v1beta1.QueryAllBalancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.bank.v1beta1.QueryAllBalancesRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryAllBalancesRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=508,
)


_QUERYALLBALANCESRESPONSE = _descriptor.Descriptor(
  name='QueryAllBalancesResponse',
  full_name='cosmos.bank.v1beta1.QueryAllBalancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='balances', full_name='cosmos.bank.v1beta1.QueryAllBalancesResponse.balances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', json_name='balances', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryAllBalancesResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=511,
  serialized_end=715,
)


_QUERYTOTALSUPPLYREQUEST = _descriptor.Descriptor(
  name='QueryTotalSupplyRequest',
  full_name='cosmos.bank.v1beta1.QueryTotalSupplyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryTotalSupplyRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=824,
)


_QUERYTOTALSUPPLYRESPONSE = _descriptor.Descriptor(
  name='QueryTotalSupplyResponse',
  full_name='cosmos.bank.v1beta1.QueryTotalSupplyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supply', full_name='cosmos.bank.v1beta1.QueryTotalSupplyResponse.supply', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', json_name='supply', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryTotalSupplyResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=827,
  serialized_end=1027,
)


_QUERYSUPPLYOFREQUEST = _descriptor.Descriptor(
  name='QuerySupplyOfRequest',
  full_name='cosmos.bank.v1beta1.QuerySupplyOfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='cosmos.bank.v1beta1.QuerySupplyOfRequest.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1029,
  serialized_end=1073,
)


_QUERYSUPPLYOFRESPONSE = _descriptor.Descriptor(
  name='QuerySupplyOfResponse',
  full_name='cosmos.bank.v1beta1.QuerySupplyOfResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.bank.v1beta1.QuerySupplyOfResponse.amount', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1075,
  serialized_end=1155,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='cosmos.bank.v1beta1.QueryParamsRequest',
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
  serialized_start=1157,
  serialized_end=1177,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='cosmos.bank.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.bank.v1beta1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1179,
  serialized_end=1259,
)


_QUERYDENOMSMETADATAREQUEST = _descriptor.Descriptor(
  name='QueryDenomsMetadataRequest',
  full_name='cosmos.bank.v1beta1.QueryDenomsMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryDenomsMetadataRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1261,
  serialized_end=1361,
)


_QUERYDENOMSMETADATARESPONSE = _descriptor.Descriptor(
  name='QueryDenomsMetadataResponse',
  full_name='cosmos.bank.v1beta1.QueryDenomsMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadatas', full_name='cosmos.bank.v1beta1.QueryDenomsMetadataResponse.metadatas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='metadatas', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.bank.v1beta1.QueryDenomsMetadataResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1364,
  serialized_end=1533,
)


_QUERYDENOMMETADATAREQUEST = _descriptor.Descriptor(
  name='QueryDenomMetadataRequest',
  full_name='cosmos.bank.v1beta1.QueryDenomMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='cosmos.bank.v1beta1.QueryDenomMetadataRequest.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='denom', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1535,
  serialized_end=1584,
)


_QUERYDENOMMETADATARESPONSE = _descriptor.Descriptor(
  name='QueryDenomMetadataResponse',
  full_name='cosmos.bank.v1beta1.QueryDenomMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cosmos.bank.v1beta1.QueryDenomMetadataResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1586,
  serialized_end=1679,
)

_QUERYBALANCERESPONSE.fields_by_name['balance'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYALLBALANCESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYALLBALANCESRESPONSE.fields_by_name['balances'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYALLBALANCESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYTOTALSUPPLYREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYTOTALSUPPLYRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYSUPPLYOFRESPONSE.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._PARAMS
_QUERYDENOMSMETADATAREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._METADATA
_QUERYDENOMSMETADATARESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYDENOMMETADATARESPONSE.fields_by_name['metadata'].message_type = cosmos_dot_bank_dot_v1beta1_dot_bank__pb2._METADATA
DESCRIPTOR.message_types_by_name['QueryBalanceRequest'] = _QUERYBALANCEREQUEST
DESCRIPTOR.message_types_by_name['QueryBalanceResponse'] = _QUERYBALANCERESPONSE
DESCRIPTOR.message_types_by_name['QueryAllBalancesRequest'] = _QUERYALLBALANCESREQUEST
DESCRIPTOR.message_types_by_name['QueryAllBalancesResponse'] = _QUERYALLBALANCESRESPONSE
DESCRIPTOR.message_types_by_name['QueryTotalSupplyRequest'] = _QUERYTOTALSUPPLYREQUEST
DESCRIPTOR.message_types_by_name['QueryTotalSupplyResponse'] = _QUERYTOTALSUPPLYRESPONSE
DESCRIPTOR.message_types_by_name['QuerySupplyOfRequest'] = _QUERYSUPPLYOFREQUEST
DESCRIPTOR.message_types_by_name['QuerySupplyOfResponse'] = _QUERYSUPPLYOFRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryDenomsMetadataRequest'] = _QUERYDENOMSMETADATAREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomsMetadataResponse'] = _QUERYDENOMSMETADATARESPONSE
DESCRIPTOR.message_types_by_name['QueryDenomMetadataRequest'] = _QUERYDENOMMETADATAREQUEST
DESCRIPTOR.message_types_by_name['QueryDenomMetadataResponse'] = _QUERYDENOMMETADATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryBalanceRequest = _reflection.GeneratedProtocolMessageType('QueryBalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBALANCEREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryBalanceRequest)
  })
_sym_db.RegisterMessage(QueryBalanceRequest)

QueryBalanceResponse = _reflection.GeneratedProtocolMessageType('QueryBalanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBALANCERESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryBalanceResponse)
  })
_sym_db.RegisterMessage(QueryBalanceResponse)

QueryAllBalancesRequest = _reflection.GeneratedProtocolMessageType('QueryAllBalancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLBALANCESREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryAllBalancesRequest)
  })
_sym_db.RegisterMessage(QueryAllBalancesRequest)

QueryAllBalancesResponse = _reflection.GeneratedProtocolMessageType('QueryAllBalancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLBALANCESRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryAllBalancesResponse)
  })
_sym_db.RegisterMessage(QueryAllBalancesResponse)

QueryTotalSupplyRequest = _reflection.GeneratedProtocolMessageType('QueryTotalSupplyRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSUPPLYREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryTotalSupplyRequest)
  })
_sym_db.RegisterMessage(QueryTotalSupplyRequest)

QueryTotalSupplyResponse = _reflection.GeneratedProtocolMessageType('QueryTotalSupplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSUPPLYRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryTotalSupplyResponse)
  })
_sym_db.RegisterMessage(QueryTotalSupplyResponse)

QuerySupplyOfRequest = _reflection.GeneratedProtocolMessageType('QuerySupplyOfRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSUPPLYOFREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySupplyOfRequest)
  })
_sym_db.RegisterMessage(QuerySupplyOfRequest)

QuerySupplyOfResponse = _reflection.GeneratedProtocolMessageType('QuerySupplyOfResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSUPPLYOFRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySupplyOfResponse)
  })
_sym_db.RegisterMessage(QuerySupplyOfResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDenomsMetadataRequest = _reflection.GeneratedProtocolMessageType('QueryDenomsMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSMETADATAREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomsMetadataRequest)
  })
_sym_db.RegisterMessage(QueryDenomsMetadataRequest)

QueryDenomsMetadataResponse = _reflection.GeneratedProtocolMessageType('QueryDenomsMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSMETADATARESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomsMetadataResponse)
  })
_sym_db.RegisterMessage(QueryDenomsMetadataResponse)

QueryDenomMetadataRequest = _reflection.GeneratedProtocolMessageType('QueryDenomMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMMETADATAREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomMetadataRequest)
  })
_sym_db.RegisterMessage(QueryDenomMetadataRequest)

QueryDenomMetadataResponse = _reflection.GeneratedProtocolMessageType('QueryDenomMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMMETADATARESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomMetadataResponse)
  })
_sym_db.RegisterMessage(QueryDenomMetadataResponse)


DESCRIPTOR._options = None
_QUERYBALANCEREQUEST._options = None
_QUERYALLBALANCESREQUEST._options = None
_QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
_QUERYTOTALSUPPLYREQUEST._options = None
_QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
_QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
_QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
_QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.bank.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1682,
  serialized_end=2756,
  methods=[
  _descriptor.MethodDescriptor(
    name='Balance',
    full_name='cosmos.bank.v1beta1.Query.Balance',
    index=0,
    containing_service=None,
    input_type=_QUERYBALANCEREQUEST,
    output_type=_QUERYBALANCERESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//cosmos/bank/v1beta1/balances/{address}/{denom}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AllBalances',
    full_name='cosmos.bank.v1beta1.Query.AllBalances',
    index=1,
    containing_service=None,
    input_type=_QUERYALLBALANCESREQUEST,
    output_type=_QUERYALLBALANCESRESPONSE,
    serialized_options=b'\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TotalSupply',
    full_name='cosmos.bank.v1beta1.Query.TotalSupply',
    index=2,
    containing_service=None,
    input_type=_QUERYTOTALSUPPLYREQUEST,
    output_type=_QUERYTOTALSUPPLYRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SupplyOf',
    full_name='cosmos.bank.v1beta1.Query.SupplyOf',
    index=3,
    containing_service=None,
    input_type=_QUERYSUPPLYOFREQUEST,
    output_type=_QUERYSUPPLYOFRESPONSE,
    serialized_options=b'\202\323\344\223\002%\022#/cosmos/bank/v1beta1/supply/{denom}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='cosmos.bank.v1beta1.Query.Params',
    index=4,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DenomMetadata',
    full_name='cosmos.bank.v1beta1.Query.DenomMetadata',
    index=5,
    containing_service=None,
    input_type=_QUERYDENOMMETADATAREQUEST,
    output_type=_QUERYDENOMMETADATARESPONSE,
    serialized_options=b'\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DenomsMetadata',
    full_name='cosmos.bank.v1beta1.Query.DenomsMetadata',
    index=6,
    containing_service=None,
    input_type=_QUERYDENOMSMETADATAREQUEST,
    output_type=_QUERYDENOMSMETADATARESPONSE,
    serialized_options=b'\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
