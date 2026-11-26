//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbitarray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbitarray.h>

//  QBitRef::QBitRef(QBitArray &array, qsizetype idx)
extern "C" Q_DECL_EXPORT
QBitRef *ritual_ZN7QBitRefC1ER9QBitArrayx(QBitArray *array, qsizetype idx) {
  return new QBitRef(*array, idx);
}

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

//  QBitRef &QBitRef::operator=(const QBitRef &val)
extern "C" Q_DECL_EXPORT
QBitRef *ritual_ZN7QBitRefaSERKS_(QBitRef *self, const QBitRef *val) {
  return &(self->operator=(*val));
}

//  QBitRef &QBitRef::operator=(bool val)
extern "C" Q_DECL_EXPORT
QBitRef *ritual_ZN7QBitRefaSEb(QBitRef *self, bool val) {
  return &(self->operator=(val));
}

//  QBitRef::~QBitRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitRefD1Ev(QBitRef *self) {
  delete self;
}
