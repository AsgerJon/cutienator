//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qremoteobjectsource.h"
#include "qremoteobjectsource_p.h"
#include "qremoteobjectnode.h"
#include "qremoteobjectdynamicreplica.h"
#include "qconnectionfactories_p.h"
#include "qremoteobjectsourceio_p.h"
#include "qremoteobjectabstractitemmodeladapter_p.h"
#include <QtCore/qmetaobject.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractitemmodel.h>
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 354, as _ZN23QRemoteObjectRootSourceD1Ev
inline QRemoteObjectRootSource::~QRemoteObjectRootSource()
{
    for (const auto &it : std::as_const(m_children)) {
        // We used QPointers for m_children because we don't control the lifetime of child QObjects
        // Since the this/source QObject's parent is the referenced QObject, it could have already
        // been deleted
        delete it.data();
    }
    d->m_sourceIo->unregisterSource(this);
    // removeListener tries to modify d->m_listeners, this is O(N²),
    // so clear d->m_listeners prior to calling unregister (consume loop).
    // We can do this, because we don't care about the return value of removeListener() here.
    const auto listeners = std::exchange(d->m_listeners, {});
    for (QtROIoDeviceBase *io : listeners) {
        removeListener(io, true);
    }
    delete d;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectRootSource that Python can take functions over in. Every QRemoteObjectRootSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRemoteObjectRootSourceCall0)(const void *, int *);
typedef QString * (*CuteQRemoteObjectRootSourceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRootSourceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRootSourceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRootSourceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRootSourceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRootSourceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRootSourceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRootSourceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectRootSource : public QRemoteObjectRootSource {
public:
  using QRemoteObjectRootSource::QRemoteObjectRootSource;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase6isRootEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase4nameEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QRemoteObjectRootSource::isRoot() const
  bool isRoot() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall0 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRemoteObjectRootSource::isRoot();
  }

  //  QString QRemoteObjectRootSource::name() const
  QString name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall1 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QRemoteObjectRootSource::name();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall2 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall3 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall4 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall5 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall6 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall7 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectRootSourceCall8 call = reinterpret_cast<CuteQRemoteObjectRootSourceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectRootSource::~QRemoteObjectRootSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRemoteObjectRootSourceD1Ev(QRemoteObjectRootSource *self) {
  delete self;
}

//  bool QRemoteObjectRootSource::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRemoteObjectRootSource6isRootEv(
    const QRemoteObjectRootSource *self) {
  return self->isRoot();
}

//  QString QRemoteObjectRootSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRemoteObjectRootSource4nameEv(
    const QRemoteObjectRootSource *self) {
  return new QString(self->name());
}

//  a Python function taken by a CuteQRemoteObjectRootSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectRootSource(
    QRemoteObjectRootSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectRootSource *>(self)->take(key, call);
}

//  bool QRemoteObjectRootSource::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QRemoteObjectRootSource6isRootEv(
    const QRemoteObjectRootSource *self) {
  return self->QRemoteObjectRootSource::isRoot();
}

//  QString QRemoteObjectRootSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QRemoteObjectRootSource4nameEv(
    const QRemoteObjectRootSource *self) {
  return new QString(self->QRemoteObjectRootSource::name());
}
