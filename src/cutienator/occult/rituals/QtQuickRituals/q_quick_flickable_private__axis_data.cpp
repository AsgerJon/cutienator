//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktimeline_p_p.h"
#include <QDebug>
#include <QMutex>
#include <QThread>
#include <QWaitCondition>
#include <QEvent>
#include <QCoreApplication>
#include <QEasingCurve>
#include <QTime>
#include <QtCore/private/qnumeric_p.h>
#include <QHash>
#include <algorithm>
#include "qquickflickable_p.h"
#include "qquickflickable_p_p.h"
#include "qquickflickablebehavior_p.h"
#include "qquickwindow.h"
#include "qquickwindow_p.h"
#include "qquickmousearea_p.h"
#if QT_CONFIG(quick_draganddrop)
#include "qquickdrag_p.h"
#endif
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <private/qqmlglobal_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qmath.h>
#include <qpa/qplatformtheme.h>
#include <math.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 894, as _ZN20QQuickTimeLineObjectD2Ev
inline QQuickTimeLineObject::~QQuickTimeLineObject()
{
    if (_t) {
        _t->remove(this);
        _t = nullptr;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickflickable.cpp, line 203, as _ZN22QQuickFlickablePrivate8AxisDataD1Ev
inline QQuickFlickablePrivate::AxisData::~AxisData()
{
    delete transitionToBounds;
}

//  from ../qtdeclarative/src/quick/items/qquickflickable.cpp, line 299, as _ZN22QQuickFlickablePrivate8AxisData17addVelocitySampleEdd
inline void QQuickFlickablePrivate::AxisData::addVelocitySample(qreal v, qreal maxVelocity)
{
    if (v > maxVelocity)
        v = maxVelocity;
    else if (v < -maxVelocity)
        v = -maxVelocity;
    velocityBuffer.append(v);
    if (velocityBuffer.count() > QML_FLICK_SAMPLEBUFFER)
        velocityBuffer.remove(0);
}

//  from ../qtdeclarative/src/quick/items/qquickflickable.cpp, line 310, as _ZN22QQuickFlickablePrivate8AxisData14updateVelocityEv
inline void QQuickFlickablePrivate::AxisData::updateVelocity()
{
    velocity = 0;
    if (velocityBuffer.count() > QML_FLICK_DISCARDSAMPLES) {
        int count = velocityBuffer.count()-QML_FLICK_DISCARDSAMPLES;
        for (int i = 0; i < count; ++i) {
            qreal v = velocityBuffer.at(i);
            velocity += v;
        }
        velocity /= count;
    }
}
//  -----------------------------------------------------------------------

//  QQuickFlickablePrivate::AxisData::~AxisData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisDataD1Ev(
    QQuickFlickablePrivate::AxisData *self) {
  delete self;
}

//  void QQuickFlickablePrivate::AxisData::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisData5resetEv(
    QQuickFlickablePrivate::AxisData *self) {
  self->reset();
}

//  void QQuickFlickablePrivate::AxisData::markExtentsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisData16markExtentsDirtyEv(
    QQuickFlickablePrivate::AxisData *self) {
  self->markExtentsDirty();
}

//  void QQuickFlickablePrivate::AxisData::resetTransitionTo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisData17resetTransitionToEv(
    QQuickFlickablePrivate::AxisData *self) {
  self->resetTransitionTo();
}

//  void QQuickFlickablePrivate::AxisData::addVelocitySample(qreal v, qreal
//      maxVelocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisData17addVelocitySampleEdd(
    QQuickFlickablePrivate::AxisData *self,
    qreal v,
    qreal maxVelocity) {
  self->addVelocitySample(v, maxVelocity);
}

//  void QQuickFlickablePrivate::AxisData::updateVelocity()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8AxisData14updateVelocityEv(
    QQuickFlickablePrivate::AxisData *self) {
  self->updateVelocity();
}
