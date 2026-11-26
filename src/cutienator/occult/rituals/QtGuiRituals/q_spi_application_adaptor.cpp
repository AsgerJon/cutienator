//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qspiapplicationadaptor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if __has_include(<QtGui/6.12.0/QtGui/private/qspiapplicationadaptor_p.h>)
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qspiapplicationadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbuserror.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qspiapplicationadaptor_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtDBus/qdbuspendingreply.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(accessibility)
#if __has_include(<xcb/xproto.h>)
#include <xcb/xproto.h>
#endif
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

//  from src/gui/accessible/linux/qspiapplicationadaptor.cpp, line 45, as _ZN22QSpiApplicationAdaptor10sendEventsEb
#if QT_CONFIG(accessibility)
inline void QSpiApplicationAdaptor::sendEvents(bool active)
{
    if (active) {
        qApp->installEventFilter(this);
    } else {
        qApp->removeEventFilter(this);
    }
}
#endif  // QT_CONFIG(accessibility)

//  from src/gui/accessible/linux/qspiapplicationadaptor.cpp, line 176, as _ZN22QSpiApplicationAdaptor12copyKeyEventEP9QKeyEvent
#if QT_CONFIG(accessibility)
inline QKeyEvent* QSpiApplicationAdaptor::copyKeyEvent(QKeyEvent* old)
{
    return new QKeyEvent(old->type(), old->key(), old->modifiers(),
                         old->nativeScanCode(), old->nativeVirtualKey(), old->nativeModifiers(),
                         old->text(), old->isAutoRepeat(), old->count());
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QSpiApplicationAdaptor that Python can take functions over in. Every QSpiApplicationAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQSpiApplicationAdaptorCall0)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(accessibility)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpiApplicationAdaptorCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiApplicationAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiApplicationAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiApplicationAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiApplicationAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiApplicationAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSpiApplicationAdaptor : public QSpiApplicationAdaptor {
public:
  using QSpiApplicationAdaptor::QSpiApplicationAdaptor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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
#if QT_CONFIG(accessibility)
  //  bool QSpiApplicationAdaptor::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpiApplicationAdaptorCall0 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall0>(taken[0]);
      bool given = call(this, obj, event, &handled);
      if (handled) return given;
    }
    return QSpiApplicationAdaptor::eventFilter(obj, event);
  }
#endif  // QT_CONFIG(accessibility)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpiApplicationAdaptorCall1 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpiApplicationAdaptorCall2 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall2>(taken[2]);
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
      CuteQSpiApplicationAdaptorCall3 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall3>(taken[3]);
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
      CuteQSpiApplicationAdaptorCall4 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall4>(taken[4]);
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
      CuteQSpiApplicationAdaptorCall5 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall5>(taken[5]);
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
      CuteQSpiApplicationAdaptorCall6 call = reinterpret_cast<CuteQSpiApplicationAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSpiApplicationAdaptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QSpiApplicationAdaptor10metaObjectEv(
    const QSpiApplicationAdaptor *self) {
  return self->metaObject();
}

//  void *QSpiApplicationAdaptor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QSpiApplicationAdaptor11qt_metacastEPKc(
    QSpiApplicationAdaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSpiApplicationAdaptor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QSpiApplicationAdaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QSpiApplicationAdaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSpiApplicationAdaptor::~QSpiApplicationAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpiApplicationAdaptorD1Ev(QSpiApplicationAdaptor *self) {
  delete self;
}

#if QT_CONFIG(accessibility)
//  void QSpiApplicationAdaptor::sendEvents(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpiApplicationAdaptor10sendEventsEb(
    QSpiApplicationAdaptor *self,
    bool active) {
  self->sendEvents(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QSpiApplicationAdaptor::windowActivated(QObject *window, bool
//      active)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpiApplicationAdaptor15windowActivatedEP7QObjectb(
    QSpiApplicationAdaptor *self,
    QObject *window,
    bool active) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSpiApplicationAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "windowActivated(QObject *,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "windowActivated(QObject *,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&window)),
      const_cast<void *>(static_cast<const void *>(&active)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QSpiApplicationAdaptor::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QSpiApplicationAdaptor11eventFilterEP7QObjectP6QEvent(
    QSpiApplicationAdaptor *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

//  void QSpiApplicationAdaptor::notifyKeyboardListenerCallback(const
//      QDBusMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpiApplicationAdaptor30notifyKeyboardListenerCallbackERK12QDBusMessage(
    QSpiApplicationAdaptor *self,
    const QDBusMessage *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSpiApplicationAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "notifyKeyboardListenerCallback(const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "notifyKeyboardListenerCallback(const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSpiApplicationAdaptor::notifyKeyboardListenerError(const QDBusError
//      &error, const QDBusMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpiApplicationAdaptor27notifyKeyboardListenerErrorERK10QDBusErrorRK12QDBusMessage(
    QSpiApplicationAdaptor *self,
    const QDBusError *error,
    const QDBusMessage *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSpiApplicationAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "notifyKeyboardListenerError(const QDBusError &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "notifyKeyboardListenerError(const QDBusError &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(error)),
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(accessibility)
//  QKeyEvent *QSpiApplicationAdaptor::copyKeyEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
QKeyEvent *ritual_ZN22QSpiApplicationAdaptor12copyKeyEventEP9QKeyEvent(
    QKeyEvent *a0) {
  return QSpiApplicationAdaptor::copyKeyEvent(a0);
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQSpiApplicationAdaptor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpiApplicationAdaptor(
    QSpiApplicationAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpiApplicationAdaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
#endif  // __has_include(<QtGui/6.12.0/QtGui/private/qspiapplicationadaptor_p.h>)
