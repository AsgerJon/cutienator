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

//  void *Timer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN5Timer11qt_metacastEPKc(Timer *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Timer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN5Timer11qt_metacallEN11QMetaObject4CallEiPPv(
    Timer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void Timer::timeout(int timerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer7timeoutEi(Timer *self, int timerId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Timer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "timeout(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "timeout(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&timerId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Timer::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Timer10timerEventEP11QTimerEvent(
    Timer *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#endif  // QT_CONFIG(modbus_serialport)
