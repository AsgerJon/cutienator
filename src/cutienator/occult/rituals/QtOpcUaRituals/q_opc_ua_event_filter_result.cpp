//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaeventfilterresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaeventfilterresult.h>
#include <QtOpcUa/qopcuacontentfilterelementresult.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  QOpcUaEventFilterResult::QOpcUaEventFilterResult()
extern "C" Q_DECL_EXPORT
QOpcUaEventFilterResult *ritual_ZN23QOpcUaEventFilterResultC1Ev() {
  return new QOpcUaEventFilterResult();
}

//  QOpcUaEventFilterResult::QOpcUaEventFilterResult(const
//      QOpcUaEventFilterResult &a0)
extern "C" Q_DECL_EXPORT
QOpcUaEventFilterResult *ritual_ZN23QOpcUaEventFilterResultC1ERKS_(
    const QOpcUaEventFilterResult *a0) {
  return new QOpcUaEventFilterResult(*a0);
}

//  QOpcUaEventFilterResult &QOpcUaEventFilterResult::operator=(const
//      QOpcUaEventFilterResult &a0)
extern "C" Q_DECL_EXPORT
QOpcUaEventFilterResult *ritual_ZN23QOpcUaEventFilterResultaSERKS_(
    QOpcUaEventFilterResult *self,
    const QOpcUaEventFilterResult *a0) {
  return &(self->operator=(*a0));
}

//  QOpcUaEventFilterResult::~QOpcUaEventFilterResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpcUaEventFilterResultD1Ev(QOpcUaEventFilterResult *self) {
  delete self;
}

//  bool QOpcUaEventFilterResult::isGood() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QOpcUaEventFilterResult6isGoodEv(
    const QOpcUaEventFilterResult *self) {
  return self->isGood();
}

//  QList<QOpcUa::UaStatusCode>
//      QOpcUaEventFilterResult::selectClauseResults() const
extern "C" Q_DECL_EXPORT
QList<QOpcUa::UaStatusCode> *ritual_ZNK23QOpcUaEventFilterResult19selectClauseResultsEv(
    const QOpcUaEventFilterResult *self) {
  return new QList<QOpcUa::UaStatusCode>(self->selectClauseResults());
}

//  QList<QOpcUa::UaStatusCode>
//      &QOpcUaEventFilterResult::selectClauseResultsRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUa::UaStatusCode> *ritual_ZN23QOpcUaEventFilterResult22selectClauseResultsRefEv(
    QOpcUaEventFilterResult *self) {
  return &(self->selectClauseResultsRef());
}

//  void QOpcUaEventFilterResult::setSelectClauseResults(const
//      QList<QOpcUa::UaStatusCode> &selectClausesResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpcUaEventFilterResult22setSelectClauseResultsERK5QListIN6QOpcUa12UaStatusCodeEE(
    QOpcUaEventFilterResult *self,
    const QList<QOpcUa::UaStatusCode> *selectClausesResult) {
  self->setSelectClauseResults(*selectClausesResult);
}

//  QList<QOpcUaContentFilterElementResult>
//      QOpcUaEventFilterResult::whereClauseResults() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElementResult> *ritual_ZNK23QOpcUaEventFilterResult18whereClauseResultsEv(
    const QOpcUaEventFilterResult *self) {
  return new QList<QOpcUaContentFilterElementResult>(
      self->whereClauseResults());
}

//  QList<QOpcUaContentFilterElementResult>
//      &QOpcUaEventFilterResult::whereClauseResultsRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElementResult> *ritual_ZN23QOpcUaEventFilterResult21whereClauseResultsRefEv(
    QOpcUaEventFilterResult *self) {
  return &(self->whereClauseResultsRef());
}

//  void QOpcUaEventFilterResult::setWhereClauseResults(const
//      QList<QOpcUaContentFilterElementResult> &whereClauseResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpcUaEventFilterResult21setWhereClauseResultsERK5QListI32QOpcUaContentFilterElementResultE(
    QOpcUaEventFilterResult *self,
    const QList<QOpcUaContentFilterElementResult> *whereClauseResult) {
  self->setWhereClauseResults(*whereClauseResult);
}

//  a QList<QOpcUa::UaStatusCode> a ritual of QOpcUaEventFilterResult gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaEventFilterResult__QList_QOpcUa_UaStatusCode(
    QList<QOpcUa::UaStatusCode> *self) {
  delete self;
}
