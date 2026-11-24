//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qcustom3dlabel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3dlabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcustom3ditem_p.h"
#include "qcustom3dlabel_p.h"
#include "utils_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 460, as _ZN20QCustom3DItemPrivateC2EP13QCustom3DItem
inline QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q) :
    q_ptr(q),
    m_textureImage(QImage(1, 1, QImage::Format_ARGB32)),
    m_position(QVector3D(0.0f, 0.0f, 0.0f)),
    m_positionAbsolute(false),
    m_scaling(QVector3D(0.1f, 0.1f, 0.1f)),
    m_scalingAbsolute(true),
    m_rotation(identityQuaternion),
    m_visible(true),
    m_shadowCasting(true),
    m_isLabelItem(false),
    m_isVolumeItem(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 493, as _ZN20QCustom3DItemPrivateD2Ev
inline QCustom3DItemPrivate::~QCustom3DItemPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 475, as _ZN20QCustom3DItemPrivateC2EP13QCustom3DItemRK7QStringRK9QVector3DS7_RK11QQuaternion
inline QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q, const QString &meshFile,
                                           const QVector3D &position, const QVector3D &scaling,
                                           const QQuaternion &rotation) :
    q_ptr(q),
    m_textureImage(QImage(1, 1, QImage::Format_ARGB32)),
    m_meshFile(meshFile),
    m_position(position),
    m_positionAbsolute(false),
    m_scaling(scaling),
    m_scalingAbsolute(true),
    m_rotation(rotation),
    m_visible(true),
    m_shadowCasting(true),
    m_isLabelItem(false),
    m_isVolumeItem(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 508, as _ZN20QCustom3DItemPrivate14resetDirtyBitsEv
inline void QCustom3DItemPrivate::resetDirtyBits()
{
    m_dirtyBits.textureDirty = false;
    m_dirtyBits.meshDirty = false;
    m_dirtyBits.positionDirty = false;
    m_dirtyBits.scalingDirty = false;
    m_dirtyBits.rotationDirty = false;
    m_dirtyBits.visibleDirty = false;
    m_dirtyBits.shadowCastingDirty = false;
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dlabel.cpp, line 331, as _ZN21QCustom3DLabelPrivate14resetDirtyBitsEv
inline void QCustom3DLabelPrivate::resetDirtyBits()
{
    QCustom3DItemPrivate::resetDirtyBits();
    m_facingCameraDirty = false;
}
//  -----------------------------------------------------------------------

//  A QCustom3DLabelPrivate that Python can take functions over in. Every QCustom3DLabelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DLabelPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DLabelPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DLabelPrivate : public QCustom3DLabelPrivate {
public:
  using QCustom3DLabelPrivate::QCustom3DLabelPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall0 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall1 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall2 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall3 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall4 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall5 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCustom3DLabelPrivateCall6 call = reinterpret_cast<CuteQCustom3DLabelPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DLabelPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QCustom3DLabelPrivate10metaObjectEv(
    const QCustom3DLabelPrivate *self) {
  return self->metaObject();
}

//  QCustom3DLabelPrivate::~QCustom3DLabelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCustom3DLabelPrivateD1Ev(QCustom3DLabelPrivate *self) {
  delete self;
}

//  void QCustom3DLabelPrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCustom3DLabelPrivate14resetDirtyBitsEv(
    QCustom3DLabelPrivate *self) {
  self->resetDirtyBits();
}

//  a Python function taken by a CuteQCustom3DLabelPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DLabelPrivate(
    QCustom3DLabelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DLabelPrivate *>(self)->take(key, call);
}
