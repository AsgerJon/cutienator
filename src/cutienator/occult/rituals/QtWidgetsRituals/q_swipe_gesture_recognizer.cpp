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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qstandardgestures.cpp, line 370, as _ZN23QSwipeGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QSwipeGestureRecognizer::reset(QGesture *state)
{
    QSwipeGesture *q = static_cast<QSwipeGesture *>(state);
    QSwipeGesturePrivate *d = q->d_func();

    d->verticalDirection = d->horizontalDirection = QSwipeGesture::NoDirection;
    d->swipeAngle = 0;

    d->lastPositions[0] = d->lastPositions[1] = d->lastPositions[2] = QPointF();
    d->state = QSwipeGesturePrivate::NoGesture;
    d->velocityValue = 0;
    d->time.invalidate();

    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 246, as _ZN23QSwipeGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QSwipeGestureRecognizer::create(QObject *target)
{
    if (target && target->isWidgetType()) {
        static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
    }
    return new QSwipeGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 254, as _ZN23QSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result QSwipeGestureRecognizer::recognize(QGesture *state,
                                                              QObject *,
                                                              QEvent *event)
{
    QSwipeGesture *q = static_cast<QSwipeGesture *>(state);
    QSwipeGesturePrivate *d = q->d_func();

    QGestureRecognizer::Result result = QGestureRecognizer::Ignore;

    switch (event->type()) {
    case QEvent::TouchBegin: {
        d->velocityValue = 1;
        d->time.start();
        d->state = QSwipeGesturePrivate::Started;
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
        if (d->state == QSwipeGesturePrivate::NoGesture)
            result = QGestureRecognizer::CancelGesture;
        else if (ev->points().size() == 3) {
            d->state = QSwipeGesturePrivate::ThreePointsReached;
            const QEventPoint &p1 = ev->points().at(0);
            const QEventPoint &p2 = ev->points().at(1);
            const QEventPoint &p3 = ev->points().at(2);

            if (d->lastPositions[0].isNull()) {
                d->lastPositions[0] = p1.globalPressPosition();
                d->lastPositions[1] = p2.globalPressPosition();
                d->lastPositions[2] = p3.globalPressPosition();
            }
            d->hotSpot = p1.globalPosition();
            d->isHotSpotSet = true;

            int xDistance = (p1.globalPosition().x() - d->lastPositions[0].x() +
                             p2.globalPosition().x() - d->lastPositions[1].x() +
                             p3.globalPosition().x() - d->lastPositions[2].x()) / 3;
            int yDistance = (p1.globalPosition().y() - d->lastPositions[0].y() +
                             p2.globalPosition().y() - d->lastPositions[1].y() +
                             p3.globalPosition().y() - d->lastPositions[2].y()) / 3;

            const int distance = xDistance >= yDistance ? xDistance : yDistance;
            int elapsedTime = d->time.restart();
            if (!elapsedTime)
                elapsedTime = 1;
            d->velocityValue = 0.9 * d->velocityValue + (qreal) distance / elapsedTime;
            d->swipeAngle = QLineF(p1.globalPressPosition(), p1.globalPosition()).angle();

            static const int MoveThreshold = 50;
            static const int directionChangeThreshold = MoveThreshold / 8;
            if (qAbs(xDistance) > MoveThreshold || qAbs(yDistance) > MoveThreshold) {
                // measure the distance to check if the direction changed
                d->lastPositions[0] = p1.globalPosition();
                d->lastPositions[1] = p2.globalPosition();
                d->lastPositions[2] = p3.globalPosition();
                result = QGestureRecognizer::TriggerGesture;
                // QTBUG-46195, small changes in direction should not cause the gesture to be canceled.
                if (d->verticalDirection == QSwipeGesture::NoDirection || qAbs(yDistance) > directionChangeThreshold) {
                    const QSwipeGesture::SwipeDirection vertical = yDistance > 0
                        ? QSwipeGesture::Down : QSwipeGesture::Up;
                    if (d->verticalDirection != QSwipeGesture::NoDirection && d->verticalDirection != vertical)
                        result = QGestureRecognizer::CancelGesture;
                    d->verticalDirection = vertical;
                }
                if (d->horizontalDirection == QSwipeGesture::NoDirection || qAbs(xDistance) > directionChangeThreshold) {
                    const QSwipeGesture::SwipeDirection horizontal = xDistance > 0
                        ? QSwipeGesture::Right : QSwipeGesture::Left;
                    if (d->horizontalDirection != QSwipeGesture::NoDirection && d->horizontalDirection != horizontal)
                        result = QGestureRecognizer::CancelGesture;
                    d->horizontalDirection = horizontal;
                }
            } else {
                if (q->state() != Qt::NoGesture)
                    result = QGestureRecognizer::TriggerGesture;
                else
                    result = QGestureRecognizer::MayBeGesture;
            }
        } else if (ev->points().size() > 3) {
            result = QGestureRecognizer::CancelGesture;
        } else { // less than 3 touch points
            switch (d->state) {
            case QSwipeGesturePrivate::NoGesture:
                result = QGestureRecognizer::MayBeGesture;
                break;
            case QSwipeGesturePrivate::Started:
                result = QGestureRecognizer::Ignore;
                break;
            case QSwipeGesturePrivate::ThreePointsReached:
                if (ev->touchPointStates() & QEventPoint::State::Pressed) {
                    result = QGestureRecognizer::CancelGesture;
                } else if (d->verticalDirection != QSwipeGesture::NoDirection ||
                           d->horizontalDirection != QSwipeGesture::NoDirection) {
                    result = QGestureRecognizer::TriggerGesture;
                } else {
                    result = QGestureRecognizer::Ignore;
                }
                break;
            }
        }
        break;
    }
    default:
        break;
    }
    return result;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 242, as _ZN23QSwipeGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QSwipeGestureRecognizer::QSwipeGestureRecognizer()
{
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QSwipeGestureRecognizer that Python can take functions over in. Every QSwipeGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQSwipeGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQSwipeGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQSwipeGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQSwipeGestureRecognizer : public QSwipeGestureRecognizer {
public:
  using QSwipeGestureRecognizer::QSwipeGestureRecognizer;
  CuteQSwipeGestureRecognizer(const QSwipeGestureRecognizer & other) : QSwipeGestureRecognizer(other) {}
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
  //  QGesture *QSwipeGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSwipeGestureRecognizerCall0 call = reinterpret_cast<CuteQSwipeGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QSwipeGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result
  //      QSwipeGestureRecognizer::recognize(QGesture *state, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *state,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSwipeGestureRecognizerCall1 call = reinterpret_cast<CuteQSwipeGestureRecognizerCall1>(taken[1]);
      int given = call(this, state, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QSwipeGestureRecognizer::recognize(state, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QSwipeGestureRecognizer::reset(QGesture *state)
  void reset(QGesture *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSwipeGestureRecognizerCall2 call = reinterpret_cast<CuteQSwipeGestureRecognizerCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
    QSwipeGestureRecognizer::reset(state);
  }
#endif  // !defined(QT_NO_GESTURES)
};

#if !defined(QT_NO_GESTURES)
//  QSwipeGestureRecognizer::QSwipeGestureRecognizer()
extern "C" Q_DECL_EXPORT
QSwipeGestureRecognizer *ritual_ZN23QSwipeGestureRecognizerC1Ev() {
  return new CuteQSwipeGestureRecognizer();
}
#endif  // !defined(QT_NO_GESTURES)

//  QGesture *QSwipeGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN23QSwipeGestureRecognizer6createEP7QObject(
    QSwipeGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QSwipeGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QSwipeGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(state, watched, event).toInt());
}

//  void QSwipeGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSwipeGestureRecognizer5resetEP8QGesture(
    QSwipeGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QSwipeGestureRecognizer::~QSwipeGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSwipeGestureRecognizerD1Ev(QSwipeGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQSwipeGestureRecognizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSwipeGestureRecognizer(
    QSwipeGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSwipeGestureRecognizer *>(self)->take(key, call);
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QSwipeGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN23QSwipeGestureRecognizer6createEP7QObject(
    QSwipeGestureRecognizer *self,
    QObject *target) {
  return self->QSwipeGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  QGestureRecognizer::Result QSwipeGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN23QSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QSwipeGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QSwipeGestureRecognizer::recognize(
          state,
          watched,
          event).toInt());
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QSwipeGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSwipeGestureRecognizer5resetEP8QGesture(
    QSwipeGestureRecognizer *self,
    QGesture *state) {
  self->QSwipeGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
