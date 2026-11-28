"""
The 'cutienator.QtWebEngineQuick' package provides the cute classes of
the part of Qt named QtWebEngineQuick, under the name PySide6 has for
it.

  from cutienator.QtWebEngineQuick import QQuickWebEngineTouchSelectionMenuRequestPrivate, ForeginWebEngineFileSystemAccessRequest

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
    'QQuickWebEngineTouchSelectionMenuRequestPrivate',
    'ForeginWebEngineFileSystemAccessRequest',
    'ForeginWebEngineWebAuthPinRequest',
    'ForeignWebEngineCertificateError',
    'ForeignWebEngineClientHints',
    'ForeignWebEngineContextMenuRequest',
    'ForeignWebEngineDesktopMediaRequest',
    'ForeignWebEngineExtensionInfo',
    'ForeignWebEngineExtensionManager',
    'ForeignWebEngineFindTextResult',
    'ForeignWebEngineFullScreenRequest',
    'ForeignWebEngineHistory',
    'ForeignWebEngineHistoryModel',
    'ForeignWebEngineLoadingInfo',
    'ForeignWebEngineNavigationRequest',
    'ForeignWebEngineNotification',
    'ForeignWebEnginePermission',
    'ForeignWebEngineQuotaRequest',
    'ForeignWebEngineRegisterProtocolHandlerRequest',
    'ForeignWebEngineScript',
    'ForeignWebEngineWebAuthUxRequest',
    'QQuickWebEngineAction',
    'QQuickWebEngineActionPrivate',
    'QQuickWebEngineAuthenticationDialogRequest',
    'QQuickWebEngineClientCertificateOption',
    'QQuickWebEngineClientCertificateSelection',
    'QQuickWebEngineColorDialogRequest',
    'QQuickWebEngineFileDialogRequest',
    'QQuickWebEngineJavaScriptDialogRequest',
    'QQuickWebEngineSettings',
    'QQuickWebEngineSingleton',
    'QQuickWebEngineTooltipRequest',
    'QQuickWebEngineTouchSelectionMenuRequest',
    'QQuickWebEngineDownloadRequest',
    'QWebEngineCertificateErrorDerived',
    'QWebEngineFileSystemAccessRequestDerived',
    'QWebEngineLoadingInfoDerived',
    'QWebEnginePermissionDerived',
    'QWebEngineScriptDerived',
    'FaviconImageResponse',
    'QQuickWebEngineProfile',
    'QQuickWebEngineScriptCollection',
    'QQuickWebEngineTouchHandleProvider',
    'QQuickWebEngineFaviconProvider',
    'QQuickWebEngineProfilePrototype',
    'QQuickWebEngineFaviconDBProvider',
    'QQuickWebEngineFrame',
    'QQuickWebEngineNewWindowRequest',
    'QQuickWebEngineView',
    'FaviconImageRequester',
    'FaviconProviderHelper',
    'QQuickWebEngineViewAccessible',
    'QtWebEngineCore',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_web_engine_touch_selection_menu_request_private import QQuickWebEngineTouchSelectionMenuRequestPrivate
  from ._foregin_web_engine_file_system_access_request import ForeginWebEngineFileSystemAccessRequest
  from ._foregin_web_engine_web_auth_pin_request import ForeginWebEngineWebAuthPinRequest
  from ._foreign_web_engine_certificate_error import ForeignWebEngineCertificateError
  from ._foreign_web_engine_client_hints import ForeignWebEngineClientHints
  from ._foreign_web_engine_context_menu_request import ForeignWebEngineContextMenuRequest
  from ._foreign_web_engine_desktop_media_request import ForeignWebEngineDesktopMediaRequest
  from ._foreign_web_engine_extension_info import ForeignWebEngineExtensionInfo
  from ._foreign_web_engine_extension_manager import ForeignWebEngineExtensionManager
  from ._foreign_web_engine_find_text_result import ForeignWebEngineFindTextResult
  from ._foreign_web_engine_full_screen_request import ForeignWebEngineFullScreenRequest
  from ._foreign_web_engine_history import ForeignWebEngineHistory
  from ._foreign_web_engine_history_model import ForeignWebEngineHistoryModel
  from ._foreign_web_engine_loading_info import ForeignWebEngineLoadingInfo
  from ._foreign_web_engine_navigation_request import ForeignWebEngineNavigationRequest
  from ._foreign_web_engine_notification import ForeignWebEngineNotification
  from ._foreign_web_engine_permission import ForeignWebEnginePermission
  from ._foreign_web_engine_quota_request import ForeignWebEngineQuotaRequest
  from ._foreign_web_engine_register_protocol_handler_request import ForeignWebEngineRegisterProtocolHandlerRequest
  from ._foreign_web_engine_script import ForeignWebEngineScript
  from ._foreign_web_engine_web_auth_ux_request import ForeignWebEngineWebAuthUxRequest
  from ._q_quick_web_engine_action import QQuickWebEngineAction
  from ._q_quick_web_engine_action_private import QQuickWebEngineActionPrivate
  from ._q_quick_web_engine_authentication_dialog_request import QQuickWebEngineAuthenticationDialogRequest
  from ._q_quick_web_engine_client_certificate_option import QQuickWebEngineClientCertificateOption
  from ._q_quick_web_engine_client_certificate_selection import QQuickWebEngineClientCertificateSelection
  from ._q_quick_web_engine_color_dialog_request import QQuickWebEngineColorDialogRequest
  from ._q_quick_web_engine_file_dialog_request import QQuickWebEngineFileDialogRequest
  from ._q_quick_web_engine_java_script_dialog_request import QQuickWebEngineJavaScriptDialogRequest
  from ._q_quick_web_engine_settings import QQuickWebEngineSettings
  from ._q_quick_web_engine_singleton import QQuickWebEngineSingleton
  from ._q_quick_web_engine_tooltip_request import QQuickWebEngineTooltipRequest
  from ._q_quick_web_engine_touch_selection_menu_request import QQuickWebEngineTouchSelectionMenuRequest
  from ._q_quick_web_engine_download_request import QQuickWebEngineDownloadRequest
  from ._q_web_engine_certificate_error_derived import QWebEngineCertificateErrorDerived
  from ._q_web_engine_file_system_access_request_derived import QWebEngineFileSystemAccessRequestDerived
  from ._q_web_engine_loading_info_derived import QWebEngineLoadingInfoDerived
  from ._q_web_engine_permission_derived import QWebEnginePermissionDerived
  from ._q_web_engine_script_derived import QWebEngineScriptDerived
  from ._favicon_image_response import FaviconImageResponse
  from ._q_quick_web_engine_profile import QQuickWebEngineProfile
  from ._q_quick_web_engine_script_collection import QQuickWebEngineScriptCollection
  from ._q_quick_web_engine_touch_handle_provider import QQuickWebEngineTouchHandleProvider
  from ._q_quick_web_engine_favicon_provider import QQuickWebEngineFaviconProvider
  from ._q_quick_web_engine_profile_prototype import QQuickWebEngineProfilePrototype
  from ._q_quick_web_engine_favicon_d_b_provider import QQuickWebEngineFaviconDBProvider
  from ._q_quick_web_engine_frame import QQuickWebEngineFrame
  from ._q_quick_web_engine_new_window_request import QQuickWebEngineNewWindowRequest
  from ._q_quick_web_engine_view import QQuickWebEngineView
  from ._favicon_image_requester import FaviconImageRequester
  from ._favicon_provider_helper import FaviconProviderHelper
  from ._q_quick_web_engine_view_accessible import QQuickWebEngineViewAccessible
  from . import QtWebEngineCore
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickWebEngineTouchSelectionMenuRequestPrivate': '_q_quick_web_engine_touch_selection_menu_request_private',
      'ForeginWebEngineFileSystemAccessRequest': '_foregin_web_engine_file_system_access_request',
      'ForeginWebEngineWebAuthPinRequest': '_foregin_web_engine_web_auth_pin_request',
      'ForeignWebEngineCertificateError': '_foreign_web_engine_certificate_error',
      'ForeignWebEngineClientHints': '_foreign_web_engine_client_hints',
      'ForeignWebEngineContextMenuRequest': '_foreign_web_engine_context_menu_request',
      'ForeignWebEngineDesktopMediaRequest': '_foreign_web_engine_desktop_media_request',
      'ForeignWebEngineExtensionInfo': '_foreign_web_engine_extension_info',
      'ForeignWebEngineExtensionManager': '_foreign_web_engine_extension_manager',
      'ForeignWebEngineFindTextResult': '_foreign_web_engine_find_text_result',
      'ForeignWebEngineFullScreenRequest': '_foreign_web_engine_full_screen_request',
      'ForeignWebEngineHistory': '_foreign_web_engine_history',
      'ForeignWebEngineHistoryModel': '_foreign_web_engine_history_model',
      'ForeignWebEngineLoadingInfo': '_foreign_web_engine_loading_info',
      'ForeignWebEngineNavigationRequest': '_foreign_web_engine_navigation_request',
      'ForeignWebEngineNotification': '_foreign_web_engine_notification',
      'ForeignWebEnginePermission': '_foreign_web_engine_permission',
      'ForeignWebEngineQuotaRequest': '_foreign_web_engine_quota_request',
      'ForeignWebEngineRegisterProtocolHandlerRequest': '_foreign_web_engine_register_protocol_handler_request',
      'ForeignWebEngineScript': '_foreign_web_engine_script',
      'ForeignWebEngineWebAuthUxRequest': '_foreign_web_engine_web_auth_ux_request',
      'QQuickWebEngineAction': '_q_quick_web_engine_action',
      'QQuickWebEngineActionPrivate': '_q_quick_web_engine_action_private',
      'QQuickWebEngineAuthenticationDialogRequest': '_q_quick_web_engine_authentication_dialog_request',
      'QQuickWebEngineClientCertificateOption': '_q_quick_web_engine_client_certificate_option',
      'QQuickWebEngineClientCertificateSelection': '_q_quick_web_engine_client_certificate_selection',
      'QQuickWebEngineColorDialogRequest': '_q_quick_web_engine_color_dialog_request',
      'QQuickWebEngineFileDialogRequest': '_q_quick_web_engine_file_dialog_request',
      'QQuickWebEngineJavaScriptDialogRequest': '_q_quick_web_engine_java_script_dialog_request',
      'QQuickWebEngineSettings': '_q_quick_web_engine_settings',
      'QQuickWebEngineSingleton': '_q_quick_web_engine_singleton',
      'QQuickWebEngineTooltipRequest': '_q_quick_web_engine_tooltip_request',
      'QQuickWebEngineTouchSelectionMenuRequest': '_q_quick_web_engine_touch_selection_menu_request',
      'QQuickWebEngineDownloadRequest': '_q_quick_web_engine_download_request',
      'QWebEngineCertificateErrorDerived': '_q_web_engine_certificate_error_derived',
      'QWebEngineFileSystemAccessRequestDerived': '_q_web_engine_file_system_access_request_derived',
      'QWebEngineLoadingInfoDerived': '_q_web_engine_loading_info_derived',
      'QWebEnginePermissionDerived': '_q_web_engine_permission_derived',
      'QWebEngineScriptDerived': '_q_web_engine_script_derived',
      'FaviconImageResponse': '_favicon_image_response',
      'QQuickWebEngineProfile': '_q_quick_web_engine_profile',
      'QQuickWebEngineScriptCollection': '_q_quick_web_engine_script_collection',
      'QQuickWebEngineTouchHandleProvider': '_q_quick_web_engine_touch_handle_provider',
      'QQuickWebEngineFaviconProvider': '_q_quick_web_engine_favicon_provider',
      'QQuickWebEngineProfilePrototype': '_q_quick_web_engine_profile_prototype',
      'QQuickWebEngineFaviconDBProvider': '_q_quick_web_engine_favicon_d_b_provider',
      'QQuickWebEngineFrame': '_q_quick_web_engine_frame',
      'QQuickWebEngineNewWindowRequest': '_q_quick_web_engine_new_window_request',
      'QQuickWebEngineView': '_q_quick_web_engine_view',
      'FaviconImageRequester': '_favicon_image_requester',
      'FaviconProviderHelper': '_favicon_provider_helper',
      'QQuickWebEngineViewAccessible': '_q_quick_web_engine_view_accessible',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtWebEngineCore',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWebEngineQuick import QQuickWebEngineViewAccessible'. Python calls
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
