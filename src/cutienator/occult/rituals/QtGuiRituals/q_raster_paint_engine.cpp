//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QRasterPaintEngine that Python can take functions over in. Every QRasterPaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRasterPaintEngineCall0)(const void *, QPaintDevice *, int *);
typedef bool (*CuteQRasterPaintEngineCall1)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall2)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall3)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall4)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall5)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall6)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall7)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall8)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall9)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall10)(const void *, QPainterState *, int *);
typedef void * (*CuteQRasterPaintEngineCall11)(const void *, QPainterState *, int *);
typedef void (*CuteQRasterPaintEngineCall12)(const void *, const QPainterPath *, QSpanData *, int *);
typedef void (*CuteQRasterPaintEngineCall13)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQRasterPaintEngineCall14)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQRasterPaintEngineCall15)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQRasterPaintEngineCall16)(const void *, const QRectF *, int *);
typedef void (*CuteQRasterPaintEngineCall17)(const void *, const QRectF *, const QBrush *, int *);
typedef void (*CuteQRasterPaintEngineCall18)(const void *, const QRectF *, const QColor *, int *);
typedef void (*CuteQRasterPaintEngineCall19)(const void *, const QRect *, int, int *);
typedef void (*CuteQRasterPaintEngineCall20)(const void *, const QRectF *, int, int *);
typedef void (*CuteQRasterPaintEngineCall21)(const void *, const QPointF *, const QPixmap *, int *);
typedef void (*CuteQRasterPaintEngineCall22)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
typedef void (*CuteQRasterPaintEngineCall23)(const void *, const QPointF *, const QImage *, int *);
typedef void (*CuteQRasterPaintEngineCall24)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef void (*CuteQRasterPaintEngineCall25)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
typedef void (*CuteQRasterPaintEngineCall26)(const void *, const QPointF *, const QTextItem *, int *);
typedef void (*CuteQRasterPaintEngineCall27)(const void *, const QLine *, int, int *);
typedef void (*CuteQRasterPaintEngineCall28)(const void *, const QLineF *, int, int *);
typedef void (*CuteQRasterPaintEngineCall29)(const void *, const QPointF *, int, int *);
typedef void (*CuteQRasterPaintEngineCall30)(const void *, const QPoint *, int, int *);
typedef void (*CuteQRasterPaintEngineCall31)(const void *, const QRect *, int, int *);
typedef void (*CuteQRasterPaintEngineCall32)(const void *, const QRegion *, int, int *);
typedef void (*CuteQRasterPaintEngineCall33)(const void *, QStaticTextItem *, int *);
typedef bool (*CuteQRasterPaintEngineCall34)(const void *, int, const glyph_t *, const QFixedPoint *, QFontEngine *, int *);
typedef int (*CuteQRasterPaintEngineCall35)(const void *, int *);
typedef const QPoint * (*CuteQRasterPaintEngineCall36)(const void *, int *);
typedef bool (*CuteQRasterPaintEngineCall37)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQRasterPaintEngineCall38)(const void *, QFontEngine *, const QTransform *, int *);
typedef void (*CuteQRasterPaintEngineCall39)(const void *, const QPainterPath *, int, int *);
typedef void (*CuteQRasterPaintEngineCall40)(const void *, const QRectF *, qreal, qreal, int, int *);
typedef void (*CuteQRasterPaintEngineCall41)(const void *, const QRect *, int *);
typedef void (*CuteQRasterPaintEngineCall42)(const void *, const QPainterPath *, int *);
typedef void (*CuteQRasterPaintEngineCall43)(const void *, const QPainter::PixmapFragment *, int, const QPixmap *, int, int *);
typedef void (*CuteQRasterPaintEngineCall44)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQRasterPaintEngineCall45)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall46)(const void *, int *);
typedef void (*CuteQRasterPaintEngineCall47)(const void *, int *);
typedef uint (*CuteQRasterPaintEngineCall48)(const void *, int *);
typedef const QPixmap * (*CuteQRasterPaintEngineCall49)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQRasterPaintEngineCall50)(const void *, const QImage *, int, int *);
class CuteQRasterPaintEngine : public QRasterPaintEngine {
public:
  using QRasterPaintEngine::QRasterPaintEngine;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10penChangedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx12brushChangedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18brushOriginChangedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx14opacityChangedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx22compositionModeChangedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18renderHintsChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx16transformChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18clipEnabledChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8setStateEP13QPainterState")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx11createStateEP13QPainterState")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperationE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeModeE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4syncEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx19beginNativePaintingEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx17endNativePaintingEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx5flagsEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12createPixmapE5QSize")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[50] = call;
      return true;
    }
    return false;
  }

  //  bool QRasterPaintEngine::begin(QPaintDevice *device)
  bool begin(QPaintDevice *device) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRasterPaintEngineCall0 call = reinterpret_cast<CuteQRasterPaintEngineCall0>(taken[0]);
      bool given = call(this, device, &handled);
      if (handled) return given;
    }
    return QRasterPaintEngine::begin(device);
  }

  //  bool QRasterPaintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRasterPaintEngineCall1 call = reinterpret_cast<CuteQRasterPaintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRasterPaintEngine::end();
  }

  //  void QRasterPaintEngine::penChanged()
  void penChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRasterPaintEngineCall2 call = reinterpret_cast<CuteQRasterPaintEngineCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::penChanged();
  }

  //  void QRasterPaintEngine::brushChanged()
  void brushChanged() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRasterPaintEngineCall3 call = reinterpret_cast<CuteQRasterPaintEngineCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::brushChanged();
  }

  //  void QRasterPaintEngine::brushOriginChanged()
  void brushOriginChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRasterPaintEngineCall4 call = reinterpret_cast<CuteQRasterPaintEngineCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::brushOriginChanged();
  }

  //  void QRasterPaintEngine::opacityChanged()
  void opacityChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQRasterPaintEngineCall5 call = reinterpret_cast<CuteQRasterPaintEngineCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::opacityChanged();
  }

  //  void QRasterPaintEngine::compositionModeChanged()
  void compositionModeChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQRasterPaintEngineCall6 call = reinterpret_cast<CuteQRasterPaintEngineCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::compositionModeChanged();
  }

  //  void QRasterPaintEngine::renderHintsChanged()
  void renderHintsChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQRasterPaintEngineCall7 call = reinterpret_cast<CuteQRasterPaintEngineCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::renderHintsChanged();
  }

  //  void QRasterPaintEngine::transformChanged()
  void transformChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQRasterPaintEngineCall8 call = reinterpret_cast<CuteQRasterPaintEngineCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::transformChanged();
  }

  //  void QRasterPaintEngine::clipEnabledChanged()
  void clipEnabledChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQRasterPaintEngineCall9 call = reinterpret_cast<CuteQRasterPaintEngineCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::clipEnabledChanged();
  }

  //  void QRasterPaintEngine::setState(QPainterState *s)
  void setState(QPainterState *s) override {
    if (taken[10]) {
      int handled = 0;
      CuteQRasterPaintEngineCall10 call = reinterpret_cast<CuteQRasterPaintEngineCall10>(taken[10]);
      call(this, s, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::setState(s);
  }

  //  QPainterState *QRasterPaintEngine::createState(QPainterState *orig)
  //      const
  QPainterState *createState(QPainterState *orig) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRasterPaintEngineCall11 call = reinterpret_cast<CuteQRasterPaintEngineCall11>(taken[11]);
      void * given = call(this, orig, &handled);
      if (handled) return static_cast<QPainterState *>(given);
    }
    return QRasterPaintEngine::createState(orig);
  }

  //  void QRasterPaintEngine::fillPath(const QPainterPath &path, QSpanData
  //      *fillData)
  void fillPath(const QPainterPath &path, QSpanData *fillData) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRasterPaintEngineCall12 call = reinterpret_cast<CuteQRasterPaintEngineCall12>(taken[12]);
      call(this, &path, fillData, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::fillPath(path, fillData);
  }

  //  void QRasterPaintEngine::fillPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void fillPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRasterPaintEngineCall13 call = reinterpret_cast<CuteQRasterPaintEngineCall13>(taken[13]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::fillPolygon(points, pointCount, mode);
  }

  //  void QRasterPaintEngine::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRasterPaintEngineCall14 call = reinterpret_cast<CuteQRasterPaintEngineCall14>(taken[14]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QRasterPaintEngine::drawPolygon(const QPoint *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPoint *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRasterPaintEngineCall15 call = reinterpret_cast<CuteQRasterPaintEngineCall15>(taken[15]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QRasterPaintEngine::drawEllipse(const QRectF &rect)
  void drawEllipse(const QRectF &rect) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRasterPaintEngineCall16 call = reinterpret_cast<CuteQRasterPaintEngineCall16>(taken[16]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawEllipse(rect);
  }

  //  void QRasterPaintEngine::fillRect(const QRectF &rect, const QBrush
  //      &brush)
  void fillRect(const QRectF &rect, const QBrush &brush) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRasterPaintEngineCall17 call = reinterpret_cast<CuteQRasterPaintEngineCall17>(taken[17]);
      call(this, &rect, &brush, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::fillRect(rect, brush);
  }

  //  void QRasterPaintEngine::fillRect(const QRectF &rect, const QColor
  //      &color)
  void fillRect(const QRectF &rect, const QColor &color) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRasterPaintEngineCall18 call = reinterpret_cast<CuteQRasterPaintEngineCall18>(taken[18]);
      call(this, &rect, &color, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::fillRect(rect, color);
  }

  //  void QRasterPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRasterPaintEngineCall19 call = reinterpret_cast<CuteQRasterPaintEngineCall19>(taken[19]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawRects(rects, rectCount);
  }

  //  void QRasterPaintEngine::drawRects(const QRectF *rects, int
  //      rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRasterPaintEngineCall20 call = reinterpret_cast<CuteQRasterPaintEngineCall20>(taken[20]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawRects(rects, rectCount);
  }

  //  void QRasterPaintEngine::drawPixmap(const QPointF &p, const QPixmap
  //      &pm)
  void drawPixmap(const QPointF &p, const QPixmap &pm) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRasterPaintEngineCall21 call = reinterpret_cast<CuteQRasterPaintEngineCall21>(taken[21]);
      call(this, &p, &pm, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPixmap(p, pm);
  }

  //  void QRasterPaintEngine::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRasterPaintEngineCall22 call = reinterpret_cast<CuteQRasterPaintEngineCall22>(taken[22]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPixmap(r, pm, sr);
  }

  //  void QRasterPaintEngine::drawImage(const QPointF &p, const QImage
  //      &img)
  void drawImage(const QPointF &p, const QImage &img) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRasterPaintEngineCall23 call = reinterpret_cast<CuteQRasterPaintEngineCall23>(taken[23]);
      call(this, &p, &img, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawImage(p, img);
  }

  //  void QRasterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
  //      const QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRasterPaintEngineCall24 call = reinterpret_cast<CuteQRasterPaintEngineCall24>(taken[24]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawImage(r, pm, sr, flags);
  }

  //  void QRasterPaintEngine::drawTiledPixmap(const QRectF &r, const
  //      QPixmap &pm, const QPointF &sr)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QPointF &sr) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRasterPaintEngineCall25 call = reinterpret_cast<CuteQRasterPaintEngineCall25>(taken[25]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawTiledPixmap(r, pm, sr);
  }

  //  void QRasterPaintEngine::drawTextItem(const QPointF &p, const
  //      QTextItem &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRasterPaintEngineCall26 call = reinterpret_cast<CuteQRasterPaintEngineCall26>(taken[26]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawTextItem(p, textItem);
  }

  //  void QRasterPaintEngine::drawLines(const QLine *line, int lineCount)
  void drawLines(const QLine *line, int lineCount) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRasterPaintEngineCall27 call = reinterpret_cast<CuteQRasterPaintEngineCall27>(taken[27]);
      call(this, line, lineCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawLines(line, lineCount);
  }

  //  void QRasterPaintEngine::drawLines(const QLineF *line, int lineCount)
  void drawLines(const QLineF *line, int lineCount) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRasterPaintEngineCall28 call = reinterpret_cast<CuteQRasterPaintEngineCall28>(taken[28]);
      call(this, line, lineCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawLines(line, lineCount);
  }

  //  void QRasterPaintEngine::drawPoints(const QPointF *points, int
  //      pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRasterPaintEngineCall29 call = reinterpret_cast<CuteQRasterPaintEngineCall29>(taken[29]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPoints(points, pointCount);
  }

  //  void QRasterPaintEngine::drawPoints(const QPoint *points, int
  //      pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRasterPaintEngineCall30 call = reinterpret_cast<CuteQRasterPaintEngineCall30>(taken[30]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawPoints(points, pointCount);
  }

  //  void QRasterPaintEngine::clip(const QRect &rect, Qt::ClipOperation
  //      op)
  void clip(const QRect &rect, Qt::ClipOperation op) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRasterPaintEngineCall31 call = reinterpret_cast<CuteQRasterPaintEngineCall31>(taken[31]);
      call(this, &rect, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::clip(rect, op);
  }

  //  void QRasterPaintEngine::clip(const QRegion &region,
  //      Qt::ClipOperation op)
  void clip(const QRegion &region, Qt::ClipOperation op) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRasterPaintEngineCall32 call = reinterpret_cast<CuteQRasterPaintEngineCall32>(taken[32]);
      call(this, &region, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::clip(region, op);
  }

  //  void QRasterPaintEngine::drawStaticTextItem(QStaticTextItem
  //      *textItem)
  void drawStaticTextItem(QStaticTextItem *textItem) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRasterPaintEngineCall33 call = reinterpret_cast<CuteQRasterPaintEngineCall33>(taken[33]);
      call(this, textItem, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawStaticTextItem(textItem);
  }

  //  bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, const
  //      glyph_t *glyphs, const QFixedPoint *positions, QFontEngine
  //      *fontEngine)
  bool drawCachedGlyphs(
      int numGlyphs,
      const glyph_t *glyphs,
      const QFixedPoint *positions,
      QFontEngine *fontEngine) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRasterPaintEngineCall34 call = reinterpret_cast<CuteQRasterPaintEngineCall34>(taken[34]);
      bool given = call(this, numGlyphs, glyphs, positions, fontEngine, &handled);
      if (handled) return given;
    }
    return QRasterPaintEngine::drawCachedGlyphs(numGlyphs, glyphs, positions, fontEngine);
  }

  //  Type QRasterPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQRasterPaintEngineCall35 call = reinterpret_cast<CuteQRasterPaintEngineCall35>(taken[35]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QRasterPaintEngine::type();
  }

  //  QPoint QRasterPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQRasterPaintEngineCall36 call = reinterpret_cast<CuteQRasterPaintEngineCall36>(taken[36]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRasterPaintEngine::coordinateOffset();
  }

  //  bool
  //      QRasterPaintEngine::requiresPretransformedGlyphPositions(QFontEng
  //      ine *fontEngine, const QTransform &m) const
  bool requiresPretransformedGlyphPositions(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQRasterPaintEngineCall37 call = reinterpret_cast<CuteQRasterPaintEngineCall37>(taken[37]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QRasterPaintEngine::requiresPretransformedGlyphPositions(fontEngine, m);
  }

  //  bool QRasterPaintEngine::shouldDrawCachedGlyphs(QFontEngine
  //      *fontEngine, const QTransform &m) const
  bool shouldDrawCachedGlyphs(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQRasterPaintEngineCall38 call = reinterpret_cast<CuteQRasterPaintEngineCall38>(taken[38]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QRasterPaintEngine::shouldDrawCachedGlyphs(fontEngine, m);
  }

  //  void QPaintEngineEx::clip(const QPainterPath &path, Qt::ClipOperation
  //      op)
  void clip(const QPainterPath &path, Qt::ClipOperation op) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRasterPaintEngineCall39 call = reinterpret_cast<CuteQRasterPaintEngineCall39>(taken[39]);
      call(this, &path, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QPaintEngineEx::clip(path, op);
  }

  //  void QPaintEngineEx::drawRoundedRect(const QRectF &rect, qreal xrad,
  //      qreal yrad, Qt::SizeMode mode)
  void drawRoundedRect(
      const QRectF &rect,
      qreal xrad,
      qreal yrad,
      Qt::SizeMode mode) override {
    if (taken[40]) {
      int handled = 0;
      CuteQRasterPaintEngineCall40 call = reinterpret_cast<CuteQRasterPaintEngineCall40>(taken[40]);
      call(this, &rect, xrad, yrad, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRoundedRect(rect, xrad, yrad, mode);
  }

  //  void QPaintEngineEx::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[41]) {
      int handled = 0;
      CuteQRasterPaintEngineCall41 call = reinterpret_cast<CuteQRasterPaintEngineCall41>(taken[41]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[42]) {
      int handled = 0;
      CuteQRasterPaintEngineCall42 call = reinterpret_cast<CuteQRasterPaintEngineCall42>(taken[42]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPath(path);
  }

  //  void QPaintEngineEx::drawPixmapFragments(const
  //      QPainter::PixmapFragment *fragments, int fragmentCount, const
  //      QPixmap &pixmap, QFlags<QPainter::PixmapFragmentHint> hints)
  void drawPixmapFragments(
      const QPainter::PixmapFragment *fragments,
      int fragmentCount,
      const QPixmap &pixmap,
      QFlags<QPainter::PixmapFragmentHint> hints) override {
    if (taken[43]) {
      int handled = 0;
      CuteQRasterPaintEngineCall43 call = reinterpret_cast<CuteQRasterPaintEngineCall43>(taken[43]);
      call(this, fragments, fragmentCount, &pixmap, static_cast<int>(hints.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPixmapFragments(fragments, fragmentCount, pixmap, hints);
  }

  //  void QPaintEngineEx::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[44]) {
      int handled = 0;
      CuteQRasterPaintEngineCall44 call = reinterpret_cast<CuteQRasterPaintEngineCall44>(taken[44]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPaintEngineEx::updateState(state);
  }

  //  void QPaintEngineEx::sync()
  void sync() override {
    if (taken[45]) {
      int handled = 0;
      CuteQRasterPaintEngineCall45 call = reinterpret_cast<CuteQRasterPaintEngineCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::sync();
  }

  //  void QPaintEngineEx::beginNativePainting()
  void beginNativePainting() override {
    if (taken[46]) {
      int handled = 0;
      CuteQRasterPaintEngineCall46 call = reinterpret_cast<CuteQRasterPaintEngineCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::beginNativePainting();
  }

  //  void QPaintEngineEx::endNativePainting()
  void endNativePainting() override {
    if (taken[47]) {
      int handled = 0;
      CuteQRasterPaintEngineCall47 call = reinterpret_cast<CuteQRasterPaintEngineCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::endNativePainting();
  }

  //  uint QPaintEngineEx::flags() const
  uint flags() const override {
    if (taken[48]) {
      int handled = 0;
      CuteQRasterPaintEngineCall48 call = reinterpret_cast<CuteQRasterPaintEngineCall48>(taken[48]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::flags();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[49]) {
      int handled = 0;
      CuteQRasterPaintEngineCall49 call = reinterpret_cast<CuteQRasterPaintEngineCall49>(taken[49]);
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
    if (taken[50]) {
      int handled = 0;
      CuteQRasterPaintEngineCall50 call = reinterpret_cast<CuteQRasterPaintEngineCall50>(taken[50]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QRasterPaintEnginePrivate *QRasterPaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QRasterPaintEnginePrivate *ritual_ZN18QRasterPaintEngine6d_funcEv(
    QRasterPaintEngine *self) {
  return self->d_func();
}

//  const QRasterPaintEnginePrivate *QRasterPaintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QRasterPaintEnginePrivate *ritual_ZNK18QRasterPaintEngine6d_funcEv(
    const QRasterPaintEngine *self) {
  return self->d_func();
}

//  QRasterPaintEngine::QRasterPaintEngine(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
QRasterPaintEngine *ritual_ZN18QRasterPaintEngineC1EP12QPaintDevice(
    QPaintDevice *device) {
  return new CuteQRasterPaintEngine(device);
}

//  QRasterPaintEngine::~QRasterPaintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngineD1Ev(QRasterPaintEngine *self) {
  delete self;
}

//  bool QRasterPaintEngine::begin(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRasterPaintEngine5beginEP12QPaintDevice(
    QRasterPaintEngine *self,
    QPaintDevice *device) {
  return self->begin(device);
}

//  bool QRasterPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRasterPaintEngine3endEv(QRasterPaintEngine *self) {
  return self->end();
}

//  void QRasterPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10penChangedEv(QRasterPaintEngine *self) {
  self->penChanged();
}

//  void QRasterPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine12brushChangedEv(
    QRasterPaintEngine *self) {
  self->brushChanged();
}

//  void QRasterPaintEngine::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine18brushOriginChangedEv(
    QRasterPaintEngine *self) {
  self->brushOriginChanged();
}

//  void QRasterPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine14opacityChangedEv(
    QRasterPaintEngine *self) {
  self->opacityChanged();
}

//  void QRasterPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine22compositionModeChangedEv(
    QRasterPaintEngine *self) {
  self->compositionModeChanged();
}

//  void QRasterPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine18renderHintsChangedEv(
    QRasterPaintEngine *self) {
  self->renderHintsChanged();
}

//  void QRasterPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine16transformChangedEv(
    QRasterPaintEngine *self) {
  self->transformChanged();
}

//  void QRasterPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine18clipEnabledChangedEv(
    QRasterPaintEngine *self) {
  self->clipEnabledChanged();
}

//  void QRasterPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine8setStateEP13QPainterState(
    QRasterPaintEngine *self,
    QPainterState *s) {
  self->setState(s);
}

//  QPainterState *QRasterPaintEngine::createState(QPainterState *orig) const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZNK18QRasterPaintEngine11createStateEP13QPainterState(
    const QRasterPaintEngine *self,
    QPainterState *orig) {
  return self->createState(orig);
}

//  QRasterPaintEngineState *QRasterPaintEngine::state()
extern "C" Q_DECL_EXPORT
QRasterPaintEngineState *ritual_ZN18QRasterPaintEngine5stateEv(
    QRasterPaintEngine *self) {
  return self->state();
}

//  const QRasterPaintEngineState *QRasterPaintEngine::state() const
extern "C" Q_DECL_EXPORT
const QRasterPaintEngineState *ritual_ZNK18QRasterPaintEngine5stateEv(
    const QRasterPaintEngine *self) {
  return self->state();
}

//  void QRasterPaintEngine::updateBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11updateBrushERK6QBrush(
    QRasterPaintEngine *self,
    const QBrush *brush) {
  self->updateBrush(*brush);
}

//  void QRasterPaintEngine::updatePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9updatePenERK4QPen(
    QRasterPaintEngine *self,
    const QPen *pen) {
  self->updatePen(*pen);
}

