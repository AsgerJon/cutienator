//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::JobId::JobId()
extern "C" Q_DECL_EXPORT
Qt3DCore::JobId *ritual_ZN8Qt3DCore5JobIdC1Ev() {
  return new Qt3DCore::JobId();
}

//  Qt3DCore::JobId::JobId(quint32 t, quint32 i)
extern "C" Q_DECL_EXPORT
Qt3DCore::JobId *ritual_ZN8Qt3DCore5JobIdC1Ejj(quint32 t, quint32 i) {
  return new Qt3DCore::JobId(t, i);
}

//  Qt3DCore::JobId::~JobId()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5JobIdD1Ev(Qt3DCore::JobId *self) {
  delete self;
}
