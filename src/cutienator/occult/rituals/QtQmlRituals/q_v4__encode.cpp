//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Encode::undefined()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Encode9undefinedEv() {
  return QV4::Encode::undefined();
}

//  ReturnedValue QV4::Encode::null()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Encode4nullEv() {
  return QV4::Encode::null();
}

//  QV4::Encode::Encode(bool b)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1Eb(bool b) {
  return new QV4::Encode(b);
}

//  QV4::Encode::Encode(double d)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1Ed(double d) {
  return new QV4::Encode(d);
}

//  QV4::Encode::Encode(int i)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1Ei(int i) {
  return new QV4::Encode(i);
}

//  QV4::Encode::Encode(uint i)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1Ej(uint i) {
  return new QV4::Encode(i);
}

//  QV4::Encode::Encode(ReturnedValue v)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1Ey(QV4::ReturnedValue v) {
  return new QV4::Encode(v);
}

//  QV4::Encode::Encode(StaticValue v)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1ENS_11StaticValueE(
    const QV4::StaticValue *v) {
  return new QV4::Encode(*v);
}

//  QV4::Encode::Encode(StaticValue *o)
extern "C" Q_DECL_EXPORT
QV4::Encode *ritual_ZN3QV46EncodeC1EPNS_11StaticValueE(QV4::StaticValue *o) {
  return new QV4::Encode(o);
}

//  ReturnedValue QV4::Encode::smallestNumber(double d)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Encode14smallestNumberEd(double d) {
  return QV4::Encode::smallestNumber(d);
}

//  ReturnedValue QV4::Encode::operator unsigned long long() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46EncodecvyEv(const QV4::Encode *self) {
  return self->operator QV4::ReturnedValue();
}

//  QV4::Encode::~Encode()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46EncodeD1Ev(QV4::Encode *self) {
  delete self;
}
