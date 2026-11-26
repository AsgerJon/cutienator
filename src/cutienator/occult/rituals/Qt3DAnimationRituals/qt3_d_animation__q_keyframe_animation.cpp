//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qkeyframeanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qkeyframeanimation.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  const QMetaObject *Qt3DAnimation::QKeyframeAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation10metaObjectEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QKeyframeAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation18QKeyframeAnimation11qt_metacastEPKc(
    Qt3DAnimation::QKeyframeAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QKeyframeAnimation::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation18QKeyframeAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QKeyframeAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QKeyframeAnimation::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation18QKeyframeAnimation2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QKeyframeAnimation::tr(s, c, n));
}

//  Qt3DAnimation::QKeyframeAnimation::QKeyframeAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimation *ritual_ZN13Qt3DAnimation18QKeyframeAnimationC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QKeyframeAnimation(parent);
}

//  QList<float> Qt3DAnimation::QKeyframeAnimation::framePositions() const
extern "C" Q_DECL_EXPORT
QList<float> *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation14framePositionsEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return new QList<float>(self->framePositions());
}

//  QList<Qt3DCore::QTransform *>
//      Qt3DAnimation::QKeyframeAnimation::keyframeList() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QTransform *> *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation12keyframeListEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return new QList<Qt3DCore::QTransform *>(self->keyframeList());
}

//  Qt3DCore::QTransform *Qt3DAnimation::QKeyframeAnimation::target() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransform *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation6targetEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->target();
}

//  QEasingCurve Qt3DAnimation::QKeyframeAnimation::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation6easingEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return new QEasingCurve(self->easing());
}

//  QString Qt3DAnimation::QKeyframeAnimation::targetName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation10targetNameEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return new QString(self->targetName());
}

//  RepeatMode Qt3DAnimation::QKeyframeAnimation::startMode() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimation::RepeatMode ritual_ZNK13Qt3DAnimation18QKeyframeAnimation9startModeEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->startMode();
}

//  RepeatMode Qt3DAnimation::QKeyframeAnimation::endMode() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimation::RepeatMode ritual_ZNK13Qt3DAnimation18QKeyframeAnimation7endModeEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->endMode();
}

//  void Qt3DAnimation::QKeyframeAnimation::setKeyframes(const
//      QList<Qt3DCore::QTransform *> &keyframes)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation12setKeyframesERK5QListIPN8Qt3DCore10QTransformEE(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QList<Qt3DCore::QTransform *> *keyframes) {
  self->setKeyframes(*keyframes);
}

//  void Qt3DAnimation::QKeyframeAnimation::addKeyframe(Qt3DCore::QTransform
//      *keyframe)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation11addKeyframeEPN8Qt3DCore10QTransformE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DCore::QTransform *keyframe) {
  self->addKeyframe(keyframe);
}

//  void
//      Qt3DAnimation::QKeyframeAnimation::removeKeyframe(Qt3DCore::QTransfor
//      m *keyframe)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation14removeKeyframeEPN8Qt3DCore10QTransformE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DCore::QTransform *keyframe) {
  self->removeKeyframe(keyframe);
}

//  void Qt3DAnimation::QKeyframeAnimation::setFramePositions(const
//      QList<float> &positions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation17setFramePositionsERK5QListIfE(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QList<float> *positions) {
  self->setFramePositions(*positions);
}

//  void Qt3DAnimation::QKeyframeAnimation::setTarget(Qt3DCore::QTransform
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation9setTargetEPN8Qt3DCore10QTransformE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DCore::QTransform *target) {
  self->setTarget(target);
}

//  void Qt3DAnimation::QKeyframeAnimation::setEasing(const QEasingCurve
//      &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation9setEasingERK12QEasingCurve(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QEasingCurve *easing) {
  self->setEasing(*easing);
}

//  void Qt3DAnimation::QKeyframeAnimation::setTargetName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation13setTargetNameERK7QString(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QString *name) {
  self->setTargetName(*name);
}

//  void Qt3DAnimation::QKeyframeAnimation::setStartMode(RepeatMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation12setStartModeENS0_10RepeatModeE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DAnimation::QKeyframeAnimation::RepeatMode mode) {
  self->setStartMode(mode);
}

//  void Qt3DAnimation::QKeyframeAnimation::setEndMode(RepeatMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation10setEndModeENS0_10RepeatModeE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DAnimation::QKeyframeAnimation::RepeatMode mode) {
  self->setEndMode(mode);
}

//  void Qt3DAnimation::QKeyframeAnimation::framePositionsChanged(const
//      QList<float> &positions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation21framePositionsChangedERK5QListIfE(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QList<float> *positions) {
  self->framePositionsChanged(*positions);
}

//  void
//      Qt3DAnimation::QKeyframeAnimation::targetChanged(Qt3DCore::QTransform
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation13targetChangedEPN8Qt3DCore10QTransformE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DCore::QTransform *target) {
  self->targetChanged(target);
}

//  void Qt3DAnimation::QKeyframeAnimation::easingChanged(const QEasingCurve
//      &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation13easingChangedERK12QEasingCurve(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QEasingCurve *easing) {
  self->easingChanged(*easing);
}

//  void Qt3DAnimation::QKeyframeAnimation::targetNameChanged(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation17targetNameChangedERK7QString(
    Qt3DAnimation::QKeyframeAnimation *self,
    const QString *name) {
  self->targetNameChanged(*name);
}

//  void Qt3DAnimation::QKeyframeAnimation::startModeChanged(QKeyframeAnimati
//      on::RepeatMode startMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation16startModeChangedENS0_10RepeatModeE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DAnimation::QKeyframeAnimation::RepeatMode startMode) {
  self->startModeChanged(startMode);
}

//  void Qt3DAnimation::QKeyframeAnimation::endModeChanged(QKeyframeAnimation
//      ::RepeatMode endMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation14endModeChangedENS0_10RepeatModeE(
    Qt3DAnimation::QKeyframeAnimation *self,
    Qt3DAnimation::QKeyframeAnimation::RepeatMode endMode) {
  self->endModeChanged(endMode);
}

//  void Qt3DAnimation::QKeyframeAnimation::updateAnimation(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QKeyframeAnimation15updateAnimationEf(
    Qt3DAnimation::QKeyframeAnimation *self,
    float position) {
  self->updateAnimation(position);
}

//  QKeyframeAnimationPrivate *Qt3DAnimation::QKeyframeAnimation::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimationPrivate *ritual_ZN13Qt3DAnimation18QKeyframeAnimation6d_funcEv(
    Qt3DAnimation::QKeyframeAnimation *self) {
  return self->d_func();
}

//  const QKeyframeAnimationPrivate
//      *Qt3DAnimation::QKeyframeAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QKeyframeAnimationPrivate *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation6d_funcEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->d_func();
}

//  a QList<float> a ritual of Qt3DAnimation::QKeyframeAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QKeyframeAnimation__QList_float(
    QList<float> *self) {
  delete self;
}

//  a QList<Qt3DCore::QTransform *> a ritual of
//      Qt3DAnimation::QKeyframeAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QKeyframeAnimation__QList_Qt3DCore_QTransform(
    QList<Qt3DCore::QTransform *> *self) {
  delete self;
}
