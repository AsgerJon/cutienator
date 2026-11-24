//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuamonitoringparameters.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtOpcUa/qopcuasimpleattributeoperand.h>
#include <QtOpcUa/qopcuacontentfilterelement.h>
#include <QtCore/qlist.h>

//  QOpcUaMonitoringParameters::EventFilter::EventFilter()
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::EventFilter *ritual_ZN26QOpcUaMonitoringParameters11EventFilterC1Ev() {
  return new QOpcUaMonitoringParameters::EventFilter();
}

//  QOpcUaMonitoringParameters::EventFilter::EventFilter(const EventFilter
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::EventFilter *ritual_ZN26QOpcUaMonitoringParameters11EventFilterC1ERKS0_(
    const QOpcUaMonitoringParameters::EventFilter *a0) {
  return new QOpcUaMonitoringParameters::EventFilter(*a0);
}

//  bool QOpcUaMonitoringParameters::EventFilter::operator==(const
//      QOpcUaMonitoringParameters::EventFilter &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaMonitoringParameters11EventFiltereqERKS0_(
    const QOpcUaMonitoringParameters::EventFilter *self,
    const QOpcUaMonitoringParameters::EventFilter *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaMonitoringParameters::EventFilter::~EventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters11EventFilterD1Ev(
    QOpcUaMonitoringParameters::EventFilter *self) {
  delete self;
}

//  QList<QOpcUaSimpleAttributeOperand>
//      QOpcUaMonitoringParameters::EventFilter::selectClauses() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaSimpleAttributeOperand> *ritual_ZNK26QOpcUaMonitoringParameters11EventFilter13selectClausesEv(
    const QOpcUaMonitoringParameters::EventFilter *self) {
  return new QList<QOpcUaSimpleAttributeOperand>(self->selectClauses());
}

//  void QOpcUaMonitoringParameters::EventFilter::setSelectClauses(const
//      QList<QOpcUaSimpleAttributeOperand> &selectClauses)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters11EventFilter16setSelectClausesERK5QListI28QOpcUaSimpleAttributeOperandE(
    QOpcUaMonitoringParameters::EventFilter *self,
    const QList<QOpcUaSimpleAttributeOperand> *selectClauses) {
  self->setSelectClauses(*selectClauses);
}

//  QList<QOpcUaContentFilterElement>
//      QOpcUaMonitoringParameters::EventFilter::whereClause() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElement> *ritual_ZNK26QOpcUaMonitoringParameters11EventFilter11whereClauseEv(
    const QOpcUaMonitoringParameters::EventFilter *self) {
  return new QList<QOpcUaContentFilterElement>(self->whereClause());
}

//  void QOpcUaMonitoringParameters::EventFilter::setWhereClause(const
//      QList<QOpcUaContentFilterElement> &whereClause)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters11EventFilter14setWhereClauseERK5QListI26QOpcUaContentFilterElementE(
    QOpcUaMonitoringParameters::EventFilter *self,
    const QList<QOpcUaContentFilterElement> *whereClause) {
  self->setWhereClause(*whereClause);
}
