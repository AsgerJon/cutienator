//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qstring.h>
#include <QtCore/quuid.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrspatialanchor_p.h>
#if defined(Q_OS_VISIONOS)
#include "visionos/qquick3dxranchormanager_visionos_p.h"
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 134, as _ZN23QQuick3DXrSpatialAnchorD1Ev
inline QQuick3DXrSpatialAnchor::~QQuick3DXrSpatialAnchor()
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 148, as _ZNK23QQuick3DXrSpatialAnchor8offset3DEv
inline QVector3D QQuick3DXrSpatialAnchor::offset3D() const
{
    return m_offset3D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 172, as _ZNK23QQuick3DXrSpatialAnchor8extent3DEv
inline QVector3D QQuick3DXrSpatialAnchor::extent3D() const
{
    return m_extent3D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 194, as _ZNK23QQuick3DXrSpatialAnchor8positionEv
inline QVector3D QQuick3DXrSpatialAnchor::position() const
{
    return m_position;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 215, as _ZNK23QQuick3DXrSpatialAnchor8rotationEv
inline QQuaternion QQuick3DXrSpatialAnchor::rotation() const
{
    return m_rotation;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 243, as _ZNK23QQuick3DXrSpatialAnchor14classificationEv
inline QQuick3DXrSpatialAnchor::Classification QQuick3DXrSpatialAnchor::classification() const
{
    return m_classification;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 271, as _ZNK23QQuick3DXrSpatialAnchor20classificationStringEv
inline QString QQuick3DXrSpatialAnchor::classificationString() const
{
    return m_classificationString;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 297, as _ZNK23QQuick3DXrSpatialAnchor11has2DBoundsEv
inline bool QQuick3DXrSpatialAnchor::has2DBounds() const
{
    return m_has2DBounds;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 330, as _ZNK23QQuick3DXrSpatialAnchor11has3DBoundsEv
inline bool QQuick3DXrSpatialAnchor::has3DBounds() const
{
    return m_has3DBounds;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 360, as _ZNK23QQuick3DXrSpatialAnchor8offset2DEv
inline QVector2D QQuick3DXrSpatialAnchor::offset2D() const
{
    return m_offset2D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 376, as _ZNK23QQuick3DXrSpatialAnchor8extent2DEv
inline QVector2D QQuick3DXrSpatialAnchor::extent2D() const
{
    return m_extent2D;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrspatialanchor.cpp, line 390, as _ZNK23QQuick3DXrSpatialAnchor10identifierEv
inline QString QQuick3DXrSpatialAnchor::identifier() const
{
    return QString::fromLatin1(m_uuid.toRfc4122());
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrSpatialAnchor that Python can take functions over in. Every QQuick3DXrSpatialAnchor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrSpatialAnchorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrSpatialAnchorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrSpatialAnchorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrSpatialAnchor : public QQuick3DXrSpatialAnchor {
public:
  using QQuick3DXrSpatialAnchor::QQuick3DXrSpatialAnchor;
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
      CuteQQuick3DXrSpatialAnchorCall0 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall0>(taken[0]);
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
      CuteQQuick3DXrSpatialAnchorCall1 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall1>(taken[1]);
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
      CuteQQuick3DXrSpatialAnchorCall2 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall2>(taken[2]);
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
      CuteQQuick3DXrSpatialAnchorCall3 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall3>(taken[3]);
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
      CuteQQuick3DXrSpatialAnchorCall4 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall4>(taken[4]);
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
      CuteQQuick3DXrSpatialAnchorCall5 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall5>(taken[5]);
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
      CuteQQuick3DXrSpatialAnchorCall6 call = reinterpret_cast<CuteQQuick3DXrSpatialAnchorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrSpatialAnchor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DXrSpatialAnchor10metaObjectEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->metaObject();
}

//  void QQuick3DXrSpatialAnchor::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchor24qt_qmlMarker_uncreatableEv(
    QQuick3DXrSpatialAnchor *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DXrSpatialAnchor::~QQuick3DXrSpatialAnchor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DXrSpatialAnchorD1Ev(QQuick3DXrSpatialAnchor *self) {
  delete self;
}

//  QVector3D QQuick3DXrSpatialAnchor::offset3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8offset3DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->offset3D());
}

//  QVector3D QQuick3DXrSpatialAnchor::extent3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8extent3DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->extent3D());
}

//  QVector3D QQuick3DXrSpatialAnchor::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DXrSpatialAnchor8positionEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector3D(self->position());
}

//  QQuaternion QQuick3DXrSpatialAnchor::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK23QQuick3DXrSpatialAnchor8rotationEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QQuaternion(self->rotation());
}

//  Classification QQuick3DXrSpatialAnchor::classification() const
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchor::Classification ritual_ZNK23QQuick3DXrSpatialAnchor14classificationEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->classification();
}

//  QString QQuick3DXrSpatialAnchor::classificationString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuick3DXrSpatialAnchor20classificationStringEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QString(self->classificationString());
}

//  bool QQuick3DXrSpatialAnchor::has2DBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DXrSpatialAnchor11has2DBoundsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->has2DBounds();
}

//  bool QQuick3DXrSpatialAnchor::has3DBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuick3DXrSpatialAnchor11has3DBoundsEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->has3DBounds();
}

//  QVector2D QQuick3DXrSpatialAnchor::offset2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuick3DXrSpatialAnchor8offset2DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector2D(self->offset2D());
}

//  QVector2D QQuick3DXrSpatialAnchor::extent2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuick3DXrSpatialAnchor8extent2DEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QVector2D(self->extent2D());
}

//  QString QQuick3DXrSpatialAnchor::identifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuick3DXrSpatialAnchor10identifierEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QString(self->identifier());
}

