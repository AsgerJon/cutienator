//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasimagepattern.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/qcanvasimagepattern.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasimagepattern.h>
#include <QtCanvasPainter/private/qcanvasimagepattern_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 414, as local:qcanvasimagepattern.cpp:DECONST
#define DECONST(d) const_cast<QCanvasImagePatternPrivate *>(d)

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 435, as _ZN26QCanvasImagePatternPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()
{
    return new QCanvasImagePatternPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasimagepattern.cpp, line 178, as _ZNK26QCanvasImagePatternPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasImagePatternPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasImagePatternPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || angle != pd.angle
        || tintColor != pd.tintColor)
        return false;

    // For images comparing the id is enough
    if (image.id() != pd.image.id())
        return false;

    return true;
}
//  -----------------------------------------------------------------------

//  QCanvasImagePattern::QCanvasImagePattern()
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1Ev() {
  return new QCanvasImagePattern();
}

//  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImage(
    const QCanvasImage *image) {
  return new QCanvasImagePattern(*image);
}

//  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image,
//      QPointF startPosition, QSizeF imageSize)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImage7QPointF6QSizeF(
    const QCanvasImage *image,
    const QPointF *startPosition,
    const QSizeF *imageSize) {
  return new QCanvasImagePattern(*image, *startPosition, *imageSize);
}

//  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImage &image, qreal
//      startX, qreal startY, qreal imageWidth, qreal imageHeight)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1ERK12QCanvasImagedddd(
    const QCanvasImage *image,
    qreal startX,
    qreal startY,
    qreal imageWidth,
    qreal imageHeight) {
  return new QCanvasImagePattern(
      *image,
      startX,
      startY,
      imageWidth,
      imageHeight);
}

//  QCanvasImagePattern::QCanvasImagePattern(const QCanvasImagePattern &a0)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1ERKS_(
    const QCanvasImagePattern *a0) {
  return new QCanvasImagePattern(*a0);
}

//  QCanvasImagePattern &QCanvasImagePattern::operator=(const
//      QCanvasImagePattern &a0)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternaSERKS_(
    QCanvasImagePattern *self,
    const QCanvasImagePattern *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasImagePattern::QCanvasImagePattern(QCanvasImagePattern &&a0)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1EOS_(
    QCanvasImagePattern *a0) {
  return new QCanvasImagePattern(std::move(*a0));
}

//  QCanvasImagePattern &QCanvasImagePattern::operator=(QCanvasImagePattern
//      &&other)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternaSEOS_(
    QCanvasImagePattern *self,
    QCanvasImagePattern *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCanvasImagePattern::~QCanvasImagePattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePatternD1Ev(QCanvasImagePattern *self) {
  delete self;
}

//  QCanvasBrush QCanvasImagePattern::operator QCanvasBrush() const
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZNK19QCanvasImagePatterncv12QCanvasBrushEv(
    const QCanvasImagePattern *self) {
  return new QCanvasBrush(self->operator QCanvasBrush());
}

//  QVariant QCanvasImagePattern::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QCanvasImagePatterncv8QVariantEv(
    const QCanvasImagePattern *self) {
  return new QVariant(self->operator QVariant());
}

//  QPointF QCanvasImagePattern::startPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QCanvasImagePattern13startPositionEv(
    const QCanvasImagePattern *self) {
  return new QPointF(self->startPosition());
}

//  void QCanvasImagePattern::setStartPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern16setStartPositionEdd(
    QCanvasImagePattern *self,
    qreal x,
    qreal y) {
  self->setStartPosition(x, y);
}

//  void QCanvasImagePattern::setStartPosition(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern16setStartPositionE7QPointF(
    QCanvasImagePattern *self,
    const QPointF *point) {
  self->setStartPosition(*point);
}

//  QSizeF QCanvasImagePattern::imageSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QCanvasImagePattern9imageSizeEv(
    const QCanvasImagePattern *self) {
  return new QSizeF(self->imageSize());
}

//  void QCanvasImagePattern::setImageSize(qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern12setImageSizeEdd(
    QCanvasImagePattern *self,
    qreal width,
    qreal height) {
  self->setImageSize(width, height);
}

//  void QCanvasImagePattern::setImageSize(QSizeF size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern12setImageSizeE6QSizeF(
    QCanvasImagePattern *self,
    const QSizeF *size) {
  self->setImageSize(*size);
}

//  QCanvasImage QCanvasImagePattern::image() const
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZNK19QCanvasImagePattern5imageEv(
    const QCanvasImagePattern *self) {
  return new QCanvasImage(self->image());
}

//  void QCanvasImagePattern::setImage(const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern8setImageERK12QCanvasImage(
    QCanvasImagePattern *self,
    const QCanvasImage *image) {
  self->setImage(*image);
}

//  qreal QCanvasImagePattern::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QCanvasImagePattern8rotationEv(
    const QCanvasImagePattern *self) {
  return self->rotation();
}

//  void QCanvasImagePattern::setRotation(qreal rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern11setRotationEd(
    QCanvasImagePattern *self,
    qreal rotation) {
  self->setRotation(rotation);
}

//  QColor QCanvasImagePattern::tintColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QCanvasImagePattern9tintColorEv(
    const QCanvasImagePattern *self) {
  return new QColor(self->tintColor());
}

//  void QCanvasImagePattern::setTintColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern12setTintColorE6QColor(
    QCanvasImagePattern *self,
    const QColor *color) {
  self->setTintColor(*color);
}

//  uint QCanvasImagePattern::serialNumber() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QCanvasImagePattern12serialNumberEv(
    const QCanvasImagePattern *self) {
  return self->serialNumber();
}

//  void QCanvasImagePattern::swap(QCanvasImagePattern &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCanvasImagePattern4swapERS_(
    QCanvasImagePattern *self,
    QCanvasImagePattern *other) {
  self->swap(*other);
}

//  bool operator==(const QCanvasImagePattern &lhs, const QCanvasImagePattern
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QCanvasImagePatternS1_(
    const QCanvasImagePattern *lhs,
    const QCanvasImagePattern *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasImagePattern &lhs, const QCanvasImagePattern
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QCanvasImagePatternS1_(
    const QCanvasImagePattern *lhs,
    const QCanvasImagePattern *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QCanvasImagePattern::QCanvasImagePattern(QCanvasImagePatternPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasImagePattern *ritual_ZN19QCanvasImagePatternC1EP26QCanvasImagePatternPrivate(
    QCanvasImagePatternPrivate *p) {
  return new QCanvasImagePattern(p);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QCanvasImagePattern &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK19QCanvasImagePattern(
    QDataStream *a0,
    const QCanvasImagePattern *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QCanvasImagePattern &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR19QCanvasImagePattern(
    QDataStream *a0,
    QCanvasImagePattern *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasImagePattern &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QCanvasImagePattern(
    const QDebug *a0,
    const QCanvasImagePattern *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
