//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qcolorspace.h>

//  PrimaryPoints QColorSpace::PrimaryPoints::fromPrimaries(Primaries
//      primaries)
extern "C" Q_DECL_EXPORT
QColorSpace::PrimaryPoints *ritual_ZN11QColorSpace13PrimaryPoints13fromPrimariesENS_9PrimariesE(
    QColorSpace::Primaries primaries) {
  return new QColorSpace::PrimaryPoints(
      QColorSpace::PrimaryPoints::fromPrimaries(
          primaries));
}

//  bool QColorSpace::PrimaryPoints::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColorSpace13PrimaryPoints7isValidEv(
    const QColorSpace::PrimaryPoints *self) {
  return self->isValid();
}

//  QColorSpace::PrimaryPoints::~PrimaryPoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace13PrimaryPointsD1Ev(
    QColorSpace::PrimaryPoints *self) {
  delete self;
}