//  void QRasterPaintEngine::updateMatrix(const QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine12updateMatrixERK10QTransform(
    QRasterPaintEngine *self,
    const QTransform *matrix) {
  self->updateMatrix(*matrix);
}

//  void QRasterPaintEngine::fillPath(const QPainterPath &path, QSpanData
//      *fillData)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData(
    QRasterPaintEngine *self,
    const QPainterPath *path,
    QSpanData *fillData) {
  self->fillPath(*path, fillData);
}

//  void QRasterPaintEngine::fillPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->fillPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawPolygon(const QPoint *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11drawEllipseERK6QRectF(
    QRasterPaintEngine *self,
    const QRectF *rect) {
  self->drawEllipse(*rect);
}

//  void QRasterPaintEngine::fillRect(const QRectF &rect, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QBrush(
    QRasterPaintEngine *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->fillRect(*rect, *brush);
}

//  void QRasterPaintEngine::fillRect(const QRectF &rect, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QColor(
    QRasterPaintEngine *self,
    const QRectF *rect,
    const QColor *color) {
  self->fillRect(*rect, *color);
}

//  void QRasterPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawRectsEPK5QRecti(
    QRasterPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QRasterPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawRectsEPK6QRectFi(
    QRasterPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QRasterPaintEngine::drawPixmap(const QPointF &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10drawPixmapERK7QPointFRK7QPixmap(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QPixmap *pm) {
  self->drawPixmap(*p, *pm);
}

//  void QRasterPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QRasterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QRasterPaintEngine::drawImage(const QPointF &p, const QImage &img)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawImageERK7QPointFRK6QImage(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QImage *img) {
  self->drawImage(*p, *img);
}

//  void QRasterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPaintEngine *self,
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

//  void QRasterPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QRasterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *sr) {
  self->drawTiledPixmap(*r, *pm, *sr);
}

