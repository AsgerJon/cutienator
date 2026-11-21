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

//  QFlag::QFlag(uint value)
extern "C" Q_DECL_EXPORT
QFlag *ritual_ZN5QFlagC1Ej(uint value) {
  return new QFlag(value);
}

//  QFlag::QFlag(short value)
extern "C" Q_DECL_EXPORT
QFlag *ritual_ZN5QFlagC1Es(short value) {
  return new QFlag(value);
}

//  QFlag::QFlag(ushort value)
extern "C" Q_DECL_EXPORT
QFlag *ritual_ZN5QFlagC1Et(ushort value) {
  return new QFlag(value);
}

//  uint QFlag::operator unsigned int() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK5QFlagcvjEv(const QFlag *self) {
  return self->operator uint();
}

//  QFlag::~QFlag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFlagD1Ev(QFlag *self) {
  delete self;
}
