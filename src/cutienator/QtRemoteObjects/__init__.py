"""
The 'cutienator.QtRemoteObjects' package provides the cute classes of
the part of Qt named QtRemoteObjects, under the name PySide6 has for it.

  from cutienator.QtRemoteObjects import CacheEntry, ModelInfo

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
    'CacheEntry',
    'ModelInfo',
    'ProxyReplicaInfo',
    'RequestedData',
    'RequestedHeaderData',
    'SourceApiMap',
    'QtROAssociativeContainer',
    'QtROSequentialContainer',
    'QRemoteObjectSourceLocationInfo',
    'DynamicApiMap',
    'QConnectionAbstractServer',
    'QQnxNativeServer',
    'QRegistrySource',
    'QRemoteObjectAbstractPersistedStorePrivate',
    'QRemoteObjectSourceBase',
    'QReplicaImplementationInterface',
    'QtROClientFactory',
    'QtROIoDeviceBasePrivate',
    'QtROServerFactory',
    'QRemoteObjectAbstractPersistedStore',
    'QRemoteObjectSource',
    'QStubReplicaImplementation',
    'QnxServerImpl',
    'QtROClientIoDevicePrivate',
    'QtROExternalIoDevicePrivate',
    'QtROIoDeviceBase',
    'TcpServerImpl',
    'LocalServerImpl',
    'QAbstractItemModelSourceAdapter',
    'QRemoteObjectMetaObjectManager',
    'QRemoteObjectSettingsStore',
    'QRemoteObjectSourceIo',
    'QtROExternalIoDevice',
    'QtROServerIoDevice',
    'AbstractLocalServerImpl',
    'LocalServerIo',
    'QRemoteObjectNode',
    'QRemoteObjectReplica',
    'QRemoteObjectPendingCall',
    'QRemoteObjectRegistry',
    'QRemoteObjectReplicaImplementation',
    'QConnectedReplicaImplementation',
    'QtROClientIoDevice',
    'QRemoteObjectNodePrivate',
    'QRemoteObjectPendingCallData',
    'QRemoteObjectRootSource',
    'LocalClientIo',
    'QIOQnxSource',
    'QInProcessReplicaImplementation',
    'QQnxNativeIo',
    'QRemoteObjectDynamicReplica',
    'QRemoteObjectHostBase',
    'QRemoteObjectHostBasePrivate',
    'QRemoteObjectPendingCallWatcher',
    'QnxClientIo',
    'TcpClientIo',
    'TcpServerIo',
    'AbstractLocalClientIo',
    'HeaderWatcher',
    'ProxyInfo',
    'QAbstractItemModelReplica',
    'QAbstractItemModelReplicaImplementation',
    'QRemoteObjectHostPrivate',
    'QRemoteObjectPendingCallWatcherHelper',
    'QRemoteObjectRegistryHostPrivate',
    'QnxServerIo',
    'RowWatcher',
    'SizeWatcher',
    'CacheData',
    'QRemoteObjectHost',
    'QRemoteObjectRegistryHost',
    'QRemoteObjectSourceLocations',
    'QRemoteObjectInternalTypes',
    'QRemoteObjectPackets',
    'QtPrivate',
    'QtRemoteObjects',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._cache_entry import CacheEntry
  from ._model_info import ModelInfo
  from ._proxy_replica_info import ProxyReplicaInfo
  from ._requested_data import RequestedData
  from ._requested_header_data import RequestedHeaderData
  from ._source_api_map import SourceApiMap
  from ._qt_r_o_associative_container import QtROAssociativeContainer
  from ._qt_r_o_sequential_container import QtROSequentialContainer
  from ._q_remote_object_source_location_info import QRemoteObjectSourceLocationInfo
  from ._dynamic_api_map import DynamicApiMap
  from ._q_connection_abstract_server import QConnectionAbstractServer
  from ._q_qnx_native_server import QQnxNativeServer
  from ._q_registry_source import QRegistrySource
  from ._q_remote_object_abstract_persisted_store_private import QRemoteObjectAbstractPersistedStorePrivate
  from ._q_remote_object_source_base import QRemoteObjectSourceBase
  from ._q_replica_implementation_interface import QReplicaImplementationInterface
  from ._qt_r_o_client_factory import QtROClientFactory
  from ._qt_r_o_io_device_base_private import QtROIoDeviceBasePrivate
  from ._qt_r_o_server_factory import QtROServerFactory
  from ._q_remote_object_abstract_persisted_store import QRemoteObjectAbstractPersistedStore
  from ._q_remote_object_source import QRemoteObjectSource
  from ._q_stub_replica_implementation import QStubReplicaImplementation
  from ._qnx_server_impl import QnxServerImpl
  from ._qt_r_o_client_io_device_private import QtROClientIoDevicePrivate
  from ._qt_r_o_external_io_device_private import QtROExternalIoDevicePrivate
  from ._qt_r_o_io_device_base import QtROIoDeviceBase
  from ._tcp_server_impl import TcpServerImpl
  from ._local_server_impl import LocalServerImpl
  from ._q_abstract_item_model_source_adapter import QAbstractItemModelSourceAdapter
  from ._q_remote_object_meta_object_manager import QRemoteObjectMetaObjectManager
  from ._q_remote_object_settings_store import QRemoteObjectSettingsStore
  from ._q_remote_object_source_io import QRemoteObjectSourceIo
  from ._qt_r_o_external_io_device import QtROExternalIoDevice
  from ._qt_r_o_server_io_device import QtROServerIoDevice
  from ._abstract_local_server_impl import AbstractLocalServerImpl
  from ._local_server_io import LocalServerIo
  from ._q_remote_object_node import QRemoteObjectNode
  from ._q_remote_object_replica import QRemoteObjectReplica
  from ._q_remote_object_pending_call import QRemoteObjectPendingCall
  from ._q_remote_object_registry import QRemoteObjectRegistry
  from ._q_remote_object_replica_implementation import QRemoteObjectReplicaImplementation
  from ._q_connected_replica_implementation import QConnectedReplicaImplementation
  from ._qt_r_o_client_io_device import QtROClientIoDevice
  from ._q_remote_object_node_private import QRemoteObjectNodePrivate
  from ._q_remote_object_pending_call_data import QRemoteObjectPendingCallData
  from ._q_remote_object_root_source import QRemoteObjectRootSource
  from ._local_client_io import LocalClientIo
  from ._q_i_o_qnx_source import QIOQnxSource
  from ._q_in_process_replica_implementation import QInProcessReplicaImplementation
  from ._q_qnx_native_io import QQnxNativeIo
  from ._q_remote_object_dynamic_replica import QRemoteObjectDynamicReplica
  from ._q_remote_object_host_base import QRemoteObjectHostBase
  from ._q_remote_object_host_base_private import QRemoteObjectHostBasePrivate
  from ._q_remote_object_pending_call_watcher import QRemoteObjectPendingCallWatcher
  from ._qnx_client_io import QnxClientIo
  from ._tcp_client_io import TcpClientIo
  from ._tcp_server_io import TcpServerIo
  from ._abstract_local_client_io import AbstractLocalClientIo
  from ._header_watcher import HeaderWatcher
  from ._proxy_info import ProxyInfo
  from ._q_abstract_item_model_replica import QAbstractItemModelReplica
  from ._q_abstract_item_model_replica_implementation import QAbstractItemModelReplicaImplementation
  from ._q_remote_object_host_private import QRemoteObjectHostPrivate
  from ._q_remote_object_pending_call_watcher_helper import QRemoteObjectPendingCallWatcherHelper
  from ._q_remote_object_registry_host_private import QRemoteObjectRegistryHostPrivate
  from ._qnx_server_io import QnxServerIo
  from ._row_watcher import RowWatcher
  from ._size_watcher import SizeWatcher
  from ._cache_data import CacheData
  from ._q_remote_object_host import QRemoteObjectHost
  from ._q_remote_object_registry_host import QRemoteObjectRegistryHost
  from ._q_remote_object_source_location_info import QRemoteObjectSourceLocations
  from . import QRemoteObjectInternalTypes
  from . import QRemoteObjectPackets
  from . import QtPrivate
  from . import QtRemoteObjects
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'CacheEntry': '_cache_entry',
      'ModelInfo': '_model_info',
      'ProxyReplicaInfo': '_proxy_replica_info',
      'RequestedData': '_requested_data',
      'RequestedHeaderData': '_requested_header_data',
      'SourceApiMap': '_source_api_map',
      'QtROAssociativeContainer': '_qt_r_o_associative_container',
      'QtROSequentialContainer': '_qt_r_o_sequential_container',
      'QRemoteObjectSourceLocationInfo': '_q_remote_object_source_location_info',
      'DynamicApiMap': '_dynamic_api_map',
      'QConnectionAbstractServer': '_q_connection_abstract_server',
      'QQnxNativeServer': '_q_qnx_native_server',
      'QRegistrySource': '_q_registry_source',
      'QRemoteObjectAbstractPersistedStorePrivate': '_q_remote_object_abstract_persisted_store_private',
      'QRemoteObjectSourceBase': '_q_remote_object_source_base',
      'QReplicaImplementationInterface': '_q_replica_implementation_interface',
      'QtROClientFactory': '_qt_r_o_client_factory',
      'QtROIoDeviceBasePrivate': '_qt_r_o_io_device_base_private',
      'QtROServerFactory': '_qt_r_o_server_factory',
      'QRemoteObjectAbstractPersistedStore': '_q_remote_object_abstract_persisted_store',
      'QRemoteObjectSource': '_q_remote_object_source',
      'QStubReplicaImplementation': '_q_stub_replica_implementation',
      'QnxServerImpl': '_qnx_server_impl',
      'QtROClientIoDevicePrivate': '_qt_r_o_client_io_device_private',
      'QtROExternalIoDevicePrivate': '_qt_r_o_external_io_device_private',
      'QtROIoDeviceBase': '_qt_r_o_io_device_base',
      'TcpServerImpl': '_tcp_server_impl',
      'LocalServerImpl': '_local_server_impl',
      'QAbstractItemModelSourceAdapter': '_q_abstract_item_model_source_adapter',
      'QRemoteObjectMetaObjectManager': '_q_remote_object_meta_object_manager',
      'QRemoteObjectSettingsStore': '_q_remote_object_settings_store',
      'QRemoteObjectSourceIo': '_q_remote_object_source_io',
      'QtROExternalIoDevice': '_qt_r_o_external_io_device',
      'QtROServerIoDevice': '_qt_r_o_server_io_device',
      'AbstractLocalServerImpl': '_abstract_local_server_impl',
      'LocalServerIo': '_local_server_io',
      'QRemoteObjectNode': '_q_remote_object_node',
      'QRemoteObjectReplica': '_q_remote_object_replica',
      'QRemoteObjectPendingCall': '_q_remote_object_pending_call',
      'QRemoteObjectRegistry': '_q_remote_object_registry',
      'QRemoteObjectReplicaImplementation': '_q_remote_object_replica_implementation',
      'QConnectedReplicaImplementation': '_q_connected_replica_implementation',
      'QtROClientIoDevice': '_qt_r_o_client_io_device',
      'QRemoteObjectNodePrivate': '_q_remote_object_node_private',
      'QRemoteObjectPendingCallData': '_q_remote_object_pending_call_data',
      'QRemoteObjectRootSource': '_q_remote_object_root_source',
      'LocalClientIo': '_local_client_io',
      'QIOQnxSource': '_q_i_o_qnx_source',
      'QInProcessReplicaImplementation': '_q_in_process_replica_implementation',
      'QQnxNativeIo': '_q_qnx_native_io',
      'QRemoteObjectDynamicReplica': '_q_remote_object_dynamic_replica',
      'QRemoteObjectHostBase': '_q_remote_object_host_base',
      'QRemoteObjectHostBasePrivate': '_q_remote_object_host_base_private',
      'QRemoteObjectPendingCallWatcher': '_q_remote_object_pending_call_watcher',
      'QnxClientIo': '_qnx_client_io',
      'TcpClientIo': '_tcp_client_io',
      'TcpServerIo': '_tcp_server_io',
      'AbstractLocalClientIo': '_abstract_local_client_io',
      'HeaderWatcher': '_header_watcher',
      'ProxyInfo': '_proxy_info',
      'QAbstractItemModelReplica': '_q_abstract_item_model_replica',
      'QAbstractItemModelReplicaImplementation': '_q_abstract_item_model_replica_implementation',
      'QRemoteObjectHostPrivate': '_q_remote_object_host_private',
      'QRemoteObjectPendingCallWatcherHelper': '_q_remote_object_pending_call_watcher_helper',
      'QRemoteObjectRegistryHostPrivate': '_q_remote_object_registry_host_private',
      'QnxServerIo': '_qnx_server_io',
      'RowWatcher': '_row_watcher',
      'SizeWatcher': '_size_watcher',
      'CacheData': '_cache_data',
      'QRemoteObjectHost': '_q_remote_object_host',
      'QRemoteObjectRegistryHost': '_q_remote_object_registry_host',
      'QRemoteObjectSourceLocations': '_q_remote_object_source_location_info',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QRemoteObjectInternalTypes', 'QRemoteObjectPackets', 'QtPrivate', 'QtRemoteObjects',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtRemoteObjects import QRemoteObjectSourceLocations'. Python calls
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