//  QtQuick3DXr::XrSpaceId QQuick3DXrSpatialAnchor::space() const
extern "C" Q_DECL_EXPORT
QtQuick3DXr::XrSpaceId ritual_ZNK23QQuick3DXrSpatialAnchor5spaceEv(
    const QQuick3DXrSpatialAnchor *self) {
  return self->space();
}

//  QUuid QQuick3DXrSpatialAnchor::uuid() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK23QQuick3DXrSpatialAnchor4uuidEv(
    const QQuick3DXrSpatialAnchor *self) {
  return new QUuid(self->uuid());
}

//  a Python function taken by a CuteQQuick3DXrSpatialAnchor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrSpatialAnchor(
    QQuick3DXrSpatialAnchor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrSpatialAnchor *>(self)->take(key, call);
}

//  QList<QQuick3DXrSpatialAnchor *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuick3DXrSpatialAnchor *> *ritual_list_make_QQuick3DXrSpatialAnchor_ptr() {
  return new QList<QQuick3DXrSpatialAnchor *>();
}

//  void QList<QQuick3DXrSpatialAnchor *>::append(const
//      QQuick3DXrSpatialAnchor * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuick3DXrSpatialAnchor_ptr(
    QList<QQuick3DXrSpatialAnchor *> *self,
    QQuick3DXrSpatialAnchor *element) {
  self->append(element);
}

//  qsizetype QList<QQuick3DXrSpatialAnchor *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuick3DXrSpatialAnchor_ptr(
    const QList<QQuick3DXrSpatialAnchor *> *self) {
  return self->size();
}

//  const QQuick3DXrSpatialAnchor * &QList<QQuick3DXrSpatialAnchor
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuick3DXrSpatialAnchor *ritual_list_at_QQuick3DXrSpatialAnchor_ptr(
    const QList<QQuick3DXrSpatialAnchor *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuick3DXrSpatialAnchor *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuick3DXrSpatialAnchor_ptr(
    QList<QQuick3DXrSpatialAnchor *> *self) {
  delete self;
}
