//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttpublishproperties.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqttpublishproperties.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttPublishProperties::QMqttPublishProperties()
extern "C" Q_DECL_EXPORT
QMqttPublishProperties *ritual_ZN22QMqttPublishPropertiesC1Ev() {
  return new QMqttPublishProperties();
}

//  QMqttPublishProperties::QMqttPublishProperties(const
//      QMqttPublishProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttPublishProperties *ritual_ZN22QMqttPublishPropertiesC1ERKS_(
    const QMqttPublishProperties *a0) {
  return new QMqttPublishProperties(*a0);
}

//  QMqttPublishProperties::~QMqttPublishProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishPropertiesD1Ev(QMqttPublishProperties *self) {
  delete self;
}

//  PublishPropertyDetails QMqttPublishProperties::availableProperties()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QMqttPublishProperties19availablePropertiesEv(
    const QMqttPublishProperties *self) {
  return static_cast<int>(self->availableProperties().toInt());
}

//  QMqtt::PayloadFormatIndicator
//      QMqttPublishProperties::payloadFormatIndicator() const
extern "C" Q_DECL_EXPORT
QMqtt::PayloadFormatIndicator ritual_ZNK22QMqttPublishProperties22payloadFormatIndicatorEv(
    const QMqttPublishProperties *self) {
  return self->payloadFormatIndicator();
}

//  void QMqttPublishProperties::setPayloadFormatIndicator(QMqtt::PayloadForm
//      atIndicator indicator)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties25setPayloadFormatIndicatorEN5QMqtt22PayloadFormatIndicatorE(
    QMqttPublishProperties *self,
    QMqtt::PayloadFormatIndicator indicator) {
  self->setPayloadFormatIndicator(indicator);
}

//  quint32 QMqttPublishProperties::messageExpiryInterval() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK22QMqttPublishProperties21messageExpiryIntervalEv(
    const QMqttPublishProperties *self) {
  return self->messageExpiryInterval();
}

//  void QMqttPublishProperties::setMessageExpiryInterval(quint32 interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties24setMessageExpiryIntervalEj(
    QMqttPublishProperties *self,
    quint32 interval) {
  self->setMessageExpiryInterval(interval);
}

//  quint16 QMqttPublishProperties::topicAlias() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK22QMqttPublishProperties10topicAliasEv(
    const QMqttPublishProperties *self) {
  return self->topicAlias();
}

//  void QMqttPublishProperties::setTopicAlias(quint16 alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties13setTopicAliasEt(
    QMqttPublishProperties *self,
    quint16 alias) {
  self->setTopicAlias(alias);
}

//  QString QMqttPublishProperties::responseTopic() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QMqttPublishProperties13responseTopicEv(
    const QMqttPublishProperties *self) {
  return new QString(self->responseTopic());
}

//  void QMqttPublishProperties::setResponseTopic(const QString &topic)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties16setResponseTopicERK7QString(
    QMqttPublishProperties *self,
    const QString *topic) {
  self->setResponseTopic(*topic);
}

//  QByteArray QMqttPublishProperties::correlationData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QMqttPublishProperties15correlationDataEv(
    const QMqttPublishProperties *self) {
  return new QByteArray(self->correlationData());
}

//  void QMqttPublishProperties::setCorrelationData(const QByteArray
//      &correlation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties18setCorrelationDataERK10QByteArray(
    QMqttPublishProperties *self,
    const QByteArray *correlation) {
  self->setCorrelationData(*correlation);
}

//  QMqttUserProperties QMqttPublishProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK22QMqttPublishProperties14userPropertiesEv(
    const QMqttPublishProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  void QMqttPublishProperties::setUserProperties(const QMqttUserProperties
//      &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttPublishProperties *self,
    const QMqttUserProperties *properties) {
  self->setUserProperties(*properties);
}

//  QString QMqttPublishProperties::contentType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QMqttPublishProperties11contentTypeEv(
    const QMqttPublishProperties *self) {
  return new QString(self->contentType());
}

//  void QMqttPublishProperties::setContentType(const QString &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMqttPublishProperties14setContentTypeERK7QString(
    QMqttPublishProperties *self,
    const QString *type) {
  self->setContentType(*type);
}
