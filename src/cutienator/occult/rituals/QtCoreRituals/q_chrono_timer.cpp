//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchronotimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qchronotimer.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QChronoTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QChronoTimer10metaObjectEv(
    const QChronoTimer *self) {
  return self->metaObject();
}

//  QString QChronoTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QChronoTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QChronoTimer::tr(s, c, n));
}

//  QChronoTimer::QChronoTimer(QObject *parent)
extern "C" Q_DECL_EXPORT
QChronoTimer *ritual_ZN12QChronoTimerC1EP7QObject(QObject *parent) {
  return new QChronoTimer(parent);
}

//  QChronoTimer::~QChronoTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimerD1Ev(QChronoTimer *self) {
  delete self;
}

//  bool QChronoTimer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QChronoTimer8isActiveEv(const QChronoTimer *self) {
  return self->isActive();
}

//  Qt::TimerId QChronoTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK12QChronoTimer2idEv(const QChronoTimer *self) {
  return self->id();
}

//  void QChronoTimer::setTimerType(Qt::TimerType atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer12setTimerTypeEN2Qt9TimerTypeE(
    QChronoTimer *self,
    Qt::TimerType atype) {
  self->setTimerType(atype);
}

//  Qt::TimerType QChronoTimer::timerType() const
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZNK12QChronoTimer9timerTypeEv(
    const QChronoTimer *self) {
  return self->timerType();
}

//  void QChronoTimer::setSingleShot(bool singleShot)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer13setSingleShotEb(
    QChronoTimer *self,
    bool singleShot) {
  self->setSingleShot(singleShot);
}

//  bool QChronoTimer::isSingleShot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QChronoTimer12isSingleShotEv(const QChronoTimer *self) {
  return self->isSingleShot();
}

//  void QChronoTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer5startEv(QChronoTimer *self) {
  self->start();
}

//  void QChronoTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer4stopEv(QChronoTimer *self) {
  self->stop();
}
