//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpaintengine.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qregion.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QAlphaPaintEngine that Python can take functions over in. Every QAlphaPaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQAlphaPaintEngineCall0)(const void *, QPaintDevice *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQAlphaPaintEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall2)(const void *, const QPaintEngineState *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall3)(const void *, const QPainterPath *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall4)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall5)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall6)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall7)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // !defined(QT_NO_PRINTER)
typedef void (*CuteQAlphaPaintEngineCall8)(const void *, const QRect *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall9)(const void *, const QRectF *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall10)(const void *, const QLine *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall11)(const void *, const QLineF *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall12)(const void *, const QRectF *, int *);
typedef void (*CuteQAlphaPaintEngineCall13)(const void *, const QRect *, int *);
typedef void (*CuteQAlphaPaintEngineCall14)(const void *, const QPointF *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall15)(const void *, const QPoint *, int, int *);
typedef void (*CuteQAlphaPaintEngineCall16)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQAlphaPaintEngineCall17)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef const QPoint * (*CuteQAlphaPaintEngineCall18)(const void *, int *);
typedef int (*CuteQAlphaPaintEngineCall19)(const void *, int *);
typedef const QPixmap * (*CuteQAlphaPaintEngineCall20)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQAlphaPaintEngineCall21)(const void *, const QImage *, int, int *);
class CuteQAlphaPaintEngine : public QAlphaPaintEngine {
public:
  using QAlphaPaintEngine::QAlphaPaintEngine;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12createPixmapE5QSize")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[21] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  bool QAlphaPaintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall0 call = reinterpret_cast<CuteQAlphaPaintEngineCall0>(taken[0]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QAlphaPaintEngine::begin(pdev);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QAlphaPaintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall1 call = reinterpret_cast<CuteQAlphaPaintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAlphaPaintEngine::end();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall2 call = reinterpret_cast<CuteQAlphaPaintEngineCall2>(taken[2]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::updateState(state);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall3 call = reinterpret_cast<CuteQAlphaPaintEngineCall3>(taken[3]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::drawPath(path);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall4 call = reinterpret_cast<CuteQAlphaPaintEngineCall4>(taken[4]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall5 call = reinterpret_cast<CuteQAlphaPaintEngineCall5>(taken[5]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::drawPixmap(r, pm, sr);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::drawTextItem(const QPointF &p, const
  //      QTextItem &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall6 call = reinterpret_cast<CuteQAlphaPaintEngineCall6>(taken[6]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::drawTextItem(p, textItem);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QAlphaPaintEngine::drawTiledPixmap(const QRectF &r, const
  //      QPixmap &pixmap, const QPointF &s)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pixmap,
      const QPointF &s) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall7 call = reinterpret_cast<CuteQAlphaPaintEngineCall7>(taken[7]);
      call(this, &r, &pixmap, &s, &handled);
      if (handled) return;
    }
    QAlphaPaintEngine::drawTiledPixmap(r, pixmap, s);
  }
