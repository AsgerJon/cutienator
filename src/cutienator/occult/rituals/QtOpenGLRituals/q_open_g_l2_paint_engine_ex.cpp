//  Written by hand on 2026-11-25 from
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: 'tr' and 'metaObject' (the class has no Q_OBJECT) and
//  the copy and move operations (deleted). The class that Python takes
//  functions over in leaves out the virtual functions taking a
//  'QVectorPath' that the class does not declare, as the file of
//  QPaintEngineEx does; 'fill', 'stroke' and 'clip' of this class are
//  rituals, not taken.
//  'setRenderTextActive' is left out: Qt declares it but its library does
//  not offer it.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qtransform.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QOpenGL2PaintEngineEx that Python can take functions over in.
//  Every QOpenGL2PaintEngineEx Python makes is one. Each function below
//  asks the Python function handed over for it, and runs Qt's own
//  without one.
typedef void * (*CuteQOpenGL2PaintEngineExCall0)(const void *, QPainterState *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall1)(const void *, const QRect *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall2)(const void *, const QRegion *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall3)(const void *, const QPainterPath *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall4)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall5)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall6)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall7)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall8)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall9)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall10)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall11)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall12)(const void *, const QRectF *, const QBrush *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall13)(const void *, const QRectF *, const QColor *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall14)(const void *, const QRectF *, qreal, qreal, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall15)(const void *, const QRect *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall16)(const void *, const QRectF *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall17)(const void *, const QLine *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall18)(const void *, const QLineF *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall19)(const void *, const QRectF *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall20)(const void *, const QRect *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall21)(const void *, const QPainterPath *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall22)(const void *, const QPointF *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall23)(const void *, const QPoint *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall24)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall25)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall26)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall27)(const void *, const QPointF *, const QPixmap *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall28)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall29)(const void *, const QPointF *, const QImage *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall30)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall31)(const void *, const QPainter::PixmapFragment *, int, const QPixmap *, int, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall32)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall33)(const void *, QStaticTextItem *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall34)(const void *, QPainterState *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall35)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall36)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall37)(const void *, int *);
typedef uint (*CuteQOpenGL2PaintEngineExCall38)(const void *, int *);
typedef bool (*CuteQOpenGL2PaintEngineExCall39)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQOpenGL2PaintEngineExCall40)(const void *, QFontEngine *, const QTransform *, int *);
typedef bool (*CuteQOpenGL2PaintEngineExCall41)(const void *, QPaintDevice *, int *);
typedef bool (*CuteQOpenGL2PaintEngineExCall42)(const void *, int *);
typedef void (*CuteQOpenGL2PaintEngineExCall43)(const void *, const QPointF *, const QTextItem *, int *);
typedef const QPoint * (*CuteQOpenGL2PaintEngineExCall44)(const void *, int *);
typedef int (*CuteQOpenGL2PaintEngineExCall45)(const void *, int *);
typedef const QPixmap * (*CuteQOpenGL2PaintEngineExCall46)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQOpenGL2PaintEngineExCall47)(const void *, const QImage *, int, int *);
class CuteQOpenGL2PaintEngineEx : public QOpenGL2PaintEngineEx {
public:
  using QOpenGL2PaintEngineEx::QOpenGL2PaintEngineEx;
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

  //  QPainterState *QOpenGL2PaintEngineEx::createState(QPainterState *orig)
  //      const

