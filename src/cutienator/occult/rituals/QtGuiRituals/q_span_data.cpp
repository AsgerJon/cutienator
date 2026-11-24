//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdrawhelper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdrawhelper_p.h>
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

//  from src/gui/painting/qpaintengine_raster.cpp, line 4465, as _ZN9QSpanData4initEP13QRasterBufferPK18QRasterPaintEngine
inline void QSpanData::init(QRasterBuffer *rb, const QRasterPaintEngine *pe)
{
    rasterBuffer = rb;
    type = None;
    txop = 0;
    bilinear = false;
    m11 = m22 = m33 = 1.;
    m12 = m13 = m21 = m23 = dx = dy = 0.0;
    clip = pe ? pe->d_func()->clip() : nullptr;
}
//  -----------------------------------------------------------------------

//  QSpanData::QSpanData()
extern "C" Q_DECL_EXPORT
QSpanData *ritual_ZN9QSpanDataC1Ev() {
  return new QSpanData();
}

//  QSpanData::~QSpanData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSpanDataD1Ev(QSpanData *self) {
  delete self;
}

//  void QSpanData::init(QRasterBuffer *rb, const QRasterPaintEngine *pe)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSpanData4initEP13QRasterBufferPK18QRasterPaintEngine(
    QSpanData *self,
    QRasterBuffer *rb,
    const QRasterPaintEngine *pe) {
  self->init(rb, pe);
}