//  void QRasterPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QRasterPaintEngine::drawLines(const QLine *line, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawLinesEPK5QLinei(
    QRasterPaintEngine *self,
    const QLine *line,
    int lineCount) {
  self->drawLines(line, lineCount);
}

//  void QRasterPaintEngine::drawLines(const QLineF *line, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9drawLinesEPK6QLineFi(
    QRasterPaintEngine *self,
    const QLineF *line,
    int lineCount) {
  self->drawLines(line, lineCount);
}

//  void QRasterPaintEngine::drawPoints(const QPointF *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10drawPointsEPK7QPointFi(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QRasterPaintEngine::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10drawPointsEPK6QPointi(
    QRasterPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QRasterPaintEngine::stroke(const QVectorPath &path, const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine6strokeERK11QVectorPathRK4QPen(
    QRasterPaintEngine *self,
    const QVectorPath *path,
    const QPen *pen) {
  self->stroke(*path, *pen);
}

//  void QRasterPaintEngine::fill(const QVectorPath &path, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine4fillERK11QVectorPathRK6QBrush(
    QRasterPaintEngine *self,
    const QVectorPath *path,
    const QBrush *brush) {
  self->fill(*path, *brush);
}

//  void QRasterPaintEngine::clip(const QVectorPath &path, Qt::ClipOperation
//      op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine4clipERK11QVectorPathN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QVectorPath *path,
    Qt::ClipOperation op) {
  self->clip(*path, op);
}

