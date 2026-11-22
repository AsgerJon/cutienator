//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbitarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbitarray.h>

//  bool QBitRef::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBitRefcvbEv(const QBitRef *self) {
  return self->operator bool();
}

//  bool QBitRef::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBitRefntEv(const QBitRef *self) {
  return self->operator!();
}

//  QBitRef::~QBitRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitRefD1Ev(QBitRef *self) {
  delete self;
}
