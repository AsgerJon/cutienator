//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QObjectPrivate::Connection::Connection()
extern "C" Q_DECL_EXPORT
QObjectPrivate::Connection *ritual_ZN14QObjectPrivate10ConnectionC1Ev() {
  return new QObjectPrivate::Connection();
}

//  int QObjectPrivate::Connection::method() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QObjectPrivate10Connection6methodEv(
    const QObjectPrivate::Connection *self) {
  return self->method();
}

//  void QObjectPrivate::Connection::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate10Connection3refEv(
    QObjectPrivate::Connection *self) {
  self->ref();
}

//  void QObjectPrivate::Connection::freeSlotObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate10Connection14freeSlotObjectEv(
    QObjectPrivate::Connection *self) {
  self->freeSlotObject();
}
