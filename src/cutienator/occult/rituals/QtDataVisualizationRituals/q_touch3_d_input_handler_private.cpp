//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qtouch3dinputhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qtouch3dinputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/private/q3dinputhandler_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#include <QtDataVisualization/private/qtouch3dinputhandler_p.h>
#include <QtCore/QTimer>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 10, as local:qtouch3dinputhandler.cpp:maxTapAndHoldJitter
static const float maxTapAndHoldJitter = 20.0f;

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 11, as local:qtouch3dinputhandler.cpp:maxPinchJitter
static const int maxPinchJitter = 10;

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 13, as local:qtouch3dinputhandler.cpp:maxSelectionJitter
#if defined (Q_OS_ANDROID) || defined(Q_OS_IOS)
static const int maxSelectionJitter = 10;
#endif  // defined (Q_OS_ANDROID) || defined(Q_OS_IOS)

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 17, as local:qtouch3dinputhandler.cpp:tapAndHoldTime
static const int tapAndHoldTime = 250;

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 18, as local:qtouch3dinputhandler.cpp:t3ihRotationSpeed
static const float t3ihRotationSpeed = 200.0f;

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 19, as local:qtouch3dinputhandler.cpp:touchZoomDrift
static const float touchZoomDrift = 0.02f;

//  from ../qtdatavis3d/src/datavisualization/input/q3dinputhandler.cpp, line 337, as _ZN22Q3DInputHandlerPrivateC2EP15Q3DInputHandler
inline Q3DInputHandlerPrivate::Q3DInputHandlerPrivate(Q3DInputHandler *q)
    : q_ptr(q),
      m_inputState(QAbstract3DInputHandlerPrivate::InputStateNone),
      m_rotationEnabled(true),
      m_zoomEnabled(true),
      m_selectionEnabled(true),
      m_zoomAtTargetEnabled(true),
      m_zoomAtTargetPending(false),
      m_controller(0),
      m_requestedZoomLevel(0.0f),
      m_driftMultiplier(0.0f)
{
    QObject::connect(q, &QAbstract3DInputHandler::sceneChanged,
                     this, &Q3DInputHandlerPrivate::handleSceneChange);
}

//  from ../qtdatavis3d/src/datavisualization/input/q3dinputhandler.cpp, line 353, as _ZN22Q3DInputHandlerPrivateD2Ev
inline Q3DInputHandlerPrivate::~Q3DInputHandlerPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 165, as _ZN27QTouch3DInputHandlerPrivateD1Ev
inline QTouch3DInputHandlerPrivate::~QTouch3DInputHandlerPrivate()
{
    m_holdTimer->stop();
    delete m_holdTimer;
}

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 171, as _ZN27QTouch3DInputHandlerPrivate15handlePinchZoomEfRK6QPoint
inline void QTouch3DInputHandlerPrivate::handlePinchZoom(float distance, const QPoint &pos)
{
    if (q_ptr->isZoomEnabled()) {
        int newDistance = distance;
        int prevDist = q_ptr->prevDistance();
        if (prevDist > 0 && qAbs(prevDist - newDistance) < maxPinchJitter)
            return;
        m_inputState = QAbstract3DInputHandlerPrivate::InputStatePinching;
        Q3DCamera *camera = q_ptr->scene()->activeCamera();
        int zoomLevel = int(camera->zoomLevel());
        const int minZoomLevel = int(camera->minZoomLevel());
        const int maxZoomLevel = int(camera->maxZoomLevel());
        float zoomRate = qSqrt(qSqrt(zoomLevel));
        if (newDistance > prevDist)
            zoomLevel += zoomRate;
        else
            zoomLevel -= zoomRate;
        zoomLevel = qBound(minZoomLevel, zoomLevel, maxZoomLevel);

        if (q_ptr->isZoomAtTargetEnabled()) {
            q_ptr->scene()->setGraphPositionQuery(pos);
            m_zoomAtTargetPending = true;
            // If zoom at target is enabled, we don't want to zoom yet, as that causes
            // jitter. Instead, we zoom next frame, when we apply the camera position.
            m_requestedZoomLevel = zoomLevel;
            m_driftMultiplier = touchZoomDrift;
        } else {
            camera->setZoomLevel(zoomLevel);
        }

        q_ptr->setPrevDistance(newDistance);
    }
}

//  from ../qtdatavis3d/src/datavisualization/input/qtouch3dinputhandler.cpp, line 205, as _ZN27QTouch3DInputHandlerPrivate16handleTapAndHoldEv
inline void QTouch3DInputHandlerPrivate::handleTapAndHold()
{
    if (q_ptr->isSelectionEnabled()) {
        QPointF distance = m_startHoldPos - m_touchHoldPos;
        if (distance.manhattanLength() < maxTapAndHoldJitter) {
            q_ptr->setInputPosition(m_touchHoldPos.toPoint());
            q_ptr->scene()->setSelectionQueryPosition(m_touchHoldPos.toPoint());
            m_inputState = QAbstract3DInputHandlerPrivate::InputStateSelecting;
        }
    }
}
//  -----------------------------------------------------------------------

//  A QTouch3DInputHandlerPrivate that Python can take functions over in. Every QTouch3DInputHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTouch3DInputHandlerPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTouch3DInputHandlerPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTouch3DInputHandlerPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTouch3DInputHandlerPrivate : public QTouch3DInputHandlerPrivate {
public:
  using QTouch3DInputHandlerPrivate::QTouch3DInputHandlerPrivate;
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
      CuteQTouch3DInputHandlerPrivateCall0 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall0>(taken[0]);
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
      CuteQTouch3DInputHandlerPrivateCall1 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall1>(taken[1]);
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
      CuteQTouch3DInputHandlerPrivateCall2 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall2>(taken[2]);
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
      CuteQTouch3DInputHandlerPrivateCall3 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall3>(taken[3]);
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
      CuteQTouch3DInputHandlerPrivateCall4 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall4>(taken[4]);
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
      CuteQTouch3DInputHandlerPrivateCall5 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall5>(taken[5]);
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
      CuteQTouch3DInputHandlerPrivateCall6 call = reinterpret_cast<CuteQTouch3DInputHandlerPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTouch3DInputHandlerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QTouch3DInputHandlerPrivate10metaObjectEv(
    const QTouch3DInputHandlerPrivate *self) {
  return self->metaObject();
}

//  void *QTouch3DInputHandlerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QTouch3DInputHandlerPrivate11qt_metacastEPKc(
    QTouch3DInputHandlerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTouch3DInputHandlerPrivate::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QTouch3DInputHandlerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QTouch3DInputHandlerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QTouch3DInputHandlerPrivate::~QTouch3DInputHandlerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTouch3DInputHandlerPrivateD1Ev(
    QTouch3DInputHandlerPrivate *self) {
  delete self;
}

//  void QTouch3DInputHandlerPrivate::handlePinchZoom(float distance, const
//      QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTouch3DInputHandlerPrivate15handlePinchZoomEfRK6QPoint(
    QTouch3DInputHandlerPrivate *self,
    float distance,
    const QPoint *pos) {
  self->handlePinchZoom(distance, *pos);
}

//  void QTouch3DInputHandlerPrivate::handleTapAndHold()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTouch3DInputHandlerPrivate16handleTapAndHoldEv(
    QTouch3DInputHandlerPrivate *self) {
  self->handleTapAndHold();
}

//  a Python function taken by a CuteQTouch3DInputHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTouch3DInputHandlerPrivate(
    QTouch3DInputHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTouch3DInputHandlerPrivate *>(self)->take(key, call);
}
