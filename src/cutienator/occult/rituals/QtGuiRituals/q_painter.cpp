//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainter.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfontinfo.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>
#include <QtGui/qregion.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qline.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpicture.h>
#include <QtGui/qimage.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qstatictext.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextoption.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qlist.h>

//  QPainter::QPainter()
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN8QPainterC1Ev() {
  return new QPainter();
}

//  QPainter::QPainter(QPaintDevice *a0)
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN8QPainterC1EP12QPaintDevice(QPaintDevice *a0) {
  return new QPainter(a0);
}

//  QPainter::~QPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainterD1Ev(QPainter *self) {
  delete self;
}

//  QPaintDevice *QPainter::device() const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK8QPainter6deviceEv(const QPainter *self) {
  return self->device();
}

//  bool QPainter::begin(QPaintDevice *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPainter5beginEP12QPaintDevice(
    QPainter *self,
    QPaintDevice *a0) {
  return self->begin(a0);
}

//  bool QPainter::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QPainter3endEv(QPainter *self) {
  return self->end();
}

//  bool QPainter::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPainter8isActiveEv(const QPainter *self) {
  return self->isActive();
}

//  void QPainter::setCompositionMode(CompositionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter18setCompositionModeENS_15CompositionModeE(
    QPainter *self,
    QPainter::CompositionMode mode) {
  self->setCompositionMode(mode);
}

//  CompositionMode QPainter::compositionMode() const
extern "C" Q_DECL_EXPORT
QPainter::CompositionMode ritual_ZNK8QPainter15compositionModeEv(
    const QPainter *self) {
  return self->compositionMode();
}

//  const QFont &QPainter::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK8QPainter4fontEv(const QPainter *self) {
  return new QFont(self->font());
}

//  void QPainter::setFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7setFontERK5QFont(QPainter *self, const QFont *f) {
  self->setFont(*f);
}

//  QFontMetrics QPainter::fontMetrics() const
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZNK8QPainter11fontMetricsEv(const QPainter *self) {
  return new QFontMetrics(self->fontMetrics());
}

//  QFontInfo QPainter::fontInfo() const
extern "C" Q_DECL_EXPORT
QFontInfo *ritual_ZNK8QPainter8fontInfoEv(const QPainter *self) {
  return new QFontInfo(self->fontInfo());
}

//  void QPainter::setPen(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter6setPenERK6QColor(
    QPainter *self,
    const QColor *color) {
  self->setPen(*color);
}

//  void QPainter::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter6setPenERK4QPen(QPainter *self, const QPen *pen) {
  self->setPen(*pen);
}

//  void QPainter::setPen(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter6setPenEN2Qt8PenStyleE(
    QPainter *self,
    Qt::PenStyle style) {
  self->setPen(style);
}

//  const QPen &QPainter::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK8QPainter3penEv(const QPainter *self) {
  return new QPen(self->pen());
}

//  void QPainter::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8setBrushERK6QBrush(
    QPainter *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  void QPainter::setBrush(Qt::BrushStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8setBrushEN2Qt10BrushStyleE(
    QPainter *self,
    Qt::BrushStyle style) {
  self->setBrush(style);
}

//  void QPainter::setBrush(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8setBrushE6QColor(
    QPainter *self,
    const QColor *color) {
  self->setBrush(*color);
}

//  void QPainter::setBrush(Qt::GlobalColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8setBrushEN2Qt11GlobalColorE(
    QPainter *self,
    Qt::GlobalColor color) {
  self->setBrush(color);
}

//  const QBrush &QPainter::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPainter5brushEv(const QPainter *self) {
  return new QBrush(self->brush());
}

//  void QPainter::setBackgroundMode(Qt::BGMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17setBackgroundModeEN2Qt6BGModeE(
    QPainter *self,
    Qt::BGMode mode) {
  self->setBackgroundMode(mode);
}

//  Qt::BGMode QPainter::backgroundMode() const
extern "C" Q_DECL_EXPORT
Qt::BGMode ritual_ZNK8QPainter14backgroundModeEv(const QPainter *self) {
  return self->backgroundMode();
}

//  QPoint QPainter::brushOrigin() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8QPainter11brushOriginEv(const QPainter *self) {
  return new QPoint(self->brushOrigin());
}

//  QPointF QPainter::brushOriginF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QPainter12brushOriginFEv(const QPainter *self) {
  return new QPointF(self->brushOriginF());
}

//  void QPainter::setBrushOrigin(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14setBrushOriginEii(QPainter *self, int x, int y) {
  self->setBrushOrigin(x, y);
}

//  void QPainter::setBrushOrigin(const QPoint &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14setBrushOriginERK6QPoint(
    QPainter *self,
    const QPoint *a0) {
  self->setBrushOrigin(*a0);
}

//  void QPainter::setBrushOrigin(const QPointF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14setBrushOriginERK7QPointF(
    QPainter *self,
    const QPointF *a0) {
  self->setBrushOrigin(*a0);
}

//  void QPainter::setBackground(const QBrush &bg)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter13setBackgroundERK6QBrush(
    QPainter *self,
    const QBrush *bg) {
  self->setBackground(*bg);
}

//  const QBrush &QPainter::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPainter10backgroundEv(const QPainter *self) {
  return new QBrush(self->background());
}

