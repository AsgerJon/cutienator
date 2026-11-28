"""
The 'cutienator.QtWebEngineCore' package provides the cute classes of
the part of Qt named QtWebEngineCore, under the name PySide6 has for it.

  from cutienator.QtWebEngineCore import QWebEngineContextMenuRequestPrivate, QWebEngineGlobalSettingsPrivate

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
    'QWebEngineContextMenuRequestPrivate',
    'QWebEngineGlobalSettingsPrivate',
    'QWebEngineNewWindowRequestPrivate',
    'QWebEngineProfileBuilderPrivate',
    'QWebEngineWebAuthUxRequestPrivate',
    'QWebEngineExtensionInfoPrivate',
    'QWebEngineHistoryItemPrivate',
    'QWebEngineHistoryItem',
    'QWebEngineSettings',
    'QWebEngineHistoryPrivate',
    'QWebEngineHttpRequest',
    'QWebEngineUrlRequestInfo',
    'QWebEngineUrlRequestInfoPrivate',
    'QWebEngineCertificateError',
    'QWebEngineClientHints',
    'QWebEngineContextMenuRequest',
    'QWebEngineDesktopMediaRequest',
    'QWebEngineDesktopMediaRequestPrivate',
    'QWebEngineDownloadRequest',
    'QWebEngineExtensionInfo',
    'QWebEngineFileSystemAccessRequest',
    'QWebEngineFindTextResult',
    'QWebEngineFullScreenRequest',
    'QWebEngineHistory',
    'QWebEngineHistoryModelPrivate',
    'QWebEngineLoadingInfo',
    'QWebEngineMessagePumpScheduler',
    'QWebEngineNavigationRequest',
    'QWebEngineNotification',
    'QWebEnginePermission',
    'QWebEnginePermissionPrivate',
    'QWebEngineQuotaRequest',
    'QWebEngineRegisterProtocolHandlerRequest',
    'QWebEngineScript',
    'QWebEngineUrlRequestInterceptor',
    'QWebEngineUrlRequestJob',
    'QWebEngineUrlScheme',
    'QWebEngineWebAuthPinRequest',
    'QWebEngineWebAuthUxRequest',
    'QWebEngineBackHistoryModelPrivate',
    'QWebEngineCookieStore',
    'QWebEngineExtensionManager',
    'QWebEngineForwardHistoryModelPrivate',
    'QWebEngineHistoryModel',
    'QWebEngineScriptCollection',
    'QWebEngineUrlSchemeHandler',
    'QWebEngineClientCertificateSelection',
    'QWebEngineClientCertificateStore',
    'QWebEngineCookieStorePrivate',
    'QWebEngineProfile',
    'QWebEngineFrame',
    'QWebEngineProfileBuilder',
    'QWebEngineNewWindowRequest',
    'QWebEnginePage',
    'QWebEngineGlobalSettings',
    'QtWebEngineCore',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_web_engine_context_menu_request_private import QWebEngineContextMenuRequestPrivate
  from ._q_web_engine_global_settings_private import QWebEngineGlobalSettingsPrivate
  from ._q_web_engine_new_window_request_private import QWebEngineNewWindowRequestPrivate
  from ._q_web_engine_profile_builder_private import QWebEngineProfileBuilderPrivate
  from ._q_web_engine_web_auth_ux_request_private import QWebEngineWebAuthUxRequestPrivate
  from ._q_web_engine_extension_info_private import QWebEngineExtensionInfoPrivate
  from ._q_web_engine_history_item_private import QWebEngineHistoryItemPrivate
  from ._q_web_engine_history_item import QWebEngineHistoryItem
  from ._q_web_engine_settings import QWebEngineSettings
  from ._q_web_engine_history_private import QWebEngineHistoryPrivate
  from ._q_web_engine_http_request import QWebEngineHttpRequest
  from ._q_web_engine_url_request_info import QWebEngineUrlRequestInfo
  from ._q_web_engine_url_request_info_private import QWebEngineUrlRequestInfoPrivate
  from ._q_web_engine_certificate_error import QWebEngineCertificateError
  from ._q_web_engine_client_hints import QWebEngineClientHints
  from ._q_web_engine_context_menu_request import QWebEngineContextMenuRequest
  from ._q_web_engine_desktop_media_request import QWebEngineDesktopMediaRequest
  from ._q_web_engine_desktop_media_request_private import QWebEngineDesktopMediaRequestPrivate
  from ._q_web_engine_download_request import QWebEngineDownloadRequest
  from ._q_web_engine_extension_info import QWebEngineExtensionInfo
  from ._q_web_engine_file_system_access_request import QWebEngineFileSystemAccessRequest
  from ._q_web_engine_find_text_result import QWebEngineFindTextResult
  from ._q_web_engine_full_screen_request import QWebEngineFullScreenRequest
  from ._q_web_engine_history import QWebEngineHistory
  from ._q_web_engine_history_model_private import QWebEngineHistoryModelPrivate
  from ._q_web_engine_loading_info import QWebEngineLoadingInfo
  from ._q_web_engine_message_pump_scheduler import QWebEngineMessagePumpScheduler
  from ._q_web_engine_navigation_request import QWebEngineNavigationRequest
  from ._q_web_engine_notification import QWebEngineNotification
  from ._q_web_engine_permission import QWebEnginePermission
  from ._q_web_engine_permission_private import QWebEnginePermissionPrivate
  from ._q_web_engine_quota_request import QWebEngineQuotaRequest
  from ._q_web_engine_register_protocol_handler_request import QWebEngineRegisterProtocolHandlerRequest
  from ._q_web_engine_script import QWebEngineScript
  from ._q_web_engine_url_request_interceptor import QWebEngineUrlRequestInterceptor
  from ._q_web_engine_url_request_job import QWebEngineUrlRequestJob
  from ._q_web_engine_url_scheme import QWebEngineUrlScheme
  from ._q_web_engine_web_auth_pin_request import QWebEngineWebAuthPinRequest
  from ._q_web_engine_web_auth_ux_request import QWebEngineWebAuthUxRequest
  from ._q_web_engine_back_history_model_private import QWebEngineBackHistoryModelPrivate
  from ._q_web_engine_cookie_store import QWebEngineCookieStore
  from ._q_web_engine_extension_manager import QWebEngineExtensionManager
  from ._q_web_engine_forward_history_model_private import QWebEngineForwardHistoryModelPrivate
  from ._q_web_engine_history_model import QWebEngineHistoryModel
  from ._q_web_engine_script_collection import QWebEngineScriptCollection
  from ._q_web_engine_url_scheme_handler import QWebEngineUrlSchemeHandler
  from ._q_web_engine_client_certificate_selection import QWebEngineClientCertificateSelection
  from ._q_web_engine_client_certificate_store import QWebEngineClientCertificateStore
  from ._q_web_engine_cookie_store_private import QWebEngineCookieStorePrivate
  from ._q_web_engine_profile import QWebEngineProfile
  from ._q_web_engine_frame import QWebEngineFrame
  from ._q_web_engine_profile_builder import QWebEngineProfileBuilder
  from ._q_web_engine_new_window_request import QWebEngineNewWindowRequest
  from ._q_web_engine_page import QWebEnginePage
  from . import QWebEngineGlobalSettings
  from . import QtWebEngineCore
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QWebEngineContextMenuRequestPrivate': '_q_web_engine_context_menu_request_private',
      'QWebEngineGlobalSettingsPrivate': '_q_web_engine_global_settings_private',
      'QWebEngineNewWindowRequestPrivate': '_q_web_engine_new_window_request_private',
      'QWebEngineProfileBuilderPrivate': '_q_web_engine_profile_builder_private',
      'QWebEngineWebAuthUxRequestPrivate': '_q_web_engine_web_auth_ux_request_private',
      'QWebEngineExtensionInfoPrivate': '_q_web_engine_extension_info_private',
      'QWebEngineHistoryItemPrivate': '_q_web_engine_history_item_private',
      'QWebEngineHistoryItem': '_q_web_engine_history_item',
      'QWebEngineSettings': '_q_web_engine_settings',
      'QWebEngineHistoryPrivate': '_q_web_engine_history_private',
      'QWebEngineHttpRequest': '_q_web_engine_http_request',
      'QWebEngineUrlRequestInfo': '_q_web_engine_url_request_info',
      'QWebEngineUrlRequestInfoPrivate': '_q_web_engine_url_request_info_private',
      'QWebEngineCertificateError': '_q_web_engine_certificate_error',
      'QWebEngineClientHints': '_q_web_engine_client_hints',
      'QWebEngineContextMenuRequest': '_q_web_engine_context_menu_request',
      'QWebEngineDesktopMediaRequest': '_q_web_engine_desktop_media_request',
      'QWebEngineDesktopMediaRequestPrivate': '_q_web_engine_desktop_media_request_private',
      'QWebEngineDownloadRequest': '_q_web_engine_download_request',
      'QWebEngineExtensionInfo': '_q_web_engine_extension_info',
      'QWebEngineFileSystemAccessRequest': '_q_web_engine_file_system_access_request',
      'QWebEngineFindTextResult': '_q_web_engine_find_text_result',
      'QWebEngineFullScreenRequest': '_q_web_engine_full_screen_request',
      'QWebEngineHistory': '_q_web_engine_history',
      'QWebEngineHistoryModelPrivate': '_q_web_engine_history_model_private',
      'QWebEngineLoadingInfo': '_q_web_engine_loading_info',
      'QWebEngineMessagePumpScheduler': '_q_web_engine_message_pump_scheduler',
      'QWebEngineNavigationRequest': '_q_web_engine_navigation_request',
      'QWebEngineNotification': '_q_web_engine_notification',
      'QWebEnginePermission': '_q_web_engine_permission',
      'QWebEnginePermissionPrivate': '_q_web_engine_permission_private',
      'QWebEngineQuotaRequest': '_q_web_engine_quota_request',
      'QWebEngineRegisterProtocolHandlerRequest': '_q_web_engine_register_protocol_handler_request',
      'QWebEngineScript': '_q_web_engine_script',
      'QWebEngineUrlRequestInterceptor': '_q_web_engine_url_request_interceptor',
      'QWebEngineUrlRequestJob': '_q_web_engine_url_request_job',
      'QWebEngineUrlScheme': '_q_web_engine_url_scheme',
      'QWebEngineWebAuthPinRequest': '_q_web_engine_web_auth_pin_request',
      'QWebEngineWebAuthUxRequest': '_q_web_engine_web_auth_ux_request',
      'QWebEngineBackHistoryModelPrivate': '_q_web_engine_back_history_model_private',
      'QWebEngineCookieStore': '_q_web_engine_cookie_store',
      'QWebEngineExtensionManager': '_q_web_engine_extension_manager',
      'QWebEngineForwardHistoryModelPrivate': '_q_web_engine_forward_history_model_private',
      'QWebEngineHistoryModel': '_q_web_engine_history_model',
      'QWebEngineScriptCollection': '_q_web_engine_script_collection',
      'QWebEngineUrlSchemeHandler': '_q_web_engine_url_scheme_handler',
      'QWebEngineClientCertificateSelection': '_q_web_engine_client_certificate_selection',
      'QWebEngineClientCertificateStore': '_q_web_engine_client_certificate_store',
      'QWebEngineCookieStorePrivate': '_q_web_engine_cookie_store_private',
      'QWebEngineProfile': '_q_web_engine_profile',
      'QWebEngineFrame': '_q_web_engine_frame',
      'QWebEngineProfileBuilder': '_q_web_engine_profile_builder',
      'QWebEngineNewWindowRequest': '_q_web_engine_new_window_request',
      'QWebEnginePage': '_q_web_engine_page',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QWebEngineGlobalSettings', 'QtWebEngineCore',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtWebEngineCore import QWebEnginePage'. Python calls
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
