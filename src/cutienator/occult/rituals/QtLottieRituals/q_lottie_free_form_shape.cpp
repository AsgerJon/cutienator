//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiefreeformshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiefreeformshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qpoint.h>
#include <QtCore/QPointF>

//  QLottieFreeFormShape::QLottieFreeFormShape(const QLottieFreeFormShape
//      &other)
extern "C" Q_DECL_EXPORT
QLottieFreeFormShape *ritual_ZN20QLottieFreeFormShapeC1ERKS_(
    const QLottieFreeFormShape *other) {
  return new QLottieFreeFormShape(*other);
}

//  QLottieFreeFormShape::QLottieFreeFormShape(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieFreeFormShape *ritual_ZN20QLottieFreeFormShapeC1EP11QLottieBase(
    QLottieBase *parent) {
  return new QLottieFreeFormShape(parent);
}

//  QLottieBase *QLottieFreeFormShape::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK20QLottieFreeFormShape5cloneEv(
    const QLottieFreeFormShape *self) {
  return self->clone();
}

//  int QLottieFreeFormShape::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QLottieFreeFormShape5parseERK11QJsonObject(
    QLottieFreeFormShape *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieFreeFormShape::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape16updatePropertiesEi(
    QLottieFreeFormShape *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieFreeFormShape::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QLottieFreeFormShape6renderER15QLottieRenderer(
    const QLottieFreeFormShape *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  bool QLottieFreeFormShape::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QLottieFreeFormShape11acceptsTrimEv(
    const QLottieFreeFormShape *self) {
  return self->acceptsTrim();
}

//  bool QLottieFreeFormShape::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QLottieFreeFormShape10isAnimatedEv(
    const QLottieFreeFormShape *self) {
  return self->isAnimated();
}

//  QLottieProperty2D<QPointF> QLottieFreeFormShape::startPointProperty()
//      const
extern "C" Q_DECL_EXPORT
QLottieProperty2D<QPointF> *ritual_ZNK20QLottieFreeFormShape18startPointPropertyEv(
    const QLottieFreeFormShape *self) {
  return new QLottieProperty2D<QPointF>(self->startPointProperty());
}

//  void QLottieFreeFormShape::parseShapeKeyframes(QJsonObject &keyframes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape19parseShapeKeyframesER11QJsonObject(
    QLottieFreeFormShape *self,
    QJsonObject *keyframes) {
  self->parseShapeKeyframes(*keyframes);
}

//  void QLottieFreeFormShape::buildShape(const QJsonObject &keyframe)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape10buildShapeERK11QJsonObject(
    QLottieFreeFormShape *self,
    const QJsonObject *keyframe) {
  self->buildShape(*keyframe);
}

//  void QLottieFreeFormShape::buildShape(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape10buildShapeEi(
    QLottieFreeFormShape *self,
    int frame) {
  self->buildShape(frame);
}

//  void QLottieFreeFormShape::parseEasedVertices(const QJsonObject
//      &keyframe, int startFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape18parseEasedVerticesERK11QJsonObjecti(
    QLottieFreeFormShape *self,
    const QJsonObject *keyframe,
    int startFrame) {
  self->parseEasedVertices(*keyframe, startFrame);
}

//  void QLottieFreeFormShape::finalizeVertices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape16finalizeVerticesEv(
    QLottieFreeFormShape *self) {
  self->finalizeVertices();
}

//  QJsonObject QLottieFreeFormShape::createKeyframe(QJsonArray startValue,
//      QJsonArray endValue, int startFrame, QJsonObject easingIn,
//      QJsonObject easingOut)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN20QLottieFreeFormShape14createKeyframeE10QJsonArrayS0_i11QJsonObjectS1_(
    QLottieFreeFormShape *self,
    const QJsonArray *startValue,
    const QJsonArray *endValue,
    int startFrame,
    const QJsonObject *easingIn,
    const QJsonObject *easingOut) {
  return new QJsonObject(
      self->createKeyframe(
          *startValue,
          *endValue,
          startFrame,
          *easingIn,
          *easingOut));
}

//  void QLottieFreeFormShape::addCurve(QPointF start, QPointF ctlOffset1,
//      QPointF ctlOffset2, QPointF end)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShape8addCurveE7QPointFS0_S0_S0_(
    QLottieFreeFormShape *self,
    const QPointF *start,
    const QPointF *ctlOffset1,
    const QPointF *ctlOffset2,
    const QPointF *end) {
  self->addCurve(*start, *ctlOffset1, *ctlOffset2, *end);
}

//  QLottieFreeFormShape::~QLottieFreeFormShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLottieFreeFormShapeD1Ev(QLottieFreeFormShape *self) {
  delete self;
}

//  QLottieBase *QLottieFreeFormShape::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK20QLottieFreeFormShape5cloneEv(
    const QLottieFreeFormShape *self) {
  return self->QLottieFreeFormShape::clone();
}

//  int QLottieFreeFormShape::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN20QLottieFreeFormShape5parseERK11QJsonObject(
    QLottieFreeFormShape *self,
    const QJsonObject *definition) {
  return self->QLottieFreeFormShape::parse(*definition);
}

//  void QLottieFreeFormShape::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLottieFreeFormShape16updatePropertiesEi(
    QLottieFreeFormShape *self,
    int frame) {
  self->QLottieFreeFormShape::updateProperties(frame);
}

//  bool QLottieFreeFormShape::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QLottieFreeFormShape11acceptsTrimEv(
    const QLottieFreeFormShape *self) {
  return self->QLottieFreeFormShape::acceptsTrim();
}

//  bool QLottieFreeFormShape::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QLottieFreeFormShape10isAnimatedEv(
    const QLottieFreeFormShape *self) {
  return self->QLottieFreeFormShape::isAnimated();
}

//  a QLottieProperty2D<QPointF> a ritual of QLottieFreeFormShape gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLottieFreeFormShape__QLottieProperty2D_QPointF(
    QLottieProperty2D<QPointF> *self) {
  delete self;
}
