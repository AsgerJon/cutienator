//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainterpath.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtGui/qregion.h>
#include <QtGui/qtransform.h>
#include <QtCore/qlist.h>

//  QPainterPath::QPainterPath()
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12QPainterPathC1Ev() {
  return new QPainterPath();
}

//  QPainterPath::QPainterPath(const QPointF &startPoint)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12QPainterPathC1ERK7QPointF(
    const QPointF *startPoint) {
  return new QPainterPath(*startPoint);
}

//  QPainterPath::QPainterPath(const QPainterPath &other)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12QPainterPathC1ERKS_(const QPainterPath *other) {
  return new QPainterPath(*other);
}

//  QPainterPath::~QPainterPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPathD1Ev(QPainterPath *self) {
  delete self;
}

//  void QPainterPath::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath5clearEv(QPainterPath *self) {
  self->clear();
}

//  void QPainterPath::reserve(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7reserveEi(QPainterPath *self, int size) {
  self->reserve(size);
}

//  int QPainterPath::capacity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPainterPath8capacityEv(const QPainterPath *self) {
  return self->capacity();
}

//  void QPainterPath::closeSubpath()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath12closeSubpathEv(QPainterPath *self) {
  self->closeSubpath();
}

//  void QPainterPath::moveTo(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6moveToERK7QPointF(
    QPainterPath *self,
    const QPointF *p) {
  self->moveTo(*p);
}

//  void QPainterPath::moveTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6moveToEdd(
    QPainterPath *self,
    qreal x,
    qreal y) {
  self->moveTo(x, y);
}

//  void QPainterPath::lineTo(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6lineToERK7QPointF(
    QPainterPath *self,
    const QPointF *p) {
  self->lineTo(*p);
}

//  void QPainterPath::lineTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6lineToEdd(
    QPainterPath *self,
    qreal x,
    qreal y) {
  self->lineTo(x, y);
}

//  void QPainterPath::arcMoveTo(const QRectF &rect, qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath9arcMoveToERK6QRectFd(
    QPainterPath *self,
    const QRectF *rect,
    qreal angle) {
  self->arcMoveTo(*rect, angle);
}

//  void QPainterPath::arcMoveTo(qreal x, qreal y, qreal w, qreal h, qreal
//      angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath9arcMoveToEddddd(
    QPainterPath *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    qreal angle) {
  self->arcMoveTo(x, y, w, h, angle);
}

//  void QPainterPath::arcTo(const QRectF &rect, qreal startAngle, qreal
//      arcLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath5arcToERK6QRectFdd(
    QPainterPath *self,
    const QRectF *rect,
    qreal startAngle,
    qreal arcLength) {
  self->arcTo(*rect, startAngle, arcLength);
}

//  void QPainterPath::arcTo(qreal x, qreal y, qreal w, qreal h, qreal
//      startAngle, qreal arcLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath5arcToEdddddd(
    QPainterPath *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    qreal startAngle,
    qreal arcLength) {
  self->arcTo(x, y, w, h, startAngle, arcLength);
}

//  void QPainterPath::cubicTo(const QPointF &ctrlPt1, const QPointF
//      &ctrlPt2, const QPointF &endPt)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7cubicToERK7QPointFS2_S2_(
    QPainterPath *self,
    const QPointF *ctrlPt1,
    const QPointF *ctrlPt2,
    const QPointF *endPt) {
  self->cubicTo(*ctrlPt1, *ctrlPt2, *endPt);
}

//  void QPainterPath::cubicTo(qreal ctrlPt1x, qreal ctrlPt1y, qreal
//      ctrlPt2x, qreal ctrlPt2y, qreal endPtx, qreal endPty)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7cubicToEdddddd(
    QPainterPath *self,
    qreal ctrlPt1x,
    qreal ctrlPt1y,
    qreal ctrlPt2x,
    qreal ctrlPt2y,
    qreal endPtx,
    qreal endPty) {
  self->cubicTo(ctrlPt1x, ctrlPt1y, ctrlPt2x, ctrlPt2y, endPtx, endPty);
}

//  void QPainterPath::quadTo(const QPointF &ctrlPt, const QPointF &endPt)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6quadToERK7QPointFS2_(
    QPainterPath *self,
    const QPointF *ctrlPt,
    const QPointF *endPt) {
  self->quadTo(*ctrlPt, *endPt);
}

