//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qspidbuscache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if __has_include(<QtGui/6.12.0/QtGui/private/qspidbuscache_p.h>)
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qspidbuscache_p.h>
#include <QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qspidbuscache_p.h>
#include <QtGui/private/qspiaccessiblebridge_p.h>
#if QT_CONFIG(accessibility)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/accessible/linux/qspidbuscache.cpp, line 52, as _ZN13QSpiDBusCache8GetItemsEv
#if QT_CONFIG(accessibility)
inline QSpiAccessibleCacheArray QSpiDBusCache::GetItems()
{
    return QSpiAccessibleCacheArray();
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QSpiDBusCache that Python can take functions over in. Every QSpiDBusCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpiDBusCacheCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpiDBusCacheCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiDBusCacheCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiDBusCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiDBusCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiDBusCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiDBusCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSpiDBusCache : public QSpiDBusCache {
public:
  using QSpiDBusCache::QSpiDBusCache;
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
      CuteQSpiDBusCacheCall0 call = reinterpret_cast<CuteQSpiDBusCacheCall0>(taken[0]);
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
      CuteQSpiDBusCacheCall1 call = reinterpret_cast<CuteQSpiDBusCacheCall1>(taken[1]);
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
      CuteQSpiDBusCacheCall2 call = reinterpret_cast<CuteQSpiDBusCacheCall2>(taken[2]);
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
      CuteQSpiDBusCacheCall3 call = reinterpret_cast<CuteQSpiDBusCacheCall3>(taken[3]);
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
      CuteQSpiDBusCacheCall4 call = reinterpret_cast<CuteQSpiDBusCacheCall4>(taken[4]);
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
      CuteQSpiDBusCacheCall5 call = reinterpret_cast<CuteQSpiDBusCacheCall5>(taken[5]);
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
      CuteQSpiDBusCacheCall6 call = reinterpret_cast<CuteQSpiDBusCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSpiDBusCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSpiDBusCache10metaObjectEv(
    const QSpiDBusCache *self) {
  return self->metaObject();
}

//  void *QSpiDBusCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QSpiDBusCache11qt_metacastEPKc(
    QSpiDBusCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSpiDBusCache::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSpiDBusCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QSpiDBusCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QSpiDBusCache::AddAccessible(const QSpiAccessibleCacheItem
//      &nodeAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpiDBusCache13AddAccessibleERK23QSpiAccessibleCacheItem(
    QSpiDBusCache *self,
    const QSpiAccessibleCacheItem *nodeAdded) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSpiDBusCache")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "AddAccessible(const QSpiAccessibleCacheItem &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "AddAccessible(const QSpiAccessibleCacheItem &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(nodeAdded)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSpiDBusCache::RemoveAccessible(const QSpiObjectReference
//      &nodeRemoved)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSpiDBusCache16RemoveAccessibleERK19QSpiObjectReference(
    QSpiDBusCache *self,
    const QSpiObjectReference *nodeRemoved) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSpiDBusCache")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "RemoveAccessible(const QSpiObjectReference &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "RemoveAccessible(const QSpiObjectReference &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(nodeRemoved)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(accessibility)
//  QSpiAccessibleCacheArray QSpiDBusCache::GetItems()
extern "C" Q_DECL_EXPORT
QList<QSpiAccessibleCacheItem> *ritual_ZN13QSpiDBusCache8GetItemsEv(
    QSpiDBusCache *self) {
  return new QList<QSpiAccessibleCacheItem>(self->GetItems());
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQSpiDBusCache, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpiDBusCache(
    QSpiDBusCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpiDBusCache *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
#endif  // __has_include(<QtGui/6.12.0/QtGui/private/qspidbuscache_p.h>)
