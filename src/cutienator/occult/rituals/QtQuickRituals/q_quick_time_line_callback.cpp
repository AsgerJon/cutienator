//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 902, as _ZN22QQuickTimeLineCallbackC1Ev
inline QQuickTimeLineCallback::QQuickTimeLineCallback()
: d0(nullptr), d1(nullptr), d2(nullptr)
{
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 912, as _ZN22QQuickTimeLineCallbackC1ERKS_
inline QQuickTimeLineCallback::QQuickTimeLineCallback(const QQuickTimeLineCallback &o)
: d0(o.d0), d1(o.d1), d2(o.d2)
{
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 925, as _ZNK22QQuickTimeLineCallback14callbackObjectEv
inline QQuickTimeLineObject *QQuickTimeLineCallback::callbackObject() const
{
    return d2;
}
//  -----------------------------------------------------------------------

//  QQuickTimeLineCallback::QQuickTimeLineCallback()
extern "C" Q_DECL_EXPORT
QQuickTimeLineCallback *ritual_ZN22QQuickTimeLineCallbackC1Ev() {
  return new QQuickTimeLineCallback();
}

//  QQuickTimeLineCallback::QQuickTimeLineCallback(const
//      QQuickTimeLineCallback &o)
extern "C" Q_DECL_EXPORT
QQuickTimeLineCallback *ritual_ZN22QQuickTimeLineCallbackC1ERKS_(
    const QQuickTimeLineCallback *o) {
  return new QQuickTimeLineCallback(*o);
}

//  QQuickTimeLineObject *QQuickTimeLineCallback::callbackObject() const
extern "C" Q_DECL_EXPORT
QQuickTimeLineObject *ritual_ZNK22QQuickTimeLineCallback14callbackObjectEv(
    const QQuickTimeLineCallback *self) {
  return self->callbackObject();
}

//  QQuickTimeLineCallback::~QQuickTimeLineCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTimeLineCallbackD1Ev(QQuickTimeLineCallback *self) {
  delete self;
}
