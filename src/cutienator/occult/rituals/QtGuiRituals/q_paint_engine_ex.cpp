//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengineex_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengineex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qtransform.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPaintEngineEx that Python can take functions over in. Every QPaintEngineEx
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPaintEngineExCall0)(const void *, QPainterState *, int *);
typedef void (*CuteQPaintEngineExCall1)(const void *, const QRect *, int, int *);
typedef void (*CuteQPaintEngineExCall2)(const void *, const QRegion *, int, int *);
typedef void (*CuteQPaintEngineExCall3)(const void *, const QPainterPath *, int, int *);
typedef void (*CuteQPaintEngineExCall4)(const void *, int *);
typedef void (*CuteQPaintEngineExCall5)(const void *, int *);
typedef void (*CuteQPaintEngineExCall6)(const void *, int *);
typedef void (*CuteQPaintEngineExCall7)(const void *, int *);
typedef void (*CuteQPaintEngineExCall8)(const void *, int *);
typedef void (*CuteQPaintEngineExCall9)(const void *, int *);
typedef void (*CuteQPaintEngineExCall10)(const void *, int *);
typedef void (*CuteQPaintEngineExCall11)(const void *, int *);
typedef void (*CuteQPaintEngineExCall12)(const void *, const QRectF *, const QBrush *, int *);
typedef void (*CuteQPaintEngineExCall13)(const void *, const QRectF *, const QColor *, int *);
typedef void (*CuteQPaintEngineExCall14)(const void *, const QRectF *, qreal, qreal, int, int *);
typedef void (*CuteQPaintEngineExCall15)(const void *, const QRect *, int, int *);
typedef void (*CuteQPaintEngineExCall16)(const void *, const QRectF *, int, int *);
typedef void (*CuteQPaintEngineExCall17)(const void *, const QLine *, int, int *);
typedef void (*CuteQPaintEngineExCall18)(const void *, const QLineF *, int, int *);
typedef void (*CuteQPaintEngineExCall19)(const void *, const QRectF *, int *);
typedef void (*CuteQPaintEngineExCall20)(const void *, const QRect *, int *);
typedef void (*CuteQPaintEngineExCall21)(const void *, const QPainterPath *, int *);
typedef void (*CuteQPaintEngineExCall22)(const void *, const QPointF *, int, int *);
typedef void (*CuteQPaintEngineExCall23)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPaintEngineExCall24)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQPaintEngineExCall25)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQPaintEngineExCall26)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
typedef void (*CuteQPaintEngineExCall27)(const void *, const QPointF *, const QPixmap *, int *);
typedef void (*CuteQPaintEngineExCall28)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef void (*CuteQPaintEngineExCall29)(const void *, const QPointF *, const QImage *, int *);
typedef void (*CuteQPaintEngineExCall30)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
typedef void (*CuteQPaintEngineExCall31)(const void *, const QPainter::PixmapFragment *, int, const QPixmap *, int, int *);
typedef void (*CuteQPaintEngineExCall32)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQPaintEngineExCall33)(const void *, QStaticTextItem *, int *);
typedef void (*CuteQPaintEngineExCall34)(const void *, QPainterState *, int *);
typedef void (*CuteQPaintEngineExCall35)(const void *, int *);
typedef void (*CuteQPaintEngineExCall36)(const void *, int *);
typedef void (*CuteQPaintEngineExCall37)(const void *, int *);
typedef uint (*CuteQPaintEngineExCall38)(const void *, int *);
typedef bool (*CuteQPaintEngineExCall39)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQPaintEngineExCall40)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQPaintEngineExCall41)(const void *, QPaintDevice *, int *);
typedef bool (*CuteQPaintEngineExCall42)(const void *, int *);
typedef void (*CuteQPaintEngineExCall43)(const void *, const QPointF *, const QTextItem *, int *);
typedef const QPoint * (*CuteQPaintEngineExCall44)(const void *, int *);
typedef int (*CuteQPaintEngineExCall45)(const void *, int *);
typedef const QPixmap * (*CuteQPaintEngineExCall46)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQPaintEngineExCall47)(const void *, const QImage *, int, int *);
class CuteQPaintEngineEx : public QPaintEngineEx {
public:
  using QPaintEngineEx::QPaintEngineEx;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx11createStateEP13QPainterState")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperationE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18clipEnabledChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10penChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx12brushChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18brushOriginChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx14opacityChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx22compositionModeChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18renderHintsChangedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx16transformChangedEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeModeE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8setStateEP13QPainterState")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4syncEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx19beginNativePaintingEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx17endNativePaintingEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx5flagsEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12createPixmapE5QSize")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[47] = call;
      return true;
    }
    return false;
  }

  //  QPainterState *QPaintEngineEx::createState(QPainterState *orig) const
  QPainterState *createState(QPainterState *orig) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintEngineExCall0 call = reinterpret_cast<CuteQPaintEngineExCall0>(taken[0]);
      void * given = call(this, orig, &handled);
      if (handled) return static_cast<QPainterState *>(given);
    }
    return QPaintEngineEx::createState(orig);
  }

  //  void QPaintEngineEx::clip(const QRect &rect, Qt::ClipOperation op)
  void clip(const QRect &rect, Qt::ClipOperation op) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintEngineExCall1 call = reinterpret_cast<CuteQPaintEngineExCall1>(taken[1]);
      call(this, &rect, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QPaintEngineEx::clip(rect, op);
  }

  //  void QPaintEngineEx::clip(const QRegion &region, Qt::ClipOperation
  //      op)
  void clip(const QRegion &region, Qt::ClipOperation op) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPaintEngineExCall2 call = reinterpret_cast<CuteQPaintEngineExCall2>(taken[2]);
      call(this, &region, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QPaintEngineEx::clip(region, op);
  }

  //  void QPaintEngineEx::clip(const QPainterPath &path, Qt::ClipOperation
  //      op)
  void clip(const QPainterPath &path, Qt::ClipOperation op) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPaintEngineExCall3 call = reinterpret_cast<CuteQPaintEngineExCall3>(taken[3]);
      call(this, &path, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QPaintEngineEx::clip(path, op);
  }

  //  void QPaintEngineEx::clipEnabledChanged()
  void clipEnabledChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPaintEngineExCall4 call = reinterpret_cast<CuteQPaintEngineExCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::penChanged()
  void penChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPaintEngineExCall5 call = reinterpret_cast<CuteQPaintEngineExCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::brushChanged()
  void brushChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPaintEngineExCall6 call = reinterpret_cast<CuteQPaintEngineExCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::brushOriginChanged()
  void brushOriginChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPaintEngineExCall7 call = reinterpret_cast<CuteQPaintEngineExCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::opacityChanged()
  void opacityChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPaintEngineExCall8 call = reinterpret_cast<CuteQPaintEngineExCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::compositionModeChanged()
  void compositionModeChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPaintEngineExCall9 call = reinterpret_cast<CuteQPaintEngineExCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::renderHintsChanged()
  void renderHintsChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPaintEngineExCall10 call = reinterpret_cast<CuteQPaintEngineExCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::transformChanged()
  void transformChanged() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPaintEngineExCall11 call = reinterpret_cast<CuteQPaintEngineExCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::fillRect(const QRectF &rect, const QBrush
  //      &brush)
  void fillRect(const QRectF &rect, const QBrush &brush) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPaintEngineExCall12 call = reinterpret_cast<CuteQPaintEngineExCall12>(taken[12]);
      call(this, &rect, &brush, &handled);
      if (handled) return;
    }
    QPaintEngineEx::fillRect(rect, brush);
  }

  //  void QPaintEngineEx::fillRect(const QRectF &rect, const QColor
  //      &color)
  void fillRect(const QRectF &rect, const QColor &color) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPaintEngineExCall13 call = reinterpret_cast<CuteQPaintEngineExCall13>(taken[13]);
      call(this, &rect, &color, &handled);
      if (handled) return;
    }
    QPaintEngineEx::fillRect(rect, color);
  }

  //  void QPaintEngineEx::drawRoundedRect(const QRectF &rect, qreal xrad,
  //      qreal yrad, Qt::SizeMode mode)
  void drawRoundedRect(
      const QRectF &rect,
      qreal xrad,
      qreal yrad,
      Qt::SizeMode mode) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPaintEngineExCall14 call = reinterpret_cast<CuteQPaintEngineExCall14>(taken[14]);
      call(this, &rect, xrad, yrad, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRoundedRect(rect, xrad, yrad, mode);
  }

  //  void QPaintEngineEx::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPaintEngineExCall15 call = reinterpret_cast<CuteQPaintEngineExCall15>(taken[15]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRects(rects, rectCount);
  }

  //  void QPaintEngineEx::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPaintEngineExCall16 call = reinterpret_cast<CuteQPaintEngineExCall16>(taken[16]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRects(rects, rectCount);
  }

  //  void QPaintEngineEx::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPaintEngineExCall17 call = reinterpret_cast<CuteQPaintEngineExCall17>(taken[17]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawLines(lines, lineCount);
  }

  //  void QPaintEngineEx::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPaintEngineExCall18 call = reinterpret_cast<CuteQPaintEngineExCall18>(taken[18]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawLines(lines, lineCount);
  }

  //  void QPaintEngineEx::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPaintEngineExCall19 call = reinterpret_cast<CuteQPaintEngineExCall19>(taken[19]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPaintEngineExCall20 call = reinterpret_cast<CuteQPaintEngineExCall20>(taken[20]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPaintEngineExCall21 call = reinterpret_cast<CuteQPaintEngineExCall21>(taken[21]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPath(path);
  }

  //  void QPaintEngineEx::drawPoints(const QPointF *points, int
  //      pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPaintEngineExCall22 call = reinterpret_cast<CuteQPaintEngineExCall22>(taken[22]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPoints(points, pointCount);
  }

  //  void QPaintEngineEx::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPaintEngineExCall23 call = reinterpret_cast<CuteQPaintEngineExCall23>(taken[23]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPoints(points, pointCount);
  }

  //  void QPaintEngineEx::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPaintEngineExCall24 call = reinterpret_cast<CuteQPaintEngineExCall24>(taken[24]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngineEx::drawPolygon(const QPoint *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPoint *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPaintEngineExCall25 call = reinterpret_cast<CuteQPaintEngineExCall25>(taken[25]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngineEx::drawPixmap(const QRectF &r, const QPixmap &pm,
  //      const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPaintEngineExCall26 call = reinterpret_cast<CuteQPaintEngineExCall26>(taken[26]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::drawPixmap(const QPointF &pos, const QPixmap
  //      &pm)
  void drawPixmap(const QPointF &pos, const QPixmap &pm) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPaintEngineExCall27 call = reinterpret_cast<CuteQPaintEngineExCall27>(taken[27]);
      call(this, &pos, &pm, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPixmap(pos, pm);
  }

  //  void QPaintEngineEx::drawImage(const QRectF &r, const QImage &pm,
  //      const QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPaintEngineExCall28 call = reinterpret_cast<CuteQPaintEngineExCall28>(taken[28]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QPaintEngineEx::drawImage(const QPointF &pos, const QImage
  //      &image)
  void drawImage(const QPointF &pos, const QImage &image) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPaintEngineExCall29 call = reinterpret_cast<CuteQPaintEngineExCall29>(taken[29]);
      call(this, &pos, &image, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawImage(pos, image);
  }

  //  void QPaintEngineEx::drawTiledPixmap(const QRectF &r, const QPixmap
  //      &pixmap, const QPointF &s)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pixmap,
      const QPointF &s) override {
    if (taken[30]) {
      int handled = 0;
      CuteQPaintEngineExCall30 call = reinterpret_cast<CuteQPaintEngineExCall30>(taken[30]);
      call(this, &r, &pixmap, &s, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawTiledPixmap(r, pixmap, s);
  }

  //  void QPaintEngineEx::drawPixmapFragments(const
  //      QPainter::PixmapFragment *fragments, int fragmentCount, const
  //      QPixmap &pixmap, QFlags<QPainter::PixmapFragmentHint> hints)
  void drawPixmapFragments(
      const QPainter::PixmapFragment *fragments,
      int fragmentCount,
      const QPixmap &pixmap,
      QFlags<QPainter::PixmapFragmentHint> hints) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPaintEngineExCall31 call = reinterpret_cast<CuteQPaintEngineExCall31>(taken[31]);
      call(this, fragments, fragmentCount, &pixmap, static_cast<int>(hints.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPixmapFragments(fragments, fragmentCount, pixmap, hints);
  }

  //  void QPaintEngineEx::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPaintEngineExCall32 call = reinterpret_cast<CuteQPaintEngineExCall32>(taken[32]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPaintEngineEx::updateState(state);
  }

  //  void QPaintEngineEx::drawStaticTextItem(QStaticTextItem *a0)
  void drawStaticTextItem(QStaticTextItem *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPaintEngineExCall33 call = reinterpret_cast<CuteQPaintEngineExCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawStaticTextItem(a0);
  }

  //  void QPaintEngineEx::setState(QPainterState *s)
  void setState(QPainterState *s) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPaintEngineExCall34 call = reinterpret_cast<CuteQPaintEngineExCall34>(taken[34]);
      call(this, s, &handled);
      if (handled) return;
    }
    QPaintEngineEx::setState(s);
  }

  //  void QPaintEngineEx::sync()
  void sync() override {
    if (taken[35]) {
      int handled = 0;
      CuteQPaintEngineExCall35 call = reinterpret_cast<CuteQPaintEngineExCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::sync();
  }

  //  void QPaintEngineEx::beginNativePainting()
  void beginNativePainting() override {
    if (taken[36]) {
      int handled = 0;
      CuteQPaintEngineExCall36 call = reinterpret_cast<CuteQPaintEngineExCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::beginNativePainting();
  }

  //  void QPaintEngineEx::endNativePainting()
  void endNativePainting() override {
    if (taken[37]) {
      int handled = 0;
      CuteQPaintEngineExCall37 call = reinterpret_cast<CuteQPaintEngineExCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::endNativePainting();
  }

  //  uint QPaintEngineEx::flags() const
  uint flags() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQPaintEngineExCall38 call = reinterpret_cast<CuteQPaintEngineExCall38>(taken[38]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::flags();
  }

  //  bool QPaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
  //      *fontEngine, const QTransform &m) const
  bool requiresPretransformedGlyphPositions(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQPaintEngineExCall39 call = reinterpret_cast<CuteQPaintEngineExCall39>(taken[39]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::requiresPretransformedGlyphPositions(fontEngine, m);
  }

  //  bool QPaintEngineEx::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
  //      const QTransform &m) const
  bool shouldDrawCachedGlyphs(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPaintEngineExCall40 call = reinterpret_cast<CuteQPaintEngineExCall40>(taken[40]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::shouldDrawCachedGlyphs(fontEngine, m);
  }

  //  bool QPaintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[41]) {
      int handled = 0;
      CuteQPaintEngineExCall41 call = reinterpret_cast<CuteQPaintEngineExCall41>(taken[41]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPaintEngine::end()
  bool end() override {
    if (taken[42]) {
      int handled = 0;
      CuteQPaintEngineExCall42 call = reinterpret_cast<CuteQPaintEngineExCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPaintEngine::drawTextItem(const QPointF &p, const QTextItem
  //      &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[43]) {
      int handled = 0;
      CuteQPaintEngineExCall43 call = reinterpret_cast<CuteQPaintEngineExCall43>(taken[43]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QPaintEngine::drawTextItem(p, textItem);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQPaintEngineExCall44 call = reinterpret_cast<CuteQPaintEngineExCall44>(taken[44]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  Type QPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQPaintEngineExCall45 call = reinterpret_cast<CuteQPaintEngineExCall45>(taken[45]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return {};
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[46]) {
      int handled = 0;
      CuteQPaintEngineExCall46 call = reinterpret_cast<CuteQPaintEngineExCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQPaintEngineExCall47 call = reinterpret_cast<CuteQPaintEngineExCall47>(taken[47]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QPaintEngineExPrivate *QPaintEngineEx::d_func()
extern "C" Q_DECL_EXPORT
QPaintEngineExPrivate *ritual_ZN14QPaintEngineEx6d_funcEv(
    QPaintEngineEx *self) {
  return self->d_func();
}

//  const QPaintEngineExPrivate *QPaintEngineEx::d_func() const
extern "C" Q_DECL_EXPORT
const QPaintEngineExPrivate *ritual_ZNK14QPaintEngineEx6d_funcEv(
    const QPaintEngineEx *self) {
  return self->d_func();
}

//  QPainterState *QPaintEngineEx::createState(QPainterState *orig) const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZNK14QPaintEngineEx11createStateEP13QPainterState(
    const QPaintEngineEx *self,
    QPainterState *orig) {
  return self->createState(orig);
}

//  void QPaintEngineEx::clip(const QRect &rect, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QRect *rect,
    Qt::ClipOperation op) {
  self->clip(*rect, op);
}

//  void QPaintEngineEx::clip(const QRegion &region, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QRegion *region,
    Qt::ClipOperation op) {
  self->clip(*region, op);
}

//  void QPaintEngineEx::clip(const QPainterPath &path, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QPainterPath *path,
    Qt::ClipOperation op) {
  self->clip(*path, op);
}

//  void QPaintEngineEx::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx18clipEnabledChangedEv(QPaintEngineEx *self) {
  self->clipEnabledChanged();
}

//  void QPaintEngineEx::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx10penChangedEv(QPaintEngineEx *self) {
  self->penChanged();
}

//  void QPaintEngineEx::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx12brushChangedEv(QPaintEngineEx *self) {
  self->brushChanged();
}

//  void QPaintEngineEx::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx18brushOriginChangedEv(QPaintEngineEx *self) {
  self->brushOriginChanged();
}

//  void QPaintEngineEx::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx14opacityChangedEv(QPaintEngineEx *self) {
  self->opacityChanged();
}

//  void QPaintEngineEx::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx22compositionModeChangedEv(
    QPaintEngineEx *self) {
  self->compositionModeChanged();
}

//  void QPaintEngineEx::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx18renderHintsChangedEv(QPaintEngineEx *self) {
  self->renderHintsChanged();
}

//  void QPaintEngineEx::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx16transformChangedEv(QPaintEngineEx *self) {
  self->transformChanged();
}

//  void QPaintEngineEx::fillRect(const QRectF &rect, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush(
    QPaintEngineEx *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->fillRect(*rect, *brush);
}

