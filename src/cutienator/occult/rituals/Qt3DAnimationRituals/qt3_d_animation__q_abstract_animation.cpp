//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qabstractanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qabstractanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QAbstractAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QAbstractAnimation10metaObjectEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAbstractAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation18QAbstractAnimation11qt_metacastEPKc(
    Qt3DAnimation::QAbstractAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAbstractAnimation::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation18QAbstractAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAbstractAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAbstractAnimation::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation18QAbstractAnimation2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAbstractAnimation::tr(s, c, n));
}

//  QString Qt3DAnimation::QAbstractAnimation::animationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation18QAbstractAnimation13animationNameEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return new QString(self->animationName());
}

//  QAbstractAnimation::AnimationType
//      Qt3DAnimation::QAbstractAnimation::animationType() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimation::AnimationType ritual_ZNK13Qt3DAnimation18QAbstractAnimation13animationTypeEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return self->animationType();
}

//  float Qt3DAnimation::QAbstractAnimation::position() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation18QAbstractAnimation8positionEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return self->position();
}

//  float Qt3DAnimation::QAbstractAnimation::duration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation18QAbstractAnimation8durationEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return self->duration();
}

//  void Qt3DAnimation::QAbstractAnimation::setAnimationName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation16setAnimationNameERK7QString(
    Qt3DAnimation::QAbstractAnimation *self,
    const QString *name) {
  self->setAnimationName(*name);
}

//  void Qt3DAnimation::QAbstractAnimation::setPosition(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation11setPositionEf(
    Qt3DAnimation::QAbstractAnimation *self,
    float position) {
  self->setPosition(position);
}

//  Qt3DAnimation::QAbstractAnimation::QAbstractAnimation(QAbstractAnimationP
//      rivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimation *ritual_ZN13Qt3DAnimation18QAbstractAnimationC1ERNS_25QAbstractAnimationPrivateEP7QObject(
    Qt3DAnimation::QAbstractAnimationPrivate *dd,
    QObject *parent) {
  return new Qt3DAnimation::QAbstractAnimation(*dd, parent);
}

//  void Qt3DAnimation::QAbstractAnimation::setDuration(float duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation11setDurationEf(
    Qt3DAnimation::QAbstractAnimation *self,
    float duration) {
  self->setDuration(duration);
}

//  void Qt3DAnimation::QAbstractAnimation::animationNameChanged(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation20animationNameChangedERK7QString(
    Qt3DAnimation::QAbstractAnimation *self,
    const QString *name) {
  self->animationNameChanged(*name);
}

//  void Qt3DAnimation::QAbstractAnimation::positionChanged(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation15positionChangedEf(
    Qt3DAnimation::QAbstractAnimation *self,
    float position) {
  self->positionChanged(position);
}

//  void Qt3DAnimation::QAbstractAnimation::durationChanged(float duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAbstractAnimation15durationChangedEf(
    Qt3DAnimation::QAbstractAnimation *self,
    float duration) {
  self->durationChanged(duration);
}

//  QAbstractAnimationPrivate *Qt3DAnimation::QAbstractAnimation::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimationPrivate *ritual_ZN13Qt3DAnimation18QAbstractAnimation6d_funcEv(
    Qt3DAnimation::QAbstractAnimation *self) {
  return self->d_func();
}

//  const QAbstractAnimationPrivate
//      *Qt3DAnimation::QAbstractAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAbstractAnimationPrivate *ritual_ZNK13Qt3DAnimation18QAbstractAnimation6d_funcEv(
    const Qt3DAnimation::QAbstractAnimation *self) {
  return self->d_func();
}
