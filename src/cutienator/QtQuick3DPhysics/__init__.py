"""
The 'cutienator.QtQuick3DPhysics' package provides the cute classes of
the part of Qt named QtQuick3DPhysics, under the name PySide6 has for
it.

  from cutienator.QtQuick3DPhysics import QPhysicsMaterial, QCollisionDebugMeshBuilder

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
    'QPhysicsMaterial',
    'QCollisionDebugMeshBuilder',
    'QAbstractCollisionShape',
    'QAbstractPhysicsNode',
    'QBoxShape',
    'QCapsuleShape',
    'QMeshShape',
    'QPlaneShape',
    'QQuick3DPhysicsMesh',
    'QSphereShape',
    'QAbstractPhysicsBody',
    'QConvexMeshShape',
    'QQuick3DPhysicsMeshManager',
    'QTriangleMeshShape',
    'QTriggerBody',
    'QCharacterController',
    'QDynamicRigidBody',
    'QHeightFieldShape',
    'QPhysicsJoint',
    'QStaticRigidBody',
    'QPhysicsCommand',
    'QPhysicsWorld',
    'QPhysXWorld',
    'QPhysicsCommandApplyCentralForce',
    'QPhysicsCommandApplyCentralImpulse',
    'QPhysicsCommandApplyForce',
    'QPhysicsCommandApplyImpulse',
    'QPhysicsCommandApplyTorque',
    'QPhysicsCommandApplyTorqueImpulse',
    'QPhysicsCommandReset',
    'QPhysicsCommandSetAngularVelocity',
    'QPhysicsCommandSetDensity',
    'QPhysicsCommandSetGravityEnabled',
    'QPhysicsCommandSetIsKinematic',
    'QPhysicsCommandSetLinearVelocity',
    'QPhysicsCommandSetMass',
    'QPhysicsCommandSetMassAndInertiaMatrix',
    'QPhysicsCommandSetMassAndInertiaTensor',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_physics_material import QPhysicsMaterial
  from ._q_collision_debug_mesh_builder import QCollisionDebugMeshBuilder
  from ._q_abstract_collision_shape import QAbstractCollisionShape
  from ._q_abstract_physics_node import QAbstractPhysicsNode
  from ._q_box_shape import QBoxShape
  from ._q_capsule_shape import QCapsuleShape
  from ._q_mesh_shape import QMeshShape
  from ._q_plane_shape import QPlaneShape
  from ._q_quick3_d_physics_mesh import QQuick3DPhysicsMesh
  from ._q_sphere_shape import QSphereShape
  from ._q_abstract_physics_body import QAbstractPhysicsBody
  from ._q_convex_mesh_shape import QConvexMeshShape
  from ._q_quick3_d_physics_mesh_manager import QQuick3DPhysicsMeshManager
  from ._q_triangle_mesh_shape import QTriangleMeshShape
  from ._q_trigger_body import QTriggerBody
  from ._q_character_controller import QCharacterController
  from ._q_dynamic_rigid_body import QDynamicRigidBody
  from ._q_height_field_shape import QHeightFieldShape
  from ._q_physics_joint import QPhysicsJoint
  from ._q_static_rigid_body import QStaticRigidBody
  from ._q_physics_command import QPhysicsCommand
  from ._q_physics_world import QPhysicsWorld
  from ._q_phys_x_world import QPhysXWorld
  from ._q_physics_command_apply_central_force import QPhysicsCommandApplyCentralForce
  from ._q_physics_command_apply_central_impulse import QPhysicsCommandApplyCentralImpulse
  from ._q_physics_command_apply_force import QPhysicsCommandApplyForce
  from ._q_physics_command_apply_impulse import QPhysicsCommandApplyImpulse
  from ._q_physics_command_apply_torque import QPhysicsCommandApplyTorque
  from ._q_physics_command_apply_torque_impulse import QPhysicsCommandApplyTorqueImpulse
  from ._q_physics_command_reset import QPhysicsCommandReset
  from ._q_physics_command_set_angular_velocity import QPhysicsCommandSetAngularVelocity
  from ._q_physics_command_set_density import QPhysicsCommandSetDensity
  from ._q_physics_command_set_gravity_enabled import QPhysicsCommandSetGravityEnabled
  from ._q_physics_command_set_is_kinematic import QPhysicsCommandSetIsKinematic
  from ._q_physics_command_set_linear_velocity import QPhysicsCommandSetLinearVelocity
  from ._q_physics_command_set_mass import QPhysicsCommandSetMass
  from ._q_physics_command_set_mass_and_inertia_matrix import QPhysicsCommandSetMassAndInertiaMatrix
  from ._q_physics_command_set_mass_and_inertia_tensor import QPhysicsCommandSetMassAndInertiaTensor
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QPhysicsMaterial': '_q_physics_material',
      'QCollisionDebugMeshBuilder': '_q_collision_debug_mesh_builder',
      'QAbstractCollisionShape': '_q_abstract_collision_shape',
      'QAbstractPhysicsNode': '_q_abstract_physics_node',
      'QBoxShape': '_q_box_shape',
      'QCapsuleShape': '_q_capsule_shape',
      'QMeshShape': '_q_mesh_shape',
      'QPlaneShape': '_q_plane_shape',
      'QQuick3DPhysicsMesh': '_q_quick3_d_physics_mesh',
      'QSphereShape': '_q_sphere_shape',
      'QAbstractPhysicsBody': '_q_abstract_physics_body',
      'QConvexMeshShape': '_q_convex_mesh_shape',
      'QQuick3DPhysicsMeshManager': '_q_quick3_d_physics_mesh_manager',
      'QTriangleMeshShape': '_q_triangle_mesh_shape',
      'QTriggerBody': '_q_trigger_body',
      'QCharacterController': '_q_character_controller',
      'QDynamicRigidBody': '_q_dynamic_rigid_body',
      'QHeightFieldShape': '_q_height_field_shape',
      'QPhysicsJoint': '_q_physics_joint',
      'QStaticRigidBody': '_q_static_rigid_body',
      'QPhysicsCommand': '_q_physics_command',
      'QPhysicsWorld': '_q_physics_world',
      'QPhysXWorld': '_q_phys_x_world',
      'QPhysicsCommandApplyCentralForce': '_q_physics_command_apply_central_force',
      'QPhysicsCommandApplyCentralImpulse': '_q_physics_command_apply_central_impulse',
      'QPhysicsCommandApplyForce': '_q_physics_command_apply_force',
      'QPhysicsCommandApplyImpulse': '_q_physics_command_apply_impulse',
      'QPhysicsCommandApplyTorque': '_q_physics_command_apply_torque',
      'QPhysicsCommandApplyTorqueImpulse': '_q_physics_command_apply_torque_impulse',
      'QPhysicsCommandReset': '_q_physics_command_reset',
      'QPhysicsCommandSetAngularVelocity': '_q_physics_command_set_angular_velocity',
      'QPhysicsCommandSetDensity': '_q_physics_command_set_density',
      'QPhysicsCommandSetGravityEnabled': '_q_physics_command_set_gravity_enabled',
      'QPhysicsCommandSetIsKinematic': '_q_physics_command_set_is_kinematic',
      'QPhysicsCommandSetLinearVelocity': '_q_physics_command_set_linear_velocity',
      'QPhysicsCommandSetMass': '_q_physics_command_set_mass',
      'QPhysicsCommandSetMassAndInertiaMatrix': '_q_physics_command_set_mass_and_inertia_matrix',
      'QPhysicsCommandSetMassAndInertiaTensor': '_q_physics_command_set_mass_and_inertia_tensor',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DPhysics import QPhysicsCommandSetMassAndInertiaTensor'. Python calls
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