//  void QPaintEngineEx::fillRect(const QRectF &rect, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor(
    QPaintEngineEx *self,
    const QRectF *rect,
    const QColor *color) {
  self->fillRect(*rect, *color);
}

//  void QPaintEngineEx::drawRoundedRect(const QRectF &rect, qreal xrad,
//      qreal yrad, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeModeE(
    QPaintEngineEx *self,
    const QRectF *rect,
    qreal xrad,
    qreal yrad,
    Qt::SizeMode mode) {
  self->drawRoundedRect(*rect, xrad, yrad, mode);
}

//  void QPaintEngineEx::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawRectsEPK5QRecti(
    QPaintEngineEx *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPaintEngineEx::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawRectsEPK6QRectFi(
    QPaintEngineEx *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPaintEngineEx::drawLines(const QLine *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawLinesEPK5QLinei(
    QPaintEngineEx *self,
    const QLine *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPaintEngineEx::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawLinesEPK6QLineFi(
    QPaintEngineEx *self,
    const QLineF *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPaintEngineEx::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx11drawEllipseERK6QRectF(
    QPaintEngineEx *self,
    const QRectF *r) {
  self->drawEllipse(*r);
}

//  void QPaintEngineEx::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx11drawEllipseERK5QRect(
    QPaintEngineEx *self,
    const QRect *r) {
  self->drawEllipse(*r);
}

//  void QPaintEngineEx::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx8drawPathERK12QPainterPath(
    QPaintEngineEx *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPaintEngineEx::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx10drawPointsEPK7QPointFi(
    QPaintEngineEx *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPaintEngineEx::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx10drawPointsEPK6QPointi(
    QPaintEngineEx *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPaintEngineEx::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPaintEngineEx *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPaintEngineEx::drawPolygon(const QPoint *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QPaintEngineEx *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPaintEngineEx::drawPixmap(const QRectF &r, const QPixmap &pm, const
//      QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPaintEngineEx *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QPaintEngineEx::drawPixmap(const QPointF &pos, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap(
    QPaintEngineEx *self,
    const QPointF *pos,
    const QPixmap *pm) {
  self->drawPixmap(*pos, *pm);
}

//  void QPaintEngineEx::drawImage(const QRectF &r, const QImage &pm, const
//      QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPaintEngineEx *self,
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

//  void QPaintEngineEx::drawImage(const QPointF &pos, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage(
    QPaintEngineEx *self,
    const QPointF *pos,
    const QImage *image) {
  self->drawImage(*pos, *image);
}

//  void QPaintEngineEx::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPaintEngineEx *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QPaintEngineEx::drawPixmapFragments(const QPainter::PixmapFragment
//      *fragments, int fragmentCount, const QPixmap &pixmap,
//      QFlags<QPainter::PixmapFragmentHint> hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE(
    QPaintEngineEx *self,
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

//  void QPaintEngineEx::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx11updateStateERK17QPaintEngineState(
    QPaintEngineEx *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QPaintEngineEx::drawStaticTextItem(QStaticTextItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem(
    QPaintEngineEx *self,
    QStaticTextItem *a0) {
  self->drawStaticTextItem(a0);
}

//  void QPaintEngineEx::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx8setStateEP13QPainterState(
    QPaintEngineEx *self,
    QPainterState *s) {
  self->setState(s);
}

//  QPainterState *QPaintEngineEx::state()
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZN14QPaintEngineEx5stateEv(QPaintEngineEx *self) {
  return self->state();
}

//  const QPainterState *QPaintEngineEx::state() const
extern "C" Q_DECL_EXPORT
const QPainterState *ritual_ZNK14QPaintEngineEx5stateEv(
    const QPaintEngineEx *self) {
  return self->state();
}

//  void QPaintEngineEx::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx4syncEv(QPaintEngineEx *self) {
  self->sync();
}

//  void QPaintEngineEx::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx19beginNativePaintingEv(QPaintEngineEx *self) {
  self->beginNativePainting();
}

//  void QPaintEngineEx::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPaintEngineEx17endNativePaintingEv(QPaintEngineEx *self) {
  self->endNativePainting();
}

//  uint QPaintEngineEx::flags() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QPaintEngineEx5flagsEv(const QPaintEngineEx *self) {
  return self->flags();
}

//  bool QPaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QPaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->requiresPretransformedGlyphPositions(fontEngine, *m);
}

