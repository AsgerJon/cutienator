//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  quint64 HPack::BitIStream::streamOffset() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream12streamOffsetEv(
    const HPack::BitIStream *self) {
  return self->streamOffset();
}

//  HPack::BitIStream::~BitIStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitIStreamD1Ev(HPack::BitIStream *self) {
  delete self;
}
