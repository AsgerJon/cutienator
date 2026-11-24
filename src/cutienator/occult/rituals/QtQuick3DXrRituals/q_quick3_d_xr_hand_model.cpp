//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandmodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxrinputmanager_visionos_p.h"
#else
#endif
#include <QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#include <QtQuick3DXr/private/qquick3dxrhandmodel_p.h>
#if defined(Q_OS_VISIONOS)
# include "visionos/qquick3dxrinputmanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 52, as _ZNK19QQuick3DXrHandInput14jointPositionsEv
inline QList<QVector3D> QQuick3DXrHandInput::jointPositions() const
{
    return m_jointPositions;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 57, as _ZNK19QQuick3DXrHandInput14jointRotationsEv
inline QList<QQuaternion> QQuick3DXrHandInput::jointRotations() const
{
    return m_jointRotations;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandmodel.cpp, line 102, as _ZN19QQuick3DXrHandModel17componentCompleteEv
inline void QQuick3DXrHandModel::componentComplete()
{
    setupModel();
    QQuick3DModel::componentComplete();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandmodel.cpp, line 123, as _ZNK19QQuick3DXrHandModel4handEv
inline QQuick3DXrHandModel::Hand QQuick3DXrHandModel::hand() const
{
    return m_hand;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandmodel.cpp, line 57, as _ZN19QQuick3DXrHandModel10updatePoseEv
inline void QQuick3DXrHandModel::updatePose()
{
    if (auto *skin = QQuick3DModel::skin()) {
        auto jointListProp = skin->joints();
        int count = jointListProp.count(&jointListProp);
        const auto positions = m_handTracker->jointPositions();
        const auto rotations = m_handTracker->jointRotations();
        for (int i = 0; i < count; ++i) {
            auto *joint = jointListProp.at(&jointListProp, i);
            joint->setPosition(positions.at(i));
            joint->setRotation(rotations.at(i));
        }
    } else {
        static bool warned = false;
        if (!warned) {
            qWarning() << "No skin available for hand model";
            warned = true;
        }
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrHandModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DXrHandModel10metaObjectEv(
    const QQuick3DXrHandModel *self) {
  return self->metaObject();
}

//  void QQuick3DXrHandModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandModel17componentCompleteEv(
    QQuick3DXrHandModel *self) {
  self->componentComplete();
}

//  Hand QQuick3DXrHandModel::hand() const
extern "C" Q_DECL_EXPORT
QQuick3DXrHandModel::Hand ritual_ZNK19QQuick3DXrHandModel4handEv(
    const QQuick3DXrHandModel *self) {
  return self->hand();
}

//  void QQuick3DXrHandModel::updatePose()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandModel10updatePoseEv(
    QQuick3DXrHandModel *self) {
  self->updatePose();
}
