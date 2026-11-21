//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariantanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariantanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qeasingcurve.h>

//  const QMetaObject *QVariantAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QVariantAnimation10metaObjectEv(
    const QVariantAnimation *self) {
  return self->metaObject();
}

//  QString QVariantAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QVariantAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVariantAnimation::tr(s, c, n));
}

//  QVariantAnimation::QVariantAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QVariantAnimation *ritual_ZN17QVariantAnimationC1EP7QObject(
    QObject *parent) {
  return new QVariantAnimation(parent);
}

//  QVariantAnimation::~QVariantAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimationD1Ev(QVariantAnimation *self) {
  delete self;
}

//  QVariant QVariantAnimation::startValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation10startValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->startValue());
}

//  void QVariantAnimation::setStartValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation13setStartValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  self->setStartValue(*value);
}

//  QVariant QVariantAnimation::endValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation8endValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->endValue());
}

//  void QVariantAnimation::setEndValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation11setEndValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  self->setEndValue(*value);
}

//  QVariant QVariantAnimation::keyValueAt(qreal step) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation10keyValueAtEd(
    const QVariantAnimation *self,
    qreal step) {
  return new QVariant(self->keyValueAt(step));
}

//  void QVariantAnimation::setKeyValueAt(qreal step, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation13setKeyValueAtEdRK8QVariant(
    QVariantAnimation *self,
    qreal step,
    const QVariant *value) {
  self->setKeyValueAt(step, *value);
}

//  QVariant QVariantAnimation::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation12currentValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->currentValue());
}

//  int QVariantAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QVariantAnimation8durationEv(const QVariantAnimation *self) {
  return self->duration();
}

//  void QVariantAnimation::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation11setDurationEi(
    QVariantAnimation *self,
    int msecs) {
  self->setDuration(msecs);
}

//  QEasingCurve QVariantAnimation::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK17QVariantAnimation11easingCurveEv(
    const QVariantAnimation *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QVariantAnimation::setEasingCurve(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation14setEasingCurveERK12QEasingCurve(
    QVariantAnimation *self,
    const QEasingCurve *easing) {
  self->setEasingCurve(*easing);
}
