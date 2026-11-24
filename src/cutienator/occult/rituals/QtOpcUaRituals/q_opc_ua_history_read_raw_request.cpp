//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuahistoryreadrawrequest.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuahistoryreadrawrequest.h>
#include <QtOpcUa/qopcuareaditem.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>

//  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadRawRequest *ritual_ZN27QOpcUaHistoryReadRawRequestC1Ev() {
  return new QOpcUaHistoryReadRawRequest();
}

//  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
//      QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
//      const QDateTime &endTimestamp, quint32 numValuesPerNode, bool
//      returnBounds)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadRawRequest *ritual_ZN27QOpcUaHistoryReadRawRequestC1ERK5QListI14QOpcUaReadItemERK9QDateTimeS7_jb(
    const QList<QOpcUaReadItem> *nodesToRead,
    const QDateTime *startTimestamp,
    const QDateTime *endTimestamp,
    quint32 numValuesPerNode,
    bool returnBounds) {
  return new QOpcUaHistoryReadRawRequest(
      *nodesToRead,
      *startTimestamp,
      *endTimestamp,
      numValuesPerNode,
      returnBounds);
}

//  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
//      QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
//      const QDateTime &endTimestamp, QOpcUa::TimestampsToReturn
//      timestampsToReturn)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadRawRequest *ritual_ZN27QOpcUaHistoryReadRawRequestC1ERK5QListI14QOpcUaReadItemERK9QDateTimeS7_N6QOpcUa18TimestampsToReturnE(
    const QList<QOpcUaReadItem> *nodesToRead,
    const QDateTime *startTimestamp,
    const QDateTime *endTimestamp,
    QOpcUa::TimestampsToReturn timestampsToReturn) {
  return new QOpcUaHistoryReadRawRequest(
      *nodesToRead,
      *startTimestamp,
      *endTimestamp,
      timestampsToReturn);
}

//  QOpcUaHistoryReadRawRequest::QOpcUaHistoryReadRawRequest(const
//      QOpcUaHistoryReadRawRequest &other)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadRawRequest *ritual_ZN27QOpcUaHistoryReadRawRequestC1ERKS_(
    const QOpcUaHistoryReadRawRequest *other) {
  return new QOpcUaHistoryReadRawRequest(*other);
}

//  QOpcUaHistoryReadRawRequest::~QOpcUaHistoryReadRawRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequestD1Ev(
    QOpcUaHistoryReadRawRequest *self) {
  delete self;
}

//  QDateTime QOpcUaHistoryReadRawRequest::startTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK27QOpcUaHistoryReadRawRequest14startTimestampEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return new QDateTime(self->startTimestamp());
}

//  void QOpcUaHistoryReadRawRequest::setStartTimestamp(const QDateTime
//      &startTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest17setStartTimestampERK9QDateTime(
    QOpcUaHistoryReadRawRequest *self,
    const QDateTime *startTimestamp) {
  self->setStartTimestamp(*startTimestamp);
}

//  QDateTime QOpcUaHistoryReadRawRequest::endTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK27QOpcUaHistoryReadRawRequest12endTimestampEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return new QDateTime(self->endTimestamp());
}

//  void QOpcUaHistoryReadRawRequest::setEndTimestamp(const QDateTime
//      &endTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest15setEndTimestampERK9QDateTime(
    QOpcUaHistoryReadRawRequest *self,
    const QDateTime *endTimestamp) {
  self->setEndTimestamp(*endTimestamp);
}

//  quint32 QOpcUaHistoryReadRawRequest::numValuesPerNode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK27QOpcUaHistoryReadRawRequest16numValuesPerNodeEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return self->numValuesPerNode();
}

//  void QOpcUaHistoryReadRawRequest::setNumValuesPerNode(quint32
//      numValuesPerNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest19setNumValuesPerNodeEj(
    QOpcUaHistoryReadRawRequest *self,
    quint32 numValuesPerNode) {
  self->setNumValuesPerNode(numValuesPerNode);
}

//  bool QOpcUaHistoryReadRawRequest::returnBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaHistoryReadRawRequest12returnBoundsEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return self->returnBounds();
}

//  void QOpcUaHistoryReadRawRequest::setReturnBounds(bool returnBounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest15setReturnBoundsEb(
    QOpcUaHistoryReadRawRequest *self,
    bool returnBounds) {
  self->setReturnBounds(returnBounds);
}

//  QOpcUa::TimestampsToReturn
//      QOpcUaHistoryReadRawRequest::timestampsToReturn() const
extern "C" Q_DECL_EXPORT
QOpcUa::TimestampsToReturn ritual_ZNK27QOpcUaHistoryReadRawRequest18timestampsToReturnEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return self->timestampsToReturn();
}

//  void QOpcUaHistoryReadRawRequest::setTimestampsToReturn(QOpcUa::Timestamp
//      sToReturn timestampsToReturn)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest21setTimestampsToReturnEN6QOpcUa18TimestampsToReturnE(
    QOpcUaHistoryReadRawRequest *self,
    QOpcUa::TimestampsToReturn timestampsToReturn) {
  self->setTimestampsToReturn(timestampsToReturn);
}

//  QList<QOpcUaReadItem> QOpcUaHistoryReadRawRequest::nodesToRead() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaReadItem> *ritual_ZNK27QOpcUaHistoryReadRawRequest11nodesToReadEv(
    const QOpcUaHistoryReadRawRequest *self) {
  return new QList<QOpcUaReadItem>(self->nodesToRead());
}

//  void QOpcUaHistoryReadRawRequest::setNodesToRead(const
//      QList<QOpcUaReadItem> &nodesToRead)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest14setNodesToReadERK5QListI14QOpcUaReadItemE(
    QOpcUaHistoryReadRawRequest *self,
    const QList<QOpcUaReadItem> *nodesToRead) {
  self->setNodesToRead(*nodesToRead);
}

//  void QOpcUaHistoryReadRawRequest::addNodeToRead(const QOpcUaReadItem
//      &nodeToRead)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaHistoryReadRawRequest13addNodeToReadERK14QOpcUaReadItem(
    QOpcUaHistoryReadRawRequest *self,
    const QOpcUaReadItem *nodeToRead) {
  self->addNodeToRead(*nodeToRead);
}

//  bool operator==(const QOpcUaHistoryReadRawRequest &lhs, const
//      QOpcUaHistoryReadRawRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK27QOpcUaHistoryReadRawRequestS1_(
    const QOpcUaHistoryReadRawRequest *lhs,
    const QOpcUaHistoryReadRawRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaHistoryReadRawRequest &lhs, const
//      QOpcUaHistoryReadRawRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK27QOpcUaHistoryReadRawRequestS1_(
    const QOpcUaHistoryReadRawRequest *lhs,
    const QOpcUaHistoryReadRawRequest *rhs) {
  return operator!=(*lhs, *rhs);
}
