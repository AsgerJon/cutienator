//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlnotifierendpoint_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlnotifierendpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlNotifierEndpoint::QQmlNotifierEndpoint(Callback callback)
extern "C" Q_DECL_EXPORT
QQmlNotifierEndpoint *ritual_ZN20QQmlNotifierEndpointC1ENS_8CallbackE(
    QQmlNotifierEndpoint::Callback callback) {
  return new QQmlNotifierEndpoint(callback);
}

//  QQmlNotifierEndpoint::~QQmlNotifierEndpoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpointD1Ev(QQmlNotifierEndpoint *self) {
  delete self;
}

//  bool QQmlNotifierEndpoint::isConnected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlNotifierEndpoint11isConnectedEv(
    const QQmlNotifierEndpoint *self) {
  return self->isConnected();
}

//  bool QQmlNotifierEndpoint::isConnected(QObject *source, int sourceSignal)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlNotifierEndpoint11isConnectedEP7QObjecti(
    const QQmlNotifierEndpoint *self,
    QObject *source,
    int sourceSignal) {
  return self->isConnected(source, sourceSignal);
}

//  bool QQmlNotifierEndpoint::isConnected(QQmlNotifier *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlNotifierEndpoint11isConnectedEP12QQmlNotifier(
    const QQmlNotifierEndpoint *self,
    QQmlNotifier *a0) {
  return self->isConnected(a0);
}

//  void QQmlNotifierEndpoint::disconnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpoint10disconnectEv(
    QQmlNotifierEndpoint *self) {
  self->disconnect();
}

//  bool QQmlNotifierEndpoint::isNotifying() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlNotifierEndpoint11isNotifyingEv(
    const QQmlNotifierEndpoint *self) {
  return self->isNotifying();
}

//  void QQmlNotifierEndpoint::startNotifying(qintptr *originalSenderPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpoint14startNotifyingEPx(
    QQmlNotifierEndpoint *self,
    qintptr *originalSenderPtr) {
  self->startNotifying(originalSenderPtr);
}

//  void QQmlNotifierEndpoint::stopNotifying(qintptr *originalSenderPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpoint13stopNotifyingEPx(
    QQmlNotifierEndpoint *self,
    qintptr *originalSenderPtr) {
  self->stopNotifying(originalSenderPtr);
}

//  void QQmlNotifierEndpoint::cancelNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpoint12cancelNotifyEv(
    QQmlNotifierEndpoint *self) {
  self->cancelNotify();
}

//  int QQmlNotifierEndpoint::signalIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlNotifierEndpoint11signalIndexEv(
    const QQmlNotifierEndpoint *self) {
  return self->signalIndex();
}

//  Callback QQmlNotifierEndpoint::callbackType() const
extern "C" Q_DECL_EXPORT
QQmlNotifierEndpoint::Callback ritual_ZNK20QQmlNotifierEndpoint12callbackTypeEv(
    const QQmlNotifierEndpoint *self) {
  return self->callbackType();
}

//  QQmlNotifierEndpoint *QQmlNotifierEndpoint::nextEndpoint() const
extern "C" Q_DECL_EXPORT
QQmlNotifierEndpoint *ritual_ZNK20QQmlNotifierEndpoint12nextEndpointEv(
    const QQmlNotifierEndpoint *self) {
  return self->nextEndpoint();
}

//  qintptr QQmlNotifierEndpoint::sender() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK20QQmlNotifierEndpoint6senderEv(
    const QQmlNotifierEndpoint *self) {
  return self->sender();
}

//  void QQmlNotifierEndpoint::setSender(qintptr sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlNotifierEndpoint9setSenderEx(
    QQmlNotifierEndpoint *self,
    qintptr sender) {
  self->setSender(sender);
}

//  QObject *QQmlNotifierEndpoint::senderAsObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QQmlNotifierEndpoint14senderAsObjectEv(
    const QQmlNotifierEndpoint *self) {
  return self->senderAsObject();
}

//  QQmlNotifier *QQmlNotifierEndpoint::senderAsNotifier() const
extern "C" Q_DECL_EXPORT
QQmlNotifier *ritual_ZNK20QQmlNotifierEndpoint16senderAsNotifierEv(
    const QQmlNotifierEndpoint *self) {
  return self->senderAsNotifier();
}
