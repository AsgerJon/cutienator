//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuadatavalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuadatavalue.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOpcUaDataValue::QOpcUaDataValue()
extern "C" Q_DECL_EXPORT
QOpcUaDataValue *ritual_ZN15QOpcUaDataValueC1Ev() {
  return new QOpcUaDataValue();
}

//  QOpcUaDataValue::QOpcUaDataValue(const QOpcUaDataValue &other)
extern "C" Q_DECL_EXPORT
QOpcUaDataValue *ritual_ZN15QOpcUaDataValueC1ERKS_(
    const QOpcUaDataValue *other) {
  return new QOpcUaDataValue(*other);
}

//  QOpcUaDataValue &QOpcUaDataValue::operator=(const QOpcUaDataValue &other)
extern "C" Q_DECL_EXPORT
QOpcUaDataValue *ritual_ZN15QOpcUaDataValueaSERKS_(
    QOpcUaDataValue *self,
    const QOpcUaDataValue *other) {
  return &(self->operator=(*other));
}

//  QOpcUaDataValue::~QOpcUaDataValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValueD1Ev(QOpcUaDataValue *self) {
  delete self;
}

//  void QOpcUaDataValue::swap(QOpcUaDataValue &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue4swapERS_(
    QOpcUaDataValue *self,
    QOpcUaDataValue *other) {
  self->swap(*other);
}

//  QDateTime QOpcUaDataValue::serverTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QOpcUaDataValue15serverTimestampEv(
    const QOpcUaDataValue *self) {
  return new QDateTime(self->serverTimestamp());
}

//  void QOpcUaDataValue::setServerTimestamp(const QDateTime
//      &serverTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue18setServerTimestampERK9QDateTime(
    QOpcUaDataValue *self,
    const QDateTime *serverTimestamp) {
  self->setServerTimestamp(*serverTimestamp);
}

//  quint16 QOpcUaDataValue::serverPicoseconds() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QOpcUaDataValue17serverPicosecondsEv(
    const QOpcUaDataValue *self) {
  return self->serverPicoseconds();
}

//  void QOpcUaDataValue::setServerPicoseconds(quint16 serverPicoseconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue20setServerPicosecondsEt(
    QOpcUaDataValue *self,
    quint16 serverPicoseconds) {
  self->setServerPicoseconds(serverPicoseconds);
}

//  QDateTime QOpcUaDataValue::sourceTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QOpcUaDataValue15sourceTimestampEv(
    const QOpcUaDataValue *self) {
  return new QDateTime(self->sourceTimestamp());
}

//  void QOpcUaDataValue::setSourceTimestamp(const QDateTime
//      &sourceTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue18setSourceTimestampERK9QDateTime(
    QOpcUaDataValue *self,
    const QDateTime *sourceTimestamp) {
  self->setSourceTimestamp(*sourceTimestamp);
}

//  quint16 QOpcUaDataValue::sourcePicoseconds() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QOpcUaDataValue17sourcePicosecondsEv(
    const QOpcUaDataValue *self) {
  return self->sourcePicoseconds();
}

//  void QOpcUaDataValue::setSourcePicoseconds(quint16 sourcePicoseconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue20setSourcePicosecondsEt(
    QOpcUaDataValue *self,
    quint16 sourcePicoseconds) {
  self->setSourcePicoseconds(sourcePicoseconds);
}

//  QOpcUa::UaStatusCode QOpcUaDataValue::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK15QOpcUaDataValue10statusCodeEv(
    const QOpcUaDataValue *self) {
  return self->statusCode();
}

//  void QOpcUaDataValue::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaDataValue *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QVariant QOpcUaDataValue::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QOpcUaDataValue5valueEv(const QOpcUaDataValue *self) {
  return new QVariant(self->value());
}

//  void QOpcUaDataValue::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaDataValue8setValueERK8QVariant(
    QOpcUaDataValue *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QVariant QOpcUaDataValue::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QOpcUaDataValuecv8QVariantEv(
    const QOpcUaDataValue *self) {
  return new QVariant(self->operator QVariant());
}

//  bool operator==(const QOpcUaDataValue &lhs, const QOpcUaDataValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QOpcUaDataValueS1_(
    const QOpcUaDataValue *lhs,
    const QOpcUaDataValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaDataValue &lhs, const QOpcUaDataValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QOpcUaDataValueS1_(
    const QOpcUaDataValue *lhs,
    const QOpcUaDataValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaDataValue>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaDataValue> *ritual_list_make_QOpcUaDataValue() {
  return new QList<QOpcUaDataValue>();
}

//  void QList<QOpcUaDataValue>::append(const QOpcUaDataValue &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaDataValue(
    QList<QOpcUaDataValue> *self,
    const QOpcUaDataValue *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaDataValue>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaDataValue(
    const QList<QOpcUaDataValue> *self) {
  return self->size();
}

//  const QOpcUaDataValue &QList<QOpcUaDataValue>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaDataValue *ritual_list_at_QOpcUaDataValue(
    const QList<QOpcUaDataValue> *self,
    long long index) {
  return new QOpcUaDataValue(self->at(index));
}

//  QList<QOpcUaDataValue>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaDataValue(QList<QOpcUaDataValue> *self) {
  delete self;
}