  QPainterState *createState(QPainterState *orig) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall0 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall0>(taken[0]);
      void * given = call(this, orig, &handled);
      if (handled) return static_cast<QPainterState *>(given);
    }
    return QOpenGL2PaintEngineEx::createState(orig);
  }

  //  void QPaintEngineEx::clip(const QRect &rect, Qt::ClipOperation op)
  void clip(const QRect &rect, Qt::ClipOperation op) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall1 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall1>(taken[1]);
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
      CuteQOpenGL2PaintEngineExCall2 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall2>(taken[2]);
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
      CuteQOpenGL2PaintEngineExCall3 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall3>(taken[3]);
      call(this, &path, static_cast<int>(op), &handled);
      if (handled) return;
    }
    QPaintEngineEx::clip(path, op);
  }

  //  void QOpenGL2PaintEngineEx::clipEnabledChanged()
  void clipEnabledChanged() override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall4 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::clipEnabledChanged();
  }

  //  void QOpenGL2PaintEngineEx::penChanged()
  void penChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall5 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::penChanged();
  }

  //  void QOpenGL2PaintEngineEx::brushChanged()
  void brushChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall6 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::brushChanged();
  }

  //  void QOpenGL2PaintEngineEx::brushOriginChanged()
  void brushOriginChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall7 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::brushOriginChanged();
  }

  //  void QOpenGL2PaintEngineEx::opacityChanged()
  void opacityChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall8 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::opacityChanged();
  }

  //  void QOpenGL2PaintEngineEx::compositionModeChanged()
  void compositionModeChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall9 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::compositionModeChanged();
  }

  //  void QOpenGL2PaintEngineEx::renderHintsChanged()
  void renderHintsChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall10 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::renderHintsChanged();
  }

  //  void QOpenGL2PaintEngineEx::transformChanged()
  void transformChanged() override {
    if (taken[11]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall11 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::transformChanged();
  }

  //  void QPaintEngineEx::fillRect(const QRectF &rect, const QBrush
  //      &brush)
  void fillRect(const QRectF &rect, const QBrush &brush) override {
    if (taken[12]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall12 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall12>(taken[12]);
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
      CuteQOpenGL2PaintEngineExCall13 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall13>(taken[13]);
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
      CuteQOpenGL2PaintEngineExCall14 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall14>(taken[14]);
      call(this, &rect, xrad, yrad, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRoundedRect(rect, xrad, yrad, mode);
  }

  //  void QPaintEngineEx::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[15]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall15 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall15>(taken[15]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRects(rects, rectCount);
  }

  //  void QPaintEngineEx::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[16]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall16 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall16>(taken[16]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawRects(rects, rectCount);
  }

  //  void QPaintEngineEx::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall17 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall17>(taken[17]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawLines(lines, lineCount);
  }

  //  void QPaintEngineEx::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[18]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall18 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall18>(taken[18]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawLines(lines, lineCount);
  }

  //  void QPaintEngineEx::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[19]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall19 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall19>(taken[19]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[20]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall20 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall20>(taken[20]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawEllipse(r);
  }

  //  void QPaintEngineEx::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[21]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall21 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall21>(taken[21]);
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
      CuteQOpenGL2PaintEngineExCall22 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall22>(taken[22]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPoints(points, pointCount);
  }

  //  void QPaintEngineEx::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[23]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall23 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall23>(taken[23]);
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
      CuteQOpenGL2PaintEngineExCall24 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall24>(taken[24]);
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
      CuteQOpenGL2PaintEngineExCall25 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall25>(taken[25]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPolygon(points, pointCount, mode);
  }

  //  void QOpenGL2PaintEngineEx::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[26]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall26 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall26>(taken[26]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::drawPixmap(r, pm, sr);
  }

  //  void QPaintEngineEx::drawPixmap(const QPointF &pos, const QPixmap
  //      &pm)
  void drawPixmap(const QPointF &pos, const QPixmap &pm) override {
    if (taken[27]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall27 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall27>(taken[27]);
      call(this, &pos, &pm, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawPixmap(pos, pm);
  }

  //  void QOpenGL2PaintEngineEx::drawImage(const QRectF &r, const QImage
  //      &pm, const QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[28]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall28 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall28>(taken[28]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::drawImage(r, pm, sr, flags);
  }

  //  void QPaintEngineEx::drawImage(const QPointF &pos, const QImage
  //      &image)
  void drawImage(const QPointF &pos, const QImage &image) override {
    if (taken[29]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall29 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall29>(taken[29]);
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
      CuteQOpenGL2PaintEngineExCall30 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall30>(taken[30]);
      call(this, &r, &pixmap, &s, &handled);
      if (handled) return;
    }
    QPaintEngineEx::drawTiledPixmap(r, pixmap, s);
  }

  //  void QOpenGL2PaintEngineEx::drawPixmapFragments(const
  //      QPainter::PixmapFragment *fragments, int fragmentCount, const
  //      QPixmap &pixmap, QFlags<QPainter::PixmapFragmentHint> hints)
  void drawPixmapFragments(
      const QPainter::PixmapFragment *fragments,
      int fragmentCount,
      const QPixmap &pixmap,
      QFlags<QPainter::PixmapFragmentHint> hints) override {
    if (taken[31]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall31 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall31>(taken[31]);
      call(this, fragments, fragmentCount, &pixmap, static_cast<int>(hints.toInt()), &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::drawPixmapFragments(fragments, fragmentCount, pixmap, hints);
  }

  //  void QPaintEngineEx::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[32]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall32 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall32>(taken[32]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPaintEngineEx::updateState(state);
  }

  //  void QOpenGL2PaintEngineEx::drawStaticTextItem(QStaticTextItem *a0)
  void drawStaticTextItem(QStaticTextItem *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall33 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::drawStaticTextItem(a0);
  }

  //  void QOpenGL2PaintEngineEx::setState(QPainterState *s)
  void setState(QPainterState *s) override {
    if (taken[34]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall34 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall34>(taken[34]);
      call(this, s, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::setState(s);
  }

  //  void QPaintEngineEx::sync()
  void sync() override {
    if (taken[35]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall35 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEngineEx::sync();
  }

  //  void QOpenGL2PaintEngineEx::beginNativePainting()
  void beginNativePainting() override {
    if (taken[36]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall36 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::beginNativePainting();
  }

  //  void QOpenGL2PaintEngineEx::endNativePainting()
  void endNativePainting() override {
    if (taken[37]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall37 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::endNativePainting();
  }

  //  uint QPaintEngineEx::flags() const
  uint flags() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall38 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall38>(taken[38]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintEngineEx::flags();
  }

  //  bool
  //      QOpenGL2PaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
  //      *fontEngine, const QTransform &m) const
  bool requiresPretransformedGlyphPositions(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall39 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall39>(taken[39]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QOpenGL2PaintEngineEx::requiresPretransformedGlyphPositions(fontEngine, m);
  }

  //  bool QOpenGL2PaintEngineEx::shouldDrawCachedGlyphs(QFontEngine
  //      *fontEngine, const QTransform &m) const
  bool shouldDrawCachedGlyphs(
      QFontEngine *fontEngine,
      const QTransform &m) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall40 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall40>(taken[40]);
      bool given = call(this, fontEngine, &m, &handled);
      if (handled) return given;
    }
    return QOpenGL2PaintEngineEx::shouldDrawCachedGlyphs(fontEngine, m);
  }

  //  bool QOpenGL2PaintEngineEx::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[41]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall41 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall41>(taken[41]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QOpenGL2PaintEngineEx::begin(pdev);
  }

  //  bool QOpenGL2PaintEngineEx::end()
  bool end() override {
    if (taken[42]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall42 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGL2PaintEngineEx::end();
  }

  //  void QOpenGL2PaintEngineEx::drawTextItem(const QPointF &p, const
  //      QTextItem &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[43]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall43 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall43>(taken[43]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QOpenGL2PaintEngineEx::drawTextItem(p, textItem);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall44 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall44>(taken[44]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  Type QOpenGL2PaintEngineEx::type() const
  QPaintEngine::Type type() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall45 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall45>(taken[45]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QOpenGL2PaintEngineEx::type();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[46]) {
      int handled = 0;
      CuteQOpenGL2PaintEngineExCall46 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall46>(taken[46]);
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
      CuteQOpenGL2PaintEngineExCall47 call = reinterpret_cast<CuteQOpenGL2PaintEngineExCall47>(taken[47]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }

};

//  QOpenGL2PaintEngineExPrivate *QOpenGL2PaintEngineEx::d_func()
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineExPrivate *ritual_ZN21QOpenGL2PaintEngineEx6d_funcEv(
    QOpenGL2PaintEngineEx *self) {
  return self->d_func();
}

//  const QOpenGL2PaintEngineExPrivate *QOpenGL2PaintEngineEx::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGL2PaintEngineExPrivate *ritual_ZNK21QOpenGL2PaintEngineEx6d_funcEv(
    const QOpenGL2PaintEngineEx *self) {
  return self->d_func();
}

//  QOpenGL2PaintEngineEx::QOpenGL2PaintEngineEx()
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineEx *ritual_ZN21QOpenGL2PaintEngineExC1Ev() {
  return new CuteQOpenGL2PaintEngineEx();
}

//  QOpenGL2PaintEngineEx::~QOpenGL2PaintEngineEx()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineExD1Ev(QOpenGL2PaintEngineEx *self) {
  delete self;
}

//  bool QOpenGL2PaintEngineEx::begin(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QOpenGL2PaintEngineEx5beginEP12QPaintDevice(
    QOpenGL2PaintEngineEx *self,
    QPaintDevice *device) {
  return self->begin(device);
}

//  void QOpenGL2PaintEngineEx::ensureActive()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx12ensureActiveEv(
    QOpenGL2PaintEngineEx *self) {
  self->ensureActive();
}

//  bool QOpenGL2PaintEngineEx::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QOpenGL2PaintEngineEx3endEv(QOpenGL2PaintEngineEx *self) {
  return self->end();
}

//  void QOpenGL2PaintEngineEx::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx18clipEnabledChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->clipEnabledChanged();
}

