//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtimerinfo_unix_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtimerinfo_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <optional>
#include <QtCore/QList>
#include <chrono>

//  QTimerInfoList::QTimerInfoList()
extern "C" Q_DECL_EXPORT
QTimerInfoList *ritual_ZN14QTimerInfoListC1Ev() {
  return new QTimerInfoList();
}

//  std::optional<Duration> QTimerInfoList::timerWait()
extern "C" Q_DECL_EXPORT
std::optional<QTimerInfoList::Duration> *ritual_ZN14QTimerInfoList9timerWaitEv(
    QTimerInfoList *self) {
  return new std::optional<QTimerInfoList::Duration>(self->timerWait());
}

//  void QTimerInfoList::timerInsert(QTimerInfo *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoList11timerInsertEP10QTimerInfo(
    QTimerInfoList *self,
    QTimerInfo *a0) {
  self->timerInsert(a0);
}

//  Duration QTimerInfoList::remainingDuration(Qt::TimerId timerId) const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK14QTimerInfoList17remainingDurationEN2Qt7TimerIdE(
    const QTimerInfoList *self,
    Qt::TimerId timerId) {
  return static_cast<long long>(self->remainingDuration(timerId).count());
}

//  void QTimerInfoList::registerTimer(Qt::TimerId timerId, Duration
//      interval, Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoList13registerTimerEN2Qt7TimerIdENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEENS0_9TimerTypeEP7QObject(
    QTimerInfoList *self,
    Qt::TimerId timerId,
    long long interval,
    Qt::TimerType timerType,
    QObject *object) {
  self->registerTimer(
      timerId,
      QTimerInfoList::Duration(interval),
      timerType,
      object);
}

//  bool QTimerInfoList::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTimerInfoList15unregisterTimerEN2Qt7TimerIdE(
    QTimerInfoList *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QTimerInfoList::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTimerInfoList16unregisterTimersEP7QObject(
    QTimerInfoList *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  QList<TimerInfo> QTimerInfoList::registeredTimers(QObject *object) const
extern "C" Q_DECL_EXPORT
QList<QTimerInfoList::TimerInfo> *ritual_ZNK14QTimerInfoList16registeredTimersEP7QObject(
    const QTimerInfoList *self,
    QObject *object) {
  return new QList<QTimerInfoList::TimerInfo>(
      self->registeredTimers(
          object));
}

//  int QTimerInfoList::activateTimers()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QTimerInfoList14activateTimersEv(QTimerInfoList *self) {
  return self->activateTimers();
}

//  bool QTimerInfoList::hasPendingTimers()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTimerInfoList16hasPendingTimersEv(QTimerInfoList *self) {
  return self->hasPendingTimers();
}

//  void QTimerInfoList::clearTimers()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoList11clearTimersEv(QTimerInfoList *self) {
  self->clearTimers();
}

//  bool QTimerInfoList::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTimerInfoList7isEmptyEv(const QTimerInfoList *self) {
  return self->isEmpty();
}

//  qsizetype QTimerInfoList::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QTimerInfoList4sizeEv(const QTimerInfoList *self) {
  return self->size();
}

//  QList<QTimerInfo *>::const_iterator
//      QTimerInfoList::findTimerById(Qt::TimerId timerId) const
extern "C" Q_DECL_EXPORT
QList<QTimerInfo *>::const_iterator *ritual_ZNK14QTimerInfoList13findTimerByIdEN2Qt7TimerIdE(
    const QTimerInfoList *self,
    Qt::TimerId timerId) {
  return new QList<QTimerInfo *>::const_iterator(
      self->findTimerById(
          timerId));
}

//  std::chrono::steady_clock::time_point QTimerInfoList::updateCurrentTime()
//      const
extern "C" Q_DECL_EXPORT
std::chrono::steady_clock::time_point *ritual_ZNK14QTimerInfoList17updateCurrentTimeEv(
    const QTimerInfoList *self) {
  return new std::chrono::steady_clock::time_point(
      self->updateCurrentTime());
}

//  QTimerInfoList::~QTimerInfoList()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoListD1Ev(QTimerInfoList *self) {
  delete self;
}

//  a std::optional<QTimerInfoList::Duration> a ritual of QTimerInfoList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimerInfoList__std_optional_QTimerInfoList_Duration(
    std::optional<QTimerInfoList::Duration> *self) {
  delete self;
}

//  a QList<QTimerInfoList::TimerInfo> a ritual of QTimerInfoList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimerInfoList__QList_QTimerInfoList_TimerInfo(
    QList<QTimerInfoList::TimerInfo> *self) {
  delete self;
}

//  a QList<QTimerInfo *>::const_iterator a ritual of QTimerInfoList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimerInfoList__QList_QTimerInfo_const_iterator(
    QList<QTimerInfo *>::const_iterator *self) {
  delete self;
}

//  a std::chrono::steady_clock::time_point a ritual of QTimerInfoList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimerInfoList__std_chrono_steady_clock_time_point(
    std::chrono::steady_clock::time_point *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX)
