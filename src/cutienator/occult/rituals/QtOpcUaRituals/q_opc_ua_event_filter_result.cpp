//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaeventfilterresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaeventfilterresult.h>
#include <QtOpcUa/qopcuacontentfilterelementresult.h>
#include <QtCore/qlist.h>

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

//  QList<QOpcUaContentFilterElementResult>
//      QOpcUaEventFilterResult::whereClauseResults() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElementResult> *ritual_ZNK23QOpcUaEventFilterResult18whereClauseResultsEv(
    const QOpcUaEventFilterResult *self) {
  return new QList<QOpcUaContentFilterElementResult>(
      self->whereClauseResults());
}

//  void QOpcUaEventFilterResult::setWhereClauseResults(const
//      QList<QOpcUaContentFilterElementResult> &whereClauseResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpcUaEventFilterResult21setWhereClauseResultsERK5QListI32QOpcUaContentFilterElementResultE(
    QOpcUaEventFilterResult *self,
    const QList<QOpcUaContentFilterElementResult> *whereClauseResult) {
  self->setWhereClauseResults(*whereClauseResult);
}
