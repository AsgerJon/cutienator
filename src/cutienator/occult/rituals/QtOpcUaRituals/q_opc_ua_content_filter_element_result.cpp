//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuacontentfilterelementresult.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtOpcUa/qopcuacontentfilterelementresult.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  QOpcUaContentFilterElementResult::QOpcUaContentFilterElementResult()
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElementResult *ritual_ZN32QOpcUaContentFilterElementResultC1Ev() {
  return new QOpcUaContentFilterElementResult();
}

//  QOpcUaContentFilterElementResult::QOpcUaContentFilterElementResult(const
//      QOpcUaContentFilterElementResult &a0)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElementResult *ritual_ZN32QOpcUaContentFilterElementResultC1ERKS_(
    const QOpcUaContentFilterElementResult *a0) {
  return new QOpcUaContentFilterElementResult(*a0);
}

//  QOpcUaContentFilterElementResult
//      &QOpcUaContentFilterElementResult::operator=(const
//      QOpcUaContentFilterElementResult &a0)
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElementResult *ritual_ZN32QOpcUaContentFilterElementResultaSERKS_(
    QOpcUaContentFilterElementResult *self,
    const QOpcUaContentFilterElementResult *a0) {
  return &(self->operator=(*a0));
}

//  QOpcUaContentFilterElementResult::~QOpcUaContentFilterElementResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpcUaContentFilterElementResultD1Ev(
    QOpcUaContentFilterElementResult *self) {
  delete self;
}

//  QOpcUa::UaStatusCode QOpcUaContentFilterElementResult::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK32QOpcUaContentFilterElementResult10statusCodeEv(
    const QOpcUaContentFilterElementResult *self) {
  return self->statusCode();
}

//  void QOpcUaContentFilterElementResult::setStatusCode(QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpcUaContentFilterElementResult13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaContentFilterElementResult *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QList<QOpcUa::UaStatusCode>
//      QOpcUaContentFilterElementResult::operandStatusCodes() const
extern "C" Q_DECL_EXPORT
QList<QOpcUa::UaStatusCode> *ritual_ZNK32QOpcUaContentFilterElementResult18operandStatusCodesEv(
    const QOpcUaContentFilterElementResult *self) {
  return new QList<QOpcUa::UaStatusCode>(self->operandStatusCodes());
}

//  QList<QOpcUa::UaStatusCode>
//      &QOpcUaContentFilterElementResult::operandStatusCodesRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUa::UaStatusCode> *ritual_ZN32QOpcUaContentFilterElementResult21operandStatusCodesRefEv(
    QOpcUaContentFilterElementResult *self) {
  return &(self->operandStatusCodesRef());
}

//  void QOpcUaContentFilterElementResult::setOperandStatusCodes(const
//      QList<QOpcUa::UaStatusCode> &operandStatusCodes)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpcUaContentFilterElementResult21setOperandStatusCodesERK5QListIN6QOpcUa12UaStatusCodeEE(
    QOpcUaContentFilterElementResult *self,
    const QList<QOpcUa::UaStatusCode> *operandStatusCodes) {
  self->setOperandStatusCodes(*operandStatusCodes);
}

//  QList<QOpcUaContentFilterElementResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaContentFilterElementResult> *ritual_list_make_QOpcUaContentFilterElementResult() {
  return new QList<QOpcUaContentFilterElementResult>();
}

//  void QList<QOpcUaContentFilterElementResult>::append(const
//      QOpcUaContentFilterElementResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaContentFilterElementResult(
    QList<QOpcUaContentFilterElementResult> *self,
    const QOpcUaContentFilterElementResult *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaContentFilterElementResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaContentFilterElementResult(
    const QList<QOpcUaContentFilterElementResult> *self) {
  return self->size();
}

//  const QOpcUaContentFilterElementResult
//      &QList<QOpcUaContentFilterElementResult>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaContentFilterElementResult *ritual_list_at_QOpcUaContentFilterElementResult(
    const QList<QOpcUaContentFilterElementResult> *self,
    long long index) {
  return new QOpcUaContentFilterElementResult(self->at(index));
}

//  QList<QOpcUaContentFilterElementResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaContentFilterElementResult(
    QList<QOpcUaContentFilterElementResult> *self) {
  delete self;
}

//  a QList<QOpcUa::UaStatusCode> a ritual of
//      QOpcUaContentFilterElementResult gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaContentFilterElementResult__QList_QOpcUa_UaStatusCode(
    QList<QOpcUa::UaStatusCode> *self) {
  delete self;
}
