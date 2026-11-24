//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::Heap::StringOrSymbol::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14StringOrSymbol4initEv(
    QV4::Heap::StringOrSymbol *self) {
  self->init();
}

//  QString QV4::Heap::StringOrSymbol::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV44Heap14StringOrSymbol9toQStringEv(
    const QV4::Heap::StringOrSymbol *self) {
  return new QString(self->toQString());
}

//  unsigned int QV4::Heap::StringOrSymbol::hashValue() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK3QV44Heap14StringOrSymbol9hashValueEv(
    const QV4::Heap::StringOrSymbol *self) {
  return self->hashValue();
}
