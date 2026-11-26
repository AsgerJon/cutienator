//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_blitter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_BLITTABLE)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_blitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qpen.h>
#include <QtGui/qregion.h>
#include <QtGui/qtransform.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QBlitterPaintEngine that Python can take functions over in. Every QBlitterPaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_BLITTABLE)
typedef int (*CuteQBlitterPaintEngineCall0)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef bool (*CuteQBlitterPaintEngineCall1)(const void *, QPaintDevice *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef bool (*CuteQBlitterPaintEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall3)(const void *, const QRectF *, const QBrush *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall4)(const void *, const QRectF *, const QColor *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall5)(const void *, const QRect *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall6)(const void *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall7)(const void *, const QPointF *, const QPixmap *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall8)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall9)(const void *, QPainterState *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall10)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall11)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall12)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall13)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall14)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall15)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall16)(const void *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall17)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall18)(const void *, const QPoint *, int, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall19)(const void *, const QPainterPath *, QSpanData *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall20)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall21)(const void *, const QRectF *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall22)(const void *, const QPointF *, const QImage *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall23)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall24)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall25)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall26)(const void *, const QPointF *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall27)(const void *, const QPoint *, int, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall28)(const void *, QStaticTextItem *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
typedef bool (*CuteQBlitterPaintEngineCall29)(const void *, int, const glyph_t *, const QFixedPoint *, QFontEngine *, int *);
#endif  // !defined(QT_NO_BLITTABLE)
typedef void (*CuteQBlitterPaintEngineCall30)(const void *, int *);
typedef void * (*CuteQBlitterPaintEngineCall31)(const void *, QPainterState *, int *);
typedef void (*CuteQBlitterPaintEngineCall32)(const void *, const QLine *, int, int *);
typedef void (*CuteQBlitterPaintEngineCall33)(const void *, const QLineF *, int, int *);
typedef void (*CuteQBlitterPaintEngineCall34)(const void *, const QRect *, int, int *);
typedef void (*CuteQBlitterPaintEngineCall35)(const void *, const QRegion *, int, int *);
typedef const QPoint * (*CuteQBlitterPaintEngineCall36)(const void *, int *);
typedef bool (*CuteQBlitterPaintEngineCall37)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQBlitterPaintEngineCall38)(const void *, QFontEngine *, const QTransform *, int *);
typedef void (*CuteQBlitterPaintEngineCall39)(const void *, const QPainterPath *, int, int *);
typedef void (*CuteQBlitterPaintEngineCall40)(const void *, const QRectF *, qreal, qreal, int, int *);
typedef void (*CuteQBlitterPaintEngineCall41)(const void *, const QRect *, int *);
typedef void (*CuteQBlitterPaintEngineCall42)(const void *, const QPainterPath *, int *);
typedef void (*CuteQBlitterPaintEngineCall43)(const void *, const QPainter::PixmapFragment *, int, const QPixmap *, int, int *);
typedef void (*CuteQBlitterPaintEngineCall44)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQBlitterPaintEngineCall45)(const void *, int *);
typedef void (*CuteQBlitterPaintEngineCall46)(const void *, int *);
typedef void (*CuteQBlitterPaintEngineCall47)(const void *, int *);
typedef uint (*CuteQBlitterPaintEngineCall48)(const void *, int *);
typedef const QPixmap * (*CuteQBlitterPaintEngineCall49)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQBlitterPaintEngineCall50)(const void *, const QImage *, int, int *);
class CuteQBlitterPaintEngine : public QBlitterPaintEngine {
public:
  using QBlitterPaintEngine::QBlitterPaintEngine;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx8setStateEP13QPainterState")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18clipEnabledChangedEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx10penChangedEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx12brushChangedEv")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx14opacityChangedEv")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx22compositionModeChangedEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18renderHintsChangedEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx16transformChangedEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine8fillPathERK12QPainterPathP9QSpanData")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
