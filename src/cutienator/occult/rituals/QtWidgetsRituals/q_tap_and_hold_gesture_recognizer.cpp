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

//  from src/widgets/kernel/qstandardgestures.cpp, line 465, as _ZN28QTapAndHoldGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QTapAndHoldGestureRecognizer::create(QObject *target)
{
    if (target && target->isWidgetType()) {
        static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
    }
    return new QTapAndHoldGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 548, as _ZN28QTapAndHoldGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QTapAndHoldGestureRecognizer::reset(QGesture *state)
{
    QTapAndHoldGesture *q = static_cast<QTapAndHoldGesture *>(state);
    QTapAndHoldGesturePrivate *d = q->d_func();

    d->position = QPointF();
    d->tapAndHoldTimer.stop();

    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QTapAndHoldGestureRecognizer that Python can take functions over in. Every QTapAndHoldGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQTapAndHoldGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQTapAndHoldGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQTapAndHoldGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQTapAndHoldGestureRecognizer : public QTapAndHoldGestureRecognizer {
public:
  using QTapAndHoldGestureRecognizer::QTapAndHoldGestureRecognizer;
  CuteQTapAndHoldGestureRecognizer(const QTapAndHoldGestureRecognizer &other) : QTapAndHoldGestureRecognizer(other) {}
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
  //  QGesture *QTapAndHoldGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTapAndHoldGestureRecognizerCall0 call = reinterpret_cast<CuteQTapAndHoldGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QTapAndHoldGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result
  //      QTapAndHoldGestureRecognizer::recognize(QGesture *state, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *state,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTapAndHoldGestureRecognizerCall1 call = reinterpret_cast<CuteQTapAndHoldGestureRecognizerCall1>(taken[1]);
      int given = call(this, state, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QTapAndHoldGestureRecognizer::recognize(state, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QTapAndHoldGestureRecognizer::reset(QGesture *state)
  void reset(QGesture *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTapAndHoldGestureRecognizerCall2 call = reinterpret_cast<CuteQTapAndHoldGestureRecognizerCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
    QTapAndHoldGestureRecognizer::reset(state);
  }
#endif  // !defined(QT_NO_GESTURES)
};

//  QGesture *QTapAndHoldGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN28QTapAndHoldGestureRecognizer6createEP7QObject(
    QTapAndHoldGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  void QTapAndHoldGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QTapAndHoldGestureRecognizer5resetEP8QGesture(
    QTapAndHoldGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QTapAndHoldGestureRecognizer::~QTapAndHoldGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QTapAndHoldGestureRecognizerD1Ev(
    QTapAndHoldGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQTapAndHoldGestureRecognizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapAndHoldGestureRecognizer(
    QTapAndHoldGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTapAndHoldGestureRecognizer *>(self)->take(key, call);
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QTapAndHoldGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN28QTapAndHoldGestureRecognizer6createEP7QObject(
    QTapAndHoldGestureRecognizer *self,
    QObject *target) {
  return self->QTapAndHoldGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QTapAndHoldGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QTapAndHoldGestureRecognizer5resetEP8QGesture(
    QTapAndHoldGestureRecognizer *self,
    QGesture *state) {
  self->QTapAndHoldGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
