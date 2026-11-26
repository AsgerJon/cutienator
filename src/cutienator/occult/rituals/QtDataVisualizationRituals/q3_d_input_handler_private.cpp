//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/q3dinputhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dinputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/private/q3dinputhandler_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/input/q3dinputhandler.cpp, line 353, as _ZN22Q3DInputHandlerPrivateD1Ev
inline Q3DInputHandlerPrivate::~Q3DInputHandlerPrivate()
{
}
//  -----------------------------------------------------------------------

//  A Q3DInputHandlerPrivate that Python can take functions over in. Every Q3DInputHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DInputHandlerPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DInputHandlerPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DInputHandlerPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DInputHandlerPrivate : public Q3DInputHandlerPrivate {
public:
  using Q3DInputHandlerPrivate::Q3DInputHandlerPrivate;
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
      CuteQ3DInputHandlerPrivateCall0 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall0>(taken[0]);
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
      CuteQ3DInputHandlerPrivateCall1 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall1>(taken[1]);
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
      CuteQ3DInputHandlerPrivateCall2 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall2>(taken[2]);
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
      CuteQ3DInputHandlerPrivateCall3 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall3>(taken[3]);
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
      CuteQ3DInputHandlerPrivateCall4 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall4>(taken[4]);
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
      CuteQ3DInputHandlerPrivateCall5 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall5>(taken[5]);
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
      CuteQ3DInputHandlerPrivateCall6 call = reinterpret_cast<CuteQ3DInputHandlerPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DInputHandlerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22Q3DInputHandlerPrivate10metaObjectEv(
    const Q3DInputHandlerPrivate *self) {
  return self->metaObject();
}

//  void *Q3DInputHandlerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22Q3DInputHandlerPrivate11qt_metacastEPKc(
    Q3DInputHandlerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DInputHandlerPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22Q3DInputHandlerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DInputHandlerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Q3DInputHandlerPrivate::~Q3DInputHandlerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22Q3DInputHandlerPrivateD1Ev(Q3DInputHandlerPrivate *self) {
  delete self;
}

//  void Q3DInputHandlerPrivate::handleSceneChange(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN22Q3DInputHandlerPrivate17handleSceneChangeEP8Q3DScene(
    Q3DInputHandlerPrivate *self,
    Q3DScene *scene) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DInputHandlerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSceneChange(Q3DScene *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSceneChange(Q3DScene *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&scene)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Q3DInputHandlerPrivate::handleQueriedGraphPositionChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22Q3DInputHandlerPrivate32handleQueriedGraphPositionChangeEv(
    Q3DInputHandlerPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Q3DInputHandlerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleQueriedGraphPositionChange()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleQueriedGraphPositionChange()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQ3DInputHandlerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DInputHandlerPrivate(
    Q3DInputHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DInputHandlerPrivate *>(self)->take(key, call);
}
