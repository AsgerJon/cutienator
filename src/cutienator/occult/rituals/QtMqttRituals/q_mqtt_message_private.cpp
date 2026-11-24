//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/6.12.0/QtMqtt/private/qmqttmessage_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/QtMqtt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QMqttMessagePrivate::operator==(const QMqttMessagePrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QMqttMessagePrivateeqERKS_(
    const QMqttMessagePrivate *self,
    const QMqttMessagePrivate *other) {
  return self->operator==(*other);
}

//  QMqttMessagePrivate::~QMqttMessagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMqttMessagePrivateD1Ev(QMqttMessagePrivate *self) {
  delete self;
}
