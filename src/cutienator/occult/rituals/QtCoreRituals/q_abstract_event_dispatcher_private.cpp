//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstracteventdispatcher_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstracteventdispatcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstractEventDispatcher *QAbstractEventDispatcherPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN31QAbstractEventDispatcherPrivate6q_funcEv(
    QAbstractEventDispatcherPrivate *self) {
  return self->q_func();
}

//  const QAbstractEventDispatcher *QAbstractEventDispatcherPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractEventDispatcher *ritual_ZNK31QAbstractEventDispatcherPrivate6q_funcEv(
    const QAbstractEventDispatcherPrivate *self) {
  return self->q_func();
}

//  QAbstractEventDispatcherPrivate::QAbstractEventDispatcherPrivate()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcherPrivate *ritual_ZN31QAbstractEventDispatcherPrivateC1Ev() {
  return new QAbstractEventDispatcherPrivate();
}

//  QAbstractEventDispatcherPrivate::~QAbstractEventDispatcherPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractEventDispatcherPrivateD1Ev(
    QAbstractEventDispatcherPrivate *self) {
  delete self;
}

//  Qt::TimerId QAbstractEventDispatcherPrivate::allocateTimerId()
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZN31QAbstractEventDispatcherPrivate15allocateTimerIdEv() {
  return QAbstractEventDispatcherPrivate::allocateTimerId();
}

//  void QAbstractEventDispatcherPrivate::releaseTimerId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractEventDispatcherPrivate14releaseTimerIdEi(int id) {
  QAbstractEventDispatcherPrivate::releaseTimerId(id);
}

//  void QAbstractEventDispatcherPrivate::releaseTimerId(Qt::TimerId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAbstractEventDispatcherPrivate14releaseTimerIdEN2Qt7TimerIdE(
    Qt::TimerId id) {
  QAbstractEventDispatcherPrivate::releaseTimerId(id);
}

//  QAbstractEventDispatcherPrivate
//      *QAbstractEventDispatcherPrivate::get(QAbstractEventDispatcher *o)
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcherPrivate *ritual_ZN31QAbstractEventDispatcherPrivate3getEP24QAbstractEventDispatcher(
    QAbstractEventDispatcher *o) {
  return QAbstractEventDispatcherPrivate::get(o);
}

//  const QAbstractEventDispatcherPrivate
//      *QAbstractEventDispatcherPrivate::get(const QAbstractEventDispatcher
//      *o)
extern "C" Q_DECL_EXPORT
const QAbstractEventDispatcherPrivate *ritual_ZN31QAbstractEventDispatcherPrivate3getEPK24QAbstractEventDispatcher(
    const QAbstractEventDispatcher *o) {
  return QAbstractEventDispatcherPrivate::get(o);
}
