//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSmoothedAnimationTimer'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Edited by hand on 2026-11-27: the
//  constructors and the destructor of QSmoothedAnimationTimer taken from Qt
//  are no longer 'inline' (2): the one definition the target file has of
//  each, which the ritual files of other classes of the part call, as
//  Microsoft's ABI emits an 'inline' one only where it is used. Kept as it
//  is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquicksmoothedanimation_p.h>
#include <QtQuick/private/qquicksmoothedanimation_p_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQml/private/qcontinuinganimationgroupjob_p.h>
#include <QtCore/qmath.h>
#include <QtQml/qqmlproperty.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QSmoothedAnimationTimer.cpp, line 1, as moc:QSmoothedAnimationTimer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QSmoothedAnimationTimerE_t {};
} // unnamed namespace

template <> constexpr inline auto QSmoothedAnimationTimer::qt_create_metaobjectdata<qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSmoothedAnimationTimer",
        "stopAnimation",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'stopAnimation'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSmoothedAnimationTimer, qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSmoothedAnimationTimer::staticMetaObject = { {
    QMetaObject::SuperData::link<QTimer::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>.metaTypes,
    nullptr
} };

void QSmoothedAnimationTimer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSmoothedAnimationTimer *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->stopAnimation(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QSmoothedAnimationTimer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSmoothedAnimationTimer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSmoothedAnimationTimerE_t>.strings))
        return static_cast<void*>(this);
    return QTimer::qt_metacast(_clname);
}

int QSmoothedAnimationTimer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTimer::qt_metacall(_c, _id, _a);
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
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 36, as _ZN23QSmoothedAnimationTimer13stopAnimationEv
inline void QSmoothedAnimationTimer::stopAnimation()
{
    m_animation->stop();
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 25, as _ZN23QSmoothedAnimationTimerC1EP18QSmoothedAnimationP7QObject
QSmoothedAnimationTimer::QSmoothedAnimationTimer(QSmoothedAnimation *animation, QObject *parent)
    : QTimer(parent)
    , m_animation(animation)
{
    connect(this, SIGNAL(timeout()), this, SLOT(stopAnimation()));
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 32, as _ZN23QSmoothedAnimationTimerD1Ev
QSmoothedAnimationTimer::~QSmoothedAnimationTimer()
{
}
//  -----------------------------------------------------------------------

//  A QSmoothedAnimationTimer that Python can take functions over in. Every QSmoothedAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSmoothedAnimationTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSmoothedAnimationTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSmoothedAnimationTimer : public QSmoothedAnimationTimer {
public:
  using QSmoothedAnimationTimer::QSmoothedAnimationTimer;
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
  //  void QTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSmoothedAnimationTimerCall0 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTimer::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSmoothedAnimationTimerCall1 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall1>(taken[1]);
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
      CuteQSmoothedAnimationTimerCall2 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall2>(taken[2]);
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
      CuteQSmoothedAnimationTimerCall3 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall3>(taken[3]);
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
      CuteQSmoothedAnimationTimerCall4 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall4>(taken[4]);
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
      CuteQSmoothedAnimationTimerCall5 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall5>(taken[5]);
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
      CuteQSmoothedAnimationTimerCall6 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSmoothedAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QSmoothedAnimationTimer10metaObjectEv(
    const QSmoothedAnimationTimer *self) {
  return self->metaObject();
}

//  void *QSmoothedAnimationTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QSmoothedAnimationTimer11qt_metacastEPKc(
    QSmoothedAnimationTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSmoothedAnimationTimer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QSmoothedAnimationTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSmoothedAnimationTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSmoothedAnimationTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QSmoothedAnimationTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSmoothedAnimationTimer::tr(s, c, n));
}

//  QSmoothedAnimationTimer::QSmoothedAnimationTimer(QSmoothedAnimation
//      *animation, QObject *parent)
extern "C" Q_DECL_EXPORT
QSmoothedAnimationTimer *ritual_ZN23QSmoothedAnimationTimerC1EP18QSmoothedAnimationP7QObject(
    QSmoothedAnimation *animation,
    QObject *parent) {
  return new CuteQSmoothedAnimationTimer(animation, parent);
}

//  QSmoothedAnimationTimer::~QSmoothedAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSmoothedAnimationTimerD1Ev(QSmoothedAnimationTimer *self) {
  delete self;
}

//  void QSmoothedAnimationTimer::stopAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSmoothedAnimationTimer13stopAnimationEv(
    QSmoothedAnimationTimer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSmoothedAnimationTimer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stopAnimation()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stopAnimation()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQSmoothedAnimationTimer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSmoothedAnimationTimer(
    QSmoothedAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSmoothedAnimationTimer *>(self)->take(key, call);
}
