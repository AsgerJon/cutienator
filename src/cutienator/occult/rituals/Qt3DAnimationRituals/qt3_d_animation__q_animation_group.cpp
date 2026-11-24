//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qanimationgroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation15QAnimationGroup10metaObjectEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::QAnimationGroup::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation15QAnimationGroup2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAnimationGroup::tr(s, c, n));
}

//  QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroupPrivate *ritual_ZN13Qt3DAnimation15QAnimationGroup6d_funcEv(
    Qt3DAnimation::QAnimationGroup *self) {
  return self->d_func();
}

//  const QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationGroupPrivate *ritual_ZNK13Qt3DAnimation15QAnimationGroup6d_funcEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->d_func();
}