//  void QRasterPaintEngine::clip(const QRect &rect, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine4clipERK5QRectN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QRect *rect,
    Qt::ClipOperation op) {
  self->clip(*rect, op);
}

//  void QRasterPaintEngine::clip(const QRegion &region, Qt::ClipOperation
//      op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine4clipERK7QRegionN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QRegion *region,
    Qt::ClipOperation op) {
  self->clip(*region, op);
}

//  const QClipData *QRasterPaintEngine::clipData() const
extern "C" Q_DECL_EXPORT
const QClipData *ritual_ZNK18QRasterPaintEngine8clipDataEv(
    const QRasterPaintEngine *self) {
  return self->clipData();
}

//  void QRasterPaintEngine::drawStaticTextItem(QStaticTextItem *textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QRasterPaintEngine *self,
    QStaticTextItem *textItem) {
  self->drawStaticTextItem(textItem);
}

//  bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRasterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine(
    QRasterPaintEngine *self,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->drawCachedGlyphs(numGlyphs, glyphs, positions, fontEngine);
}

//  ClipType QRasterPaintEngine::clipType() const
extern "C" Q_DECL_EXPORT
QRasterPaintEngine::ClipType ritual_ZNK18QRasterPaintEngine8clipTypeEv(
    const QRasterPaintEngine *self) {
  return self->clipType();
}

