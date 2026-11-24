//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
#include "qcdistancefieldglyphcache_p.h"
#include <private/qrawfont_p.h>
#endif
#include "qcpainterengine_p.h"
#include "qcpainterrhirenderer_p.h"
#include "qcanvaspainter_p.h"
#include "qcanvascustombrush.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <QFile>
#include <QtGui/private/qvectorpath_p.h>
#include <rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3727, as _ZN11QCRhiCanvas7destroyEv
inline void QCRhiCanvas::destroy()
{
    delete rp;
    delete rt;
    delete ds;
    delete msaaColorBuffer;
    delete tex;
}
//  -----------------------------------------------------------------------

//  bool QCRhiCanvas::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QCRhiCanvas6isNullEv(const QCRhiCanvas *self) {
  return self->isNull();
}

//  void QCRhiCanvas::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCRhiCanvas7destroyEv(QCRhiCanvas *self) {
  self->destroy();
}

//  QCRhiCanvas::~QCRhiCanvas()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCRhiCanvasD1Ev(QCRhiCanvas *self) {
  delete self;
}
