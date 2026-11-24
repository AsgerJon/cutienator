//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmacgesturerecognizer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if defined(Q_OS_MACOS)
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmacgesturerecognizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmacgesturerecognizer_p.h"
#include "qgesture.h"
#include "qgesture_p.h"
#include "qevent.h"
#include "qwidget.h"
#include "qdebug.h"
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 55, as _ZN26QMacPinchGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QMacPinchGestureRecognizer::QMacPinchGestureRecognizer()
{
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 59, as _ZN26QMacPinchGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QMacPinchGestureRecognizer::create(QObject * /*target*/)
{
    return new QPinchGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 64, as _ZN26QMacPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result
QMacPinchGestureRecognizer::recognize(QGesture *gesture, QObject *obj, QEvent *event)
{
    if (event->type() == QEvent::NativeGesture && obj->isWidgetType()) {
        QPinchGesture *g = static_cast<QPinchGesture *>(gesture);
        QNativeGestureEvent *ev = static_cast<QNativeGestureEvent*>(event);
        switch (ev->gestureType()) {
        case Qt::BeginNativeGesture:
            reset(gesture);
            g->setStartCenterPoint(static_cast<QWidget*>(obj)->mapFromGlobal(ev->globalPosition()));
            g->setCenterPoint(g->startCenterPoint());
            g->setChangeFlags(QPinchGesture::CenterPointChanged);
            g->setTotalChangeFlags(g->totalChangeFlags() | g->changeFlags());
            g->setHotSpot(ev->globalPosition());
            return QGestureRecognizer::MayBeGesture | QGestureRecognizer::ConsumeEventHint;
        case Qt::RotateNativeGesture:
            g->setLastScaleFactor(g->scaleFactor());
            g->setLastRotationAngle(g->rotationAngle());
            g->setRotationAngle(g->rotationAngle() + ev->value());
            g->setChangeFlags(QPinchGesture::RotationAngleChanged);
            g->setTotalChangeFlags(g->totalChangeFlags() | g->changeFlags());
            g->setHotSpot(ev->globalPosition());
            return QGestureRecognizer::TriggerGesture | QGestureRecognizer::ConsumeEventHint;
        case Qt::ZoomNativeGesture:
            g->setLastScaleFactor(g->scaleFactor());
            g->setLastRotationAngle(g->rotationAngle());
            g->setScaleFactor(1 + ev->value());
            g->setTotalScaleFactor(g->totalScaleFactor() * g->scaleFactor());
            g->setChangeFlags(QPinchGesture::ScaleFactorChanged);
            g->setTotalChangeFlags(g->totalChangeFlags() | g->changeFlags());
            g->setHotSpot(ev->globalPosition());
            return QGestureRecognizer::TriggerGesture | QGestureRecognizer::ConsumeEventHint;
        case Qt::SmartZoomNativeGesture:
            g->setLastScaleFactor(g->scaleFactor());
            g->setLastRotationAngle(g->rotationAngle());
            g->setScaleFactor(ev->value() ? 1.7f : 1.0f);
            g->setChangeFlags(QPinchGesture::ScaleFactorChanged);
            g->setTotalChangeFlags(g->totalChangeFlags() | g->changeFlags());
            g->setHotSpot(ev->globalPosition());
            return QGestureRecognizer::TriggerGesture | QGestureRecognizer::ConsumeEventHint;
        case Qt::EndNativeGesture:
            return QGestureRecognizer::FinishGesture | QGestureRecognizer::ConsumeEventHint;
        default:
            break;
        }
    }

    return QGestureRecognizer::Ignore;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 114, as _ZN26QMacPinchGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QMacPinchGestureRecognizer::reset(QGesture *gesture)
{
    QPinchGesture *g = static_cast<QPinchGesture *>(gesture);
    g->setChangeFlags({});
    g->setTotalChangeFlags({});
    g->setScaleFactor(1.0f);
    g->setTotalScaleFactor(1.0f);
    g->setLastScaleFactor(1.0f);
    g->setRotationAngle(0.0f);
    g->setTotalRotationAngle(0.0f);
    g->setLastRotationAngle(0.0f);
    g->setCenterPoint(QPointF());
    g->setStartCenterPoint(QPointF());
    g->setLastCenterPoint(QPointF());
    QGestureRecognizer::reset(gesture);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QMacPinchGestureRecognizer that Python can take functions over in. Every QMacPinchGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQMacPinchGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQMacPinchGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQMacPinchGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQMacPinchGestureRecognizer : public QMacPinchGestureRecognizer {
public:
  using QMacPinchGestureRecognizer::QMacPinchGestureRecognizer;
  CuteQMacPinchGestureRecognizer(const QMacPinchGestureRecognizer &other) : QMacPinchGestureRecognizer(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer6createEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer5resetEP8QGesture")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
    return false;
  }

#if !defined(QT_NO_GESTURES)
  //  QGesture *QMacPinchGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMacPinchGestureRecognizerCall0 call = reinterpret_cast<CuteQMacPinchGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QMacPinchGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result
  //      QMacPinchGestureRecognizer::recognize(QGesture *gesture, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *gesture,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMacPinchGestureRecognizerCall1 call = reinterpret_cast<CuteQMacPinchGestureRecognizerCall1>(taken[1]);
      int given = call(this, gesture, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QMacPinchGestureRecognizer::recognize(gesture, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QMacPinchGestureRecognizer::reset(QGesture *gesture)
  void reset(QGesture *gesture) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMacPinchGestureRecognizerCall2 call = reinterpret_cast<CuteQMacPinchGestureRecognizerCall2>(taken[2]);
      call(this, gesture, &handled);
      if (handled) return;
    }
    QMacPinchGestureRecognizer::reset(gesture);
  }
#endif  // !defined(QT_NO_GESTURES)
};

//  QMacPinchGestureRecognizer::QMacPinchGestureRecognizer()
extern "C" Q_DECL_EXPORT
QMacPinchGestureRecognizer *ritual_ZN26QMacPinchGestureRecognizerC1Ev() {
  return new CuteQMacPinchGestureRecognizer();
}

//  QGesture *QMacPinchGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN26QMacPinchGestureRecognizer6createEP7QObject(
    QMacPinchGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QMacPinchGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QMacPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacPinchGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(gesture, watched, event).toInt());
}

//  void QMacPinchGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMacPinchGestureRecognizer5resetEP8QGesture(
    QMacPinchGestureRecognizer *self,
    QGesture *gesture) {
  self->reset(gesture);
}

//  QMacPinchGestureRecognizer::~QMacPinchGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMacPinchGestureRecognizerD1Ev(
    QMacPinchGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQMacPinchGestureRecognizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMacPinchGestureRecognizer(
    QMacPinchGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMacPinchGestureRecognizer *>(self)->take(key, call);
}

//  QGesture *QMacPinchGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN26QMacPinchGestureRecognizer6createEP7QObject(
    QMacPinchGestureRecognizer *self,
    QObject *target) {
  return self->QMacPinchGestureRecognizer::create(target);
}

//  QGestureRecognizer::Result QMacPinchGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN26QMacPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacPinchGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QMacPinchGestureRecognizer::recognize(
          gesture,
          watched,
          event).toInt());
}

//  void QMacPinchGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QMacPinchGestureRecognizer5resetEP8QGesture(
    QMacPinchGestureRecognizer *self,
    QGesture *gesture) {
  self->QMacPinchGestureRecognizer::reset(gesture);
}

#endif  // !defined(QT_NO_GESTURES)
#endif  // defined(Q_OS_MACOS)