//  void QOpenGL2PaintEngineEx::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx10penChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->penChanged();
}

//  void QOpenGL2PaintEngineEx::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx12brushChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->brushChanged();
}

//  void QOpenGL2PaintEngineEx::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx18brushOriginChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->brushOriginChanged();
}

//  void QOpenGL2PaintEngineEx::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx14opacityChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->opacityChanged();
}

//  void QOpenGL2PaintEngineEx::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx22compositionModeChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->compositionModeChanged();
}

//  void QOpenGL2PaintEngineEx::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx18renderHintsChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->renderHintsChanged();
}

//  void QOpenGL2PaintEngineEx::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx16transformChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->transformChanged();
}

//  void QOpenGL2PaintEngineEx::drawPixmap(const QRectF &r, const QPixmap
//      &pm, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx10drawPixmapERK6QRectFRK7QPixmapS2_(
    QOpenGL2PaintEngineEx *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QOpenGL2PaintEngineEx::drawPixmapFragments(const
//      QPainter::PixmapFragment *fragments, int fragmentCount, const QPixmap
//      &pixmap, QPainter::PixmapFragmentHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE(
    QOpenGL2PaintEngineEx *self,
    const QPainter::PixmapFragment *fragments,
    int fragmentCount,
    const QPixmap *pixmap,
    int hints) {
  self->drawPixmapFragments(fragments, fragmentCount, *pixmap, QFlags<QPainter::PixmapFragmentHint>::fromInt(hints));
}

