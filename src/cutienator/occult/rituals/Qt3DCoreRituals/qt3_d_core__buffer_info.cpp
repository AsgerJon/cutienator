//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/bufferutils_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/bufferutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::BufferInfo::BufferInfo()
extern "C" Q_DECL_EXPORT
Qt3DCore::BufferInfo *ritual_ZN8Qt3DCore10BufferInfoC1Ev() {
  return new Qt3DCore::BufferInfo();
}

//  Qt3DCore::BufferInfo::~BufferInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10BufferInfoD1Ev(Qt3DCore::BufferInfo *self) {
  delete self;
}
