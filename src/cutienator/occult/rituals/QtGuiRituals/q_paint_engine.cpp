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
#include <cstring>

//  A QPaintEngine that Python can take functions over in. Every QPaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPaintEngineCall0)(const void *, QPaintDevice *, int *);
typedef bool (*CuteQPaintEngineCall1)(const void *, int *);
typedef void (*CuteQPaintEngineCall2)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQPaintEngineCall3)(const void *, const QRect *, int, int *);
typedef void (*CuteQPaintEngineCall4)(const void *, const QRectF *, int, int *);
typedef void (*CuteQPaintEngineCall5)(const void *, const QLine *, int, int *);
typedef void (*CuteQPaintEngineCall6)(const void *, const QLineF *, int, int *);
typedef void (*CuteQPaintEngineCall7)(const void *, const QRectF *, int *);
typedef void (*CuteQPaintEngineCall8)(const void *, const QRect *, int *);
typedef void (*CuteQPaintEngineCall9)(const void *, const QPainterPath *, int *);
typedef void (*CuteQPaintEngineCall10)(const void *, const QPointF *, int, int *);
typedef void (*CuteQPaintEngineCall11)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPaintEngineCall12)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQPaintEngineCall13)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQPaintEngineCall14)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
typedef void (*CuteQPaintEngineCall15)(const void *, const QPointF *, const QTextItem *, int *);
typedef void (*CuteQPaintEngineCall16)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
typedef const QPoint * (*CuteQPaintEngineCall17)(const void *, int *);
typedef int (*CuteQPaintEngineCall18)(const void *, int *);
typedef const QPixmap * (*CuteQPaintEngineCall19)(const void *, const QSize *, int *);
class CuteQPaintEngine : public QPaintEngine {
public:
  using QPaintEngine::QPaintEngine;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12createPixmapE5QSize")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  bool QPaintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintEngineCall0 call = reinterpret_cast<CuteQPaintEngineCall0>(taken[0]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPaintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintEngineCall1 call = reinterpret_cast<CuteQPaintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPaintEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPaintEngineCall2 call = reinterpret_cast<CuteQPaintEngineCall2>(taken[2]);
      call(this, &state, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPaintEngineCall3 call = reinterpret_cast<CuteQPaintEngineCall3>(taken[3]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPaintEngineCall4 call = reinterpret_cast<CuteQPaintEngineCall4>(taken[4]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPaintEngineCall5 call = reinterpret_cast<CuteQPaintEngineCall5>(taken[5]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPaintEngineCall6 call = reinterpret_cast<CuteQPaintEngineCall6>(taken[6]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPaintEngineCall7 call = reinterpret_cast<CuteQPaintEngineCall7>(taken[7]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPaintEngineCall8 call = reinterpret_cast<CuteQPaintEngineCall8>(taken[8]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPaintEngineCall9 call = reinterpret_cast<CuteQPaintEngineCall9>(taken[9]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPath(path);
  }

  //  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPaintEngineCall10 call = reinterpret_cast<CuteQPaintEngineCall10>(taken[10]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPaintEngineCall11 call = reinterpret_cast<CuteQPaintEngineCall11>(taken[11]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPolygon(const QPointF *points, int pointCount,
  //      PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPaintEngineCall12 call = reinterpret_cast<CuteQPaintEngineCall12>(taken[12]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
  //      PolygonDrawMode mode)
  void drawPolygon(
      const QPoint *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPaintEngineCall13 call = reinterpret_cast<CuteQPaintEngineCall13>(taken[13]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
  //      const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPaintEngineCall14 call = reinterpret_cast<CuteQPaintEngineCall14>(taken[14]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngine::drawTextItem(const QPointF &p, const QTextItem
  //      &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPaintEngineCall15 call = reinterpret_cast<CuteQPaintEngineCall15>(taken[15]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QPaintEngine::drawTextItem(p, textItem);
  }

  //  void QPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
  //      &pixmap, const QPointF &s)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pixmap,
      const QPointF &s) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPaintEngineCall16 call = reinterpret_cast<CuteQPaintEngineCall16>(taken[16]);
      call(this, &r, &pixmap, &s, &handled);
      if (handled) return;
    }
    QPaintEngine::drawTiledPixmap(r, pixmap, s);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPaintEngineCall17 call = reinterpret_cast<CuteQPaintEngineCall17>(taken[17]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  Type QPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPaintEngineCall18 call = reinterpret_cast<CuteQPaintEngineCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return {};
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPaintEngineCall19 call = reinterpret_cast<CuteQPaintEngineCall19>(taken[19]);
      const QPixmap * given = call(this, &size, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmap(size);
  }
};

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

//  a Python function taken by a CuteQPaintEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintEngine(
    QPaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintEngine *>(self)->take(key, call);
}

//  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine9drawRectsEPK5QRecti(
    QPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->QPaintEngine::drawRects(rects, rectCount);
}

//  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine9drawRectsEPK6QRectFi(
    QPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->QPaintEngine::drawRects(rects, rectCount);
}

//  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine9drawLinesEPK5QLinei(
    QPaintEngine *self,
    const QLine *lines,
    int lineCount) {
  self->QPaintEngine::drawLines(lines, lineCount);
}

//  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine9drawLinesEPK6QLineFi(
    QPaintEngine *self,
    const QLineF *lines,
    int lineCount) {
  self->QPaintEngine::drawLines(lines, lineCount);
}

//  void QPaintEngine::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine11drawEllipseERK6QRectF(
    QPaintEngine *self,
    const QRectF *r) {
  self->QPaintEngine::drawEllipse(*r);
}

//  void QPaintEngine::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine11drawEllipseERK5QRect(
    QPaintEngine *self,
    const QRect *r) {
  self->QPaintEngine::drawEllipse(*r);
}

//  void QPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine8drawPathERK12QPainterPath(
    QPaintEngine *self,
    const QPainterPath *path) {
  self->QPaintEngine::drawPath(*path);
}

//  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine10drawPointsEPK7QPointFi(
    QPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->QPaintEngine::drawPoints(points, pointCount);
}

//  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine10drawPointsEPK6QPointi(
    QPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->QPaintEngine::drawPoints(points, pointCount);
}

//  void QPaintEngine::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE(
    QPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE(
    QPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QPaintEngine::drawTextItem(*p, *textItem);
}

//  void QPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->QPaintEngine::drawTiledPixmap(*r, *pixmap, *s);
}

//  QPoint QPaintEngine::coordinateOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK12QPaintEngine16coordinateOffsetEv(
    const QPaintEngine *self) {
  return new QPoint(self->QPaintEngine::coordinateOffset());
}

//  QPixmap QPaintEngine::createPixmap(QSize size)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN12QPaintEngine12createPixmapE5QSize(
    QPaintEngine *self,
    const QSize *size) {
  return new QPixmap(self->QPaintEngine::createPixmap(*size));
}
