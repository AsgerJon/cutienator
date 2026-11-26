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
#include <QtWidgets/private/qstandardgestures_p.h>
#include <QtWidgets/qgesture.h>
#include <QtWidgets/private/qgesture_p.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qwidget.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qabstractscrollarea.h>
#endif
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#endif
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qstandardgestures.cpp, line 26, as local:qstandardgestures.cpp:kSingleStepScaleMax
#if !defined(QT_NO_GESTURES)
static const qreal kSingleStepScaleMax = 2.0;
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 27, as local:qstandardgestures.cpp:kSingleStepScaleMin
#if !defined(QT_NO_GESTURES)
static const qreal kSingleStepScaleMin = 0.1;
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

//  from src/widgets/kernel/qstandardgestures.cpp, line 129, as _ZN23QPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result QPinchGestureRecognizer::recognize(QGesture *state,
                                                              QObject *,
                                                              QEvent *event)
{
    QPinchGesture *q = static_cast<QPinchGesture *>(state);
    QPinchGesturePrivate *d = q->d_func();

    QGestureRecognizer::Result result = QGestureRecognizer::Ignore;

    switch (event->type()) {
    case QEvent::TouchBegin: {
        result = QGestureRecognizer::MayBeGesture;
        break;
    }
    case QEvent::TouchEnd: {
        if (q->state() != Qt::NoGesture) {
            result = QGestureRecognizer::FinishGesture;
        } else {
            result = QGestureRecognizer::CancelGesture;
        }
        break;
    }
    case QEvent::TouchUpdate: {
        const QTouchEvent *ev = static_cast<const QTouchEvent *>(event);
        d->changeFlags = { };
        if (ev->points().size() == 2) {
            const QEventPoint &p1 = ev->points().at(0);
            const QEventPoint &p2 = ev->points().at(1);

            d->hotSpot = p1.globalPosition();
            d->isHotSpotSet = true;

            QPointF centerPoint = (p1.globalPosition() + p2.globalPosition()) / 2.0;
            if (d->isNewSequence) {
                d->startPosition[0] = p1.globalPosition();
                d->startPosition[1] = p2.globalPosition();
                d->lastCenterPoint = centerPoint;
            } else {
                d->lastCenterPoint = d->centerPoint;
            }
            d->centerPoint = centerPoint;

            d->changeFlags |= QPinchGesture::CenterPointChanged;

            if (d->isNewSequence) {
                d->scaleFactor = 1.0;
                d->lastScaleFactor = 1.0;
            } else {
                d->lastScaleFactor = d->scaleFactor;
                QLineF line(p1.globalPosition(), p2.globalPosition());
                QLineF lastLine(p1.globalLastPosition(),  p2.globalLastPosition());
                qreal newScaleFactor = line.length() / lastLine.length();
                if (newScaleFactor > kSingleStepScaleMax || newScaleFactor < kSingleStepScaleMin)
                    return QGestureRecognizer::Ignore;
                d->scaleFactor = newScaleFactor;
            }
            d->totalScaleFactor = d->totalScaleFactor * d->scaleFactor;
            d->changeFlags |= QPinchGesture::ScaleFactorChanged;

            qreal angle = QLineF(p1.globalPosition(), p2.globalPosition()).angle();
            if (angle > 180)
                angle -= 360;
            qreal startAngle = QLineF(p1.globalPressPosition(), p2.globalPressPosition()).angle();
            if (startAngle > 180)
                startAngle -= 360;
            const qreal rotationAngle = startAngle - angle;
            if (d->isNewSequence)
                d->lastRotationAngle = 0.0;
            else
                d->lastRotationAngle = d->rotationAngle;
            d->rotationAngle = rotationAngle;
            d->totalRotationAngle += d->rotationAngle - d->lastRotationAngle;
            d->changeFlags |= QPinchGesture::RotationAngleChanged;

            d->totalChangeFlags |= d->changeFlags;
            d->isNewSequence = false;
            result = QGestureRecognizer::TriggerGesture;
        } else {
            d->isNewSequence = true;
            if (q->state() == Qt::NoGesture)
                result = QGestureRecognizer::Ignore;
            else
                result = QGestureRecognizer::FinishGesture;
        }
        break;
    }
    default:
        break;
    }
    return result;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 117, as _ZN23QPinchGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QPinchGestureRecognizer::QPinchGestureRecognizer()
{
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
  CuteQPinchGestureRecognizer(const QPinchGestureRecognizer & other) : QPinchGestureRecognizer(other) {}
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

#if !defined(QT_NO_GESTURES)
//  QPinchGestureRecognizer::QPinchGestureRecognizer()
extern "C" Q_DECL_EXPORT
QPinchGestureRecognizer *ritual_ZN23QPinchGestureRecognizerC1Ev() {
  return new CuteQPinchGestureRecognizer();
}
#endif  // !defined(QT_NO_GESTURES)

//  QGesture *QPinchGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN23QPinchGestureRecognizer6createEP7QObject(
    QPinchGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QPinchGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QPinchGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(state, watched, event).toInt());
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
//  QGestureRecognizer::Result QPinchGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN23QPinchGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QPinchGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QPinchGestureRecognizer::recognize(
          state,
          watched,
          event).toInt());
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
