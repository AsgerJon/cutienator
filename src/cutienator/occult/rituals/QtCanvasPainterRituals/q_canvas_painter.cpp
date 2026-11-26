//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspainter.h, Qt 6.12.0. Changes made here are lost.
#include <QtCanvasPainter/qcanvaspainter.h>
#include <QtGui/qcolor.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtGui/qtransform.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCanvasPainter/qcanvaspath.h>
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>
#include <QtCore/qsize.h>

//  QCanvasPainter::QCanvasPainter()
extern "C" Q_DECL_EXPORT
QCanvasPainter *ritual_ZN14QCanvasPainterC1Ev() {
  return new QCanvasPainter();
}

//  QCanvasPainter::~QCanvasPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainterD1Ev(QCanvasPainter *self) {
  delete self;
}

//  void QCanvasPainter::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4saveEv(QCanvasPainter *self) {
  self->save();
}

//  void QCanvasPainter::restore()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7restoreEv(QCanvasPainter *self) {
  self->restore();
}

//  void QCanvasPainter::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter5resetEv(QCanvasPainter *self) {
  self->reset();
}

//  void QCanvasPainter::setStrokeStyle(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter14setStrokeStyleE6QColor(
    QCanvasPainter *self,
    const QColor *color) {
  self->setStrokeStyle(*color);
}

//  void QCanvasPainter::setStrokeStyle(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter14setStrokeStyleERK12QCanvasBrush(
    QCanvasPainter *self,
    const QCanvasBrush *brush) {
  self->setStrokeStyle(*brush);
}

//  void QCanvasPainter::setFillStyle(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setFillStyleE6QColor(
    QCanvasPainter *self,
    const QColor *color) {
  self->setFillStyle(*color);
}

//  void QCanvasPainter::setFillStyle(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setFillStyleERK12QCanvasBrush(
    QCanvasPainter *self,
    const QCanvasBrush *brush) {
  self->setFillStyle(*brush);
}

//  void QCanvasPainter::setMiterLimit(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13setMiterLimitEd(
    QCanvasPainter *self,
    qreal limit) {
  self->setMiterLimit(limit);
}

//  void QCanvasPainter::setLineWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setLineWidthEd(
    QCanvasPainter *self,
    qreal width) {
  self->setLineWidth(width);
}

//  void QCanvasPainter::setLineCap(LineCap cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter10setLineCapENS_7LineCapE(
    QCanvasPainter *self,
    QCanvasPainter::LineCap cap) {
  self->setLineCap(cap);
}

//  void QCanvasPainter::setLineJoin(LineJoin join)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter11setLineJoinENS_8LineJoinE(
    QCanvasPainter *self,
    QCanvasPainter::LineJoin join) {
  self->setLineJoin(join);
}

//  void QCanvasPainter::setGlobalAlpha(qreal alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter14setGlobalAlphaEd(
    QCanvasPainter *self,
    qreal alpha) {
  self->setGlobalAlpha(alpha);
}

//  void QCanvasPainter::setGlobalCompositeOperation(CompositeOperation
//      operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter27setGlobalCompositeOperationENS_18CompositeOperationE(
    QCanvasPainter *self,
    QCanvasPainter::CompositeOperation operation) {
  self->setGlobalCompositeOperation(operation);
}

//  void QCanvasPainter::setGlobalBrightness(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter19setGlobalBrightnessEd(
    QCanvasPainter *self,
    qreal value) {
  self->setGlobalBrightness(value);
}

//  void QCanvasPainter::setGlobalContrast(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter17setGlobalContrastEd(
    QCanvasPainter *self,
    qreal value) {
  self->setGlobalContrast(value);
}

//  void QCanvasPainter::setGlobalSaturation(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter19setGlobalSaturationEd(
    QCanvasPainter *self,
    qreal value) {
  self->setGlobalSaturation(value);
}

//  void QCanvasPainter::setFillRule(FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter11setFillRuleENS_8FillRuleE(
    QCanvasPainter *self,
    QCanvasPainter::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  void QCanvasPainter::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter14resetTransformEv(QCanvasPainter *self) {
  self->resetTransform();
}

//  void QCanvasPainter::setTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setTransformERK10QTransform(
    QCanvasPainter *self,
    const QTransform *transform) {
  self->setTransform(*transform);
}

