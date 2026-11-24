//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsnumbercoercion.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjsnumbercoercion.h>

//  bool QJSNumberCoercion::isInteger(double d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QJSNumberCoercion9isIntegerEd(double d) {
  return QJSNumberCoercion::isInteger(d);
}

//  bool QJSNumberCoercion::isArrayIndex(double d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QJSNumberCoercion12isArrayIndexEd(double d) {
  return QJSNumberCoercion::isArrayIndex(d);
}

//  bool QJSNumberCoercion::isArrayIndex(qint64 i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QJSNumberCoercion12isArrayIndexEx(qint64 i) {
  return QJSNumberCoercion::isArrayIndex(i);
}

//  bool QJSNumberCoercion::isArrayIndex(quint64 i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QJSNumberCoercion12isArrayIndexEy(quint64 i) {
  return QJSNumberCoercion::isArrayIndex(i);
}

//  int QJSNumberCoercion::toInteger(double d)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QJSNumberCoercion9toIntegerEd(double d) {
  return QJSNumberCoercion::toInteger(d);
}

//  bool QJSNumberCoercion::equals(double lhs, double rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QJSNumberCoercion6equalsEdd(double lhs, double rhs) {
  return QJSNumberCoercion::equals(lhs, rhs);
}

//  double QJSNumberCoercion::roundTowards0(double d)
extern "C" Q_DECL_EXPORT
double ritual_ZN17QJSNumberCoercion13roundTowards0Ed(double d) {
  return QJSNumberCoercion::roundTowards0(d);
}

//  QJSNumberCoercion::QJSNumberCoercion(double dbl)
extern "C" Q_DECL_EXPORT
QJSNumberCoercion *ritual_ZN17QJSNumberCoercionC1Ed(double dbl) {
  return new QJSNumberCoercion(dbl);
}

//  int QJSNumberCoercion::sign() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QJSNumberCoercion4signEv(const QJSNumberCoercion *self) {
  return self->sign();
}

//  bool QJSNumberCoercion::isDenormal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSNumberCoercion10isDenormalEv(
    const QJSNumberCoercion *self) {
  return self->isDenormal();
}

//  int QJSNumberCoercion::exponent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QJSNumberCoercion8exponentEv(const QJSNumberCoercion *self) {
  return self->exponent();
}

//  quint64 QJSNumberCoercion::significant() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QJSNumberCoercion11significantEv(
    const QJSNumberCoercion *self) {
  return self->significant();
}

//  int QJSNumberCoercion::toInteger()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QJSNumberCoercion9toIntegerEv(QJSNumberCoercion *self) {
  return self->toInteger();
}

//  QJSNumberCoercion::~QJSNumberCoercion()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QJSNumberCoercionD1Ev(QJSNumberCoercion *self) {
  delete self;
}
