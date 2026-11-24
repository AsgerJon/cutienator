//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstandardgestures_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstandardgestures_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qstandardgestures_p.h"
#include "qgesture.h"
#include "qgesture_p.h"
#include "qevent.h"
#include "qwidget.h"
#if QT_CONFIG(scrollarea)
#include "qabstractscrollarea.h"
#endif
#if QT_CONFIG(graphicsview)
#include <qgraphicssceneevent.h>
#endif
#include "qdebug.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qstandardgestures.cpp, line 121, as _ZN23QPinchGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QPinchGestureRecognizer::create(QObject *target)
{
    if (target && target->isWidgetType()) {
        static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
    }
    return new QPinchGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 221, as _ZN23QPinchGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QPinchGestureRecognizer::reset(QGesture *state)
{
    QPinchGesture *pinch = static_cast<QPinchGesture *>(state);
    QPinchGesturePrivate *d = pinch->d_func();

    d->totalChangeFlags = d->changeFlags = { };

    d->startCenterPoint = d->lastCenterPoint = d->centerPoint = QPointF();
    d->totalScaleFactor = d->lastScaleFactor = d->scaleFactor = 1;
    d->totalRotationAngle = d->lastRotationAngle = d->rotationAngle = 0;

    d->isNewSequence = true;
    d->startPosition[0] = d->startPosition[1] = QPointF();

    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QPinchGestureRecognizer that Python can take functions over in. Every QPinchGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQPinchGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQPinchGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQPinchGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQPinchGestureRecognizer : public QPinchGestureRecognizer {
public:
  using QPinchGestureRecognizer::QPinchGestureRecognizer;
  CuteQPinchGestureRecognizer(const QPinchGestureRecognizer &other) : QPinchGestureRecognizer(other) {}
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
  //  QGesture *QPinchGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPinchGestureRecognizerCall0 call = reinterpret_cast<CuteQPinchGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QPinchGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result
  //      QPinchGestureRecognizer::recognize(QGesture *state, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *state,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPinchGestureRecognizerCall1 call = reinterpret_cast<CuteQPinchGestureRecognizerCall1>(taken[1]);
      int given = call(this, state, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QPinchGestureRecognizer::recognize(state, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QPinchGestureRecognizer::reset(QGesture *state)
  void reset(QGesture *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPinchGestureRecognizerCall2 call = reinterpret_cast<CuteQPinchGestureRecognizerCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
    QPinchGestureRecognizer::reset(state);
  }
#endif  // !defined(QT_NO_GESTURES)
};

//  QGesture *QPinchGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN23QPinchGestureRecognizer6createEP7QObject(
    QPinchGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  void QPinchGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPinchGestureRecognizer5resetEP8QGesture(
    QPinchGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QPinchGestureRecognizer::~QPinchGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPinchGestureRecognizerD1Ev(QPinchGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQPinchGestureRecognizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPinchGestureRecognizer(
    QPinchGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPinchGestureRecognizer *>(self)->take(key, call);
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QPinchGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN23QPinchGestureRecognizer6createEP7QObject(
    QPinchGestureRecognizer *self,
    QObject *target) {
  return self->QPinchGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QPinchGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPinchGestureRecognizer5resetEP8QGesture(
    QPinchGestureRecognizer *self,
    QGesture *state) {
  self->QPinchGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