//  void QPainterPath::quadTo(qreal ctrlPtx, qreal ctrlPty, qreal endPtx,
//      qreal endPty)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath6quadToEdddd(
    QPainterPath *self,
    qreal ctrlPtx,
    qreal ctrlPty,
    qreal endPtx,
    qreal endPty) {
  self->quadTo(ctrlPtx, ctrlPty, endPtx, endPty);
}

//  QPointF QPainterPath::currentPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QPainterPath15currentPositionEv(
    const QPainterPath *self) {
  return new QPointF(self->currentPosition());
}

//  void QPainterPath::addRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7addRectERK6QRectF(
    QPainterPath *self,
    const QRectF *rect) {
  self->addRect(*rect);
}

//  void QPainterPath::addRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7addRectEdddd(
    QPainterPath *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->addRect(x, y, w, h);
}

//  void QPainterPath::addEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath10addEllipseERK6QRectF(
    QPainterPath *self,
    const QRectF *rect) {
  self->addEllipse(*rect);
}

//  void QPainterPath::addEllipse(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath10addEllipseEdddd(
    QPainterPath *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->addEllipse(x, y, w, h);
}

//  void QPainterPath::addEllipse(const QPointF &center, qreal rx, qreal ry)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath10addEllipseERK7QPointFdd(
    QPainterPath *self,
    const QPointF *center,
    qreal rx,
    qreal ry) {
  self->addEllipse(*center, rx, ry);
}

//  void QPainterPath::addPolygon(const QPolygonF &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath10addPolygonERK9QPolygonF(
    QPainterPath *self,
    const QPolygonF *polygon) {
  self->addPolygon(*polygon);
}

//  void QPainterPath::addText(const QPointF &point, const QFont &f, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7addTextERK7QPointFRK5QFontRK7QString(
    QPainterPath *self,
    const QPointF *point,
    const QFont *f,
    const QString *text) {
  self->addText(*point, *f, *text);
}

//  void QPainterPath::addText(qreal x, qreal y, const QFont &f, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7addTextEddRK5QFontRK7QString(
    QPainterPath *self,
    qreal x,
    qreal y,
    const QFont *f,
    const QString *text) {
  self->addText(x, y, *f, *text);
}

//  void QPainterPath::addPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7addPathERKS_(
    QPainterPath *self,
    const QPainterPath *path) {
  self->addPath(*path);
}

//  void QPainterPath::addRegion(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath9addRegionERK7QRegion(
    QPainterPath *self,
    const QRegion *region) {
  self->addRegion(*region);
}

//  void QPainterPath::addRoundedRect(const QRectF &rect, qreal xRadius,
//      qreal yRadius, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath14addRoundedRectERK6QRectFddN2Qt8SizeModeE(
    QPainterPath *self,
    const QRectF *rect,
    qreal xRadius,
    qreal yRadius,
    Qt::SizeMode mode) {
  self->addRoundedRect(*rect, xRadius, yRadius, mode);
}

//  void QPainterPath::addRoundedRect(qreal x, qreal y, qreal w, qreal h,
//      qreal xRadius, qreal yRadius, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath14addRoundedRectEddddddN2Qt8SizeModeE(
    QPainterPath *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    qreal xRadius,
    qreal yRadius,
    Qt::SizeMode mode) {
  self->addRoundedRect(x, y, w, h, xRadius, yRadius, mode);
}

//  void QPainterPath::connectPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath11connectPathERKS_(
    QPainterPath *self,
    const QPainterPath *path) {
  self->connectPath(*path);
}

//  bool QPainterPath::contains(const QPointF &pt) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath8containsERK7QPointF(
    const QPainterPath *self,
    const QPointF *pt) {
  return self->contains(*pt);
}

//  bool QPainterPath::contains(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath8containsERK6QRectF(
    const QPainterPath *self,
    const QRectF *rect) {
  return self->contains(*rect);
}

//  bool QPainterPath::intersects(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath10intersectsERK6QRectF(
    const QPainterPath *self,
    const QRectF *rect) {
  return self->intersects(*rect);
}

//  void QPainterPath::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath9translateEdd(
    QPainterPath *self,
    qreal dx,
    qreal dy) {
  self->translate(dx, dy);
}

//  void QPainterPath::translate(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath9translateERK7QPointF(
    QPainterPath *self,
    const QPointF *offset) {
  self->translate(*offset);
}

//  QPainterPath QPainterPath::translated(qreal dx, qreal dy) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath10translatedEdd(
    const QPainterPath *self,
    qreal dx,
    qreal dy) {
  return new QPainterPath(self->translated(dx, dy));
}