//  bool QPaintEngineEx::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
//      const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QPaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->shouldDrawCachedGlyphs(fontEngine, *m);
}

//  a Python function taken by a CuteQPaintEngineEx, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintEngineEx(
    QPaintEngineEx *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintEngineEx *>(self)->take(key, call);
}

//  QPainterState *QPaintEngineEx::createState(QPainterState *orig) const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_own_ZNK14QPaintEngineEx11createStateEP13QPainterState(
    const QPaintEngineEx *self,
    QPainterState *orig) {
  return self->QPaintEngineEx::createState(orig);
}

//  void QPaintEngineEx::clip(const QRect &rect, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QRect *rect,
    Qt::ClipOperation op) {
  self->QPaintEngineEx::clip(*rect, op);
}

//  void QPaintEngineEx::clip(const QRegion &region, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QRegion *region,
    Qt::ClipOperation op) {
  self->QPaintEngineEx::clip(*region, op);
}

//  void QPaintEngineEx::clip(const QPainterPath &path, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperationE(
    QPaintEngineEx *self,
    const QPainterPath *path,
    Qt::ClipOperation op) {
  self->QPaintEngineEx::clip(*path, op);
}

//  void QPaintEngineEx::fillRect(const QRectF &rect, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush(
    QPaintEngineEx *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->QPaintEngineEx::fillRect(*rect, *brush);
}

