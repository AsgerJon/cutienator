//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qcolor.h>

//  QLottieSolidLayer::QLottieSolidLayer()
extern "C" Q_DECL_EXPORT
QLottieSolidLayer *ritual_ZN17QLottieSolidLayerC1Ev() {
  return new QLottieSolidLayer();
}

//  QLottieSolidLayer::QLottieSolidLayer(const QLottieSolidLayer &other)
extern "C" Q_DECL_EXPORT
QLottieSolidLayer *ritual_ZN17QLottieSolidLayerC1ERKS_(
    const QLottieSolidLayer *other) {
  return new QLottieSolidLayer(*other);
}

//  QLottieBase *QLottieSolidLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK17QLottieSolidLayer5cloneEv(
    const QLottieSolidLayer *self) {
  return self->clone();
}

//  int QLottieSolidLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QLottieSolidLayer5parseERK11QJsonObject(
    QLottieSolidLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QColor QLottieSolidLayer::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QLottieSolidLayer5colorEv(
    const QLottieSolidLayer *self) {
  return new QColor(self->color());
}

//  QLottieSolidLayer::~QLottieSolidLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieSolidLayerD1Ev(QLottieSolidLayer *self) {
  delete self;
}

//  QLottieBase *QLottieSolidLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK17QLottieSolidLayer5cloneEv(
    const QLottieSolidLayer *self) {
  return self->QLottieSolidLayer::clone();
}

//  int QLottieSolidLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QLottieSolidLayer5parseERK11QJsonObject(
    QLottieSolidLayer *self,
    const QJsonObject *definition) {
  return self->QLottieSolidLayer::parse(*definition);
}