//  QRectF QRasterPaintEngine::clipBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QRasterPaintEngine16clipBoundingRectEv(
    const QRasterPaintEngine *self) {
  return new QRectF(self->clipBoundingRect());
}

//  QRasterBuffer *QRasterPaintEngine::rasterBuffer()
extern "C" Q_DECL_EXPORT
QRasterBuffer *ritual_ZN18QRasterPaintEngine12rasterBufferEv(
    QRasterPaintEngine *self) {
  return self->rasterBuffer();
}

//  void QRasterPaintEngine::alphaPenBlt(const void *src, int bpl, int depth,
//      int rx, int ry, int w, int h, bool useGammaCorrection)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11alphaPenBltEPKviiiiiib(
    QRasterPaintEngine *self,
    const void *src,
    int bpl,
    int depth,
    int rx,
    int ry,
    int w,
    int h,
    bool useGammaCorrection) {
  self->alphaPenBlt(src, bpl, depth, rx, ry, w, h, useGammaCorrection);
}

//  Type QRasterPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK18QRasterPaintEngine4typeEv(
    const QRasterPaintEngine *self) {
  return self->type();
}

//  QPoint QRasterPaintEngine::coordinateOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18QRasterPaintEngine16coordinateOffsetEv(
    const QRasterPaintEngine *self) {
  return new QPoint(self->coordinateOffset());
}

