//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(easingcurve)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qeasingcurve.h>

//  void QQmlEasingValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType20qt_qmlMarker_foreignEv(
    QQmlEasingValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlEasingValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType21qt_qmlMarker_extendedEv(
    QQmlEasingValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlEasingValueType::QQmlEasingValueType()
extern "C" Q_DECL_EXPORT
QQmlEasingValueType *ritual_ZN19QQmlEasingValueTypeC1Ev() {
  return new QQmlEasingValueType();
}

//  QQmlEasingValueType::QQmlEasingValueType(QQmlEasing::Type type)
extern "C" Q_DECL_EXPORT
QQmlEasingValueType *ritual_ZN19QQmlEasingValueTypeC1EN10QQmlEasing4TypeE(
    QQmlEasing::Type type) {
  return new QQmlEasingValueType(type);
}

//  QQmlEasingValueType::QQmlEasingValueType(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
QQmlEasingValueType *ritual_ZN19QQmlEasingValueTypeC1ERK12QEasingCurve(
    const QEasingCurve *easing) {
  return new QQmlEasingValueType(*easing);
}

//  qreal QQmlEasingValueType::valueForProgress(qreal progress)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN19QQmlEasingValueType16valueForProgressEd(
    QQmlEasingValueType *self,
    qreal progress) {
  return self->valueForProgress(progress);
}

//  QQmlEasing::Type QQmlEasingValueType::type() const
extern "C" Q_DECL_EXPORT
QQmlEasing::Type ritual_ZNK19QQmlEasingValueType4typeEv(
    const QQmlEasingValueType *self) {
  return self->type();
}

//  qreal QQmlEasingValueType::amplitude() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQmlEasingValueType9amplitudeEv(
    const QQmlEasingValueType *self) {
  return self->amplitude();
}

//  qreal QQmlEasingValueType::overshoot() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQmlEasingValueType9overshootEv(
    const QQmlEasingValueType *self) {
  return self->overshoot();
}

//  qreal QQmlEasingValueType::period() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQmlEasingValueType6periodEv(
    const QQmlEasingValueType *self) {
  return self->period();
}

//  void QQmlEasingValueType::setType(QQmlEasing::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType7setTypeEN10QQmlEasing4TypeE(
    QQmlEasingValueType *self,
    QQmlEasing::Type a0) {
  self->setType(a0);
}

//  void QQmlEasingValueType::setAmplitude(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType12setAmplitudeEd(
    QQmlEasingValueType *self,
    qreal a0) {
  self->setAmplitude(a0);
}

//  void QQmlEasingValueType::setOvershoot(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType12setOvershootEd(
    QQmlEasingValueType *self,
    qreal a0) {
  self->setOvershoot(a0);
}

//  void QQmlEasingValueType::setPeriod(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueType9setPeriodEd(
    QQmlEasingValueType *self,
    qreal a0) {
  self->setPeriod(a0);
}

//  QQmlEasingValueType::~QQmlEasingValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlEasingValueTypeD1Ev(QQmlEasingValueType *self) {
  delete self;
}

#endif  // QT_CONFIG(easingcurve)
