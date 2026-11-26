//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qvertexblendanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qvertexblendanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <Qt3DAnimation/Qt3DAnimation>

//  const QMetaObject *Qt3DAnimation::QVertexBlendAnimation::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation10metaObjectEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QVertexBlendAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation21QVertexBlendAnimation11qt_metacastEPKc(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QVertexBlendAnimation::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation21QVertexBlendAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QVertexBlendAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  Qt3DAnimation::QVertexBlendAnimation::QVertexBlendAnimation(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QVertexBlendAnimation *ritual_ZN13Qt3DAnimation21QVertexBlendAnimationC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QVertexBlendAnimation(parent);
}

//  QList<float> Qt3DAnimation::QVertexBlendAnimation::targetPositions()
//      const
extern "C" Q_DECL_EXPORT
QList<float> *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation15targetPositionsEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return new QList<float>(self->targetPositions());
}

//  float Qt3DAnimation::QVertexBlendAnimation::interpolator() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation12interpolatorEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->interpolator();
}

//  Qt3DRender::QGeometryRenderer
//      *Qt3DAnimation::QVertexBlendAnimation::target() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation6targetEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return self->target();
}

//  QString Qt3DAnimation::QVertexBlendAnimation::targetName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation10targetNameEv(
    const Qt3DAnimation::QVertexBlendAnimation *self) {
  return new QString(self->targetName());
}

//  void Qt3DAnimation::QVertexBlendAnimation::setMorphTargets(const
//      QList<Qt3DAnimation::QMorphTarget *> &targets)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation15setMorphTargetsERK5QListIPNS_12QMorphTargetEE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const QList<Qt3DAnimation::QMorphTarget *> *targets) {
  self->setMorphTargets(*targets);
}

//  void Qt3DAnimation::QVertexBlendAnimation::addMorphTarget(Qt3DAnimation::
//      QMorphTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation14addMorphTargetEPNS_12QMorphTargetE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    Qt3DAnimation::QMorphTarget *target) {
  self->addMorphTarget(target);
}

//  void Qt3DAnimation::QVertexBlendAnimation::removeMorphTarget(Qt3DAnimatio
//      n::QMorphTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation17removeMorphTargetEPNS_12QMorphTargetE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    Qt3DAnimation::QMorphTarget *target) {
  self->removeMorphTarget(target);
}

//  QList<Qt3DAnimation::QMorphTarget *>
//      Qt3DAnimation::QVertexBlendAnimation::morphTargetList()
extern "C" Q_DECL_EXPORT
QList<Qt3DAnimation::QMorphTarget *> *ritual_ZN13Qt3DAnimation21QVertexBlendAnimation15morphTargetListEv(
    Qt3DAnimation::QVertexBlendAnimation *self) {
  return new QList<Qt3DAnimation::QMorphTarget *>(self->morphTargetList());
}

//  void Qt3DAnimation::QVertexBlendAnimation::setTargetPositions(const
//      QList<float> &targetPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation18setTargetPositionsERK5QListIfE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const QList<float> *targetPositions) {
  self->setTargetPositions(*targetPositions);
}

//  void Qt3DAnimation::QVertexBlendAnimation::setTarget(Qt3DRender::QGeometr
//      yRenderer *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation9setTargetEPN10Qt3DRender17QGeometryRendererE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    Qt3DRender::QGeometryRenderer *target) {
  self->setTarget(target);
}

//  void Qt3DAnimation::QVertexBlendAnimation::setTargetName(const QString
//      name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation13setTargetNameE7QString(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const QString *name) {
  self->setTargetName(*name);
}

//  void Qt3DAnimation::QVertexBlendAnimation::targetPositionsChanged(const
//      QList<float> &targetPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation22targetPositionsChangedERK5QListIfE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const QList<float> *targetPositions) {
  self->targetPositionsChanged(*targetPositions);
}

//  void Qt3DAnimation::QVertexBlendAnimation::interpolatorChanged(float
//      interpolator)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation19interpolatorChangedEf(
    Qt3DAnimation::QVertexBlendAnimation *self,
    float interpolator) {
  self->interpolatorChanged(interpolator);
}

//  void Qt3DAnimation::QVertexBlendAnimation::targetChanged(Qt3DRender::QGeo
//      metryRenderer *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation13targetChangedEPN10Qt3DRender17QGeometryRendererE(
    Qt3DAnimation::QVertexBlendAnimation *self,
    Qt3DRender::QGeometryRenderer *target) {
  self->targetChanged(target);
}

//  void Qt3DAnimation::QVertexBlendAnimation::targetNameChanged(const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation17targetNameChangedERK7QString(
    Qt3DAnimation::QVertexBlendAnimation *self,
    const QString *name) {
  self->targetNameChanged(*name);
}

//  void Qt3DAnimation::QVertexBlendAnimation::updateAnimation(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation21QVertexBlendAnimation15updateAnimationEf(
    Qt3DAnimation::QVertexBlendAnimation *self,
    float position) {
  self->updateAnimation(position);
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

//  a QList<float> a ritual of Qt3DAnimation::QVertexBlendAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QVertexBlendAnimation__QList_float(
    QList<float> *self) {
  delete self;
}

//  a QList<Qt3DAnimation::QMorphTarget *> a ritual of
//      Qt3DAnimation::QVertexBlendAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QVertexBlendAnimation__QList_Qt3DAnimation_QMorphTarget(
    QList<Qt3DAnimation::QMorphTarget *> *self) {
  delete self;
}