//  bool QRasterPaintEngine::requiresPretransformedGlyphPositions(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRasterPaintEngine36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QRasterPaintEngine *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->requiresPretransformedGlyphPositions(fontEngine, *m);
}

//  bool QRasterPaintEngine::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
//      const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRasterPaintEngine22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QRasterPaintEngine *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->shouldDrawCachedGlyphs(fontEngine, *m);
}

//  QRasterPaintEngine::QRasterPaintEngine(QRasterPaintEnginePrivate &d,
//      QPaintDevice *a1)
extern "C" Q_DECL_EXPORT
QRasterPaintEngine *ritual_ZN18QRasterPaintEngineC1ER25QRasterPaintEnginePrivateP12QPaintDevice(
    QRasterPaintEnginePrivate *d,
    QPaintDevice *a1) {
  return new CuteQRasterPaintEngine(*d, a1);
}

//  void QRasterPaintEngine::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine4initEv(QRasterPaintEngine *self) {
  self->init();
}

//  void QRasterPaintEngine::fillRect(const QRectF &rect, QSpanData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine8fillRectERK6QRectFP9QSpanData(
    QRasterPaintEngine *self,
    const QRectF *rect,
    QSpanData *data) {
  self->fillRect(*rect, data);
}

//  void QRasterPaintEngine::drawBitmap(const QPointF &pos, const QImage
//      &image, QSpanData *fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine10drawBitmapERK7QPointFRK6QImageP9QSpanData(
    QRasterPaintEngine *self,
    const QPointF *pos,
    const QImage *image,
    QSpanData *fill) {
  self->drawBitmap(*pos, *image, fill);
}

