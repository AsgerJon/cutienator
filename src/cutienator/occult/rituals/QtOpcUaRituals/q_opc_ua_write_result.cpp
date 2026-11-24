//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuawriteresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuawriteresult.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpcUaWriteResult::QOpcUaWriteResult()
extern "C" Q_DECL_EXPORT
QOpcUaWriteResult *ritual_ZN17QOpcUaWriteResultC1Ev() {
  return new QOpcUaWriteResult();
}

//  QOpcUaWriteResult::QOpcUaWriteResult(const QOpcUaWriteResult &other)
extern "C" Q_DECL_EXPORT
QOpcUaWriteResult *ritual_ZN17QOpcUaWriteResultC1ERKS_(
    const QOpcUaWriteResult *other) {
  return new QOpcUaWriteResult(*other);
}

//  QOpcUaWriteResult::~QOpcUaWriteResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaWriteResultD1Ev(QOpcUaWriteResult *self) {
  delete self;
}

//  QString QOpcUaWriteResult::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QOpcUaWriteResult6nodeIdEv(
    const QOpcUaWriteResult *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaWriteResult::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaWriteResult9setNodeIdERK7QString(
    QOpcUaWriteResult *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QOpcUa::NodeAttribute QOpcUaWriteResult::attribute() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeAttribute ritual_ZNK17QOpcUaWriteResult9attributeEv(
    const QOpcUaWriteResult *self) {
  return self->attribute();
}

//  void QOpcUaWriteResult::setAttribute(QOpcUa::NodeAttribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaWriteResult12setAttributeEN6QOpcUa13NodeAttributeE(
    QOpcUaWriteResult *self,
    QOpcUa::NodeAttribute attribute) {
  self->setAttribute(attribute);
}

//  QString QOpcUaWriteResult::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QOpcUaWriteResult10indexRangeEv(
    const QOpcUaWriteResult *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaWriteResult::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaWriteResult13setIndexRangeERK7QString(
    QOpcUaWriteResult *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}

//  QOpcUa::UaStatusCode QOpcUaWriteResult::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK17QOpcUaWriteResult10statusCodeEv(
    const QOpcUaWriteResult *self) {
  return self->statusCode();
}

//  void QOpcUaWriteResult::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaWriteResult13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaWriteResult *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QList<QOpcUaWriteResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaWriteResult> *ritual_list_make_QOpcUaWriteResult() {
  return new QList<QOpcUaWriteResult>();
}

//  void QList<QOpcUaWriteResult>::append(const QOpcUaWriteResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaWriteResult(
    QList<QOpcUaWriteResult> *self,
    const QOpcUaWriteResult *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaWriteResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaWriteResult(
    const QList<QOpcUaWriteResult> *self) {
  return self->size();
}

//  const QOpcUaWriteResult &QList<QOpcUaWriteResult>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaWriteResult *ritual_list_at_QOpcUaWriteResult(
    const QList<QOpcUaWriteResult> *self,
    long long index) {
  return new QOpcUaWriteResult(self->at(index));
}

//  QList<QOpcUaWriteResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaWriteResult(QList<QOpcUaWriteResult> *self) {
  delete self;
}