#if !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN18QRasterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_BLITTABLE)
    if (!std::strcmp(key, "_ZN14QPaintEngineEx18brushOriginChangedEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPaintEngineEx11createStateEP13QPainterState")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE")) {
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

#if !defined(QT_NO_BLITTABLE)
  //  QPaintEngine::Type QBlitterPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall0 call = reinterpret_cast<CuteQBlitterPaintEngineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QBlitterPaintEngine::type();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  bool QBlitterPaintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall1 call = reinterpret_cast<CuteQBlitterPaintEngineCall1>(taken[1]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QBlitterPaintEngine::begin(pdev);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  bool QBlitterPaintEngine::end()
  bool end() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall2 call = reinterpret_cast<CuteQBlitterPaintEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBlitterPaintEngine::end();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QBrush
  //      &brush)
  void fillRect(const QRectF &rect, const QBrush &brush) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall3 call = reinterpret_cast<CuteQBlitterPaintEngineCall3>(taken[3]);
      call(this, &rect, &brush, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::fillRect(rect, brush);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QColor
  //      &color)
  void fillRect(const QRectF &rect, const QColor &color) override {
    if (taken[4]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall4 call = reinterpret_cast<CuteQBlitterPaintEngineCall4>(taken[4]);
      call(this, &rect, &color, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::fillRect(rect, color);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawRects(const QRect *rects, int
  //      rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[5]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall5 call = reinterpret_cast<CuteQBlitterPaintEngineCall5>(taken[5]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawRects(rects, rectCount);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawRects(const QRectF *rects, int
  //      rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[6]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall6 call = reinterpret_cast<CuteQBlitterPaintEngineCall6>(taken[6]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawRects(rects, rectCount);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPixmap(const QPointF &p, const QPixmap
  //      &pm)
  void drawPixmap(const QPointF &p, const QPixmap &pm) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall7 call = reinterpret_cast<CuteQBlitterPaintEngineCall7>(taken[7]);
      call(this, &p, &pm, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPixmap(p, pm);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[8]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall8 call = reinterpret_cast<CuteQBlitterPaintEngineCall8>(taken[8]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPixmap(r, pm, sr);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::setState(QPainterState *s)
  void setState(QPainterState *s) override {
    if (taken[9]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall9 call = reinterpret_cast<CuteQBlitterPaintEngineCall9>(taken[9]);
      call(this, s, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::setState(s);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::clipEnabledChanged()
  void clipEnabledChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall10 call = reinterpret_cast<CuteQBlitterPaintEngineCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::clipEnabledChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::penChanged()
  void penChanged() override {
    if (taken[11]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall11 call = reinterpret_cast<CuteQBlitterPaintEngineCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::penChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::brushChanged()
  void brushChanged() override {
    if (taken[12]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall12 call = reinterpret_cast<CuteQBlitterPaintEngineCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::brushChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::opacityChanged()
  void opacityChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall13 call = reinterpret_cast<CuteQBlitterPaintEngineCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::opacityChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::compositionModeChanged()
  void compositionModeChanged() override {
    if (taken[14]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall14 call = reinterpret_cast<CuteQBlitterPaintEngineCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::compositionModeChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::renderHintsChanged()
  void renderHintsChanged() override {
    if (taken[15]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall15 call = reinterpret_cast<CuteQBlitterPaintEngineCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::renderHintsChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::transformChanged()
  void transformChanged() override {
    if (taken[16]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall16 call = reinterpret_cast<CuteQBlitterPaintEngineCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::transformChanged();
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[17]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall17 call = reinterpret_cast<CuteQBlitterPaintEngineCall17>(taken[17]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPolygon(const QPoint *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPoint *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[18]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall18 call = reinterpret_cast<CuteQBlitterPaintEngineCall18>(taken[18]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::fillPath(const QPainterPath &path,
  //      QSpanData *fillData)
  void fillPath(const QPainterPath &path, QSpanData *fillData) override {
    if (taken[19]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall19 call = reinterpret_cast<CuteQBlitterPaintEngineCall19>(taken[19]);
      call(this, &path, fillData, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::fillPath(path, fillData);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::fillPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void fillPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[20]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall20 call = reinterpret_cast<CuteQBlitterPaintEngineCall20>(taken[20]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::fillPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawEllipse(const QRectF &rect)
  void drawEllipse(const QRectF &rect) override {
    if (taken[21]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall21 call = reinterpret_cast<CuteQBlitterPaintEngineCall21>(taken[21]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawEllipse(rect);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawImage(const QPointF &p, const QImage
  //      &img)
  void drawImage(const QPointF &p, const QImage &img) override {
    if (taken[22]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall22 call = reinterpret_cast<CuteQBlitterPaintEngineCall22>(taken[22]);
      call(this, &p, &img, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawImage(p, img);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawImage(const QRectF &r, const QImage
  //      &pm, const QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[23]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall23 call = reinterpret_cast<CuteQBlitterPaintEngineCall23>(taken[23]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawImage(r, pm, sr, flags);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawTiledPixmap(const QRectF &r, const
  //      QPixmap &pm, const QPointF &sr)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QPointF &sr) override {
    if (taken[24]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall24 call = reinterpret_cast<CuteQBlitterPaintEngineCall24>(taken[24]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawTiledPixmap(r, pm, sr);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawTextItem(const QPointF &p, const
  //      QTextItem &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[25]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall25 call = reinterpret_cast<CuteQBlitterPaintEngineCall25>(taken[25]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawTextItem(p, textItem);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPoints(const QPointF *points, int
  //      pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[26]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall26 call = reinterpret_cast<CuteQBlitterPaintEngineCall26>(taken[26]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPoints(points, pointCount);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawPoints(const QPoint *points, int
  //      pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[27]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall27 call = reinterpret_cast<CuteQBlitterPaintEngineCall27>(taken[27]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawPoints(points, pointCount);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  void QBlitterPaintEngine::drawStaticTextItem(QStaticTextItem *a0)
  void drawStaticTextItem(QStaticTextItem *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall28 call = reinterpret_cast<CuteQBlitterPaintEngineCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QBlitterPaintEngine::drawStaticTextItem(a0);
  }
#endif  // !defined(QT_NO_BLITTABLE)

#if !defined(QT_NO_BLITTABLE)
  //  bool QBlitterPaintEngine::drawCachedGlyphs(int numGlyphs, const
  //      glyph_t *glyphs, const QFixedPoint *positions, QFontEngine
  //      *fontEngine)
  bool drawCachedGlyphs(
      int numGlyphs,
      const glyph_t *glyphs,
      const QFixedPoint *positions,
      QFontEngine *fontEngine) override {
    if (taken[29]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall29 call = reinterpret_cast<CuteQBlitterPaintEngineCall29>(taken[29]);
      bool given = call(this, numGlyphs, glyphs, positions, fontEngine, &handled);
      if (handled) return given;
    }
    return QBlitterPaintEngine::drawCachedGlyphs(numGlyphs, glyphs, positions, fontEngine);
  }
#endif  // !defined(QT_NO_BLITTABLE)

  //  void QRasterPaintEngine::brushOriginChanged()
  void brushOriginChanged() override {
    if (taken[30]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall30 call = reinterpret_cast<CuteQBlitterPaintEngineCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::brushOriginChanged();
  }

  //  QPainterState *QRasterPaintEngine::createState(QPainterState *orig)
  //      const
  QPainterState *createState(QPainterState *orig) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall31 call = reinterpret_cast<CuteQBlitterPaintEngineCall31>(taken[31]);
      void * given = call(this, orig, &handled);
      if (handled) return static_cast<QPainterState *>(given);
    }
    return QRasterPaintEngine::createState(orig);
  }

  //  void QRasterPaintEngine::drawLines(const QLine *line, int lineCount)
  void drawLines(const QLine *line, int lineCount) override {
    if (taken[32]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall32 call = reinterpret_cast<CuteQBlitterPaintEngineCall32>(taken[32]);
      call(this, line, lineCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawLines(line, lineCount);
  }

  //  void QRasterPaintEngine::drawLines(const QLineF *line, int lineCount)
  void drawLines(const QLineF *line, int lineCount) override {
    if (taken[33]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall33 call = reinterpret_cast<CuteQBlitterPaintEngineCall33>(taken[33]);
      call(this, line, lineCount, &handled);
      if (handled) return;
    }
    QRasterPaintEngine::drawLines(line, lineCount);
  }

  //  void QRasterPaintEngine::clip(const QRect &rect, Qt::ClipOperation
  //      op)
  void clip(const QRect &rect, Qt::ClipOperation op) override {
    if (taken[34]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall34 call = reinterpret_cast<CuteQBlitterPaintEngineCall34>(taken[34]);
      call(this, &rect, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::clip(rect, op);
  }

  //  void QRasterPaintEngine::clip(const QRegion &region,
  //      Qt::ClipOperation op)
  void clip(const QRegion &region, Qt::ClipOperation op) override {
    if (taken[35]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall35 call = reinterpret_cast<CuteQBlitterPaintEngineCall35>(taken[35]);
      call(this, &region, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QRasterPaintEngine::clip(region, op);
  }

  //  QPoint QRasterPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall36 call = reinterpret_cast<CuteQBlitterPaintEngineCall36>(taken[36]);
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
      CuteQBlitterPaintEngineCall37 call = reinterpret_cast<CuteQBlitterPaintEngineCall37>(taken[37]);
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
      CuteQBlitterPaintEngineCall38 call = reinterpret_cast<CuteQBlitterPaintEngineCall38>(taken[38]);
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
      CuteQBlitterPaintEngineCall39 call = reinterpret_cast<CuteQBlitterPaintEngineCall39>(taken[39]);
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
      CuteQBlitterPaintEngineCall40 call = reinterpret_cast<CuteQBlitterPaintEngineCall40>(taken[40]);
      call(this, &rect, xrad, yrad, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRoundedRect(rect, xrad, yrad, mode);
  }

  //  void QPaintEngineEx::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[41]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall41 call = reinterpret_cast<CuteQBlitterPaintEngineCall41>(taken[41]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[42]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall42 call = reinterpret_cast<CuteQBlitterPaintEngineCall42>(taken[42]);
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
      CuteQBlitterPaintEngineCall43 call = reinterpret_cast<CuteQBlitterPaintEngineCall43>(taken[43]);
      call(this, fragments, fragmentCount, &pixmap, static_cast<int>(hints.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPixmapFragments(fragments, fragmentCount, pixmap, hints);
  }

  //  void QPaintEngineEx::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[44]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall44 call = reinterpret_cast<CuteQBlitterPaintEngineCall44>(taken[44]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPaintEngineEx::updateState(state);
  }

  //  void QPaintEngineEx::sync()
  void sync() override {
    if (taken[45]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall45 call = reinterpret_cast<CuteQBlitterPaintEngineCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::sync();
  }

  //  void QPaintEngineEx::beginNativePainting()
  void beginNativePainting() override {
    if (taken[46]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall46 call = reinterpret_cast<CuteQBlitterPaintEngineCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::beginNativePainting();
  }

  //  void QPaintEngineEx::endNativePainting()
  void endNativePainting() override {
    if (taken[47]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall47 call = reinterpret_cast<CuteQBlitterPaintEngineCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::endNativePainting();
  }

  //  uint QPaintEngineEx::flags() const
  uint flags() const override {
    if (taken[48]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall48 call = reinterpret_cast<CuteQBlitterPaintEngineCall48>(taken[48]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::flags();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[49]) {
      int handled = 0;
      CuteQBlitterPaintEngineCall49 call = reinterpret_cast<CuteQBlitterPaintEngineCall49>(taken[49]);
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
      CuteQBlitterPaintEngineCall50 call = reinterpret_cast<CuteQBlitterPaintEngineCall50>(taken[50]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QBlitterPaintEnginePrivate *QBlitterPaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QBlitterPaintEnginePrivate *ritual_ZN19QBlitterPaintEngine6d_funcEv(
    QBlitterPaintEngine *self) {
  return self->d_func();
}

//  const QBlitterPaintEnginePrivate *QBlitterPaintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QBlitterPaintEnginePrivate *ritual_ZNK19QBlitterPaintEngine6d_funcEv(
    const QBlitterPaintEngine *self) {
  return self->d_func();
}

//  QBlitterPaintEngine::QBlitterPaintEngine(QBlittablePlatformPixmap *p)
extern "C" Q_DECL_EXPORT
QBlitterPaintEngine *ritual_ZN19QBlitterPaintEngineC1EP24QBlittablePlatformPixmap(
    QBlittablePlatformPixmap *p) {
  return new CuteQBlitterPaintEngine(p);
}

//  QPaintEngine::Type QBlitterPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK19QBlitterPaintEngine4typeEv(
    const QBlitterPaintEngine *self) {
  return self->type();
}

//  bool QBlitterPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBlitterPaintEngine5beginEP12QPaintDevice(
    QBlitterPaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QBlitterPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBlitterPaintEngine3endEv(QBlitterPaintEngine *self) {
  return self->end();
}

//  void QBlitterPaintEngine::fill(const QVectorPath &path, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine4fillERK11QVectorPathRK6QBrush(
    QBlitterPaintEngine *self,
    const QVectorPath *path,
    const QBrush *brush) {
  self->fill(*path, *brush);
}

//  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QBrush(
    QBlitterPaintEngine *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->fillRect(*rect, *brush);
}

//  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QColor(
    QBlitterPaintEngine *self,
    const QRectF *rect,
    const QColor *color) {
  self->fillRect(*rect, *color);
}

//  void QBlitterPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine9drawRectsEPK5QRecti(
    QBlitterPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QBlitterPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine9drawRectsEPK6QRectFi(
    QBlitterPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QBlitterPaintEngine::drawPixmap(const QPointF &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine10drawPixmapERK7QPointFRK7QPixmap(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QPixmap *pm) {
  self->drawPixmap(*p, *pm);
}

//  void QBlitterPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QBlitterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QBlitterPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine8setStateEP13QPainterState(
    QBlitterPaintEngine *self,
    QPainterState *s) {
  self->setState(s);
}

//  void QBlitterPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine18clipEnabledChangedEv(
    QBlitterPaintEngine *self) {
  self->clipEnabledChanged();
}

//  void QBlitterPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine10penChangedEv(
    QBlitterPaintEngine *self) {
  self->penChanged();
}

//  void QBlitterPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine12brushChangedEv(
    QBlitterPaintEngine *self) {
  self->brushChanged();
}

//  void QBlitterPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine14opacityChangedEv(
    QBlitterPaintEngine *self) {
  self->opacityChanged();
}

//  void QBlitterPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine22compositionModeChangedEv(
    QBlitterPaintEngine *self) {
  self->compositionModeChanged();
}

//  void QBlitterPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine18renderHintsChangedEv(
    QBlitterPaintEngine *self) {
  self->renderHintsChanged();
}

//  void QBlitterPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine16transformChangedEv(
    QBlitterPaintEngine *self) {
  self->transformChanged();
}

//  void QBlitterPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::drawPolygon(const QPoint *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::fillPath(const QPainterPath &path, QSpanData
//      *fillData)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine8fillPathERK12QPainterPathP9QSpanData(
    QBlitterPaintEngine *self,
    const QPainterPath *path,
    QSpanData *fillData) {
  self->fillPath(*path, fillData);
}

//  void QBlitterPaintEngine::fillPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->fillPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::drawEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine11drawEllipseERK6QRectF(
    QBlitterPaintEngine *self,
    const QRectF *rect) {
  self->drawEllipse(*rect);
}

//  void QBlitterPaintEngine::drawImage(const QPointF &p, const QImage &img)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine9drawImageERK7QPointFRK6QImage(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QImage *img) {
  self->drawImage(*p, *img);
}

//  void QBlitterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QBlitterPaintEngine *self,
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

//  void QBlitterPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QBlitterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *sr) {
  self->drawTiledPixmap(*r, *pm, *sr);
}

//  void QBlitterPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QBlitterPaintEngine::drawPoints(const QPointF *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine10drawPointsEPK7QPointFi(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QBlitterPaintEngine::drawPoints(const QPoint *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine10drawPointsEPK6QPointi(
    QBlitterPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QBlitterPaintEngine::stroke(const QVectorPath &path, const QPen
//      &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine6strokeERK11QVectorPathRK4QPen(
    QBlitterPaintEngine *self,
    const QVectorPath *path,
    const QPen *pen) {
  self->stroke(*path, *pen);
}

//  void QBlitterPaintEngine::drawStaticTextItem(QStaticTextItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBlitterPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QBlitterPaintEngine *self,
    QStaticTextItem *a0) {
  self->drawStaticTextItem(a0);
}

//  bool QBlitterPaintEngine::drawCachedGlyphs(int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBlitterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine(
    QBlitterPaintEngine *self,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->drawCachedGlyphs(numGlyphs, glyphs, positions, fontEngine);
}

//  a Python function taken by a CuteQBlitterPaintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBlitterPaintEngine(
    QBlitterPaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBlitterPaintEngine *>(self)->take(key, call);
}

//  QPaintEngine::Type QBlitterPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK19QBlitterPaintEngine4typeEv(
    const QBlitterPaintEngine *self) {
  return self->QBlitterPaintEngine::type();
}

//  bool QBlitterPaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QBlitterPaintEngine5beginEP12QPaintDevice(
    QBlitterPaintEngine *self,
    QPaintDevice *pdev) {
  return self->QBlitterPaintEngine::begin(pdev);
}

//  bool QBlitterPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QBlitterPaintEngine3endEv(QBlitterPaintEngine *self) {
  return self->QBlitterPaintEngine::end();
}

//  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QBrush(
    QBlitterPaintEngine *self,
    const QRectF *rect,
    const QBrush *brush) {
  self->QBlitterPaintEngine::fillRect(*rect, *brush);
}

//  void QBlitterPaintEngine::fillRect(const QRectF &rect, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine8fillRectERK6QRectFRK6QColor(
    QBlitterPaintEngine *self,
    const QRectF *rect,
    const QColor *color) {
  self->QBlitterPaintEngine::fillRect(*rect, *color);
}

//  void QBlitterPaintEngine::drawRects(const QRect *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine9drawRectsEPK5QRecti(
    QBlitterPaintEngine *self,
    const QRect *rects,
    int rectCount) {
  self->QBlitterPaintEngine::drawRects(rects, rectCount);
}

//  void QBlitterPaintEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine9drawRectsEPK6QRectFi(
    QBlitterPaintEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->QBlitterPaintEngine::drawRects(rects, rectCount);
}

//  void QBlitterPaintEngine::drawPixmap(const QPointF &p, const QPixmap &pm)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine10drawPixmapERK7QPointFRK7QPixmap(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QPixmap *pm) {
  self->QBlitterPaintEngine::drawPixmap(*p, *pm);
}

//  void QBlitterPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QBlitterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QBlitterPaintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QBlitterPaintEngine::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine8setStateEP13QPainterState(
    QBlitterPaintEngine *self,
    QPainterState *s) {
  self->QBlitterPaintEngine::setState(s);
}

//  void QBlitterPaintEngine::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine18clipEnabledChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::clipEnabledChanged();
}

//  void QBlitterPaintEngine::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine10penChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::penChanged();
}

//  void QBlitterPaintEngine::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine12brushChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::brushChanged();
}

//  void QBlitterPaintEngine::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine14opacityChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::opacityChanged();
}

//  void QBlitterPaintEngine::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine22compositionModeChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::compositionModeChanged();
}

//  void QBlitterPaintEngine::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine18renderHintsChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::renderHintsChanged();
}

//  void QBlitterPaintEngine::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine16transformChangedEv(
    QBlitterPaintEngine *self) {
  self->QBlitterPaintEngine::transformChanged();
}

//  void QBlitterPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QBlitterPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::drawPolygon(const QPoint *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine11drawPolygonEPK6QPointiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPoint *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QBlitterPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::fillPath(const QPainterPath &path, QSpanData
//      *fillData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine8fillPathERK12QPainterPathP9QSpanData(
    QBlitterPaintEngine *self,
    const QPainterPath *path,
    QSpanData *fillData) {
  self->QBlitterPaintEngine::fillPath(*path, fillData);
}

//  void QBlitterPaintEngine::fillPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine11fillPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QBlitterPaintEngine::fillPolygon(points, pointCount, mode);
}

//  void QBlitterPaintEngine::drawEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine11drawEllipseERK6QRectF(
    QBlitterPaintEngine *self,
    const QRectF *rect) {
  self->QBlitterPaintEngine::drawEllipse(*rect);
}

//  void QBlitterPaintEngine::drawImage(const QPointF &p, const QImage &img)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine9drawImageERK7QPointFRK6QImage(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QImage *img) {
  self->QBlitterPaintEngine::drawImage(*p, *img);
}

//  void QBlitterPaintEngine::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QBlitterPaintEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->QBlitterPaintEngine::drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QBlitterPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QBlitterPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *sr) {
  self->QBlitterPaintEngine::drawTiledPixmap(*r, *pm, *sr);
}

//  void QBlitterPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QBlitterPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QBlitterPaintEngine::drawTextItem(*p, *textItem);
}

//  void QBlitterPaintEngine::drawPoints(const QPointF *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine10drawPointsEPK7QPointFi(
    QBlitterPaintEngine *self,
    const QPointF *points,
    int pointCount) {
  self->QBlitterPaintEngine::drawPoints(points, pointCount);
}

//  void QBlitterPaintEngine::drawPoints(const QPoint *points, int
//      pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine10drawPointsEPK6QPointi(
    QBlitterPaintEngine *self,
    const QPoint *points,
    int pointCount) {
  self->QBlitterPaintEngine::drawPoints(points, pointCount);
}

//  void QBlitterPaintEngine::drawStaticTextItem(QStaticTextItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBlitterPaintEngine18drawStaticTextItemEP15QStaticTextItem(
    QBlitterPaintEngine *self,
    QStaticTextItem *a0) {
  self->QBlitterPaintEngine::drawStaticTextItem(a0);
}

//  bool QBlitterPaintEngine::drawCachedGlyphs(int numGlyphs, const glyph_t
//      *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QBlitterPaintEngine16drawCachedGlyphsEiPKjPK11QFixedPointP11QFontEngine(
    QBlitterPaintEngine *self,
    int numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    QFontEngine *fontEngine) {
  return self->QBlitterPaintEngine::drawCachedGlyphs(
      numGlyphs,
      glyphs,
      positions,
      fontEngine);
}

#endif  // !defined(QT_NO_BLITTABLE)
