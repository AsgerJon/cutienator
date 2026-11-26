//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuareadresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuareadresult.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOpcUaReadResult::QOpcUaReadResult()
extern "C" Q_DECL_EXPORT
QOpcUaReadResult *ritual_ZN16QOpcUaReadResultC1Ev() {
  return new QOpcUaReadResult();
}

//  QOpcUaReadResult::QOpcUaReadResult(const QOpcUaReadResult &other)
extern "C" Q_DECL_EXPORT
QOpcUaReadResult *ritual_ZN16QOpcUaReadResultC1ERKS_(
    const QOpcUaReadResult *other) {
  return new QOpcUaReadResult(*other);
}

//  QOpcUaReadResult &QOpcUaReadResult::operator=(const QOpcUaReadResult
//      &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaReadResult *ritual_ZN16QOpcUaReadResultaSERKS_(
    QOpcUaReadResult *self,
    const QOpcUaReadResult *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaReadResult::~QOpcUaReadResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResultD1Ev(QOpcUaReadResult *self) {
  delete self;
}

//  QDateTime QOpcUaReadResult::serverTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QOpcUaReadResult15serverTimestampEv(
    const QOpcUaReadResult *self) {
  return new QDateTime(self->serverTimestamp());
}

//  void QOpcUaReadResult::setServerTimestamp(const QDateTime
//      &serverTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult18setServerTimestampERK9QDateTime(
    QOpcUaReadResult *self,
    const QDateTime *serverTimestamp) {
  self->setServerTimestamp(*serverTimestamp);
}

//  QDateTime QOpcUaReadResult::sourceTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QOpcUaReadResult15sourceTimestampEv(
    const QOpcUaReadResult *self) {
  return new QDateTime(self->sourceTimestamp());
}

//  void QOpcUaReadResult::setSourceTimestamp(const QDateTime
//      &sourceTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult18setSourceTimestampERK9QDateTime(
    QOpcUaReadResult *self,
    const QDateTime *sourceTimestamp) {
  self->setSourceTimestamp(*sourceTimestamp);
}

//  QOpcUa::UaStatusCode QOpcUaReadResult::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK16QOpcUaReadResult10statusCodeEv(
    const QOpcUaReadResult *self) {
  return self->statusCode();
}

//  void QOpcUaReadResult::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaReadResult *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QString QOpcUaReadResult::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QOpcUaReadResult6nodeIdEv(
    const QOpcUaReadResult *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaReadResult::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult9setNodeIdERK7QString(
    QOpcUaReadResult *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QOpcUa::NodeAttribute QOpcUaReadResult::attribute() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK16QOpcUaReadResult9attributeEv(
    const QOpcUaReadResult *self) {
  return self->attribute();
}

//  void QOpcUaReadResult::setAttribute(QOpcUa::NodeAttribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult12setAttributeEN6QOpcUa13NodeAttributeE(
    QOpcUaReadResult *self,
    QOpcUa::NodeAttribute attribute) {
  self->setAttribute(attribute);
}

//  QString QOpcUaReadResult::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QOpcUaReadResult10indexRangeEv(
    const QOpcUaReadResult *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaReadResult::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult13setIndexRangeERK7QString(
    QOpcUaReadResult *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  QVariant QOpcUaReadResult::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QOpcUaReadResult5valueEv(
    const QOpcUaReadResult *self) {
  return new QVariant(self->value());
}

//  void QOpcUaReadResult::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaReadResult8setValueERK8QVariant(
    QOpcUaReadResult *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QList<QOpcUaReadResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaReadResult> *ritual_list_make_QOpcUaReadResult() {
  return new QList<QOpcUaReadResult>();
}

//  void QList<QOpcUaReadResult>::append(const QOpcUaReadResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaReadResult(
    QList<QOpcUaReadResult> *self,
    const QOpcUaReadResult *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaReadResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaReadResult(
    const QList<QOpcUaReadResult> *self) {
  return self->size();
}

//  const QOpcUaReadResult &QList<QOpcUaReadResult>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaReadResult *ritual_list_at_QOpcUaReadResult(
    const QList<QOpcUaReadResult> *self,
    long long index) {
  return new QOpcUaReadResult(self->at(index));
}

//  QList<QOpcUaReadResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaReadResult(QList<QOpcUaReadResult> *self) {
  delete self;
}
