//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspath.h, Qt 6.12.0. Changes made here are lost.
#include <QtCanvasPainter/qcanvaspath.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>

//  QCanvasPath::QCanvasPath()
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathC1Ev() {
  return new QCanvasPath();
}

//  QCanvasPath::QCanvasPath(qsizetype commandsSize, qsizetype
//      commandsDataSize)
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathC1Exx(
    qsizetype commandsSize,
    qsizetype commandsDataSize) {
  return new QCanvasPath(commandsSize, commandsDataSize);
}

//  QCanvasPath::QCanvasPath(const QCanvasPath &path)
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathC1ERKS_(const QCanvasPath *path) {
  return new QCanvasPath(*path);
}

//  QCanvasPath::~QCanvasPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPathD1Ev(QCanvasPath *self) {
  delete self;
}

//  QCanvasPath &QCanvasPath::operator=(const QCanvasPath &path)
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathaSERKS_(
    QCanvasPath *self,
    const QCanvasPath *path) {
  return &(self->operator=(*path));
}

//  QCanvasPath::QCanvasPath(QCanvasPath &&other)
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathC1EOS_(QCanvasPath *other) {
  return new QCanvasPath(std::move(*other));
}

//  QCanvasPath &QCanvasPath::operator=(QCanvasPath &&other)
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZN11QCanvasPathaSEOS_(
    QCanvasPath *self,
    QCanvasPath *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCanvasPath::swap(QCanvasPath &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath4swapERS_(QCanvasPath *self, QCanvasPath *other) {
  self->swap(*other);
}

//  QVariant QCanvasPath::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QCanvasPathcv8QVariantEv(const QCanvasPath *self) {
  return new QVariant(self->operator QVariant());
}

//  void QCanvasPath::closePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath9closePathEv(QCanvasPath *self) {
  self->closePath();
}

//  void QCanvasPath::moveTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6moveToEdd(QCanvasPath *self, qreal x, qreal y) {
  self->moveTo(x, y);
}

//  void QCanvasPath::moveTo(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6moveToE7QPointF(
    QCanvasPath *self,
    const QPointF *point) {
  self->moveTo(*point);
}

//  void QCanvasPath::lineTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6lineToEdd(QCanvasPath *self, qreal x, qreal y) {
  self->lineTo(x, y);
}

//  void QCanvasPath::lineTo(QPointF point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6lineToE7QPointF(
    QCanvasPath *self,
    const QPointF *point) {
  self->lineTo(*point);
}

//  void QCanvasPath::bezierCurveTo(qreal c1x, qreal c1y, qreal c2x, qreal
//      c2y, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath13bezierCurveToEdddddd(
    QCanvasPath *self,
    qreal c1x,
    qreal c1y,
    qreal c2x,
    qreal c2y,
    qreal x,
    qreal y) {
  self->bezierCurveTo(c1x, c1y, c2x, c2y, x, y);
}

//  void QCanvasPath::bezierCurveTo(QPointF controlPoint1, QPointF
//      controlPoint2, QPointF endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath13bezierCurveToE7QPointFS0_S0_(
    QCanvasPath *self,
    const QPointF *controlPoint1,
    const QPointF *controlPoint2,
    const QPointF *endPoint) {
  self->bezierCurveTo(*controlPoint1, *controlPoint2, *endPoint);
}

//  void QCanvasPath::quadraticCurveTo(qreal cx, qreal cy, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath16quadraticCurveToEdddd(
    QCanvasPath *self,
    qreal cx,
    qreal cy,
    qreal x,
    qreal y) {
  self->quadraticCurveTo(cx, cy, x, y);
}

//  void QCanvasPath::quadraticCurveTo(QPointF controlPoint, QPointF
//      endPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath16quadraticCurveToE7QPointFS0_(
    QCanvasPath *self,
    const QPointF *controlPoint,
    const QPointF *endPoint) {
  self->quadraticCurveTo(*controlPoint, *endPoint);
}

//  void QCanvasPath::arcTo(qreal c1x, qreal c1y, qreal c2x, qreal c2y, qreal
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath5arcToEddddd(
    QCanvasPath *self,
    qreal c1x,
    qreal c1y,
    qreal c2x,
    qreal c2y,
    qreal radius) {
  self->arcTo(c1x, c1y, c2x, c2y, radius);
}

