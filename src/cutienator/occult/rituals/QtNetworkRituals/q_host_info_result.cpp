//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QHostInfoResult' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostinfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtNetwork/qhostinfo.h>
#include <QtNetwork/private/qhostinfo_p.h>
#include <qplatformdefs.h>
#include "QtCore/qapplicationstatic.h"
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/qurl.h>
#include <QtCore/private/qobject_p.h>
#include <algorithm>
#ifdef Q_OS_UNIX
#  include <unistd.h>
#  include <netdb.h>
#  include <netinet/in.h>
#elif defined Q_OS_WIN
#  include <ws2tcpip.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtNetwork__QHostInfoResult.cpp, line 1, as moc:QHostInfoResult
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QHostInfoResultE_t {};
} // unnamed namespace

template <> constexpr inline auto QHostInfoResult::qt_create_metaobjectdata<qt_meta_tag_ZN15QHostInfoResultE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QHostInfoResult",
        "resultsReady",
        "",
        "QHostInfo",
        "info",
        "finalizePostResultsReady"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'resultsReady'
        QtMocHelpers::SignalData<void(const QHostInfo &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'finalizePostResultsReady'
        QtMocHelpers::SlotData<void(const QHostInfo &)>(5, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QHostInfoResult, qt_meta_tag_ZN15QHostInfoResultE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QHostInfoResult::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QHostInfoResultE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QHostInfoResultE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QHostInfoResultE_t>.metaTypes,
    nullptr
} };

void QHostInfoResult::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QHostInfoResult *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->resultsReady((*reinterpret_cast<std::add_pointer_t<QHostInfo>>(_a[1]))); break;
        case 1: _t->finalizePostResultsReady((*reinterpret_cast<std::add_pointer_t<QHostInfo>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QHostInfo >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QHostInfo >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QHostInfoResult::*)(const QHostInfo & )>(_a, &QHostInfoResult::resultsReady, 0))
            return;
    }
}

const QMetaObject *QHostInfoResult::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QHostInfoResult::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QHostInfoResultE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QHostInfoResult::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QHostInfoResult::resultsReady(const QHostInfo & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from src/network/kernel/qhostinfo.cpp, line 122, as _ZN15QHostInfoResult24finalizePostResultsReadyERK9QHostInfo
inline void QHostInfoResult::finalizePostResultsReady(const QHostInfo &info)
{
    Q_ASSERT(slotObj);

    // we used to have a context object, but it's already destroyed
    if (receiver) {
        void *args[] = { nullptr, const_cast<QHostInfo *>(&info) };
        slotObj->call(const_cast<QObject *>(receiver.data()), args);
    }

    deleteLater();
}

//  from src/network/kernel/qhostinfo.cpp, line 84, as _ZN15QHostInfoResultD0Ev
inline QHostInfoResult::~QHostInfoResult()
    = default;

//  from src/network/kernel/qhostinfo.cpp, line 98, as _ZN15QHostInfoResult16postResultsReadyERK9QHostInfo
inline void QHostInfoResult::postResultsReady(const QHostInfo &info)
{
    // queued connection will take care of dispatching to right thread
    if (!slotObj) {
        emit resultsReady(info);
        return;
    }
    // we used to have a context object, but it's already destroyed
    if (!receiver)
        return;

    // a long-living version of this
    auto result = new QHostInfoResult(this);
    Q_CHECK_PTR(result);

    QMetaObject::invokeMethod(result,
                              &QHostInfoResult::finalizePostResultsReady,
                              Qt::QueuedConnection,
                              info);
}
//  -----------------------------------------------------------------------

//  A QHostInfoResult that Python can take functions over in. Every QHostInfoResult
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHostInfoResultCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHostInfoResultCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHostInfoResultCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHostInfoResultCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHostInfoResultCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHostInfoResultCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHostInfoResultCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHostInfoResult : public QHostInfoResult {
public:
  using QHostInfoResult::QHostInfoResult;
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
      CuteQHostInfoResultCall0 call = reinterpret_cast<CuteQHostInfoResultCall0>(taken[0]);
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
      CuteQHostInfoResultCall1 call = reinterpret_cast<CuteQHostInfoResultCall1>(taken[1]);
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
      CuteQHostInfoResultCall2 call = reinterpret_cast<CuteQHostInfoResultCall2>(taken[2]);
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
      CuteQHostInfoResultCall3 call = reinterpret_cast<CuteQHostInfoResultCall3>(taken[3]);
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
      CuteQHostInfoResultCall4 call = reinterpret_cast<CuteQHostInfoResultCall4>(taken[4]);
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
      CuteQHostInfoResultCall5 call = reinterpret_cast<CuteQHostInfoResultCall5>(taken[5]);
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
      CuteQHostInfoResultCall6 call = reinterpret_cast<CuteQHostInfoResultCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHostInfoResult::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QHostInfoResult10metaObjectEv(
    const QHostInfoResult *self) {
  return self->metaObject();
}

//  void *QHostInfoResult::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QHostInfoResult11qt_metacastEPKc(
    QHostInfoResult *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHostInfoResult::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QHostInfoResult11qt_metacallEN11QMetaObject4CallEiPPv(
    QHostInfoResult *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHostInfoResult::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHostInfoResult2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHostInfoResult::tr(s, c, n));
}

//  QHostInfoResult::~QHostInfoResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHostInfoResultD1Ev(QHostInfoResult *self) {
  delete self;
}

//  void QHostInfoResult::postResultsReady(const QHostInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHostInfoResult16postResultsReadyERK9QHostInfo(
    QHostInfoResult *self,
    const QHostInfo *info) {
  self->postResultsReady(*info);
}

//  void QHostInfoResult::resultsReady(const QHostInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHostInfoResult12resultsReadyERK9QHostInfo(
    QHostInfoResult *self,
    const QHostInfo *info) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHostInfoResult")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resultsReady(const QHostInfo &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resultsReady(const QHostInfo &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHostInfoResult::finalizePostResultsReady(const QHostInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHostInfoResult24finalizePostResultsReadyERK9QHostInfo(
    QHostInfoResult *self,
    const QHostInfo *info) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHostInfoResult")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finalizePostResultsReady(const QHostInfo &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finalizePostResultsReady(const QHostInfo &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QHostInfoResult::QHostInfoResult(QHostInfoResult *other)
extern "C" Q_DECL_EXPORT
QHostInfoResult *ritual_ZN15QHostInfoResultC1EPS_(QHostInfoResult *other) {
  return new CuteQHostInfoResult(other);
}

//  a Python function taken by a CuteQHostInfoResult, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHostInfoResult(
    QHostInfoResult *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHostInfoResult *>(self)->take(key, call);
}
