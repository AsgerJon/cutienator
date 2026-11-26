//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 411, as _ZN24QQuick3DXrHapticFeedback10classBeginEv
inline void QQuick3DXrHapticFeedback::classBegin()
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 415, as _ZN24QQuick3DXrHapticFeedback17componentCompleteEv
inline void QQuick3DXrHapticFeedback::componentComplete()
{
    QQuick3DXrActionMapper::registerHapticEffect(this);
    m_componentComplete = true;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 536, as _ZN24QQuick3DXrHapticFeedback4stopEv
inline void QQuick3DXrHapticFeedback::stop()
{
    m_pending = false;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 527, as _ZN24QQuick3DXrHapticFeedback5startEv
inline void QQuick3DXrHapticFeedback::start()
{
    m_pending = true;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 406, as _ZN24QQuick3DXrHapticFeedbackD0Ev
inline QQuick3DXrHapticFeedback::~QQuick3DXrHapticFeedback()
{
    QQuick3DXrActionMapper::removeHapticEffect(this);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 79, as _ZN22QQuick3DXrActionMapper20registerHapticEffectE8QPointerI24QQuick3DXrHapticFeedbackE
inline void QQuick3DXrActionMapper::registerHapticEffect(QPointer<QQuick3DXrHapticFeedback> action)
{
    auto *that = instance();

    that->m_hapticData[size_t(action->controller())].m_hapticEffects.append(action);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 25, as _ZN22QQuick3DXrActionMapper8instanceEv
inline QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()
{
    static QQuick3DXrActionMapper instance;
    return &instance;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 11, as _ZN22QQuick3DXrActionMapperC1EP7QObject
inline QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent) : QObject(parent)
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 485, as _ZNK24QQuick3DXrHapticFeedback12hapticEffectEv
inline QQuick3DXrAbstractHapticEffect *QQuick3DXrHapticFeedback::hapticEffect() const
{
    return m_hapticEffect;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 432, as _ZNK24QQuick3DXrHapticFeedback10controllerEv
inline QQuick3DXrHapticFeedback::Controller QQuick3DXrHapticFeedback::controller() const
{
    return m_controller;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 454, as _ZN24QQuick3DXrHapticFeedback7triggerEv
inline bool QQuick3DXrHapticFeedback::trigger()
{
    return m_trigger;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 510, as _ZNK24QQuick3DXrHapticFeedback9conditionEv
inline enum QQuick3DXrHapticFeedback::Condition QQuick3DXrHapticFeedback::condition() const
{
    return m_condition;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 541, as _ZN24QQuick3DXrHapticFeedback12testAndClearEv
inline bool QQuick3DXrHapticFeedback::testAndClear()
{
    bool t = m_pending;
    m_pending = false;
    return t;
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrHapticFeedback that Python can take functions over in. Every QQuick3DXrHapticFeedback
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DXrHapticFeedbackCall0)(const void *, int *);
typedef void (*CuteQQuick3DXrHapticFeedbackCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrHapticFeedbackCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrHapticFeedbackCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrHapticFeedbackCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrHapticFeedbackCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrHapticFeedbackCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrHapticFeedbackCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrHapticFeedbackCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrHapticFeedback : public QQuick3DXrHapticFeedback {
public:
  using QQuick3DXrHapticFeedback::QQuick3DXrHapticFeedback;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DXrHapticFeedback::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall0 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DXrHapticFeedback::classBegin();
  }

  //  void QQuick3DXrHapticFeedback::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall1 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DXrHapticFeedback::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall2 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall3 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall4 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall5 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall6 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall7 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DXrHapticFeedbackCall8 call = reinterpret_cast<CuteQQuick3DXrHapticFeedbackCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrHapticFeedback::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DXrHapticFeedback10metaObjectEv(
    const QQuick3DXrHapticFeedback *self) {
  return self->metaObject();
}

//  void *QQuick3DXrHapticFeedback::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuick3DXrHapticFeedback11qt_metacastEPKc(
    QQuick3DXrHapticFeedback *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrHapticFeedback::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuick3DXrHapticFeedback11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrHapticFeedback *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DXrHapticFeedback::~QQuick3DXrHapticFeedback()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedbackD1Ev(
    QQuick3DXrHapticFeedback *self) {
  delete self;
}

//  void QQuick3DXrHapticFeedback::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback10classBeginEv(
    QQuick3DXrHapticFeedback *self) {
  self->classBegin();
}

//  void QQuick3DXrHapticFeedback::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback17componentCompleteEv(
    QQuick3DXrHapticFeedback *self) {
  self->componentComplete();
}

//  QQuick3DXrAbstractHapticEffect *QQuick3DXrHapticFeedback::hapticEffect()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DXrAbstractHapticEffect *ritual_ZNK24QQuick3DXrHapticFeedback12hapticEffectEv(
    const QQuick3DXrHapticFeedback *self) {
  return self->hapticEffect();
}

//  Controller QQuick3DXrHapticFeedback::controller() const
extern "C" Q_DECL_EXPORT
QQuick3DXrHapticFeedback::Controller ritual_ZNK24QQuick3DXrHapticFeedback10controllerEv(
    const QQuick3DXrHapticFeedback *self) {
  return self->controller();
}

//  bool QQuick3DXrHapticFeedback::trigger()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DXrHapticFeedback7triggerEv(
    QQuick3DXrHapticFeedback *self) {
  return self->trigger();
}

//  enum Condition QQuick3DXrHapticFeedback::condition() const
extern "C" Q_DECL_EXPORT
enum QQuick3DXrHapticFeedback::Condition *ritual_ZNK24QQuick3DXrHapticFeedback9conditionEv(
    const QQuick3DXrHapticFeedback *self) {
  return new enum QQuick3DXrHapticFeedback::Condition(self->condition());
}

//  bool QQuick3DXrHapticFeedback::testAndClear()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuick3DXrHapticFeedback12testAndClearEv(
    QQuick3DXrHapticFeedback *self) {
  return self->testAndClear();
}

//  void QQuick3DXrHapticFeedback::controllerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback17controllerChangedEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controllerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controllerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHapticFeedback::hapticEffectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback19hapticEffectChangedEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hapticEffectChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hapticEffectChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHapticFeedback::triggerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback14triggerChangedEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "triggerChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "triggerChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHapticFeedback::conditionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback16conditionChangedEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "conditionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "conditionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHapticFeedback::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback5startEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "start()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "start()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DXrHapticFeedback::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DXrHapticFeedback4stopEv(
    QQuick3DXrHapticFeedback *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DXrHapticFeedback")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stop()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stop()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuick3DXrHapticFeedback as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DXrHapticFeedback_QQmlParserStatus(
    QQuick3DXrHapticFeedback *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DXrHapticFeedback, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrHapticFeedback(
    QQuick3DXrHapticFeedback *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrHapticFeedback *>(self)->take(key, call);
}

//  void QQuick3DXrHapticFeedback::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DXrHapticFeedback10classBeginEv(
    QQuick3DXrHapticFeedback *self) {
  self->QQuick3DXrHapticFeedback::classBegin();
}

//  void QQuick3DXrHapticFeedback::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DXrHapticFeedback17componentCompleteEv(
    QQuick3DXrHapticFeedback *self) {
  self->QQuick3DXrHapticFeedback::componentComplete();
}

//  a enum QQuick3DXrHapticFeedback::Condition a ritual of
//      QQuick3DXrHapticFeedback gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DXrHapticFeedback__enum_QQuick3DXrHapticFeedback_Condition(
    enum QQuick3DXrHapticFeedback::Condition *self) {
  delete self;
}
