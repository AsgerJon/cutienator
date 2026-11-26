//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuawriteitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuawriteitem.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>

//  QOpcUaWriteItem::QOpcUaWriteItem()
extern "C" Q_DECL_EXPORT
QOpcUaWriteItem *ritual_ZN15QOpcUaWriteItemC1Ev() {
  return new QOpcUaWriteItem();
}

//  QOpcUaWriteItem::QOpcUaWriteItem(const QOpcUaWriteItem &other)
extern "C" Q_DECL_EXPORT
QOpcUaWriteItem *ritual_ZN15QOpcUaWriteItemC1ERKS_(
    const QOpcUaWriteItem *other) {
  return new QOpcUaWriteItem(*other);
}

//  QOpcUaWriteItem::QOpcUaWriteItem(const QString &nodeId,
//      QOpcUa::NodeAttribute attribute, const QVariant &value, QOpcUa::Types
//      type, const QString &indexRange)
extern "C" Q_DECL_EXPORT
QOpcUaWriteItem *ritual_ZN15QOpcUaWriteItemC1ERK7QStringN6QOpcUa13NodeAttributeERK8QVariantNS3_5TypesES2_(
    const QString *nodeId,
    QOpcUa::NodeAttribute attribute,
    const QVariant *value,
    QOpcUa::Types type,
    const QString *indexRange) {
  return new QOpcUaWriteItem(*nodeId, attribute, *value, type, *indexRange);
}

//  QOpcUaWriteItem &QOpcUaWriteItem::operator=(const QOpcUaWriteItem &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaWriteItem *ritual_ZN15QOpcUaWriteItemaSERKS_(
    QOpcUaWriteItem *self,
    const QOpcUaWriteItem *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaWriteItem::~QOpcUaWriteItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItemD1Ev(QOpcUaWriteItem *self) {
  delete self;
}

//  QString QOpcUaWriteItem::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaWriteItem6nodeIdEv(const QOpcUaWriteItem *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaWriteItem::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem9setNodeIdERK7QString(
    QOpcUaWriteItem *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QOpcUa::NodeAttribute QOpcUaWriteItem::attribute() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK15QOpcUaWriteItem9attributeEv(
    const QOpcUaWriteItem *self) {
  return self->attribute();
}

//  void QOpcUaWriteItem::setAttribute(QOpcUa::NodeAttribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem12setAttributeEN6QOpcUa13NodeAttributeE(
    QOpcUaWriteItem *self,
    QOpcUa::NodeAttribute attribute) {
  self->setAttribute(attribute);
}

//  QString QOpcUaWriteItem::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaWriteItem10indexRangeEv(
    const QOpcUaWriteItem *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaWriteItem::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem13setIndexRangeERK7QString(
    QOpcUaWriteItem *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  QVariant QOpcUaWriteItem::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QOpcUaWriteItem5valueEv(const QOpcUaWriteItem *self) {
  return new QVariant(self->value());
}

//  void QOpcUaWriteItem::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem8setValueERK8QVariant(
    QOpcUaWriteItem *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  void QOpcUaWriteItem::setValue(const QVariant &value, QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem8setValueERK8QVariantN6QOpcUa5TypesE(
    QOpcUaWriteItem *self,
    const QVariant *value,
    QOpcUa::Types type) {
  self->setValue(*value, type);
}

//  QOpcUa::Types QOpcUaWriteItem::type() const
extern "C" Q_DECL_EXPORT
QOpcUa::Types ritual_ZNK15QOpcUaWriteItem4typeEv(
    const QOpcUaWriteItem *self) {
  return self->type();
}

//  void QOpcUaWriteItem::setType(QOpcUa::Types type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem7setTypeEN6QOpcUa5TypesE(
    QOpcUaWriteItem *self,
    QOpcUa::Types type) {
  self->setType(type);
}

//  QDateTime QOpcUaWriteItem::sourceTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QOpcUaWriteItem15sourceTimestampEv(
    const QOpcUaWriteItem *self) {
  return new QDateTime(self->sourceTimestamp());
}

//  void QOpcUaWriteItem::setSourceTimestamp(const QDateTime
//      &sourceTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem18setSourceTimestampERK9QDateTime(
    QOpcUaWriteItem *self,
    const QDateTime *sourceTimestamp) {
  self->setSourceTimestamp(*sourceTimestamp);
}

//  QDateTime QOpcUaWriteItem::serverTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QOpcUaWriteItem15serverTimestampEv(
    const QOpcUaWriteItem *self) {
  return new QDateTime(self->serverTimestamp());
}

//  void QOpcUaWriteItem::setServerTimestamp(const QDateTime
//      &serverTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem18setServerTimestampERK9QDateTime(
    QOpcUaWriteItem *self,
    const QDateTime *serverTimestamp) {
  self->setServerTimestamp(*serverTimestamp);
}

//  QOpcUa::UaStatusCode QOpcUaWriteItem::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK15QOpcUaWriteItem10statusCodeEv(
    const QOpcUaWriteItem *self) {
  return self->statusCode();
}

//  bool QOpcUaWriteItem::hasStatusCode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QOpcUaWriteItem13hasStatusCodeEv(
    const QOpcUaWriteItem *self) {
  return self->hasStatusCode();
}

//  void QOpcUaWriteItem::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaWriteItem13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaWriteItem *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QList<QOpcUaWriteItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaWriteItem> *ritual_list_make_QOpcUaWriteItem() {
  return new QList<QOpcUaWriteItem>();
}

//  void QList<QOpcUaWriteItem>::append(const QOpcUaWriteItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaWriteItem(
    QList<QOpcUaWriteItem> *self,
    const QOpcUaWriteItem *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaWriteItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaWriteItem(
    const QList<QOpcUaWriteItem> *self) {
  return self->size();
}

//  const QOpcUaWriteItem &QList<QOpcUaWriteItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaWriteItem *ritual_list_at_QOpcUaWriteItem(
    const QList<QOpcUaWriteItem> *self,
    long long index) {
  return new QOpcUaWriteItem(self->at(index));
}

//  QList<QOpcUaWriteItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaWriteItem(QList<QOpcUaWriteItem> *self) {
  delete self;
}
