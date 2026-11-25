//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_win_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  A Windows handle (HDC, HGLOBAL) is passed as an address.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_win_p.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qtransform.h>
#include <cstring>

//  A QWin32PrintEngine that Python can take functions over in. Every
//  QWin32PrintEngine Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQWin32PrintEngineCall0)(const void *, QPaintDevice *, int *);
typedef bool (*CuteQWin32PrintEngineCall1)(const void *, int *);
typedef void (*CuteQWin32PrintEngineCall2)(const void *, const QPaintEngineState *, int *);
typedef void (*CuteQWin32PrintEngineCall3)(const void *, const QPainterPath *, int *);
typedef void (*CuteQWin32PrintEngineCall4)(const void *, const QPointF *, int, int, int *);
typedef void (*CuteQWin32PrintEngineCall5)(const void *, const QPointF *, const QTextItem *, int *);
typedef void (*CuteQWin32PrintEngineCall6)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
typedef void (*CuteQWin32PrintEngineCall7)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
typedef void (*CuteQWin32PrintEngineCall8)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQWin32PrintEngineCall9)(const void *, int, int *);
typedef bool (*CuteQWin32PrintEngineCall10)(const void *, int *);
typedef bool (*CuteQWin32PrintEngineCall11)(const void *, int *);
typedef int (*CuteQWin32PrintEngineCall12)(const void *, int, int *);
typedef int (*CuteQWin32PrintEngineCall13)(const void *, int *);
typedef int (*CuteQWin32PrintEngineCall14)(const void *, int *);
typedef void (*CuteQWin32PrintEngineCall15)(const void *, const QRect *, int, int *);
typedef void (*CuteQWin32PrintEngineCall16)(const void *, const QRectF *, int, int *);
typedef void (*CuteQWin32PrintEngineCall17)(const void *, const QLine *, int, int *);
typedef void (*CuteQWin32PrintEngineCall18)(const void *, const QLineF *, int, int *);
typedef void (*CuteQWin32PrintEngineCall19)(const void *, const QRectF *, int *);
typedef void (*CuteQWin32PrintEngineCall20)(const void *, const QRect *, int *);
typedef void (*CuteQWin32PrintEngineCall21)(const void *, const QPointF *, int, int *);
typedef void (*CuteQWin32PrintEngineCall22)(const void *, const QPoint *, int, int *);
typedef void (*CuteQWin32PrintEngineCall23)(const void *, const QPoint *, int, int, int *);
typedef void (*CuteQWin32PrintEngineCall24)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
typedef const QPoint * (*CuteQWin32PrintEngineCall25)(const void *, int *);
typedef const QPixmap * (*CuteQWin32PrintEngineCall26)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQWin32PrintEngineCall27)(const void *, const QImage *, int, int *);
class CuteQWin32PrintEngine : public QWin32PrintEngine {
public:
  using QWin32PrintEngine::QWin32PrintEngine;
  void *taken[28] = {};

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
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8QVariant")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPrintEngine7newPageEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPrintEngine5abortEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPrintEngine12printerStateEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
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

