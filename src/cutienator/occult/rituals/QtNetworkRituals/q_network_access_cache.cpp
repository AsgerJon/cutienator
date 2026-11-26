//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkaccesscache_p.h>
#include "QtCore/qpointer.h"
#include "QtCore/qdeadlinetimer.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkaccesscache.cpp, line 46, as _ZN19QNetworkAccessCacheD1Ev
inline QNetworkAccessCache::~QNetworkAccessCache()
{
    clear();
}

//  from src/network/access/qnetworkaccesscache.cpp, line 224, as _ZNK19QNetworkAccessCache8hasEntryERK10QByteArray
inline bool QNetworkAccessCache::hasEntry(const QByteArray &key) const
{
    return hash.contains(key);
}
//  -----------------------------------------------------------------------

//  A QNetworkAccessCache that Python can take functions over in. Every QNetworkAccessCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessCacheCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessCacheCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessCache : public QNetworkAccessCache {
public:
  using QNetworkAccessCache::QNetworkAccessCache;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
  //  void QNetworkAccessCache::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessCacheCall0 call = reinterpret_cast<CuteQNetworkAccessCacheCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QNetworkAccessCache::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessCacheCall1 call = reinterpret_cast<CuteQNetworkAccessCacheCall1>(taken[1]);
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
      CuteQNetworkAccessCacheCall2 call = reinterpret_cast<CuteQNetworkAccessCacheCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessCacheCall3 call = reinterpret_cast<CuteQNetworkAccessCacheCall3>(taken[3]);
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
      CuteQNetworkAccessCacheCall4 call = reinterpret_cast<CuteQNetworkAccessCacheCall4>(taken[4]);
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
      CuteQNetworkAccessCacheCall5 call = reinterpret_cast<CuteQNetworkAccessCacheCall5>(taken[5]);
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
      CuteQNetworkAccessCacheCall6 call = reinterpret_cast<CuteQNetworkAccessCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkAccessCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QNetworkAccessCache10metaObjectEv(
    const QNetworkAccessCache *self) {
  return self->metaObject();
}

//  void *QNetworkAccessCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QNetworkAccessCache11qt_metacastEPKc(
    QNetworkAccessCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkAccessCache::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QNetworkAccessCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkAccessCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNetworkAccessCache::~QNetworkAccessCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNetworkAccessCacheD1Ev(QNetworkAccessCache *self) {
  delete self;
}

//  bool QNetworkAccessCache::hasEntry(const QByteArray &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNetworkAccessCache8hasEntryERK10QByteArray(
    const QNetworkAccessCache *self,
    const QByteArray *key) {
  return self->hasEntry(*key);
}

//  void QNetworkAccessCache::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNetworkAccessCache10timerEventEP11QTimerEvent(
    QNetworkAccessCache *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  a Python function taken by a CuteQNetworkAccessCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessCache(
    QNetworkAccessCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessCache *>(self)->take(key, call);
}
