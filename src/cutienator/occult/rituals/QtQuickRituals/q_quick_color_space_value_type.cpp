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

//  void QQuickColorSpaceValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType22qt_qmlMarker_anonymousEv(
    QQuickColorSpaceValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQuickColorSpaceValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType20qt_qmlMarker_foreignEv(
    QQuickColorSpaceValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickColorSpaceValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType21qt_qmlMarker_extendedEv(
    QQuickColorSpaceValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickColorSpaceValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN25QQuickColorSpaceValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickColorSpaceValueType::create(*params));
}

//  QQuickColorSpaceEnums::NamedColorSpace
//      QQuickColorSpaceValueType::namedColorSpace() const
extern "C" Q_DECL_EXPORT
QQuickColorSpaceEnums::NamedColorSpace ritual_ZNK25QQuickColorSpaceValueType15namedColorSpaceEv(
    const QQuickColorSpaceValueType *self) {
  return self->namedColorSpace();
}

//  void QQuickColorSpaceValueType::setNamedColorSpace(QQuickColorSpaceEnums:
//      :NamedColorSpace namedColorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType18setNamedColorSpaceEN21QQuickColorSpaceEnums15NamedColorSpaceE(
    QQuickColorSpaceValueType *self,
    QQuickColorSpaceEnums::NamedColorSpace namedColorSpace) {
  self->setNamedColorSpace(namedColorSpace);
}

//  QQuickColorSpaceEnums::Primaries QQuickColorSpaceValueType::primaries()
//      const
extern "C" Q_DECL_EXPORT
QQuickColorSpaceEnums::Primaries ritual_ZNK25QQuickColorSpaceValueType9primariesEv(
    const QQuickColorSpaceValueType *self) {
  return self->primaries();
}

//  void
//      QQuickColorSpaceValueType::setPrimaries(QQuickColorSpaceEnums::Primar
//      ies primariesId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType12setPrimariesEN21QQuickColorSpaceEnums9PrimariesE(
    QQuickColorSpaceValueType *self,
    QQuickColorSpaceEnums::Primaries primariesId) {
  self->setPrimaries(primariesId);
}

//  QQuickColorSpaceEnums::TransferFunction
//      QQuickColorSpaceValueType::transferFunction() const
extern "C" Q_DECL_EXPORT
QQuickColorSpaceEnums::TransferFunction ritual_ZNK25QQuickColorSpaceValueType16transferFunctionEv(
    const QQuickColorSpaceValueType *self) {
  return self->transferFunction();
}

//  void QQuickColorSpaceValueType::setTransferFunction(QQuickColorSpaceEnums
//      ::TransferFunction transferFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType19setTransferFunctionEN21QQuickColorSpaceEnums16TransferFunctionE(
    QQuickColorSpaceValueType *self,
    QQuickColorSpaceEnums::TransferFunction transferFunction) {
  self->setTransferFunction(transferFunction);
}

//  float QQuickColorSpaceValueType::gamma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QQuickColorSpaceValueType5gammaEv(
    const QQuickColorSpaceValueType *self) {
  return self->gamma();
}

//  void QQuickColorSpaceValueType::setGamma(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueType8setGammaEf(
    QQuickColorSpaceValueType *self,
    float gamma) {
  self->setGamma(gamma);
}

//  QQuickColorSpaceValueType::~QQuickColorSpaceValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickColorSpaceValueTypeD1Ev(
    QQuickColorSpaceValueType *self) {
  delete self;
}
