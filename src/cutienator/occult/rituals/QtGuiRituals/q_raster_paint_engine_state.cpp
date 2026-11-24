//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtCore/qmutex.h>
#include <QtGui/private/qrasterdefs_p.h>
#include <QtGui/private/qgrayraster_p.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qdebug.h>
#include <QtGui/qbitmap.h>
#include <QtGui/private/qmath_p.h>
#include <QtCore/qrandom.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qpixmap_raster_p.h>
#include <QtGui/private/qimage_p.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtGui/private/qcosmeticstroker_p.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtGui/private/qmemrotate_p.h>
#include <QtGui/private/qpixellayout_p.h>
#include <QtGui/private/qrgba64_p.h>
#include <QtGui/private/qpaintengine_raster_p.h>
#include <QtGui/private/qoutlinemapper_p.h>
#include <limits.h>
#include <algorithm>
#ifdef Q_OS_WIN
#  include <QtCore/qvarlengtharray.h>
#  include <QtGui/private/qfontengine_p.h>
#  include <QtCore/qt_windows.h>
#ifdef Q_OS_WIN64
#    include <malloc.h>
#  endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpaintengine_raster.cpp, line 3796, as _ZN9QClipDataD1Ev
inline QClipData::~QClipData()
{
    if (m_clipLines)
        free(m_clipLines);
    if (m_spans)
        free(m_spans);
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 525, as _ZN23QRasterPaintEngineStateC1ERKS_
inline QRasterPaintEngineState::QRasterPaintEngineState(const QRasterPaintEngineState &s)
    : QPainterState(s)
    , lastPen(s.lastPen)
    , penData(s.penData)
    , stroker(s.stroker)
    , strokeFlags(s.strokeFlags)
    , lastBrush(s.lastBrush)
    , brushData(s.brushData)
    , fillFlags(s.fillFlags)
    , pixmapFlags(s.pixmapFlags)
    , intOpacity(s.intOpacity)
    , txscale(s.txscale)
    , clip(s.clip)
    , dirty(s.dirty)
    , flag_bits(s.flag_bits)
{
    brushData.tempImage = nullptr;
    penData.tempImage = nullptr;
    flags.has_clip_ownership = false;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 497, as _ZN23QRasterPaintEngineStateC1Ev
inline QRasterPaintEngineState::QRasterPaintEngineState()
{
    stroker = nullptr;

    fillFlags = 0;
    strokeFlags = 0;
    pixmapFlags = 0;

    intOpacity = 256;

    txscale = 1.;

    flag_bits = 0;
    flags.fast_pen = true;
    flags.non_complex_pen = false;
    flags.antialiased = false;
    flags.bilinear = false;
    flags.fast_text = true;
    flags.tx_noshear = true;
    flags.fast_images = true;
    flags.cosmetic_brush = true;

    clip = nullptr;
    flags.has_clip_ownership = false;

    dirty = 0;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 490, as _ZN23QRasterPaintEngineStateD1Ev
inline QRasterPaintEngineState::~QRasterPaintEngineState()
{
    if (flags.has_clip_ownership)
        delete clip;
}
//  -----------------------------------------------------------------------

//  QRasterPaintEngineState::QRasterPaintEngineState(const
//      QRasterPaintEngineState &other)
extern "C" Q_DECL_EXPORT
QRasterPaintEngineState *ritual_ZN23QRasterPaintEngineStateC1ERKS_(
    const QRasterPaintEngineState *other) {
  return new QRasterPaintEngineState(*other);
}

//  QRasterPaintEngineState::QRasterPaintEngineState()
extern "C" Q_DECL_EXPORT
QRasterPaintEngineState *ritual_ZN23QRasterPaintEngineStateC1Ev() {
  return new QRasterPaintEngineState();
}

//  QRasterPaintEngineState::~QRasterPaintEngineState()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRasterPaintEngineStateD1Ev(QRasterPaintEngineState *self) {
  delete self;
}
