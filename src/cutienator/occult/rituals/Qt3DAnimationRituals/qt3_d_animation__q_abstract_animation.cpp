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

//  QString Qt3DAnimation::QAbstractAnimation::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation18QAbstractAnimation2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAbstractAnimation::tr(s, c, n));
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
