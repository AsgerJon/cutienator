//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRhiBuffer::~QSSGRhiBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRhiBufferD1Ev(QSSGRhiBuffer *self) {
  delete self;
}

//  QRhiBuffer *QSSGRhiBuffer::buffer() const
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZNK13QSSGRhiBuffer6bufferEv(const QSSGRhiBuffer *self) {
  return self->buffer();
}

//  quint32 QSSGRhiBuffer::stride() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK13QSSGRhiBuffer6strideEv(const QSSGRhiBuffer *self) {
  return self->stride();
}

//  quint32 QSSGRhiBuffer::numVertices() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK13QSSGRhiBuffer11numVerticesEv(const QSSGRhiBuffer *self) {
  return self->numVertices();
}

//  QRhiCommandBuffer::IndexFormat QSSGRhiBuffer::indexFormat() const
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer::IndexFormat ritual_ZNK13QSSGRhiBuffer11indexFormatEv(
    const QSSGRhiBuffer *self) {
  return self->indexFormat();
}
