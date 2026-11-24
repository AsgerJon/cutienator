//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCanvasPainter/private/qcanvasimage_p.h>
#include <QtCore/qvariant.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimage.cpp, line 305, as _ZN19QCanvasImagePrivateC1Ev
inline QCanvasImagePrivate::QCanvasImagePrivate()
    : id(0)
    , width(0)
    , height(0)
    , devicePixelRatio(1.0)
    , type(DataType::Unknown)
    , sizeInBytes(0)
    , tintColor(QColorConstants::White)
{
}
//  -----------------------------------------------------------------------

//  QCanvasImagePrivate::QCanvasImagePrivate()
extern "C" Q_DECL_EXPORT
QCanvasImagePrivate *ritual_ZN19QCanvasImagePrivateC1Ev() {
  return new QCanvasImagePrivate();
}

//  QCanvasImagePrivate *QCanvasImagePrivate::get(QCanvasImage *image)
extern "C" Q_DECL_EXPORT
QCanvasImagePrivate *ritual_ZN19QCanvasImagePrivate3getEP12QCanvasImage(
    QCanvasImage *image) {
  return QCanvasImagePrivate::get(image);
}

//  const QCanvasImagePrivate *QCanvasImagePrivate::get(const QCanvasImage
//      *image)
extern "C" Q_DECL_EXPORT
const QCanvasImagePrivate *ritual_ZN19QCanvasImagePrivate3getEPK12QCanvasImage(
    const QCanvasImage *image) {
  return QCanvasImagePrivate::get(image);
}

//  QCanvasImagePrivate::~QCanvasImagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePrivateD1Ev(QCanvasImagePrivate *self) {
  delete self;
}
