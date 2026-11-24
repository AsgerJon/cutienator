//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaaxisinformation.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaaxisinformation.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuaeuinformation.h>
#include <QtOpcUa/qopcuarange.h>
#include <QtOpcUa/qopcualocalizedtext.h>

//  QOpcUaAxisInformation::QOpcUaAxisInformation()
extern "C" Q_DECL_EXPORT
QOpcUaAxisInformation *ritual_ZN21QOpcUaAxisInformationC1Ev() {
  return new QOpcUaAxisInformation();
}

//  QOpcUaAxisInformation::QOpcUaAxisInformation(const QOpcUaAxisInformation
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAxisInformation *ritual_ZN21QOpcUaAxisInformationC1ERKS_(
    const QOpcUaAxisInformation *a0) {
  return new QOpcUaAxisInformation(*a0);
}

//  bool QOpcUaAxisInformation::operator==(const QOpcUaAxisInformation &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpcUaAxisInformationeqERKS_(
    const QOpcUaAxisInformation *self,
    const QOpcUaAxisInformation *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaAxisInformation::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QOpcUaAxisInformationcv8QVariantEv(
    const QOpcUaAxisInformation *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaAxisInformation::~QOpcUaAxisInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformationD1Ev(QOpcUaAxisInformation *self) {
  delete self;
}

//  QOpcUaEUInformation QOpcUaAxisInformation::engineeringUnits() const
extern "C" Q_DECL_EXPORT
QOpcUaEUInformation *ritual_ZNK21QOpcUaAxisInformation16engineeringUnitsEv(
    const QOpcUaAxisInformation *self) {
  return new QOpcUaEUInformation(self->engineeringUnits());
}

//  void QOpcUaAxisInformation::setEngineeringUnits(const QOpcUaEUInformation
//      &engineeringUnits)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformation19setEngineeringUnitsERK19QOpcUaEUInformation(
    QOpcUaAxisInformation *self,
    const QOpcUaEUInformation *engineeringUnits) {
  self->setEngineeringUnits(*engineeringUnits);
}

//  QOpcUaRange QOpcUaAxisInformation::eURange() const
extern "C" Q_DECL_EXPORT
QOpcUaRange *ritual_ZNK21QOpcUaAxisInformation7eURangeEv(
    const QOpcUaAxisInformation *self) {
  return new QOpcUaRange(self->eURange());
}

//  void QOpcUaAxisInformation::setEURange(const QOpcUaRange &eURange)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformation10setEURangeERK11QOpcUaRange(
    QOpcUaAxisInformation *self,
    const QOpcUaRange *eURange) {
  self->setEURange(*eURange);
}

//  QOpcUaLocalizedText QOpcUaAxisInformation::title() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK21QOpcUaAxisInformation5titleEv(
    const QOpcUaAxisInformation *self) {
  return new QOpcUaLocalizedText(self->title());
}

//  void QOpcUaAxisInformation::setTitle(const QOpcUaLocalizedText &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformation8setTitleERK19QOpcUaLocalizedText(
    QOpcUaAxisInformation *self,
    const QOpcUaLocalizedText *title) {
  self->setTitle(*title);
}

//  QOpcUa::AxisScale QOpcUaAxisInformation::axisScaleType() const
extern "C" Q_DECL_EXPORT
QOpcUa::AxisScale ritual_ZNK21QOpcUaAxisInformation13axisScaleTypeEv(
    const QOpcUaAxisInformation *self) {
  return self->axisScaleType();
}

//  void QOpcUaAxisInformation::setAxisScaleType(QOpcUa::AxisScale
//      axisScaleType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformation16setAxisScaleTypeEN6QOpcUa9AxisScaleE(
    QOpcUaAxisInformation *self,
    QOpcUa::AxisScale axisScaleType) {
  self->setAxisScaleType(axisScaleType);
}
