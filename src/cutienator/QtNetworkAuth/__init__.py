"""
The 'cutienator.QtNetworkAuth' package provides the cute classes of the
part of Qt named QtNetworkAuth, under the name PySide6 has for it.

  from cutienator.QtNetworkAuth import QOAuth1Signature, QOAuthOobReplyHandlerPrivate

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
    'QOAuth1Signature',
    'QOAuthOobReplyHandlerPrivate',
    'QOAuth1SignaturePrivate',
    'QOAuthUriSchemeReplyHandlerPrivate',
    'QAbstractOAuth',
    'QAbstractOAuthPrivate',
    'QAbstractOAuthReplyHandler',
    'QAbstractOAuth2Private',
    'QOAuth1',
    'QOAuth1Private',
    'QOAuthOobReplyHandler',
    'QAbstractOAuth2',
    'QOAuth2AuthorizationCodeFlowPrivate',
    'QOAuth2DeviceAuthorizationFlowPrivate',
    'QOAuthHttpServerReplyHandler',
    'QOAuthUriSchemeReplyHandler',
    'QOAuth2AuthorizationCodeFlow',
    'QOAuth2DeviceAuthorizationFlow',
    'QOAuthHttpServerReplyHandlerPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_o_auth1_signature import QOAuth1Signature
  from ._q_o_auth_oob_reply_handler_private import QOAuthOobReplyHandlerPrivate
  from ._q_o_auth1_signature_private import QOAuth1SignaturePrivate
  from ._q_o_auth_uri_scheme_reply_handler_private import QOAuthUriSchemeReplyHandlerPrivate
  from ._q_abstract_o_auth import QAbstractOAuth
  from ._q_abstract_o_auth_private import QAbstractOAuthPrivate
  from ._q_abstract_o_auth_reply_handler import QAbstractOAuthReplyHandler
  from ._q_abstract_o_auth2_private import QAbstractOAuth2Private
  from ._q_o_auth1 import QOAuth1
  from ._q_o_auth1_private import QOAuth1Private
  from ._q_o_auth_oob_reply_handler import QOAuthOobReplyHandler
  from ._q_abstract_o_auth2 import QAbstractOAuth2
  from ._q_o_auth2_authorization_code_flow_private import QOAuth2AuthorizationCodeFlowPrivate
  from ._q_o_auth2_device_authorization_flow_private import QOAuth2DeviceAuthorizationFlowPrivate
  from ._q_o_auth_http_server_reply_handler import QOAuthHttpServerReplyHandler
  from ._q_o_auth_uri_scheme_reply_handler import QOAuthUriSchemeReplyHandler
  from ._q_o_auth2_authorization_code_flow import QOAuth2AuthorizationCodeFlow
  from ._q_o_auth2_device_authorization_flow import QOAuth2DeviceAuthorizationFlow
  from ._q_o_auth_http_server_reply_handler_private import QOAuthHttpServerReplyHandlerPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QOAuth1Signature': '_q_o_auth1_signature',
      'QOAuthOobReplyHandlerPrivate': '_q_o_auth_oob_reply_handler_private',
      'QOAuth1SignaturePrivate': '_q_o_auth1_signature_private',
      'QOAuthUriSchemeReplyHandlerPrivate': '_q_o_auth_uri_scheme_reply_handler_private',
      'QAbstractOAuth': '_q_abstract_o_auth',
      'QAbstractOAuthPrivate': '_q_abstract_o_auth_private',
      'QAbstractOAuthReplyHandler': '_q_abstract_o_auth_reply_handler',
      'QAbstractOAuth2Private': '_q_abstract_o_auth2_private',
      'QOAuth1': '_q_o_auth1',
      'QOAuth1Private': '_q_o_auth1_private',
      'QOAuthOobReplyHandler': '_q_o_auth_oob_reply_handler',
      'QAbstractOAuth2': '_q_abstract_o_auth2',
      'QOAuth2AuthorizationCodeFlowPrivate': '_q_o_auth2_authorization_code_flow_private',
      'QOAuth2DeviceAuthorizationFlowPrivate': '_q_o_auth2_device_authorization_flow_private',
      'QOAuthHttpServerReplyHandler': '_q_o_auth_http_server_reply_handler',
      'QOAuthUriSchemeReplyHandler': '_q_o_auth_uri_scheme_reply_handler',
      'QOAuth2AuthorizationCodeFlow': '_q_o_auth2_authorization_code_flow',
      'QOAuth2DeviceAuthorizationFlow': '_q_o_auth2_device_authorization_flow',
      'QOAuthHttpServerReplyHandlerPrivate': '_q_o_auth_http_server_reply_handler_private',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtNetworkAuth import QOAuthHttpServerReplyHandlerPrivate'. Python calls
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
