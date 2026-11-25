//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_pdf_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: the '#if' the whole file
//  stands under now also asks '__has_include(<cups/ppd.h>)' where Qt's
//  'qprint_p.h', which 'qprintengine_pdf_p.h' includes, includes that
//  header of CUPS, on macOS and on Unix with 'QT_CONFIG(cups)', since a
//  machine without the headers of CUPS, as GitHub's Linux, refused the
//  file. Kept as it is when the generator runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER) && \
    (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || \
     __has_include(<cups/ppd.h>))
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_pdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPdfPrintEngine that Python can take functions over in. Every QPdfPrintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPdfPrintEngineCall0)(const void *, QPaintDevice *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPdfPrintEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPdfPrintEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPdfPrintEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPdfPrintEngineCall4)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPdfPrintEngineCall5)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPdfPrintEngineCall6)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QVariant * (*CuteQPdfPrintEngineCall7)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall8)(const void *, const QPointF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall9)(const void *, const QLineF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall10)(const void *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall11)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall12)(const void *, const QPainterPath *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall13)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall14)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall15)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall16)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall17)(const void *, const QPaintEngineState *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef int (*CuteQPdfPrintEngineCall18)(const void *, int *);
#endif  // !defined(QT_NO_PDF)
typedef void (*CuteQPdfPrintEngineCall19)(const void *, const QRect *, int, int *);
typedef void (*CuteQPdfPrintEngineCall20)(const void *, const QLine *, int, int *);
typedef void (*CuteQPdfPrintEngineCall21)(const void *, const QRectF *, int *);
typedef void (*CuteQPdfPrintEngineCall22)(const void *, const QRect *, int *);
typedef void (*CuteQPdfPrintEngineCall23)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPdfPrintEngineCall24)(const void *, const QPoint *, int, int, int *);
typedef const QPoint * (*CuteQPdfPrintEngineCall25)(const void *, int *);
typedef const QPixmap * (*CuteQPdfPrintEngineCall26)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQPdfPrintEngineCall27)(const void *, const QImage *, int, int *);
class CuteQPdfPrintEngine : public QPdfPrintEngine {
public:
  using QPdfPrintEngine::QPdfPrintEngine;
  void *taken[28] = {};

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
    if (!std::strcmp(key, "_ZN12QPrintEngine5abortEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine12printerStateEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPrintEngine7newPageEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8QVariant")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
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

#if !defined(QT_NO_PRINTER)
  //  bool QPdfPrintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfPrintEngineCall0 call = reinterpret_cast<CuteQPdfPrintEngineCall0>(taken[0]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QPdfPrintEngine::begin(pdev);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPdfPrintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfPrintEngineCall1 call = reinterpret_cast<CuteQPdfPrintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfPrintEngine::end();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPdfPrintEngine::abort()
  bool abort() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfPrintEngineCall2 call = reinterpret_cast<CuteQPdfPrintEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfPrintEngine::abort();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrinter::PrinterState QPdfPrintEngine::printerState() const
  QPrinter::PrinterState printerState() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfPrintEngineCall3 call = reinterpret_cast<CuteQPdfPrintEngineCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrinter::PrinterState>(given);
    }
    return QPdfPrintEngine::printerState();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPdfPrintEngine::newPage()
  bool newPage() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPdfPrintEngineCall4 call = reinterpret_cast<CuteQPdfPrintEngineCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfPrintEngine::newPage();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  int QPdfPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPdfPrintEngineCall5 call = reinterpret_cast<CuteQPdfPrintEngineCall5>(taken[5]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPdfPrintEngine::metric(a0);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPdfPrintEngine::setProperty(PrintEnginePropertyKey key, const
  //      QVariant &value)
  void setProperty(
      QPrintEngine::PrintEnginePropertyKey key,
      const QVariant &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPdfPrintEngineCall6 call = reinterpret_cast<CuteQPdfPrintEngineCall6>(taken[6]);
      call(this, static_cast<int>(key), &value, &handled);
      if (handled) return;
    }
    QPdfPrintEngine::setProperty(key, value);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QVariant QPdfPrintEngine::property(PrintEnginePropertyKey key) const
  QVariant property(
      QPrintEngine::PrintEnginePropertyKey key) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPdfPrintEngineCall7 call = reinterpret_cast<CuteQPdfPrintEngineCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QPdfPrintEngine::property(key);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPdfPrintEngineCall8 call = reinterpret_cast<CuteQPdfPrintEngineCall8>(taken[8]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPdfEngine::drawPoints(points, pointCount);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPdfPrintEngineCall9 call = reinterpret_cast<CuteQPdfPrintEngineCall9>(taken[9]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPdfEngine::drawLines(lines, lineCount);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPdfPrintEngineCall10 call = reinterpret_cast<CuteQPdfPrintEngineCall10>(taken[10]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPdfEngine::drawRects(rects, rectCount);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPolygon(const QPointF *points, int pointCount,
  //      PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPdfPrintEngineCall11 call = reinterpret_cast<CuteQPdfPrintEngineCall11>(taken[11]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPdfEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPdfPrintEngineCall12 call = reinterpret_cast<CuteQPdfPrintEngineCall12>(taken[12]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPdfEngine::drawPath(path);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawTextItem(const QPointF &p, const QTextItem
  //      &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPdfPrintEngineCall13 call = reinterpret_cast<CuteQPdfPrintEngineCall13>(taken[13]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QPdfEngine::drawTextItem(p, textItem);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPixmap(const QRectF &rectangle, const QPixmap
  //      &pixmap, const QRectF &sr)
  void drawPixmap(
      const QRectF &rectangle,
      const QPixmap &pixmap,
      const QRectF &sr) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPdfPrintEngineCall14 call = reinterpret_cast<CuteQPdfPrintEngineCall14>(taken[14]);
      call(this, &rectangle, &pixmap, &sr, &handled);
      if (handled) return;
    }
    QPdfEngine::drawPixmap(rectangle, pixmap, sr);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawImage(const QRectF &r, const QImage &pm, const
  //      QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &pm,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPdfPrintEngineCall15 call = reinterpret_cast<CuteQPdfPrintEngineCall15>(taken[15]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPdfEngine::drawImage(r, pm, sr, flags);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawTiledPixmap(const QRectF &rectangle, const
  //      QPixmap &pixmap, const QPointF &point)
  void drawTiledPixmap(
      const QRectF &rectangle,
      const QPixmap &pixmap,
      const QPointF &point) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPdfPrintEngineCall16 call = reinterpret_cast<CuteQPdfPrintEngineCall16>(taken[16]);
      call(this, &rectangle, &pixmap, &point, &handled);
      if (handled) return;
    }
    QPdfEngine::drawTiledPixmap(rectangle, pixmap, point);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPdfPrintEngineCall17 call = reinterpret_cast<CuteQPdfPrintEngineCall17>(taken[17]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPdfEngine::updateState(state);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  Type QPdfEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPdfPrintEngineCall18 call = reinterpret_cast<CuteQPdfPrintEngineCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QPdfEngine::type();
  }
#endif  // !defined(QT_NO_PDF)

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPdfPrintEngineCall19 call = reinterpret_cast<CuteQPdfPrintEngineCall19>(taken[19]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPdfPrintEngineCall20 call = reinterpret_cast<CuteQPdfPrintEngineCall20>(taken[20]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPdfPrintEngineCall21 call = reinterpret_cast<CuteQPdfPrintEngineCall21>(taken[21]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPdfPrintEngineCall22 call = reinterpret_cast<CuteQPdfPrintEngineCall22>(taken[22]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPdfPrintEngineCall23 call = reinterpret_cast<CuteQPdfPrintEngineCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQPdfPrintEngineCall24 call = reinterpret_cast<CuteQPdfPrintEngineCall24>(taken[24]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPdfPrintEngineCall25 call = reinterpret_cast<CuteQPdfPrintEngineCall25>(taken[25]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPdfPrintEngineCall26 call = reinterpret_cast<CuteQPdfPrintEngineCall26>(taken[26]);
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
      CuteQPdfPrintEngineCall27 call = reinterpret_cast<CuteQPdfPrintEngineCall27>(taken[27]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QPdfPrintEnginePrivate *QPdfPrintEngine::d_func()
extern "C" Q_DECL_EXPORT
QPdfPrintEnginePrivate *ritual_ZN15QPdfPrintEngine6d_funcEv(
    QPdfPrintEngine *self) {
  return self->d_func();
}

//  const QPdfPrintEnginePrivate *QPdfPrintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QPdfPrintEnginePrivate *ritual_ZNK15QPdfPrintEngine6d_funcEv(
    const QPdfPrintEngine *self) {
  return self->d_func();
}

//  QPdfPrintEngine::QPdfPrintEngine(QPrinter::PrinterMode m,
//      QPdfEngine::PdfVersion version)
extern "C" Q_DECL_EXPORT
QPdfPrintEngine *ritual_ZN15QPdfPrintEngineC1EN8QPrinter11PrinterModeEN10QPdfEngine10PdfVersionE(
    QPrinter::PrinterMode m,
    QPdfEngine::PdfVersion version) {
  return new CuteQPdfPrintEngine(m, version);
}

//  QPdfPrintEngine::~QPdfPrintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfPrintEngineD1Ev(QPdfPrintEngine *self) {
  delete self;
}

//  bool QPdfPrintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPdfPrintEngine5beginEP12QPaintDevice(
    QPdfPrintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QPdfPrintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPdfPrintEngine3endEv(QPdfPrintEngine *self) {
  return self->end();
}

//  bool QPdfPrintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPdfPrintEngine5abortEv(QPdfPrintEngine *self) {
  return self->abort();
}

//  QPrinter::PrinterState QPdfPrintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK15QPdfPrintEngine12printerStateEv(
    const QPdfPrintEngine *self) {
  return self->printerState();
}

//  bool QPdfPrintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPdfPrintEngine7newPageEv(QPdfPrintEngine *self) {
  return self->newPage();
}

//  int QPdfPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPdfPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPdfPrintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  void QPdfPrintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfPrintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QPdfPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->setProperty(key, *value);
}

//  QVariant QPdfPrintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QPdfPrintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QPdfPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->property(key));
}

//  QPdfPrintEngine as the QPrintEngine it is built on
extern "C" Q_DECL_EXPORT
QPrintEngine *ritual_cast_QPdfPrintEngine_QPrintEngine(
    QPdfPrintEngine *self) {
  return static_cast<QPrintEngine *>(self);
}

//  a Python function taken by a CuteQPdfPrintEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfPrintEngine(
    QPdfPrintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfPrintEngine *>(self)->take(key, call);
}

//  bool QPdfPrintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPdfPrintEngine5beginEP12QPaintDevice(
    QPdfPrintEngine *self,
    QPaintDevice *pdev) {
  return self->QPdfPrintEngine::begin(pdev);
}

//  bool QPdfPrintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPdfPrintEngine3endEv(QPdfPrintEngine *self) {
  return self->QPdfPrintEngine::end();
}

//  bool QPdfPrintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPdfPrintEngine5abortEv(QPdfPrintEngine *self) {
  return self->QPdfPrintEngine::abort();
}

//  QPrinter::PrinterState QPdfPrintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_own_ZNK15QPdfPrintEngine12printerStateEv(
    const QPdfPrintEngine *self) {
  return self->QPdfPrintEngine::printerState();
}

//  bool QPdfPrintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPdfPrintEngine7newPageEv(QPdfPrintEngine *self) {
  return self->QPdfPrintEngine::newPage();
}

//  int QPdfPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QPdfPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPdfPrintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->QPdfPrintEngine::metric(a0);
}

//  void QPdfPrintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPdfPrintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QPdfPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->QPdfPrintEngine::setProperty(key, *value);
}

//  QVariant QPdfPrintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK15QPdfPrintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QPdfPrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->QPdfPrintEngine::property(key));
}

#endif  // !defined(QT_NO_PRINTER) && (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || __has_include(<cups/ppd.h>))
