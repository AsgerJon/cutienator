//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGDepthTextureAttachment::QSSGDepthTextureAttachment(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QSSGDepthTextureAttachment *ritual_ZN26QSSGDepthTextureAttachmentC1ERK10QByteArray(
    const QByteArray *name) {
  return new QSSGDepthTextureAttachment(*name);
}

//  QSSGDepthTextureAttachment::~QSSGDepthTextureAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGDepthTextureAttachmentD1Ev(
    QSSGDepthTextureAttachment *self) {
  delete self;
}