//  void QPaintEngineEx::fillRect(const QRectF &rect, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor(
    QPaintEngineEx *self,
    const QRectF *rect,
    const QColor *color) {
  self->QPaintEngineEx::fillRect(*rect, *color);
}

//  void QPaintEngineEx::drawRoundedRect(const QRectF &rect, qreal xrad,
//      qreal yrad, Qt::SizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeModeE(
    QPaintEngineEx *self,
    const QRectF *rect,
    qreal xrad,
    qreal yrad,
    Qt::SizeMode mode) {
  self->QPaintEngineEx::drawRoundedRect(*rect, xrad, yrad, mode);
}

//  void QPaintEngineEx::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx9drawRectsEPK5QRecti(
    QPaintEngineEx *self,
    const QRect *rects,
    int rectCount) {
  self->QPaintEngineEx::drawRects(rects, rectCount);
}

//  void QPaintEngineEx::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx9drawRectsEPK6QRectFi(
    QPaintEngineEx *self,
    const QRectF *rects,
    int rectCount) {
  self->QPaintEngineEx::drawRects(rects, rectCount);
}

//  void QPaintEngineEx::drawLines(const QLine *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx9drawLinesEPK5QLinei(
    QPaintEngineEx *self,
    const QLine *lines,
    int lineCount) {
  self->QPaintEngineEx::drawLines(lines, lineCount);
}

