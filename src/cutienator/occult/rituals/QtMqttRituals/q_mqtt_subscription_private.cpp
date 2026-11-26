//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/6.12.0/QtMqtt/private/qmqttsubscription_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/qmqttsubscription.h>
#include <QtMqtt/QtMqtt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttsubscription_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/qmqttsubscription.h>
#include <QtMqtt/private/qmqttsubscription_p.h>
#include <QtMqtt/qmqttclient.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttsubscription.cpp, line 219, as _ZN24QMqttSubscriptionPrivateC1Ev
inline QMqttSubscriptionPrivate::QMqttSubscriptionPrivate()
    : QObjectPrivate()
{

}
//  -----------------------------------------------------------------------

//  QMqttSubscription *QMqttSubscriptionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMqttSubscription *ritual_ZN24QMqttSubscriptionPrivate6q_funcEv(
    QMqttSubscriptionPrivate *self) {
  return self->q_func();
}

//  const QMqttSubscription *QMqttSubscriptionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMqttSubscription *ritual_ZNK24QMqttSubscriptionPrivate6q_funcEv(
    const QMqttSubscriptionPrivate *self) {
  return self->q_func();
}

//  QMqttSubscriptionPrivate::QMqttSubscriptionPrivate()
extern "C" Q_DECL_EXPORT
QMqttSubscriptionPrivate *ritual_ZN24QMqttSubscriptionPrivateC1Ev() {
  return new QMqttSubscriptionPrivate();
}

//  QMqttSubscriptionPrivate::~QMqttSubscriptionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMqttSubscriptionPrivateD1Ev(
    QMqttSubscriptionPrivate *self) {
  delete self;
}
