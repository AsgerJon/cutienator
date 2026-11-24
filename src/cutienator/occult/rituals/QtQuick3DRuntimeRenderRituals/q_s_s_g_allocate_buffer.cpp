//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGAllocateBuffer::QSSGAllocateBuffer()
extern "C" Q_DECL_EXPORT
QSSGAllocateBuffer *ritual_ZN18QSSGAllocateBufferC1Ev() {
  return new QSSGAllocateBuffer();
}

//  QSSGAllocateBuffer::QSSGAllocateBuffer(const QByteArray &inName,
//      QSSGRenderTextureFormat inFormat, QSSGRenderTextureFilterOp
//      inFilterOp, QSSGRenderTextureCoordOp inCoordOp, float inMultiplier,
//      QSSGAllocateBufferFlags inFlags)
extern "C" Q_DECL_EXPORT
QSSGAllocateBuffer *ritual_ZN18QSSGAllocateBufferC1ERK10QByteArray23QSSGRenderTextureFormat25QSSGRenderTextureFilterOp24QSSGRenderTextureCoordOpf23QSSGAllocateBufferFlags(
    const QByteArray *inName,
    const QSSGRenderTextureFormat *inFormat,
    QSSGRenderTextureFilterOp inFilterOp,
    QSSGRenderTextureCoordOp inCoordOp,
    float inMultiplier,
    const QSSGAllocateBufferFlags *inFlags) {
  return new QSSGAllocateBuffer(
      *inName,
      *inFormat,
      inFilterOp,
      inCoordOp,
      inMultiplier,
      *inFlags);
}

//  QSSGAllocateBuffer::QSSGAllocateBuffer(const QSSGAllocateBuffer &command)
extern "C" Q_DECL_EXPORT
QSSGAllocateBuffer *ritual_ZN18QSSGAllocateBufferC1ERKS_(
    const QSSGAllocateBuffer *command) {
  return new QSSGAllocateBuffer(*command);
}

//  QSSGAllocateBuffer::~QSSGAllocateBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGAllocateBufferD1Ev(QSSGAllocateBuffer *self) {
  delete self;
}