//  void QCanvasPainter::transform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9transformERK10QTransform(
    QCanvasPainter *self,
    const QTransform *transform) {
  self->transform(*transform);
}

//  void QCanvasPainter::translate(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9translateEdd(
    QCanvasPainter *self,
    qreal x,
    qreal y) {
  self->translate(x, y);
}

//  void QCanvasPainter::translate(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9translateE7QPointF(
    QCanvasPainter *self,
    const QPointF *point) {
  self->translate(*point);
}

//  void QCanvasPainter::rotate(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6rotateEd(QCanvasPainter *self, qreal angle) {
  self->rotate(angle);
}

//  void QCanvasPainter::skew(qreal angleX, qreal angleY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4skewEdd(
    QCanvasPainter *self,
    qreal angleX,
    qreal angleY) {
  self->skew(angleX, angleY);
}

//  void QCanvasPainter::scale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter5scaleEd(QCanvasPainter *self, qreal scale) {
  self->scale(scale);
}

//  void QCanvasPainter::scale(qreal scaleX, qreal scaleY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter5scaleEdd(
    QCanvasPainter *self,
    qreal scaleX,
    qreal scaleY) {
  self->scale(scaleX, scaleY);
}

//  QTransform QCanvasPainter::getTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK14QCanvasPainter12getTransformEv(
    const QCanvasPainter *self) {
  return new QTransform(self->getTransform());
}

//  void QCanvasPainter::setClipRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter11setClipRectEdddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->setClipRect(x, y, width, height);
}

//  void QCanvasPainter::setClipRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter11setClipRectERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->setClipRect(*rect);
}

//  void QCanvasPainter::resetClipping()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13resetClippingEv(QCanvasPainter *self) {
  self->resetClipping();
}

//  void QCanvasPainter::beginPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9beginPathEv(QCanvasPainter *self) {
  self->beginPath();
}

//  void QCanvasPainter::closePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9closePathEv(QCanvasPainter *self) {
  self->closePath();
}

//  void QCanvasPainter::moveTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6moveToEdd(
    QCanvasPainter *self,
    qreal x,
    qreal y) {
  self->moveTo(x, y);
}

//  void QCanvasPainter::moveTo(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6moveToE7QPointF(
    QCanvasPainter *self,
    const QPointF *point) {
  self->moveTo(*point);
}

//  void QCanvasPainter::lineTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6lineToEdd(
    QCanvasPainter *self,
    qreal x,
    qreal y) {
  self->lineTo(x, y);
}

//  void QCanvasPainter::lineTo(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6lineToE7QPointF(
    QCanvasPainter *self,
    const QPointF *point) {
  self->lineTo(*point);
}

//  void QCanvasPainter::bezierCurveTo(qreal cp1X, qreal cp1Y, qreal cp2X,
//      qreal cp2Y, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13bezierCurveToEdddddd(
    QCanvasPainter *self,
    qreal cp1X,
    qreal cp1Y,
    qreal cp2X,
    qreal cp2Y,
    qreal x,
    qreal y) {
  self->bezierCurveTo(cp1X, cp1Y, cp2X, cp2Y, x, y);
}

//  void QCanvasPainter::bezierCurveTo(QPointF controlPoint1, QPointF
//      controlPoint2, QPointF endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13bezierCurveToE7QPointFS0_S0_(
    QCanvasPainter *self,
    const QPointF *controlPoint1,
    const QPointF *controlPoint2,
    const QPointF *endPoint) {
  self->bezierCurveTo(*controlPoint1, *controlPoint2, *endPoint);
}

//  void QCanvasPainter::quadraticCurveTo(qreal cpX, qreal cpY, qreal x,
//      qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16quadraticCurveToEdddd(
    QCanvasPainter *self,
    qreal cpX,
    qreal cpY,
    qreal x,
    qreal y) {
  self->quadraticCurveTo(cpX, cpY, x, y);
}

//  void QCanvasPainter::quadraticCurveTo(QPointF controlPoint, QPointF
//      endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16quadraticCurveToE7QPointFS0_(
    QCanvasPainter *self,
    const QPointF *controlPoint,
    const QPointF *endPoint) {
  self->quadraticCurveTo(*controlPoint, *endPoint);
}

