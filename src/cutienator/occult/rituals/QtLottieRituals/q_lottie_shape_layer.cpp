//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieshapelayer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieshapelayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>

//  QLottieShapeLayer::QLottieShapeLayer()
extern "C" Q_DECL_EXPORT
QLottieShapeLayer *ritual_ZN17QLottieShapeLayerC1Ev() {
  return new QLottieShapeLayer();
}

//  QLottieShapeLayer::QLottieShapeLayer(const QLottieShapeLayer &other)
extern "C" Q_DECL_EXPORT
QLottieShapeLayer *ritual_ZN17QLottieShapeLayerC1ERKS_(
    const QLottieShapeLayer *other) {
  return new QLottieShapeLayer(*other);
}

//  QLottieBase *QLottieShapeLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK17QLottieShapeLayer5cloneEv(
    const QLottieShapeLayer *self) {
  return self->clone();
}

//  void QLottieShapeLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieShapeLayer16updatePropertiesEi(
    QLottieShapeLayer *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieShapeLayer::render(QLottieRenderer &render) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QLottieShapeLayer6renderER15QLottieRenderer(
    const QLottieShapeLayer *self,
    QLottieRenderer *render) {
  self->render(*render);
}

//  int QLottieShapeLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QLottieShapeLayer5parseERK11QJsonObject(
    QLottieShapeLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QLottieShapeLayer::~QLottieShapeLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieShapeLayerD1Ev(QLottieShapeLayer *self) {
  delete self;
}

//  QLottieBase *QLottieShapeLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK17QLottieShapeLayer5cloneEv(
    const QLottieShapeLayer *self) {
  return self->QLottieShapeLayer::clone();
}

//  void QLottieShapeLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QLottieShapeLayer16updatePropertiesEi(
    QLottieShapeLayer *self,
    int frame) {
  self->QLottieShapeLayer::updateProperties(frame);
}

//  int QLottieShapeLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QLottieShapeLayer5parseERK11QJsonObject(
    QLottieShapeLayer *self,
    const QJsonObject *definition) {
  return self->QLottieShapeLayer::parse(*definition);
}
