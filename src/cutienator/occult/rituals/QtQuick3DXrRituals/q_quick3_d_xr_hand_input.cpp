//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxrinputmanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 23, as _ZNK19QQuick3DXrHandInput8isActiveEv
inline bool QQuick3DXrHandInput::isActive() const
{
    return m_isActive;
}

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

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 62, as _ZNK19QQuick3DXrHandInput12pokePositionEv
inline QVector3D QQuick3DXrHandInput::pokePosition() const
{
    return m_pokePosition;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrhandinput.cpp, line 75, as _ZNK19QQuick3DXrHandInput20isHandTrackingActiveEv
inline bool QQuick3DXrHandInput::isHandTrackingActive() const
{
    return m_isHandTracking;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrHandInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DXrHandInput10metaObjectEv(
    const QQuick3DXrHandInput *self) {
  return self->metaObject();
}

//  void *QQuick3DXrHandInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DXrHandInput11qt_metacastEPKc(
    QQuick3DXrHandInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrHandInput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DXrHandInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrHandInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool QQuick3DXrHandInput::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DXrHandInput8isActiveEv(
    const QQuick3DXrHandInput *self) {
  return self->isActive();
}

//  QList<QVector3D> QQuick3DXrHandInput::jointPositions() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK19QQuick3DXrHandInput14jointPositionsEv(
    const QQuick3DXrHandInput *self) {
  return new QList<QVector3D>(self->jointPositions());
}

//  QList<QQuaternion> QQuick3DXrHandInput::jointRotations() const
extern "C" Q_DECL_EXPORT
QList<QQuaternion> *ritual_ZNK19QQuick3DXrHandInput14jointRotationsEv(
    const QQuick3DXrHandInput *self) {
  return new QList<QQuaternion>(self->jointRotations());
}

//  QVector3D QQuick3DXrHandInput::pokePosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK19QQuick3DXrHandInput12pokePositionEv(
    const QQuick3DXrHandInput *self) {
  return new QVector3D(self->pokePosition());
}

//  bool QQuick3DXrHandInput::isHandTrackingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DXrHandInput20isHandTrackingActiveEv(
    const QQuick3DXrHandInput *self) {
  return self->isHandTrackingActive();
}

//  void QQuick3DXrHandInput::isActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput15isActiveChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isActiveChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isActiveChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::poseSpaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput16poseSpaceChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "poseSpaceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "poseSpaceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::posePositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19posePositionChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "posePositionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "posePositionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::poseRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19poseRotationChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "poseRotationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "poseRotationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointPositionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21jointPositionsChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointPositionsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointPositionsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointRotationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21jointRotationsChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointRotationsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointRotationsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::jointDataUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput16jointDataUpdatedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "jointDataUpdated()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "jointDataUpdated()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::pokePositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput19pokePositionChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pokePositionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pokePositionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandInput::isHandTrackingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandInput21isHandTrackingChangedEv(
    QQuick3DXrHandInput *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandInput")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isHandTrackingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isHandTrackingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