//  void QCanvasPainter::arcTo(qreal x1, qreal y1, qreal x2, qreal y2, qreal
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter5arcToEddddd(
    QCanvasPainter *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    qreal radius) {
  self->arcTo(x1, y1, x2, y2, radius);
}

//  void QCanvasPainter::arcTo(QPointF controlPoint1, QPointF controlPoint2,
//      qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter5arcToE7QPointFS0_d(
    QCanvasPainter *self,
    const QPointF *controlPoint1,
    const QPointF *controlPoint2,
    qreal radius) {
  self->arcTo(*controlPoint1, *controlPoint2, radius);
}

//  void QCanvasPainter::arc(qreal centerX, qreal centerY, qreal radius,
//      qreal a0, qreal a1, PathWinding direction, PathConnection connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter3arcEdddddNS_11PathWindingENS_14PathConnectionE(
    QCanvasPainter *self,
    qreal centerX,
    qreal centerY,
    qreal radius,
    qreal a0,
    qreal a1,
    QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection) {
  self->arc(centerX, centerY, radius, a0, a1, direction, connection);
}

//  void QCanvasPainter::arc(QPointF centerPoint, qreal radius, qreal a0,
//      qreal a1, PathWinding direction, PathConnection connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter3arcE7QPointFdddNS_11PathWindingENS_14PathConnectionE(
    QCanvasPainter *self,
    const QPointF *centerPoint,
    qreal radius,
    qreal a0,
    qreal a1,
    QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection) {
  self->arc(*centerPoint, radius, a0, a1, direction, connection);
}

//  void QCanvasPainter::rect(qreal x, qreal y, qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4rectEdddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->rect(x, y, width, height);
}

//  void QCanvasPainter::rect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4rectERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->rect(*rect);
}

//  void QCanvasPainter::roundRect(qreal x, qreal y, qreal width, qreal
//      height, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9roundRectEddddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    qreal radius) {
  self->roundRect(x, y, width, height, radius);
}

//  void QCanvasPainter::roundRect(const QRectF &rect, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9roundRectERK6QRectFd(
    QCanvasPainter *self,
    const QRectF *rect,
    qreal radius) {
  self->roundRect(*rect, radius);
}

//  void QCanvasPainter::roundRect(qreal x, qreal y, qreal width, qreal
//      height, qreal radiusTopLeft, qreal radiusTopRight, qreal
//      radiusBottomRight, qreal radiusBottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9roundRectEdddddddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    qreal radiusTopLeft,
    qreal radiusTopRight,
    qreal radiusBottomRight,
    qreal radiusBottomLeft) {
  self->roundRect(
      x,
      y,
      width,
      height,
      radiusTopLeft,
      radiusTopRight,
      radiusBottomRight,
      radiusBottomLeft);
}

//  void QCanvasPainter::roundRect(const QRectF &rect, qreal radiusTopLeft,
//      qreal radiusTopRight, qreal radiusBottomRight, qreal
//      radiusBottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9roundRectERK6QRectFdddd(
    QCanvasPainter *self,
    const QRectF *rect,
    qreal radiusTopLeft,
    qreal radiusTopRight,
    qreal radiusBottomRight,
    qreal radiusBottomLeft) {
  self->roundRect(
      *rect,
      radiusTopLeft,
      radiusTopRight,
      radiusBottomRight,
      radiusBottomLeft);
}

//  void QCanvasPainter::ellipse(qreal centerX, qreal centerY, qreal radiusX,
//      qreal radiusY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7ellipseEdddd(
    QCanvasPainter *self,
    qreal centerX,
    qreal centerY,
    qreal radiusX,
    qreal radiusY) {
  self->ellipse(centerX, centerY, radiusX, radiusY);
}

//  void QCanvasPainter::ellipse(QPointF centerPoint, qreal radiusX, qreal
//      radiusY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7ellipseE7QPointFdd(
    QCanvasPainter *self,
    const QPointF *centerPoint,
    qreal radiusX,
    qreal radiusY) {
  self->ellipse(*centerPoint, radiusX, radiusY);
}

//  void QCanvasPainter::ellipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7ellipseERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->ellipse(*rect);
}

//  void QCanvasPainter::circle(qreal centerX, qreal centerY, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6circleEddd(
    QCanvasPainter *self,
    qreal centerX,
    qreal centerY,
    qreal radius) {
  self->circle(centerX, centerY, radius);
}