//  qreal QPainter::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QPainter7opacityEv(const QPainter *self) {
  return self->opacity();
}

//  void QPainter::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10setOpacityEd(QPainter *self, qreal opacity) {
  self->setOpacity(opacity);
}

//  QRegion QPainter::clipRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK8QPainter10clipRegionEv(const QPainter *self) {
  return new QRegion(self->clipRegion());
}

//  QPainterPath QPainter::clipPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK8QPainter8clipPathEv(const QPainter *self) {
  return new QPainterPath(self->clipPath());
}

//  void QPainter::setClipRect(const QRectF &a0, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setClipRectERK6QRectFN2Qt13ClipOperationE(
    QPainter *self,
    const QRectF *a0,
    Qt::ClipOperation op) {
  self->setClipRect(*a0, op);
}

//  void QPainter::setClipRect(const QRect &a0, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setClipRectERK5QRectN2Qt13ClipOperationE(
    QPainter *self,
    const QRect *a0,
    Qt::ClipOperation op) {
  self->setClipRect(*a0, op);
}

//  void QPainter::setClipRect(int x, int y, int w, int h, Qt::ClipOperation
//      op)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setClipRectEiiiiN2Qt13ClipOperationE(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    Qt::ClipOperation op) {
  self->setClipRect(x, y, w, h, op);
}

//  void QPainter::setClipRegion(const QRegion &a0, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter13setClipRegionERK7QRegionN2Qt13ClipOperationE(
    QPainter *self,
    const QRegion *a0,
    Qt::ClipOperation op) {
  self->setClipRegion(*a0, op);
}

//  void QPainter::setClipPath(const QPainterPath &path, Qt::ClipOperation
//      op)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setClipPathERK12QPainterPathN2Qt13ClipOperationE(
    QPainter *self,
    const QPainterPath *path,
    Qt::ClipOperation op) {
  self->setClipPath(*path, op);
}

//  void QPainter::setClipping(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setClippingEb(QPainter *self, bool enable) {
  self->setClipping(enable);
}

//  bool QPainter::hasClipping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPainter11hasClippingEv(const QPainter *self) {
  return self->hasClipping();
}

//  QRectF QPainter::clipBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QPainter16clipBoundingRectEv(const QPainter *self) {
  return new QRectF(self->clipBoundingRect());
}

//  void QPainter::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter4saveEv(QPainter *self) {
  self->save();
}

//  void QPainter::restore()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7restoreEv(QPainter *self) {
  self->restore();
}

//  void QPainter::setTransform(const QTransform &transform, bool combine)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12setTransformERK10QTransformb(
    QPainter *self,
    const QTransform *transform,
    bool combine) {
  self->setTransform(*transform, combine);
}

//  const QTransform &QPainter::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK8QPainter9transformEv(const QPainter *self) {
  return new QTransform(self->transform());
}

//  const QTransform &QPainter::deviceTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK8QPainter15deviceTransformEv(const QPainter *self) {
  return new QTransform(self->deviceTransform());
}

//  void QPainter::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14resetTransformEv(QPainter *self) {
  self->resetTransform();
}

//  void QPainter::setWorldTransform(const QTransform &matrix, bool combine)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17setWorldTransformERK10QTransformb(
    QPainter *self,
    const QTransform *matrix,
    bool combine) {
  self->setWorldTransform(*matrix, combine);
}

//  const QTransform &QPainter::worldTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK8QPainter14worldTransformEv(const QPainter *self) {
  return new QTransform(self->worldTransform());
}

//  QTransform QPainter::combinedTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK8QPainter17combinedTransformEv(const QPainter *self) {
  return new QTransform(self->combinedTransform());
}

//  void QPainter::setWorldMatrixEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter21setWorldMatrixEnabledEb(
    QPainter *self,
    bool enabled) {
  self->setWorldMatrixEnabled(enabled);
}

//  bool QPainter::worldMatrixEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPainter18worldMatrixEnabledEv(const QPainter *self) {
  return self->worldMatrixEnabled();
}

//  void QPainter::scale(qreal sx, qreal sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter5scaleEdd(QPainter *self, qreal sx, qreal sy) {
  self->scale(sx, sy);
}

//  void QPainter::shear(qreal sh, qreal sv)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter5shearEdd(QPainter *self, qreal sh, qreal sv) {
  self->shear(sh, sv);
}

//  void QPainter::rotate(qreal a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter6rotateEd(QPainter *self, qreal a) {
  self->rotate(a);
}

//  void QPainter::translate(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9translateERK7QPointF(
    QPainter *self,
    const QPointF *offset) {
  self->translate(*offset);
}

//  void QPainter::translate(const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9translateERK6QPoint(
    QPainter *self,
    const QPoint *offset) {
  self->translate(*offset);
}

//  void QPainter::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9translateEdd(QPainter *self, qreal dx, qreal dy) {
  self->translate(dx, dy);
}

//  QRect QPainter::window() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QPainter6windowEv(const QPainter *self) {
  return new QRect(self->window());
}

//  void QPainter::setWindow(const QRect &window)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9setWindowERK5QRect(
    QPainter *self,
    const QRect *window) {
  self->setWindow(*window);
}

//  void QPainter::setWindow(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9setWindowEiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h) {
  self->setWindow(x, y, w, h);
}

