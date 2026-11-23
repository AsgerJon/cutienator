//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qflags.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qflags.h>

//  QIncompatibleFlag::QIncompatibleFlag(int i)
extern "C" Q_DECL_EXPORT
QIncompatibleFlag *ritual_ZN17QIncompatibleFlagC1Ei(int i) {
  return new QIncompatibleFlag(i);
}

//  int QIncompatibleFlag::operator int() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QIncompatibleFlagcviEv(const QIncompatibleFlag *self) {
  return self->operator int();
}

//  QIncompatibleFlag::~QIncompatibleFlag()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIncompatibleFlagD1Ev(QIncompatibleFlag *self) {
  delete self;
}
