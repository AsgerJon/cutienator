//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/quuid.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/quuid.h>
#include <QtCore/qbytearrayview.h>

//  QByteArrayView QUuid::Id128Bytes::operator QByteArrayView() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK5QUuid10Id128Bytescv14QByteArrayViewEv(
    const QUuid::Id128Bytes *self) {
  return new QByteArrayView(self->operator QByteArrayView());
}

//  QUuid::Id128Bytes::~Id128Bytes()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QUuid10Id128BytesD1Ev(QUuid::Id128Bytes *self) {
  delete self;
}