//  QRect QPainter::viewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QPainter8viewportEv(const QPainter *self) {
  return new QRect(self->viewport());
}

//  void QPainter::setViewport(const QRect &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setViewportERK5QRect(
    QPainter *self,
    const QRect *viewport) {
  self->setViewport(*viewport);
}

//  void QPainter::setViewport(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11setViewportEiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h) {
  self->setViewport(x, y, w, h);
}

//  void QPainter::setViewTransformEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter23setViewTransformEnabledEb(
    QPainter *self,
    bool enable) {
  self->setViewTransformEnabled(enable);
}

//  bool QPainter::viewTransformEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPainter20viewTransformEnabledEv(const QPainter *self) {
  return self->viewTransformEnabled();
}

//  void QPainter::strokePath(const QPainterPath &path, const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10strokePathERK12QPainterPathRK4QPen(
    QPainter *self,
    const QPainterPath *path,
    const QPen *pen) {
  self->strokePath(*path, *pen);
}

//  void QPainter::fillPath(const QPainterPath &path, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillPathERK12QPainterPathRK6QBrush(
    QPainter *self,
    const QPainterPath *path,
    const QBrush *brush) {
  self->fillPath(*path, *brush);
}

//  void QPainter::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawPathERK12QPainterPath(
    QPainter *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPainter::drawPoint(const QPointF &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawPointERK7QPointF(
    QPainter *self,
    const QPointF *pt) {
  self->drawPoint(*pt);
}

//  void QPainter::drawPoint(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawPointERK6QPoint(
    QPainter *self,
    const QPoint *p) {
  self->drawPoint(*p);
}

//  void QPainter::drawPoint(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawPointEii(QPainter *self, int x, int y) {
  self->drawPoint(x, y);
}

//  void QPainter::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPointsEPK7QPointFi(
    QPainter *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPainter::drawPoints(const QPolygonF &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPointsERK9QPolygonF(
    QPainter *self,
    const QPolygonF *points) {
  self->drawPoints(*points);
}

//  void QPainter::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPointsEPK6QPointi(
    QPainter *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPainter::drawPoints(const QPolygon &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPointsERK8QPolygon(
    QPainter *self,
    const QPolygon *points) {
  self->drawPoints(*points);
}

//  void QPainter::drawLine(const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawLineERK6QLineF(
    QPainter *self,
    const QLineF *line) {
  self->drawLine(*line);
}

//  void QPainter::drawLine(const QLine &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawLineERK5QLine(
    QPainter *self,
    const QLine *line) {
  self->drawLine(*line);
}

//  void QPainter::drawLine(int x1, int y1, int x2, int y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawLineEiiii(
    QPainter *self,
    int x1,
    int y1,
    int x2,
    int y2) {
  self->drawLine(x1, y1, x2, y2);
}

//  void QPainter::drawLine(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawLineERK6QPointS2_(
    QPainter *self,
    const QPoint *p1,
    const QPoint *p2) {
  self->drawLine(*p1, *p2);
}

//  void QPainter::drawLine(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawLineERK7QPointFS2_(
    QPainter *self,
    const QPointF *p1,
    const QPointF *p2) {
  self->drawLine(*p1, *p2);
}

//  void QPainter::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesEPK6QLineFi(
    QPainter *self,
    const QLineF *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPainter::drawLines(const QList<QLineF> &lines)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesERK5QListI6QLineFE(
    QPainter *self,
    const QList<QLineF> *lines) {
  self->drawLines(*lines);
}

//  void QPainter::drawLines(const QPointF *pointPairs, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesEPK7QPointFi(
    QPainter *self,
    const QPointF *pointPairs,
    int lineCount) {
  self->drawLines(pointPairs, lineCount);
}

//  void QPainter::drawLines(const QList<QPointF> &pointPairs)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesERK5QListI7QPointFE(
    QPainter *self,
    const QList<QPointF> *pointPairs) {
  self->drawLines(*pointPairs);
}

//  void QPainter::drawLines(const QLine *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesEPK5QLinei(
    QPainter *self,
    const QLine *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPainter::drawLines(const QList<QLine> &lines)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesERK5QListI5QLineE(
    QPainter *self,
    const QList<QLine> *lines) {
  self->drawLines(*lines);
}

//  void QPainter::drawLines(const QPoint *pointPairs, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesEPK6QPointi(
    QPainter *self,
    const QPoint *pointPairs,
    int lineCount) {
  self->drawLines(pointPairs, lineCount);
}

//  void QPainter::drawLines(const QList<QPoint> &pointPairs)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawLinesERK5QListI6QPointE(
    QPainter *self,
    const QList<QPoint> *pointPairs) {
  self->drawLines(*pointPairs);
}

//  void QPainter::drawRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawRectERK6QRectF(
    QPainter *self,
    const QRectF *rect) {
  self->drawRect(*rect);
}

//  void QPainter::drawRect(int x1, int y1, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawRectEiiii(
    QPainter *self,
    int x1,
    int y1,
    int w,
    int h) {
  self->drawRect(x1, y1, w, h);
}

//  void QPainter::drawRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawRectERK5QRect(
    QPainter *self,
    const QRect *rect) {
  self->drawRect(*rect);
}

//  void QPainter::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawRectsEPK6QRectFi(
    QPainter *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPainter::drawRects(const QList<QRectF> &rectangles)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawRectsERK5QListI6QRectFE(
    QPainter *self,
    const QList<QRectF> *rectangles) {
  self->drawRects(*rectangles);
}

