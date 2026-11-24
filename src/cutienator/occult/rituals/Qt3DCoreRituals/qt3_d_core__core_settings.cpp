//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/coresettings_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/coresettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DCore::CoreSettings::setAspect(QCoreAspect *aspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12CoreSettings9setAspectEPNS_11QCoreAspectE(
    Qt3DCore::CoreSettings *self,
    Qt3DCore::QCoreAspect *aspect) {
  self->setAspect(aspect);
}

//  void Qt3DCore::CoreSettings::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12CoreSettings16syncFromFrontEndEPKNS_5QNodeEb(
    Qt3DCore::CoreSettings *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DCore::CoreSettings::syncFromFrontEnd(frontEnd, firstTime);
}
