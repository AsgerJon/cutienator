//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dbars_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dbars_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/q3dbars_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 453, as _ZN14Q3DBarsPrivateD1Ev
inline Q3DBarsPrivate::~Q3DBarsPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 457, as _ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
{
    emit qptr()->columnAxisChanged(static_cast<QCategory3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 462, as _ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
{
    emit qptr()->valueAxisChanged(static_cast<QValue3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 467, as _ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
{
    emit qptr()->rowAxisChanged(static_cast<QCategory3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 472, as _ZN14Q3DBarsPrivate4qptrEv
inline Q3DBars *Q3DBarsPrivate::qptr()
{
    return static_cast<Q3DBars *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A Q3DBarsPrivate that Python can take functions over in. Every Q3DBarsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQ3DBarsPrivateCall0)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DBarsPrivateCall1)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DBarsPrivateCall2)(const void *, QAbstract3DAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DBarsPrivate : public Q3DBarsPrivate {
public:
  using Q3DBarsPrivate::Q3DBarsPrivate;
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

  //  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall0 call = reinterpret_cast<CuteQ3DBarsPrivateCall0>(taken[0]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisXChanged(axis);
  }

  //  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall1 call = reinterpret_cast<CuteQ3DBarsPrivateCall1>(taken[1]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisYChanged(axis);
  }

  //  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall2 call = reinterpret_cast<CuteQ3DBarsPrivateCall2>(taken[2]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisZChanged(axis);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall3 call = reinterpret_cast<CuteQ3DBarsPrivateCall3>(taken[3]);
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
      CuteQ3DBarsPrivateCall4 call = reinterpret_cast<CuteQ3DBarsPrivateCall4>(taken[4]);
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
      CuteQ3DBarsPrivateCall5 call = reinterpret_cast<CuteQ3DBarsPrivateCall5>(taken[5]);
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
      CuteQ3DBarsPrivateCall6 call = reinterpret_cast<CuteQ3DBarsPrivateCall6>(taken[6]);
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
      CuteQ3DBarsPrivateCall7 call = reinterpret_cast<CuteQ3DBarsPrivateCall7>(taken[7]);
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
      CuteQ3DBarsPrivateCall8 call = reinterpret_cast<CuteQ3DBarsPrivateCall8>(taken[8]);
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
      CuteQ3DBarsPrivateCall9 call = reinterpret_cast<CuteQ3DBarsPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DBarsPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14Q3DBarsPrivate10metaObjectEv(
    const Q3DBarsPrivate *self) {
  return self->metaObject();
}

//  Q3DBarsPrivate::~Q3DBarsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivateD1Ev(Q3DBarsPrivate *self) {
  delete self;
}

//  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  Q3DBars *Q3DBarsPrivate::qptr()
extern "C" Q_DECL_EXPORT
Q3DBars *ritual_ZN14Q3DBarsPrivate4qptrEv(Q3DBarsPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQ3DBarsPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DBarsPrivate(
    Q3DBarsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DBarsPrivate *>(self)->take(key, call);
}

//  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisXChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisYChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisZChanged(axis);
}