//  void QPainter::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawRectsEPK5QRecti(
    QPainter *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPainter::drawRects(const QList<QRect> &rectangles)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawRectsERK5QListI5QRectE(
    QPainter *self,
    const QList<QRect> *rectangles) {
  self->drawRects(*rectangles);
}

//  void QPainter::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawEllipseERK6QRectF(
    QPainter *self,
    const QRectF *r) {
  self->drawEllipse(*r);
}

//  void QPainter::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawEllipseERK5QRect(
    QPainter *self,
    const QRect *r) {
  self->drawEllipse(*r);
}

//  void QPainter::drawEllipse(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawEllipseEiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h) {
  self->drawEllipse(x, y, w, h);
}

//  void QPainter::drawEllipse(const QPointF &center, qreal rx, qreal ry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawEllipseERK7QPointFdd(
    QPainter *self,
    const QPointF *center,
    qreal rx,
    qreal ry) {
  self->drawEllipse(*center, rx, ry);
}

//  void QPainter::drawEllipse(const QPoint &center, int rx, int ry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawEllipseERK6QPointii(
    QPainter *self,
    const QPoint *center,
    int rx,
    int ry) {
  self->drawEllipse(*center, rx, ry);
}

//  void QPainter::drawPolyline(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawPolylineEPK7QPointFi(
    QPainter *self,
    const QPointF *points,
    int pointCount) {
  self->drawPolyline(points, pointCount);
}

//  void QPainter::drawPolyline(const QPolygonF &polyline)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawPolylineERK9QPolygonF(
    QPainter *self,
    const QPolygonF *polyline) {
  self->drawPolyline(*polyline);
}

//  void QPainter::drawPolyline(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawPolylineEPK6QPointi(
    QPainter *self,
    const QPoint *points,
    int pointCount) {
  self->drawPolyline(points, pointCount);
}

//  void QPainter::drawPolyline(const QPolygon &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawPolylineERK8QPolygon(
    QPainter *self,
    const QPolygon *polygon) {
  self->drawPolyline(*polygon);
}

//  void QPainter::drawPolygon(const QPointF *points, int pointCount,
//      Qt::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPolygonEPK7QPointFiN2Qt8FillRuleE(
    QPainter *self,
    const QPointF *points,
    int pointCount,
    Qt::FillRule fillRule) {
  self->drawPolygon(points, pointCount, fillRule);
}

//  void QPainter::drawPolygon(const QPolygonF &polygon, Qt::FillRule
//      fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPolygonERK9QPolygonFN2Qt8FillRuleE(
    QPainter *self,
    const QPolygonF *polygon,
    Qt::FillRule fillRule) {
  self->drawPolygon(*polygon, fillRule);
}

//  void QPainter::drawPolygon(const QPoint *points, int pointCount,
//      Qt::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPolygonEPK6QPointiN2Qt8FillRuleE(
    QPainter *self,
    const QPoint *points,
    int pointCount,
    Qt::FillRule fillRule) {
  self->drawPolygon(points, pointCount, fillRule);
}

//  void QPainter::drawPolygon(const QPolygon &polygon, Qt::FillRule
//      fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPolygonERK8QPolygonN2Qt8FillRuleE(
    QPainter *self,
    const QPolygon *polygon,
    Qt::FillRule fillRule) {
  self->drawPolygon(*polygon, fillRule);
}

//  void QPainter::drawConvexPolygon(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17drawConvexPolygonEPK7QPointFi(
    QPainter *self,
    const QPointF *points,
    int pointCount) {
  self->drawConvexPolygon(points, pointCount);
}

//  void QPainter::drawConvexPolygon(const QPolygonF &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17drawConvexPolygonERK9QPolygonF(
    QPainter *self,
    const QPolygonF *polygon) {
  self->drawConvexPolygon(*polygon);
}

//  void QPainter::drawConvexPolygon(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17drawConvexPolygonEPK6QPointi(
    QPainter *self,
    const QPoint *points,
    int pointCount) {
  self->drawConvexPolygon(points, pointCount);
}

//  void QPainter::drawConvexPolygon(const QPolygon &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17drawConvexPolygonERK8QPolygon(
    QPainter *self,
    const QPolygon *polygon) {
  self->drawConvexPolygon(*polygon);
}

//  void QPainter::drawArc(const QRectF &rect, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawArcERK6QRectFii(
    QPainter *self,
    const QRectF *rect,
    int a,
    int alen) {
  self->drawArc(*rect, a, alen);
}

//  void QPainter::drawArc(const QRect &a0, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawArcERK5QRectii(
    QPainter *self,
    const QRect *a0,
    int a,
    int alen) {
  self->drawArc(*a0, a, alen);
}

//  void QPainter::drawArc(int x, int y, int w, int h, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawArcEiiiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    int a,
    int alen) {
  self->drawArc(x, y, w, h, a, alen);
}

//  void QPainter::drawPie(const QRectF &rect, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawPieERK6QRectFii(
    QPainter *self,
    const QRectF *rect,
    int a,
    int alen) {
  self->drawPie(*rect, a, alen);
}

//  void QPainter::drawPie(int x, int y, int w, int h, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawPieEiiiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    int a,
    int alen) {
  self->drawPie(x, y, w, h, a, alen);
}