//  void QOpenGL2PaintEngineEx::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QOpenGL2PaintEngineEx *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->drawImage(*r, *pm, *sr, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QOpenGL2PaintEngineEx::drawTextItem(const QPointF &p, const
//      QTextItem &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx12drawTextItemERK7QPointFRK9QTextItem(
    QOpenGL2PaintEngineEx *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QOpenGL2PaintEngineEx::fill(const QVectorPath &path, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx4fillERK11QVectorPathRK6QBrush(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    const QBrush *brush) {
  self->fill(*path, *brush);
}

//  void QOpenGL2PaintEngineEx::stroke(const QVectorPath &path, const QPen
//      &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx6strokeERK11QVectorPathRK4QPen(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    const QPen *pen) {
  self->stroke(*path, *pen);
}

//  void QOpenGL2PaintEngineEx::clip(const QVectorPath &path,
//      Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx4clipERK11QVectorPathN2Qt13ClipOperationE(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    Qt::ClipOperation op) {
  self->clip(*path, op);
}

//  void QOpenGL2PaintEngineEx::drawStaticTextItem(QStaticTextItem *textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx18drawStaticTextItemEP15QStaticTextItem(
    QOpenGL2PaintEngineEx *self,
    QStaticTextItem *textItem) {
  self->drawStaticTextItem(textItem);
}

//  bool QOpenGL2PaintEngineEx::drawTexture(const QRectF &r, GLuint
//      textureId, const QSize &size, const QRectF &sr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QOpenGL2PaintEngineEx11drawTextureERK6QRectFjRK5QSizeS2_(
    QOpenGL2PaintEngineEx *self,
    const QRectF *r,
    unsigned int textureId,
    const QSize *size,
    const QRectF *sr) {
  return self->drawTexture(*r, textureId, *size, *sr);
}

//  Type QOpenGL2PaintEngineEx::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QOpenGL2PaintEngineEx4typeEv(
    const QOpenGL2PaintEngineEx *self) {
  return static_cast<int>(self->type());
}

//  void QOpenGL2PaintEngineEx::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx8setStateEP13QPainterState(
    QOpenGL2PaintEngineEx *self,
    QPainterState *s) {
  self->setState(s);
}

