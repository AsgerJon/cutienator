//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Entry *QBinaryJsonPrivate::Object::entryAt(uint i) const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Entry *ritual_ZNK18QBinaryJsonPrivate6Object7entryAtEj(
    const QBinaryJsonPrivate::Object *self,
    uint i) {
  return self->entryAt(i);
}

//  Entry *QBinaryJsonPrivate::Object::entryAt(uint i)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Entry *ritual_ZN18QBinaryJsonPrivate6Object7entryAtEj(
    QBinaryJsonPrivate::Object *self,
    uint i) {
  return self->entryAt(i);
}

//  QBinaryJsonPrivate::Object::~Object()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6ObjectD1Ev(
    QBinaryJsonPrivate::Object *self) {
  delete self;
}
