"""
The 'cutienator.QtHttpServer' package provides the cute classes of the
part of Qt named QtHttpServer, under the name PySide6 has for it.

  from cutienator.QtHttpServer import QHttpServerHttp2Data, QHttpServerHttp2Queue

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
    'QHttpServerHttp2Data',
    'QHttpServerHttp2Queue',
    'QHttpServerRouterRulePrivate',
    'QHttpServerWebSocketUpgradeResponse',
    'LessHostAddress',
    'QHttpServerConfiguration',
    'QHttpServerResponse',
    'QHttpServerRequestFilter',
    'QHttpServerResponsePrivate',
    'QHttpServerResponder',
    'QHttpServerResponderPrivate',
    'QHttpServerStream',
    'QAbstractHttpServerPrivate',
    'QHttpServerParser',
    'QHttpServerRequestPrivate',
    'QHttpServerRequest',
    'QAbstractHttpServer',
    'QHttpServerRouterRule',
    'QHttpServer',
    'QHttpServerHttp1ProtocolHandler',
    'QHttpServerHttp2ProtocolHandler',
    'QHttpServerRouter',
    'QHttpServerRouterPrivate',
    'QHttpServerPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_http_server_http2_data import QHttpServerHttp2Data
  from ._q_http_server_http2_queue import QHttpServerHttp2Queue
  from ._q_http_server_router_rule_private import QHttpServerRouterRulePrivate
  from ._q_http_server_web_socket_upgrade_response import QHttpServerWebSocketUpgradeResponse
  from ._less_host_address import LessHostAddress
  from ._q_http_server_configuration import QHttpServerConfiguration
  from ._q_http_server_response import QHttpServerResponse
  from ._q_http_server_request_filter import QHttpServerRequestFilter
  from ._q_http_server_response_private import QHttpServerResponsePrivate
  from ._q_http_server_responder import QHttpServerResponder
  from ._q_http_server_responder_private import QHttpServerResponderPrivate
  from ._q_http_server_stream import QHttpServerStream
  from ._q_abstract_http_server_private import QAbstractHttpServerPrivate
  from ._q_http_server_parser import QHttpServerParser
  from ._q_http_server_request_private import QHttpServerRequestPrivate
  from ._q_http_server_request import QHttpServerRequest
  from ._q_abstract_http_server import QAbstractHttpServer
  from ._q_http_server_router_rule import QHttpServerRouterRule
  from ._q_http_server import QHttpServer
  from ._q_http_server_http1_protocol_handler import QHttpServerHttp1ProtocolHandler
  from ._q_http_server_http2_protocol_handler import QHttpServerHttp2ProtocolHandler
  from ._q_http_server_router import QHttpServerRouter
  from ._q_http_server_router_private import QHttpServerRouterPrivate
  from ._q_http_server_private import QHttpServerPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QHttpServerHttp2Data': '_q_http_server_http2_data',
      'QHttpServerHttp2Queue': '_q_http_server_http2_queue',
      'QHttpServerRouterRulePrivate': '_q_http_server_router_rule_private',
      'QHttpServerWebSocketUpgradeResponse': '_q_http_server_web_socket_upgrade_response',
      'LessHostAddress': '_less_host_address',
      'QHttpServerConfiguration': '_q_http_server_configuration',
      'QHttpServerResponse': '_q_http_server_response',
      'QHttpServerRequestFilter': '_q_http_server_request_filter',
      'QHttpServerResponsePrivate': '_q_http_server_response_private',
      'QHttpServerResponder': '_q_http_server_responder',
      'QHttpServerResponderPrivate': '_q_http_server_responder_private',
      'QHttpServerStream': '_q_http_server_stream',
      'QAbstractHttpServerPrivate': '_q_abstract_http_server_private',
      'QHttpServerParser': '_q_http_server_parser',
      'QHttpServerRequestPrivate': '_q_http_server_request_private',
      'QHttpServerRequest': '_q_http_server_request',
      'QAbstractHttpServer': '_q_abstract_http_server',
      'QHttpServerRouterRule': '_q_http_server_router_rule',
      'QHttpServer': '_q_http_server',
      'QHttpServerHttp1ProtocolHandler': '_q_http_server_http1_protocol_handler',
      'QHttpServerHttp2ProtocolHandler': '_q_http_server_http2_protocol_handler',
      'QHttpServerRouter': '_q_http_server_router',
      'QHttpServerRouterPrivate': '_q_http_server_router_private',
      'QHttpServerPrivate': '_q_http_server_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtHttpServer import QHttpServerPrivate'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
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
