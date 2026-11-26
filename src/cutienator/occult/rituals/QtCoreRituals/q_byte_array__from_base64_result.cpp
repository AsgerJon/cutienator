//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearray.h>

//  void QByteArray::FromBase64Result::swap(QByteArray::FromBase64Result
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray16FromBase64Result4swapERS0_(
    QByteArray::FromBase64Result *self,
    QByteArray::FromBase64Result *other) {
  self->swap(*other);
}

//  bool QByteArray::FromBase64Result::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray16FromBase64ResultcvbEv(
    const QByteArray::FromBase64Result *self) {
  return self->operator bool();
}

//  QByteArray &QByteArray::FromBase64Result::operator*()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNR10QByteArray16FromBase64ResultdeEv(
    QByteArray::FromBase64Result *self) {
  return &(self->operator*());
}

//  const QByteArray &QByteArray::FromBase64Result::operator*() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray16FromBase64ResultdeEv(
    const QByteArray::FromBase64Result *self) {
  return new QByteArray(self->operator*());
}

//  bool operator==(const QByteArray::FromBase64Result &lhs, const
//      QByteArray::FromBase64Result &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN10QByteArray16FromBase64ResultES2_(
    const QByteArray::FromBase64Result *lhs,
    const QByteArray::FromBase64Result *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QByteArray::FromBase64Result &lhs, const
//      QByteArray::FromBase64Result &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN10QByteArray16FromBase64ResultES2_(
    const QByteArray::FromBase64Result *lhs,
    const QByteArray::FromBase64Result *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QByteArray::FromBase64Result::~FromBase64Result()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray16FromBase64ResultD1Ev(
    QByteArray::FromBase64Result *self) {
  delete self;
}
