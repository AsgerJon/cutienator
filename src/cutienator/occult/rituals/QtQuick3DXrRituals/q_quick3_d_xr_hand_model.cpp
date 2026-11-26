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
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrHandModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DXrHandModel10metaObjectEv(
    const QQuick3DXrHandModel *self) {
  return self->metaObject();
}

//  void *QQuick3DXrHandModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DXrHandModel11qt_metacastEPKc(
    QQuick3DXrHandModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrHandModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DXrHandModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrHandModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuick3DXrHandModel::handChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandModel11handChangedEv(
    QQuick3DXrHandModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandModel::handTrackerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandModel18handTrackerChangedEv(
    QQuick3DXrHandModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handTrackerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handTrackerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHandModel::updatePose()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DXrHandModel10updatePoseEv(
    QQuick3DXrHandModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHandModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updatePose()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updatePose()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
