//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasimage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCanvasPainter/private/qcanvasimage_p.h>
#include <QtCore/qvariant.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimage.cpp, line 295, as _ZN12QCanvasImage6detachEv
inline void QCanvasImage::detach()
{
    if (d)
        d.detach();
    else
        d = new QCanvasImagePrivate();
}
//  -----------------------------------------------------------------------

//  QCanvasImage::QCanvasImage()
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN12QCanvasImageC1Ev() {
  return new QCanvasImage();
}

//  QCanvasImage::QCanvasImage(const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN12QCanvasImageC1ERKS_(const QCanvasImage *image) {
  return new QCanvasImage(*image);
}

//  QCanvasImage::~QCanvasImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanvasImageD1Ev(QCanvasImage *self) {
  delete self;
}

//  QCanvasImage &QCanvasImage::operator=(const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN12QCanvasImageaSERKS_(
    QCanvasImage *self,
    const QCanvasImage *image) {
  return &(self->operator=(*image));
}

//  QCanvasImage::QCanvasImage(QCanvasImage &&other)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN12QCanvasImageC1EOS_(QCanvasImage *other) {
  return new QCanvasImage(std::move(*other));
}

//  QCanvasImage &QCanvasImage::operator=(QCanvasImage &&other)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN12QCanvasImageaSEOS_(
    QCanvasImage *self,
    QCanvasImage *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCanvasImage::swap(QCanvasImage &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanvasImage4swapERS_(
    QCanvasImage *self,
    QCanvasImage *other) {
  self->swap(*other);
}

//  QVariant QCanvasImage::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QCanvasImagecv8QVariantEv(const QCanvasImage *self) {
  return new QVariant(self->operator QVariant());
}

//  int QCanvasImage::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCanvasImage2idEv(const QCanvasImage *self) {
  return self->id();
}

//  int QCanvasImage::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCanvasImage5widthEv(const QCanvasImage *self) {
  return self->width();
}

//  int QCanvasImage::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCanvasImage6heightEv(const QCanvasImage *self) {
  return self->height();
}

//  QSize QCanvasImage::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QCanvasImage4sizeEv(const QCanvasImage *self) {
  return new QSize(self->size());
}

//  qsizetype QCanvasImage::sizeInBytes() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QCanvasImage11sizeInBytesEv(const QCanvasImage *self) {
  return self->sizeInBytes();
}

//  qreal QCanvasImage::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QCanvasImage16devicePixelRatioEv(
    const QCanvasImage *self) {
  return self->devicePixelRatio();
}

//  bool QCanvasImage::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCanvasImage6isNullEv(const QCanvasImage *self) {
  return self->isNull();
}

//  QColor QCanvasImage::tintColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QCanvasImage9tintColorEv(const QCanvasImage *self) {
  return new QColor(self->tintColor());
}

//  void QCanvasImage::setTintColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanvasImage12setTintColorE6QColor(
    QCanvasImage *self,
    const QColor *color) {
  self->setTintColor(*color);
}

//  bool operator==(const QCanvasImage &lhs, const QCanvasImage &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QCanvasImageS1_(
    const QCanvasImage *lhs,
    const QCanvasImage *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasImage &lhs, const QCanvasImage &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QCanvasImageS1_(
    const QCanvasImage *lhs,
    const QCanvasImage *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QCanvasImage::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCanvasImage6detachEv(QCanvasImage *self) {
  self->detach();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasImage &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK12QCanvasImage(
    const QDebug *a0,
    const QCanvasImage *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
