//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasgridpattern.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/qcanvasgridpattern.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasgridpattern.h>
#include <QtCanvasPainter/private/qcanvasgridpattern_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 427, as local:qcanvasgridpattern.cpp:DECONST
#define DECONST(d) const_cast<QCanvasGridPatternPrivate *>(d)

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 465, as _ZN25QCanvasGridPatternPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
{
    return new QCanvasGridPatternPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 157, as _ZNK25QCanvasGridPatternPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasGridPatternPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &pd = static_cast<const QCanvasGridPatternPrivate &>(other);

    if (x != pd.x
        || y != pd.y
        || width != pd.width
        || height != pd.height
        || feather != pd.feather
        || angle != pd.angle
        || lineWidth != pd.lineWidth
        || lineColor != pd.lineColor
        || backgroundColor != pd.backgroundColor)
        return false;

    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 429, as _ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanvasPainter
inline QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter *painter) const
{
    auto *d = this;
    Q_UNUSED(painter);
    if (d->changed) {
        createGridPattern();
        DECONST(d)->changed = false;
    }
    return d->paint;
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 440, as _ZNK25QCanvasGridPatternPrivate17createGridPatternEv
inline void QCanvasGridPatternPrivate::createGridPattern() const
{
    auto *d = this;
    QCPaint &p = DECONST(d)->paint;
    p.brushType = BrushGrid;
    p.transform = QTransform::fromTranslate(d->x, d->y);
    if (!qFuzzyIsNull(d->angle))
        p.transform = p.transform.rotateRadians(d->angle);

    p.extent[0] = float(d->width);
    p.extent[1] = float(d->height);

    p.feather = float(d->feather);
    p.radius = float(d->lineWidth);

    p.innerColor = { d->lineColor.redF(),
                     d->lineColor.greenF(),
                     d->lineColor.blueF(),
                     d->lineColor.alphaF() };
    p.outerColor = { d->backgroundColor.redF(),
                     d->backgroundColor.greenF(),
                     d->backgroundColor.blueF(),
                     d->backgroundColor.alphaF() };
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvasgridpattern.cpp, line 71, as _ZN18QCanvasGridPattern6detachEv
inline void QCanvasGridPattern::detach()
{
    if (d)
        d.detach();
}
//  -----------------------------------------------------------------------

//  QCanvasGridPattern::QCanvasGridPattern()
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1Ev() {
  return new QCanvasGridPattern();
}

//  QCanvasGridPattern::QCanvasGridPattern(QPointF startPosition, QSizeF
//      cellSize)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1E7QPointF6QSizeF(
    const QPointF *startPosition,
    const QSizeF *cellSize) {
  return new QCanvasGridPattern(*startPosition, *cellSize);
}

//  QCanvasGridPattern::QCanvasGridPattern(qreal startX, qreal startY, qreal
//      cellWidth, qreal cellHeight)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1Edddd(
    qreal startX,
    qreal startY,
    qreal cellWidth,
    qreal cellHeight) {
  return new QCanvasGridPattern(startX, startY, cellWidth, cellHeight);
}

//  QCanvasGridPattern::QCanvasGridPattern(const QCanvasGridPattern &a0)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1ERKS_(
    const QCanvasGridPattern *a0) {
  return new QCanvasGridPattern(*a0);
}

//  QCanvasGridPattern &QCanvasGridPattern::operator=(const
//      QCanvasGridPattern &a0)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternaSERKS_(
    QCanvasGridPattern *self,
    const QCanvasGridPattern *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPattern &&a0)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1EOS_(
    QCanvasGridPattern *a0) {
  return new QCanvasGridPattern(std::move(*a0));
}

//  QCanvasGridPattern &QCanvasGridPattern::operator=(QCanvasGridPattern
//      &&other)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternaSEOS_(
    QCanvasGridPattern *self,
    QCanvasGridPattern *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCanvasGridPattern::~QCanvasGridPattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPatternD1Ev(QCanvasGridPattern *self) {
  delete self;
}

//  QCanvasBrush QCanvasGridPattern::operator QCanvasBrush() const
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZNK18QCanvasGridPatterncv12QCanvasBrushEv(
    const QCanvasGridPattern *self) {
  return new QCanvasBrush(self->operator QCanvasBrush());
}

