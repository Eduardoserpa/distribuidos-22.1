# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rgateway.proto\"\xd6\x01\n\x0eGatewayRequest\x12\x31\n\x0crequest_type\x18\x01 \x01(\x0e\x32\x1b.GatewayRequest.RequestType\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\x05\x12\x0b\n\x03\x61ux\x18\x04 \x01(\t\"b\n\x0bRequestType\x12\x0e\n\nReadStatus\x10\x00\x12\x0e\n\nReadSensor\x10\x01\x12\x10\n\x0cUpdateStatus\x10\x02\x12\x0f\n\x0bUpdateOnOff\x10\x03\x12\x10\n\x0cListCommands\x10\x04\"\x84\x01\n\x0e\x44\x65viceResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tsensor_id\x18\x03 \x01(\x05\x12\x11\n\tclient_id\x18\x04 \x01(\x05\x12\x15\n\robject_status\x18\x05 \x01(\x05\x12\x17\n\x0fobject_commands\x18\x06 \x03(\t\"2\n\x08\x44\x65viceID\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x03\x62\x06proto3')
)



_GATEWAYREQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='GatewayRequest.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ReadStatus', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReadSensor', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateStatus', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateOnOff', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ListCommands', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=134,
  serialized_end=232,
)
_sym_db.RegisterEnumDescriptor(_GATEWAYREQUEST_REQUESTTYPE)


_GATEWAYREQUEST = _descriptor.Descriptor(
  name='GatewayRequest',
  full_name='GatewayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='GatewayRequest.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='GatewayRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='GatewayRequest.client_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aux', full_name='GatewayRequest.aux', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GATEWAYREQUEST_REQUESTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=232,
)


_DEVICERESPONSE = _descriptor.Descriptor(
  name='DeviceResponse',
  full_name='DeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='DeviceResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='DeviceResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='DeviceResponse.sensor_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='DeviceResponse.client_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_status', full_name='DeviceResponse.object_status', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_commands', full_name='DeviceResponse.object_commands', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=235,
  serialized_end=367,
)


_DEVICEID = _descriptor.Descriptor(
  name='DeviceID',
  full_name='DeviceID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='DeviceID.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='DeviceID.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='DeviceID.port', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=369,
  serialized_end=419,
)

_GATEWAYREQUEST.fields_by_name['request_type'].enum_type = _GATEWAYREQUEST_REQUESTTYPE
_GATEWAYREQUEST_REQUESTTYPE.containing_type = _GATEWAYREQUEST
DESCRIPTOR.message_types_by_name['GatewayRequest'] = _GATEWAYREQUEST
DESCRIPTOR.message_types_by_name['DeviceResponse'] = _DEVICERESPONSE
DESCRIPTOR.message_types_by_name['DeviceID'] = _DEVICEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GatewayRequest = _reflection.GeneratedProtocolMessageType('GatewayRequest', (_message.Message,), dict(
  DESCRIPTOR = _GATEWAYREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:GatewayRequest)
  ))
_sym_db.RegisterMessage(GatewayRequest)

DeviceResponse = _reflection.GeneratedProtocolMessageType('DeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEVICERESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:DeviceResponse)
  ))
_sym_db.RegisterMessage(DeviceResponse)

DeviceID = _reflection.GeneratedProtocolMessageType('DeviceID', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEID,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:DeviceID)
  ))
_sym_db.RegisterMessage(DeviceID)


# @@protoc_insertion_point(module_scope)
