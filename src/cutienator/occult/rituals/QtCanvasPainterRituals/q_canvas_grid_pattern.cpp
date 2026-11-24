//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasgridpattern.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvasgridpattern.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>

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

//  QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPatternPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasGridPattern *ritual_ZN18QCanvasGridPatternC1EP25QCanvasGridPatternPrivate(
    QCanvasGridPatternPrivate *p) {
  return new QCanvasGridPattern(p);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasGridPattern &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QCanvasGridPattern(
    const QDebug *a0,
    const QCanvasGridPattern *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