//  QVariant QCanvasGridPattern::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QCanvasGridPatterncv8QVariantEv(
    const QCanvasGridPattern *self) {
  return new QVariant(self->operator QVariant());
}

//  QPointF QCanvasGridPattern::startPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QCanvasGridPattern13startPositionEv(
    const QCanvasGridPattern *self) {
  return new QPointF(self->startPosition());
}

//  void QCanvasGridPattern::setStartPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern16setStartPositionEdd(
    QCanvasGridPattern *self,
    qreal x,
    qreal y) {
  self->setStartPosition(x, y);
}

//  void QCanvasGridPattern::setStartPosition(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern16setStartPositionE7QPointF(
    QCanvasGridPattern *self,
    const QPointF *point) {
  self->setStartPosition(*point);
}

//  QSizeF QCanvasGridPattern::cellSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18QCanvasGridPattern8cellSizeEv(
    const QCanvasGridPattern *self) {
  return new QSizeF(self->cellSize());
}

//  void QCanvasGridPattern::setCellSize(qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern11setCellSizeEdd(
    QCanvasGridPattern *self,
    qreal width,
    qreal height) {
  self->setCellSize(width, height);
}

//  void QCanvasGridPattern::setCellSize(QSizeF size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern11setCellSizeE6QSizeF(
    QCanvasGridPattern *self,
    const QSizeF *size) {
  self->setCellSize(*size);
}

//  qreal QCanvasGridPattern::lineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCanvasGridPattern9lineWidthEv(
    const QCanvasGridPattern *self) {
  return self->lineWidth();
}

//  void QCanvasGridPattern::setLineWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern12setLineWidthEd(
    QCanvasGridPattern *self,
    qreal width) {
  self->setLineWidth(width);
}

//  qreal QCanvasGridPattern::feather() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCanvasGridPattern7featherEv(
    const QCanvasGridPattern *self) {
  return self->feather();
}

//  void QCanvasGridPattern::setFeather(qreal feather)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern10setFeatherEd(
    QCanvasGridPattern *self,
    qreal feather) {
  self->setFeather(feather);
}

//  qreal QCanvasGridPattern::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCanvasGridPattern8rotationEv(
    const QCanvasGridPattern *self) {
  return self->rotation();
}

//  void QCanvasGridPattern::setRotation(qreal rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern11setRotationEd(
    QCanvasGridPattern *self,
    qreal rotation) {
  self->setRotation(rotation);
}

//  QColor QCanvasGridPattern::lineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QCanvasGridPattern9lineColorEv(
    const QCanvasGridPattern *self) {
  return new QColor(self->lineColor());
}

//  void QCanvasGridPattern::setLineColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern12setLineColorE6QColor(
    QCanvasGridPattern *self,
    const QColor *color) {
  self->setLineColor(*color);
}

//  QColor QCanvasGridPattern::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QCanvasGridPattern15backgroundColorEv(
    const QCanvasGridPattern *self) {
  return new QColor(self->backgroundColor());
}

//  void QCanvasGridPattern::setBackgroundColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern18setBackgroundColorE6QColor(
    QCanvasGridPattern *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  void QCanvasGridPattern::swap(QCanvasGridPattern &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern4swapERS_(
    QCanvasGridPattern *self,
    QCanvasGridPattern *other) {
  self->swap(*other);
}

//  bool operator==(const QCanvasGridPattern &lhs, const QCanvasGridPattern
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QCanvasGridPatternS1_(
    const QCanvasGridPattern *lhs,
    const QCanvasGridPattern *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasGridPattern &lhs, const QCanvasGridPattern
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QCanvasGridPatternS1_(
    const QCanvasGridPattern *lhs,
    const QCanvasGridPattern *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QCanvasGridPattern::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasGridPattern6detachEv(QCanvasGridPattern *self) {
  self->detach();
}

//  QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPatternPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1EP25QCanvasGridPatternPrivate(
    QCanvasGridPatternPrivate *p) {
  return new QCanvasGridPattern(p);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QCanvasGridPattern &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK18QCanvasGridPattern(
    QDataStream *a0,
    const QCanvasGridPattern *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QCanvasGridPattern &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR18QCanvasGridPattern(
    QDataStream *a0,
    QCanvasGridPattern *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasGridPattern &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QCanvasGridPattern(
    const QDebug *a0,
    const QCanvasGridPattern *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
