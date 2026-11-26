//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  void Qt3DCore::Quick::QQuick3DColorValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType20qt_qmlMarker_foreignEv(
    Qt3DCore::Quick::QQuick3DColorValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType21qt_qmlMarker_extendedEv(
    Qt3DCore::Quick::QQuick3DColorValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant Qt3DCore::Quick::QQuick3DColorValueType::create(const QJSValue
//      &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(
      Qt3DCore::Quick::QQuick3DColorValueType::create(
          *params));
}

//  QString Qt3DCore::Quick::QQuick3DColorValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType8toStringEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return new QString(self->toString());
}

//  QVariant Qt3DCore::Quick::QQuick3DColorValueType::alpha(qreal value)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType5alphaEd(
    const Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal value) {
  return new QVariant(self->alpha(value));
}

//  QVariant Qt3DCore::Quick::QQuick3DColorValueType::lighter(qreal factor)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType7lighterEd(
    const Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal factor) {
  return new QVariant(self->lighter(factor));
}

//  QVariant Qt3DCore::Quick::QQuick3DColorValueType::darker(qreal factor)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6darkerEd(
    const Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal factor) {
  return new QVariant(self->darker(factor));
}

//  QVariant Qt3DCore::Quick::QQuick3DColorValueType::tint(QVariant factor)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType4tintE8QVariant(
    const Qt3DCore::Quick::QQuick3DColorValueType *self,
    const QVariant *factor) {
  return new QVariant(self->tint(*factor));
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::r() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1rEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->r();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::g() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1gEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->g();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::b() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1bEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->b();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::a() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1aEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->a();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvHue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6hsvHueEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hsvHue();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType13hsvSaturationEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hsvSaturation();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType8hsvValueEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hsvValue();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslHue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6hslHueEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hslHue();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType13hslSaturationEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hslSaturation();
}

//  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslLightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType12hslLightnessEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->hslLightness();
}

//  bool Qt3DCore::Quick::QQuick3DColorValueType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType7isValidEv(
    const Qt3DCore::Quick::QQuick3DColorValueType *self) {
  return self->isValid();
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setR(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setREd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setR(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setG(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setGEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setG(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setB(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setBEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setB(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setA(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setAEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setA(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvHue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType9setHsvHueEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHsvHue(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvSaturation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType16setHsvSaturationEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHsvSaturation(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvValue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType11setHsvValueEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHsvValue(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHslHue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType9setHslHueEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHslHue(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHslSaturation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType16setHslSaturationEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHslSaturation(a0);
}

//  void Qt3DCore::Quick::QQuick3DColorValueType::setHslLightness(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType15setHslLightnessEd(
    Qt3DCore::Quick::QQuick3DColorValueType *self,
    qreal a0) {
  self->setHslLightness(a0);
}

//  Qt3DCore::Quick::QQuick3DColorValueType::~QQuick3DColorValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueTypeD1Ev(
    Qt3DCore::Quick::QQuick3DColorValueType *self) {
  delete self;
}
