//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGSubRenderPass::QSSGSubRenderPass()
extern "C" Q_DECL_EXPORT
QSSGSubRenderPass *ritual_ZN17QSSGSubRenderPassC1Ev() {
  return new QSSGSubRenderPass();
}

//  void QSSGSubRenderPass::setSubPass(QSSGResourceId userPassId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGSubRenderPass10setSubPassE14QSSGResourceId(
    QSSGSubRenderPass *self,
    QSSGResourceId userPassId) {
  self->setSubPass(userPassId);
}

//  void QSSGSubRenderPass::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QSSGSubRenderPass8addDebugER6QDebug(
    const QSSGSubRenderPass *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGSubRenderPass::~QSSGSubRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGSubRenderPassD1Ev(QSSGSubRenderPass *self) {
  delete self;
}
