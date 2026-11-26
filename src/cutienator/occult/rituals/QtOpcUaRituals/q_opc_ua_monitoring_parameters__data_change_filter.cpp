//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuamonitoringparameters.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtCore/qvariant.h>

//  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter()
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter *ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1Ev() {
  return new QOpcUaMonitoringParameters::DataChangeFilter();
}

//  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(const
//      DataChangeFilter &a0)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter *ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1ERKS0_(
    const QOpcUaMonitoringParameters::DataChangeFilter *a0) {
  return new QOpcUaMonitoringParameters::DataChangeFilter(*a0);
}

//  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(DataChange
//      Trigger trigger, DeadbandType deadbandType, double deadbandValue)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter *ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1ENS0_17DataChangeTriggerENS0_12DeadbandTypeEd(
    QOpcUaMonitoringParameters::DataChangeFilter::DataChangeTrigger trigger,
    QOpcUaMonitoringParameters::DataChangeFilter::DeadbandType deadbandType,
    double deadbandValue) {
  return new QOpcUaMonitoringParameters::DataChangeFilter(
      trigger,
      deadbandType,
      deadbandValue);
}

//  DataChangeFilter
//      &QOpcUaMonitoringParameters::DataChangeFilter::operator=(const
//      DataChangeFilter &a0)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter *ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilteraSERKS0_(
    QOpcUaMonitoringParameters::DataChangeFilter *self,
    const QOpcUaMonitoringParameters::DataChangeFilter *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaMonitoringParameters::DataChangeFilter::operator==(const
//      DataChangeFilter &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFiltereqERKS0_(
    const QOpcUaMonitoringParameters::DataChangeFilter *self,
    const QOpcUaMonitoringParameters::DataChangeFilter *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaMonitoringParameters::DataChangeFilter::operator
//      QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFiltercv8QVariantEv(
    const QOpcUaMonitoringParameters::DataChangeFilter *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaMonitoringParameters::DataChangeFilter::~DataChangeFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterD1Ev(
    QOpcUaMonitoringParameters::DataChangeFilter *self) {
  delete self;
}

//  DataChangeTrigger QOpcUaMonitoringParameters::DataChangeFilter::trigger()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter::DataChangeTrigger ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter7triggerEv(
    const QOpcUaMonitoringParameters::DataChangeFilter *self) {
  return self->trigger();
}

//  void QOpcUaMonitoringParameters::DataChangeFilter::setTrigger(DataChangeT
//      rigger trigger)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter10setTriggerENS0_17DataChangeTriggerE(
    QOpcUaMonitoringParameters::DataChangeFilter *self,
    QOpcUaMonitoringParameters::DataChangeFilter::DataChangeTrigger trigger) {
  self->setTrigger(trigger);
}

//  DeadbandType QOpcUaMonitoringParameters::DataChangeFilter::deadbandType()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::DataChangeFilter::DeadbandType ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter12deadbandTypeEv(
    const QOpcUaMonitoringParameters::DataChangeFilter *self) {
  return self->deadbandType();
}

//  void QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandType(Deadba
//      ndType deadbandType)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter15setDeadbandTypeENS0_12DeadbandTypeE(
    QOpcUaMonitoringParameters::DataChangeFilter *self,
    QOpcUaMonitoringParameters::DataChangeFilter::DeadbandType deadbandType) {
  self->setDeadbandType(deadbandType);
}

//  double QOpcUaMonitoringParameters::DataChangeFilter::deadbandValue()
//      const
extern "C" Q_DECL_EXPORT
double ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter13deadbandValueEv(
    const QOpcUaMonitoringParameters::DataChangeFilter *self) {
  return self->deadbandValue();
}

//  void
//      QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandValue(double
//      deadbandValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter16setDeadbandValueEd(
    QOpcUaMonitoringParameters::DataChangeFilter *self,
    double deadbandValue) {
  self->setDeadbandValue(deadbandValue);
}
