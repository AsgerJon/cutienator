//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusframe.h>

//  QCanBusFrame::TimeStamp::TimeStamp(qint64 s, qint64 usec)
extern "C" Q_DECL_EXPORT
QCanBusFrame::TimeStamp *ritual_ZN12QCanBusFrame9TimeStampC1Exx(
    qint64 s,
    qint64 usec) {
  return new QCanBusFrame::TimeStamp(s, usec);
}

//  TimeStamp QCanBusFrame::TimeStamp::fromMicroSeconds(qint64 usec)
extern "C" Q_DECL_EXPORT
QCanBusFrame::TimeStamp *ritual_ZN12QCanBusFrame9TimeStamp16fromMicroSecondsEx(
    qint64 usec) {
  return new QCanBusFrame::TimeStamp(
      QCanBusFrame::TimeStamp::fromMicroSeconds(
          usec));
}

//  qint64 QCanBusFrame::TimeStamp::seconds() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QCanBusFrame9TimeStamp7secondsEv(
    const QCanBusFrame::TimeStamp *self) {
  return self->seconds();
}

//  qint64 QCanBusFrame::TimeStamp::microSeconds() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QCanBusFrame9TimeStamp12microSecondsEv(
    const QCanBusFrame::TimeStamp *self) {
  return self->microSeconds();
}

//  QCanBusFrame::TimeStamp::~TimeStamp()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanBusFrame9TimeStampD1Ev(QCanBusFrame::TimeStamp *self) {
  delete self;
}
