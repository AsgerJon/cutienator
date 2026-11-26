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

//  from src/widgets/kernel/qstandardgestures.cpp, line 43, as local:qstandardgestures.cpp:panOffset
#if !defined(QT_NO_GESTURES)
static QPointF panOffset(const QList<QEventPoint> &touchPoints, int maxCount)
{
    QPointF result;
    const int count = qMin(touchPoints.size(), maxCount);
    for (int p = 0; p < count; ++p)
        result += touchPoints.at(p).position() - touchPoints.at(p).pressPosition();
    return result / qreal(count);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qstandardgestures.cpp, line 29, as _ZN21QPanGestureRecognizer6createEP7QObject
#if !defined(QT_NO_GESTURES)
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)
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

//  QGestureRecognizer::Result QPanGestureRecognizer::recognize(QGesture
//      *state, QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QPanGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QPanGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(state, watched, event).toInt());
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
#if defined(Q_OS_LINUX)
//  QGesture *QPanGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN21QPanGestureRecognizer6createEP7QObject(
    QPanGestureRecognizer *self,
    QObject *target) {
  return self->QPanGestureRecognizer::create(target);
}
#endif  // defined(Q_OS_LINUX)
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
