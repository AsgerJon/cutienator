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

//  QTimerInfoList::QTimerInfoList()
extern "C" Q_DECL_EXPORT
QTimerInfoList *ritual_ZN14QTimerInfoListC1Ev() {
  return new QTimerInfoList();
}

//  void QTimerInfoList::timerInsert(QTimerInfo *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoList11timerInsertEP10QTimerInfo(
    QTimerInfoList *self,
    QTimerInfo *a0) {
  self->timerInsert(a0);
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

//  QTimerInfoList::~QTimerInfoList()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTimerInfoListD1Ev(QTimerInfoList *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX)
