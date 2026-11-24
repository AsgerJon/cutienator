//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuahistoryreadeventrequest.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuahistoryreadeventrequest.h>
#include <QtOpcUa/qopcuareaditem.h>
#include <QtCore/qdatetime.h>
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtCore/qlist.h>

//  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadEventRequest *ritual_ZN29QOpcUaHistoryReadEventRequestC1Ev() {
  return new QOpcUaHistoryReadEventRequest();
}

//  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
//      QList<QOpcUaReadItem> &nodesToRead, const QDateTime &startTimestamp,
//      const QDateTime &endTimestamp, const
//      QOpcUaMonitoringParameters::EventFilter &filter)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadEventRequest *ritual_ZN29QOpcUaHistoryReadEventRequestC1ERK5QListI14QOpcUaReadItemERK9QDateTimeS7_RKN26QOpcUaMonitoringParameters11EventFilterE(
    const QList<QOpcUaReadItem> *nodesToRead,
    const QDateTime *startTimestamp,
    const QDateTime *endTimestamp,
    const QOpcUaMonitoringParameters::EventFilter *filter) {
  return new QOpcUaHistoryReadEventRequest(
      *nodesToRead,
      *startTimestamp,
      *endTimestamp,
      *filter);
}

//  QOpcUaHistoryReadEventRequest::QOpcUaHistoryReadEventRequest(const
//      QOpcUaHistoryReadEventRequest &other)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadEventRequest *ritual_ZN29QOpcUaHistoryReadEventRequestC1ERKS_(
    const QOpcUaHistoryReadEventRequest *other) {
  return new QOpcUaHistoryReadEventRequest(*other);
}

//  QOpcUaHistoryReadEventRequest::~QOpcUaHistoryReadEventRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequestD1Ev(
    QOpcUaHistoryReadEventRequest *self) {
  delete self;
}

//  QDateTime QOpcUaHistoryReadEventRequest::startTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK29QOpcUaHistoryReadEventRequest14startTimestampEv(
    const QOpcUaHistoryReadEventRequest *self) {
  return new QDateTime(self->startTimestamp());
}

//  void QOpcUaHistoryReadEventRequest::setStartTimestamp(const QDateTime
//      &startTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest17setStartTimestampERK9QDateTime(
    QOpcUaHistoryReadEventRequest *self,
    const QDateTime *startTimestamp) {
  self->setStartTimestamp(*startTimestamp);
}

//  QDateTime QOpcUaHistoryReadEventRequest::endTimestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK29QOpcUaHistoryReadEventRequest12endTimestampEv(
    const QOpcUaHistoryReadEventRequest *self) {
  return new QDateTime(self->endTimestamp());
}

//  void QOpcUaHistoryReadEventRequest::setEndTimestamp(const QDateTime
//      &endTimestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest15setEndTimestampERK9QDateTime(
    QOpcUaHistoryReadEventRequest *self,
    const QDateTime *endTimestamp) {
  self->setEndTimestamp(*endTimestamp);
}

//  quint32 QOpcUaHistoryReadEventRequest::numValuesPerNode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK29QOpcUaHistoryReadEventRequest16numValuesPerNodeEv(
    const QOpcUaHistoryReadEventRequest *self) {
  return self->numValuesPerNode();
}

//  void QOpcUaHistoryReadEventRequest::setNumValuesPerNode(quint32
//      numValuesPerNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest19setNumValuesPerNodeEj(
    QOpcUaHistoryReadEventRequest *self,
    quint32 numValuesPerNode) {
  self->setNumValuesPerNode(numValuesPerNode);
}

//  QOpcUaMonitoringParameters::EventFilter
//      QOpcUaHistoryReadEventRequest::filter() const
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::EventFilter *ritual_ZNK29QOpcUaHistoryReadEventRequest6filterEv(
    const QOpcUaHistoryReadEventRequest *self) {
  return new QOpcUaMonitoringParameters::EventFilter(self->filter());
}

//  void QOpcUaHistoryReadEventRequest::setFilter(const
//      QOpcUaMonitoringParameters::EventFilter &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest9setFilterERKN26QOpcUaMonitoringParameters11EventFilterE(
    QOpcUaHistoryReadEventRequest *self,
    const QOpcUaMonitoringParameters::EventFilter *filter) {
  self->setFilter(*filter);
}

//  QList<QOpcUaReadItem> QOpcUaHistoryReadEventRequest::nodesToRead() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaReadItem> *ritual_ZNK29QOpcUaHistoryReadEventRequest11nodesToReadEv(
    const QOpcUaHistoryReadEventRequest *self) {
  return new QList<QOpcUaReadItem>(self->nodesToRead());
}

//  void QOpcUaHistoryReadEventRequest::setNodesToRead(const
//      QList<QOpcUaReadItem> &nodesToRead)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest14setNodesToReadERK5QListI14QOpcUaReadItemE(
    QOpcUaHistoryReadEventRequest *self,
    const QList<QOpcUaReadItem> *nodesToRead) {
  self->setNodesToRead(*nodesToRead);
}

//  void QOpcUaHistoryReadEventRequest::addNodeToRead(const QOpcUaReadItem
//      &nodeToRead)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpcUaHistoryReadEventRequest13addNodeToReadERK14QOpcUaReadItem(
    QOpcUaHistoryReadEventRequest *self,
    const QOpcUaReadItem *nodeToRead) {
  self->addNodeToRead(*nodeToRead);
}

//  bool operator==(const QOpcUaHistoryReadEventRequest &lhs, const
//      QOpcUaHistoryReadEventRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK29QOpcUaHistoryReadEventRequestS1_(
    const QOpcUaHistoryReadEventRequest *lhs,
    const QOpcUaHistoryReadEventRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaHistoryReadEventRequest &lhs, const
//      QOpcUaHistoryReadEventRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK29QOpcUaHistoryReadEventRequestS1_(
    const QOpcUaHistoryReadEventRequest *lhs,
    const QOpcUaHistoryReadEventRequest *rhs) {
  return operator!=(*lhs, *rhs);
}
