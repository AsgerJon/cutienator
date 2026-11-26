//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PDF)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpdf_p.h>
#ifndef QT_NO_PDF
#include "qplatformdefs.h"
#include <QtGui/private/qcmyk_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtGui/qimagewriter.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qtimezone.h>
#include <QtCore/quuid.h>
#include <QtCore/qxmlstream.h>
#include <cstdio>
#include <map>
#ifndef QT_NO_COMPRESS
#include <zlib.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/painting/qpdf.cpp, line 570, as local:qpdf.cpp:moveToHook
#if !defined(QT_NO_PDF)
static void moveToHook(qfixed x, qfixed y, void *data)
{
    QPdf::Stroker *t = (QPdf::Stroker *)data;
    if (!t->first)
        *t->stream << "h\n";
    if (!t->cosmeticPen)
        t->matrix.map(x, y, &x, &y);
    *t->stream << x << y << "m\n";
    t->first = false;
}
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 581, as local:qpdf.cpp:lineToHook
#if !defined(QT_NO_PDF)
static void lineToHook(qfixed x, qfixed y, void *data)
{
    QPdf::Stroker *t = (QPdf::Stroker *)data;
    if (!t->cosmeticPen)
        t->matrix.map(x, y, &x, &y);
    *t->stream << x << y << "l\n";
}
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 589, as local:qpdf.cpp:cubicToHook
#if !defined(QT_NO_PDF)
static void cubicToHook(qfixed c1x, qfixed c1y,
                        qfixed c2x, qfixed c2y,
                        qfixed ex, qfixed ey,
                        void *data)
{
    QPdf::Stroker *t = (QPdf::Stroker *)data;
    if (!t->cosmeticPen) {
        t->matrix.map(c1x, c1y, &c1x, &c1y);
        t->matrix.map(c2x, c2y, &c2x, &c2y);
        t->matrix.map(ex, ey, &ex, &ey);
    }
    *t->stream << c1x << c1y
               << c2x << c2y
               << ex << ey
               << "c\n";
}
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 619, as _ZN4QPdf7Stroker6setPenERK4QPen6QFlagsIN8QPainter10RenderHintEE
#if !defined(QT_NO_PDF)
inline void QPdf::Stroker::setPen(const QPen &pen, QPainter::RenderHints)
{
    if (pen.style() == Qt::NoPen) {
        stroker = nullptr;
        return;
    }
    qreal w = pen.widthF();
    bool zeroWidth = w < 0.0001;
    cosmeticPen = pen.isCosmetic();
    if (zeroWidth)
        w = .1;

    basicStroker.setStrokeWidth(w);
    basicStroker.setCapStyle(pen.capStyle());
    basicStroker.setJoinStyle(pen.joinStyle());
    basicStroker.setMiterLimit(pen.miterLimit());

    QList<qreal> dashpattern = pen.dashPattern();
    if (zeroWidth) {
        for (int i = 0; i < dashpattern.size(); ++i)
            dashpattern[i] *= 10.;
    }
    if (!dashpattern.isEmpty()) {
        dashStroker.setDashPattern(dashpattern);
        dashStroker.setDashOffset(pen.dashOffset());
        stroker = &dashStroker;
    } else {
        stroker = &basicStroker;
    }
}
#endif  // !defined(QT_NO_PDF)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_PDF)
//  void QPdf::Stroker::setPen(const QPen &pen, QPainter::RenderHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPdf7Stroker6setPenERK4QPen6QFlagsIN8QPainter10RenderHintEE(
    QPdf::Stroker *self,
    const QPen *pen,
    int hints) {
  self->setPen(*pen, QFlags<QPainter::RenderHint>::fromInt(hints));
}
#endif  // !defined(QT_NO_PDF)

#endif  // !defined(QT_NO_PDF)
