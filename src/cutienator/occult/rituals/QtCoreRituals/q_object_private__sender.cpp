//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QObjectPrivate::Sender::Sender(QObject *receiver, QObject *sender, int
//      signal, ConnectionData *receiverConnections)
extern "C" Q_DECL_EXPORT
QObjectPrivate::Sender *ritual_ZN14QObjectPrivate6SenderC1EP7QObjectS2_iPNS_14ConnectionDataE(
    QObject *receiver,
    QObject *sender,
    int signal,
    QObjectPrivate::ConnectionData *receiverConnections) {
  return new QObjectPrivate::Sender(
      receiver,
      sender,
      signal,
      receiverConnections);
}

//  QObjectPrivate::Sender::~Sender()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate6SenderD1Ev(QObjectPrivate::Sender *self) {
  delete self;
}

//  void QObjectPrivate::Sender::receiverDeleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate6Sender15receiverDeletedEv(
    QObjectPrivate::Sender *self) {
  self->receiverDeleted();
}