//  void QCanvasPainter::circle(QPointF centerPoint, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6circleE7QPointFd(
    QCanvasPainter *self,
    const QPointF *centerPoint,
    qreal radius) {
  self->circle(*centerPoint, radius);
}

//  void QCanvasPainter::addPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7addPathERK12QPainterPath(
    QCanvasPainter *self,
    const QPainterPath *path) {
  self->addPath(*path);
}

//  void QCanvasPainter::addPath(const QCanvasPath &path, const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7addPathERK11QCanvasPathRK10QTransform(
    QCanvasPainter *self,
    const QCanvasPath *path,
    const QTransform *transform) {
  self->addPath(*path, *transform);
}

//  void QCanvasPainter::addPath(const QCanvasPath &path, qsizetype start,
//      qsizetype count, const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7addPathERK11QCanvasPathxxRK10QTransform(
    QCanvasPainter *self,
    const QCanvasPath *path,
    qsizetype start,
    qsizetype count,
    const QTransform *transform) {
  self->addPath(*path, start, count, *transform);
}

//  void QCanvasPainter::setPathWinding(PathWinding winding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter14setPathWindingENS_11PathWindingE(
    QCanvasPainter *self,
    QCanvasPainter::PathWinding winding) {
  self->setPathWinding(winding);
}

//  void QCanvasPainter::beginSolidSubPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter17beginSolidSubPathEv(QCanvasPainter *self) {
  self->beginSolidSubPath();
}

//  void QCanvasPainter::beginHoleSubPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16beginHoleSubPathEv(QCanvasPainter *self) {
  self->beginHoleSubPath();
}

//  void QCanvasPainter::fill()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4fillEv(QCanvasPainter *self) {
  self->fill();
}

//  void QCanvasPainter::fill(FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4fillENS_8FillRuleE(
    QCanvasPainter *self,
    QCanvasPainter::FillRule fillRule) {
  self->fill(fillRule);
}

//  void QCanvasPainter::stroke()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6strokeEv(QCanvasPainter *self) {
  self->stroke();
}

//  void QCanvasPainter::fill(const QCanvasPath &path, int pathGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4fillERK11QCanvasPathi(
    QCanvasPainter *self,
    const QCanvasPath *path,
    int pathGroup) {
  self->fill(*path, pathGroup);
}

//  void QCanvasPainter::fill(const QCanvasPath &path, FillRule fillRule, int
//      pathGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter4fillERK11QCanvasPathNS_8FillRuleEi(
    QCanvasPainter *self,
    const QCanvasPath *path,
    QCanvasPainter::FillRule fillRule,
    int pathGroup) {
  self->fill(*path, fillRule, pathGroup);
}

//  void QCanvasPainter::stroke(const QCanvasPath &path, int pathGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter6strokeERK11QCanvasPathi(
    QCanvasPainter *self,
    const QCanvasPath *path,
    int pathGroup) {
  self->stroke(*path, pathGroup);
}

//  void QCanvasPainter::fillRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter8fillRectEdddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->fillRect(x, y, width, height);
}

//  void QCanvasPainter::fillRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter8fillRectERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->fillRect(*rect);
}

//  void QCanvasPainter::clearRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9clearRectEdddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->clearRect(x, y, width, height);
}

//  void QCanvasPainter::clearRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9clearRectERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->clearRect(*rect);
}

//  void QCanvasPainter::strokeRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter10strokeRectEdddd(
    QCanvasPainter *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->strokeRect(x, y, width, height);
}

//  void QCanvasPainter::strokeRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter10strokeRectERK6QRectF(
    QCanvasPainter *self,
    const QRectF *rect) {
  self->strokeRect(*rect);
}

//  void QCanvasPainter::drawBoxShadow(const QCanvasBoxShadow &shadow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13drawBoxShadowERK16QCanvasBoxShadow(
    QCanvasPainter *self,
    const QCanvasBoxShadow *shadow) {
  self->drawBoxShadow(*shadow);
}

//  void QCanvasPainter::drawImage(const QCanvasImage &image, qreal x, qreal
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImagedd(
    QCanvasPainter *self,
    const QCanvasImage *image,
    qreal x,
    qreal y) {
  self->drawImage(*image, x, y);
}

