//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qringbuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qringbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "private/qringbuffer_p.h"
#include <type_traits>
#include <string.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/tools/qringbuffer.cpp, line 18, as _ZN10QRingChunk8allocateEx
inline void QRingChunk::allocate(qsizetype alloc)
{
    Q_ASSERT(alloc > 0 && size() == 0);

    if (chunk.size() < alloc || isShared())
        chunk = QByteArray(alloc, Qt::Uninitialized);
}
//  -----------------------------------------------------------------------

//  QRingChunk::QRingChunk()
extern "C" Q_DECL_EXPORT
QRingChunk *ritual_ZN10QRingChunkC1Ev() {
  return new QRingChunk();
}

//  QRingChunk::QRingChunk(qsizetype alloc)
extern "C" Q_DECL_EXPORT
QRingChunk *ritual_ZN10QRingChunkC1Ex(qsizetype alloc) {
  return new QRingChunk(alloc);
}

//  QRingChunk::QRingChunk(const QByteArray &qba)
extern "C" Q_DECL_EXPORT
QRingChunk *ritual_ZN10QRingChunkC1ERK10QByteArray(const QByteArray *qba) {
  return new QRingChunk(*qba);
}

//  void QRingChunk::allocate(qsizetype alloc)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk8allocateEx(QRingChunk *self, qsizetype alloc) {
  self->allocate(alloc);
}

//  bool QRingChunk::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRingChunk8isSharedEv(const QRingChunk *self) {
  return self->isShared();
}

//  void QRingChunk::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk6detachEv(QRingChunk *self) {
  self->detach();
}

//  qsizetype QRingChunk::head() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QRingChunk4headEv(const QRingChunk *self) {
  return self->head();
}

//  qsizetype QRingChunk::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QRingChunk4sizeEv(const QRingChunk *self) {
  return self->size();
}

//  qsizetype QRingChunk::capacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QRingChunk8capacityEv(const QRingChunk *self) {
  return self->capacity();
}

//  qsizetype QRingChunk::available() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QRingChunk9availableEv(const QRingChunk *self) {
  return self->available();
}

//  const char *QRingChunk::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK10QRingChunk4dataEv(const QRingChunk *self) {
  return self->data();
}

//  void QRingChunk::advance(qsizetype offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk7advanceEx(QRingChunk *self, qsizetype offset) {
  self->advance(offset);
}

//  void QRingChunk::grow(qsizetype offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk4growEx(QRingChunk *self, qsizetype offset) {
  self->grow(offset);
}

//  void QRingChunk::assign(const QByteArray &qba)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk6assignERK10QByteArray(
    QRingChunk *self,
    const QByteArray *qba) {
  self->assign(*qba);
}

//  void QRingChunk::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk5resetEv(QRingChunk *self) {
  self->reset();
}

//  void QRingChunk::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunk5clearEv(QRingChunk *self) {
  self->clear();
}

//  QRingChunk::~QRingChunk()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRingChunkD1Ev(QRingChunk *self) {
  delete self;
}
