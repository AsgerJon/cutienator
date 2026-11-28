"""
The namespace 'Qt3DCore::Quick' of Qt, a package of 'cutienator.Qt3DQuick':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.Qt3DQuick import Qt3DCore
  Qt3DCore.Quick.QAbstractSkeletonForeign

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
    'QAbstractSkeletonForeign',
    'QArmatureForeign',
    'QAttributeForeign',
    'QBoundingVolumeForeign',
    'QBufferForeign',
    'QComponentForeign',
    'QEntityForeign',
    'QGeometryForeign',
    'QGeometryViewForeign',
    'QJointForeign',
    'QNodeForeign',
    'QQmlAspectEngine',
    'QQmlAspectEnginePrivate',
    'QSkeletonLoaderForeign',
    'QTransformForeign',
    'Quick3DEntity',
    'Quick3DGeometry',
    'Quick3DJoint',
    'Quick3DNode',
    'QQuick3DColorValueType',
    'QQuick3DMatrix4x4ValueType',
    'QQuick3DQuaternionValueType',
    'QQuick3DVector2DValueType',
    'QQuick3DVector3DValueType',
    'QQuick3DVector4DValueType',
    'Quick3DBuffer',
    'Quick3DEntityLoader',
    'Quick3DEntityLoaderPrivate',
    'Quick3DNodeInstantiator',
    'QQuaternionAnimation',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._qt3_d_core__quick__q_abstract_skeleton_foreign import QAbstractSkeletonForeign
  from ..._qt3_d_core__quick__q_armature_foreign import QArmatureForeign
  from ..._qt3_d_core__quick__q_attribute_foreign import QAttributeForeign
  from ..._qt3_d_core__quick__q_bounding_volume_foreign import QBoundingVolumeForeign
  from ..._qt3_d_core__quick__q_buffer_foreign import QBufferForeign
  from ..._qt3_d_core__quick__q_component_foreign import QComponentForeign
  from ..._qt3_d_core__quick__q_entity_foreign import QEntityForeign
  from ..._qt3_d_core__quick__q_geometry_foreign import QGeometryForeign
  from ..._qt3_d_core__quick__q_geometry_view_foreign import QGeometryViewForeign
  from ..._qt3_d_core__quick__q_joint_foreign import QJointForeign
  from ..._qt3_d_core__quick__q_node_foreign import QNodeForeign
  from ..._qt3_d_core__quick__q_qml_aspect_engine import QQmlAspectEngine
  from ..._qt3_d_core__quick__q_qml_aspect_engine_private import QQmlAspectEnginePrivate
  from ..._qt3_d_core__quick__q_skeleton_loader_foreign import QSkeletonLoaderForeign
  from ..._qt3_d_core__quick__q_transform_foreign import QTransformForeign
  from ..._qt3_d_core__quick__quick3_d_entity import Quick3DEntity
  from ..._qt3_d_core__quick__quick3_d_geometry import Quick3DGeometry
  from ..._qt3_d_core__quick__quick3_d_joint import Quick3DJoint
  from ..._qt3_d_core__quick__quick3_d_node import Quick3DNode
  from ..._qt3_d_core__quick__q_quick3_d_color_value_type import QQuick3DColorValueType
  from ..._qt3_d_core__quick__q_quick3_d_matrix4x4_value_type import QQuick3DMatrix4x4ValueType
  from ..._qt3_d_core__quick__q_quick3_d_quaternion_value_type import QQuick3DQuaternionValueType
  from ..._qt3_d_core__quick__q_quick3_d_vector2_d_value_type import QQuick3DVector2DValueType
  from ..._qt3_d_core__quick__q_quick3_d_vector3_d_value_type import QQuick3DVector3DValueType
  from ..._qt3_d_core__quick__q_quick3_d_vector4_d_value_type import QQuick3DVector4DValueType
  from ..._qt3_d_core__quick__quick3_d_buffer import Quick3DBuffer
  from ..._qt3_d_core__quick__quick3_d_entity_loader import Quick3DEntityLoader
  from ..._qt3_d_core__quick__quick3_d_entity_loader_private import Quick3DEntityLoaderPrivate
  from ..._qt3_d_core__quick__quick3_d_node_instantiator import Quick3DNodeInstantiator
  from ..._qt3_d_core__quick__q_quaternion_animation import QQuaternionAnimation
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QAbstractSkeletonForeign': '_qt3_d_core__quick__q_abstract_skeleton_foreign',
      'QArmatureForeign': '_qt3_d_core__quick__q_armature_foreign',
      'QAttributeForeign': '_qt3_d_core__quick__q_attribute_foreign',
      'QBoundingVolumeForeign': '_qt3_d_core__quick__q_bounding_volume_foreign',
      'QBufferForeign': '_qt3_d_core__quick__q_buffer_foreign',
      'QComponentForeign': '_qt3_d_core__quick__q_component_foreign',
      'QEntityForeign': '_qt3_d_core__quick__q_entity_foreign',
      'QGeometryForeign': '_qt3_d_core__quick__q_geometry_foreign',
      'QGeometryViewForeign': '_qt3_d_core__quick__q_geometry_view_foreign',
      'QJointForeign': '_qt3_d_core__quick__q_joint_foreign',
      'QNodeForeign': '_qt3_d_core__quick__q_node_foreign',
      'QQmlAspectEngine': '_qt3_d_core__quick__q_qml_aspect_engine',
      'QQmlAspectEnginePrivate': '_qt3_d_core__quick__q_qml_aspect_engine_private',
      'QSkeletonLoaderForeign': '_qt3_d_core__quick__q_skeleton_loader_foreign',
      'QTransformForeign': '_qt3_d_core__quick__q_transform_foreign',
      'Quick3DEntity': '_qt3_d_core__quick__quick3_d_entity',
      'Quick3DGeometry': '_qt3_d_core__quick__quick3_d_geometry',
      'Quick3DJoint': '_qt3_d_core__quick__quick3_d_joint',
      'Quick3DNode': '_qt3_d_core__quick__quick3_d_node',
      'QQuick3DColorValueType': '_qt3_d_core__quick__q_quick3_d_color_value_type',
      'QQuick3DMatrix4x4ValueType': '_qt3_d_core__quick__q_quick3_d_matrix4x4_value_type',
      'QQuick3DQuaternionValueType': '_qt3_d_core__quick__q_quick3_d_quaternion_value_type',
      'QQuick3DVector2DValueType': '_qt3_d_core__quick__q_quick3_d_vector2_d_value_type',
      'QQuick3DVector3DValueType': '_qt3_d_core__quick__q_quick3_d_vector3_d_value_type',
      'QQuick3DVector4DValueType': '_qt3_d_core__quick__q_quick3_d_vector4_d_value_type',
      'Quick3DBuffer': '_qt3_d_core__quick__quick3_d_buffer',
      'Quick3DEntityLoader': '_qt3_d_core__quick__quick3_d_entity_loader',
      'Quick3DEntityLoaderPrivate': '_qt3_d_core__quick__quick3_d_entity_loader_private',
      'Quick3DNodeInstantiator': '_qt3_d_core__quick__quick3_d_node_instantiator',
      'QQuaternionAnimation': '_qt3_d_core__quick__q_quaternion_animation',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt3DCore.Quick.QAbstractSkeletonForeign'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
