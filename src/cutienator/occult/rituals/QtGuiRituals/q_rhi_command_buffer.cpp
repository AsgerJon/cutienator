//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QRhiCommandBuffer that Python can take functions over in. Every QRhiCommandBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiCommandBufferCall0)(const void *, int *);
typedef void (*CuteQRhiCommandBufferCall1)(const void *, int *);
class CuteQRhiCommandBuffer : public QRhiCommandBuffer {
public:
  using QRhiCommandBuffer::QRhiCommandBuffer;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiCommandBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiCommandBufferCall0 call = reinterpret_cast<CuteQRhiCommandBufferCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiCommandBuffer::resourceType();
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiCommandBufferCall1 call = reinterpret_cast<CuteQRhiCommandBufferCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiCommandBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK17QRhiCommandBuffer12resourceTypeEv(
    const QRhiCommandBuffer *self) {
  return self->resourceType();
}

//  void QRhiCommandBuffer::resourceUpdate(QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer14resourceUpdateEP23QRhiResourceUpdateBatch(
    QRhiCommandBuffer *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(resourceUpdates);
}

//  void QRhiCommandBuffer::beginPass(QRhiRenderTarget *rt, const QColor
//      &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer9beginPassEP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS_13BeginPassFlagEE(
    QRhiCommandBuffer *self,
    QRhiRenderTarget *rt,
    const QColor *colorClearValue,
    const QRhiDepthStencilClearValue *depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginPass(
      rt,
      *colorClearValue,
      *depthStencilClearValue,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiCommandBuffer::endPass(QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer7endPassEP23QRhiResourceUpdateBatch(
    QRhiCommandBuffer *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(resourceUpdates);
}

//  void QRhiCommandBuffer::setGraphicsPipeline(QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer19setGraphicsPipelineEP20QRhiGraphicsPipeline(
    QRhiCommandBuffer *self,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(ps);
}

//  void QRhiCommandBuffer::setViewport(const QRhiViewport &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer11setViewportERK12QRhiViewport(
    QRhiCommandBuffer *self,
    const QRhiViewport *viewport) {
  self->setViewport(*viewport);
}

//  void QRhiCommandBuffer::setScissor(const QRhiScissor &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer10setScissorERK11QRhiScissor(
    QRhiCommandBuffer *self,
    const QRhiScissor *scissor) {
  self->setScissor(*scissor);
}

//  void QRhiCommandBuffer::setBlendConstants(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer17setBlendConstantsERK6QColor(
    QRhiCommandBuffer *self,
    const QColor *c) {
  self->setBlendConstants(*c);
}

//  void QRhiCommandBuffer::setStencilRef(quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer13setStencilRefEj(
    QRhiCommandBuffer *self,
    quint32 refValue) {
  self->setStencilRef(refValue);
}

//  void QRhiCommandBuffer::setShadingRate(const QSize &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer14setShadingRateERK5QSize(
    QRhiCommandBuffer *self,
    const QSize *coarsePixelSize) {
  self->setShadingRate(*coarsePixelSize);
}

//  void QRhiCommandBuffer::draw(quint32 vertexCount, quint32 instanceCount,
//      quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer4drawEjjjj(
    QRhiCommandBuffer *self,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiCommandBuffer::drawIndexed(quint32 indexCount, quint32
//      instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32
//      firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer11drawIndexedEjjjij(
    QRhiCommandBuffer *self,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->drawIndexed(
      indexCount,
      instanceCount,
      firstIndex,
      vertexOffset,
      firstInstance);
}

//  void QRhiCommandBuffer::drawIndirect(QRhiBuffer *indirectBuffer, quint32
//      indirectBufferOffset, quint32 drawCount, quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer12drawIndirectEP10QRhiBufferjjj(
    QRhiCommandBuffer *self,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndirect(
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiCommandBuffer::drawIndexedIndirect(QRhiBuffer *indirectBuffer,
//      quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer19drawIndexedIndirectEP10QRhiBufferjjj(
    QRhiCommandBuffer *self,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndexedIndirect(
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiCommandBuffer::debugMarkBegin(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer14debugMarkBeginERK10QByteArray(
    QRhiCommandBuffer *self,
    const QByteArray *name) {
  self->debugMarkBegin(*name);
}

//  void QRhiCommandBuffer::debugMarkEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer12debugMarkEndEv(QRhiCommandBuffer *self) {
  self->debugMarkEnd();
}

//  void QRhiCommandBuffer::debugMarkMsg(const QByteArray &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer12debugMarkMsgERK10QByteArray(
    QRhiCommandBuffer *self,
    const QByteArray *msg) {
  self->debugMarkMsg(*msg);
}

//  void QRhiCommandBuffer::beginComputePass(QRhiResourceUpdateBatch
//      *resourceUpdates, BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer16beginComputePassEP23QRhiResourceUpdateBatch6QFlagsINS_13BeginPassFlagEE(
    QRhiCommandBuffer *self,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiCommandBuffer::endComputePass(QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer14endComputePassEP23QRhiResourceUpdateBatch(
    QRhiCommandBuffer *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(resourceUpdates);
}

//  void QRhiCommandBuffer::setComputePipeline(QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer18setComputePipelineEP19QRhiComputePipeline(
    QRhiCommandBuffer *self,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(ps);
}

//  void QRhiCommandBuffer::dispatch(int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer8dispatchEiii(
    QRhiCommandBuffer *self,
    int x,
    int y,
    int z) {
  self->dispatch(x, y, z);
}

//  const QRhiNativeHandles *QRhiCommandBuffer::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN17QRhiCommandBuffer13nativeHandlesEv(
    QRhiCommandBuffer *self) {
  return self->nativeHandles();
}

//  void QRhiCommandBuffer::beginExternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer13beginExternalEv(QRhiCommandBuffer *self) {
  self->beginExternal();
}

//  void QRhiCommandBuffer::endExternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiCommandBuffer11endExternalEv(QRhiCommandBuffer *self) {
  self->endExternal();
}

//  double QRhiCommandBuffer::lastCompletedGpuTime()
extern "C" Q_DECL_EXPORT
double ritual_ZN17QRhiCommandBuffer20lastCompletedGpuTimeEv(
    QRhiCommandBuffer *self) {
  return self->lastCompletedGpuTime();
}

//  a Python function taken by a CuteQRhiCommandBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiCommandBuffer(
    QRhiCommandBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiCommandBuffer *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiCommandBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK17QRhiCommandBuffer12resourceTypeEv(
    const QRhiCommandBuffer *self) {
  return self->QRhiCommandBuffer::resourceType();
}
