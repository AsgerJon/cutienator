//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktimeline_p_p.h>
#include <QtCore/QDebug>
#include <QtCore/QMutex>
#include <QtCore/QThread>
#include <QtCore/QWaitCondition>
#include <QtCore/QEvent>
#include <QtCore/QCoreApplication>
#include <QtCore/QEasingCurve>
#include <QtCore/QTime>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QHash>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 889, as _ZN20QQuickTimeLineObjectC2Ev
inline QQuickTimeLineObject::QQuickTimeLineObject()
: _t(nullptr)
{
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 894, as _ZN20QQuickTimeLineObjectD2Ev
inline QQuickTimeLineObject::~QQuickTimeLineObject()
{
    if (_t) {
        _t->remove(this);
        _t = nullptr;
    }
}
//  -----------------------------------------------------------------------

//  qreal QQuickTimeLineValue::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickTimeLineValue5valueEv(
    const QQuickTimeLineValue *self) {
  return self->value();
}

//  void QQuickTimeLineValue::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTimeLineValue8setValueEd(
    QQuickTimeLineValue *self,
    qreal v) {
  self->setValue(v);
}

//  QQuickTimeLine *QQuickTimeLineValue::timeLine() const
extern "C" Q_DECL_EXPORT
QQuickTimeLine *ritual_ZNK19QQuickTimeLineValue8timeLineEv(
    const QQuickTimeLineValue *self) {
  return self->timeLine();
}

//  qreal QQuickTimeLineValue::operator double() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickTimeLineValuecvdEv(const QQuickTimeLineValue *self) {
  return self->operator qreal();
}

//  QQuickTimeLineValue::~QQuickTimeLineValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickTimeLineValueD1Ev(QQuickTimeLineValue *self) {
  delete self;
}

//  qreal QQuickTimeLineValue::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK19QQuickTimeLineValue5valueEv(
    const QQuickTimeLineValue *self) {
  return self->QQuickTimeLineValue::value();
}

//  void QQuickTimeLineValue::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickTimeLineValue8setValueEd(
    QQuickTimeLineValue *self,
    qreal v) {
  self->QQuickTimeLineValue::setValue(v);
}
