//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGDepthStencilAttachment::QSSGDepthStencilAttachment()
extern "C" Q_DECL_EXPORT
QSSGDepthStencilAttachment *ritual_ZN26QSSGDepthStencilAttachmentC1Ev() {
  return new QSSGDepthStencilAttachment();
}

//  void QSSGDepthStencilAttachment::addDebug(QDebug &stream) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QSSGDepthStencilAttachment8addDebugER6QDebug(
    const QSSGDepthStencilAttachment *self,
    QDebug *stream) {
  self->addDebug(*stream);
}

//  QSSGDepthStencilAttachment::~QSSGDepthStencilAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGDepthStencilAttachmentD1Ev(
    QSSGDepthStencilAttachment *self) {
  delete self;
}