//  QPainterPath QPainterPath::translated(const QPointF &offset) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath10translatedERK7QPointF(
    const QPainterPath *self,
    const QPointF *offset) {
  return new QPainterPath(self->translated(*offset));
}

//  QRectF QPainterPath::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QPainterPath12boundingRectEv(const QPainterPath *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QPainterPath::controlPointRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QPainterPath16controlPointRectEv(
    const QPainterPath *self) {
  return new QRectF(self->controlPointRect());
}

//  Qt::FillRule QPainterPath::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK12QPainterPath8fillRuleEv(const QPainterPath *self) {
  return self->fillRule();
}

//  void QPainterPath::setFillRule(Qt::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath11setFillRuleEN2Qt8FillRuleE(
    QPainterPath *self,
    Qt::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  bool QPainterPath::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7isEmptyEv(const QPainterPath *self) {
  return self->isEmpty();
}

//  QPainterPath QPainterPath::toReversed() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath10toReversedEv(
    const QPainterPath *self) {
  return new QPainterPath(self->toReversed());
}

//  QList<QPolygonF> QPainterPath::toSubpathPolygons(const QTransform
//      &matrix) const
extern "C" Q_DECL_EXPORT
QList<QPolygonF> *ritual_ZNK12QPainterPath17toSubpathPolygonsERK10QTransform(
    const QPainterPath *self,
    const QTransform *matrix) {
  return new QList<QPolygonF>(self->toSubpathPolygons(*matrix));
}

//  QList<QPolygonF> QPainterPath::toFillPolygons(const QTransform &matrix)
//      const
extern "C" Q_DECL_EXPORT
QList<QPolygonF> *ritual_ZNK12QPainterPath14toFillPolygonsERK10QTransform(
    const QPainterPath *self,
    const QTransform *matrix) {
  return new QList<QPolygonF>(self->toFillPolygons(*matrix));
}

//  QPolygonF QPainterPath::toFillPolygon(const QTransform &matrix) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK12QPainterPath13toFillPolygonERK10QTransform(
    const QPainterPath *self,
    const QTransform *matrix) {
  return new QPolygonF(self->toFillPolygon(*matrix));
}

//  int QPainterPath::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPainterPath12elementCountEv(const QPainterPath *self) {
  return self->elementCount();
}

//  QPainterPath::Element QPainterPath::elementAt(int i) const
extern "C" Q_DECL_EXPORT
QPainterPath::Element *ritual_ZNK12QPainterPath9elementAtEi(
    const QPainterPath *self,
    int i) {
  return new QPainterPath::Element(self->elementAt(i));
}

//  void QPainterPath::setElementPositionAt(int i, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath20setElementPositionAtEidd(
    QPainterPath *self,
    int i,
    qreal x,
    qreal y) {
  self->setElementPositionAt(i, x, y);
}

//  bool QPainterPath::isCachingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath16isCachingEnabledEv(const QPainterPath *self) {
  return self->isCachingEnabled();
}

//  void QPainterPath::setCachingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath17setCachingEnabledEb(
    QPainterPath *self,
    bool enabled) {
  self->setCachingEnabled(enabled);
}

//  qreal QPainterPath::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPainterPath6lengthEv(const QPainterPath *self) {
  return self->length();
}

//  qreal QPainterPath::percentAtLength(qreal len) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPainterPath15percentAtLengthEd(
    const QPainterPath *self,
    qreal len) {
  return self->percentAtLength(len);
}

//  QPointF QPainterPath::pointAtPercent(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QPainterPath14pointAtPercentEd(
    const QPainterPath *self,
    qreal t) {
  return new QPointF(self->pointAtPercent(t));
}

//  qreal QPainterPath::angleAtPercent(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPainterPath14angleAtPercentEd(
    const QPainterPath *self,
    qreal t) {
  return self->angleAtPercent(t);
}

//  qreal QPainterPath::slopeAtPercent(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPainterPath14slopeAtPercentEd(
    const QPainterPath *self,
    qreal t) {
  return self->slopeAtPercent(t);
}

//  QPainterPath QPainterPath::trimmed(qreal fromFraction, qreal toFraction,
//      qreal offset) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath7trimmedEddd(
    const QPainterPath *self,
    qreal fromFraction,
    qreal toFraction,
    qreal offset) {
  return new QPainterPath(self->trimmed(fromFraction, toFraction, offset));
}