//  void QPainter::drawPie(const QRect &a0, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter7drawPieERK5QRectii(
    QPainter *self,
    const QRect *a0,
    int a,
    int alen) {
  self->drawPie(*a0, a, alen);
}

//  void QPainter::drawChord(const QRectF &rect, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawChordERK6QRectFii(
    QPainter *self,
    const QRectF *rect,
    int a,
    int alen) {
  self->drawChord(*rect, a, alen);
}

//  void QPainter::drawChord(int x, int y, int w, int h, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawChordEiiiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    int a,
    int alen) {
  self->drawChord(x, y, w, h, a, alen);
}

//  void QPainter::drawChord(const QRect &a0, int a, int alen)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawChordERK5QRectii(
    QPainter *self,
    const QRect *a0,
    int a,
    int alen) {
  self->drawChord(*a0, a, alen);
}

//  void QPainter::drawRoundedRect(const QRectF &rect, qreal xRadius, qreal
//      yRadius, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawRoundedRectERK6QRectFddN2Qt8SizeModeE(
    QPainter *self,
    const QRectF *rect,
    qreal xRadius,
    qreal yRadius,
    Qt::SizeMode mode) {
  self->drawRoundedRect(*rect, xRadius, yRadius, mode);
}

//  void QPainter::drawRoundedRect(int x, int y, int w, int h, qreal xRadius,
//      qreal yRadius, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawRoundedRectEiiiiddN2Qt8SizeModeE(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    qreal xRadius,
    qreal yRadius,
    Qt::SizeMode mode) {
  self->drawRoundedRect(x, y, w, h, xRadius, yRadius, mode);
}

//  void QPainter::drawRoundedRect(const QRect &rect, qreal xRadius, qreal
//      yRadius, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawRoundedRectERK5QRectddN2Qt8SizeModeE(
    QPainter *self,
    const QRect *rect,
    qreal xRadius,
    qreal yRadius,
    Qt::SizeMode mode) {
  self->drawRoundedRect(*rect, xRadius, yRadius, mode);
}

//  void QPainter::drawTiledPixmap(const QRectF &rect, const QPixmap &pm,
//      const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPainter *self,
    const QRectF *rect,
    const QPixmap *pm,
    const QPointF *offset) {
  self->drawTiledPixmap(*rect, *pm, *offset);
}

//  void QPainter::drawTiledPixmap(int x, int y, int w, int h, const QPixmap
//      &a4, int sx, int sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawTiledPixmapEiiiiRK7QPixmapii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    const QPixmap *a4,
    int sx,
    int sy) {
  self->drawTiledPixmap(x, y, w, h, *a4, sx, sy);
}

//  void QPainter::drawTiledPixmap(const QRect &a0, const QPixmap &a1, const
//      QPoint &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter15drawTiledPixmapERK5QRectRK7QPixmapRK6QPoint(
    QPainter *self,
    const QRect *a0,
    const QPixmap *a1,
    const QPoint *a2) {
  self->drawTiledPixmap(*a0, *a1, *a2);
}

//  void QPainter::drawPicture(const QPointF &p, const QPicture &picture)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPictureERK7QPointFRK8QPicture(
    QPainter *self,
    const QPointF *p,
    const QPicture *picture) {
  self->drawPicture(*p, *picture);
}

//  void QPainter::drawPicture(int x, int y, const QPicture &picture)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPictureEiiRK8QPicture(
    QPainter *self,
    int x,
    int y,
    const QPicture *picture) {
  self->drawPicture(x, y, *picture);
}

//  void QPainter::drawPicture(const QPoint &p, const QPicture &picture)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter11drawPictureERK6QPointRK8QPicture(
    QPainter *self,
    const QPoint *p,
    const QPicture *picture) {
  self->drawPicture(*p, *picture);
}

//  void QPainter::drawPixmap(const QRectF &targetRect, const QPixmap
//      &pixmap, const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPainter *self,
    const QRectF *targetRect,
    const QPixmap *pixmap,
    const QRectF *sourceRect) {
  self->drawPixmap(*targetRect, *pixmap, *sourceRect);
}

//  void QPainter::drawPixmap(const QRect &targetRect, const QPixmap &pixmap,
//      const QRect &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK5QRectRK7QPixmapS2_(
    QPainter *self,
    const QRect *targetRect,
    const QPixmap *pixmap,
    const QRect *sourceRect) {
  self->drawPixmap(*targetRect, *pixmap, *sourceRect);
}

//  void QPainter::drawPixmap(int x, int y, int w, int h, const QPixmap &pm,
//      int sx, int sy, int sw, int sh)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapEiiiiRK7QPixmapiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    const QPixmap *pm,
    int sx,
    int sy,
    int sw,
    int sh) {
  self->drawPixmap(x, y, w, h, *pm, sx, sy, sw, sh);
}

//  void QPainter::drawPixmap(int x, int y, const QPixmap &pm, int sx, int
//      sy, int sw, int sh)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapEiiRK7QPixmapiiii(
    QPainter *self,
    int x,
    int y,
    const QPixmap *pm,
    int sx,
    int sy,
    int sw,
    int sh) {
  self->drawPixmap(x, y, *pm, sx, sy, sw, sh);
}

