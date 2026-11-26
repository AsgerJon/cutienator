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
#include <QtWidgets/private/qmacgesturerecognizer_p.h>
#include <QtWidgets/qgesture.h>
#include <QtWidgets/private/qgesture_p.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qdebug.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 17, as _ZN26QMacSwipeGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QMacSwipeGestureRecognizer::QMacSwipeGestureRecognizer()
{
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 21, as _ZN26QMacSwipeGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QMacSwipeGestureRecognizer::create(QObject * /*target*/)
{
    return new QSwipeGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 26, as _ZN26QMacSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result
QMacSwipeGestureRecognizer::recognize(QGesture *gesture, QObject *obj, QEvent *event)
{
    if (event->type() == QEvent::NativeGesture && obj->isWidgetType()) {
        QNativeGestureEvent *ev = static_cast<QNativeGestureEvent*>(event);
        switch (ev->gestureType()) {
            case Qt::SwipeNativeGesture: {
                QSwipeGesture *g = static_cast<QSwipeGesture *>(gesture);
                g->setSwipeAngle(ev->value());
                g->setHotSpot(ev->globalPosition());
                return QGestureRecognizer::FinishGesture | QGestureRecognizer::ConsumeEventHint;
                break; }
            default:
                break;
        }
    }

    return QGestureRecognizer::Ignore;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 46, as _ZN26QMacSwipeGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QMacSwipeGestureRecognizer::reset(QGesture *gesture)
{
    QSwipeGesture *g = static_cast<QSwipeGesture *>(gesture);
    g->setSwipeAngle(0);
    QGestureRecognizer::reset(gesture);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QMacSwipeGestureRecognizer that Python can take functions over in. Every QMacSwipeGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQMacSwipeGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQMacSwipeGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQMacSwipeGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQMacSwipeGestureRecognizer : public QMacSwipeGestureRecognizer {
public:
  using QMacSwipeGestureRecognizer::QMacSwipeGestureRecognizer;
  CuteQMacSwipeGestureRecognizer(const QMacSwipeGestureRecognizer & other) : QMacSwipeGestureRecognizer(other) {}
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
  //  QGesture *QMacSwipeGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMacSwipeGestureRecognizerCall0 call = reinterpret_cast<CuteQMacSwipeGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QMacSwipeGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  QGestureRecognizer::Result
  //      QMacSwipeGestureRecognizer::recognize(QGesture *gesture, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *gesture,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMacSwipeGestureRecognizerCall1 call = reinterpret_cast<CuteQMacSwipeGestureRecognizerCall1>(taken[1]);
      int given = call(this, gesture, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return QMacSwipeGestureRecognizer::recognize(gesture, watched, event);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QMacSwipeGestureRecognizer::reset(QGesture *gesture)
  void reset(QGesture *gesture) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMacSwipeGestureRecognizerCall2 call = reinterpret_cast<CuteQMacSwipeGestureRecognizerCall2>(taken[2]);
      call(this, gesture, &handled);
      if (handled) return;
    }
    QMacSwipeGestureRecognizer::reset(gesture);
  }
#endif  // !defined(QT_NO_GESTURES)
};

//  QMacSwipeGestureRecognizer::QMacSwipeGestureRecognizer()
extern "C" Q_DECL_EXPORT
QMacSwipeGestureRecognizer *ritual_ZN26QMacSwipeGestureRecognizerC1Ev() {
  return new CuteQMacSwipeGestureRecognizer();
}

//  QGesture *QMacSwipeGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN26QMacSwipeGestureRecognizer6createEP7QObject(
    QMacSwipeGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QMacSwipeGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QMacSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacSwipeGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(gesture, watched, event).toInt());
}

//  void QMacSwipeGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMacSwipeGestureRecognizer5resetEP8QGesture(
    QMacSwipeGestureRecognizer *self,
    QGesture *gesture) {
  self->reset(gesture);
}

//  QMacSwipeGestureRecognizer::~QMacSwipeGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMacSwipeGestureRecognizerD1Ev(
    QMacSwipeGestureRecognizer *self) {
  delete self;
}

//  a Python function taken by a CuteQMacSwipeGestureRecognizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMacSwipeGestureRecognizer(
    QMacSwipeGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMacSwipeGestureRecognizer *>(self)->take(key, call);
}

//  QGesture *QMacSwipeGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN26QMacSwipeGestureRecognizer6createEP7QObject(
    QMacSwipeGestureRecognizer *self,
    QObject *target) {
  return self->QMacSwipeGestureRecognizer::create(target);
}

//  QGestureRecognizer::Result QMacSwipeGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN26QMacSwipeGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacSwipeGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QMacSwipeGestureRecognizer::recognize(
          gesture,
          watched,
          event).toInt());
}

//  void QMacSwipeGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QMacSwipeGestureRecognizer5resetEP8QGesture(
    QMacSwipeGestureRecognizer *self,
    QGesture *gesture) {
  self->QMacSwipeGestureRecognizer::reset(gesture);
}

#endif  // !defined(QT_NO_GESTURES)
#endif  // defined(Q_OS_MACOS)
