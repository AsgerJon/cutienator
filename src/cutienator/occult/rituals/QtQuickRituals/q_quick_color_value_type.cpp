//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstring.h>

//  void QQuickColorValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType20qt_qmlMarker_foreignEv(
    QQuickColorValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickColorValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType21qt_qmlMarker_extendedEv(
    QQuickColorValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickColorValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QQuickColorValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickColorValueType::create(*params));
}

//  QQuickColorValueType::QQuickColorValueType()
extern "C" Q_DECL_EXPORT
QQuickColorValueType *ritual_ZN20QQuickColorValueTypeC1Ev() {
  return new QQuickColorValueType();
}

//  QQuickColorValueType::QQuickColorValueType(const QColor &color)
extern "C" Q_DECL_EXPORT
QQuickColorValueType *ritual_ZN20QQuickColorValueTypeC1ERK6QColor(
    const QColor *color) {
  return new QQuickColorValueType(*color);
}

//  QQuickColorValueType::QQuickColorValueType(const QString &string)
extern "C" Q_DECL_EXPORT
QQuickColorValueType *ritual_ZN20QQuickColorValueTypeC1ERK7QString(
    const QString *string) {
  return new QQuickColorValueType(*string);
}

//  QString QQuickColorValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickColorValueType8toStringEv(
    const QQuickColorValueType *self) {
  return new QString(self->toString());
}

//  QColor QQuickColorValueType::alpha(qreal value) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorValueType5alphaEd(
    const QQuickColorValueType *self,
    qreal value) {
  return new QColor(self->alpha(value));
}

//  QColor QQuickColorValueType::lighter(qreal factor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorValueType7lighterEd(
    const QQuickColorValueType *self,
    qreal factor) {
  return new QColor(self->lighter(factor));
}

//  QColor QQuickColorValueType::darker(qreal factor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorValueType6darkerEd(
    const QQuickColorValueType *self,
    qreal factor) {
  return new QColor(self->darker(factor));
}

//  QColor QQuickColorValueType::tint(const QColor &tintColor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorValueType4tintERK6QColor(
    const QQuickColorValueType *self,
    const QColor *tintColor) {
  return new QColor(self->tint(*tintColor));
}

//  qreal QQuickColorValueType::r() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType1rEv(
    const QQuickColorValueType *self) {
  return self->r();
}

//  qreal QQuickColorValueType::g() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType1gEv(
    const QQuickColorValueType *self) {
  return self->g();
}

//  qreal QQuickColorValueType::b() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType1bEv(
    const QQuickColorValueType *self) {
  return self->b();
}

//  qreal QQuickColorValueType::a() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType1aEv(
    const QQuickColorValueType *self) {
  return self->a();
}

//  qreal QQuickColorValueType::hsvHue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType6hsvHueEv(
    const QQuickColorValueType *self) {
  return self->hsvHue();
}

//  qreal QQuickColorValueType::hsvSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType13hsvSaturationEv(
    const QQuickColorValueType *self) {
  return self->hsvSaturation();
}

//  qreal QQuickColorValueType::hsvValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType8hsvValueEv(
    const QQuickColorValueType *self) {
  return self->hsvValue();
}

//  qreal QQuickColorValueType::hslHue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType6hslHueEv(
    const QQuickColorValueType *self) {
  return self->hslHue();
}

//  qreal QQuickColorValueType::hslSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType13hslSaturationEv(
    const QQuickColorValueType *self) {
  return self->hslSaturation();
}

//  qreal QQuickColorValueType::hslLightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickColorValueType12hslLightnessEv(
    const QQuickColorValueType *self) {
  return self->hslLightness();
}

//  bool QQuickColorValueType::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickColorValueType7isValidEv(
    const QQuickColorValueType *self) {
  return self->isValid();
}

//  int QQuickColorValueType::rgba() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickColorValueType4rgbaEv(
    const QQuickColorValueType *self) {
  return self->rgba();
}

//  void QQuickColorValueType::setR(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType4setREd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setR(a0);
}

//  void QQuickColorValueType::setG(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType4setGEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setG(a0);
}

//  void QQuickColorValueType::setB(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType4setBEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setB(a0);
}

//  void QQuickColorValueType::setA(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType4setAEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setA(a0);
}

//  void QQuickColorValueType::setHsvHue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType9setHsvHueEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHsvHue(a0);
}

//  void QQuickColorValueType::setHsvSaturation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType16setHsvSaturationEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHsvSaturation(a0);
}

//  void QQuickColorValueType::setHsvValue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType11setHsvValueEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHsvValue(a0);
}

//  void QQuickColorValueType::setHslHue(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType9setHslHueEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHslHue(a0);
}

//  void QQuickColorValueType::setHslSaturation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType16setHslSaturationEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHslSaturation(a0);
}

//  void QQuickColorValueType::setHslLightness(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueType15setHslLightnessEd(
    QQuickColorValueType *self,
    qreal a0) {
  self->setHslLightness(a0);
}

//  QQuickColorValueType::~QQuickColorValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorValueTypeD1Ev(QQuickColorValueType *self) {
  delete self;
}
