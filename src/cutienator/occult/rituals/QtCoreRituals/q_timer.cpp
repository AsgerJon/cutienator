//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtimer.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QTimer10metaObjectEv(const QTimer *self) {
  return self->metaObject();
}

//  QString QTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QTimer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QTimer::tr(s, c, n));
}

//  QTimer::QTimer(QObject *parent)
extern "C" Q_DECL_EXPORT
QTimer *ritual_ZN6QTimerC1EP7QObject(QObject *parent) {
  return new QTimer(parent);
}

//  QTimer::~QTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimerD1Ev(QTimer *self) {
  delete self;
}

//  bool QTimer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QTimer8isActiveEv(const QTimer *self) {
  return self->isActive();
}

//  int QTimer::timerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer7timerIdEv(const QTimer *self) {
  return self->timerId();
}

//  Qt::TimerId QTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK6QTimer2idEv(const QTimer *self) {
  return self->id();
}

//  void QTimer::setInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer11setIntervalEi(QTimer *self, int msec) {
  self->setInterval(msec);
}

//  int QTimer::interval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer8intervalEv(const QTimer *self) {
  return self->interval();
}

//  int QTimer::remainingTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer13remainingTimeEv(const QTimer *self) {
  return self->remainingTime();
}

//  void QTimer::setTimerType(Qt::TimerType atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer12setTimerTypeEN2Qt9TimerTypeE(
    QTimer *self,
    Qt::TimerType atype) {
  self->setTimerType(atype);
}

//  Qt::TimerType QTimer::timerType() const
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZNK6QTimer9timerTypeEv(const QTimer *self) {
  return self->timerType();
}

//  void QTimer::setSingleShot(bool singleShot)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer13setSingleShotEb(QTimer *self, bool singleShot) {
  self->setSingleShot(singleShot);
}

//  bool QTimer::isSingleShot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QTimer12isSingleShotEv(const QTimer *self) {
  return self->isSingleShot();
}

//  void QTimer::singleShot(int msec, const QObject *receiver, const char
//      *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotEiPK7QObjectPKc(
    int msec,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(msec, receiver, member);
}

//  void QTimer::singleShot(int msec, Qt::TimerType timerType, const QObject
//      *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotEiN2Qt9TimerTypeEPK7QObjectPKc(
    int msec,
    Qt::TimerType timerType,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(msec, timerType, receiver, member);
}

//  void QTimer::start(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer5startEi(QTimer *self, int msec) {
  self->start(msec);
}

//  void QTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer5startEv(QTimer *self) {
  self->start();
}

//  void QTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer4stopEv(QTimer *self) {
  self->stop();
}
