//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qmorphtarget.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qmorphtarget.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DAnimation::QMorphTarget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation12QMorphTarget10metaObjectEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::QMorphTarget::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation12QMorphTarget2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QMorphTarget::tr(s, c, n));
}

//  QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTargetPrivate *ritual_ZN13Qt3DAnimation12QMorphTarget6d_funcEv(
    Qt3DAnimation::QMorphTarget *self) {
  return self->d_func();
}

//  const QMorphTargetPrivate *Qt3DAnimation::QMorphTarget::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QMorphTargetPrivate *ritual_ZNK13Qt3DAnimation12QMorphTarget6d_funcEv(
    const Qt3DAnimation::QMorphTarget *self) {
  return self->d_func();
}
