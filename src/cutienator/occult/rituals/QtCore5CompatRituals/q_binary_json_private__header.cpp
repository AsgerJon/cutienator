//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Base *QBinaryJsonPrivate::Header::root()
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Base *ritual_ZN18QBinaryJsonPrivate6Header4rootEv(
    QBinaryJsonPrivate::Header *self) {
  return self->root();
}

//  const Base *QBinaryJsonPrivate::Header::root() const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Base *ritual_ZNK18QBinaryJsonPrivate6Header4rootEv(
    const QBinaryJsonPrivate::Header *self) {
  return self->root();
}

//  QBinaryJsonPrivate::Header::~Header()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6HeaderD1Ev(
    QBinaryJsonPrivate::Header *self) {
  delete self;
}
