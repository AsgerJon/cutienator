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

//  from src/widgets/kernel/qstandardgestures.cpp, line 29, as _ZN21QPanGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QPanGestureRecognizer::create(QObject *target)
{
    if (target && target->isWidgetType()) {
#if (defined(Q_OS_MACOS) || defined(Q_OS_WIN)) && !defined(QT_NO_NATIVE_GESTURES) && QT_CONFIG(scrollarea)
        // for scroll areas on Windows and OS X we want to use native gestures instead
        if (!qobject_cast<QAbstractScrollArea *>(target->parent()))
            static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
#else
        static_cast<QWidget *>(target)->setAttribute(Qt::WA_AcceptTouchEvents);
#endif
    }
    return new QPanGesture;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 101, as _ZN21QPanGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QPanGestureRecognizer::reset(QGesture *state)
{
    QPanGesture *pan = static_cast<QPanGesture*>(state);
    QPanGesturePrivate *d = pan->d_func();

    d->lastOffset = d->offset = QPointF();
    d->acceleration = 0;

    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  QGesture *QPanGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN21QPanGestureRecognizer6createEP7QObject(
    QPanGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  void QPanGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPanGestureRecognizer5resetEP8QGesture(
    QPanGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QPanGestureRecognizer::~QPanGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPanGestureRecognizerD1Ev(QPanGestureRecognizer *self) {
  delete self;
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QPanGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN21QPanGestureRecognizer6createEP7QObject(
    QPanGestureRecognizer *self,
    QObject *target) {
  return self->QPanGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QPanGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPanGestureRecognizer5resetEP8QGesture(
    QPanGestureRecognizer *self,
    QGesture *state) {
  self->QPanGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
