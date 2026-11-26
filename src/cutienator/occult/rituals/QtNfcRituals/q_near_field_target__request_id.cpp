//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qnearfieldtarget.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qnearfieldtarget.h>

//  QNearFieldTarget::RequestId::RequestId()
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget9RequestIdC1Ev() {
  return new QNearFieldTarget::RequestId();
}

//  QNearFieldTarget::RequestId::RequestId(const RequestId &other)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget9RequestIdC1ERKS0_(
    const QNearFieldTarget::RequestId *other) {
  return new QNearFieldTarget::RequestId(*other);
}

//  QNearFieldTarget::RequestId::RequestId(RequestIdPrivate *p)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget9RequestIdC1EPNS_16RequestIdPrivateE(
    QNearFieldTarget::RequestIdPrivate *p) {
  return new QNearFieldTarget::RequestId(p);
}

//  QNearFieldTarget::RequestId::~RequestId()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNearFieldTarget9RequestIdD1Ev(
    QNearFieldTarget::RequestId *self) {
  delete self;
}

//  bool QNearFieldTarget::RequestId::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNearFieldTarget9RequestId7isValidEv(
    const QNearFieldTarget::RequestId *self) {
  return self->isValid();
}

//  int QNearFieldTarget::RequestId::refCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNearFieldTarget9RequestId8refCountEv(
    const QNearFieldTarget::RequestId *self) {
  return self->refCount();
}

//  bool QNearFieldTarget::RequestId::operator<(const RequestId &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNearFieldTarget9RequestIdltERKS0_(
    const QNearFieldTarget::RequestId *self,
    const QNearFieldTarget::RequestId *other) {
  return self->operator<(*other);
}

//  bool QNearFieldTarget::RequestId::operator==(const RequestId &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNearFieldTarget9RequestIdeqERKS0_(
    const QNearFieldTarget::RequestId *self,
    const QNearFieldTarget::RequestId *other) {
  return self->operator==(*other);
}

//  bool QNearFieldTarget::RequestId::operator!=(const RequestId &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QNearFieldTarget9RequestIdneERKS0_(
    const QNearFieldTarget::RequestId *self,
    const QNearFieldTarget::RequestId *other) {
  return self->operator!=(*other);
}

//  RequestId &QNearFieldTarget::RequestId::operator=(const RequestId &other)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget9RequestIdaSERKS0_(
    QNearFieldTarget::RequestId *self,
    const QNearFieldTarget::RequestId *other) {
  return &(self->operator=(*other));
}
