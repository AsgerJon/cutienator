//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QNumberStyleAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNumberStyleAnimation : QNumberStyleAnimation {
  using QNumberStyleAnimation::isUpdateNeeded;
};

//  const QMetaObject *QNumberStyleAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNumberStyleAnimation10metaObjectEv(
    const QNumberStyleAnimation *self) {
  return self->metaObject();
}

//  QString QNumberStyleAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QNumberStyleAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNumberStyleAnimation::tr(s, c, n));
}

//  QNumberStyleAnimation::QNumberStyleAnimation(QObject *target)
extern "C" Q_DECL_EXPORT
QNumberStyleAnimation *ritual_ZN21QNumberStyleAnimationC1EP7QObject(
    QObject *target) {
  return new QNumberStyleAnimation(target);
}

//  qreal QNumberStyleAnimation::startValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QNumberStyleAnimation10startValueEv(
    const QNumberStyleAnimation *self) {
  return self->startValue();
}

//  void QNumberStyleAnimation::setStartValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNumberStyleAnimation13setStartValueEd(
    QNumberStyleAnimation *self,
    qreal value) {
  self->setStartValue(value);
}

//  qreal QNumberStyleAnimation::endValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QNumberStyleAnimation8endValueEv(
    const QNumberStyleAnimation *self) {
  return self->endValue();
}

//  void QNumberStyleAnimation::setEndValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNumberStyleAnimation11setEndValueEd(
    QNumberStyleAnimation *self,
    qreal value) {
  self->setEndValue(value);
}

//  qreal QNumberStyleAnimation::currentValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QNumberStyleAnimation12currentValueEv(
    const QNumberStyleAnimation *self) {
  return self->currentValue();
}

//  bool QNumberStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNumberStyleAnimation14isUpdateNeededEv(
    const QNumberStyleAnimation *self) {
  return self->isUpdateNeeded();
}

//  bool QNumberStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QNumberStyleAnimation14isUpdateNeededEv(
    const QNumberStyleAnimation *self) {
  return static_cast<const OwnQNumberStyleAnimation *>(self)->OwnQNumberStyleAnimation::isUpdateNeeded();
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