//  void QPaintEngineEx::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx9drawLinesEPK6QLineFi(
    QPaintEngineEx *self,
    const QLineF *lines,
    int lineCount) {
  self->QPaintEngineEx::drawLines(lines, lineCount);
}

//  void QPaintEngineEx::drawEllipse(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx11drawEllipseERK6QRectF(
    QPaintEngineEx *self,
    const QRectF *r) {
  self->QPaintEngineEx::drawEllipse(*r);
}

//  void QPaintEngineEx::drawEllipse(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx11drawEllipseERK5QRect(
    QPaintEngineEx *self,
    const QRect *r) {
  self->QPaintEngineEx::drawEllipse(*r);
}

//  void QPaintEngineEx::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx8drawPathERK12QPainterPath(
    QPaintEngineEx *self,
    const QPainterPath *path) {
  self->QPaintEngineEx::drawPath(*path);
}

//  void QPaintEngineEx::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx10drawPointsEPK7QPointFi(
    QPaintEngineEx *self,
    const QPointF *points,
    int pointCount) {
  self->QPaintEngineEx::drawPoints(points, pointCount);
}

//  void QPaintEngineEx::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx10drawPointsEPK6QPointi(
    QPaintEngineEx *self,
    const QPoint *points,
    int pointCount) {
  self->QPaintEngineEx::drawPoints(points, pointCount);
}

