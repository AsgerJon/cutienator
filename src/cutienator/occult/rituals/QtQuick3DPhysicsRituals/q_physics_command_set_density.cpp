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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3dphysics/src/quick3dphysics/qphysicscommands.cpp, line 21, as _ZN15QPhysicsCommandD1Ev
inline QPhysicsCommand::~QPhysicsCommand()
    = default;

//  from ../qtquick3dphysics/src/quick3dphysics/qphysicscommands.cpp, line 234, as _ZN25QPhysicsCommandSetDensityD1Ev
inline QPhysicsCommandSetDensity::~QPhysicsCommandSetDensity()
    = default;
//  -----------------------------------------------------------------------

//  QPhysicsCommandSetDensity::~QPhysicsCommandSetDensity()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPhysicsCommandSetDensityD1Ev(
    QPhysicsCommandSetDensity *self) {
  delete self;
}

//  void QPhysicsCommandSetDensity::execute(const QDynamicRigidBody
//      &rigidBody, physx::PxRigidBody &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPhysicsCommandSetDensity7executeERK17QDynamicRigidBodyRN5physx11PxRigidBodyE(
    QPhysicsCommandSetDensity *self,
    const QDynamicRigidBody *rigidBody,
    physx::PxRigidBody *body) {
  self->execute(*rigidBody, *body);
}
