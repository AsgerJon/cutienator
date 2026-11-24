//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/hpacktable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/hpacktable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  HPack::HeaderField::HeaderField()
extern "C" Q_DECL_EXPORT
HPack::HeaderField *ritual_ZN5HPack11HeaderFieldC1Ev() {
  return new HPack::HeaderField();
}

//  HPack::HeaderField::HeaderField(const QByteArray &n, const QByteArray &v)
extern "C" Q_DECL_EXPORT
HPack::HeaderField *ritual_ZN5HPack11HeaderFieldC1ERK10QByteArrayS3_(
    const QByteArray *n,
    const QByteArray *v) {
  return new HPack::HeaderField(*n, *v);
}

//  bool HPack::HeaderField::operator==(const HeaderField &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack11HeaderFieldeqERKS0_(
    const HPack::HeaderField *self,
    const HPack::HeaderField *rhs) {
  return self->operator==(*rhs);
}

//  HPack::HeaderField::~HeaderField()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack11HeaderFieldD1Ev(HPack::HeaderField *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
