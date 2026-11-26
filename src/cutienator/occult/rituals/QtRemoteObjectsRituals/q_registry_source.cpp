//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectregistrysource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtCore/qdatastream.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 19, as _ZNK15QRegistrySource15sourceLocationsEv
inline QRemoteObjectSourceLocations QRegistrySource::sourceLocations() const
{
    qCDebug(QT_REMOTEOBJECT) << "sourceLocations property requested on RegistrySource" << m_sourceLocations;
    return m_sourceLocations;
}
//  -----------------------------------------------------------------------

//  A QRegistrySource that Python can take functions over in. Every QRegistrySource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRegistrySourceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRegistrySourceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRegistrySource : public QRegistrySource {
public:
  using QRegistrySource::QRegistrySource;
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
      CuteQRegistrySourceCall0 call = reinterpret_cast<CuteQRegistrySourceCall0>(taken[0]);
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
      CuteQRegistrySourceCall1 call = reinterpret_cast<CuteQRegistrySourceCall1>(taken[1]);
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
      CuteQRegistrySourceCall2 call = reinterpret_cast<CuteQRegistrySourceCall2>(taken[2]);
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
      CuteQRegistrySourceCall3 call = reinterpret_cast<CuteQRegistrySourceCall3>(taken[3]);
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
      CuteQRegistrySourceCall4 call = reinterpret_cast<CuteQRegistrySourceCall4>(taken[4]);
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
      CuteQRegistrySourceCall5 call = reinterpret_cast<CuteQRegistrySourceCall5>(taken[5]);
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
      CuteQRegistrySourceCall6 call = reinterpret_cast<CuteQRegistrySourceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRegistrySource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QRegistrySource10metaObjectEv(
    const QRegistrySource *self) {
  return self->metaObject();
}

//  void *QRegistrySource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QRegistrySource11qt_metacastEPKc(
    QRegistrySource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRegistrySource::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QRegistrySource11qt_metacallEN11QMetaObject4CallEiPPv(
    QRegistrySource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QRegistrySource::~QRegistrySource()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySourceD1Ev(QRegistrySource *self) {
  delete self;
}

//  QRemoteObjectSourceLocations QRegistrySource::sourceLocations() const
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_ZNK15QRegistrySource15sourceLocationsEv(
    const QRegistrySource *self) {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>(
      self->sourceLocations());
}

//  void QRegistrySource::remoteObjectAdded(const QRemoteObjectSourceLocation
//      &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource17remoteObjectAddedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectAdded(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectAdded(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::remoteObjectRemoved(const
//      QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource19remoteObjectRemovedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectRemoved(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectRemoved(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::addSource(const QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource9addSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "addSource(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "addSource(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::removeSource(const QRemoteObjectSourceLocation
//      &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource12removeSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeSource(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeSource(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::removeServer(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource12removeServerERK4QUrl(
    QRegistrySource *self,
    const QUrl *url) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeServer(const QUrl &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeServer(const QUrl &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(url)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQRegistrySource, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRegistrySource(
    QRegistrySource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRegistrySource *>(self)->take(key, call);
}
