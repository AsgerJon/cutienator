//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrasterizer_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrasterizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrasterizer_p.h>
#include <QtCore/QPoint>
#include <QtCore/QRect>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qdatabuffer_p.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtGui/qpainterpath.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qrasterizer.cpp, line 21, as local:qrasterizer.cpp:QScFixed
#if Q_PROCESSOR_WORDSIZE == 8
typedef qint64 QScFixed;
#endif  // Q_PROCESSOR_WORDSIZE == 8

//  from src/gui/painting/qrasterizer.cpp, line 35, as local:qrasterizer.cpp:SPAN_BUFFER_SIZE
#define SPAN_BUFFER_SIZE 256

//  from src/gui/painting/qrasterizer.cpp, line 97, as local:qrasterizer.cpp:CHUNK_SIZE
#define CHUNK_SIZE 64

//  from src/gui/painting/qrasterizer.cpp, line 248, as local:qrasterizer.cpp:split
static void split(QT_FT_Vector *b)
{
    b[6] = b[3];

    {
        const QT_FT_Pos temp = (b[1].x + b[2].x)/2;

        b[1].x = (b[0].x + b[1].x)/2;
        b[5].x = (b[2].x + b[3].x)/2;
        b[2].x = (b[1].x + temp)/2;
        b[4].x = (b[5].x + temp)/2;
        b[3].x = (b[2].x + b[4].x)/2;
    }
    {
        const QT_FT_Pos temp = (b[1].y + b[2].y)/2;

        b[1].y = (b[0].y + b[1].y)/2;
        b[5].y = (b[2].y + b[3].y)/2;
        b[2].y = (b[1].y + temp)/2;
        b[4].y = (b[5].y + temp)/2;
        b[3].y = (b[2].y + b[4].y)/2;
    }
}

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
