//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpen_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#include <QtGui/private/qpen_p.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qvariant.h>
#include <QtGui/qbrush.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpen.cpp, line 192, as _ZN11QPenPrivateC1ERK6QBrushdN2Qt8PenStyleENS3_11PenCapStyleENS3_12PenJoinStyleE
inline QPenPrivate::QPenPrivate(const QBrush &_brush, qreal _width, Qt::PenStyle penStyle,
                         Qt::PenCapStyle _capStyle, Qt::PenJoinStyle _joinStyle)
    : dashOffset(0), miterLimit(2),
      cosmetic(false)
{
    width = _width;
    brush = _brush;
    style = penStyle;
    capStyle = _capStyle;
    joinStyle = _joinStyle;
}
//  -----------------------------------------------------------------------

//  QPenPrivate::QPenPrivate(const QBrush &brush, qreal width, Qt::PenStyle
//      a2, Qt::PenCapStyle a3, Qt::PenJoinStyle _joinStyle)
extern "C" Q_DECL_EXPORT
QPenPrivate *ritual_ZN11QPenPrivateC1ERK6QBrushdN2Qt8PenStyleENS3_11PenCapStyleENS3_12PenJoinStyleE(
    const QBrush *brush,
    qreal width,
    Qt::PenStyle a2,
    Qt::PenCapStyle a3,
    Qt::PenJoinStyle _joinStyle) {
  return new QPenPrivate(*brush, width, a2, a3, _joinStyle);
}

//  QPenPrivate::~QPenPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPenPrivateD1Ev(QPenPrivate *self) {
  delete self;
}