//  void QCanvasPath::arcTo(QPointF controlPoint1, QPointF controlPoint2,
//      qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath5arcToE7QPointFS0_d(
    QCanvasPath *self,
    const QPointF *controlPoint1,
    const QPointF *controlPoint2,
    qreal radius) {
  self->arcTo(*controlPoint1, *controlPoint2, radius);
}

//  void QCanvasPath::arc(qreal centerX, qreal centerY, qreal radius, qreal
//      a0, qreal a1, QCanvasPainter::PathWinding direction,
//      QCanvasPainter::PathConnection connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath3arcEdddddN14QCanvasPainter11PathWindingENS0_14PathConnectionE(
    QCanvasPath *self,
    qreal centerX,
    qreal centerY,
    qreal radius,
    qreal a0,
    qreal a1,
    QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection) {
  self->arc(centerX, centerY, radius, a0, a1, direction, connection);
}

//  void QCanvasPath::arc(QPointF centerPoint, qreal radius, qreal a0, qreal
//      a1, QCanvasPainter::PathWinding direction,
//      QCanvasPainter::PathConnection connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath3arcE7QPointFdddN14QCanvasPainter11PathWindingENS1_14PathConnectionE(
    QCanvasPath *self,
    const QPointF *centerPoint,
    qreal radius,
    qreal a0,
    qreal a1,
    QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection) {
  self->arc(*centerPoint, radius, a0, a1, direction, connection);
}

//  void QCanvasPath::rect(qreal x, qreal y, qreal width, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath4rectEdddd(
    QCanvasPath *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->rect(x, y, width, height);
}

//  void QCanvasPath::rect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath4rectERK6QRectF(
    QCanvasPath *self,
    const QRectF *rect) {
  self->rect(*rect);
}

//  void QCanvasPath::roundRect(qreal x, qreal y, qreal width, qreal height,
//      qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath9roundRectEddddd(
    QCanvasPath *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    qreal radius) {
  self->roundRect(x, y, width, height, radius);
}

//  void QCanvasPath::roundRect(const QRectF &rect, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath9roundRectERK6QRectFd(
    QCanvasPath *self,
    const QRectF *rect,
    qreal radius) {
  self->roundRect(*rect, radius);
}

//  void QCanvasPath::roundRect(qreal x, qreal y, qreal width, qreal height,
//      qreal radiusTopLeft, qreal radiusTopRight, qreal radiusBottomRight,
//      qreal radiusBottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath9roundRectEdddddddd(
    QCanvasPath *self,
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

//  void QCanvasPath::roundRect(const QRectF &rect, qreal radiusTopLeft,
//      qreal radiusTopRight, qreal radiusBottomRight, qreal
//      radiusBottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath9roundRectERK6QRectFdddd(
    QCanvasPath *self,
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

//  void QCanvasPath::ellipse(qreal x, qreal y, qreal radiusX, qreal radiusY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7ellipseEdddd(
    QCanvasPath *self,
    qreal x,
    qreal y,
    qreal radiusX,
    qreal radiusY) {
  self->ellipse(x, y, radiusX, radiusY);
}

//  void QCanvasPath::ellipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7ellipseERK6QRectF(
    QCanvasPath *self,
    const QRectF *rect) {
  self->ellipse(*rect);
}

//  void QCanvasPath::circle(qreal x, qreal y, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6circleEddd(
    QCanvasPath *self,
    qreal x,
    qreal y,
    qreal radius) {
  self->circle(x, y, radius);
}

//  void QCanvasPath::circle(QPointF centerPoint, qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath6circleE7QPointFd(
    QCanvasPath *self,
    const QPointF *centerPoint,
    qreal radius) {
  self->circle(*centerPoint, radius);
}

//  void QCanvasPath::setPathWinding(QCanvasPainter::PathWinding winding)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath14setPathWindingEN14QCanvasPainter11PathWindingE(
    QCanvasPath *self,
    QCanvasPainter::PathWinding winding) {
  self->setPathWinding(winding);
}

//  void QCanvasPath::beginSolidSubPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath17beginSolidSubPathEv(QCanvasPath *self) {
  self->beginSolidSubPath();
}

