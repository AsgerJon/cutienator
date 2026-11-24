//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qgeometryview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qgeometryview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  Qt3DCore::BoundingVolumeCalculator::BoundingVolumeCalculator()
extern "C" Q_DECL_EXPORT
Qt3DCore::BoundingVolumeCalculator *ritual_ZN8Qt3DCore24BoundingVolumeCalculatorC1Ev() {
  return new Qt3DCore::BoundingVolumeCalculator();
}

//  const QVector3D Qt3DCore::BoundingVolumeCalculator::min() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore24BoundingVolumeCalculator3minEv(
    const Qt3DCore::BoundingVolumeCalculator *self) {
  return new QVector3D(self->min());
}

//  const QVector3D Qt3DCore::BoundingVolumeCalculator::max() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore24BoundingVolumeCalculator3maxEv(
    const Qt3DCore::BoundingVolumeCalculator *self) {
  return new QVector3D(self->max());
}

//  const QVector3D Qt3DCore::BoundingVolumeCalculator::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore24BoundingVolumeCalculator6centerEv(
    const Qt3DCore::BoundingVolumeCalculator *self) {
  return new QVector3D(self->center());
}

//  float Qt3DCore::BoundingVolumeCalculator::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore24BoundingVolumeCalculator6radiusEv(
    const Qt3DCore::BoundingVolumeCalculator *self) {
  return self->radius();
}

//  bool Qt3DCore::BoundingVolumeCalculator::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore24BoundingVolumeCalculator7isValidEv(
    const Qt3DCore::BoundingVolumeCalculator *self) {
  return self->isValid();
}

//  Qt3DCore::BoundingVolumeCalculator::~BoundingVolumeCalculator()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore24BoundingVolumeCalculatorD1Ev(
    Qt3DCore::BoundingVolumeCalculator *self) {
  delete self;
}
