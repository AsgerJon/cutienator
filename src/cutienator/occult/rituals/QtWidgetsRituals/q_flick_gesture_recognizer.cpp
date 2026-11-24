//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgesture.h"
#include "qapplication.h"
#include "qevent.h"
#include "qwidget.h"
#if QT_CONFIG(graphicsview)
#include "qgraphicsitem.h"
#include "qgraphicsscene.h"
#include "qgraphicssceneevent.h"
#include "qgraphicsview.h"
#endif
#include "qscroller.h"
#include <QtGui/qpointingdevice.h>
#include "private/qapplication_p.h"
#include "private/qevent_p.h"
#include "private/qflickgesture_p.h"
#include "qbasictimer.h"
#include "qdebug.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/util/qflickgesture.cpp, line 304, as _ZN23QFlickGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
inline QGesture *QFlickGestureRecognizer::create(QObject *target)
{
#if QT_CONFIG(graphicsview)
    QGraphicsObject *go = qobject_cast<QGraphicsObject*>(target);
    if (go && button == Qt::NoButton) {
        go->setAcceptTouchEvents(true);
    }
#endif
    return new QFlickGesture(target, button);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/util/qflickgesture.cpp, line 632, as _ZN23QFlickGestureRecognizer5resetEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QFlickGestureRecognizer::reset(QGesture *state)
{
    QGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  QGesture *QFlickGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN23QFlickGestureRecognizer6createEP7QObject(
    QFlickGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  void QFlickGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFlickGestureRecognizer5resetEP8QGesture(
    QFlickGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  QFlickGestureRecognizer::~QFlickGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFlickGestureRecognizerD1Ev(QFlickGestureRecognizer *self) {
  delete self;
}

#if !defined(QT_NO_GESTURES)
//  QGesture *QFlickGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN23QFlickGestureRecognizer6createEP7QObject(
    QFlickGestureRecognizer *self,
    QObject *target) {
  return self->QFlickGestureRecognizer::create(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QFlickGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QFlickGestureRecognizer5resetEP8QGesture(
    QFlickGestureRecognizer *self,
    QGesture *state) {
  self->QFlickGestureRecognizer::reset(state);
}
#endif  // !defined(QT_NO_GESTURES)

#endif  // !defined(QT_NO_GESTURES)
