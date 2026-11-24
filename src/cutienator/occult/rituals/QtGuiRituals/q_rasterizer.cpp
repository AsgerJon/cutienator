//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrasterizer_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrasterizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrasterizer_p.h"
#include <QPoint>
#include <QRect>
#include <private/qmath_p.h>
#include <private/qdatabuffer_p.h>
#include <private/qdrawhelper_p.h>
#include <QtGui/qpainterpath.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qrasterizer.cpp, line 598, as _ZN11QRasterizerD1Ev
inline QRasterizer::~QRasterizer()
{
    delete d;
}
//  -----------------------------------------------------------------------

//  QRasterizer::~QRasterizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRasterizerD1Ev(QRasterizer *self) {
  delete self;
}
