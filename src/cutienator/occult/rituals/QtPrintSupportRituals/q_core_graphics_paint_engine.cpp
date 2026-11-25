//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_mac_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
//  Its header names CoreGraphics' types without including
//  CoreGraphics, as Qt's own sources include it first; so does this
//  file.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructors, 'updatePen', 'updateBrush',
//  'updateFont', 'updateOpacity', 'updateMatrix', 'updateTransform',
//  'updateClipRegion', 'updateClipPath', 'updateCompositionMode',
//  'updateRenderHints', 'handle', 'initialize', 'cleanup' and
//  'supportedRenderHints', which Qt's library offers not.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_MACOS)
#include <ApplicationServices/ApplicationServices.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_mac_p.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmap.h>

//  QCoreGraphicsPaintEngine::~QCoreGraphicsPaintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngineD1Ev(
    QCoreGraphicsPaintEngine *self) {
  delete self;
}

//  bool QCoreGraphicsPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QCoreGraphicsPaintEngine5beginEP12QPaintDevice(
    QCoreGraphicsPaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QCoreGraphicsPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QCoreGraphicsPaintEngine3endEv(
    QCoreGraphicsPaintEngine *self) {
  return self->end();
}

//  void QCoreGraphicsPaintEngine::updateState(const QPaintEngineState
//      &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine11updateStateERK17QPaintEngineState(
    QCoreGraphicsPaintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QCoreGraphicsPaintEngine::drawLines(const QLineF *lines, int
//      lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine9drawLinesEPK6QLineFi(
    QCoreGraphicsPaintEngine *self,
    const QLineF *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QCoreGraphicsPaintEngine::drawRects(const QRectF *rects, int
//      rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine9drawRectsEPK6QRectFi(
    QCoreGraphicsPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QCoreGraphicsPaintEngine::drawPoints(const QPointF *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine10drawPointsEPK7QPointFi(
    QCoreGraphicsPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QCoreGraphicsPaintEngine::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine11drawEllipseERK6QRectF(
    QCoreGraphicsPaintEngine *self,
    const QRectF *r) {
  self->drawEllipse(*r);
}

//  void QCoreGraphicsPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine8drawPathERK12QPainterPath(
    QCoreGraphicsPaintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QCoreGraphicsPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QCoreGraphicsPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QCoreGraphicsPaintEngine::drawPixmap(const QRectF &r, const QPixmap
//      &pm, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QCoreGraphicsPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QCoreGraphicsPaintEngine::drawTiledPixmap(const QRectF &r, const
//      QPixmap &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QCoreGraphicsPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QCoreGraphicsPaintEngine::drawTextItem(const QPointF &p, const
//      QTextItem &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QCoreGraphicsPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QCoreGraphicsPaintEngine::drawImage(const QRectF &r, const QImage
//      &pm, const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QCoreGraphicsPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->drawImage(
      *r, *pm, *sr, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  QPaintEngine::Type QCoreGraphicsPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK24QCoreGraphicsPaintEngine4typeEv(
    const QCoreGraphicsPaintEngine *self) {
  return self->type();
}

//  void QCoreGraphicsPaintEngine::drawLines(const QLine *lines, int
//      lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine9drawLinesEPK5QLinei(
    QCoreGraphicsPaintEngine *self,
    const QLine *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QCoreGraphicsPaintEngine::drawRects(const QRect *rects, int
//      rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine9drawRectsEPK5QRecti(
    QCoreGraphicsPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QCoreGraphicsPaintEngine::drawPoints(const QPoint *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine10drawPointsEPK6QPointi(
    QCoreGraphicsPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QCoreGraphicsPaintEngine::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine11drawEllipseERK5QRect(
    QCoreGraphicsPaintEngine *self,
    const QRect *r) {
  self->drawEllipse(*r);
}

//  void QCoreGraphicsPaintEngine::drawPolygon(const QPoint *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCoreGraphicsPaintEngine11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QCoreGraphicsPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  QCoreGraphicsPaintEnginePrivate *QCoreGraphicsPaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QCoreGraphicsPaintEnginePrivate *ritual_ZN24QCoreGraphicsPaintEngine6d_funcEv(
    QCoreGraphicsPaintEngine *self) {
  return self->d_func();
}

//  const QCoreGraphicsPaintEnginePrivate *QCoreGraphicsPaintEngine::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QCoreGraphicsPaintEnginePrivate *ritual_ZNK24QCoreGraphicsPaintEngine6d_funcEv(
    const QCoreGraphicsPaintEngine *self) {
  return self->d_func();
}

#endif  // defined(Q_OS_MACOS)
