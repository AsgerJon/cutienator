//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool Qt3DCore::BoundingVolumeComputeData::valid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore25BoundingVolumeComputeData5validEv(
    const Qt3DCore::BoundingVolumeComputeData *self) {
  return self->valid();
}

//  Qt3DCore::BoundingVolumeComputeData::~BoundingVolumeComputeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25BoundingVolumeComputeDataD1Ev(
    Qt3DCore::BoundingVolumeComputeData *self) {
  delete self;
}
