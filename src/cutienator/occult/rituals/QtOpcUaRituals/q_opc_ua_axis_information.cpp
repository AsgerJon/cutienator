//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaaxisinformation.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaaxisinformation.h>
#include <QtOpcUa/qopcuaeuinformation.h>
#include <QtOpcUa/qopcuarange.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qvariant.h>
#include <QtCore/QList>

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

//  QOpcUaAxisInformation::QOpcUaAxisInformation(const QOpcUaEUInformation
//      &engineeringUnits, const QOpcUaRange &eURange, const
//      QOpcUaLocalizedText &title, const QOpcUa::AxisScale &axisScaleType,
//      const QList<double> &axisSteps)
extern "C" Q_DECL_EXPORT
QOpcUaAxisInformation *ritual_ZN21QOpcUaAxisInformationC1ERK19QOpcUaEUInformationRK11QOpcUaRangeRK19QOpcUaLocalizedTextRKN6QOpcUa9AxisScaleERK5QListIdE(
    const QOpcUaEUInformation *engineeringUnits,
    const QOpcUaRange *eURange,
    const QOpcUaLocalizedText *title,
    const QOpcUa::AxisScale *axisScaleType,
    const QList<double> *axisSteps) {
  return new QOpcUaAxisInformation(
      *engineeringUnits,
      *eURange,
      *title,
      *axisScaleType,
      *axisSteps);
}

//  QOpcUaAxisInformation &QOpcUaAxisInformation::operator=(const
//      QOpcUaAxisInformation &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAxisInformation *ritual_ZN21QOpcUaAxisInformationaSERKS_(
    QOpcUaAxisInformation *self,
    const QOpcUaAxisInformation *a0) {
  return &(self->operator=(*a0));
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

//  QList<double> QOpcUaAxisInformation::axisSteps() const
extern "C" Q_DECL_EXPORT
QList<double> *ritual_ZNK21QOpcUaAxisInformation9axisStepsEv(
    const QOpcUaAxisInformation *self) {
  return new QList<double>(self->axisSteps());
}

//  void QOpcUaAxisInformation::setAxisSteps(const QList<double> &axisSteps)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaAxisInformation12setAxisStepsERK5QListIdE(
    QOpcUaAxisInformation *self,
    const QList<double> *axisSteps) {
  self->setAxisSteps(*axisSteps);
}

//  QList<double> &QOpcUaAxisInformation::axisStepsRef()
extern "C" Q_DECL_EXPORT
QList<double> *ritual_ZN21QOpcUaAxisInformation12axisStepsRefEv(
    QOpcUaAxisInformation *self) {
  return &(self->axisStepsRef());
}

//  a QList<double> a ritual of QOpcUaAxisInformation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaAxisInformation__QList_double(QList<double> *self) {
  delete self;
}
