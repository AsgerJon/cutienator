//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcareaallocator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcareaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcareaallocator_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
}
//  -----------------------------------------------------------------------

//  QCAreaAllocator::~QCAreaAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCAreaAllocatorD1Ev(QCAreaAllocator *self) {
  delete self;
}

//  bool QCAreaAllocator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCAreaAllocator7isEmptyEv(const QCAreaAllocator *self) {
  return self->isEmpty();
}

//  QSize QCAreaAllocator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCAreaAllocator4sizeEv(const QCAreaAllocator *self) {
  return new QSize(self->size());
}
