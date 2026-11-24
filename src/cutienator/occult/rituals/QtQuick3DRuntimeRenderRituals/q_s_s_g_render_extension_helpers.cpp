//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGRenderExtensionHelpers::registerRenderResult(const QSSGFrameData
//      &frameData, QSSGExtensionId extension, QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderExtensionHelpers20registerRenderResultERK13QSSGFrameData15QSSGExtensionIdP11QRhiTexture(
    const QSSGFrameData *frameData,
    QSSGExtensionId extension,
    QRhiTexture *texture) {
  QSSGRenderExtensionHelpers::registerRenderResult(
      *frameData,
      extension,
      texture);
}

//  QSSGRenderExtensionHelpers::~QSSGRenderExtensionHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderExtensionHelpersD1Ev(
    QSSGRenderExtensionHelpers *self) {
  delete self;
}
