//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qmorphinganimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qmorphinganimation.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/QVector>
#include <Qt3DAnimation/Qt3DAnimation>

//  const QMetaObject *Qt3DAnimation::QMorphingAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation18QMorphingAnimation10metaObjectEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QMorphingAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation18QMorphingAnimation11qt_metacastEPKc(
    Qt3DAnimation::QMorphingAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QMorphingAnimation::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation18QMorphingAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QMorphingAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  Qt3DAnimation::QMorphingAnimation::QMorphingAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimation *ritual_ZN13Qt3DAnimation18QMorphingAnimationC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QMorphingAnimation(parent);
}

//  QVector<float> Qt3DAnimation::QMorphingAnimation::targetPositions() const
extern "C" Q_DECL_EXPORT
QVector<float> *ritual_ZNK13Qt3DAnimation18QMorphingAnimation15targetPositionsEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return new QVector<float>(self->targetPositions());
}

//  float Qt3DAnimation::QMorphingAnimation::interpolator() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation18QMorphingAnimation12interpolatorEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->interpolator();
}

//  Qt3DRender::QGeometryRenderer
//      *Qt3DAnimation::QMorphingAnimation::target() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer *ritual_ZNK13Qt3DAnimation18QMorphingAnimation6targetEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->target();
}

//  QString Qt3DAnimation::QMorphingAnimation::targetName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation18QMorphingAnimation10targetNameEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return new QString(self->targetName());
}

//  QMorphingAnimation::Method Qt3DAnimation::QMorphingAnimation::method()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimation::Method ritual_ZNK13Qt3DAnimation18QMorphingAnimation6methodEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return self->method();
}

//  QEasingCurve Qt3DAnimation::QMorphingAnimation::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK13Qt3DAnimation18QMorphingAnimation6easingEv(
    const Qt3DAnimation::QMorphingAnimation *self) {
  return new QEasingCurve(self->easing());
}

//  void Qt3DAnimation::QMorphingAnimation::setMorphTargets(const
//      QVector<Qt3DAnimation::QMorphTarget *> &targets)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation15setMorphTargetsERK5QListIPNS_12QMorphTargetEE(
    Qt3DAnimation::QMorphingAnimation *self,
    const QVector<Qt3DAnimation::QMorphTarget *> *targets) {
  self->setMorphTargets(*targets);
}

//  void Qt3DAnimation::QMorphingAnimation::addMorphTarget(Qt3DAnimation::QMo
//      rphTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation14addMorphTargetEPNS_12QMorphTargetE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DAnimation::QMorphTarget *target) {
  self->addMorphTarget(target);
}

//  void Qt3DAnimation::QMorphingAnimation::removeMorphTarget(Qt3DAnimation::
//      QMorphTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation17removeMorphTargetEPNS_12QMorphTargetE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DAnimation::QMorphTarget *target) {
  self->removeMorphTarget(target);
}

//  void Qt3DAnimation::QMorphingAnimation::setWeights(int positionIndex,
//      const QVector<float> &weights)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation10setWeightsEiRK5QListIfE(
    Qt3DAnimation::QMorphingAnimation *self,
    int positionIndex,
    const QVector<float> *weights) {
  self->setWeights(positionIndex, *weights);
}

//  QVector<float> Qt3DAnimation::QMorphingAnimation::getWeights(int
//      positionIndex)
extern "C" Q_DECL_EXPORT
QVector<float> *ritual_ZN13Qt3DAnimation18QMorphingAnimation10getWeightsEi(
    Qt3DAnimation::QMorphingAnimation *self,
    int positionIndex) {
  return new QVector<float>(self->getWeights(positionIndex));
}

//  QVector<Qt3DAnimation::QMorphTarget *>
//      Qt3DAnimation::QMorphingAnimation::morphTargetList()
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::QMorphTarget *> *ritual_ZN13Qt3DAnimation18QMorphingAnimation15morphTargetListEv(
    Qt3DAnimation::QMorphingAnimation *self) {
  return new QVector<Qt3DAnimation::QMorphTarget *>(self->morphTargetList());
}

