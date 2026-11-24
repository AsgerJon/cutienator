//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QV4::VTable *QV4::StringOrSymbol::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV414StringOrSymbol12staticVTableEv() {
  return QV4::StringOrSymbol::staticVTable();
}

//  void QV4::StringOrSymbol::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414StringOrSymbol10__dataTestEv(QV4::StringOrSymbol *self) {
  self->__dataTest();
}

//  QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringOrSymbol *ritual_ZNK3QV414StringOrSymbol11d_uncheckedEv(
    const QV4::StringOrSymbol *self) {
  return self->d_unchecked();
}

//  QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringOrSymbol *ritual_ZNK3QV414StringOrSymbol1dEv(
    const QV4::StringOrSymbol *self) {
  return self->d();
}

//  void QV4::StringOrSymbol::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414StringOrSymbol14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::StringOrSymbol::virtualDestroy(b);
}

//  void QV4::StringOrSymbol::createPropertyKey() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV414StringOrSymbol17createPropertyKeyEv(
    const QV4::StringOrSymbol *self) {
  self->createPropertyKey();
}

//  PropertyKey QV4::StringOrSymbol::propertyKey() const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV414StringOrSymbol11propertyKeyEv(
    const QV4::StringOrSymbol *self) {
  return new QV4::PropertyKey(self->propertyKey());
}

//  PropertyKey QV4::StringOrSymbol::toPropertyKey() const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV414StringOrSymbol13toPropertyKeyEv(
    const QV4::StringOrSymbol *self) {
  return new QV4::PropertyKey(self->toPropertyKey());
}

//  QString QV4::StringOrSymbol::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV414StringOrSymbol9toQStringEv(
    const QV4::StringOrSymbol *self) {
  return new QString(self->toQString());
}
