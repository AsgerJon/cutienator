//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapquickitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qdeclarativegeomapquickitem_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/QSGOpacityNode>
#include <QtPositioning/private/qdoublevector2d_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickmousearea_p.h>
#include <QtLocation/private/qgeomap_p.h>
#include <QtLocation/private/qgeoprojection_p.h>
#include <QtCore/QDebug>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapquickitem.cpp, line 108, as _ZNK22QMapQuickItemMatrix4x47applyToEP10QMatrix4x4
inline void QMapQuickItemMatrix4x4::applyTo(QMatrix4x4 *matrix) const
{
    *matrix *= m_matrix;
}

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapquickitem.cpp, line 100, as _ZN22QMapQuickItemMatrix4x49setMatrixERK10QMatrix4x4
inline void QMapQuickItemMatrix4x4::setMatrix(const QMatrix4x4 &matrix)
{
    if (m_matrix == matrix)
        return;
    m_matrix = matrix;
    update();
}
//  -----------------------------------------------------------------------

//  A QMapQuickItemMatrix4x4 that Python can take functions over in. Every QMapQuickItemMatrix4x4
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMapQuickItemMatrix4x4Call0)(const void *, QMatrix4x4 *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMapQuickItemMatrix4x4Call1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMapQuickItemMatrix4x4Call2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMapQuickItemMatrix4x4Call3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMapQuickItemMatrix4x4Call4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMapQuickItemMatrix4x4Call5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMapQuickItemMatrix4x4Call6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMapQuickItemMatrix4x4Call7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMapQuickItemMatrix4x4 : public QMapQuickItemMatrix4x4 {
public:
  using QMapQuickItemMatrix4x4::QMapQuickItemMatrix4x4;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QQuickTransform7applyToEP10QMatrix4x4")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QMapQuickItemMatrix4x4::applyTo(QMatrix4x4 *matrix) const
  void applyTo(QMatrix4x4 *matrix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call0 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call0>(taken[0]);
      call(this, matrix, &handled);
      if (handled) return;
    }
    QMapQuickItemMatrix4x4::applyTo(matrix);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call1 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call2 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call3 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call4 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call5 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call6 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMapQuickItemMatrix4x4Call7 call = reinterpret_cast<CuteQMapQuickItemMatrix4x4Call7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  void QMapQuickItemMatrix4x4::setMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMapQuickItemMatrix4x49setMatrixERK10QMatrix4x4(
    QMapQuickItemMatrix4x4 *self,
    const QMatrix4x4 *matrix) {
  self->setMatrix(*matrix);
}

//  void QMapQuickItemMatrix4x4::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QMapQuickItemMatrix4x47applyToEP10QMatrix4x4(
    const QMapQuickItemMatrix4x4 *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  a Python function taken by a CuteQMapQuickItemMatrix4x4, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMapQuickItemMatrix4x4(
    QMapQuickItemMatrix4x4 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMapQuickItemMatrix4x4 *>(self)->take(key, call);
}

//  void QMapQuickItemMatrix4x4::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK22QMapQuickItemMatrix4x47applyToEP10QMatrix4x4(
    const QMapQuickItemMatrix4x4 *self,
    QMatrix4x4 *matrix) {
  self->QMapQuickItemMatrix4x4::applyTo(matrix);
}
