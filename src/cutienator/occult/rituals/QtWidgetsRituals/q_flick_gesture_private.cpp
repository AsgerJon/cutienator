//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scroller)
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qgesture.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qwidget.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qgraphicsview.h>
#endif
#include <QtWidgets/qscroller.h>
#include <QtGui/qpointingdevice.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtWidgets/private/qflickgesture_p.h>
#include <QtCore/qbasictimer.h>
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

//  from src/widgets/util/qflickgesture.cpp, line 281, as _ZN20QFlickGesturePrivateC1Ev
#if !defined(QT_NO_GESTURES)
inline QFlickGesturePrivate::QFlickGesturePrivate()
    : receiverScroller(nullptr), button(Qt::NoButton), macIgnoreWheel(false)
{ }
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  QFlickGesture *QFlickGesturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFlickGesture *ritual_ZN20QFlickGesturePrivate6q_funcEv(
    QFlickGesturePrivate *self) {
  return self->q_func();
}

//  const QFlickGesture *QFlickGesturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFlickGesture *ritual_ZNK20QFlickGesturePrivate6q_funcEv(
    const QFlickGesturePrivate *self) {
  return self->q_func();
}

//  QFlickGesturePrivate::QFlickGesturePrivate()
extern "C" Q_DECL_EXPORT
QFlickGesturePrivate *ritual_ZN20QFlickGesturePrivateC1Ev() {
  return new QFlickGesturePrivate();
}

#endif  // !defined(QT_NO_GESTURES)
#endif  // QT_CONFIG(scroller)
