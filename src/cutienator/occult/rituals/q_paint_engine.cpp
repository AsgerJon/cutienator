//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>

//  QPaintEngine::~QPaintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngineD1Ev(QPaintEngine *self) {
  delete self;
}

//  bool QPaintEngine::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPaintEngine8isActiveEv(const QPaintEngine *self) {
  return self->isActive();
}

//  void QPaintEngine::setActive(bool newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9setActiveEb(QPaintEngine *self, bool newState) {
  self->setActive(newState);
}

//  bool QPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPaintEngine5beginEP12QPaintDevice(
    QPaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPaintEngine3endEv(QPaintEngine *self) {
  return self->end();
}

//  void QPaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine11updateStateERK17QPaintEngineState(
    QPaintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9drawRectsEPK5QRecti(
    QPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9drawRectsEPK6QRectFi(
    QPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9drawLinesEPK5QLinei(
    QPaintEngine *self,
    const QLine *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9drawLinesEPK6QLineFi(
    QPaintEngine *self,
    const QLineF *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPaintEngine::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine11drawEllipseERK6QRectF(
    QPaintEngine *self,
    const QRectF *r) {
  self->drawEllipse(*r);
}

//  void QPaintEngine::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine11drawEllipseERK5QRect(
    QPaintEngine *self,
    const QRect *r) {
  self->drawEllipse(*r);
}

//  void QPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine8drawPathERK12QPainterPath(
    QPaintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine10drawPointsEPK7QPointFi(
    QPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine10drawPointsEPK6QPointi(
    QPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPaintEngine::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE(
    QPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE(
    QPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm, const
//      QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QPaintEngine::drawImage(const QRectF &r, const QImage &pm, const
//      QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPaintEngine::setPaintDevice(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine14setPaintDeviceEP12QPaintDevice(
    QPaintEngine *self,
    QPaintDevice *device) {
  self->setPaintDevice(device);
}

//  QPaintDevice *QPaintEngine::paintDevice() const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK12QPaintEngine11paintDeviceEv(
    const QPaintEngine *self) {
  return self->paintDevice();
}

//  void QPaintEngine::setSystemClip(const QRegion &baseClip)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine13setSystemClipERK7QRegion(
    QPaintEngine *self,
    const QRegion *baseClip) {
  self->setSystemClip(*baseClip);
}

//  QRegion QPaintEngine::systemClip() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK12QPaintEngine10systemClipEv(const QPaintEngine *self) {
  return new QRegion(self->systemClip());
}

//  void QPaintEngine::setSystemRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine13setSystemRectERK5QRect(
    QPaintEngine *self,
    const QRect *rect) {
  self->setSystemRect(*rect);
}

//  QRect QPaintEngine::systemRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QPaintEngine10systemRectEv(const QPaintEngine *self) {
  return new QRect(self->systemRect());
}

//  QPoint QPaintEngine::coordinateOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QPaintEngine16coordinateOffsetEv(
    const QPaintEngine *self) {
  return new QPoint(self->coordinateOffset());
}

//  Type QPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK12QPaintEngine4typeEv(
    const QPaintEngine *self) {
  return self->type();
}

//  void QPaintEngine::fix_neg_rect(int *x, int *y, int *w, int *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine12fix_neg_rectEPiS0_S0_S0_(
    QPaintEngine *self,
    int *x,
    int *y,
    int *w,
    int *h) {
  self->fix_neg_rect(x, y, w, h);
}

//  bool QPaintEngine::testDirty(DirtyFlags df)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPaintEngine9testDirtyE6QFlagsINS_9DirtyFlagEE(
    QPaintEngine *self,
    int df) {
  return self->testDirty(QFlags<QPaintEngine::DirtyFlag>::fromInt(df));
}

//  void QPaintEngine::setDirty(DirtyFlags df)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine8setDirtyE6QFlagsINS_9DirtyFlagEE(
    QPaintEngine *self,
    int df) {
  self->setDirty(QFlags<QPaintEngine::DirtyFlag>::fromInt(df));
}

//  void QPaintEngine::clearDirty(DirtyFlags df)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine10clearDirtyE6QFlagsINS_9DirtyFlagEE(
    QPaintEngine *self,
    int df) {
  self->clearDirty(QFlags<QPaintEngine::DirtyFlag>::fromInt(df));
}

//  bool QPaintEngine::hasFeature(PaintEngineFeatures feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPaintEngine10hasFeatureE6QFlagsINS_18PaintEngineFeatureEE(
    const QPaintEngine *self,
    int feature) {
  return self->hasFeature(
      QFlags<QPaintEngine::PaintEngineFeature>::fromInt(feature));
}

//  QPainter *QPaintEngine::painter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZNK12QPaintEngine7painterEv(const QPaintEngine *self) {
  return self->painter();
}

//  void QPaintEngine::syncState()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintEngine9syncStateEv(QPaintEngine *self) {
  self->syncState();
}

//  bool QPaintEngine::isExtended() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPaintEngine10isExtendedEv(const QPaintEngine *self) {
  return self->isExtended();
}

//  QPixmap QPaintEngine::createPixmap(QSize size)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN12QPaintEngine12createPixmapE5QSize(
    QPaintEngine *self,
    const QSize *size) {
  return new QPixmap(self->createPixmap(*size));
}

//  QPixmap QPaintEngine::createPixmapFromImage(QImage image,
//      Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    QPaintEngine *self,
    const QImage *image,
    int flags) {
  return new QPixmap(
      self->createPixmapFromImage(
          *image,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}