//  void QCanvasPainter::drawImage(const QCanvasImage &image, qreal x, qreal
//      y, qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImagedddd(
    QCanvasPainter *self,
    const QCanvasImage *image,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->drawImage(*image, x, y, width, height);
}

//  void QCanvasPainter::drawImage(const QCanvasImage &image, const QRectF
//      &destinationRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImageRK6QRectF(
    QCanvasPainter *self,
    const QCanvasImage *image,
    const QRectF *destinationRect) {
  self->drawImage(*image, *destinationRect);
}

//  void QCanvasPainter::drawImage(const QCanvasImage &image, const QRectF
//      &sourceRect, const QRectF &destinationRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter9drawImageERK12QCanvasImageRK6QRectFS5_(
    QCanvasPainter *self,
    const QCanvasImage *image,
    const QRectF *sourceRect,
    const QRectF *destinationRect) {
  self->drawImage(*image, *sourceRect, *destinationRect);
}

//  void QCanvasPainter::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter7setFontERK5QFont(
    QCanvasPainter *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QCanvasPainter::setTextAlign(QCanvasPainter::TextAlign align)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setTextAlignENS_9TextAlignE(
    QCanvasPainter *self,
    QCanvasPainter::TextAlign align) {
  self->setTextAlign(align);
}

//  void QCanvasPainter::setTextBaseline(QCanvasPainter::TextBaseline
//      baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter15setTextBaselineENS_12TextBaselineE(
    QCanvasPainter *self,
    QCanvasPainter::TextBaseline baseline) {
  self->setTextBaseline(baseline);
}

//  void QCanvasPainter::setTextDirection(QCanvasPainter::TextDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16setTextDirectionENS_13TextDirectionE(
    QCanvasPainter *self,
    QCanvasPainter::TextDirection direction) {
  self->setTextDirection(direction);
}

//  void QCanvasPainter::setTextWrapMode(QCanvasPainter::WrapMode wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter15setTextWrapModeENS_8WrapModeE(
    QCanvasPainter *self,
    QCanvasPainter::WrapMode wrapMode) {
  self->setTextWrapMode(wrapMode);
}

//  void QCanvasPainter::setTextLineHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter17setTextLineHeightEd(
    QCanvasPainter *self,
    qreal height) {
  self->setTextLineHeight(height);
}

//  void QCanvasPainter::setTextAntialias(qreal antialias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16setTextAntialiasEd(
    QCanvasPainter *self,
    qreal antialias) {
  self->setTextAntialias(antialias);
}

//  void QCanvasPainter::fillText(const QString &text, qreal x, qreal y,
//      qreal maxWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter8fillTextERK7QStringddd(
    QCanvasPainter *self,
    const QString *text,
    qreal x,
    qreal y,
    qreal maxWidth) {
  self->fillText(*text, x, y, maxWidth);
}

//  void QCanvasPainter::fillText(const QString &text, QPointF point, qreal
//      maxWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter8fillTextERK7QString7QPointFd(
    QCanvasPainter *self,
    const QString *text,
    const QPointF *point,
    qreal maxWidth) {
  self->fillText(*text, *point, maxWidth);
}

//  void QCanvasPainter::fillText(const QString &text, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter8fillTextERK7QStringRK6QRectF(
    QCanvasPainter *self,
    const QString *text,
    const QRectF *rect) {
  self->fillText(*text, *rect);
}

//  QRectF QCanvasPainter::textBoundingBox(const QString &text, qreal x,
//      qreal y, qreal maxWidth) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QStringddd(
    const QCanvasPainter *self,
    const QString *text,
    qreal x,
    qreal y,
    qreal maxWidth) {
  return new QRectF(self->textBoundingBox(*text, x, y, maxWidth));
}

//  QRectF QCanvasPainter::textBoundingBox(const QString &text, QPointF
//      point, qreal maxWidth) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QString7QPointFd(
    const QCanvasPainter *self,
    const QString *text,
    const QPointF *point,
    qreal maxWidth) {
  return new QRectF(self->textBoundingBox(*text, *point, maxWidth));
}

//  QRectF QCanvasPainter::textBoundingBox(const QString &text, const QRectF
//      &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QCanvasPainter15textBoundingBoxERK7QStringRK6QRectF(
    const QCanvasPainter *self,
    const QString *text,
    const QRectF *rect) {
  return new QRectF(self->textBoundingBox(*text, *rect));
}

