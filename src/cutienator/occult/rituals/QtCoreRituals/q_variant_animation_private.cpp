//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qvariantanimation_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: completed by hand: getInterpolator (exported),
//  and Qt's code taken from its source for updateInterpolator,
//  recalculateCurrentInterval, valueAt, setValueAt and
//  setDefaultStartEndValue. Kept as it is when the generator runs again.
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
//  from src/corelib/animation/qvariantanimation.cpp, lines 112 and 117, as the helpers of the functions below
static bool animationValueLessThan(const QVariantAnimation::KeyValue &p1, const QVariantAnimation::KeyValue &p2)
{
    return p1.first < p2.first;
}

static QVariant defaultInterpolator(const void *, const void *, qreal)
{
    return QVariant();
}

//  from src/corelib/animation/qvariantanimation.cpp, line 175, as _ZN24QVariantAnimationPrivate18updateInterpolatorEv
inline void QVariantAnimationPrivate::updateInterpolator()
{
    int type = currentInterval.start.second.userType();
    if (type == currentInterval.end.second.userType())
        interpolator = getInterpolator(type);
    else
        interpolator = nullptr;

    //we make sure that the interpolator is always set to something
    if (!interpolator)
        interpolator = &defaultInterpolator;
}

//  from src/corelib/animation/qvariantanimation.cpp, line 194, as _ZN24QVariantAnimationPrivate26recalculateCurrentIntervalEb
inline void QVariantAnimationPrivate::recalculateCurrentInterval(bool force)
{
    // can't interpolate if we don't have at least 2 values
    if ((keyValues.size() + (defaultStartEndValue.isValid() ? 1 : 0)) < 2)
        return;

    const qreal endProgress = (direction == QAbstractAnimation::Forward) ? qreal(1) : qreal(0);
    const qreal progress = easing.value().valueForProgress(
            duration == 0 ? endProgress : qreal(currentTime) / qreal(duration));

    //0 and 1 are still the boundaries
    if (force || (currentInterval.start.first > 0 && progress < currentInterval.start.first)
        || (currentInterval.end.first < 1 && progress > currentInterval.end.first)) {
        //let's update currentInterval
        QVariantAnimation::KeyValues::const_iterator it = std::lower_bound(keyValues.constBegin(),
                                                                           keyValues.constEnd(),
                                                                           std::pair{progress, QVariant{}},
                                                                           animationValueLessThan);
        if (it == keyValues.constBegin()) {
            //the item pointed to by it is the start element in the range
            if (it->first == 0 && keyValues.size() > 1) {
                currentInterval.start = *it;
                currentInterval.end = *(it+1);
            } else {
                currentInterval.start = {qreal(0), defaultStartEndValue};
                currentInterval.end = *it;
            }
        } else if (it == keyValues.constEnd()) {
            --it; //position the iterator on the last item
            if (it->first == 1 && keyValues.size() > 1) {
                //we have an end value (item with progress = 1)
                currentInterval.start = *(it-1);
                currentInterval.end = *it;
            } else {
                //we use the default end value here
                currentInterval.start = *it;
                currentInterval.end = {qreal(1), defaultStartEndValue};
            }
        } else {
            currentInterval.start = *(it-1);
            currentInterval.end = *it;
        }

        // update all the values of the currentInterval
        updateInterpolator();
    }
    setCurrentValueForProgress(progress);
}

//  from src/corelib/animation/qvariantanimation.cpp, line 269, as _ZNK24QVariantAnimationPrivate7valueAtEd
inline QVariant QVariantAnimationPrivate::valueAt(qreal step) const
{
    const auto sought = std::pair{step, QVariant()};
    const auto result = std::lower_bound(keyValues.cbegin(), keyValues.cend(), sought,
                                         animationValueLessThan);
    if (result != keyValues.cend() && !animationValueLessThan(sought, *result))
        return result->second;

    return QVariant();
}

//  from src/corelib/animation/qvariantanimation.cpp, line 280, as _ZN24QVariantAnimationPrivate10setValueAtEdRK8QVariant
inline void QVariantAnimationPrivate::setValueAt(qreal step, const QVariant &value)
{
    if (step < qreal(0.0) || step > qreal(1.0)) {
        qWarning("QVariantAnimation::setValueAt: invalid step = %f", step);
        return;
    }

    QVariantAnimation::KeyValue pair(step, value);

    QVariantAnimation::KeyValues::iterator result = std::lower_bound(keyValues.begin(), keyValues.end(), pair, animationValueLessThan);
    if (result == keyValues.end() || result->first != step) {
        keyValues.insert(result, pair);
    } else {
        if (value.isValid())
            result->second = value; // replaces the previous value
        else
            keyValues.erase(result); // removes the previous value
    }

    recalculateCurrentInterval(/*force=*/true);
}

//  from src/corelib/animation/qvariantanimation.cpp, line 302, as _ZN24QVariantAnimationPrivate23setDefaultStartEndValueERK8QVariant
inline void QVariantAnimationPrivate::setDefaultStartEndValue(const QVariant &value)
{
    defaultStartEndValue = value;
    recalculateCurrentInterval(/*force=*/true);
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

//  QVariantAnimation::Interpolator
//      QVariantAnimationPrivate::getInterpolator(int interpolationTy
//      pe)
extern "C" Q_DECL_EXPORT
void * ritual_ZN24QVariantAnimationPrivate15getInterpolatorEi(
    int interpolationType) {
  return reinterpret_cast<void *>(reinterpret_cast<void (*)()>(
      QVariantAnimationPrivate::getInterpolator(interpolationType)));
}

//  void QVariantAnimationPrivate::updateInterpolator()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate18updateInterpolatorEv(
    QVariantAnimationPrivate *self) {
  self->updateInterpolator();
}

//  void QVariantAnimationPrivate::recalculateCurrentInterval(bool
//      force)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate26recalculateCurrentIntervalEb(
    QVariantAnimationPrivate *self,
    bool force) {
  self->recalculateCurrentInterval(force);
}

//  QVariant QVariantAnimationPrivate::valueAt(qreal step) const
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZNK24QVariantAnimationPrivate7valueAtEd(
    const QVariantAnimationPrivate *self,
    double step) {
  return new QVariant(self->valueAt(step));
}

//  void QVariantAnimationPrivate::setValueAt(qreal, const QVarian
//      t &)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate10setValueAtEdRK8QVariant(
    QVariantAnimationPrivate *self,
    double step,
    const QVariant *value) {
  self->setValueAt(step, *value);
}

//  void QVariantAnimationPrivate::setDefaultStartEndValue(const Q
//      Variant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVariantAnimationPrivate23setDefaultStartEndValueERK8QVariant(
    QVariantAnimationPrivate *self,
    const QVariant *value) {
  self->setDefaultStartEndValue(*value);
}

#endif  // QT_CONFIG(animation)
