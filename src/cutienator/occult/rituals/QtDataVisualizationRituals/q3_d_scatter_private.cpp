//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dscatter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dscatter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/q3dscatter.h>
#include <QtDataVisualization/private/q3dscatter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/q3dscatter.cpp, line 273, as _ZN17Q3DScatterPrivate18handleAxisXChangedEP15QAbstract3DAxis
inline void Q3DScatterPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
{
    emit qptr()->axisXChanged(static_cast<QValue3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dscatter.cpp, line 278, as _ZN17Q3DScatterPrivate18handleAxisYChangedEP15QAbstract3DAxis
inline void Q3DScatterPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
{
    emit qptr()->axisYChanged(static_cast<QValue3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dscatter.cpp, line 283, as _ZN17Q3DScatterPrivate18handleAxisZChangedEP15QAbstract3DAxis
inline void Q3DScatterPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
{
    emit qptr()->axisZChanged(static_cast<QValue3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dscatter.cpp, line 269, as _ZN17Q3DScatterPrivateD1Ev
inline Q3DScatterPrivate::~Q3DScatterPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dscatter.cpp, line 288, as _ZN17Q3DScatterPrivate4qptrEv
inline Q3DScatter *Q3DScatterPrivate::qptr()
{
    return static_cast<Q3DScatter *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A Q3DScatterPrivate that Python can take functions over in. Every Q3DScatterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQ3DScatterPrivateCall0)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DScatterPrivateCall1)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DScatterPrivateCall2)(const void *, QAbstract3DAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DScatterPrivate : public Q3DScatterPrivate {
public:
  using Q3DScatterPrivate::Q3DScatterPrivate;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Q3DScatterPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall0 call = reinterpret_cast<CuteQ3DScatterPrivateCall0>(taken[0]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DScatterPrivate::handleAxisXChanged(axis);
  }

  //  void Q3DScatterPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall1 call = reinterpret_cast<CuteQ3DScatterPrivateCall1>(taken[1]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DScatterPrivate::handleAxisYChanged(axis);
  }

  //  void Q3DScatterPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall2 call = reinterpret_cast<CuteQ3DScatterPrivateCall2>(taken[2]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DScatterPrivate::handleAxisZChanged(axis);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall3 call = reinterpret_cast<CuteQ3DScatterPrivateCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall4 call = reinterpret_cast<CuteQ3DScatterPrivateCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall5 call = reinterpret_cast<CuteQ3DScatterPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall6 call = reinterpret_cast<CuteQ3DScatterPrivateCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall7 call = reinterpret_cast<CuteQ3DScatterPrivateCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall8 call = reinterpret_cast<CuteQ3DScatterPrivateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQ3DScatterPrivateCall9 call = reinterpret_cast<CuteQ3DScatterPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DScatterPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17Q3DScatterPrivate10metaObjectEv(
    const Q3DScatterPrivate *self) {
  return self->metaObject();
}

//  void *Q3DScatterPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17Q3DScatterPrivate11qt_metacastEPKc(
    Q3DScatterPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DScatterPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17Q3DScatterPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DScatterPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Q3DScatterPrivate::~Q3DScatterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DScatterPrivateD1Ev(Q3DScatterPrivate *self) {
  delete self;
}

//  void Q3DScatterPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DScatterPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void Q3DScatterPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DScatterPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void Q3DScatterPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DScatterPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  Q3DScatter *Q3DScatterPrivate::qptr()
extern "C" Q_DECL_EXPORT
Q3DScatter *ritual_ZN17Q3DScatterPrivate4qptrEv(Q3DScatterPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQ3DScatterPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScatterPrivate(
    Q3DScatterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DScatterPrivate *>(self)->take(key, call);
}

//  void Q3DScatterPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Q3DScatterPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DScatterPrivate::handleAxisXChanged(axis);
}

//  void Q3DScatterPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Q3DScatterPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DScatterPrivate::handleAxisYChanged(axis);
}

//  void Q3DScatterPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Q3DScatterPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DScatterPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DScatterPrivate::handleAxisZChanged(axis);
}
