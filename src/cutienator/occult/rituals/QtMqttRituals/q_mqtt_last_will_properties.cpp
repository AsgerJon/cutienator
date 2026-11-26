//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttconnectionproperties.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttLastWillProperties::QMqttLastWillProperties()
extern "C" Q_DECL_EXPORT
QMqttLastWillProperties *ritual_ZN23QMqttLastWillPropertiesC1Ev() {
  return new QMqttLastWillProperties();
}

//  QMqttLastWillProperties::QMqttLastWillProperties(const
//      QMqttLastWillProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttLastWillProperties *ritual_ZN23QMqttLastWillPropertiesC1ERKS_(
    const QMqttLastWillProperties *a0) {
  return new QMqttLastWillProperties(*a0);
}

//  QMqttLastWillProperties &QMqttLastWillProperties::operator=(const
//      QMqttLastWillProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttLastWillProperties *ritual_ZN23QMqttLastWillPropertiesaSERKS_(
    QMqttLastWillProperties *self,
    const QMqttLastWillProperties *a0) {
  return &(self->operator=(*a0));
}

//  QMqttLastWillProperties::~QMqttLastWillProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillPropertiesD1Ev(QMqttLastWillProperties *self) {
  delete self;
}

//  quint32 QMqttLastWillProperties::willDelayInterval() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK23QMqttLastWillProperties17willDelayIntervalEv(
    const QMqttLastWillProperties *self) {
  return self->willDelayInterval();
}

//  QMqtt::PayloadFormatIndicator
//      QMqttLastWillProperties::payloadFormatIndicator() const
extern "C" Q_DECL_EXPORT
QMqtt::PayloadFormatIndicator ritual_ZNK23QMqttLastWillProperties22payloadFormatIndicatorEv(
    const QMqttLastWillProperties *self) {
  return self->payloadFormatIndicator();
}

//  quint32 QMqttLastWillProperties::messageExpiryInterval() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK23QMqttLastWillProperties21messageExpiryIntervalEv(
    const QMqttLastWillProperties *self) {
  return self->messageExpiryInterval();
}

//  QString QMqttLastWillProperties::contentType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QMqttLastWillProperties11contentTypeEv(
    const QMqttLastWillProperties *self) {
  return new QString(self->contentType());
}

//  QString QMqttLastWillProperties::responseTopic() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QMqttLastWillProperties13responseTopicEv(
    const QMqttLastWillProperties *self) {
  return new QString(self->responseTopic());
}

//  QByteArray QMqttLastWillProperties::correlationData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QMqttLastWillProperties15correlationDataEv(
    const QMqttLastWillProperties *self) {
  return new QByteArray(self->correlationData());
}

//  QMqttUserProperties QMqttLastWillProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK23QMqttLastWillProperties14userPropertiesEv(
    const QMqttLastWillProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  void QMqttLastWillProperties::setWillDelayInterval(quint32 delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties20setWillDelayIntervalEj(
    QMqttLastWillProperties *self,
    quint32 delay) {
  self->setWillDelayInterval(delay);
}

//  void QMqttLastWillProperties::setPayloadFormatIndicator(QMqtt::PayloadFor
//      matIndicator p)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties25setPayloadFormatIndicatorEN5QMqtt22PayloadFormatIndicatorE(
    QMqttLastWillProperties *self,
    QMqtt::PayloadFormatIndicator p) {
  self->setPayloadFormatIndicator(p);
}

//  void QMqttLastWillProperties::setMessageExpiryInterval(quint32 expiry)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties24setMessageExpiryIntervalEj(
    QMqttLastWillProperties *self,
    quint32 expiry) {
  self->setMessageExpiryInterval(expiry);
}

//  void QMqttLastWillProperties::setContentType(const QString &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties14setContentTypeERK7QString(
    QMqttLastWillProperties *self,
    const QString *content) {
  self->setContentType(*content);
}

//  void QMqttLastWillProperties::setResponseTopic(const QString &response)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties16setResponseTopicERK7QString(
    QMqttLastWillProperties *self,
    const QString *response) {
  self->setResponseTopic(*response);
}

//  void QMqttLastWillProperties::setCorrelationData(const QByteArray
//      &correlation)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties18setCorrelationDataERK10QByteArray(
    QMqttLastWillProperties *self,
    const QByteArray *correlation) {
  self->setCorrelationData(*correlation);
}

//  void QMqttLastWillProperties::setUserProperties(const QMqttUserProperties
//      &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMqttLastWillProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttLastWillProperties *self,
    const QMqttUserProperties *properties) {
  self->setUserProperties(*properties);
}
