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

//  from src/widgets/kernel/qstandardgestures.cpp, line 447, as _ZN21QTapGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QTapGestureRecognizer::reset(QGesture *state)
{
    QTapGesture *q = static_cast<QTapGesture *>(state);
    QTapGesturePrivate *d = q->d_func();

    d->position = QPointF();

    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 394, as _ZN21QTapGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QTapGestureRecognizer::create(QObject *target)
{
    if (target && target->isWidgetType()) {
        static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
    }
    return new QTapGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 402, as _ZN21QTapGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result QTapGestureRecognizer::recognize(QGesture *state,
                                                            QObject *,
                                                            QEvent *event)
{
    QTapGesture *q = static_cast<QTapGesture *>(state);
    QTapGesturePrivate *d = q->d_func();

    QGestureRecognizer::Result result = QGestureRecognizer::CancelGesture;

    switch (event->type()) {
    case QEvent::TouchBegin: {
        const auto ev = static_cast<const QTouchEvent *>(event);
        d->position = ev->points().at(0).position();
        q->setHotSpot(ev->points().at(0).globalPosition());
        result = QGestureRecognizer::TriggerGesture;
        break;
    }
    case QEvent::TouchUpdate:
    case QEvent::TouchEnd: {
        const auto ev = static_cast<const QTouchEvent *>(event);
        if (q->state() != Qt::NoGesture && ev->points().size() == 1) {
            const QEventPoint &p = ev->points().at(0);
            const QPointF delta = p.position() - p.pressPosition();
            constexpr auto TapRadius = 40.;
            if (delta.manhattanLength() <= TapRadius) {
                if (event->type() == QEvent::TouchEnd)
                    result = QGestureRecognizer::FinishGesture;
                else
                    result = QGestureRecognizer::TriggerGesture;
            }
        }
        break;
    }
    case QEvent::MouseButtonPress:
    case QEvent::MouseMove:
    case QEvent::MouseButtonRelease:
        result = QGestureRecognizer::Ignore;
        break;
    default:
        result = QGestureRecognizer::Ignore;
        break;
    }
    return result;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 390, as _ZN21QTapGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QTapGestureRecognizer::QTapGestureRecognizer()
{
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QTapGestureRecognizer that Python can take functions over in. Every QTapGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQTapGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQTapGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQTapGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQTapGestureRecognizer : public QTapGestureRecognizer {
public:
  using QTapGestureRecognizer::QTapGestureRecognizer;
  CuteQTapGestureRecognizer(const QTapGestureRecognizer & other) : QTapGestureRecognizer(other) {}
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
  //  QGesture *QTapGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTapGestureRecognizerCall0 call = reinterpret_cast<CuteQTapGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QTapGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result QTapGestureRecognizer::recognize(QGesture
  //      *state, QObject *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *state,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTapGestureRecognizerCall1 call = reinterpret_cast<CuteQTapGestureRecognizerCall1>(taken[1]);
      int given = call(this, state, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QTapGestureRecognizer::recognize(state, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QTapGestureRecognizer::reset(QGesture *state)
  void reset(QGesture *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTapGestureRecognizerCall2 call = reinterpret_cast<CuteQTapGestureRecognizerCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
    QTapGestureRecognizer::reset(state);
  }
#endif  // !defined(QT_NO_GESTURES)
};

#if !defined(QT_NO_GESTURES)
//  QTapGestureRecognizer::QTapGestureRecognizer()
extern "C" Q_DECL_EXPORT
QTapGestureRecognizer *ritual_ZN21QTapGestureRecognizerC1Ev() {
  return new CuteQTapGestureRecognizer();
}
#endif  // !defined(QT_NO_GESTURES)

//  QGesture *QTapGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN21QTapGestureRecognizer6createEP7QObject(
    QTapGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QTapGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QTapGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QTapGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(state, watched, event).toInt());
}

//  void QTapGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTapGestureRecognizer5resetEP8QGesture(
    QTapGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QTapGestureRecognizer::~QTapGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTapGestureRecognizerD1Ev(QTapGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQTapGestureRecognizer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapGestureRecognizer(
    QTapGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTapGestureRecognizer *>(self)->take(key, call);
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QTapGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN21QTapGestureRecognizer6createEP7QObject(
    QTapGestureRecognizer *self,
    QObject *target) {
  return self->QTapGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  QGestureRecognizer::Result QTapGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN21QTapGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QTapGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QTapGestureRecognizer::recognize(
          state,
          watched,
          event).toInt());
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QTapGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QTapGestureRecognizer5resetEP8QGesture(
    QTapGestureRecognizer *self,
    QGesture *state) {
  self->QTapGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
