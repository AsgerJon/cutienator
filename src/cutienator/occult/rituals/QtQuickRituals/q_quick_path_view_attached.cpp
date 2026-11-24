//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_pathview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickpathview_p.h"
#include "qquickpathview_p_p.h"
#include "qquickflickablebehavior_p.h" //Contains flicking behavior defines
#include "qquicktext_p.h"
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <private/qqmlglobal_p.h>
#include <private/qqmlopenmetaobject_p.h>
#include <private/qqmlchangeset_p.h>
#include <qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qmath.h>
#include <cmath>
#if QT_CONFIG(quick_itemview)
#include <private/qquickitemview_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 53, as _ZN22QQuickPathViewAttachedD1Ev
inline QQuickPathViewAttached::~QQuickPathViewAttached()
{
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 57, as _ZNK22QQuickPathViewAttached5valueERK10QByteArray
inline QVariant QQuickPathViewAttached::value(const QByteArray &name) const
{
    return m_metaobject->value(name);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 61, as _ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVariant
inline void QQuickPathViewAttached::setValue(const QByteArray &name, const QVariant &val)
{
    m_metaobject->setValue(name, val);
}
//  -----------------------------------------------------------------------

//  A QQuickPathViewAttached that Python can take functions over in. Every QQuickPathViewAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPathViewAttached : public QQuickPathViewAttached {
public:
  using QQuickPathViewAttached::QQuickPathViewAttached;
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
      CuteQQuickPathViewAttachedCall0 call = reinterpret_cast<CuteQQuickPathViewAttachedCall0>(taken[0]);
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
      CuteQQuickPathViewAttachedCall1 call = reinterpret_cast<CuteQQuickPathViewAttachedCall1>(taken[1]);
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
      CuteQQuickPathViewAttachedCall2 call = reinterpret_cast<CuteQQuickPathViewAttachedCall2>(taken[2]);
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
      CuteQQuickPathViewAttachedCall3 call = reinterpret_cast<CuteQQuickPathViewAttachedCall3>(taken[3]);
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
      CuteQQuickPathViewAttachedCall4 call = reinterpret_cast<CuteQQuickPathViewAttachedCall4>(taken[4]);
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
      CuteQQuickPathViewAttachedCall5 call = reinterpret_cast<CuteQQuickPathViewAttachedCall5>(taken[5]);
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
      CuteQQuickPathViewAttachedCall6 call = reinterpret_cast<CuteQQuickPathViewAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPathViewAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickPathViewAttached10metaObjectEv(
    const QQuickPathViewAttached *self) {
  return self->metaObject();
}

//  QQuickPathViewAttached::~QQuickPathViewAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttachedD1Ev(QQuickPathViewAttached *self) {
  delete self;
}

//  QQuickPathView *QQuickPathViewAttached::view() const
extern "C" Q_DECL_EXPORT
QQuickPathView *ritual_ZNK22QQuickPathViewAttached4viewEv(
    const QQuickPathViewAttached *self) {
  return self->view();
}

//  bool QQuickPathViewAttached::isCurrentItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickPathViewAttached13isCurrentItemEv(
    const QQuickPathViewAttached *self) {
  return self->isCurrentItem();
}

//  QVariant QQuickPathViewAttached::value(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQuickPathViewAttached5valueERK10QByteArray(
    const QQuickPathViewAttached *self,
    const QByteArray *name) {
  return new QVariant(self->value(*name));
}

//  void QQuickPathViewAttached::setValue(const QByteArray &name, const
//      QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVariant(
    QQuickPathViewAttached *self,
    const QByteArray *name,
    const QVariant *val) {
  self->setValue(*name, *val);
}

//  bool QQuickPathViewAttached::isOnPath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickPathViewAttached8isOnPathEv(
    const QQuickPathViewAttached *self) {
  return self->isOnPath();
}

//  a Python function taken by a CuteQQuickPathViewAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathViewAttached(
    QQuickPathViewAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathViewAttached *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_pathview)
