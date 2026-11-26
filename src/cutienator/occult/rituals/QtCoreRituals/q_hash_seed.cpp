//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qhashfunctions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qhashfunctions.h>

//  QHashSeed::QHashSeed(size_t d)
extern "C" Q_DECL_EXPORT
QHashSeed *ritual_ZN9QHashSeedC1Em(size_t d) {
  return new QHashSeed(d);
}

//  size_t QHashSeed::operator unsigned long() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK9QHashSeedcvmEv(const QHashSeed *self) {
  return self->operator size_t();
}

//  QHashSeed QHashSeed::globalSeed()
extern "C" Q_DECL_EXPORT
QHashSeed *ritual_ZN9QHashSeed10globalSeedEv() {
  return new QHashSeed(QHashSeed::globalSeed());
}

//  void QHashSeed::setDeterministicGlobalSeed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHashSeed26setDeterministicGlobalSeedEv() {
  QHashSeed::setDeterministicGlobalSeed();
}

//  void QHashSeed::resetRandomGlobalSeed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHashSeed21resetRandomGlobalSeedEv() {
  QHashSeed::resetRandomGlobalSeed();
}

//  QHashSeed::~QHashSeed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QHashSeedD1Ev(QHashSeed *self) {
  delete self;
}
