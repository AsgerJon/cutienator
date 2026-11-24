//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DPhysi
//  cs/6.12.0/QtQuick3DPhysics/private/qabstractphysicsbody_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractphysicsbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractphysicsbody_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 48, as _ZNK20QAbstractPhysicsBody15physicsMaterialEv
inline QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial() const
{
    return m_physicsMaterial;
}

//  from ../qtquick3dphysics/src/quick3dphysics/qabstractphysicsbody.cpp, line 61, as _ZNK20QAbstractPhysicsBody17simulationEnabledEv
inline bool QAbstractPhysicsBody::simulationEnabled() const
{
    return m_simulationEnabled;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractPhysicsBody::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QAbstractPhysicsBody10metaObjectEv(
    const QAbstractPhysicsBody *self) {
  return self->metaObject();
}

//  void QAbstractPhysicsBody::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractPhysicsBody24qt_qmlMarker_uncreatableEv(
    QAbstractPhysicsBody *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial() const
extern "C" Q_DECL_EXPORT
QPhysicsMaterial *ritual_ZNK20QAbstractPhysicsBody15physicsMaterialEv(
    const QAbstractPhysicsBody *self) {
  return self->physicsMaterial();
}

//  bool QAbstractPhysicsBody::simulationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAbstractPhysicsBody17simulationEnabledEv(
    const QAbstractPhysicsBody *self) {
  return self->simulationEnabled();
}
