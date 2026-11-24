//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicustommaterialsyste
//  m_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGCustomMaterialSystem::QSSGCustomMaterialSystem()
extern "C" Q_DECL_EXPORT
QSSGCustomMaterialSystem *ritual_ZN24QSSGCustomMaterialSystemC1Ev() {
  return new QSSGCustomMaterialSystem();
}

//  QSSGCustomMaterialSystem::~QSSGCustomMaterialSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystemD1Ev(
    QSSGCustomMaterialSystem *self) {
  delete self;
}

//  void QSSGCustomMaterialSystem::setRenderContextInterface(QSSGRenderContex
//      tInterface *inContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem25setRenderContextInterfaceEP26QSSGRenderContextInterface(
    QSSGCustomMaterialSystem *self,
    QSSGRenderContextInterface *inContext) {
  self->setRenderContextInterface(inContext);
}

//  void QSSGCustomMaterialSystem::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem22releaseCachedResourcesEv(
    QSSGCustomMaterialSystem *self) {
  self->releaseCachedResources();
}
