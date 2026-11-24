//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuamonitoringparameters.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuamonitoringparameters.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuaeventfilterresult.h>
#include <QtCore/qstring.h>

//  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters()
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters *ritual_ZN26QOpcUaMonitoringParametersC1Ev() {
  return new QOpcUaMonitoringParameters();
}

//  QOpcUaMonitoringParameters::~QOpcUaMonitoringParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParametersD1Ev(
    QOpcUaMonitoringParameters *self) {
  delete self;
}

//  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(double
//      publishingInterval, SubscriptionType subscriptionType, quint32
//      subscriptionId)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters *ritual_ZN26QOpcUaMonitoringParametersC1EdNS_16SubscriptionTypeEj(
    double publishingInterval,
    QOpcUaMonitoringParameters::SubscriptionType subscriptionType,
    quint32 subscriptionId) {
  return new QOpcUaMonitoringParameters(
      publishingInterval,
      subscriptionType,
      subscriptionId);
}

//  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(const
//      QOpcUaMonitoringParameters &other)
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters *ritual_ZN26QOpcUaMonitoringParametersC1ERKS_(
    const QOpcUaMonitoringParameters *other) {
  return new QOpcUaMonitoringParameters(*other);
}

//  double QOpcUaMonitoringParameters::samplingInterval() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK26QOpcUaMonitoringParameters16samplingIntervalEv(
    const QOpcUaMonitoringParameters *self) {
  return self->samplingInterval();
}

//  void QOpcUaMonitoringParameters::setSamplingInterval(double
//      samplingInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters19setSamplingIntervalEd(
    QOpcUaMonitoringParameters *self,
    double samplingInterval) {
  self->setSamplingInterval(samplingInterval);
}

//  QVariant QOpcUaMonitoringParameters::filter() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QOpcUaMonitoringParameters6filterEv(
    const QOpcUaMonitoringParameters *self) {
  return new QVariant(self->filter());
}

//  void QOpcUaMonitoringParameters::setFilter(const
//      QOpcUaMonitoringParameters::DataChangeFilter &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters9setFilterERKNS_16DataChangeFilterE(
    QOpcUaMonitoringParameters *self,
    const QOpcUaMonitoringParameters::DataChangeFilter *filter) {
  self->setFilter(*filter);
}

//  void QOpcUaMonitoringParameters::setFilter(const
//      QOpcUaMonitoringParameters::EventFilter &eventFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters9setFilterERKNS_11EventFilterE(
    QOpcUaMonitoringParameters *self,
    const QOpcUaMonitoringParameters::EventFilter *eventFilter) {
  self->setFilter(*eventFilter);
}

//  void QOpcUaMonitoringParameters::clearFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters11clearFilterEv(
    QOpcUaMonitoringParameters *self) {
  self->clearFilter();
}

//  QVariant QOpcUaMonitoringParameters::filterResult() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QOpcUaMonitoringParameters12filterResultEv(
    const QOpcUaMonitoringParameters *self) {
  return new QVariant(self->filterResult());
}

//  void QOpcUaMonitoringParameters::setFilterResult(const
//      QOpcUaEventFilterResult &eventFilterResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters15setFilterResultERK23QOpcUaEventFilterResult(
    QOpcUaMonitoringParameters *self,
    const QOpcUaEventFilterResult *eventFilterResult) {
  self->setFilterResult(*eventFilterResult);
}

//  void QOpcUaMonitoringParameters::clearFilterResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters17clearFilterResultEv(
    QOpcUaMonitoringParameters *self) {
  self->clearFilterResult();
}

//  quint32 QOpcUaMonitoringParameters::queueSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters9queueSizeEv(
    const QOpcUaMonitoringParameters *self) {
  return self->queueSize();
}

//  void QOpcUaMonitoringParameters::setQueueSize(quint32 queueSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters12setQueueSizeEj(
    QOpcUaMonitoringParameters *self,
    quint32 queueSize) {
  self->setQueueSize(queueSize);
}

//  bool QOpcUaMonitoringParameters::discardOldest() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaMonitoringParameters13discardOldestEv(
    const QOpcUaMonitoringParameters *self) {
  return self->discardOldest();
}

//  void QOpcUaMonitoringParameters::setDiscardOldest(bool discardOldest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16setDiscardOldestEb(
    QOpcUaMonitoringParameters *self,
    bool discardOldest) {
  self->setDiscardOldest(discardOldest);
}

//  QOpcUaMonitoringParameters::MonitoringMode
//      QOpcUaMonitoringParameters::monitoringMode() const
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::MonitoringMode ritual_ZNK26QOpcUaMonitoringParameters14monitoringModeEv(
    const QOpcUaMonitoringParameters *self) {
  return self->monitoringMode();
}

//  void QOpcUaMonitoringParameters::setMonitoringMode(MonitoringMode
//      monitoringMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters17setMonitoringModeENS_14MonitoringModeE(
    QOpcUaMonitoringParameters *self,
    QOpcUaMonitoringParameters::MonitoringMode monitoringMode) {
  self->setMonitoringMode(monitoringMode);
}

//  quint32 QOpcUaMonitoringParameters::subscriptionId() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters14subscriptionIdEv(
    const QOpcUaMonitoringParameters *self) {
  return self->subscriptionId();
}

