//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qresourcemanager_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qresourcemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void *Qt3DCore::AlignedAllocator::allocate(uint size)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore16AlignedAllocator8allocateEj(uint size) {
  return Qt3DCore::AlignedAllocator::allocate(size);
}

//  void Qt3DCore::AlignedAllocator::release(void *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16AlignedAllocator7releaseEPv(void *p) {
  Qt3DCore::AlignedAllocator::release(p);
}

//  Qt3DCore::AlignedAllocator::~AlignedAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16AlignedAllocatorD1Ev(
    Qt3DCore::AlignedAllocator *self) {
  delete self;
}