//  void QPaintEngineEx::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPaintEngineEx *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPaintEngineEx::drawPolygon(points, pointCount, mode);
}

//  void QPaintEngineEx::drawPolygon(const QPoint *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QPaintEngineEx *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPaintEngineEx::drawPolygon(points, pointCount, mode);
}

//  void QPaintEngineEx::drawPixmap(const QPointF &pos, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap(
    QPaintEngineEx *self,
    const QPointF *pos,
    const QPixmap *pm) {
  self->QPaintEngineEx::drawPixmap(*pos, *pm);
}

//  void QPaintEngineEx::drawImage(const QPointF &pos, const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage(
    QPaintEngineEx *self,
    const QPointF *pos,
    const QImage *image) {
  self->QPaintEngineEx::drawImage(*pos, *image);
}

//  void QPaintEngineEx::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPaintEngineEx *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->QPaintEngineEx::drawTiledPixmap(*r, *pixmap, *s);
}

//  void QPaintEngineEx::drawPixmapFragments(const QPainter::PixmapFragment
//      *fragments, int fragmentCount, const QPixmap &pixmap,
//      QFlags<QPainter::PixmapFragmentHint> hints)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE(
    QPaintEngineEx *self,
    const QPainter::PixmapFragment *fragments,
    int fragmentCount,
    const QPixmap *pixmap,
    int hints) {
  self->QPaintEngineEx::drawPixmapFragments(
      fragments,
      fragmentCount,
      *pixmap,
      QFlags<QPainter::PixmapFragmentHint>::fromInt(hints));
}

