//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqttmessage.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqtttopicname.h>
#include <QtMqtt/qmqttpublishproperties.h>

//  QMqttMessage::QMqttMessage()
extern "C" Q_DECL_EXPORT
QMqttMessage *ritual_ZN12QMqttMessageC1Ev() {
  return new QMqttMessage();
}

//  QMqttMessage::QMqttMessage(const QMqttMessage &other)
extern "C" Q_DECL_EXPORT
QMqttMessage *ritual_ZN12QMqttMessageC1ERKS_(const QMqttMessage *other) {
  return new QMqttMessage(*other);
}

//  QMqttMessage::~QMqttMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMqttMessageD1Ev(QMqttMessage *self) {
  delete self;
}

//  bool QMqttMessage::operator==(const QMqttMessage &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMqttMessageeqERKS_(
    const QMqttMessage *self,
    const QMqttMessage *other) {
  return self->operator==(*other);
}

//  const QByteArray &QMqttMessage::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QMqttMessage7payloadEv(const QMqttMessage *self) {
  return new QByteArray(self->payload());
}

//  quint8 QMqttMessage::qos() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK12QMqttMessage3qosEv(const QMqttMessage *self) {
  return self->qos();
}

//  quint16 QMqttMessage::id() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK12QMqttMessage2idEv(const QMqttMessage *self) {
  return self->id();
}

//  QMqttTopicName QMqttMessage::topic() const
extern "C" Q_DECL_EXPORT
QMqttTopicName *ritual_ZNK12QMqttMessage5topicEv(const QMqttMessage *self) {
  return new QMqttTopicName(self->topic());
}

//  bool QMqttMessage::duplicate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMqttMessage9duplicateEv(const QMqttMessage *self) {
  return self->duplicate();
}

//  bool QMqttMessage::retain() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMqttMessage6retainEv(const QMqttMessage *self) {
  return self->retain();
}

//  QMqttPublishProperties QMqttMessage::publishProperties() const
extern "C" Q_DECL_EXPORT
QMqttPublishProperties *ritual_ZNK12QMqttMessage17publishPropertiesEv(
    const QMqttMessage *self) {
  return new QMqttPublishProperties(self->publishProperties());
}

//  QMqttMessage::QMqttMessage(const QMqttTopicName &topic, const QByteArray
//      &payload, quint16 id, quint8 qos, bool dup, bool retain)
extern "C" Q_DECL_EXPORT
QMqttMessage *ritual_ZN12QMqttMessageC1ERK14QMqttTopicNameRK10QByteArraythbb(
    const QMqttTopicName *topic,
    const QByteArray *payload,
    quint16 id,
    quint8 qos,
    bool dup,
    bool retain) {
  return new QMqttMessage(*topic, *payload, id, qos, dup, retain);
}