//  bool QRasterPaintEngine::setClipRectInDeviceCoords(const QRect &r,
//      Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRasterPaintEngine25setClipRectInDeviceCoordsERK5QRectN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QRect *r,
    Qt::ClipOperation op) {
  return self->setClipRectInDeviceCoords(*r, op);
}

//  QRect QRasterPaintEngine::toNormalizedFillRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN18QRasterPaintEngine20toNormalizedFillRectERK6QRectF(
    QRasterPaintEngine *self,
    const QRectF *rect) {
  return new QRect(self->toNormalizedFillRect(*rect));
}

//  void QRasterPaintEngine::ensureBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11ensureBrushERK6QBrush(
    QRasterPaintEngine *self,
    const QBrush *brush) {
  self->ensureBrush(*brush);
}

//  void QRasterPaintEngine::ensureBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine11ensureBrushEv(QRasterPaintEngine *self) {
  self->ensureBrush();
}

//  void QRasterPaintEngine::ensurePen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9ensurePenERK4QPen(
    QRasterPaintEngine *self,
    const QPen *pen) {
  self->ensurePen(*pen);
}

//  void QRasterPaintEngine::ensurePen()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine9ensurePenEv(QRasterPaintEngine *self) {
  self->ensurePen();
}

//  void QRasterPaintEngine::updateOutlineMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine19updateOutlineMapperEv(
    QRasterPaintEngine *self) {
  self->updateOutlineMapper();
}

//  void QRasterPaintEngine::ensureOutlineMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine19ensureOutlineMapperEv(
    QRasterPaintEngine *self) {
  self->ensureOutlineMapper();
}

//  void QRasterPaintEngine::updateRasterState()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine17updateRasterStateEv(
    QRasterPaintEngine *self) {
  self->updateRasterState();
}

//  void QRasterPaintEngine::ensureRasterState()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRasterPaintEngine17ensureRasterStateEv(
    QRasterPaintEngine *self) {
  self->ensureRasterState();
}

//  a Python function taken by a CuteQRasterPaintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRasterPaintEngine(
    QRasterPaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRasterPaintEngine *>(self)->take(key, call);
}

//  bool QRasterPaintEngine::begin(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QRasterPaintEngine5beginEP12QPaintDevice(
    QRasterPaintEngine *self,
    QPaintDevice *device) {
  return self->QRasterPaintEngine::begin(device);
}

//  bool QRasterPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QRasterPaintEngine3endEv(QRasterPaintEngine *self) {
  return self->QRasterPaintEngine::end();
}

//  void QRasterPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine10penChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::penChanged();
}

//  void QRasterPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine12brushChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::brushChanged();
}

//  void QRasterPaintEngine::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine18brushOriginChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::brushOriginChanged();
}

//  void QRasterPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine14opacityChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::opacityChanged();
}

//  void QRasterPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine22compositionModeChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::compositionModeChanged();
}

//  void QRasterPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine18renderHintsChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::renderHintsChanged();
}

//  void QRasterPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine16transformChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::transformChanged();
}

//  void QRasterPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine18clipEnabledChangedEv(
    QRasterPaintEngine *self) {
  self->QRasterPaintEngine::clipEnabledChanged();
}

//  void QRasterPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine8setStateEP13QPainterState(
    QRasterPaintEngine *self,
    QPainterState *s) {
  self->QRasterPaintEngine::setState(s);
}

//  QPainterState *QRasterPaintEngine::createState(QPainterState *orig) const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_own_ZNK18QRasterPaintEngine11createStateEP13QPainterState(
    const QRasterPaintEngine *self,
    QPainterState *orig) {
  return self->QRasterPaintEngine::createState(orig);
}

//  void QRasterPaintEngine::fillPath(const QPainterPath &path, QSpanData
//      *fillData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData(
    QRasterPaintEngine *self,
    const QPainterPath *path,
    QSpanData *fillData) {
  self->QRasterPaintEngine::fillPath(*path, fillData);
}

