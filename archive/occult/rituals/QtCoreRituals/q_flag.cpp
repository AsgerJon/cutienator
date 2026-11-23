//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qflags.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qflags.h>

//  QFlag::QFlag(int value)
extern "C" Q_DECL_EXPORT
QFlag *ritual_ZN5QFlagC1Ei(int value) {
  return new QFlag(value);
}

//  int QFlag::operator int() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFlagcviEv(const QFlag *self) {
  return self->operator int();
}

//  QFlag::~QFlag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFlagD1Ev(QFlag *self) {
  delete self;
}
