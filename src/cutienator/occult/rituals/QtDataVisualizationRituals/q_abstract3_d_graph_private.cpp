//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qabstract3dgraph_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dgraph_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/qabstract3dgraph.h>
#include <QtDataVisualization/private/qabstract3dgraph_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#include <QtDataVisualization/private/qabstract3dinputhandler_p.h>
#include <QtDataVisualization/private/q3dscene_p.h>
#include <QtDataVisualization/qutils.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QGuiApplication>
#include <QtGui/QOpenGLContext>
#include <QtOpenGL/QOpenGLPaintDevice>
#include <QtGui/QPainter>
#include <QtOpenGL/QOpenGLFramebufferObject>
#include <QtGui/QOffscreenSurface>
#if defined(Q_OS_MACOS)
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1134, as _ZN23QAbstract3DGraphPrivate11renderLaterEv
inline void QAbstract3DGraphPrivate::renderLater()
{
    if (!m_updatePending) {
        m_updatePending = true;
        QCoreApplication::postEvent(q_ptr, new QEvent(QEvent::UpdateRequest));
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1046, as _ZN23QAbstract3DGraphPrivateD1Ev
inline QAbstract3DGraphPrivate::~QAbstract3DGraphPrivate()
{
    if (m_offscreenSurface) {
        m_offscreenSurface->destroy();
        delete m_offscreenSurface;
    }
    if (m_context) {
        if (!m_context->makeCurrent(q_ptr))
            m_context->doneCurrent();
    }

    delete m_visualController;
}

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1118, as _ZN23QAbstract3DGraphPrivate28handleDevicePixelRatioChangeEv
inline void QAbstract3DGraphPrivate::handleDevicePixelRatioChange()
{
    if (q_ptr->devicePixelRatio() == m_devicePixelRatio || !m_visualController)
        return;

    m_devicePixelRatio = q_ptr->devicePixelRatio();
    m_visualController->scene()->setDevicePixelRatio(m_devicePixelRatio);
}

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1127, as _ZN23QAbstract3DGraphPrivate6renderEv
inline void QAbstract3DGraphPrivate::render()
{
    handleDevicePixelRatioChange();
    m_visualController->synchDataToRenderer();
    m_visualController->render();
}
//  -----------------------------------------------------------------------

//  A QAbstract3DGraphPrivate that Python can take functions over in. Every QAbstract3DGraphPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstract3DGraphPrivateCall0)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQAbstract3DGraphPrivateCall1)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQAbstract3DGraphPrivateCall2)(const void *, QAbstract3DAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DGraphPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DGraphPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DGraphPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DGraphPrivate : public QAbstract3DGraphPrivate {
public:
  using QAbstract3DGraphPrivate::QAbstract3DGraphPrivate;
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

  //  void QAbstract3DGraphPrivate::handleAxisXChanged(QAbstract3DAxis
  //      *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DGraphPrivateCall0 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall0>(taken[0]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

  //  void QAbstract3DGraphPrivate::handleAxisYChanged(QAbstract3DAxis
  //      *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DGraphPrivateCall1 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall1>(taken[1]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

  //  void QAbstract3DGraphPrivate::handleAxisZChanged(QAbstract3DAxis
  //      *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DGraphPrivateCall2 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall2>(taken[2]);
      call(this, axis, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DGraphPrivateCall3 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall3>(taken[3]);
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
      CuteQAbstract3DGraphPrivateCall4 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall4>(taken[4]);
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
      CuteQAbstract3DGraphPrivateCall5 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall5>(taken[5]);
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
      CuteQAbstract3DGraphPrivateCall6 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall6>(taken[6]);
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
      CuteQAbstract3DGraphPrivateCall7 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall7>(taken[7]);
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
      CuteQAbstract3DGraphPrivateCall8 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall8>(taken[8]);
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
      CuteQAbstract3DGraphPrivateCall9 call = reinterpret_cast<CuteQAbstract3DGraphPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DGraphPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QAbstract3DGraphPrivate10metaObjectEv(
    const QAbstract3DGraphPrivate *self) {
  return self->metaObject();
}

//  void *QAbstract3DGraphPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QAbstract3DGraphPrivate11qt_metacastEPKc(
    QAbstract3DGraphPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstract3DGraphPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QAbstract3DGraphPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstract3DGraphPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QAbstract3DGraphPrivate::~QAbstract3DGraphPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivateD1Ev(QAbstract3DGraphPrivate *self) {
  delete self;
}

//  void QAbstract3DGraphPrivate::handleDevicePixelRatioChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate28handleDevicePixelRatioChangeEv(
    QAbstract3DGraphPrivate *self) {
  self->handleDevicePixelRatioChange();
}

//  void QAbstract3DGraphPrivate::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate6renderEv(
    QAbstract3DGraphPrivate *self) {
  self->render();
}

//  void QAbstract3DGraphPrivate::renderLater()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate11renderLaterEv(
    QAbstract3DGraphPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstract3DGraphPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "renderLater()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "renderLater()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstract3DGraphPrivate::renderNow()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate9renderNowEv(
    QAbstract3DGraphPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstract3DGraphPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "renderNow()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "renderNow()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstract3DGraphPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    QAbstract3DGraphPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void QAbstract3DGraphPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    QAbstract3DGraphPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void QAbstract3DGraphPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstract3DGraphPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    QAbstract3DGraphPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  a Python function taken by a CuteQAbstract3DGraphPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DGraphPrivate(
    QAbstract3DGraphPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DGraphPrivate *>(self)->take(key, call);
}