//  void QRasterPaintEngine::fillPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QRasterPaintEngine::fillPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QRasterPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawPolygon(const QPoint *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QRasterPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QRasterPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QRasterPaintEngine::drawEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine11drawEllipseERK6QRectF(
    QRasterPaintEngine *self,
    const QRectF *rect) {
  self->QRasterPaintEngine::drawEllipse(*rect);
}

//  void QRasterPaintEngine::fillRect(const QRectF &rect, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QBrush(
    QRasterPaintEngine *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->QRasterPaintEngine::fillRect(*rect, *brush);
}

//  void QRasterPaintEngine::fillRect(const QRectF &rect, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine8fillRectERK6QRectFRK6QColor(
    QRasterPaintEngine *self,
    const QRectF *rect,
    const QColor *color) {
  self->QRasterPaintEngine::fillRect(*rect, *color);
}

//  void QRasterPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawRectsEPK5QRecti(
    QRasterPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->QRasterPaintEngine::drawRects(rects, rectCount);
}

//  void QRasterPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawRectsEPK6QRectFi(
    QRasterPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->QRasterPaintEngine::drawRects(rects, rectCount);
}

//  void QRasterPaintEngine::drawPixmap(const QPointF &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine10drawPixmapERK7QPointFRK7QPixmap(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QPixmap *pm) {
  self->QRasterPaintEngine::drawPixmap(*p, *pm);
}

//  void QRasterPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QRasterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QRasterPaintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QRasterPaintEngine::drawImage(const QPointF &p, const QImage &img)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawImageERK7QPointFRK6QImage(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QImage *img) {
  self->QRasterPaintEngine::drawImage(*p, *img);
}

//  void QRasterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QRasterPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->QRasterPaintEngine::drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QRasterPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QRasterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *sr) {
  self->QRasterPaintEngine::drawTiledPixmap(*r, *pm, *sr);
}

//  void QRasterPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QRasterPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QRasterPaintEngine::drawTextItem(*p, *textItem);
}

//  void QRasterPaintEngine::drawLines(const QLine *line, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawLinesEPK5QLinei(
    QRasterPaintEngine *self,
    const QLine *line,
    int lineCount) {
  self->QRasterPaintEngine::drawLines(line, lineCount);
}

//  void QRasterPaintEngine::drawLines(const QLineF *line, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine9drawLinesEPK6QLineFi(
    QRasterPaintEngine *self,
    const QLineF *line,
    int lineCount) {
  self->QRasterPaintEngine::drawLines(line, lineCount);
}

//  void QRasterPaintEngine::drawPoints(const QPointF *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine10drawPointsEPK7QPointFi(
    QRasterPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->QRasterPaintEngine::drawPoints(points, pointCount);
}

//  void QRasterPaintEngine::drawPoints(const QPoint *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine10drawPointsEPK6QPointi(
    QRasterPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->QRasterPaintEngine::drawPoints(points, pointCount);
}

//  void QRasterPaintEngine::clip(const QRect &rect, Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine4clipERK5QRectN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QRect *rect,
    Qt::ClipOperation op) {
  self->QRasterPaintEngine::clip(*rect, op);
}

//  void QRasterPaintEngine::clip(const QRegion &region, Qt::ClipOperation
//      op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine4clipERK7QRegionN2Qt13ClipOperationE(
    QRasterPaintEngine *self,
    const QRegion *region,
    Qt::ClipOperation op) {
  self->QRasterPaintEngine::clip(*region, op);
}

//  void QRasterPaintEngine::drawStaticTextItem(QStaticTextItem *textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QRasterPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QRasterPaintEngine *self,
    QStaticTextItem *textItem) {
  self->QRasterPaintEngine::drawStaticTextItem(textItem);
}

//  bool QRasterPaintEngine::drawCachedGlyphs(int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QRasterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine(
    QRasterPaintEngine *self,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->QRasterPaintEngine::drawCachedGlyphs(
      numGlyphs,
      glyphs,
      positions,
      fontEngine);
}

//  Type QRasterPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK18QRasterPaintEngine4typeEv(
    const QRasterPaintEngine *self) {
  return self->QRasterPaintEngine::type();
}

//  QPoint QRasterPaintEngine::coordinateOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK18QRasterPaintEngine16coordinateOffsetEv(
    const QRasterPaintEngine *self) {
  return new QPoint(self->QRasterPaintEngine::coordinateOffset());
}

//  bool QRasterPaintEngine::requiresPretransformedGlyphPositions(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QRasterPaintEngine36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QRasterPaintEngine *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->QRasterPaintEngine::requiresPretransformedGlyphPositions(
      fontEngine,
      *m);
}

//  bool QRasterPaintEngine::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
//      const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QRasterPaintEngine22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QRasterPaintEngine *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->QRasterPaintEngine::shouldDrawCachedGlyphs(fontEngine, *m);
}
