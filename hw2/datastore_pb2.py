# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datastore.proto

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
  name='datastore.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x61tastore.proto\"$\n\x07Request\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"%\n\x08Response\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x1d\n\x0bPullRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t2}\n\tDatastore\x12 \n\x03put\x12\x08.Request\x1a\t.Response\"\x00(\x01\x30\x01\x12#\n\x06\x64\x65lete\x12\x08.Request\x1a\t.Response\"\x00(\x01\x30\x01\x12)\n\nreplicator\x12\x0c.PullRequest\x1a\t.Response\"\x00\x30\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Request.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Request.data', index=1,
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
  serialized_start=19,
  serialized_end=55,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Response.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Response.data', index=1,
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
  serialized_start=57,
  serialized_end=94,
)


_PULLREQUEST = _descriptor.Descriptor(
  name='PullRequest',
  full_name='PullRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='PullRequest.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=96,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['PullRequest'] = _PULLREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

PullRequest = _reflection.GeneratedProtocolMessageType('PullRequest', (_message.Message,), dict(
  DESCRIPTOR = _PULLREQUEST,
  __module__ = 'datastore_pb2'
  # @@protoc_insertion_point(class_scope:PullRequest)
  ))
_sym_db.RegisterMessage(PullRequest)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DatastoreStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.put = channel.stream_stream(
          '/Datastore/put',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.delete = channel.stream_stream(
          '/Datastore/delete',
          request_serializer=Request.SerializeToString,
          response_deserializer=Response.FromString,
          )
      self.replicator = channel.unary_stream(
          '/Datastore/replicator',
          request_serializer=PullRequest.SerializeToString,
          response_deserializer=Response.FromString,
          )


  class DatastoreServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def put(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def delete(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def replicator(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DatastoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'put': grpc.stream_stream_rpc_method_handler(
            servicer.put,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'delete': grpc.stream_stream_rpc_method_handler(
            servicer.delete,
            request_deserializer=Request.FromString,
            response_serializer=Response.SerializeToString,
        ),
        'replicator': grpc.unary_stream_rpc_method_handler(
            servicer.replicator,
            request_deserializer=PullRequest.FromString,
            response_serializer=Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Datastore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDatastoreServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def delete(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def replicator(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDatastoreStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def put(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def delete(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def replicator(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()


  def beta_create_Datastore_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Datastore', 'delete'): Request.FromString,
      ('Datastore', 'put'): Request.FromString,
      ('Datastore', 'replicator'): PullRequest.FromString,
    }
    response_serializers = {
      ('Datastore', 'delete'): Response.SerializeToString,
      ('Datastore', 'put'): Response.SerializeToString,
      ('Datastore', 'replicator'): Response.SerializeToString,
    }
    method_implementations = {
      ('Datastore', 'delete'): face_utilities.stream_stream_inline(servicer.delete),
      ('Datastore', 'put'): face_utilities.stream_stream_inline(servicer.put),
      ('Datastore', 'replicator'): face_utilities.unary_stream_inline(servicer.replicator),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Datastore_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Datastore', 'delete'): Request.SerializeToString,
      ('Datastore', 'put'): Request.SerializeToString,
      ('Datastore', 'replicator'): PullRequest.SerializeToString,
    }
    response_deserializers = {
      ('Datastore', 'delete'): Response.FromString,
      ('Datastore', 'put'): Response.FromString,
      ('Datastore', 'replicator'): Response.FromString,
    }
    cardinalities = {
      'delete': cardinality.Cardinality.STREAM_STREAM,
      'put': cardinality.Cardinality.STREAM_STREAM,
      'replicator': cardinality.Cardinality.UNARY_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Datastore', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
