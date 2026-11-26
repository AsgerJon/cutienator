//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/qmqttmessage.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqtttopicname.h>
#include <QtMqtt/qmqttpublishproperties.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/qmqttmessage.h>
#include <QtMqtt/private/qmqttmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttmessage.cpp, line 105, as _ZNK12QMqttMessageneERKS_
inline bool QMqttMessage::operator!=(const QMqttMessage &other) const
{
    return !(*this == other);
}
//  -----------------------------------------------------------------------

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

//  QMqttMessage &QMqttMessage::operator=(const QMqttMessage &other)
extern "C" Q_DECL_EXPORT
QMqttMessage *ritual_ZN12QMqttMessageaSERKS_(
    QMqttMessage *self,
    const QMqttMessage *other) {
  return &(self->operator=(*other));
}

//  bool QMqttMessage::operator==(const QMqttMessage &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMqttMessageeqERKS_(
    const QMqttMessage *self,
    const QMqttMessage *other) {
  return self->operator==(*other);
}

//  bool QMqttMessage::operator!=(const QMqttMessage &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMqttMessageneERKS_(
    const QMqttMessage *self,
    const QMqttMessage *other) {
  return self->operator!=(*other);
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
