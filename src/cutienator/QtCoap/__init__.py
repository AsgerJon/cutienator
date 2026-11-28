"""
The 'cutienator.QtCoap' package provides the cute classes of the part of
Qt named QtCoap, under the name PySide6 has for it.

  from cutienator.QtCoap import CoapExchangeData, QCoapResourcePrivate

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
    'CoapExchangeData',
    'QCoapResourcePrivate',
    'QCoapPrivateKey',
    'CoapFrame',
    'QCoapOption',
    'QCoapOptionPrivate',
    'QCoapMessage',
    'QCoapMessagePrivate',
    'QCoapConnectionPrivate',
    'QCoapInternalMessagePrivate',
    'QCoapRequest',
    'QCoapInternalMessage',
    'QCoapInternalReplyPrivate',
    'QCoapInternalRequestPrivate',
    'QCoapReplyPrivate',
    'QCoapRequestPrivate',
    'QCoapResource',
    'QCoapInternalReply',
    'QCoapReply',
    'QCoapResourceDiscoveryReplyPrivate',
    'QCoapSecurityConfiguration',
    'QCoapResourceDiscoveryReply',
    'QCoapClient',
    'QCoapConnection',
    'QCoapQUdpConnectionPrivate',
    'QCoapInternalRequest',
    'QCoapProtocol',
    'QCoapQUdpConnection',
    'QCoapClientPrivate',
    'QCoapProtocolPrivate',
    'QtCoap',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._coap_exchange_data import CoapExchangeData
  from ._q_coap_resource_private import QCoapResourcePrivate
  from ._q_coap_private_key import QCoapPrivateKey
  from ._coap_frame import CoapFrame
  from ._q_coap_option import QCoapOption
  from ._q_coap_option_private import QCoapOptionPrivate
  from ._q_coap_message import QCoapMessage
  from ._q_coap_message_private import QCoapMessagePrivate
  from ._q_coap_connection_private import QCoapConnectionPrivate
  from ._q_coap_internal_message_private import QCoapInternalMessagePrivate
  from ._q_coap_request import QCoapRequest
  from ._q_coap_internal_message import QCoapInternalMessage
  from ._q_coap_internal_reply_private import QCoapInternalReplyPrivate
  from ._q_coap_internal_request_private import QCoapInternalRequestPrivate
  from ._q_coap_reply_private import QCoapReplyPrivate
  from ._q_coap_request_private import QCoapRequestPrivate
  from ._q_coap_resource import QCoapResource
  from ._q_coap_internal_reply import QCoapInternalReply
  from ._q_coap_reply import QCoapReply
  from ._q_coap_resource_discovery_reply_private import QCoapResourceDiscoveryReplyPrivate
  from ._q_coap_security_configuration import QCoapSecurityConfiguration
  from ._q_coap_resource_discovery_reply import QCoapResourceDiscoveryReply
  from ._q_coap_client import QCoapClient
  from ._q_coap_connection import QCoapConnection
  from ._q_coap_q_udp_connection_private import QCoapQUdpConnectionPrivate
  from ._q_coap_internal_request import QCoapInternalRequest
  from ._q_coap_protocol import QCoapProtocol
  from ._q_coap_q_udp_connection import QCoapQUdpConnection
  from ._q_coap_client_private import QCoapClientPrivate
  from ._q_coap_protocol_private import QCoapProtocolPrivate
  from . import QtCoap
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'CoapExchangeData': '_coap_exchange_data',
      'QCoapResourcePrivate': '_q_coap_resource_private',
      'QCoapPrivateKey': '_q_coap_private_key',
      'CoapFrame': '_coap_frame',
      'QCoapOption': '_q_coap_option',
      'QCoapOptionPrivate': '_q_coap_option_private',
      'QCoapMessage': '_q_coap_message',
      'QCoapMessagePrivate': '_q_coap_message_private',
      'QCoapConnectionPrivate': '_q_coap_connection_private',
      'QCoapInternalMessagePrivate': '_q_coap_internal_message_private',
      'QCoapRequest': '_q_coap_request',
      'QCoapInternalMessage': '_q_coap_internal_message',
      'QCoapInternalReplyPrivate': '_q_coap_internal_reply_private',
      'QCoapInternalRequestPrivate': '_q_coap_internal_request_private',
      'QCoapReplyPrivate': '_q_coap_reply_private',
      'QCoapRequestPrivate': '_q_coap_request_private',
      'QCoapResource': '_q_coap_resource',
      'QCoapInternalReply': '_q_coap_internal_reply',
      'QCoapReply': '_q_coap_reply',
      'QCoapResourceDiscoveryReplyPrivate': '_q_coap_resource_discovery_reply_private',
      'QCoapSecurityConfiguration': '_q_coap_security_configuration',
      'QCoapResourceDiscoveryReply': '_q_coap_resource_discovery_reply',
      'QCoapClient': '_q_coap_client',
      'QCoapConnection': '_q_coap_connection',
      'QCoapQUdpConnectionPrivate': '_q_coap_q_udp_connection_private',
      'QCoapInternalRequest': '_q_coap_internal_request',
      'QCoapProtocol': '_q_coap_protocol',
      'QCoapQUdpConnection': '_q_coap_q_udp_connection',
      'QCoapClientPrivate': '_q_coap_client_private',
      'QCoapProtocolPrivate': '_q_coap_protocol_private',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtCoap',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtCoap import QCoapProtocolPrivate'. Python calls
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
