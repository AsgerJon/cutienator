//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qatomic.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qatomic.h>

//  QAtomicInt::QAtomicInt(int value)
extern "C" Q_DECL_EXPORT
QAtomicInt *ritual_ZN10QAtomicIntC1Ei(int value) {
  return new QAtomicInt(value);
}

//  QAtomicInt::~QAtomicInt()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAtomicIntD1Ev(QAtomicInt *self) {
  delete self;
}