  //  bool QWin32PrintEngine::begin(QPaintDevice *dev)
  bool begin(QPaintDevice *dev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWin32PrintEngineCall0 call = reinterpret_cast<CuteQWin32PrintEngineCall0>(taken[0]);
      bool given = call(this, dev, &handled);
      if (handled) return given;
    }
    return QWin32PrintEngine::begin(dev);
  }

  //  bool QWin32PrintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWin32PrintEngineCall1 call = reinterpret_cast<CuteQWin32PrintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWin32PrintEngine::end();
  }

  //  void QWin32PrintEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWin32PrintEngineCall2 call = reinterpret_cast<CuteQWin32PrintEngineCall2>(taken[2]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::updateState(state);
  }

  //  void QWin32PrintEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWin32PrintEngineCall3 call = reinterpret_cast<CuteQWin32PrintEngineCall3>(taken[3]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::drawPath(path);
  }

  //  void QWin32PrintEngine::drawPolygon(const QPointF *points, int
  //      pointCount, PolygonDrawMode mode)
  void drawPolygon(const QPointF *points, int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWin32PrintEngineCall4 call = reinterpret_cast<CuteQWin32PrintEngineCall4>(taken[4]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QWin32PrintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QWin32PrintEngine::drawTextItem(const QPointF &p, const QTextItem
  //      &textItem)
  void drawTextItem(const QPointF &p, const QTextItem &textItem) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWin32PrintEngineCall5 call = reinterpret_cast<CuteQWin32PrintEngineCall5>(taken[5]);
      call(this, &p, &textItem, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::drawTextItem(p, textItem);
  }

  //  void QWin32PrintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
  //      const QRectF &sr)
  void drawPixmap(const QRectF &r, const QPixmap &pm, const QRectF &sr) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWin32PrintEngineCall6 call = reinterpret_cast<CuteQWin32PrintEngineCall6>(taken[6]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::drawPixmap(r, pm, sr);
  }

  //  void QWin32PrintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
  //      &pm, const QPointF &p)
  void drawTiledPixmap(const QRectF &r, const QPixmap &pm,
      const QPointF &p) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWin32PrintEngineCall7 call = reinterpret_cast<CuteQWin32PrintEngineCall7>(taken[7]);
      call(this, &r, &pm, &p, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::drawTiledPixmap(r, pm, p);
  }

  //  void QWin32PrintEngine::setProperty(PrintEnginePropertyKey key, const
  //      QVariant &value)
  void setProperty(QPrintEngine::PrintEnginePropertyKey key,
      const QVariant &value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWin32PrintEngineCall8 call = reinterpret_cast<CuteQWin32PrintEngineCall8>(taken[8]);
      call(this, static_cast<int>(key), &value, &handled);
      if (handled) return;
    }
    QWin32PrintEngine::setProperty(key, value);
  }

  //  QVariant QWin32PrintEngine::property(PrintEnginePropertyKey key) const
  QVariant property(QPrintEngine::PrintEnginePropertyKey key) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWin32PrintEngineCall9 call = reinterpret_cast<CuteQWin32PrintEngineCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QWin32PrintEngine::property(key);
  }

  //  bool QWin32PrintEngine::newPage()
  bool newPage() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWin32PrintEngineCall10 call = reinterpret_cast<CuteQWin32PrintEngineCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWin32PrintEngine::newPage();
  }

  //  bool QWin32PrintEngine::abort()
  bool abort() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWin32PrintEngineCall11 call = reinterpret_cast<CuteQWin32PrintEngineCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWin32PrintEngine::abort();
  }

  //  int QWin32PrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQWin32PrintEngineCall12 call = reinterpret_cast<CuteQWin32PrintEngineCall12>(taken[12]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWin32PrintEngine::metric(a0);
  }

  //  QPrinter::PrinterState QWin32PrintEngine::printerState() const
  QPrinter::PrinterState printerState() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQWin32PrintEngineCall13 call = reinterpret_cast<CuteQWin32PrintEngineCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrinter::PrinterState>(given);
    }
    return QWin32PrintEngine::printerState();
  }

  //  QPaintEngine::Type QWin32PrintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQWin32PrintEngineCall14 call = reinterpret_cast<CuteQWin32PrintEngineCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QWin32PrintEngine::type();
  }

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWin32PrintEngineCall15 call = reinterpret_cast<CuteQWin32PrintEngineCall15>(taken[15]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWin32PrintEngineCall16 call = reinterpret_cast<CuteQWin32PrintEngineCall16>(taken[16]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWin32PrintEngineCall17 call = reinterpret_cast<CuteQWin32PrintEngineCall17>(taken[17]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWin32PrintEngineCall18 call = reinterpret_cast<CuteQWin32PrintEngineCall18>(taken[18]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWin32PrintEngineCall19 call = reinterpret_cast<CuteQWin32PrintEngineCall19>(taken[19]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWin32PrintEngineCall20 call = reinterpret_cast<CuteQWin32PrintEngineCall20>(taken[20]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWin32PrintEngineCall21 call = reinterpret_cast<CuteQWin32PrintEngineCall21>(taken[21]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWin32PrintEngineCall22 call = reinterpret_cast<CuteQWin32PrintEngineCall22>(taken[22]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPolygon(const QPoint *points, int pointCount,
  //      PolygonDrawMode mode)
  void drawPolygon(const QPoint *points, int pointCount,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWin32PrintEngineCall23 call = reinterpret_cast<CuteQWin32PrintEngineCall23>(taken[23]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  void QPaintEngine::drawImage(const QRectF &r, const QImage &pm, const
  //      QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(const QRectF &r, const QImage &pm, const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWin32PrintEngineCall24 call = reinterpret_cast<CuteQWin32PrintEngineCall24>(taken[24]);
      call(this, &r, &pm, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPaintEngine::drawImage(r, pm, sr, flags);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQWin32PrintEngineCall25 call = reinterpret_cast<CuteQWin32PrintEngineCall25>(taken[25]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWin32PrintEngineCall26 call = reinterpret_cast<CuteQWin32PrintEngineCall26>(taken[26]);
      const QPixmap * given = call(this, &size, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmap(size);
  }

  //  QPixmap QPaintEngine::createPixmapFromImage(QImage image,
  //      Qt::ImageConversionFlags flags)
  QPixmap createPixmapFromImage(QImage image,
      Qt::ImageConversionFlags flags) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWin32PrintEngineCall27 call = reinterpret_cast<CuteQWin32PrintEngineCall27>(taken[27]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QWin32PrintEngine::QWin32PrintEngine(QPrinter::PrinterMode mode, const
//      QString &deviceId)
extern "C" Q_DECL_EXPORT
QWin32PrintEngine *ritual_ZN17QWin32PrintEngineC1EN8QPrinter11PrinterModeERK7QString(
    QPrinter::PrinterMode mode,
    const QString *deviceId) {
  return new CuteQWin32PrintEngine(mode, *deviceId);
}

//  QWin32PrintEngine::~QWin32PrintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngineD1Ev(QWin32PrintEngine *self) {
  delete self;
}

//  bool QWin32PrintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWin32PrintEngine5beginEP12QPaintDevice(
    QWin32PrintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QWin32PrintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWin32PrintEngine3endEv(QWin32PrintEngine *self) {
  return self->end();
}

//  void QWin32PrintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine11updateStateERK17QPaintEngineState(
    QWin32PrintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QWin32PrintEngine::updateMatrix(const QTransform &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine12updateMatrixERK10QTransform(
    QWin32PrintEngine *self,
    const QTransform *matrix) {
  self->updateMatrix(*matrix);
}

//  void QWin32PrintEngine::updateClipPath(const QPainterPath &clip,
//      Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine14updateClipPathERK12QPainterPathN2Qt13ClipOperationE(
    QWin32PrintEngine *self,
    const QPainterPath *clip,
    Qt::ClipOperation op) {
  self->updateClipPath(*clip, op);
}

//  void QWin32PrintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine8drawPathERK12QPainterPath(
    QWin32PrintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QWin32PrintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QWin32PrintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QWin32PrintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QWin32PrintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QWin32PrintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QWin32PrintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QWin32PrintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QWin32PrintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QWin32PrintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QWin32PrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->setProperty(key, *value);
}

//  QVariant QWin32PrintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QWin32PrintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QWin32PrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->property(key));
}

//  bool QWin32PrintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWin32PrintEngine7newPageEv(QWin32PrintEngine *self) {
  return self->newPage();
}

//  bool QWin32PrintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWin32PrintEngine5abortEv(QWin32PrintEngine *self) {
  return self->abort();
}

//  int QWin32PrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QWin32PrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QWin32PrintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  QPrinter::PrinterState QWin32PrintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK17QWin32PrintEngine12printerStateEv(
    const QWin32PrintEngine *self) {
  return self->printerState();
}

//  QPaintEngine::Type QWin32PrintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK17QWin32PrintEngine4typeEv(
    const QWin32PrintEngine *self) {
  return self->type();
}

//  HDC QWin32PrintEngine::getDC() const
extern "C" Q_DECL_EXPORT
HDC ritual_ZNK17QWin32PrintEngine5getDCEv(const QWin32PrintEngine *self) {
  return self->getDC();
}

//  void QWin32PrintEngine::releaseDC(HDC a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QWin32PrintEngine9releaseDCEP5HDC__(
    const QWin32PrintEngine *self,
    HDC a0) {
  self->releaseDC(a0);
}

//  void QWin32PrintEngine::setGlobalDevMode(HGLOBAL globalDevNames, HGLOBAL
//      globalDevMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWin32PrintEngine16setGlobalDevModeEPvS0_(
    QWin32PrintEngine *self,
    HGLOBAL globalDevNames,
    HGLOBAL globalDevMode) {
  self->setGlobalDevMode(globalDevNames, globalDevMode);
}

//  HGLOBAL *QWin32PrintEngine::createGlobalDevNames()
extern "C" Q_DECL_EXPORT
HGLOBAL *ritual_ZN17QWin32PrintEngine20createGlobalDevNamesEv(
    QWin32PrintEngine *self) {
  return self->createGlobalDevNames();
}

//  HGLOBAL QWin32PrintEngine::globalDevMode()
extern "C" Q_DECL_EXPORT
HGLOBAL ritual_ZN17QWin32PrintEngine13globalDevModeEv(
    QWin32PrintEngine *self) {
  return self->globalDevMode();
}

//  QWin32PrintEnginePrivate *QWin32PrintEngine::d_func()
extern "C" Q_DECL_EXPORT
QWin32PrintEnginePrivate *ritual_ZN17QWin32PrintEngine6d_funcEv(
    QWin32PrintEngine *self) {
  return self->d_func();
}

//  const QWin32PrintEnginePrivate *QWin32PrintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QWin32PrintEnginePrivate *ritual_ZNK17QWin32PrintEngine6d_funcEv(
    const QWin32PrintEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWin32PrintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWin32PrintEngine(
    QWin32PrintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWin32PrintEngine *>(self)->take(key, call);
}

//  bool QWin32PrintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QWin32PrintEngine5beginEP12QPaintDevice(
    QWin32PrintEngine *self,
    QPaintDevice *pdev) {
  return self->QWin32PrintEngine::begin(pdev);
}

//  bool QWin32PrintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QWin32PrintEngine3endEv(QWin32PrintEngine *self) {
  return self->QWin32PrintEngine::end();
}

//  void QWin32PrintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine11updateStateERK17QPaintEngineState(
    QWin32PrintEngine *self,
    const QPaintEngineState *state) {
  self->QWin32PrintEngine::updateState(*state);
}

//  void QWin32PrintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine8drawPathERK12QPainterPath(
    QWin32PrintEngine *self,
    const QPainterPath *path) {
  self->QWin32PrintEngine::drawPath(*path);
}

//  void QWin32PrintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QWin32PrintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QWin32PrintEngine::drawPolygon(points, pointCount, mode);
}

//  void QWin32PrintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QWin32PrintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QWin32PrintEngine::drawTextItem(*p, *textItem);
}

//  void QWin32PrintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QWin32PrintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QWin32PrintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QWin32PrintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QWin32PrintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->QWin32PrintEngine::drawTiledPixmap(*r, *pixmap, *s);
}

//  void QWin32PrintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QWin32PrintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QWin32PrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->QWin32PrintEngine::setProperty(key, *value);
}

//  QVariant QWin32PrintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QWin32PrintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QWin32PrintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->QWin32PrintEngine::property(key));
}

//  bool QWin32PrintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QWin32PrintEngine7newPageEv(QWin32PrintEngine *self) {
  return self->QWin32PrintEngine::newPage();
}

//  bool QWin32PrintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QWin32PrintEngine5abortEv(QWin32PrintEngine *self) {
  return self->QWin32PrintEngine::abort();
}

//  int QWin32PrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QWin32PrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QWin32PrintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->QWin32PrintEngine::metric(a0);
}

//  QPrinter::PrinterState QWin32PrintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_own_ZNK17QWin32PrintEngine12printerStateEv(
    const QWin32PrintEngine *self) {
  return self->QWin32PrintEngine::printerState();
}

//  QPaintEngine::Type QWin32PrintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK17QWin32PrintEngine4typeEv(
    const QWin32PrintEngine *self) {
  return self->QWin32PrintEngine::type();
}

#endif  // defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
