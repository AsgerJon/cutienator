//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmapcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmapcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickpixmapcache_p.h>
#include <QtQuick/private/qquickimageprovider_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgtexturereader_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qimage_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qimagereader.h>
#include <QtGui/qpixmapcache.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qhash.h>
#include <QtCore/qfile.h>
#include <QtCore/qthread.h>
#include <QtCore/qmutex.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#if QT_CONFIG(qml_network)
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qsslerror.h>
#endif
#include <QtCore/private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 48, as local:qquickpixmapcache.cpp:CACHE_REMOVAL_FRACTION
#define CACHE_REMOVAL_FRACTION 4

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 146, as local:qquickpixmapcache.cpp:QQuickPixmapData
class QQuickPixmapData;

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 1258, as _ZN17QQuickPixmapCacheD1Ev
inline QQuickPixmapCache::~QQuickPixmapCache()
{
    destroyCache();
}

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 1401, as _ZN17QQuickPixmapCache10timerEventEP11QTimerEvent
inline void QQuickPixmapCache::timerEvent(QTimerEvent *)
{
    int removalCost = m_unreferencedCost / CACHE_REMOVAL_FRACTION;

    shrinkCache(removalCost);

    if (m_unreferencedPixmaps == nullptr) {
        killTimer(m_timerId);
        m_timerId = -1;
    }
}
//  -----------------------------------------------------------------------

//  A QQuickPixmapCache that Python can take functions over in. Every QQuickPixmapCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPixmapCacheCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPixmapCacheCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPixmapCacheCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPixmapCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPixmapCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPixmapCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPixmapCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPixmapCache : public QQuickPixmapCache {
public:
  using QQuickPixmapCache::QQuickPixmapCache;
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
  //  void QQuickPixmapCache::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPixmapCacheCall0 call = reinterpret_cast<CuteQQuickPixmapCacheCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPixmapCache::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPixmapCacheCall1 call = reinterpret_cast<CuteQQuickPixmapCacheCall1>(taken[1]);
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
      CuteQQuickPixmapCacheCall2 call = reinterpret_cast<CuteQQuickPixmapCacheCall2>(taken[2]);
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
      CuteQQuickPixmapCacheCall3 call = reinterpret_cast<CuteQQuickPixmapCacheCall3>(taken[3]);
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
      CuteQQuickPixmapCacheCall4 call = reinterpret_cast<CuteQQuickPixmapCacheCall4>(taken[4]);
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
      CuteQQuickPixmapCacheCall5 call = reinterpret_cast<CuteQQuickPixmapCacheCall5>(taken[5]);
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
      CuteQQuickPixmapCacheCall6 call = reinterpret_cast<CuteQQuickPixmapCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPixmapCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickPixmapCache10metaObjectEv(
    const QQuickPixmapCache *self) {
  return self->metaObject();
}

//  void *QQuickPixmapCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickPixmapCache11qt_metacastEPKc(
    QQuickPixmapCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPixmapCache::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickPixmapCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPixmapCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickPixmapCache::~QQuickPixmapCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPixmapCacheD1Ev(QQuickPixmapCache *self) {
  delete self;
}

//  void QQuickPixmapCache::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPixmapCache10timerEventEP11QTimerEvent(
    QQuickPixmapCache *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  a Python function taken by a CuteQQuickPixmapCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPixmapCache(
    QQuickPixmapCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPixmapCache *>(self)->take(key, call);
}
