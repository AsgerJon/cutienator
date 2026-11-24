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
#include <QtCore/qstring.h>
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

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 133, as _ZN24QMacPanGestureRecognizerC1Ev
#if !defined(QT_NO_GESTURES)
inline QMacPanGestureRecognizer::QMacPanGestureRecognizer() : _panCanceled(true)
{
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 137, as _ZN24QMacPanGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QMacPanGestureRecognizer::create(QObject *target)
{
    if (!target)
        return new QPanGesture;

    if (QWidget *w = qobject_cast<QWidget *>(target)) {
        w->setAttribute(Qt::WA_AcceptTouchEvents);
        w->setAttribute(Qt::WA_TouchPadAcceptSingleTouchEvents);
        return new QPanGesture;
    }
    return nullptr;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 160, as _ZN24QMacPanGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent
#if !defined(QT_NO_GESTURES)
inline QGestureRecognizer::Result
QMacPanGestureRecognizer::recognize(QGesture *gesture, QObject *target, QEvent *event)
{
    const int panBeginDelay = 300;
    const int panBeginRadius = 3;

    QPanGesture *g = static_cast<QPanGesture *>(gesture);

    switch (event->type()) {
    case QEvent::TouchBegin: {
        const QTouchEvent *ev = static_cast<const QTouchEvent*>(event);
        if (ev->points().size() == 1) {
            reset(gesture);
            _startPos = QCursor::pos();
            _target = target;
            _panTimer.start(panBeginDelay, this);
            _panCanceled = false;
            return QGestureRecognizer::MayBeGesture;
        }
        break;}
    case QEvent::TouchEnd: {
        if (_panCanceled)
            break;

        const QTouchEvent *ev = static_cast<const QTouchEvent*>(event);
        if (ev->points().size() == 1)
            return QGestureRecognizer::FinishGesture;
        break;}
    case QEvent::TouchUpdate: {
        if (_panCanceled)
            break;

        const QTouchEvent *ev = static_cast<const QTouchEvent*>(event);
        if (ev->points().size() == 1) {
            if (_panTimer.isActive()) {
                // INVARIANT: Still in maybeGesture. Check if the user
                // moved his finger so much that it makes sense to cancel the pan:
                const QPointF p = QCursor::pos();
                if ((p - _startPos).manhattanLength() > panBeginRadius) {
                    _panCanceled = true;
                    _panTimer.stop();
                    return QGestureRecognizer::CancelGesture;
                }
            } else {
                const QPointF p = QCursor::pos();
                const QPointF posOffset = p - _startPos;
                g->setLastOffset(g->offset());
                g->setOffset(QPointF(posOffset.x(), posOffset.y()));
                g->setHotSpot(_startPos);
                return QGestureRecognizer::TriggerGesture;
            }
        } else if (_panTimer.isActive()) {
            // I only want to cancel the pan if the user is pressing
            // more than one finger, and the pan hasn't started yet:
            _panCanceled = true;
            _panTimer.stop();
            return QGestureRecognizer::CancelGesture;
        }
        break;}
    case QEvent::Timer: {
        QTimerEvent *ev = static_cast<QTimerEvent *>(event);
        if (ev->timerId() == _panTimer.timerId()) {
            if (_panCanceled)
                break;
            // Begin new pan session!
            _startPos = QCursor::pos();
            g->setHotSpot(_startPos);
            return QGestureRecognizer::TriggerGesture | QGestureRecognizer::ConsumeEventHint;
        }
        break; }
    default:
        break;
    }

    return QGestureRecognizer::Ignore;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 237, as _ZN24QMacPanGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QMacPanGestureRecognizer::reset(QGesture *gesture)
{
    QPanGesture *g = static_cast<QPanGesture *>(gesture);
    _startPos = QPointF();
    _panCanceled = true;
    _panTimer.stop();
    g->setOffset(QPointF(0, 0));
    g->setLastOffset(QPointF(0, 0));
    g->setAcceleration(qreal(1));
    QGestureRecognizer::reset(gesture);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qmacgesturerecognizer.cpp, line 150, as _ZN24QMacPanGestureRecognizer10timerEventEP11QTimerEvent
#if !defined(QT_NO_GESTURES)
inline void QMacPanGestureRecognizer::timerEvent(QTimerEvent *ev)
{
    if (ev->timerId() == _panTimer.timerId()) {
        if (_panTimer.isActive())
           _panTimer.stop();
        if (_target)
            QCoreApplication::sendEvent(_target, ev);
    }
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  Only a class built on QMacPanGestureRecognizer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMacPanGestureRecognizer : QMacPanGestureRecognizer {
  using QMacPanGestureRecognizer::timerEvent;
};

//  const QMetaObject *QMacPanGestureRecognizer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QMacPanGestureRecognizer10metaObjectEv(
    const QMacPanGestureRecognizer *self) {
  return self->metaObject();
}

//  QString QMacPanGestureRecognizer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QMacPanGestureRecognizer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMacPanGestureRecognizer::tr(s, c, n));
}

//  QMacPanGestureRecognizer::QMacPanGestureRecognizer()
extern "C" Q_DECL_EXPORT
QMacPanGestureRecognizer *ritual_ZN24QMacPanGestureRecognizerC1Ev() {
  return new QMacPanGestureRecognizer();
}

//  QGesture *QMacPanGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN24QMacPanGestureRecognizer6createEP7QObject(
    QMacPanGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  QGestureRecognizer::Result QMacPanGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QMacPanGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacPanGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(gesture, watched, event).toInt());
}

//  void QMacPanGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMacPanGestureRecognizer5resetEP8QGesture(
    QMacPanGestureRecognizer *self,
    QGesture *gesture) {
  self->reset(gesture);
}

//  void QMacPanGestureRecognizer::timerEvent(QTimerEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMacPanGestureRecognizer10timerEventEP11QTimerEvent(
    QMacPanGestureRecognizer *self,
    QTimerEvent *ev) {
  self->timerEvent(ev);
}

//  QMacPanGestureRecognizer as the QGestureRecognizer it is built on
extern "C" Q_DECL_EXPORT
QGestureRecognizer *ritual_cast_QMacPanGestureRecognizer_QGestureRecognizer(
    QMacPanGestureRecognizer *self) {
  return static_cast<QGestureRecognizer *>(self);
}

//  QGesture *QMacPanGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN24QMacPanGestureRecognizer6createEP7QObject(
    QMacPanGestureRecognizer *self,
    QObject *target) {
  return self->QMacPanGestureRecognizer::create(target);
}

//  QGestureRecognizer::Result QMacPanGestureRecognizer::recognize(QGesture
//      *gesture, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN24QMacPanGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QMacPanGestureRecognizer *self,
    QGesture *gesture,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(
      self->QMacPanGestureRecognizer::recognize(
          gesture,
          watched,
          event).toInt());
}

//  void QMacPanGestureRecognizer::reset(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QMacPanGestureRecognizer5resetEP8QGesture(
    QMacPanGestureRecognizer *self,
    QGesture *gesture) {
  self->QMacPanGestureRecognizer::reset(gesture);
}

//  void QMacPanGestureRecognizer::timerEvent(QTimerEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QMacPanGestureRecognizer10timerEventEP11QTimerEvent(
    QMacPanGestureRecognizer *self,
    QTimerEvent *ev) {
  static_cast<OwnQMacPanGestureRecognizer *>(self)->OwnQMacPanGestureRecognizer::timerEvent(
      ev);
}

#endif  // !defined(QT_NO_GESTURES)
#endif  // defined(Q_OS_MACOS)
