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

//  Only a class built on QProgressStyleAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQProgressStyleAnimation : QProgressStyleAnimation {
  using QProgressStyleAnimation::isUpdateNeeded;
};

//  const QMetaObject *QProgressStyleAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QProgressStyleAnimation10metaObjectEv(
    const QProgressStyleAnimation *self) {
  return self->metaObject();
}

//  QString QProgressStyleAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QProgressStyleAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProgressStyleAnimation::tr(s, c, n));
}

//  QProgressStyleAnimation::QProgressStyleAnimation(int speed, QObject
//      *target)
extern "C" Q_DECL_EXPORT
QProgressStyleAnimation *ritual_ZN23QProgressStyleAnimationC1EiP7QObject(
    int speed,
    QObject *target) {
  return new QProgressStyleAnimation(speed, target);
}

//  int QProgressStyleAnimation::animationStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QProgressStyleAnimation13animationStepEv(
    const QProgressStyleAnimation *self) {
  return self->animationStep();
}

//  int QProgressStyleAnimation::progressStep(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QProgressStyleAnimation12progressStepEi(
    const QProgressStyleAnimation *self,
    int width) {
  return self->progressStep(width);
}

//  int QProgressStyleAnimation::speed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QProgressStyleAnimation5speedEv(
    const QProgressStyleAnimation *self) {
  return self->speed();
}

//  void QProgressStyleAnimation::setSpeed(int speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProgressStyleAnimation8setSpeedEi(
    QProgressStyleAnimation *self,
    int speed) {
  self->setSpeed(speed);
}

//  bool QProgressStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QProgressStyleAnimation14isUpdateNeededEv(
    const QProgressStyleAnimation *self) {
  return self->isUpdateNeeded();
}

//  bool QProgressStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QProgressStyleAnimation14isUpdateNeededEv(
    const QProgressStyleAnimation *self) {
  return static_cast<const OwnQProgressStyleAnimation *>(self)->OwnQProgressStyleAnimation::isUpdateNeeded();
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
