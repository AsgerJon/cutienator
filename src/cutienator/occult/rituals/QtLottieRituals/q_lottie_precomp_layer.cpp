//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieprecomplayer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieprecomplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>

//  QLottiePrecompLayer::QLottiePrecompLayer()
extern "C" Q_DECL_EXPORT
QLottiePrecompLayer *ritual_ZN19QLottiePrecompLayerC1Ev() {
  return new QLottiePrecompLayer();
}

//  QLottiePrecompLayer::QLottiePrecompLayer(const QLottiePrecompLayer
//      &other)
extern "C" Q_DECL_EXPORT
QLottiePrecompLayer *ritual_ZN19QLottiePrecompLayerC1ERKS_(
    const QLottiePrecompLayer *other) {
  return new QLottiePrecompLayer(*other);
}

//  QLottieBase *QLottiePrecompLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK19QLottiePrecompLayer5cloneEv(
    const QLottiePrecompLayer *self) {
  return self->clone();
}

//  void QLottiePrecompLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLottiePrecompLayer16updatePropertiesEi(
    QLottiePrecompLayer *self,
    int frame) {
  self->updateProperties(frame);
}

//  int QLottiePrecompLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QLottiePrecompLayer5parseERK11QJsonObject(
    QLottiePrecompLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QString QLottiePrecompLayer::refId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QLottiePrecompLayer5refIdEv(
    const QLottiePrecompLayer *self) {
  return new QString(self->refId());
}

//  QLottiePrecompLayer::~QLottiePrecompLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLottiePrecompLayerD1Ev(QLottiePrecompLayer *self) {
  delete self;
}

//  QLottieBase *QLottiePrecompLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK19QLottiePrecompLayer5cloneEv(
    const QLottiePrecompLayer *self) {
  return self->QLottiePrecompLayer::clone();
}

//  void QLottiePrecompLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLottiePrecompLayer16updatePropertiesEi(
    QLottiePrecompLayer *self,
    int frame) {
  self->QLottiePrecompLayer::updateProperties(frame);
}

//  int QLottiePrecompLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN19QLottiePrecompLayer5parseERK11QJsonObject(
    QLottiePrecompLayer *self,
    const QJsonObject *definition) {
  return self->QLottiePrecompLayer::parse(*definition);
}