//  void QPaintEngineEx::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx11updateStateERK17QPaintEngineState(
    QPaintEngineEx *self,
    const QPaintEngineState *state) {
  self->QPaintEngineEx::updateState(*state);
}

//  void QPaintEngineEx::drawStaticTextItem(QStaticTextItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem(
    QPaintEngineEx *self,
    QStaticTextItem *a0) {
  self->QPaintEngineEx::drawStaticTextItem(a0);
}

//  void QPaintEngineEx::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx8setStateEP13QPainterState(
    QPaintEngineEx *self,
    QPainterState *s) {
  self->QPaintEngineEx::setState(s);
}

//  void QPaintEngineEx::sync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx4syncEv(QPaintEngineEx *self) {
  self->QPaintEngineEx::sync();
}

//  void QPaintEngineEx::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx19beginNativePaintingEv(
    QPaintEngineEx *self) {
  self->QPaintEngineEx::beginNativePainting();
}

//  void QPaintEngineEx::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPaintEngineEx17endNativePaintingEv(
    QPaintEngineEx *self) {
  self->QPaintEngineEx::endNativePainting();
}

//  uint QPaintEngineEx::flags() const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK14QPaintEngineEx5flagsEv(const QPaintEngineEx *self) {
  return self->QPaintEngineEx::flags();
}

//  bool QPaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QPaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->QPaintEngineEx::requiresPretransformedGlyphPositions(
      fontEngine,
      *m);
}

//  bool QPaintEngineEx::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
//      const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QPaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->QPaintEngineEx::shouldDrawCachedGlyphs(fontEngine, *m);
}