//  void QPainter::drawPixmap(const QPointF &p, const QPixmap &pm, const
//      QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK7QPointFRK7QPixmapRK6QRectF(
    QPainter *self,
    const QPointF *p,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*p, *pm, *sr);
}

//  void QPainter::drawPixmap(const QPoint &p, const QPixmap &pm, const QRect
//      &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK6QPointRK7QPixmapRK5QRect(
    QPainter *self,
    const QPoint *p,
    const QPixmap *pm,
    const QRect *sr) {
  self->drawPixmap(*p, *pm, *sr);
}

//  void QPainter::drawPixmap(const QPointF &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK7QPointFRK7QPixmap(
    QPainter *self,
    const QPointF *p,
    const QPixmap *pm) {
  self->drawPixmap(*p, *pm);
}

//  void QPainter::drawPixmap(const QPoint &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK6QPointRK7QPixmap(
    QPainter *self,
    const QPoint *p,
    const QPixmap *pm) {
  self->drawPixmap(*p, *pm);
}

//  void QPainter::drawPixmap(int x, int y, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapEiiRK7QPixmap(
    QPainter *self,
    int x,
    int y,
    const QPixmap *pm) {
  self->drawPixmap(x, y, *pm);
}

//  void QPainter::drawPixmap(const QRect &r, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapERK5QRectRK7QPixmap(
    QPainter *self,
    const QRect *r,
    const QPixmap *pm) {
  self->drawPixmap(*r, *pm);
}

//  void QPainter::drawPixmap(int x, int y, int w, int h, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter10drawPixmapEiiiiRK7QPixmap(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    const QPixmap *pm) {
  self->drawPixmap(x, y, w, h, *pm);
}

//  void QPainter::drawPixmapFragments(const PixmapFragment *fragments, int
//      fragmentCount, const QPixmap &pixmap, PixmapFragmentHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter19drawPixmapFragmentsEPKNS_14PixmapFragmentEiRK7QPixmap6QFlagsINS_18PixmapFragmentHintEE(
    QPainter *self,
    const QPainter::PixmapFragment *fragments,
    int fragmentCount,
    const QPixmap *pixmap,
    int hints) {
  self->drawPixmapFragments(
      fragments,
      fragmentCount,
      *pixmap,
      QFlags<QPainter::PixmapFragmentHint>::fromInt(hints));
}

//  void QPainter::drawImage(const QRectF &targetRect, const QImage &image,
//      const QRectF &sourceRect, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPainter *self,
    const QRectF *targetRect,
    const QImage *image,
    const QRectF *sourceRect,
    int flags) {
  self->drawImage(
      *targetRect,
      *image,
      *sourceRect,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPainter::drawImage(const QRect &targetRect, const QImage &image,
//      const QRect &sourceRect, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK5QRectRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPainter *self,
    const QRect *targetRect,
    const QImage *image,
    const QRect *sourceRect,
    int flags) {
  self->drawImage(
      *targetRect,
      *image,
      *sourceRect,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPainter::drawImage(const QPointF &p, const QImage &image, const
//      QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK7QPointFRK6QImageRK6QRectF6QFlagsIN2Qt19ImageConversionFlagEE(
    QPainter *self,
    const QPointF *p,
    const QImage *image,
    const QRectF *sr,
    int flags) {
  self->drawImage(
      *p,
      *image,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPainter::drawImage(const QPoint &p, const QImage &image, const
//      QRect &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK6QPointRK6QImageRK5QRect6QFlagsIN2Qt19ImageConversionFlagEE(
    QPainter *self,
    const QPoint *p,
    const QImage *image,
    const QRect *sr,
    int flags) {
  self->drawImage(
      *p,
      *image,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPainter::drawImage(const QRectF &r, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK6QRectFRK6QImage(
    QPainter *self,
    const QRectF *r,
    const QImage *image) {
  self->drawImage(*r, *image);
}

//  void QPainter::drawImage(const QRect &r, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK5QRectRK6QImage(
    QPainter *self,
    const QRect *r,
    const QImage *image) {
  self->drawImage(*r, *image);
}

//  void QPainter::drawImage(const QPointF &p, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK7QPointFRK6QImage(
    QPainter *self,
    const QPointF *p,
    const QImage *image) {
  self->drawImage(*p, *image);
}

//  void QPainter::drawImage(const QPoint &p, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageERK6QPointRK6QImage(
    QPainter *self,
    const QPoint *p,
    const QImage *image) {
  self->drawImage(*p, *image);
}

//  void QPainter::drawImage(int x, int y, const QImage &image, int sx, int
//      sy, int sw, int sh, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9drawImageEiiRK6QImageiiii6QFlagsIN2Qt19ImageConversionFlagEE(
    QPainter *self,
    int x,
    int y,
    const QImage *image,
    int sx,
    int sy,
    int sw,
    int sh,
    int flags) {
  self->drawImage(
      x,
      y,
      *image,
      sx,
      sy,
      sw,
      sh,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPainter::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QPainter *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  Qt::LayoutDirection QPainter::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK8QPainter15layoutDirectionEv(
    const QPainter *self) {
  return self->layoutDirection();
}

//  void QPainter::drawGlyphRun(const QPointF &position, const QGlyphRun
//      &glyphRun)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawGlyphRunERK7QPointFRK9QGlyphRun(
    QPainter *self,
    const QPointF *position,
    const QGlyphRun *glyphRun) {
  self->drawGlyphRun(*position, *glyphRun);
}

//  void QPainter::drawStaticText(const QPointF &topLeftPosition, const
//      QStaticText &staticText)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14drawStaticTextERK7QPointFRK11QStaticText(
    QPainter *self,
    const QPointF *topLeftPosition,
    const QStaticText *staticText) {
  self->drawStaticText(*topLeftPosition, *staticText);
}

//  void QPainter::drawStaticText(const QPoint &topLeftPosition, const
//      QStaticText &staticText)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14drawStaticTextERK6QPointRK11QStaticText(
    QPainter *self,
    const QPoint *topLeftPosition,
    const QStaticText *staticText) {
  self->drawStaticText(*topLeftPosition, *staticText);
}

//  void QPainter::drawStaticText(int left, int top, const QStaticText
//      &staticText)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14drawStaticTextEiiRK11QStaticText(
    QPainter *self,
    int left,
    int top,
    const QStaticText *staticText) {
  self->drawStaticText(left, top, *staticText);
}

//  void QPainter::drawText(const QPointF &p, const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK7QPointFRK7QString(
    QPainter *self,
    const QPointF *p,
    const QString *s) {
  self->drawText(*p, *s);
}

//  void QPainter::drawText(const QPoint &p, const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK6QPointRK7QString(
    QPainter *self,
    const QPoint *p,
    const QString *s) {
  self->drawText(*p, *s);
}

//  void QPainter::drawText(int x, int y, const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextEiiRK7QString(
    QPainter *self,
    int x,
    int y,
    const QString *s) {
  self->drawText(x, y, *s);
}