//  void QCanvasPainter::setAntialias(qreal antialias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter12setAntialiasEd(
    QCanvasPainter *self,
    qreal antialias) {
  self->setAntialias(antialias);
}

//  void QCanvasPainter::setWindingEnforce(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter17setWindingEnforceEb(
    QCanvasPainter *self,
    bool enabled) {
  self->setWindingEnforce(enabled);
}

//  void QCanvasPainter::setHighQualityStroking(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter22setHighQualityStrokingEb(
    QCanvasPainter *self,
    bool enabled) {
  self->setHighQualityStroking(enabled);
}

//  QCanvasImage QCanvasPainter::addImage(const QImage &image,
//      QCanvasPainter::ImageFlags flags)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN14QCanvasPainter8addImageERK6QImage6QFlagsINS_9ImageFlagEE(
    QCanvasPainter *self,
    const QImage *image,
    int flags) {
  return new QCanvasImage(
      self->addImage(
          *image,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags)));
}

//  QCanvasImage QCanvasPainter::addImage(QRhiTexture *texture,
//      QCanvasPainter::ImageFlags flags)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN14QCanvasPainter8addImageEP11QRhiTexture6QFlagsINS_9ImageFlagEE(
    QCanvasPainter *self,
    QRhiTexture *texture,
    int flags) {
  return new QCanvasImage(
      self->addImage(
          texture,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags)));
}

//  QCanvasImage QCanvasPainter::addImage(const QCanvasOffscreenCanvas
//      &canvas, QCanvasPainter::ImageFlags flags)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN14QCanvasPainter8addImageERK22QCanvasOffscreenCanvas6QFlagsINS_9ImageFlagEE(
    QCanvasPainter *self,
    const QCanvasOffscreenCanvas *canvas,
    int flags) {
  return new QCanvasImage(
      self->addImage(
          *canvas,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags)));
}

//  void QCanvasPainter::removeImage(const QCanvasImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter11removeImageERK12QCanvasImage(
    QCanvasPainter *self,
    const QCanvasImage *image) {
  self->removeImage(*image);
}

//  void QCanvasPainter::cleanupResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter16cleanupResourcesEv(QCanvasPainter *self) {
  self->cleanupResources();
}

//  qsizetype QCanvasPainter::activeImageMemoryUsage() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QCanvasPainter22activeImageMemoryUsageEv(
    const QCanvasPainter *self) {
  return self->activeImageMemoryUsage();
}

//  qsizetype QCanvasPainter::activeImageCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QCanvasPainter16activeImageCountEv(
    const QCanvasPainter *self) {
  return self->activeImageCount();
}

//  void QCanvasPainter::removePathGroup(int pathGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter15removePathGroupEi(
    QCanvasPainter *self,
    int pathGroup) {
  self->removePathGroup(pathGroup);
}

//  QCanvasOffscreenCanvas QCanvasPainter::createCanvas(QSize pixelSize, int
//      sampleCount, QCanvasOffscreenCanvas::Flags flags)
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN14QCanvasPainter12createCanvasE5QSizei6QFlagsIN22QCanvasOffscreenCanvas4FlagEE(
    QCanvasPainter *self,
    const QSize *pixelSize,
    int sampleCount,
    int flags) {
  return new QCanvasOffscreenCanvas(
      self->createCanvas(
          *pixelSize,
          sampleCount,
          QFlags<QCanvasOffscreenCanvas::Flag>::fromInt(flags)));
}

//  void QCanvasPainter::destroyCanvas(QCanvasOffscreenCanvas &canvas)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCanvasPainter13destroyCanvasER22QCanvasOffscreenCanvas(
    QCanvasPainter *self,
    QCanvasOffscreenCanvas *canvas) {
  self->destroyCanvas(*canvas);
}

//  QCanvasPainterPrivate *QCanvasPainter::d_func()
extern "C" Q_DECL_EXPORT
QCanvasPainterPrivate *ritual_ZN14QCanvasPainter6d_funcEv(
    QCanvasPainter *self) {
  return self->d_func();
}

//  const QCanvasPainterPrivate *QCanvasPainter::d_func() const
extern "C" Q_DECL_EXPORT
const QCanvasPainterPrivate *ritual_ZNK14QCanvasPainter6d_funcEv(
    const QCanvasPainter *self) {
  return self->d_func();
}