//  void QOpcUaMonitoringParameters::setSubscriptionId(quint32
//      subscriptionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters17setSubscriptionIdEj(
    QOpcUaMonitoringParameters *self,
    quint32 subscriptionId) {
  self->setSubscriptionId(subscriptionId);
}

//  quint32 QOpcUaMonitoringParameters::monitoredItemId() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters15monitoredItemIdEv(
    const QOpcUaMonitoringParameters *self) {
  return self->monitoredItemId();
}

//  void QOpcUaMonitoringParameters::setMonitoredItemId(quint32
//      monitoredItemId)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters18setMonitoredItemIdEj(
    QOpcUaMonitoringParameters *self,
    quint32 monitoredItemId) {
  self->setMonitoredItemId(monitoredItemId);
}

//  double QOpcUaMonitoringParameters::publishingInterval() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK26QOpcUaMonitoringParameters18publishingIntervalEv(
    const QOpcUaMonitoringParameters *self) {
  return self->publishingInterval();
}

//  void QOpcUaMonitoringParameters::setPublishingInterval(double
//      publishingInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters21setPublishingIntervalEd(
    QOpcUaMonitoringParameters *self,
    double publishingInterval) {
  self->setPublishingInterval(publishingInterval);
}

//  quint32 QOpcUaMonitoringParameters::lifetimeCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters13lifetimeCountEv(
    const QOpcUaMonitoringParameters *self) {
  return self->lifetimeCount();
}

//  void QOpcUaMonitoringParameters::setLifetimeCount(quint32 lifetimeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters16setLifetimeCountEj(
    QOpcUaMonitoringParameters *self,
    quint32 lifetimeCount) {
  self->setLifetimeCount(lifetimeCount);
}

//  quint32 QOpcUaMonitoringParameters::maxKeepAliveCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters17maxKeepAliveCountEv(
    const QOpcUaMonitoringParameters *self) {
  return self->maxKeepAliveCount();
}

//  void QOpcUaMonitoringParameters::setMaxKeepAliveCount(quint32
//      maxKeepAliveCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters20setMaxKeepAliveCountEj(
    QOpcUaMonitoringParameters *self,
    quint32 maxKeepAliveCount) {
  self->setMaxKeepAliveCount(maxKeepAliveCount);
}

//  quint32 QOpcUaMonitoringParameters::maxNotificationsPerPublish() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK26QOpcUaMonitoringParameters26maxNotificationsPerPublishEv(
    const QOpcUaMonitoringParameters *self) {
  return self->maxNotificationsPerPublish();
}

//  void QOpcUaMonitoringParameters::setMaxNotificationsPerPublish(quint32
//      maxNotificationsPerPublish)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters29setMaxNotificationsPerPublishEj(
    QOpcUaMonitoringParameters *self,
    quint32 maxNotificationsPerPublish) {
  self->setMaxNotificationsPerPublish(maxNotificationsPerPublish);
}

//  quint8 QOpcUaMonitoringParameters::priority() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK26QOpcUaMonitoringParameters8priorityEv(
    const QOpcUaMonitoringParameters *self) {
  return self->priority();
}

//  void QOpcUaMonitoringParameters::setPriority(quint8 priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters11setPriorityEh(
    QOpcUaMonitoringParameters *self,
    quint8 priority) {
  self->setPriority(priority);
}

//  bool QOpcUaMonitoringParameters::isPublishingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaMonitoringParameters19isPublishingEnabledEv(
    const QOpcUaMonitoringParameters *self) {
  return self->isPublishingEnabled();
}

//  void QOpcUaMonitoringParameters::setPublishingEnabled(bool
//      publishingEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters20setPublishingEnabledEb(
    QOpcUaMonitoringParameters *self,
    bool publishingEnabled) {
  self->setPublishingEnabled(publishingEnabled);
}

//  QOpcUa::UaStatusCode QOpcUaMonitoringParameters::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK26QOpcUaMonitoringParameters10statusCodeEv(
    const QOpcUaMonitoringParameters *self) {
  return self->statusCode();
}

//  void QOpcUaMonitoringParameters::setStatusCode(QOpcUa::UaStatusCode
//      statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaMonitoringParameters *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QOpcUaMonitoringParameters::SubscriptionType
//      QOpcUaMonitoringParameters::subscriptionType() const
extern "C" Q_DECL_EXPORT
QOpcUaMonitoringParameters::SubscriptionType ritual_ZNK26QOpcUaMonitoringParameters16subscriptionTypeEv(
    const QOpcUaMonitoringParameters *self) {
  return self->subscriptionType();
}

//  void QOpcUaMonitoringParameters::setSubscriptionType(SubscriptionType
//      subscriptionType)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters19setSubscriptionTypeENS_16SubscriptionTypeE(
    QOpcUaMonitoringParameters *self,
    QOpcUaMonitoringParameters::SubscriptionType subscriptionType) {
  self->setSubscriptionType(subscriptionType);
}

//  QString QOpcUaMonitoringParameters::indexRange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaMonitoringParameters10indexRangeEv(
    const QOpcUaMonitoringParameters *self) {
  return new QString(self->indexRange());
}

//  void QOpcUaMonitoringParameters::setIndexRange(const QString &indexRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaMonitoringParameters13setIndexRangeERK7QString(
    QOpcUaMonitoringParameters *self,
    const QString *indexRange) {
  self->setIndexRange(*indexRange);
}
