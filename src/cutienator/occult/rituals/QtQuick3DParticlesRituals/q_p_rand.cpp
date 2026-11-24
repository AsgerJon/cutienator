//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerandomizer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerandomizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrandom.h>

//  void QPRand::init(quint32 seed, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPRand4initEji(QPRand *self, quint32 seed, int size) {
  self->init(seed, size);
}

//  void QPRand::setDeterministic(bool deterministic)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPRand16setDeterministicEb(QPRand *self, bool deterministic) {
  self->setDeterministic(deterministic);
}

//  float QPRand::get(int particleIndex, UserType user)
extern "C" Q_DECL_EXPORT
float ritual_ZN6QPRand3getEiNS_8UserTypeE(
    QPRand *self,
    int particleIndex,
    QPRand::UserType user) {
  return self->get(particleIndex, user);
}

//  float QPRand::get()
extern "C" Q_DECL_EXPORT
float ritual_ZN6QPRand3getEv(QPRand *self) {
  return self->get();
}

//  QRandomGenerator QPRand::generator() const
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZNK6QPRand9generatorEv(const QPRand *self) {
  return new QRandomGenerator(self->generator());
}

//  QPRand::~QPRand()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPRandD1Ev(QPRand *self) {
  delete self;
}
