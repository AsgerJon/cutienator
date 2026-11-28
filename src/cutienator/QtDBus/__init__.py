"""
The 'cutienator.QtDBus' package provides the cute classes of the part of
Qt named QtDBus, under the name PySide6 has for it.

  from cutienator.QtDBus import QDBusErrorInternal, QDBusSlotCache

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
    'QDBusErrorInternal',
    'QDBusSlotCache',
    'QDBusUnixFileDescriptor',
    'QDBusIntrospection',
    'QDBusObjectPath',
    'QDBusSignature',
    'QDBusXmlParser',
    'QDBusAbstractAdaptor',
    'QDBusConnection',
    'QDBusMessage',
    'QDBusError',
    'QDBusAbstractInterfacePrivate',
    'QDBusServer',
    'QDBusServiceWatcher',
    'QDBusAbstractInterfaceBase',
    'QDBusAbstractInterface',
    'QDBusConnectionPrivate',
    'QDBusMessagePrivate',
    'QDBusPendingCallPrivate',
    'QDBusVirtualObject',
    'QDBusVariant',
    'QDBusAbstractAdaptorPrivate',
    'QDBusActivateObjectEvent',
    'QDBusAdaptorConnector',
    'QDBusArgument',
    'QDBusArgumentPrivate',
    'QDBusCallDeliveryEvent',
    'QDBusConnectionInterface',
    'QDBusConnectionManager',
    'QDBusContext',
    'QDBusContextPrivate',
    'QDBusInterfacePrivate',
    'QDBusLockerBase',
    'QDBusMetaObject',
    'QDBusPendingCall',
    'QDBusSpyCallEvent',
    'QDBusDemarshaller',
    'QDBusInterface',
    'QDBusMetaType',
    'QDBusPendingCallWatcher',
    'QDBusPendingReplyBase',
    'QDBusReadLocker',
    'QDBusWriteLocker',
    'QDBusMarshaller',
    'QDBusPendingCallWatcherHelper',
    'ServiceDataList',
    'QDBus',
    'QDBusUtil',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_d_bus_error_internal import QDBusErrorInternal
  from ._q_d_bus_slot_cache import QDBusSlotCache
  from ._q_d_bus_unix_file_descriptor import QDBusUnixFileDescriptor
  from ._q_d_bus_introspection import QDBusIntrospection
  from ._q_d_bus_object_path import QDBusObjectPath
  from ._q_d_bus_signature import QDBusSignature
  from ._q_d_bus_xml_parser import QDBusXmlParser
  from ._q_d_bus_abstract_adaptor import QDBusAbstractAdaptor
  from ._q_d_bus_connection import QDBusConnection
  from ._q_d_bus_message import QDBusMessage
  from ._q_d_bus_error import QDBusError
  from ._q_d_bus_abstract_interface_private import QDBusAbstractInterfacePrivate
  from ._q_d_bus_server import QDBusServer
  from ._q_d_bus_service_watcher import QDBusServiceWatcher
  from ._q_d_bus_abstract_interface_base import QDBusAbstractInterfaceBase
  from ._q_d_bus_abstract_interface import QDBusAbstractInterface
  from ._q_d_bus_connection_private import QDBusConnectionPrivate
  from ._q_d_bus_message_private import QDBusMessagePrivate
  from ._q_d_bus_pending_call_private import QDBusPendingCallPrivate
  from ._q_d_bus_virtual_object import QDBusVirtualObject
  from ._q_d_bus_variant import QDBusVariant
  from ._q_d_bus_abstract_adaptor_private import QDBusAbstractAdaptorPrivate
  from ._q_d_bus_activate_object_event import QDBusActivateObjectEvent
  from ._q_d_bus_adaptor_connector import QDBusAdaptorConnector
  from ._q_d_bus_argument import QDBusArgument
  from ._q_d_bus_argument_private import QDBusArgumentPrivate
  from ._q_d_bus_call_delivery_event import QDBusCallDeliveryEvent
  from ._q_d_bus_connection_interface import QDBusConnectionInterface
  from ._q_d_bus_connection_manager import QDBusConnectionManager
  from ._q_d_bus_context import QDBusContext
  from ._q_d_bus_context_private import QDBusContextPrivate
  from ._q_d_bus_interface_private import QDBusInterfacePrivate
  from ._q_d_bus_locker_base import QDBusLockerBase
  from ._q_d_bus_meta_object import QDBusMetaObject
  from ._q_d_bus_pending_call import QDBusPendingCall
  from ._q_d_bus_spy_call_event import QDBusSpyCallEvent
  from ._q_d_bus_demarshaller import QDBusDemarshaller
  from ._q_d_bus_interface import QDBusInterface
  from ._q_d_bus_meta_type import QDBusMetaType
  from ._q_d_bus_pending_call_watcher import QDBusPendingCallWatcher
  from ._q_d_bus_pending_reply_base import QDBusPendingReplyBase
  from ._q_d_bus_read_locker import QDBusReadLocker
  from ._q_d_bus_write_locker import QDBusWriteLocker
  from ._q_d_bus_marshaller import QDBusMarshaller
  from ._q_d_bus_pending_call_watcher_helper import QDBusPendingCallWatcherHelper
  from ._q_d_bus_variant import ServiceDataList
  from . import QDBus
  from . import QDBusUtil
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QDBusErrorInternal': '_q_d_bus_error_internal',
      'QDBusSlotCache': '_q_d_bus_slot_cache',
      'QDBusUnixFileDescriptor': '_q_d_bus_unix_file_descriptor',
      'QDBusIntrospection': '_q_d_bus_introspection',
      'QDBusObjectPath': '_q_d_bus_object_path',
      'QDBusSignature': '_q_d_bus_signature',
      'QDBusXmlParser': '_q_d_bus_xml_parser',
      'QDBusAbstractAdaptor': '_q_d_bus_abstract_adaptor',
      'QDBusConnection': '_q_d_bus_connection',
      'QDBusMessage': '_q_d_bus_message',
      'QDBusError': '_q_d_bus_error',
      'QDBusAbstractInterfacePrivate': '_q_d_bus_abstract_interface_private',
      'QDBusServer': '_q_d_bus_server',
      'QDBusServiceWatcher': '_q_d_bus_service_watcher',
      'QDBusAbstractInterfaceBase': '_q_d_bus_abstract_interface_base',
      'QDBusAbstractInterface': '_q_d_bus_abstract_interface',
      'QDBusConnectionPrivate': '_q_d_bus_connection_private',
      'QDBusMessagePrivate': '_q_d_bus_message_private',
      'QDBusPendingCallPrivate': '_q_d_bus_pending_call_private',
      'QDBusVirtualObject': '_q_d_bus_virtual_object',
      'QDBusVariant': '_q_d_bus_variant',
      'QDBusAbstractAdaptorPrivate': '_q_d_bus_abstract_adaptor_private',
      'QDBusActivateObjectEvent': '_q_d_bus_activate_object_event',
      'QDBusAdaptorConnector': '_q_d_bus_adaptor_connector',
      'QDBusArgument': '_q_d_bus_argument',
      'QDBusArgumentPrivate': '_q_d_bus_argument_private',
      'QDBusCallDeliveryEvent': '_q_d_bus_call_delivery_event',
      'QDBusConnectionInterface': '_q_d_bus_connection_interface',
      'QDBusConnectionManager': '_q_d_bus_connection_manager',
      'QDBusContext': '_q_d_bus_context',
      'QDBusContextPrivate': '_q_d_bus_context_private',
      'QDBusInterfacePrivate': '_q_d_bus_interface_private',
      'QDBusLockerBase': '_q_d_bus_locker_base',
      'QDBusMetaObject': '_q_d_bus_meta_object',
      'QDBusPendingCall': '_q_d_bus_pending_call',
      'QDBusSpyCallEvent': '_q_d_bus_spy_call_event',
      'QDBusDemarshaller': '_q_d_bus_demarshaller',
      'QDBusInterface': '_q_d_bus_interface',
      'QDBusMetaType': '_q_d_bus_meta_type',
      'QDBusPendingCallWatcher': '_q_d_bus_pending_call_watcher',
      'QDBusPendingReplyBase': '_q_d_bus_pending_reply_base',
      'QDBusReadLocker': '_q_d_bus_read_locker',
      'QDBusWriteLocker': '_q_d_bus_write_locker',
      'QDBusMarshaller': '_q_d_bus_marshaller',
      'QDBusPendingCallWatcherHelper': '_q_d_bus_pending_call_watcher_helper',
      'ServiceDataList': '_q_d_bus_variant',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QDBus', 'QDBusUtil',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtDBus import ServiceDataList'. Python calls
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
