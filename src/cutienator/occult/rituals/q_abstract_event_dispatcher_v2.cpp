//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>

//  const QMetaObject *QAbstractEventDispatcherV2::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAbstractEventDispatcherV210metaObjectEv(
    const QAbstractEventDispatcherV2 *self) {
  return self->metaObject();
}

//  QString QAbstractEventDispatcherV2::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAbstractEventDispatcherV22trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractEventDispatcherV2::tr(s, c, n));
}

//  QAbstractEventDispatcherV2::~QAbstractEventDispatcherV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractEventDispatcherV2D1Ev(
    QAbstractEventDispatcherV2 *self) {
  delete self;
}

//  bool QAbstractEventDispatcherV2::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractEventDispatcherV215unregisterTimerEN2Qt7TimerIdE(
    QAbstractEventDispatcherV2 *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop::Pr
//      ocessEventsFlags flags, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer(
    QAbstractEventDispatcherV2 *self,
    int flags,
    const QDeadlineTimer *deadline) {
  return self->processEventsWithDeadline(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}
