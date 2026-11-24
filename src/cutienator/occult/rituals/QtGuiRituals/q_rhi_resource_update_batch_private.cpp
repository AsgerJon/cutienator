//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhi_p.h"
#include <qmath.h>
#include <QLoggingCategory>
#include "private/qloggingregistry_p.h"
#include "qrhinull_p.h"
#ifndef QT_NO_OPENGL
#include "qrhigles2_p.h"
#endif
#if QT_CONFIG(vulkan)
#endif
#ifdef Q_OS_WIN
#include "qrhid3d11_p.h"
#include "qrhid3d12_p.h"
#endif
#if QT_CONFIG(metal)
#include "qrhimetal_p.h"
#endif
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 10256, as _ZN30QRhiResourceUpdateBatchPrivate5mergeEPS_
inline void QRhiResourceUpdateBatchPrivate::merge(QRhiResourceUpdateBatchPrivate *other)
{
    int combinedSize = activeBufferOpCount + other->activeBufferOpCount;
    if (bufferOps.size() < combinedSize)
        bufferOps.resize(combinedSize);
    for (int i = activeBufferOpCount; i < combinedSize; ++i)
        bufferOps[i] = std::move(other->bufferOps[i - activeBufferOpCount]);
    activeBufferOpCount += other->activeBufferOpCount;

    combinedSize = activeTextureOpCount + other->activeTextureOpCount;
    if (textureOps.size() < combinedSize)
        textureOps.resize(combinedSize);
    for (int i = activeTextureOpCount; i < combinedSize; ++i)
        textureOps[i] = std::move(other->textureOps[i - activeTextureOpCount]);
    activeTextureOpCount += other->activeTextureOpCount;
}

//  from src/gui/rhi/qrhi.cpp, line 10273, as _ZNK30QRhiResourceUpdateBatchPrivate18hasOptimalCapacityEv
inline bool QRhiResourceUpdateBatchPrivate::hasOptimalCapacity() const
{
    return activeBufferOpCount < BUFFER_OPS_STATIC_ALLOC - 4
            && activeTextureOpCount < TEXTURE_OPS_STATIC_ALLOC - 4;
}

//  from src/gui/rhi/qrhi.cpp, line 10279, as _ZN30QRhiResourceUpdateBatchPrivate11trimOpListsEv
inline void QRhiResourceUpdateBatchPrivate::trimOpLists()
{
    // Unlike free(), this is expected to aggressively deallocate all memory
    // used by both the buffer and texture operation lists. (i.e. using
    // squeeze() to only keep the stack prealloc of the QVLAs)
    //
    // This (e.g. just the destruction of bufferOps elements) may have a
    // non-negligible performance impact e.g. with Qt Quick with scenes where
    // there are lots of buffer operations per frame.

    activeBufferOpCount = 0;
    bufferOps.clear();
    bufferOps.squeeze();

    activeTextureOpCount = 0;
    textureOps.clear();
    textureOps.squeeze();
}
//  -----------------------------------------------------------------------

//  void QRhiResourceUpdateBatchPrivate::merge(QRhiResourceUpdateBatchPrivate
//      *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate5mergeEPS_(
    QRhiResourceUpdateBatchPrivate *self,
    QRhiResourceUpdateBatchPrivate *other) {
  self->merge(other);
}

//  bool QRhiResourceUpdateBatchPrivate::hasOptimalCapacity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QRhiResourceUpdateBatchPrivate18hasOptimalCapacityEv(
    const QRhiResourceUpdateBatchPrivate *self) {
  return self->hasOptimalCapacity();
}

//  void QRhiResourceUpdateBatchPrivate::trimOpLists()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate11trimOpListsEv(
    QRhiResourceUpdateBatchPrivate *self) {
  self->trimOpLists();
}

//  QRhiResourceUpdateBatchPrivate
//      *QRhiResourceUpdateBatchPrivate::get(QRhiResourceUpdateBatch *b)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate *ritual_ZN30QRhiResourceUpdateBatchPrivate3getEP23QRhiResourceUpdateBatch(
    QRhiResourceUpdateBatch *b) {
  return QRhiResourceUpdateBatchPrivate::get(b);
}

//  QRhiResourceUpdateBatchPrivate::~QRhiResourceUpdateBatchPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivateD1Ev(
    QRhiResourceUpdateBatchPrivate *self) {
  delete self;
}
