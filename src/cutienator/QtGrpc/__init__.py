"""
The 'cutienator.QtGrpc' package provides the cute classes of the part of
Qt named QtGrpc, under the name PySide6 has for it.

  from cutienator.QtGrpc import QGrpcInterceptorChain, QGrpcInterceptorChainPrivate

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QGrpcInterceptorChain',
    'QGrpcInterceptorChainPrivate',
    'QGrpcCallOptions',
    'QGrpcCommonOptions',
    'QGrpcStatus',
    'QGrpcOperationContextPrivate',
    'QGrpcSerializationFormat',
    'QGrpcChannelOptions',
    'QAbstractGrpcChannel',
    'QGrpcOperation',
    'QAbstractGrpcChannelPrivate',
    'QGrpcOperationContext',
    'QGrpcBidiStream',
    'QGrpcCallReply',
    'QGrpcClientBase',
    'QGrpcClientStream',
    'QGrpcHttp2Channel',
    'QGrpcInterceptionContext',
    'QGrpcInterceptorEngine',
    'QGrpcOperationPrivate',
    'QGrpcServerStream',
    'QGrpcCancelInterceptor',
    'QGrpcFinishedInterceptor',
    'QGrpcInitialMetadataInterceptor',
    'QGrpcMessageReceivedInterceptor',
    'QGrpcStartInterceptor',
    'QGrpcTrailingMetadataInterceptor',
    'QGrpcWriteMessageInterceptor',
    'QGrpcWritesDoneInterceptor',
    'QtGrpc',
    'QtGrpcPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_grpc_interceptor_chain import QGrpcInterceptorChain
  from ._q_grpc_interceptor_chain_private import QGrpcInterceptorChainPrivate
  from ._q_grpc_call_options import QGrpcCallOptions
  from ._q_grpc_common_options import QGrpcCommonOptions
  from ._q_grpc_status import QGrpcStatus
  from ._q_grpc_operation_context_private import QGrpcOperationContextPrivate
  from ._q_grpc_serialization_format import QGrpcSerializationFormat
  from ._q_grpc_channel_options import QGrpcChannelOptions
  from ._q_abstract_grpc_channel import QAbstractGrpcChannel
  from ._q_grpc_operation import QGrpcOperation
  from ._q_abstract_grpc_channel_private import QAbstractGrpcChannelPrivate
  from ._q_grpc_operation_context import QGrpcOperationContext
  from ._q_grpc_bidi_stream import QGrpcBidiStream
  from ._q_grpc_call_reply import QGrpcCallReply
  from ._q_grpc_client_base import QGrpcClientBase
  from ._q_grpc_client_stream import QGrpcClientStream
  from ._q_grpc_http2_channel import QGrpcHttp2Channel
  from ._q_grpc_interception_context import QGrpcInterceptionContext
  from ._q_grpc_interceptor_engine import QGrpcInterceptorEngine
  from ._q_grpc_operation_private import QGrpcOperationPrivate
  from ._q_grpc_server_stream import QGrpcServerStream
  from ._q_grpc_cancel_interceptor import QGrpcCancelInterceptor
  from ._q_grpc_finished_interceptor import QGrpcFinishedInterceptor
  from ._q_grpc_initial_metadata_interceptor import QGrpcInitialMetadataInterceptor
  from ._q_grpc_message_received_interceptor import QGrpcMessageReceivedInterceptor
  from ._q_grpc_start_interceptor import QGrpcStartInterceptor
  from ._q_grpc_trailing_metadata_interceptor import QGrpcTrailingMetadataInterceptor
  from ._q_grpc_write_message_interceptor import QGrpcWriteMessageInterceptor
  from ._q_grpc_writes_done_interceptor import QGrpcWritesDoneInterceptor
  from . import QtGrpc
  from . import QtGrpcPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QGrpcInterceptorChain': '_q_grpc_interceptor_chain',
      'QGrpcInterceptorChainPrivate': '_q_grpc_interceptor_chain_private',
      'QGrpcCallOptions': '_q_grpc_call_options',
      'QGrpcCommonOptions': '_q_grpc_common_options',
      'QGrpcStatus': '_q_grpc_status',
      'QGrpcOperationContextPrivate': '_q_grpc_operation_context_private',
      'QGrpcSerializationFormat': '_q_grpc_serialization_format',
      'QGrpcChannelOptions': '_q_grpc_channel_options',
      'QAbstractGrpcChannel': '_q_abstract_grpc_channel',
      'QGrpcOperation': '_q_grpc_operation',
      'QAbstractGrpcChannelPrivate': '_q_abstract_grpc_channel_private',
      'QGrpcOperationContext': '_q_grpc_operation_context',
      'QGrpcBidiStream': '_q_grpc_bidi_stream',
      'QGrpcCallReply': '_q_grpc_call_reply',
      'QGrpcClientBase': '_q_grpc_client_base',
      'QGrpcClientStream': '_q_grpc_client_stream',
      'QGrpcHttp2Channel': '_q_grpc_http2_channel',
      'QGrpcInterceptionContext': '_q_grpc_interception_context',
      'QGrpcInterceptorEngine': '_q_grpc_interceptor_engine',
      'QGrpcOperationPrivate': '_q_grpc_operation_private',
      'QGrpcServerStream': '_q_grpc_server_stream',
      'QGrpcCancelInterceptor': '_q_grpc_cancel_interceptor',
      'QGrpcFinishedInterceptor': '_q_grpc_finished_interceptor',
      'QGrpcInitialMetadataInterceptor': '_q_grpc_initial_metadata_interceptor',
      'QGrpcMessageReceivedInterceptor': '_q_grpc_message_received_interceptor',
      'QGrpcStartInterceptor': '_q_grpc_start_interceptor',
      'QGrpcTrailingMetadataInterceptor': '_q_grpc_trailing_metadata_interceptor',
      'QGrpcWriteMessageInterceptor': '_q_grpc_write_message_interceptor',
      'QGrpcWritesDoneInterceptor': '_q_grpc_writes_done_interceptor',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtGrpc', 'QtGrpcPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtGrpc import QGrpcWritesDoneInterceptor'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
