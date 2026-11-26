//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbuserror.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusPendingCallWatcherHelper that Python can take functions over in. Every QDBusPendingCallWatcherHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPendingCallWatcherHelperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPendingCallWatcherHelperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherHelperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherHelperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherHelperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherHelperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherHelperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusPendingCallWatcherHelper : public QDBusPendingCallWatcherHelper {
public:
  using QDBusPendingCallWatcherHelper::QDBusPendingCallWatcherHelper;
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
      CuteQDBusPendingCallWatcherHelperCall0 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall0>(taken[0]);
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
      CuteQDBusPendingCallWatcherHelperCall1 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall1>(taken[1]);
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
      CuteQDBusPendingCallWatcherHelperCall2 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall2>(taken[2]);
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
      CuteQDBusPendingCallWatcherHelperCall3 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall3>(taken[3]);
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
      CuteQDBusPendingCallWatcherHelperCall4 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall4>(taken[4]);
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
      CuteQDBusPendingCallWatcherHelperCall5 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall5>(taken[5]);
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
      CuteQDBusPendingCallWatcherHelperCall6 call = reinterpret_cast<CuteQDBusPendingCallWatcherHelperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusPendingCallWatcherHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDBusPendingCallWatcherHelper10metaObjectEv(
    const QDBusPendingCallWatcherHelper *self) {
  return self->metaObject();
}

//  void *QDBusPendingCallWatcherHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QDBusPendingCallWatcherHelper11qt_metacastEPKc(
    QDBusPendingCallWatcherHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusPendingCallWatcherHelper::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QDBusPendingCallWatcherHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusPendingCallWatcherHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QDBusPendingCallWatcherHelper::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusPendingCallWatcherHelper8finishedEv(
    QDBusPendingCallWatcherHelper *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPendingCallWatcherHelper")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusPendingCallWatcherHelper::reply(const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusPendingCallWatcherHelper5replyERK12QDBusMessage(
    QDBusPendingCallWatcherHelper *self,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPendingCallWatcherHelper")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "reply(const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "reply(const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusPendingCallWatcherHelper::error(const QDBusError &error, const
//      QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusPendingCallWatcherHelper5errorERK10QDBusErrorRK12QDBusMessage(
    QDBusPendingCallWatcherHelper *self,
    const QDBusError *error,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPendingCallWatcherHelper")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "error(const QDBusError &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "error(const QDBusError &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(error)),
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQDBusPendingCallWatcherHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusPendingCallWatcherHelper(
    QDBusPendingCallWatcherHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusPendingCallWatcherHelper *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
