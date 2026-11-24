//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGBindTarget::QSSGBindTarget(QSSGRenderTextureFormat inFormat)
extern "C" Q_DECL_EXPORT
QSSGBindTarget *ritual_ZN14QSSGBindTargetC1E23QSSGRenderTextureFormat(
    const QSSGRenderTextureFormat *inFormat) {
  return new QSSGBindTarget(*inFormat);
}

//  QSSGBindTarget::QSSGBindTarget(const QSSGBindTarget &command)
extern "C" Q_DECL_EXPORT
QSSGBindTarget *ritual_ZN14QSSGBindTargetC1ERKS_(
    const QSSGBindTarget *command) {
  return new QSSGBindTarget(*command);
}

//  QSSGBindTarget::~QSSGBindTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGBindTargetD1Ev(QSSGBindTarget *self) {
  delete self;
}
