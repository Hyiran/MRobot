# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetGoodsCategoryResult.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetGoodsCategoryResult.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1cGetGoodsCategoryResult.proto\"i\n\x16GetGoodsCategoryResult\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x19\n\x11\x65rror_description\x18\x03 \x01(\t\x12\x17\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\t.Category\"E\n\x08\x43\x61tegory\x12\x14\n\x0c\x63\x61tegoryName\x18\x01 \x01(\t\x12#\n\x0c\x63\x61tegoryItem\x18\x02 \x03(\x0b\x32\r.CategoryItem\"I\n\x0c\x43\x61tegoryItem\x12\x14\n\x0c\x63\x61tegoryName\x18\x01 \x01(\t\x12#\n\x0c\x63\x61tegoryInfo\x18\x02 \x03(\x0b\x32\r.CategoryInfo\".\n\x0c\x43\x61tegoryInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08imageUrl\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETGOODSCATEGORYRESULT = _descriptor.Descriptor(
  name='GetGoodsCategoryResult',
  full_name='GetGoodsCategoryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='GetGoodsCategoryResult.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='GetGoodsCategoryResult.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_description', full_name='GetGoodsCategoryResult.error_description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='GetGoodsCategoryResult.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=137,
)


_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categoryName', full_name='Category.categoryName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='categoryItem', full_name='Category.categoryItem', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=208,
)


_CATEGORYITEM = _descriptor.Descriptor(
  name='CategoryItem',
  full_name='CategoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categoryName', full_name='CategoryItem.categoryName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='categoryInfo', full_name='CategoryItem.categoryInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=283,
)


_CATEGORYINFO = _descriptor.Descriptor(
  name='CategoryInfo',
  full_name='CategoryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CategoryInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageUrl', full_name='CategoryInfo.imageUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=331,
)

_GETGOODSCATEGORYRESULT.fields_by_name['data'].message_type = _CATEGORY
_CATEGORY.fields_by_name['categoryItem'].message_type = _CATEGORYITEM
_CATEGORYITEM.fields_by_name['categoryInfo'].message_type = _CATEGORYINFO
DESCRIPTOR.message_types_by_name['GetGoodsCategoryResult'] = _GETGOODSCATEGORYRESULT
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['CategoryItem'] = _CATEGORYITEM
DESCRIPTOR.message_types_by_name['CategoryInfo'] = _CATEGORYINFO

GetGoodsCategoryResult = _reflection.GeneratedProtocolMessageType('GetGoodsCategoryResult', (_message.Message,), dict(
  DESCRIPTOR = _GETGOODSCATEGORYRESULT,
  __module__ = 'GetGoodsCategoryResult_pb2'
  # @@protoc_insertion_point(class_scope:GetGoodsCategoryResult)
  ))
_sym_db.RegisterMessage(GetGoodsCategoryResult)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORY,
  __module__ = 'GetGoodsCategoryResult_pb2'
  # @@protoc_insertion_point(class_scope:Category)
  ))
_sym_db.RegisterMessage(Category)

CategoryItem = _reflection.GeneratedProtocolMessageType('CategoryItem', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORYITEM,
  __module__ = 'GetGoodsCategoryResult_pb2'
  # @@protoc_insertion_point(class_scope:CategoryItem)
  ))
_sym_db.RegisterMessage(CategoryItem)

CategoryInfo = _reflection.GeneratedProtocolMessageType('CategoryInfo', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORYINFO,
  __module__ = 'GetGoodsCategoryResult_pb2'
  # @@protoc_insertion_point(class_scope:CategoryInfo)
  ))
_sym_db.RegisterMessage(CategoryInfo)


# @@protoc_insertion_point(module_scope)
