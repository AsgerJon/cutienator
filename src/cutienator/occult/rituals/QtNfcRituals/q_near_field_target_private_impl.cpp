//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_pcsc_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object ('metaObject'
//  included). Qt builds it only with the feature 'pcsclite'.
//  Not written: the constructor and 'tr', the slots and signals, which
//  are not virtual, and 'writeNdefMessages', which takes a 'QList'.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/qtnfc-config.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_pcsc_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QNearFieldTargetPrivateImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QNearFieldTargetPrivateImpl10metaObjectEv(
    const QNearFieldTargetPrivateImpl *self) {
  return self->metaObject();
}

//  QNearFieldTargetPrivateImpl::~QNearFieldTargetPrivateImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QNearFieldTargetPrivateImplD1Ev(
    QNearFieldTargetPrivateImpl *self) {
  delete self;
}

//  QByteArray QNearFieldTargetPrivateImpl::uid() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QNearFieldTargetPrivateImpl3uidEv(
    const QNearFieldTargetPrivateImpl *self) {
  return new QByteArray(self->uid());
}

//  QNearFieldTarget::Type QNearFieldTargetPrivateImpl::type() const
extern "C" Q_DECL_EXPORT
QNearFieldTarget::Type ritual_ZNK27QNearFieldTargetPrivateImpl4typeEv(
    const QNearFieldTargetPrivateImpl *self) {
  return self->type();
}

//  QNearFieldTarget::AccessMethods
//      QNearFieldTargetPrivateImpl::accessMethods() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QNearFieldTargetPrivateImpl13accessMethodsEv(
    const QNearFieldTargetPrivateImpl *self) {
  return static_cast<int>(self->accessMethods().toInt());
}

//  bool QNearFieldTargetPrivateImpl::disconnect()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QNearFieldTargetPrivateImpl10disconnectEv(
    QNearFieldTargetPrivateImpl *self) {
  return self->disconnect();
}

//  int QNearFieldTargetPrivateImpl::maxCommandLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QNearFieldTargetPrivateImpl16maxCommandLengthEv(
    const QNearFieldTargetPrivateImpl *self) {
  return self->maxCommandLength();
}

//  QNearFieldTarget::RequestId
//      QNearFieldTargetPrivateImpl::sendCommand(const QByteArray &command)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN27QNearFieldTargetPrivateImpl11sendCommandERK10QByteArray(
    QNearFieldTargetPrivateImpl *self,
    const QByteArray *command) {
  return new QNearFieldTarget::RequestId(self->sendCommand(*command));
}

//  QNearFieldTarget::RequestId
//      QNearFieldTargetPrivateImpl::readNdefMessages()
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN27QNearFieldTargetPrivateImpl16readNdefMessagesEv(
    QNearFieldTargetPrivateImpl *self) {
  return new QNearFieldTarget::RequestId(self->readNdefMessages());
}

#endif  // QT_CONFIG(pcsclite)
