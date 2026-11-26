//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QDBusPendingCallWatcherHelper' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  3 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbuserror.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDBus/qdbuspendingcall.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qlocking_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtDBus__QDBusPendingCallWatcherHelper.cpp, line 1, as moc:QDBusPendingCallWatcherHelper
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t {};
} // unnamed namespace

template <> constexpr inline auto QDBusPendingCallWatcherHelper::qt_create_metaobjectdata<qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QDBusPendingCallWatcherHelper",
        "finished",
        "",
        "reply",
        "QDBusMessage",
        "msg",
        "error",
        "QDBusError"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'finished'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'reply'
        QtMocHelpers::SignalData<void(const QDBusMessage &)>(3, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 4, 5 },
        }}),
        // Signal 'error'
        QtMocHelpers::SignalData<void(const QDBusError &, const QDBusMessage &)>(6, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 7, 6 }, { 0x80000000 | 4, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QDBusPendingCallWatcherHelper, qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QDBusPendingCallWatcherHelper::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>.metaTypes,
    nullptr
} };

void QDBusPendingCallWatcherHelper::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QDBusPendingCallWatcherHelper *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->finished(); break;
        case 1: _t->reply((*reinterpret_cast<std::add_pointer_t<QDBusMessage>>(_a[1]))); break;
        case 2: _t->error((*reinterpret_cast<std::add_pointer_t<QDBusError>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QDBusMessage>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusMessage >(); break;
            }
            break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusError >(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusMessage >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QDBusPendingCallWatcherHelper::*)()>(_a, &QDBusPendingCallWatcherHelper::finished, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QDBusPendingCallWatcherHelper::*)(const QDBusMessage & )>(_a, &QDBusPendingCallWatcherHelper::reply, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QDBusPendingCallWatcherHelper::*)(const QDBusError & , const QDBusMessage & )>(_a, &QDBusPendingCallWatcherHelper::error, 2))
            return;
    }
}

const QMetaObject *QDBusPendingCallWatcherHelper::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QDBusPendingCallWatcherHelper::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDBusPendingCallWatcherHelperE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QDBusPendingCallWatcherHelper::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QDBusPendingCallWatcherHelper::finished()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QDBusPendingCallWatcherHelper::reply(const QDBusMessage & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void QDBusPendingCallWatcherHelper::error(const QDBusError & _t1, const QDBusMessage & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from src/dbus/qdbuspendingcall.cpp, line 96, as _ZN29QDBusPendingCallWatcherHelper3addEP23QDBusPendingCallWatcher
#if !defined(QT_NO_DBUS)
inline void QDBusPendingCallWatcherHelper::add(QDBusPendingCallWatcher *watcher)
{
    connect(this, &QDBusPendingCallWatcherHelper::finished, watcher,
            [watcher] { Q_EMIT watcher->finished(watcher); }, Qt::QueuedConnection);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

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

//  QString QDBusPendingCallWatcherHelper::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDBusPendingCallWatcherHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusPendingCallWatcherHelper::tr(s, c, n));
}

#if !defined(QT_NO_DBUS)
//  void QDBusPendingCallWatcherHelper::add(QDBusPendingCallWatcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusPendingCallWatcherHelper3addEP23QDBusPendingCallWatcher(
    QDBusPendingCallWatcherHelper *self,
    QDBusPendingCallWatcher *watcher) {
  self->add(watcher);
}
#endif  // !defined(QT_NO_DBUS)

//  void QDBusPendingCallWatcherHelper::emitSignals(const QDBusMessage
//      &replyMessage, const QDBusMessage &sentMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusPendingCallWatcherHelper11emitSignalsERK12QDBusMessageS2_(
    QDBusPendingCallWatcherHelper *self,
    const QDBusMessage *replyMessage,
    const QDBusMessage *sentMessage) {
  self->emitSignals(*replyMessage, *sentMessage);
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
