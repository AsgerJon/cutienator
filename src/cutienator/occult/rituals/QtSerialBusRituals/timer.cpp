//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'Timer' is pasted in, cut
//  from what the moc of Qt 6.12.0 writes for its header: Qt's library keeps
//  it to itself; added are 3 rituals that lean on what moc writes for a
//  class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtSerialBus/qtserialbusglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(modbus_serialport)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtSerialBus__Timer.cpp, line 1, as moc:Timer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN5TimerE_t {};
} // unnamed namespace

template <> constexpr inline auto Timer::qt_create_metaobjectdata<qt_meta_tag_ZN5TimerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Timer",
        "timeout",
        "",
        "timerId"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'timeout'
        QtMocHelpers::SignalData<void(int)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 3 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Timer, qt_meta_tag_ZN5TimerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Timer::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN5TimerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN5TimerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN5TimerE_t>.metaTypes,
    nullptr
} };

void Timer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Timer *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->timeout((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (Timer::*)(int )>(_a, &Timer::timeout, 0))
            return;
    }
}

const QMetaObject *Timer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Timer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN5TimerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Timer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
void Timer::timeout(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *Timer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5Timer10metaObjectEv(const Timer *self) {
  return self->metaObject();
}

//  void *Timer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN5Timer11qt_metacastEPKc(Timer *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Timer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN5Timer11qt_metacallEN11QMetaObject4CallEiPPv(
    Timer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Timer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5Timer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Timer::tr(s, c, n));
}

//  Timer::Timer()
extern "C" Q_DECL_EXPORT
Timer *ritual_ZN5TimerC1Ev() {
  return new Timer();
}

//  int Timer::start(int msec)
extern "C" Q_DECL_EXPORT
int ritual_ZN5Timer5startEi(Timer *self, int msec) {
  return self->start(msec);
}

//  void Timer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer4stopEv(Timer *self) {
  self->stop();
}

//  bool Timer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Timer8isActiveEv(const Timer *self) {
  return self->isActive();
}

//  void Timer::timeout(int timerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer7timeoutEi(Timer *self, int timerId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Timer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "timeout(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "timeout(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&timerId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Timer::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer10timerEventEP11QTimerEvent(
    Timer *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void Timer::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5Timer10timerEventEP11QTimerEvent(
    Timer *self,
    QTimerEvent *event) {
  self->Timer::timerEvent(event);
}

#endif  // QT_CONFIG(modbus_serialport)
