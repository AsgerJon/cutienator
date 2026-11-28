"""
The namespace 'Qt3DCore' of Qt, a package of 'cutienator.Qt3DCore':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DCore import Qt3DCore
  Qt3DCore.AlignedAllocator

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'AlignedAllocator',
    'BoundingVolumeCalculator',
    'BoundingVolumeComputeData',
    'BoundingVolumeComputeResult',
    'BoundingVolumeJobProcessor',
    'BufferInfo',
    'ComponentRelationshipChange',
    'JobId',
    'JointNamesAndLocalPoses',
    'NodeTreeChange',
    'QAbstractFrontEndNodeManager',
    'QAbstractFunctor',
    'QAbstractNodeFactory',
    'QArmatureData',
    'QAspectJob',
    'QAspectJobPrivate',
    'QAspectJobProviderInterface',
    'QBackendNode',
    'QBackendNodeMapper',
    'QBackendNodePrivate',
    'QBufferUpdate',
    'QDestructionIdAndTypeCollector',
    'QJointData',
    'QNodeId',
    'QNodeVisitor',
    'QServiceLocator',
    'QSkeletonData',
    'QSkeletonLoaderData',
    'QTaskLogger',
    'QTickClock',
    'QTransformData',
    'Sqt',
    'CalculateBoundingVolumeJob',
    'CoreSettingsFunctor',
    'QGeometryFactory',
    'QScene',
    'RunnableInterface',
    'AspectTaskRunnable',
    'SyncTaskRunnable',
    'QDownloadRequest',
    'QUrlHelper',
    'NodePostConstructorInit',
    'PropertyChangeHandlerBase',
    'QAbstractAspect',
    'QAbstractAspectJobManager',
    'QAbstractAspectPrivate',
    'QAbstractServiceProvider',
    'QAbstractServiceProviderPrivate',
    'QAspectEngine',
    'QAspectEnginePrivate',
    'QAspectFactory',
    'QChangeArbiter',
    'QNode',
    'QNodeIdTypePair',
    'QNodePrivate',
    'QScheduler',
    'QThreadPooler',
    'CoreSettings',
    'QAbstractFrameAdvanceService',
    'QAbstractFrameAdvanceServicePrivate',
    'QAbstractSkeleton',
    'QAbstractSkeletonPrivate',
    'QAspectJobManager',
    'QAttribute',
    'QAttributePrivate',
    'QBuffer',
    'QBufferPrivate',
    'QComponent',
    'QComponentPrivate',
    'QCoreAspect',
    'QCoreAspectPrivate',
    'QDownloadHelperService',
    'QEntity',
    'QEntityPrivate',
    'QEventFilterService',
    'QGeometryView',
    'QGeometryViewPrivate',
    'QJointPrivate',
    'QOpenGLInformationService',
    'QOpenGLInformationServicePrivate',
    'QSystemInformationService',
    'QSystemInformationServicePrivate',
    'NullOpenGLInformationService',
    'QArmature',
    'QArmaturePrivate',
    'QAspectManager',
    'QCoreSettings',
    'QCoreSettingsPrivate',
    'QSkeletonLoaderPrivate',
    'QSkeletonPrivate',
    'QTickClockService',
    'QBoundingVolume',
    'QBoundingVolumePrivate',
    'QGeometry',
    'QGeometryPrivate',
    'QJoint',
    'QTransform',
    'QTransformPrivate',
    'QSkeleton',
    'QSkeletonLoader',
    'QDownloadNetworkWorker',
    'Debug',
    'JobTypes',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt3_d_core__aligned_allocator import AlignedAllocator
  from .._qt3_d_core__bounding_volume_calculator import BoundingVolumeCalculator
  from .._qt3_d_core__bounding_volume_compute_data import BoundingVolumeComputeData
  from .._qt3_d_core__bounding_volume_compute_result import BoundingVolumeComputeResult
  from .._qt3_d_core__bounding_volume_job_processor import BoundingVolumeJobProcessor
  from .._qt3_d_core__buffer_info import BufferInfo
  from .._qt3_d_core__component_relationship_change import ComponentRelationshipChange
  from .._qt3_d_core__job_id import JobId
  from .._qt3_d_core__joint_names_and_local_poses import JointNamesAndLocalPoses
  from .._qt3_d_core__node_tree_change import NodeTreeChange
  from .._qt3_d_core__q_abstract_front_end_node_manager import QAbstractFrontEndNodeManager
  from .._qt3_d_core__q_abstract_functor import QAbstractFunctor
  from .._qt3_d_core__q_abstract_node_factory import QAbstractNodeFactory
  from .._qt3_d_core__q_armature_data import QArmatureData
  from .._qt3_d_core__q_aspect_job import QAspectJob
  from .._qt3_d_core__q_aspect_job_private import QAspectJobPrivate
  from .._qt3_d_core__q_aspect_job_provider_interface import QAspectJobProviderInterface
  from .._qt3_d_core__q_backend_node import QBackendNode
  from .._qt3_d_core__q_backend_node_mapper import QBackendNodeMapper
  from .._qt3_d_core__q_backend_node_private import QBackendNodePrivate
  from .._qt3_d_core__q_buffer_update import QBufferUpdate
  from .._qt3_d_core__q_destruction_id_and_type_collector import QDestructionIdAndTypeCollector
  from .._qt3_d_core__q_joint_data import QJointData
  from .._qt3_d_core__q_node_id import QNodeId
  from .._qt3_d_core__q_node_visitor import QNodeVisitor
  from .._qt3_d_core__q_service_locator import QServiceLocator
  from .._qt3_d_core__q_skeleton_data import QSkeletonData
  from .._qt3_d_core__q_skeleton_loader_data import QSkeletonLoaderData
  from .._qt3_d_core__q_task_logger import QTaskLogger
  from .._qt3_d_core__q_tick_clock import QTickClock
  from .._qt3_d_core__q_transform_data import QTransformData
  from .._qt3_d_core__sqt import Sqt
  from .._qt3_d_core__calculate_bounding_volume_job import CalculateBoundingVolumeJob
  from .._qt3_d_core__core_settings_functor import CoreSettingsFunctor
  from .._qt3_d_core__q_geometry_factory import QGeometryFactory
  from .._qt3_d_core__q_scene import QScene
  from .._qt3_d_core__runnable_interface import RunnableInterface
  from .._qt3_d_core__aspect_task_runnable import AspectTaskRunnable
  from .._qt3_d_core__sync_task_runnable import SyncTaskRunnable
  from .._qt3_d_core__q_download_request import QDownloadRequest
  from .._qt3_d_core__q_url_helper import QUrlHelper
  from .._qt3_d_core__node_post_constructor_init import NodePostConstructorInit
  from .._qt3_d_core__property_change_handler_base import PropertyChangeHandlerBase
  from .._qt3_d_core__q_abstract_aspect import QAbstractAspect
  from .._qt3_d_core__q_abstract_aspect_job_manager import QAbstractAspectJobManager
  from .._qt3_d_core__q_abstract_aspect_private import QAbstractAspectPrivate
  from .._qt3_d_core__q_abstract_service_provider import QAbstractServiceProvider
  from .._qt3_d_core__q_abstract_service_provider_private import QAbstractServiceProviderPrivate
  from .._qt3_d_core__q_aspect_engine import QAspectEngine
  from .._qt3_d_core__q_aspect_engine_private import QAspectEnginePrivate
  from .._qt3_d_core__q_aspect_factory import QAspectFactory
  from .._qt3_d_core__q_change_arbiter import QChangeArbiter
  from .._qt3_d_core__q_node import QNode
  from .._qt3_d_core__q_node_id_type_pair import QNodeIdTypePair
  from .._qt3_d_core__q_node_private import QNodePrivate
  from .._qt3_d_core__q_scheduler import QScheduler
  from .._qt3_d_core__q_thread_pooler import QThreadPooler
  from .._qt3_d_core__core_settings import CoreSettings
  from .._qt3_d_core__q_abstract_frame_advance_service import QAbstractFrameAdvanceService
  from .._qt3_d_core__q_abstract_frame_advance_service_private import QAbstractFrameAdvanceServicePrivate
  from .._qt3_d_core__q_abstract_skeleton import QAbstractSkeleton
  from .._qt3_d_core__q_abstract_skeleton_private import QAbstractSkeletonPrivate
  from .._qt3_d_core__q_aspect_job_manager import QAspectJobManager
  from .._qt3_d_core__q_attribute import QAttribute
  from .._qt3_d_core__q_attribute_private import QAttributePrivate
  from .._qt3_d_core__q_buffer import QBuffer
  from .._qt3_d_core__q_buffer_private import QBufferPrivate
  from .._qt3_d_core__q_component import QComponent
  from .._qt3_d_core__q_component_private import QComponentPrivate
  from .._qt3_d_core__q_core_aspect import QCoreAspect
  from .._qt3_d_core__q_core_aspect_private import QCoreAspectPrivate
  from .._qt3_d_core__q_download_helper_service import QDownloadHelperService
  from .._qt3_d_core__q_entity import QEntity
  from .._qt3_d_core__q_entity_private import QEntityPrivate
  from .._qt3_d_core__q_event_filter_service import QEventFilterService
  from .._qt3_d_core__q_geometry_view import QGeometryView
  from .._qt3_d_core__q_geometry_view_private import QGeometryViewPrivate
  from .._qt3_d_core__q_joint_private import QJointPrivate
  from .._qt3_d_core__q_open_g_l_information_service import QOpenGLInformationService
  from .._qt3_d_core__q_open_g_l_information_service_private import QOpenGLInformationServicePrivate
  from .._qt3_d_core__q_system_information_service import QSystemInformationService
  from .._qt3_d_core__q_system_information_service_private import QSystemInformationServicePrivate
  from .._qt3_d_core__null_open_g_l_information_service import NullOpenGLInformationService
  from .._qt3_d_core__q_armature import QArmature
  from .._qt3_d_core__q_armature_private import QArmaturePrivate
  from .._qt3_d_core__q_aspect_manager import QAspectManager
  from .._qt3_d_core__q_core_settings import QCoreSettings
  from .._qt3_d_core__q_core_settings_private import QCoreSettingsPrivate
  from .._qt3_d_core__q_skeleton_loader_private import QSkeletonLoaderPrivate
  from .._qt3_d_core__q_skeleton_private import QSkeletonPrivate
  from .._qt3_d_core__q_tick_clock_service import QTickClockService
  from .._qt3_d_core__q_bounding_volume import QBoundingVolume
  from .._qt3_d_core__q_bounding_volume_private import QBoundingVolumePrivate
  from .._qt3_d_core__q_geometry import QGeometry
  from .._qt3_d_core__q_geometry_private import QGeometryPrivate
  from .._qt3_d_core__q_joint import QJoint
  from .._qt3_d_core__q_transform import QTransform
  from .._qt3_d_core__q_transform_private import QTransformPrivate
  from .._qt3_d_core__q_skeleton import QSkeleton
  from .._qt3_d_core__q_skeleton_loader import QSkeletonLoader
  from .._qt3_d_core__q_download_network_worker import QDownloadNetworkWorker
  from . import Debug
  from . import JobTypes
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AlignedAllocator': '_qt3_d_core__aligned_allocator',
      'BoundingVolumeCalculator': '_qt3_d_core__bounding_volume_calculator',
      'BoundingVolumeComputeData': '_qt3_d_core__bounding_volume_compute_data',
      'BoundingVolumeComputeResult': '_qt3_d_core__bounding_volume_compute_result',
      'BoundingVolumeJobProcessor': '_qt3_d_core__bounding_volume_job_processor',
      'BufferInfo': '_qt3_d_core__buffer_info',
      'ComponentRelationshipChange': '_qt3_d_core__component_relationship_change',
      'JobId': '_qt3_d_core__job_id',
      'JointNamesAndLocalPoses': '_qt3_d_core__joint_names_and_local_poses',
      'NodeTreeChange': '_qt3_d_core__node_tree_change',
      'QAbstractFrontEndNodeManager': '_qt3_d_core__q_abstract_front_end_node_manager',
      'QAbstractFunctor': '_qt3_d_core__q_abstract_functor',
      'QAbstractNodeFactory': '_qt3_d_core__q_abstract_node_factory',
      'QArmatureData': '_qt3_d_core__q_armature_data',
      'QAspectJob': '_qt3_d_core__q_aspect_job',
      'QAspectJobPrivate': '_qt3_d_core__q_aspect_job_private',
      'QAspectJobProviderInterface': '_qt3_d_core__q_aspect_job_provider_interface',
      'QBackendNode': '_qt3_d_core__q_backend_node',
      'QBackendNodeMapper': '_qt3_d_core__q_backend_node_mapper',
      'QBackendNodePrivate': '_qt3_d_core__q_backend_node_private',
      'QBufferUpdate': '_qt3_d_core__q_buffer_update',
      'QDestructionIdAndTypeCollector': '_qt3_d_core__q_destruction_id_and_type_collector',
      'QJointData': '_qt3_d_core__q_joint_data',
      'QNodeId': '_qt3_d_core__q_node_id',
      'QNodeVisitor': '_qt3_d_core__q_node_visitor',
      'QServiceLocator': '_qt3_d_core__q_service_locator',
      'QSkeletonData': '_qt3_d_core__q_skeleton_data',
      'QSkeletonLoaderData': '_qt3_d_core__q_skeleton_loader_data',
      'QTaskLogger': '_qt3_d_core__q_task_logger',
      'QTickClock': '_qt3_d_core__q_tick_clock',
      'QTransformData': '_qt3_d_core__q_transform_data',
      'Sqt': '_qt3_d_core__sqt',
      'CalculateBoundingVolumeJob': '_qt3_d_core__calculate_bounding_volume_job',
      'CoreSettingsFunctor': '_qt3_d_core__core_settings_functor',
      'QGeometryFactory': '_qt3_d_core__q_geometry_factory',
      'QScene': '_qt3_d_core__q_scene',
      'RunnableInterface': '_qt3_d_core__runnable_interface',
      'AspectTaskRunnable': '_qt3_d_core__aspect_task_runnable',
      'SyncTaskRunnable': '_qt3_d_core__sync_task_runnable',
      'QDownloadRequest': '_qt3_d_core__q_download_request',
      'QUrlHelper': '_qt3_d_core__q_url_helper',
      'NodePostConstructorInit': '_qt3_d_core__node_post_constructor_init',
      'PropertyChangeHandlerBase': '_qt3_d_core__property_change_handler_base',
      'QAbstractAspect': '_qt3_d_core__q_abstract_aspect',
      'QAbstractAspectJobManager': '_qt3_d_core__q_abstract_aspect_job_manager',
      'QAbstractAspectPrivate': '_qt3_d_core__q_abstract_aspect_private',
      'QAbstractServiceProvider': '_qt3_d_core__q_abstract_service_provider',
      'QAbstractServiceProviderPrivate': '_qt3_d_core__q_abstract_service_provider_private',
      'QAspectEngine': '_qt3_d_core__q_aspect_engine',
      'QAspectEnginePrivate': '_qt3_d_core__q_aspect_engine_private',
      'QAspectFactory': '_qt3_d_core__q_aspect_factory',
      'QChangeArbiter': '_qt3_d_core__q_change_arbiter',
      'QNode': '_qt3_d_core__q_node',
      'QNodeIdTypePair': '_qt3_d_core__q_node_id_type_pair',
      'QNodePrivate': '_qt3_d_core__q_node_private',
      'QScheduler': '_qt3_d_core__q_scheduler',
      'QThreadPooler': '_qt3_d_core__q_thread_pooler',
      'CoreSettings': '_qt3_d_core__core_settings',
      'QAbstractFrameAdvanceService': '_qt3_d_core__q_abstract_frame_advance_service',
      'QAbstractFrameAdvanceServicePrivate': '_qt3_d_core__q_abstract_frame_advance_service_private',
      'QAbstractSkeleton': '_qt3_d_core__q_abstract_skeleton',
      'QAbstractSkeletonPrivate': '_qt3_d_core__q_abstract_skeleton_private',
      'QAspectJobManager': '_qt3_d_core__q_aspect_job_manager',
      'QAttribute': '_qt3_d_core__q_attribute',
      'QAttributePrivate': '_qt3_d_core__q_attribute_private',
      'QBuffer': '_qt3_d_core__q_buffer',
      'QBufferPrivate': '_qt3_d_core__q_buffer_private',
      'QComponent': '_qt3_d_core__q_component',
      'QComponentPrivate': '_qt3_d_core__q_component_private',
      'QCoreAspect': '_qt3_d_core__q_core_aspect',
      'QCoreAspectPrivate': '_qt3_d_core__q_core_aspect_private',
      'QDownloadHelperService': '_qt3_d_core__q_download_helper_service',
      'QEntity': '_qt3_d_core__q_entity',
      'QEntityPrivate': '_qt3_d_core__q_entity_private',
      'QEventFilterService': '_qt3_d_core__q_event_filter_service',
      'QGeometryView': '_qt3_d_core__q_geometry_view',
      'QGeometryViewPrivate': '_qt3_d_core__q_geometry_view_private',
      'QJointPrivate': '_qt3_d_core__q_joint_private',
      'QOpenGLInformationService': '_qt3_d_core__q_open_g_l_information_service',
      'QOpenGLInformationServicePrivate': '_qt3_d_core__q_open_g_l_information_service_private',
      'QSystemInformationService': '_qt3_d_core__q_system_information_service',
      'QSystemInformationServicePrivate': '_qt3_d_core__q_system_information_service_private',
      'NullOpenGLInformationService': '_qt3_d_core__null_open_g_l_information_service',
      'QArmature': '_qt3_d_core__q_armature',
      'QArmaturePrivate': '_qt3_d_core__q_armature_private',
      'QAspectManager': '_qt3_d_core__q_aspect_manager',
      'QCoreSettings': '_qt3_d_core__q_core_settings',
      'QCoreSettingsPrivate': '_qt3_d_core__q_core_settings_private',
      'QSkeletonLoaderPrivate': '_qt3_d_core__q_skeleton_loader_private',
      'QSkeletonPrivate': '_qt3_d_core__q_skeleton_private',
      'QTickClockService': '_qt3_d_core__q_tick_clock_service',
      'QBoundingVolume': '_qt3_d_core__q_bounding_volume',
      'QBoundingVolumePrivate': '_qt3_d_core__q_bounding_volume_private',
      'QGeometry': '_qt3_d_core__q_geometry',
      'QGeometryPrivate': '_qt3_d_core__q_geometry_private',
      'QJoint': '_qt3_d_core__q_joint',
      'QTransform': '_qt3_d_core__q_transform',
      'QTransformPrivate': '_qt3_d_core__q_transform_private',
      'QSkeleton': '_qt3_d_core__q_skeleton',
      'QSkeletonLoader': '_qt3_d_core__q_skeleton_loader',
      'QDownloadNetworkWorker': '_qt3_d_core__q_download_network_worker',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('Debug', 'JobTypes',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DCore.AlignedAllocator'. Python calls this for a
    name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
