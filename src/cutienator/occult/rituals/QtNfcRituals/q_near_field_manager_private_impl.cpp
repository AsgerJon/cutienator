//  Written by hand on 2026-11-25 from
//  QtNfc/6.12.0/QtNfc/private/qnearfieldmanager_pcsc_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it, and that of Linux alike.
//  Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, 'tr', the slots 'onCardInserted'
//  and 'onTargetLost', and the signals.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/qtnfc-config.h>
#if QT_CONFIG(pcsclite)
#include <QtNfc/6.12.0/QtNfc/private/qnearfieldmanager_pcsc_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QNearFieldManagerPrivateImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QNearFieldManagerPrivateImpl10metaObjectEv(
    const QNearFieldManagerPrivateImpl *self) {
  return self->metaObject();
}

//  QNearFieldManagerPrivateImpl::~QNearFieldManagerPrivateImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNearFieldManagerPrivateImplD1Ev(
    QNearFieldManagerPrivateImpl *self) {
  delete self;
}

//  bool QNearFieldManagerPrivateImpl::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QNearFieldManagerPrivateImpl9isEnabledEv(
    const QNearFieldManagerPrivateImpl *self) {
  return self->isEnabled();
}

//  bool
//      QNearFieldManagerPrivateImpl::isSupported(QNearFieldTarget::AccessMet
//      hod accessMethod) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QNearFieldManagerPrivateImpl11isSupportedEN16QNearFieldTarget12AccessMethodE(
    const QNearFieldManagerPrivateImpl *self,
    QNearFieldTarget::AccessMethod accessMethod) {
  return self->isSupported(accessMethod);
}

//  bool QNearFieldManagerPrivateImpl::startTargetDetection(QNearFieldTarget:
//      :AccessMethod accessMethod)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QNearFieldManagerPrivateImpl20startTargetDetectionEN16QNearFieldTarget12AccessMethodE(
    QNearFieldManagerPrivateImpl *self,
    QNearFieldTarget::AccessMethod accessMethod) {
  return self->startTargetDetection(accessMethod);
}

//  void QNearFieldManagerPrivateImpl::stopTargetDetection(const QString
//      &errorMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNearFieldManagerPrivateImpl19stopTargetDetectionERK7QString(
    QNearFieldManagerPrivateImpl *self,
    const QString *errorMessage) {
  self->stopTargetDetection(*errorMessage);
}

#endif  // QT_CONFIG(pcsclite)
