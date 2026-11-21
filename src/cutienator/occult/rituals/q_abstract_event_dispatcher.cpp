//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAbstractEventDispatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QAbstractEventDispatcher10metaObjectEv(
    const QAbstractEventDispatcher *self) {
  return self->metaObject();
}

//  QString QAbstractEventDispatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QAbstractEventDispatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractEventDispatcher::tr(s, c, n));
}

//  QAbstractEventDispatcher::~QAbstractEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcherD1Ev(
    QAbstractEventDispatcher *self) {
  delete self;
}

//  QAbstractEventDispatcher *QAbstractEventDispatcher::instance(QThread
//      *thread)
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN24QAbstractEventDispatcher8instanceEP7QThread(
    QThread *thread) {
  return QAbstractEventDispatcher::instance(thread);
}

//  bool
//      QAbstractEventDispatcher::processEvents(QEventLoop::ProcessEventsFlag
//      s flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QAbstractEventDispatcher *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSocketNotifier(
    QAbstractEventDispatcher *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15QSocketNotifier(
    QAbstractEventDispatcher *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

//  int QAbstractEventDispatcher::registerTimer(qint64 interval,
//      Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QAbstractEventDispatcher13registerTimerExN2Qt9TimerTypeEP7QObject(
    QAbstractEventDispatcher *self,
    qint64 interval,
    Qt::TimerType timerType,
    QObject *object) {
  return self->registerTimer(interval, timerType, object);
}

//  void QAbstractEventDispatcher::registerTimer(int timerId, qint64
//      interval, Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher13registerTimerEixN2Qt9TimerTypeEP7QObject(
    QAbstractEventDispatcher *self,
    int timerId,
    qint64 interval,
    Qt::TimerType timerType,
    QObject *object) {
  self->registerTimer(timerId, interval, timerType, object);
}

//  bool QAbstractEventDispatcher::unregisterTimer(int timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher15unregisterTimerEi(
    QAbstractEventDispatcher *self,
    int timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QAbstractEventDispatcher::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher16unregisterTimersEP7QObject(
    QAbstractEventDispatcher *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  int QAbstractEventDispatcher::remainingTime(int timerId)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QAbstractEventDispatcher13remainingTimeEi(
    QAbstractEventDispatcher *self,
    int timerId) {
  return self->remainingTime(timerId);
}

//  bool QAbstractEventDispatcher::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher15unregisterTimerEN2Qt7TimerIdE(
    QAbstractEventDispatcher *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  void QAbstractEventDispatcher::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher6wakeUpEv(
    QAbstractEventDispatcher *self) {
  self->wakeUp();
}

//  void QAbstractEventDispatcher::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher9interruptEv(
    QAbstractEventDispatcher *self) {
  self->interrupt();
}

//  void QAbstractEventDispatcher::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher10startingUpEv(
    QAbstractEventDispatcher *self) {
  self->startingUp();
}

//  void QAbstractEventDispatcher::closingDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher11closingDownEv(
    QAbstractEventDispatcher *self) {
  self->closingDown();
}

//  void QAbstractEventDispatcher::installNativeEventFilter(QAbstractNativeEv
//      entFilter *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher24installNativeEventFilterEP26QAbstractNativeEventFilter(
    QAbstractEventDispatcher *self,
    QAbstractNativeEventFilter *filterObj) {
  self->installNativeEventFilter(filterObj);
}

//  void QAbstractEventDispatcher::removeNativeEventFilter(QAbstractNativeEve
//      ntFilter *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher23removeNativeEventFilterEP26QAbstractNativeEventFilter(
    QAbstractEventDispatcher *self,
    QAbstractNativeEventFilter *filterObj) {
  self->removeNativeEventFilter(filterObj);
}