#endif  // !defined(QT_NO_PRINTER)

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall8 call = reinterpret_cast<CuteQAlphaPaintEngineCall8>(taken[8]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall9 call = reinterpret_cast<CuteQAlphaPaintEngineCall9>(taken[9]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall10 call = reinterpret_cast<CuteQAlphaPaintEngineCall10>(taken[10]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall11 call = reinterpret_cast<CuteQAlphaPaintEngineCall11>(taken[11]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall12 call = reinterpret_cast<CuteQAlphaPaintEngineCall12>(taken[12]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall13 call = reinterpret_cast<CuteQAlphaPaintEngineCall13>(taken[13]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall14 call = reinterpret_cast<CuteQAlphaPaintEngineCall14>(taken[14]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall15 call = reinterpret_cast<CuteQAlphaPaintEngineCall15>(taken[15]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
  //      PolygonDrawMode mode)
  void drawPolygon(
      const QPoint *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall16 call = reinterpret_cast<CuteQAlphaPaintEngineCall16>(taken[16]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngine::drawImage(const QRectF &r, const QImage &pm, const
  //      QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall17 call = reinterpret_cast<CuteQAlphaPaintEngineCall17>(taken[17]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngine::drawImage(r, pm, sr, flags);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall18 call = reinterpret_cast<CuteQAlphaPaintEngineCall18>(taken[18]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  Type QPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall19 call = reinterpret_cast<CuteQAlphaPaintEngineCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return {};
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall20 call = reinterpret_cast<CuteQAlphaPaintEngineCall20>(taken[20]);
      const QPixmap * given = call(this, &size, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmap(size);
  }

  //  QPixmap QPaintEngine::createPixmapFromImage(QImage image,
  //      Qt::ImageConversionFlags flags)
  QPixmap createPixmapFromImage(
      QImage image,
      Qt::ImageConversionFlags flags) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAlphaPaintEngineCall21 call = reinterpret_cast<CuteQAlphaPaintEngineCall21>(taken[21]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QAlphaPaintEnginePrivate *QAlphaPaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QAlphaPaintEnginePrivate *ritual_ZN17QAlphaPaintEngine6d_funcEv(
    QAlphaPaintEngine *self) {
  return self->d_func();
}

//  const QAlphaPaintEnginePrivate *QAlphaPaintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QAlphaPaintEnginePrivate *ritual_ZNK17QAlphaPaintEngine6d_funcEv(
    const QAlphaPaintEngine *self) {
  return self->d_func();
}

//  QAlphaPaintEngine::~QAlphaPaintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngineD1Ev(QAlphaPaintEngine *self) {
  delete self;
}

//  bool QAlphaPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAlphaPaintEngine5beginEP12QPaintDevice(
    QAlphaPaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QAlphaPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAlphaPaintEngine3endEv(QAlphaPaintEngine *self) {
  return self->end();
}

//  void QAlphaPaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine11updateStateERK17QPaintEngineState(
    QAlphaPaintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QAlphaPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine8drawPathERK12QPainterPath(
    QAlphaPaintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QAlphaPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QAlphaPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QAlphaPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QAlphaPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QAlphaPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QAlphaPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QAlphaPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QAlphaPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  QAlphaPaintEngine::QAlphaPaintEngine(QAlphaPaintEnginePrivate &data,
//      PaintEngineFeatures devcaps)
extern "C" Q_DECL_EXPORT
QAlphaPaintEngine *ritual_ZN17QAlphaPaintEngineC1ER24QAlphaPaintEnginePrivate6QFlagsIN12QPaintEngine18PaintEngineFeatureEE(
    QAlphaPaintEnginePrivate *data,
    int devcaps) {
  return new CuteQAlphaPaintEngine(
      *data,
      QFlags<QPaintEngine::PaintEngineFeature>::fromInt(devcaps));
}

//  QRegion QAlphaPaintEngine::alphaClipping() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK17QAlphaPaintEngine13alphaClippingEv(
    const QAlphaPaintEngine *self) {
  return new QRegion(self->alphaClipping());
}

//  bool QAlphaPaintEngine::continueCall() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAlphaPaintEngine12continueCallEv(
    const QAlphaPaintEngine *self) {
  return self->continueCall();
}

//  void QAlphaPaintEngine::flushAndInit(bool init)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine12flushAndInitEb(
    QAlphaPaintEngine *self,
    bool init) {
  self->flushAndInit(init);
}

//  void QAlphaPaintEngine::cleanUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAlphaPaintEngine7cleanUpEv(QAlphaPaintEngine *self) {
  self->cleanUp();
}

//  a Python function taken by a CuteQAlphaPaintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAlphaPaintEngine(
    QAlphaPaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAlphaPaintEngine *>(self)->take(key, call);
}

//  bool QAlphaPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAlphaPaintEngine5beginEP12QPaintDevice(
    QAlphaPaintEngine *self,
    QPaintDevice *pdev) {
  return self->QAlphaPaintEngine::begin(pdev);
}

//  bool QAlphaPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAlphaPaintEngine3endEv(QAlphaPaintEngine *self) {
  return self->QAlphaPaintEngine::end();
}

//  void QAlphaPaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine11updateStateERK17QPaintEngineState(
    QAlphaPaintEngine *self,
    const QPaintEngineState *state) {
  self->QAlphaPaintEngine::updateState(*state);
}

//  void QAlphaPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine8drawPathERK12QPainterPath(
    QAlphaPaintEngine *self,
    const QPainterPath *path) {
  self->QAlphaPaintEngine::drawPath(*path);
}

//  void QAlphaPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QAlphaPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QAlphaPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QAlphaPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QAlphaPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QAlphaPaintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QAlphaPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QAlphaPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QAlphaPaintEngine::drawTextItem(*p, *textItem);
}

//  void QAlphaPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAlphaPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QAlphaPaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->QAlphaPaintEngine::drawTiledPixmap(*r, *pixmap, *s);
}

#endif  // !defined(QT_NO_PRINTER)
