"""
The 'cutienator.QtWebSockets' package provides the cute classes of the
part of Qt named QtWebSockets, under the name PySide6 has for it.

  from cutienator.QtWebSockets import QWebSocketConfiguration, QWebSocketHandshakeOptions

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
    'QWebSocketConfiguration',
    'QWebSocketHandshakeOptions',
    'QWebSocketHandshakeOptionsPrivate',
    'QWebSocketHandshakeRequest',
    'QWebSocketCorsAuthenticator',
    'QWebSocketCorsAuthenticatorPrivate',
    'QMaskGenerator',
    'QWebSocketFrame',
    'QWebSocketHandshakeResponse',
    'QDefaultMaskGenerator',
    'QWebSocketDataProcessor',
    'QWebSocket',
    'QWebSocketPrivate',
    'QWebSocketServer',
    'QWebSocketServerPrivate',
    'QWebSocketProtocol',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_web_socket_configuration import QWebSocketConfiguration
  from ._q_web_socket_handshake_options import QWebSocketHandshakeOptions
  from ._q_web_socket_handshake_options_private import QWebSocketHandshakeOptionsPrivate
  from ._q_web_socket_handshake_request import QWebSocketHandshakeRequest
  from ._q_web_socket_cors_authenticator import QWebSocketCorsAuthenticator
  from ._q_web_socket_cors_authenticator_private import QWebSocketCorsAuthenticatorPrivate
  from ._q_mask_generator import QMaskGenerator
  from ._q_web_socket_frame import QWebSocketFrame
  from ._q_web_socket_handshake_response import QWebSocketHandshakeResponse
  from ._q_default_mask_generator import QDefaultMaskGenerator
  from ._q_web_socket_data_processor import QWebSocketDataProcessor
  from ._q_web_socket import QWebSocket
  from ._q_web_socket_private import QWebSocketPrivate
  from ._q_web_socket_server import QWebSocketServer
  from ._q_web_socket_server_private import QWebSocketServerPrivate
  from . import QWebSocketProtocol
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QWebSocketConfiguration': '_q_web_socket_configuration',
      'QWebSocketHandshakeOptions': '_q_web_socket_handshake_options',
      'QWebSocketHandshakeOptionsPrivate': '_q_web_socket_handshake_options_private',
      'QWebSocketHandshakeRequest': '_q_web_socket_handshake_request',
      'QWebSocketCorsAuthenticator': '_q_web_socket_cors_authenticator',
      'QWebSocketCorsAuthenticatorPrivate': '_q_web_socket_cors_authenticator_private',
      'QMaskGenerator': '_q_mask_generator',
      'QWebSocketFrame': '_q_web_socket_frame',
      'QWebSocketHandshakeResponse': '_q_web_socket_handshake_response',
      'QDefaultMaskGenerator': '_q_default_mask_generator',
      'QWebSocketDataProcessor': '_q_web_socket_data_processor',
      'QWebSocket': '_q_web_socket',
      'QWebSocketPrivate': '_q_web_socket_private',
      'QWebSocketServer': '_q_web_socket_server',
      'QWebSocketServerPrivate': '_q_web_socket_server_private',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QWebSocketProtocol',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWebSockets import QWebSocketServerPrivate'. Python calls
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
