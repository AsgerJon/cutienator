//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qvertexblendanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qvertexblendanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QVertexBlendAnimation::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation10metaObjectEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::QVertexBlendAnimation::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation21QVertexBlendAnimation2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QVertexBlendAnimation::tr(s, c, n));
}

//  QVertexBlendAnimationPrivate
//      *Qt3DAnimation::QVertexBlendAnimation::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QVertexBlendAnimationPrivate *ritual_ZN13Qt3DAnimation21QVertexBlendAnimation6d_funcEv(
    Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->d_func();
}

//  const QVertexBlendAnimationPrivate
//      *Qt3DAnimation::QVertexBlendAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QVertexBlendAnimationPrivate *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation6d_funcEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->d_func();
}