//  void QCanvasPath::beginHoleSubPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath16beginHoleSubPathEv(QCanvasPath *self) {
  self->beginHoleSubPath();
}

//  void QCanvasPath::addPath(const QCanvasPath &path, const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7addPathERKS_RK10QTransform(
    QCanvasPath *self,
    const QCanvasPath *path,
    const QTransform *transform) {
  self->addPath(*path, *transform);
}

//  void QCanvasPath::addPath(const QCanvasPath &path, qsizetype start,
//      qsizetype count, const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7addPathERKS_xxRK10QTransform(
    QCanvasPath *self,
    const QCanvasPath *path,
    qsizetype start,
    qsizetype count,
    const QTransform *transform) {
  self->addPath(*path, start, count, *transform);
}

//  void QCanvasPath::addPath(QStringView svgPath, const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7addPathE11QStringViewRK10QTransform(
    QCanvasPath *self,
    const QString *svgPath,
    const QTransform *transform) {
  self->addPath(QStringView(*svgPath), *transform);
}

//  void QCanvasPath::addPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7addPathERK12QPainterPath(
    QCanvasPath *self,
    const QPainterPath *path) {
  self->addPath(*path);
}

//  bool QCanvasPath::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QCanvasPath7isEmptyEv(const QCanvasPath *self) {
  return self->isEmpty();
}

//  void QCanvasPath::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath5clearEv(QCanvasPath *self) {
  self->clear();
}

//  void QCanvasPath::squeeze()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7squeezeEv(QCanvasPath *self) {
  self->squeeze();
}

//  qsizetype QCanvasPath::commandsSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QCanvasPath12commandsSizeEv(const QCanvasPath *self) {
  return self->commandsSize();
}

//  qsizetype QCanvasPath::commandsDataSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QCanvasPath16commandsDataSizeEv(
    const QCanvasPath *self) {
  return self->commandsDataSize();
}

//  qsizetype QCanvasPath::commandsCapacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QCanvasPath16commandsCapacityEv(
    const QCanvasPath *self) {
  return self->commandsCapacity();
}

//  qsizetype QCanvasPath::commandsDataCapacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QCanvasPath20commandsDataCapacityEv(
    const QCanvasPath *self) {
  return self->commandsDataCapacity();
}

//  void QCanvasPath::reserve(qsizetype commandsSize, qsizetype
//      commandsDataSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCanvasPath7reserveExx(
    QCanvasPath *self,
    qsizetype commandsSize,
    qsizetype commandsDataSize) {
  self->reserve(commandsSize, commandsDataSize);
}

//  QPointF QCanvasPath::currentPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QCanvasPath15currentPositionEv(
    const QCanvasPath *self) {
  return new QPointF(self->currentPosition());
}

//  QPointF QCanvasPath::positionAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QCanvasPath10positionAtEx(
    const QCanvasPath *self,
    qsizetype index) {
  return new QPointF(self->positionAt(index));
}

//  QCanvasPath QCanvasPath::sliced(qsizetype start, qsizetype count, const
//      QTransform &transform) const
extern "C" Q_DECL_EXPORT
QCanvasPath *ritual_ZNK11QCanvasPath6slicedExxRK10QTransform(
    const QCanvasPath *self,
    qsizetype start,
    qsizetype count,
    const QTransform *transform) {
  return new QCanvasPath(self->sliced(start, count, *transform));
}

//  bool operator==(const QCanvasPath &lhs, const QCanvasPath &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QCanvasPathS1_(
    const QCanvasPath *lhs,
    const QCanvasPath *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasPath &lhs, const QCanvasPath &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QCanvasPathS1_(
    const QCanvasPath *lhs,
    const QCanvasPath *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QCanvasPathPrivate *QCanvasPath::d_func()
extern "C" Q_DECL_EXPORT
QCanvasPathPrivate *ritual_ZN11QCanvasPath6d_funcEv(QCanvasPath *self) {
  return self->d_func();
}

//  const QCanvasPathPrivate *QCanvasPath::d_func() const
extern "C" Q_DECL_EXPORT
const QCanvasPathPrivate *ritual_ZNK11QCanvasPath6d_funcEv(
    const QCanvasPath *self) {
  return self->d_func();
}