//  QPainterState *QOpenGL2PaintEngineEx::createState(QPainterState *orig)
//      const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_ZNK21QOpenGL2PaintEngineEx11createStateEP13QPainterState(
    const QOpenGL2PaintEngineEx *self,
    QPainterState *orig) {
  return self->createState(orig);
}

//  QOpenGL2PaintEngineState *QOpenGL2PaintEngineEx::state()
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineState *ritual_ZN21QOpenGL2PaintEngineEx5stateEv(
    QOpenGL2PaintEngineEx *self) {
  return self->state();
}

//  const QOpenGL2PaintEngineState *QOpenGL2PaintEngineEx::state() const
extern "C" Q_DECL_EXPORT
const QOpenGL2PaintEngineState *ritual_ZNK21QOpenGL2PaintEngineEx5stateEv(
    const QOpenGL2PaintEngineEx *self) {
  return self->state();
}

//  void QOpenGL2PaintEngineEx::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx19beginNativePaintingEv(
    QOpenGL2PaintEngineEx *self) {
  self->beginNativePainting();
}

//  void QOpenGL2PaintEngineEx::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx17endNativePaintingEv(
    QOpenGL2PaintEngineEx *self) {
  self->endNativePainting();
}

//  void QOpenGL2PaintEngineEx::invalidateState()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2PaintEngineEx15invalidateStateEv(
    QOpenGL2PaintEngineEx *self) {
  self->invalidateState();
}

//  bool QOpenGL2PaintEngineEx::isNativePaintingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGL2PaintEngineEx22isNativePaintingActiveEv(
    const QOpenGL2PaintEngineEx *self) {
  return self->isNativePaintingActive();
}

//  bool
//      QOpenGL2PaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
//      *a0, const QTransform &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGL2PaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QOpenGL2PaintEngineEx *self,
    QFontEngine *a0,
    const QTransform *a1) {
  return self->requiresPretransformedGlyphPositions(a0, *a1);
}

//  bool QOpenGL2PaintEngineEx::shouldDrawCachedGlyphs(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpenGL2PaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QOpenGL2PaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->shouldDrawCachedGlyphs(fontEngine, *m);
}

//  a Python function taken by a CuteQOpenGL2PaintEngineEx, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGL2PaintEngineEx(
    QOpenGL2PaintEngineEx *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGL2PaintEngineEx *>(self)->take(key, call);
}

//  bool QOpenGL2PaintEngineEx::begin(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QOpenGL2PaintEngineEx5beginEP12QPaintDevice(
    QOpenGL2PaintEngineEx *self,
    QPaintDevice *device) {
  return self->QOpenGL2PaintEngineEx::begin(device);
}

//  bool QOpenGL2PaintEngineEx::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QOpenGL2PaintEngineEx3endEv(
    QOpenGL2PaintEngineEx *self) {
  return self->QOpenGL2PaintEngineEx::end();
}

//  void QOpenGL2PaintEngineEx::clipEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx18clipEnabledChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::clipEnabledChanged();
}

//  void QOpenGL2PaintEngineEx::penChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx10penChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::penChanged();
}

//  void QOpenGL2PaintEngineEx::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx12brushChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::brushChanged();
}

//  void QOpenGL2PaintEngineEx::brushOriginChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx18brushOriginChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::brushOriginChanged();
}

//  void QOpenGL2PaintEngineEx::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx14opacityChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::opacityChanged();
}

//  void QOpenGL2PaintEngineEx::compositionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx22compositionModeChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::compositionModeChanged();
}

//  void QOpenGL2PaintEngineEx::renderHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx18renderHintsChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::renderHintsChanged();
}

//  void QOpenGL2PaintEngineEx::transformChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx16transformChangedEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::transformChanged();
}

//  void QOpenGL2PaintEngineEx::drawPixmap(const QRectF &r, const QPixmap
//      &pm, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx10drawPixmapERK6QRectFRK7QPixmapS2_(
    QOpenGL2PaintEngineEx *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QOpenGL2PaintEngineEx::drawPixmap(*r, *pm, *sr);
}

