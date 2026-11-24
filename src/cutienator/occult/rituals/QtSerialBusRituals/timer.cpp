//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSerialBus/qtserialbusglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(modbus_serialport)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *Timer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5Timer10metaObjectEv(const Timer *self) {
  return self->metaObject();
}

//  int Timer::start(int msec)
extern "C" Q_DECL_EXPORT
int ritual_ZN5Timer5startEi(Timer *self, int msec) {
  return self->start(msec);
}

//  void Timer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer4stopEv(Timer *self) {
  self->stop();
}

//  bool Timer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Timer8isActiveEv(const Timer *self) {
  return self->isActive();
}

//  void Timer::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer10timerEventEP11QTimerEvent(
    Timer *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#endif  // QT_CONFIG(modbus_serialport)
