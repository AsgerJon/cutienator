//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qkeyframeanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qkeyframeanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QKeyframeAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QKeyframeAnimation10metaObjectEv(
    const Qt3DAnimation::QKeyframeAnimation *self) {
  return self->metaObject();
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