//  void QPainter::drawText(const QPointF &p, const QString &str, int tf, int
//      justificationPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK7QPointFRK7QStringii(
    QPainter *self,
    const QPointF *p,
    const QString *str,
    int tf,
    int justificationPadding) {
  self->drawText(*p, *str, tf, justificationPadding);
}

//  void QPainter::drawText(const QRectF &r, int flags, const QString &text,
//      QRectF *br)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK6QRectFiRK7QStringPS0_(
    QPainter *self,
    const QRectF *r,
    int flags,
    const QString *text,
    QRectF *br) {
  self->drawText(*r, flags, *text, br);
}

//  void QPainter::drawText(const QRect &r, int flags, const QString &text,
//      QRect *br)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK5QRectiRK7QStringPS0_(
    QPainter *self,
    const QRect *r,
    int flags,
    const QString *text,
    QRect *br) {
  self->drawText(*r, flags, *text, br);
}

//  void QPainter::drawText(int x, int y, int w, int h, int flags, const
//      QString &text, QRect *br)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextEiiiiiRK7QStringP5QRect(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    int flags,
    const QString *text,
    QRect *br) {
  self->drawText(x, y, w, h, flags, *text, br);
}

//  void QPainter::drawText(const QRectF &r, const QString &text, const
//      QTextOption &o)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8drawTextERK6QRectFRK7QStringRK11QTextOption(
    QPainter *self,
    const QRectF *r,
    const QString *text,
    const QTextOption *o) {
  self->drawText(*r, *text, *o);
}

//  QRectF QPainter::boundingRect(const QRectF &rect, int flags, const
//      QString &text)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN8QPainter12boundingRectERK6QRectFiRK7QString(
    QPainter *self,
    const QRectF *rect,
    int flags,
    const QString *text) {
  return new QRectF(self->boundingRect(*rect, flags, *text));
}

//  QRect QPainter::boundingRect(const QRect &rect, int flags, const QString
//      &text)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN8QPainter12boundingRectERK5QRectiRK7QString(
    QPainter *self,
    const QRect *rect,
    int flags,
    const QString *text) {
  return new QRect(self->boundingRect(*rect, flags, *text));
}

//  QRect QPainter::boundingRect(int x, int y, int w, int h, int flags, const
//      QString &text)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN8QPainter12boundingRectEiiiiiRK7QString(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    int flags,
    const QString *text) {
  return new QRect(self->boundingRect(x, y, w, h, flags, *text));
}

//  QRectF QPainter::boundingRect(const QRectF &rect, const QString &text,
//      const QTextOption &o)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN8QPainter12boundingRectERK6QRectFRK7QStringRK11QTextOption(
    QPainter *self,
    const QRectF *rect,
    const QString *text,
    const QTextOption *o) {
  return new QRectF(self->boundingRect(*rect, *text, *o));
}

//  void QPainter::drawTextItem(const QPointF &p, const QTextItem &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawTextItemERK7QPointFRK9QTextItem(
    QPainter *self,
    const QPointF *p,
    const QTextItem *ti) {
  self->drawTextItem(*p, *ti);
}

//  void QPainter::drawTextItem(int x, int y, const QTextItem &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawTextItemEiiRK9QTextItem(
    QPainter *self,
    int x,
    int y,
    const QTextItem *ti) {
  self->drawTextItem(x, y, *ti);
}

//  void QPainter::drawTextItem(const QPoint &p, const QTextItem &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter12drawTextItemERK6QPointRK9QTextItem(
    QPainter *self,
    const QPoint *p,
    const QTextItem *ti) {
  self->drawTextItem(*p, *ti);
}

