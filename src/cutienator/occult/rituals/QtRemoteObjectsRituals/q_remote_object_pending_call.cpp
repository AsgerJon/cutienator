//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectpendingcall.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qvariant.h>

//  QRemoteObjectPendingCall::QRemoteObjectPendingCall()
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN24QRemoteObjectPendingCallC1Ev() {
  return new QRemoteObjectPendingCall();
}

//  QRemoteObjectPendingCall::QRemoteObjectPendingCall(const
//      QRemoteObjectPendingCall &other)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN24QRemoteObjectPendingCallC1ERKS_(
    const QRemoteObjectPendingCall *other) {
  return new QRemoteObjectPendingCall(*other);
}

//  QRemoteObjectPendingCall::~QRemoteObjectPendingCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectPendingCallD1Ev(
    QRemoteObjectPendingCall *self) {
  delete self;
}

//  QRemoteObjectPendingCall &QRemoteObjectPendingCall::operator=(const
//      QRemoteObjectPendingCall &other)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN24QRemoteObjectPendingCallaSERKS_(
    QRemoteObjectPendingCall *self,
    const QRemoteObjectPendingCall *other) {
  return &(self->operator=(*other));
}

//  QVariant QRemoteObjectPendingCall::returnValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QRemoteObjectPendingCall11returnValueEv(
    const QRemoteObjectPendingCall *self) {
  return new QVariant(self->returnValue());
}

//  QRemoteObjectPendingCall::Error QRemoteObjectPendingCall::error() const
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall::Error ritual_ZNK24QRemoteObjectPendingCall5errorEv(
    const QRemoteObjectPendingCall *self) {
  return self->error();
}

//  bool QRemoteObjectPendingCall::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QRemoteObjectPendingCall10isFinishedEv(
    const QRemoteObjectPendingCall *self) {
  return self->isFinished();
}

//  bool QRemoteObjectPendingCall::waitForFinished(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QRemoteObjectPendingCall15waitForFinishedEi(
    QRemoteObjectPendingCall *self,
    int timeout) {
  return self->waitForFinished(timeout);
}

//  QRemoteObjectPendingCall
//      QRemoteObjectPendingCall::fromCompletedCall(const QVariant
//      &returnValue)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN24QRemoteObjectPendingCall17fromCompletedCallERK8QVariant(
    const QVariant *returnValue) {
  return new QRemoteObjectPendingCall(
      QRemoteObjectPendingCall::fromCompletedCall(
          *returnValue));
}

//  QRemoteObjectPendingCall::QRemoteObjectPendingCall(QRemoteObjectPendingCa
//      llData *dd)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN24QRemoteObjectPendingCallC1EP28QRemoteObjectPendingCallData(
    QRemoteObjectPendingCallData *dd) {
  return new QRemoteObjectPendingCall(dd);
}
