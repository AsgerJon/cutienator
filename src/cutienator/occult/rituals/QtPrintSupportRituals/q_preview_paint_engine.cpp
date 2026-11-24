//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_preview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(printpreviewwidget)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_preview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpaintengine.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qvariant.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPreviewPaintEngine that Python can take functions over in. Every QPreviewPaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(printpreviewwidget)
typedef bool (*CuteQPreviewPaintEngineCall0)(const void *, QPaintDevice *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef bool (*CuteQPreviewPaintEngineCall1)(const void *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall2)(const void *, const QPaintEngineState *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall3)(const void *, const QPainterPath *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall4)(const void *, const QPointF *, int, int, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall5)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall6)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall7)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
typedef int (*CuteQPreviewPaintEngineCall8)(const void *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef void (*CuteQPreviewPaintEngineCall9)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef const QVariant * (*CuteQPreviewPaintEngineCall10)(const void *, int, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef bool (*CuteQPreviewPaintEngineCall11)(const void *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef bool (*CuteQPreviewPaintEngineCall12)(const void *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef int (*CuteQPreviewPaintEngineCall13)(const void *, int, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
typedef int (*CuteQPreviewPaintEngineCall14)(const void *, int *);
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
typedef void (*CuteQPreviewPaintEngineCall15)(const void *, const QRect *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall16)(const void *, const QRectF *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall17)(const void *, const QLine *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall18)(const void *, const QLineF *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall19)(const void *, const QRectF *, int *);
typedef void (*CuteQPreviewPaintEngineCall20)(const void *, const QRect *, int *);
typedef void (*CuteQPreviewPaintEngineCall21)(const void *, const QPointF *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall22)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPreviewPaintEngineCall23)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQPreviewPaintEngineCall24)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef const QPoint * (*CuteQPreviewPaintEngineCall25)(const void *, int *);
typedef const QPixmap * (*CuteQPreviewPaintEngineCall26)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQPreviewPaintEngineCall27)(const void *, const QImage *, int, int *);
class CuteQPreviewPaintEngine : public QPreviewPaintEngine {
public:
  using QPreviewPaintEngine::QPreviewPaintEngine;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8QVariant")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPrintEngine7newPageEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZN12QPrintEngine5abortEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
    if (!std::strcmp(key, "_ZNK12QPrintEngine12printerStateEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)
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
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12createPixmapE5QSize")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine21createPixmapFromImageE6QImage6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[27] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(printpreviewwidget)
  //  bool QPreviewPaintEngine::begin(QPaintDevice *dev)
  bool begin(QPaintDevice *dev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall0 call = reinterpret_cast<CuteQPreviewPaintEngineCall0>(taken[0]);
      bool given = call(this, dev, &handled);
      if (handled) return given;
    }
    return QPreviewPaintEngine::begin(dev);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  bool QPreviewPaintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall1 call = reinterpret_cast<CuteQPreviewPaintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPreviewPaintEngine::end();
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall2 call = reinterpret_cast<CuteQPreviewPaintEngineCall2>(taken[2]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::updateState(state);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall3 call = reinterpret_cast<CuteQPreviewPaintEngineCall3>(taken[3]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::drawPath(path);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall4 call = reinterpret_cast<CuteQPreviewPaintEngineCall4>(taken[4]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::drawTextItem(const QPointF &p, const
  //      QTextItem &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall5 call = reinterpret_cast<CuteQPreviewPaintEngineCall5>(taken[5]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::drawTextItem(p, textItem);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall6 call = reinterpret_cast<CuteQPreviewPaintEngineCall6>(taken[6]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::drawPixmap(r, pm, sr);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r, const
  //      QPixmap &pm, const QPointF &p)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QPointF &p) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall7 call = reinterpret_cast<CuteQPreviewPaintEngineCall7>(taken[7]);
      call(this, &r, &pm, &p, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::drawTiledPixmap(r, pm, p);
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if QT_CONFIG(printpreviewwidget)
  //  QPaintEngine::Type QPreviewPaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall8 call = reinterpret_cast<CuteQPreviewPaintEngineCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QPreviewPaintEngine::type();
  }
#endif  // QT_CONFIG(printpreviewwidget)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey key,
  //      const QVariant &value)
  void setProperty(
      QPrintEngine::PrintEnginePropertyKey key,
      const QVariant &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall9 call = reinterpret_cast<CuteQPreviewPaintEngineCall9>(taken[9]);
      call(this, static_cast<int>(key), &value, &handled);
      if (handled) return;
    }
    QPreviewPaintEngine::setProperty(key, value);
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey key)
  //      const
  QVariant property(
      QPrintEngine::PrintEnginePropertyKey key) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall10 call = reinterpret_cast<CuteQPreviewPaintEngineCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QPreviewPaintEngine::property(key);
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  bool QPreviewPaintEngine::newPage()
  bool newPage() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall11 call = reinterpret_cast<CuteQPreviewPaintEngineCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPreviewPaintEngine::newPage();
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  bool QPreviewPaintEngine::abort()
  bool abort() override {
    if (taken[12]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall12 call = reinterpret_cast<CuteQPreviewPaintEngineCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPreviewPaintEngine::abort();
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  int QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric a0)
  //      const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall13 call = reinterpret_cast<CuteQPreviewPaintEngineCall13>(taken[13]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPreviewPaintEngine::metric(a0);
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(printpreviewwidget)
  //  QPrinter::PrinterState QPreviewPaintEngine::printerState() const
  QPrinter::PrinterState printerState() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall14 call = reinterpret_cast<CuteQPreviewPaintEngineCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrinter::PrinterState>(given);
    }
    return QPreviewPaintEngine::printerState();
  }
#endif  // QT_CONFIG(printpreviewwidget)
#endif  // !defined(QT_NO_PRINTER)

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall15 call = reinterpret_cast<CuteQPreviewPaintEngineCall15>(taken[15]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall16 call = reinterpret_cast<CuteQPreviewPaintEngineCall16>(taken[16]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall17 call = reinterpret_cast<CuteQPreviewPaintEngineCall17>(taken[17]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall18 call = reinterpret_cast<CuteQPreviewPaintEngineCall18>(taken[18]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall19 call = reinterpret_cast<CuteQPreviewPaintEngineCall19>(taken[19]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall20 call = reinterpret_cast<CuteQPreviewPaintEngineCall20>(taken[20]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall21 call = reinterpret_cast<CuteQPreviewPaintEngineCall21>(taken[21]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall22 call = reinterpret_cast<CuteQPreviewPaintEngineCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall23 call = reinterpret_cast<CuteQPreviewPaintEngineCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall24 call = reinterpret_cast<CuteQPreviewPaintEngineCall24>(taken[24]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngine::drawImage(r, pm, sr, flags);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall25 call = reinterpret_cast<CuteQPreviewPaintEngineCall25>(taken[25]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall26 call = reinterpret_cast<CuteQPreviewPaintEngineCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQPreviewPaintEngineCall27 call = reinterpret_cast<CuteQPreviewPaintEngineCall27>(taken[27]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QPaintEngine::Type QPreviewPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK19QPreviewPaintEngine4typeEv(
    const QPreviewPaintEngine *self) {
  return self->type();
}

//  QPreviewPaintEngine as the QPrintEngine it is built on
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_cast_QPreviewPaintEngine_QPrintEngine(
    QPreviewPaintEngine *self) {
  return static_cast<QPrintEngine *>(self);
}

//  a Python function taken by a CuteQPreviewPaintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPreviewPaintEngine(
    QPreviewPaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPreviewPaintEngine *>(self)->take(key, call);
}

//  QPaintEngine::Type QPreviewPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK19QPreviewPaintEngine4typeEv(
    const QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::type();
}

#endif  // QT_CONFIG(printpreviewwidget)