//  void QPainter::fillRect(const QRectF &a0, const QBrush &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK6QRectFRK6QBrush(
    QPainter *self,
    const QRectF *a0,
    const QBrush *a1) {
  self->fillRect(*a0, *a1);
}

//  void QPainter::fillRect(int x, int y, int w, int h, const QBrush &a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectEiiiiRK6QBrush(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    const QBrush *a4) {
  self->fillRect(x, y, w, h, *a4);
}

//  void QPainter::fillRect(const QRect &a0, const QBrush &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK5QRectRK6QBrush(
    QPainter *self,
    const QRect *a0,
    const QBrush *a1) {
  self->fillRect(*a0, *a1);
}

//  void QPainter::fillRect(const QRectF &a0, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK6QRectFRK6QColor(
    QPainter *self,
    const QRectF *a0,
    const QColor *color) {
  self->fillRect(*a0, *color);
}

//  void QPainter::fillRect(int x, int y, int w, int h, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectEiiiiRK6QColor(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    const QColor *color) {
  self->fillRect(x, y, w, h, *color);
}

//  void QPainter::fillRect(const QRect &a0, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK5QRectRK6QColor(
    QPainter *self,
    const QRect *a0,
    const QColor *color) {
  self->fillRect(*a0, *color);
}

//  void QPainter::fillRect(int x, int y, int w, int h, Qt::GlobalColor c)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectEiiiiN2Qt11GlobalColorE(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    Qt::GlobalColor c) {
  self->fillRect(x, y, w, h, c);
}

//  void QPainter::fillRect(const QRect &r, Qt::GlobalColor c)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK5QRectN2Qt11GlobalColorE(
    QPainter *self,
    const QRect *r,
    Qt::GlobalColor c) {
  self->fillRect(*r, c);
}

//  void QPainter::fillRect(const QRectF &r, Qt::GlobalColor c)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK6QRectFN2Qt11GlobalColorE(
    QPainter *self,
    const QRectF *r,
    Qt::GlobalColor c) {
  self->fillRect(*r, c);
}

//  void QPainter::fillRect(int x, int y, int w, int h, Qt::BrushStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectEiiiiN2Qt10BrushStyleE(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    Qt::BrushStyle style) {
  self->fillRect(x, y, w, h, style);
}

//  void QPainter::fillRect(const QRect &r, Qt::BrushStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK5QRectN2Qt10BrushStyleE(
    QPainter *self,
    const QRect *r,
    Qt::BrushStyle style) {
  self->fillRect(*r, style);
}

//  void QPainter::fillRect(const QRectF &r, Qt::BrushStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK6QRectFN2Qt10BrushStyleE(
    QPainter *self,
    const QRectF *r,
    Qt::BrushStyle style) {
  self->fillRect(*r, style);
}

//  void QPainter::fillRect(int x, int y, int w, int h, QGradient::Preset
//      preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectEiiiiN9QGradient6PresetE(
    QPainter *self,
    int x,
    int y,
    int w,
    int h,
    QGradient::Preset preset) {
  self->fillRect(x, y, w, h, preset);
}

//  void QPainter::fillRect(const QRect &r, QGradient::Preset preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK5QRectN9QGradient6PresetE(
    QPainter *self,
    const QRect *r,
    QGradient::Preset preset) {
  self->fillRect(*r, preset);
}

//  void QPainter::fillRect(const QRectF &r, QGradient::Preset preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter8fillRectERK6QRectFN9QGradient6PresetE(
    QPainter *self,
    const QRectF *r,
    QGradient::Preset preset) {
  self->fillRect(*r, preset);
}

//  void QPainter::eraseRect(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9eraseRectERK6QRectF(
    QPainter *self,
    const QRectF *a0) {
  self->eraseRect(*a0);
}

//  void QPainter::eraseRect(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9eraseRectEiiii(
    QPainter *self,
    int x,
    int y,
    int w,
    int h) {
  self->eraseRect(x, y, w, h);
}

//  void QPainter::eraseRect(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter9eraseRectERK5QRect(QPainter *self, const QRect *a0) {
  self->eraseRect(*a0);
}

//  void QPainter::setRenderHint(RenderHint hint, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter13setRenderHintENS_10RenderHintEb(
    QPainter *self,
    QPainter::RenderHint hint,
    bool on) {
  self->setRenderHint(hint, on);
}

//  void QPainter::setRenderHints(RenderHints hints, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter14setRenderHintsE6QFlagsINS_10RenderHintEEb(
    QPainter *self,
    int hints,
    bool on) {
  self->setRenderHints(QFlags<QPainter::RenderHint>::fromInt(hints), on);
}

//  RenderHints QPainter::renderHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPainter11renderHintsEv(const QPainter *self) {
  return static_cast<int>(self->renderHints().toInt());
}

//  bool QPainter::testRenderHint(RenderHint hint) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPainter14testRenderHintENS_10RenderHintE(
    const QPainter *self,
    QPainter::RenderHint hint) {
  return self->testRenderHint(hint);
}

//  QPaintEngine *QPainter::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK8QPainter11paintEngineEv(const QPainter *self) {
  return self->paintEngine();
}

//  void QPainter::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter19beginNativePaintingEv(QPainter *self) {
  self->beginNativePainting();
}

//  void QPainter::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPainter17endNativePaintingEv(QPainter *self) {
  self->endNativePainting();
}
