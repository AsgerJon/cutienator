//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbasictimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbasictimer.h>

//  QBasicTimer::QBasicTimer()
extern "C" Q_DECL_EXPORT
QBasicTimer *ritual_ZN11QBasicTimerC1Ev() {
  return new QBasicTimer();
}

//  QBasicTimer::~QBasicTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimerD1Ev(QBasicTimer *self) {
  delete self;
}

//  QBasicTimer::QBasicTimer(QBasicTimer &&other)
extern "C" Q_DECL_EXPORT
QBasicTimer *ritual_ZN11QBasicTimerC1EOS_(QBasicTimer *other) {
  return new QBasicTimer(std::move(*other));
}

//  QBasicTimer &QBasicTimer::operator=(QBasicTimer &&other)
extern "C" Q_DECL_EXPORT
QBasicTimer *ritual_ZN11QBasicTimeraSEOS_(
    QBasicTimer *self,
    QBasicTimer *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QBasicTimer::swap(QBasicTimer &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer4swapERS_(QBasicTimer *self, QBasicTimer *other) {
  self->swap(*other);
}

//  bool QBasicTimer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QBasicTimer8isActiveEv(const QBasicTimer *self) {
  return self->isActive();
}

//  int QBasicTimer::timerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QBasicTimer7timerIdEv(const QBasicTimer *self) {
  return self->timerId();
}

//  Qt::TimerId QBasicTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK11QBasicTimer2idEv(const QBasicTimer *self) {
  return self->id();
}

//  void QBasicTimer::start(int msec, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer5startEiP7QObject(
    QBasicTimer *self,
    int msec,
    QObject *obj) {
  self->start(msec, obj);
}

//  void QBasicTimer::start(int msec, Qt::TimerType timerType, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer5startEiN2Qt9TimerTypeEP7QObject(
    QBasicTimer *self,
    int msec,
    Qt::TimerType timerType,
    QObject *obj) {
  self->start(msec, timerType, obj);
}

//  void QBasicTimer::start(Duration duration, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer5startENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEP7QObject(
    QBasicTimer *self,
    long long duration,
    QObject *obj) {
  self->start(QBasicTimer::Duration(duration), obj);
}

//  void QBasicTimer::start(Duration duration, Qt::TimerType timerType,
//      QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer5startENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEP7QObject(
    QBasicTimer *self,
    long long duration,
    Qt::TimerType timerType,
    QObject *obj) {
  self->start(QBasicTimer::Duration(duration), timerType, obj);
}

//  void QBasicTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicTimer4stopEv(QBasicTimer *self) {
  self->stop();
}