//  void QOpenGL2PaintEngineEx::drawPixmapFragments(const
//      QPainter::PixmapFragment *fragments, int fragmentCount, const QPixmap
//      &pixmap, QPainter::PixmapFragmentHints hints)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE(
    QOpenGL2PaintEngineEx *self,
    const QPainter::PixmapFragment *fragments,
    int fragmentCount,
    const QPixmap *pixmap,
    int hints) {
  self->QOpenGL2PaintEngineEx::drawPixmapFragments(fragments, fragmentCount, *pixmap, QFlags<QPainter::PixmapFragmentHint>::fromInt(hints));
}

//  void QOpenGL2PaintEngineEx::drawImage(const QRectF &r, const QImage &pm,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QOpenGL2PaintEngineEx *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->QOpenGL2PaintEngineEx::drawImage(*r, *pm, *sr, QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QOpenGL2PaintEngineEx::drawTextItem(const QPointF &p, const
//      QTextItem &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx12drawTextItemERK7QPointFRK9QTextItem(
    QOpenGL2PaintEngineEx *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QOpenGL2PaintEngineEx::drawTextItem(*p, *textItem);
}

//  void QOpenGL2PaintEngineEx::fill(const QVectorPath &path, const QBrush
//      &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx4fillERK11QVectorPathRK6QBrush(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    const QBrush *brush) {
  self->QOpenGL2PaintEngineEx::fill(*path, *brush);
}

//  void QOpenGL2PaintEngineEx::stroke(const QVectorPath &path, const QPen
//      &pen)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx6strokeERK11QVectorPathRK4QPen(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    const QPen *pen) {
  self->QOpenGL2PaintEngineEx::stroke(*path, *pen);
}

//  void QOpenGL2PaintEngineEx::clip(const QVectorPath &path,
//      Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx4clipERK11QVectorPathN2Qt13ClipOperationE(
    QOpenGL2PaintEngineEx *self,
    const QVectorPath *path,
    Qt::ClipOperation op) {
  self->QOpenGL2PaintEngineEx::clip(*path, op);
}

//  void QOpenGL2PaintEngineEx::drawStaticTextItem(QStaticTextItem *textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx18drawStaticTextItemEP15QStaticTextItem(
    QOpenGL2PaintEngineEx *self,
    QStaticTextItem *textItem) {
  self->QOpenGL2PaintEngineEx::drawStaticTextItem(textItem);
}

//  Type QOpenGL2PaintEngineEx::type() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QOpenGL2PaintEngineEx4typeEv(
    const QOpenGL2PaintEngineEx *self) {
  return static_cast<int>(self->QOpenGL2PaintEngineEx::type());
}

//  void QOpenGL2PaintEngineEx::setState(QPainterState *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx8setStateEP13QPainterState(
    QOpenGL2PaintEngineEx *self,
    QPainterState *s) {
  self->QOpenGL2PaintEngineEx::setState(s);
}

//  QPainterState *QOpenGL2PaintEngineEx::createState(QPainterState *orig)
//      const
extern "C" Q_DECL_EXPORT
QPainterState *ritual_own_ZNK21QOpenGL2PaintEngineEx11createStateEP13QPainterState(
    const QOpenGL2PaintEngineEx *self,
    QPainterState *orig) {
  return self->QOpenGL2PaintEngineEx::createState(orig);
}

//  void QOpenGL2PaintEngineEx::beginNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx19beginNativePaintingEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::beginNativePainting();
}

//  void QOpenGL2PaintEngineEx::endNativePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2PaintEngineEx17endNativePaintingEv(
    QOpenGL2PaintEngineEx *self) {
  self->QOpenGL2PaintEngineEx::endNativePainting();
}

//  bool
//      QOpenGL2PaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
//      *a0, const QTransform &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QOpenGL2PaintEngineEx36requiresPretransformedGlyphPositionsEP11QFontEngineRK10QTransform(
    const QOpenGL2PaintEngineEx *self,
    QFontEngine *a0,
    const QTransform *a1) {
  return self->QOpenGL2PaintEngineEx::requiresPretransformedGlyphPositions(a0, *a1);
}

//  bool QOpenGL2PaintEngineEx::shouldDrawCachedGlyphs(QFontEngine
//      *fontEngine, const QTransform &m) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QOpenGL2PaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10QTransform(
    const QOpenGL2PaintEngineEx *self,
    QFontEngine *fontEngine,
    const QTransform *m) {
  return self->QOpenGL2PaintEngineEx::shouldDrawCachedGlyphs(fontEngine, *m);
}