//  bool QPainterPath::intersects(const QPainterPath &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath10intersectsERKS_(
    const QPainterPath *self,
    const QPainterPath *p) {
  return self->intersects(*p);
}

//  bool QPainterPath::contains(const QPainterPath &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath8containsERKS_(
    const QPainterPath *self,
    const QPainterPath *p) {
  return self->contains(*p);
}

//  QPainterPath QPainterPath::united(const QPainterPath &r) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath6unitedERKS_(
    const QPainterPath *self,
    const QPainterPath *r) {
  return new QPainterPath(self->united(*r));
}

//  QPainterPath QPainterPath::intersected(const QPainterPath &r) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath11intersectedERKS_(
    const QPainterPath *self,
    const QPainterPath *r) {
  return new QPainterPath(self->intersected(*r));
}

//  QPainterPath QPainterPath::subtracted(const QPainterPath &r) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath10subtractedERKS_(
    const QPainterPath *self,
    const QPainterPath *r) {
  return new QPainterPath(self->subtracted(*r));
}

//  QPainterPath QPainterPath::simplified() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPath10simplifiedEv(
    const QPainterPath *self) {
  return new QPainterPath(self->simplified());
}

//  bool QPainterPath::operator==(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPatheqERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return self->operator==(*other);
}

//  bool QPainterPath::operator!=(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPathneERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return self->operator!=(*other);
}

//  QPainterPath QPainterPath::operator&(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPathanERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return new QPainterPath(self->operator&(*other));
}

//  QPainterPath QPainterPath::operator|(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPathorERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return new QPainterPath(self->operator|(*other));
}

//  QPainterPath QPainterPath::operator+(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPathplERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return new QPainterPath(self->operator+(*other));
}

//  QPainterPath QPainterPath::operator-(const QPainterPath &other) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QPainterPathmiERKS_(
    const QPainterPath *self,
    const QPainterPath *other) {
  return new QPainterPath(self->operator-(*other));
}

//  QPainterPath &QPainterPath::operator&=(const QPainterPath &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPathaNERKS_(
    QPainterPath *self,
    const QPainterPath *other) {
  self->operator&=(*other);
}

//  QPainterPath &QPainterPath::operator|=(const QPainterPath &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPathoRERKS_(
    QPainterPath *self,
    const QPainterPath *other) {
  self->operator|=(*other);
}

//  QPainterPath &QPainterPath::operator+=(const QPainterPath &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPathpLERKS_(
    QPainterPath *self,
    const QPainterPath *other) {
  self->operator+=(*other);
}

//  QPainterPath &QPainterPath::operator-=(const QPainterPath &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPathmIERKS_(
    QPainterPath *self,
    const QPainterPath *other) {
  self->operator-=(*other);
}

//  void QPainterPath::ensureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath10ensureDataEv(QPainterPath *self) {
  self->ensureData();
}

//  void QPainterPath::ensureData_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath17ensureData_helperEv(QPainterPath *self) {
  self->ensureData_helper();
}

//  void QPainterPath::setDirty(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath8setDirtyEb(QPainterPath *self, bool a0) {
  self->setDirty(a0);
}

//  void QPainterPath::computeBoundingRect() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPainterPath19computeBoundingRectEv(
    const QPainterPath *self) {
  self->computeBoundingRect();
}

//  void QPainterPath::computeControlPointRect() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPainterPath23computeControlPointRectEv(
    const QPainterPath *self) {
  self->computeControlPointRect();
}

//  QPainterPathPrivate *QPainterPath::d_func() const
extern "C" Q_DECL_EXPORT
QPainterPathPrivate *ritual_ZNK12QPainterPath6d_funcEv(
    const QPainterPath *self) {
  return self->d_func();
}

//  QList<QPainterPath>::QList()
extern "C" Q_DECL_EXPORT
QList<QPainterPath> *ritual_list_make_QPainterPath() {
  return new QList<QPainterPath>();
}

//  void QList<QPainterPath>::append(const QPainterPath &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPainterPath(
    QList<QPainterPath> *self,
    const QPainterPath *element) {
  self->append(*element);
}

//  qsizetype QList<QPainterPath>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPainterPath(const QList<QPainterPath> *self) {
  return self->size();
}

//  const QPainterPath &QList<QPainterPath>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_list_at_QPainterPath(
    const QList<QPainterPath> *self,
    long long index) {
  return new QPainterPath(self->at(index));
}

//  QList<QPainterPath>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPainterPath(QList<QPainterPath> *self) {
  delete self;
}
