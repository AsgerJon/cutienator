//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const VTable *QV4::Heap::String::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV44Heap6String6vtableEv(
    const QV4::Heap::String *self) {
  return self->vtable();
}

//  int QV4::Heap::String::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap6String6lengthEv(const QV4::Heap::String *self) {
  return self->length();
}

//  QString QV4::Heap::String::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV44Heap6String9toQStringEv(
    const QV4::Heap::String *self) {
  return new QString(self->toQString());
}

//  bool QV4::Heap::String::isEqualTo(const String *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap6String9isEqualToEPKS1_(
    const QV4::Heap::String *self,
    const QV4::Heap::String *other) {
  return self->isEqualTo(other);
}
