//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearray.h>

//  bool QByteArray::FromBase64Result::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray16FromBase64ResultcvbEv(
    const QByteArray::FromBase64Result *self) {
  return self->operator bool();
}

//  const QByteArray &QByteArray::FromBase64Result::operator*() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray16FromBase64ResultdeEv(
    const QByteArray::FromBase64Result *self) {
  return new QByteArray(self->operator*());
}

//  QByteArray::FromBase64Result::~FromBase64Result()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray16FromBase64ResultD1Ev(
    QByteArray::FromBase64Result *self) {
  delete self;
}
