//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicscommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicscommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/private/qphysicsworld_p.h>
#include <QtQuick3DPhysics/private/qphysicscommands_p.h>
#include <QtQuick3DPhysics/private/qdynamicrigidbody_p.h>
#include <QtGui/qquaternion.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3dphysics/src/quick3dphysics/qphysicscommands.cpp, line 21, as _ZN15QPhysicsCommandD1Ev
inline QPhysicsCommand::~QPhysicsCommand()
    = default;

//  from ../qtquick3dphysics/src/quick3dphysics/qphysicscommands.cpp, line 29, as _ZN32QPhysicsCommandApplyCentralForceD1Ev
inline QPhysicsCommandApplyCentralForce::~QPhysicsCommandApplyCentralForce()
    = default;
//  -----------------------------------------------------------------------

//  QPhysicsCommandApplyCentralForce::~QPhysicsCommandApplyCentralForce()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QPhysicsCommandApplyCentralForceD1Ev(
    QPhysicsCommandApplyCentralForce *self) {
  delete self;
}

//  void QPhysicsCommandApplyCentralForce::execute(const QDynamicRigidBody
//      &rigidBody, physx::PxRigidBody &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QPhysicsCommandApplyCentralForce7executeERK17QDynamicRigidBodyRN5physx11PxRigidBodyE(
    QPhysicsCommandApplyCentralForce *self,
    const QDynamicRigidBody *rigidBody,
    physx::PxRigidBody *body) {
  self->execute(*rigidBody, *body);
}
