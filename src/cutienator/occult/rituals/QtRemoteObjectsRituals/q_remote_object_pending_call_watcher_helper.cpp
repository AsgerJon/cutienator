//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectpendingcall_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QRemoteObjectPendingCallWatcherHelper' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 3 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__QRemoteObjectPendingCallWatcherHelper.cpp, line 1, as moc:QRemoteObjectPendingCallWatcherHelper
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t {};
} // unnamed namespace

template <> constexpr inline auto QRemoteObjectPendingCallWatcherHelper::qt_create_metaobjectdata<qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QRemoteObjectPendingCallWatcherHelper",
        "finished",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'finished'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QRemoteObjectPendingCallWatcherHelper, qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QRemoteObjectPendingCallWatcherHelper::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>.metaTypes,
    nullptr
} };

void QRemoteObjectPendingCallWatcherHelper::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QRemoteObjectPendingCallWatcherHelper *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->finished(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QRemoteObjectPendingCallWatcherHelper::*)()>(_a, &QRemoteObjectPendingCallWatcherHelper::finished, 0))
            return;
    }
}

const QMetaObject *QRemoteObjectPendingCallWatcherHelper::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QRemoteObjectPendingCallWatcherHelper::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN37QRemoteObjectPendingCallWatcherHelperE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QRemoteObjectPendingCallWatcherHelper::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QRemoteObjectPendingCallWatcherHelper::finished()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpendingcall.cpp, line 30, as _ZN37QRemoteObjectPendingCallWatcherHelper3addEP31QRemoteObjectPendingCallWatcher
inline void QRemoteObjectPendingCallWatcherHelper::add(QRemoteObjectPendingCallWatcher *watcher)
{
    connect(this, &QRemoteObjectPendingCallWatcherHelper::finished, watcher, [watcher]() {
        emit watcher->finished(watcher);
    }, Qt::QueuedConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpendingcall.cpp, line 37, as _ZN37QRemoteObjectPendingCallWatcherHelper11emitSignalsEv
inline void QRemoteObjectPendingCallWatcherHelper::emitSignals()
{
    emit finished();
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectPendingCallWatcherHelper that Python can take functions over in. Every QRemoteObjectPendingCallWatcherHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectPendingCallWatcherHelperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectPendingCallWatcherHelperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherHelperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherHelperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherHelperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherHelperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherHelperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectPendingCallWatcherHelper : public QRemoteObjectPendingCallWatcherHelper {
public:
  using QRemoteObjectPendingCallWatcherHelper::QRemoteObjectPendingCallWatcherHelper;
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
      CuteQRemoteObjectPendingCallWatcherHelperCall0 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall0>(taken[0]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall1 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall1>(taken[1]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall2 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall2>(taken[2]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall3 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall3>(taken[3]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall4 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall4>(taken[4]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall5 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall5>(taken[5]);
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
      CuteQRemoteObjectPendingCallWatcherHelperCall6 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherHelperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectPendingCallWatcherHelper::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QRemoteObjectPendingCallWatcherHelper10metaObjectEv(
    const QRemoteObjectPendingCallWatcherHelper *self) {
  return self->metaObject();
}

//  void *QRemoteObjectPendingCallWatcherHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN37QRemoteObjectPendingCallWatcherHelper11qt_metacastEPKc(
    QRemoteObjectPendingCallWatcherHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRemoteObjectPendingCallWatcherHelper::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN37QRemoteObjectPendingCallWatcherHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QRemoteObjectPendingCallWatcherHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QRemoteObjectPendingCallWatcherHelper::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN37QRemoteObjectPendingCallWatcherHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectPendingCallWatcherHelper::tr(s, c, n));
}

//  void QRemoteObjectPendingCallWatcherHelper::add(QRemoteObjectPendingCallW
//      atcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QRemoteObjectPendingCallWatcherHelper3addEP31QRemoteObjectPendingCallWatcher(
    QRemoteObjectPendingCallWatcherHelper *self,
    QRemoteObjectPendingCallWatcher *watcher) {
  self->add(watcher);
}

//  void QRemoteObjectPendingCallWatcherHelper::emitSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QRemoteObjectPendingCallWatcherHelper11emitSignalsEv(
    QRemoteObjectPendingCallWatcherHelper *self) {
  self->emitSignals();
}

//  void QRemoteObjectPendingCallWatcherHelper::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QRemoteObjectPendingCallWatcherHelper8finishedEv(
    QRemoteObjectPendingCallWatcherHelper *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectPendingCallWatcherHelper")) {
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

//  a Python function taken by a CuteQRemoteObjectPendingCallWatcherHelper,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectPendingCallWatcherHelper(
    QRemoteObjectPendingCallWatcherHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectPendingCallWatcherHelper *>(self)->take(key, call);
}