//  void Qt3DAnimation::QMorphingAnimation::setTargetPositions(const
//      QVector<float> &targetPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation18setTargetPositionsERK5QListIfE(
    Qt3DAnimation::QMorphingAnimation *self,
    const QVector<float> *targetPositions) {
  self->setTargetPositions(*targetPositions);
}

//  void Qt3DAnimation::QMorphingAnimation::setTarget(Qt3DRender::QGeometryRe
//      nderer *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation9setTargetEPN10Qt3DRender17QGeometryRendererE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DRender::QGeometryRenderer *target) {
  self->setTarget(target);
}

//  void Qt3DAnimation::QMorphingAnimation::setTargetName(const QString name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation13setTargetNameE7QString(
    Qt3DAnimation::QMorphingAnimation *self,
    const QString *name) {
  self->setTargetName(*name);
}

//  void
//      Qt3DAnimation::QMorphingAnimation::setMethod(QMorphingAnimation::Meth
//      od method)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation9setMethodENS0_6MethodE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DAnimation::QMorphingAnimation::Method method) {
  self->setMethod(method);
}

//  void Qt3DAnimation::QMorphingAnimation::setEasing(const QEasingCurve
//      &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation9setEasingERK12QEasingCurve(
    Qt3DAnimation::QMorphingAnimation *self,
    const QEasingCurve *easing) {
  self->setEasing(*easing);
}

//  void Qt3DAnimation::QMorphingAnimation::targetPositionsChanged(const
//      QVector<float> &targetPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation22targetPositionsChangedERK5QListIfE(
    Qt3DAnimation::QMorphingAnimation *self,
    const QVector<float> *targetPositions) {
  self->targetPositionsChanged(*targetPositions);
}

//  void Qt3DAnimation::QMorphingAnimation::interpolatorChanged(float
//      interpolator)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation19interpolatorChangedEf(
    Qt3DAnimation::QMorphingAnimation *self,
    float interpolator) {
  self->interpolatorChanged(interpolator);
}

//  void Qt3DAnimation::QMorphingAnimation::targetChanged(Qt3DRender::QGeomet
//      ryRenderer *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation13targetChangedEPN10Qt3DRender17QGeometryRendererE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DRender::QGeometryRenderer *target) {
  self->targetChanged(target);
}

//  void Qt3DAnimation::QMorphingAnimation::targetNameChanged(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation17targetNameChangedERK7QString(
    Qt3DAnimation::QMorphingAnimation *self,
    const QString *name) {
  self->targetNameChanged(*name);
}

//  void Qt3DAnimation::QMorphingAnimation::methodChanged(QMorphingAnimation:
//      :Method method)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation13methodChangedENS0_6MethodE(
    Qt3DAnimation::QMorphingAnimation *self,
    Qt3DAnimation::QMorphingAnimation::Method method) {
  self->methodChanged(method);
}

//  void Qt3DAnimation::QMorphingAnimation::easingChanged(const QEasingCurve
//      &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation13easingChangedERK12QEasingCurve(
    Qt3DAnimation::QMorphingAnimation *self,
    const QEasingCurve *easing) {
  self->easingChanged(*easing);
}

//  void Qt3DAnimation::QMorphingAnimation::updateAnimation(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QMorphingAnimation15updateAnimationEf(
    Qt3DAnimation::QMorphingAnimation *self,
    float position) {
  self->updateAnimation(position);
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

//  a QVector<float> a ritual of Qt3DAnimation::QMorphingAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QMorphingAnimation__QVector_float(
    QVector<float> *self) {
  delete self;
}

//  a QVector<Qt3DAnimation::QMorphTarget *> a ritual of
//      Qt3DAnimation::QMorphingAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QMorphingAnimation__QVector_Qt3DAnimation_QMorphTarget(
    QVector<Qt3DAnimation::QMorphTarget *> *self) {
  delete self;
}
