//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationcontroller.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qanimationcontroller.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QAnimationController::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation20QAnimationController10metaObjectEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::QAnimationController::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation20QAnimationController2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAnimationController::tr(s, c, n));
}

//  QAnimationControllerPrivate
//      *Qt3DAnimation::QAnimationController::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationControllerPrivate *ritual_ZN13Qt3DAnimation20QAnimationController6d_funcEv(
    Qt3DAnimation::QAnimationController *self) {
  return self->d_func();
}

//  const QAnimationControllerPrivate
//      *Qt3DAnimation::QAnimationController::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationControllerPrivate *ritual_ZNK13Qt3DAnimation20QAnimationController6d_funcEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->d_func();
}
