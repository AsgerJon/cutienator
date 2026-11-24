//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventloop_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qeventloop.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QEventLoop *QEventLoopPrivate::q_func()
extern "C" Q_DECL_EXPORT
QEventLoop *ritual_ZN17QEventLoopPrivate6q_funcEv(QEventLoopPrivate *self) {
  return self->q_func();
}

//  const QEventLoop *QEventLoopPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QEventLoop *ritual_ZNK17QEventLoopPrivate6q_funcEv(
    const QEventLoopPrivate *self) {
  return self->q_func();
}

//  void QEventLoopPrivate::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QEventLoopPrivate3refEv(QEventLoopPrivate *self) {
  self->ref();
}

//  void QEventLoopPrivate::deref()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QEventLoopPrivate5derefEv(QEventLoopPrivate *self) {
  self->deref();
}
