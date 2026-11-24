//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusclient_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbuspdu.h>
#include <QtSerialBus/qmodbusdataunit.h>

//  QModbusClientPrivate::QueueElement::QueueElement()
extern "C" Q_DECL_EXPORT
QModbusClientPrivate::QueueElement *ritual_ZN20QModbusClientPrivate12QueueElementC1Ev() {
  return new QModbusClientPrivate::QueueElement();
}

//  QModbusClientPrivate::QueueElement::QueueElement(QModbusReply *r, const
//      QModbusRequest &req, const QModbusDataUnit &u, int num, int timeout)
extern "C" Q_DECL_EXPORT
QModbusClientPrivate::QueueElement *ritual_ZN20QModbusClientPrivate12QueueElementC1EP12QModbusReplyRK14QModbusRequestRK15QModbusDataUnitii(
    QModbusReply *r,
    const QModbusRequest *req,
    const QModbusDataUnit *u,
    int num,
    int timeout) {
  return new QModbusClientPrivate::QueueElement(r, *req, *u, num, timeout);
}

//  bool QModbusClientPrivate::QueueElement::operator==(const QueueElement
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QModbusClientPrivate12QueueElementeqERKS0_(
    const QModbusClientPrivate::QueueElement *self,
    const QModbusClientPrivate::QueueElement *other) {
  return self->operator==(*other);
}

//  QModbusClientPrivate::QueueElement::~QueueElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusClientPrivate12QueueElementD1Ev(
    QModbusClientPrivate::QueueElement *self) {
  delete self;
}
