//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qmorphinganimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qmorphinganimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QMorphingAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QMorphingAnimation10metaObjectEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::QMorphingAnimation::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation18QMorphingAnimation2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QMorphingAnimation::tr(s, c, n));
}

//  QMorphingAnimationPrivate *Qt3DAnimation::QMorphingAnimation::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimationPrivate *ritual_ZN13Qt3DAnimation18QMorphingAnimation6d_funcEv(
    Qt3DAnimation::QMorphingAnimation *self) {
  return self->d_func();
}

//  const QMorphingAnimationPrivate
//      *Qt3DAnimation::QMorphingAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QMorphingAnimationPrivate *ritual_ZNK13Qt3DAnimation18QMorphingAnimation6d_funcEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->d_func();
}
