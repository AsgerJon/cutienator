//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qvariantanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qvariantanimation.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qvariantanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qeasingcurve.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qvariantanimation.h"
#include "qvariantanimation_p.h"
#include <QtCore/qrect.h>
#include <QtCore/qline.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qlocking_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qvariantanimation.cpp, line 243, as _ZN24QVariantAnimationPrivate26setCurrentValueForProgressEd
inline void QVariantAnimationPrivate::setCurrentValueForProgress(const qreal progress)
{
    Q_Q(QVariantAnimation);

    const qreal startProgress = currentInterval.start.first;
    const qreal endProgress = currentInterval.end.first;
    const qreal localProgress =
            qIsNull(progress - startProgress) ? 0.0 // avoid 0/0 below
            /* else */                        : (progress - startProgress) / (endProgress - startProgress);

    QVariant ret = q->interpolated(currentInterval.start.second,
                                   currentInterval.end.second,
                                   localProgress);
    qSwap(currentValue, ret);
    q->updateCurrentValue(currentValue);
    Q_CONSTINIT static QBasicAtomicInt changedSignalIndex = Q_BASIC_ATOMIC_INITIALIZER(0);
    if (!changedSignalIndex.loadRelaxed()) {
        //we keep the mask so that we emit valueChanged only when needed (for performance reasons)
        changedSignalIndex.testAndSetRelaxed(0, signalIndex("valueChanged(QVariant)"));
    }
    if (isSignalConnected(changedSignalIndex.loadRelaxed()) && currentValue != ret) {
        //the value has changed
        emit q->valueChanged(currentValue);
    }
}
//  -----------------------------------------------------------------------

//  QVariantAnimation *QVariantAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QVariantAnimation *ritual_ZN24QVariantAnimationPrivate6q_funcEv(
    QVariantAnimationPrivate *self) {
  return self->q_func();
}

//  const QVariantAnimation *QVariantAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QVariantAnimation *ritual_ZNK24QVariantAnimationPrivate6q_funcEv(
    const QVariantAnimationPrivate *self) {
  return self->q_func();
}

//  QVariantAnimationPrivate *QVariantAnimationPrivate::get(QVariantAnimation
//      *q)
extern "C" Q_DECL_EXPORT
QVariantAnimationPrivate *ritual_ZN24QVariantAnimationPrivate3getEP17QVariantAnimation(
    QVariantAnimation *q) {
  return QVariantAnimationPrivate::get(q);
}

//  void QVariantAnimationPrivate::setEasingCurve(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate14setEasingCurveERK12QEasingCurve(
    QVariantAnimationPrivate *self,
    const QEasingCurve *easing) {
  self->setEasingCurve(*easing);
}

//  void QVariantAnimationPrivate::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate11setDurationEi(
    QVariantAnimationPrivate *self,
    int msecs) {
  self->setDuration(msecs);
}

//  void QVariantAnimationPrivate::setCurrentValueForProgress(const qreal
//      progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate26setCurrentValueForProgressEd(
    QVariantAnimationPrivate *self,
    qreal progress) {
  self->setCurrentValueForProgress(progress);
}

#endif  // QT_CONFIG(animation)
