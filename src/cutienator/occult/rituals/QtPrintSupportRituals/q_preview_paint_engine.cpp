//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_preview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(printpreviewwidget)
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
#include <QtCore/QList>
#include <QtGui/QPicture>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/private/qpaintengine_preview_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qpaintengine_p.h>
#include <QtGui/private/qpicture_p.h>
#include <QtPrintSupport/qprintengine.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpicture.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 16, as local:qpaintengine_preview.cpp:QPreviewPaintEnginePrivate
class QPreviewPaintEnginePrivate : public QPaintEnginePrivate
{
    Q_DECLARE_PUBLIC(QPreviewPaintEngine)
public:
    QPreviewPaintEnginePrivate() : state(QPrinter::Idle) {}
    ~QPreviewPaintEnginePrivate() {}

    QList<const QPicture *> pages;
    QPaintEngine *engine;
    QPainter *painter;
    QPrinter::PrinterState state;

    QPaintEngine *proxy_paint_engine;
    QPrintEngine *proxy_print_engine;
};

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 48, as _ZN19QPreviewPaintEngine5beginEP12QPaintDevice
inline bool QPreviewPaintEngine::begin(QPaintDevice *)
{
    Q_D(QPreviewPaintEngine);

    qDeleteAll(d->pages);
    d->pages.clear();

    QPicture *page = new QPicture;
    page->d_func()->in_memory_only = true;
    d->painter = new QPainter(page);
    d->engine = d->painter->paintEngine();
    *d->painter->d_func()->state = *painter()->d_func()->state;
    d->pages.append(page);
    d->state = QPrinter::Active;
    return true;
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 65, as _ZN19QPreviewPaintEngine3endEv
inline bool QPreviewPaintEngine::end()
{
    Q_D(QPreviewPaintEngine);

    delete d->painter;
    d->painter = nullptr;
    d->engine = nullptr;
    d->state = QPrinter::Idle;
    return true;
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 76, as _ZN19QPreviewPaintEngine11updateStateERK17QPaintEngineState
inline void QPreviewPaintEngine::updateState(const QPaintEngineState &state)
{
    Q_D(QPreviewPaintEngine);
    d->engine->updateState(state);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 82, as _ZN19QPreviewPaintEngine8drawPathERK12QPainterPath
inline void QPreviewPaintEngine::drawPath(const QPainterPath &path)
{
    Q_D(QPreviewPaintEngine);
    d->engine->drawPath(path);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 88, as _ZN19QPreviewPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE
inline void QPreviewPaintEngine::drawPolygon(const QPointF *points, int pointCount, PolygonDrawMode mode)
{
    Q_D(QPreviewPaintEngine);
    d->engine->drawPolygon(points, pointCount, mode);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 94, as _ZN19QPreviewPaintEngine12drawTextItemERK7QPointFRK9QTextItem
inline void QPreviewPaintEngine::drawTextItem(const QPointF &p, const QTextItem &textItem)
{
    Q_D(QPreviewPaintEngine);
    d->engine->drawTextItem(p, textItem);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 100, as _ZN19QPreviewPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_
inline void QPreviewPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm, const QRectF &sr)
{
    Q_D(QPreviewPaintEngine);
    d->engine->drawPixmap(r, pm, sr);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 106, as _ZN19QPreviewPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF
inline void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap &pm, const QPointF &p)
{
    Q_D(QPreviewPaintEngine);
    d->engine->drawTiledPixmap(r, pm, p);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 160, as _ZN19QPreviewPaintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant
inline void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey key, const QVariant &value)
{
    Q_D(QPreviewPaintEngine);
    d->proxy_print_engine->setProperty(key, value);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 166, as _ZNK19QPreviewPaintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE
inline QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey key) const
{
    Q_D(const QPreviewPaintEngine);
    return d->proxy_print_engine->property(key);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 112, as _ZN19QPreviewPaintEngine7newPageEv
inline bool QPreviewPaintEngine::newPage()
{
    Q_D(QPreviewPaintEngine);

    QPicture *page = new QPicture;
    page->d_func()->in_memory_only = true;
    QPainter *tmp_painter = new QPainter(page);
    QPaintEngine *tmp_engine = tmp_painter->paintEngine();

    // copy the painter state from the original painter
    Q_ASSERT(painter()->d_func()->state && tmp_painter->d_func()->state);
    *tmp_painter->d_func()->state = *painter()->d_func()->state;

    // composition modes aren't supported on a QPrinter and yields a
    // warning, so ignore it for now
    tmp_engine->setDirty(DirtyFlags(AllDirty & ~DirtyCompositionMode));
    tmp_engine->syncState();

    delete d->painter;
    d->painter = tmp_painter;
    d->pages.append(page);
    d->engine = tmp_engine;
    return true;
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 137, as _ZN19QPreviewPaintEngine5abortEv
inline bool QPreviewPaintEngine::abort()
{
    Q_D(QPreviewPaintEngine);
    end();
    qDeleteAll(d->pages);
    d->state = QPrinter::Aborted;

    return true;
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 172, as _ZNK19QPreviewPaintEngine6metricEN12QPaintDevice17PaintDeviceMetricE
inline int QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric id) const
{
    Q_D(const QPreviewPaintEngine);
    return d->proxy_print_engine->metric(id);
}

//  from src/printsupport/kernel/qpaintengine_preview.cpp, line 178, as _ZNK19QPreviewPaintEngine12printerStateEv
inline QPrinter::PrinterState QPreviewPaintEngine::printerState() const
{
    Q_D(const QPreviewPaintEngine);
    return d->state;
}
//  -----------------------------------------------------------------------

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

//  QPreviewPaintEnginePrivate *QPreviewPaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QPreviewPaintEnginePrivate *ritual_ZN19QPreviewPaintEngine6d_funcEv(
    QPreviewPaintEngine *self) {
  return self->d_func();
}

//  const QPreviewPaintEnginePrivate *QPreviewPaintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QPreviewPaintEnginePrivate *ritual_ZNK19QPreviewPaintEngine6d_funcEv(
    const QPreviewPaintEngine *self) {
  return self->d_func();
}

//  bool QPreviewPaintEngine::begin(QPaintDevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPreviewPaintEngine5beginEP12QPaintDevice(
    QPreviewPaintEngine *self,
    QPaintDevice *dev) {
  return self->begin(dev);
}

//  bool QPreviewPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPreviewPaintEngine3endEv(QPreviewPaintEngine *self) {
  return self->end();
}

//  void QPreviewPaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine11updateStateERK17QPaintEngineState(
    QPreviewPaintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QPreviewPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine8drawPathERK12QPainterPath(
    QPreviewPaintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPreviewPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPreviewPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPreviewPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPreviewPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QPreviewPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPreviewPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPreviewPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *p) {
  self->drawTiledPixmap(*r, *pm, *p);
}

//  QPaintEngine::Type QPreviewPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK19QPreviewPaintEngine4typeEv(
    const QPreviewPaintEngine *self) {
  return self->type();
}

//  void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPreviewPaintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QPreviewPaintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->setProperty(key, *value);
}

//  QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QPreviewPaintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QPreviewPaintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->property(key));
}

//  bool QPreviewPaintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPreviewPaintEngine7newPageEv(QPreviewPaintEngine *self) {
  return self->newPage();
}

//  bool QPreviewPaintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPreviewPaintEngine5abortEv(QPreviewPaintEngine *self) {
  return self->abort();
}

//  int QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPreviewPaintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPreviewPaintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  QPrinter::PrinterState QPreviewPaintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_ZNK19QPreviewPaintEngine12printerStateEv(
    const QPreviewPaintEngine *self) {
  return self->printerState();
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

//  bool QPreviewPaintEngine::begin(QPaintDevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QPreviewPaintEngine5beginEP12QPaintDevice(
    QPreviewPaintEngine *self,
    QPaintDevice *dev) {
  return self->QPreviewPaintEngine::begin(dev);
}

//  bool QPreviewPaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QPreviewPaintEngine3endEv(QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::end();
}

//  void QPreviewPaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine11updateStateERK17QPaintEngineState(
    QPreviewPaintEngine *self,
    const QPaintEngineState *state) {
  self->QPreviewPaintEngine::updateState(*state);
}

//  void QPreviewPaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine8drawPathERK12QPainterPath(
    QPreviewPaintEngine *self,
    const QPainterPath *path) {
  self->QPreviewPaintEngine::drawPath(*path);
}

//  void QPreviewPaintEngine::drawPolygon(const QPointF *points, int
//      pointCount, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPreviewPaintEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPreviewPaintEngine::drawPolygon(points, pointCount, mode);
}

//  void QPreviewPaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPreviewPaintEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QPreviewPaintEngine::drawTextItem(*p, *textItem);
}

//  void QPreviewPaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPreviewPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->QPreviewPaintEngine::drawPixmap(*r, *pm, *sr);
}

//  void QPreviewPaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pm, const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPreviewPaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QPointF *p) {
  self->QPreviewPaintEngine::drawTiledPixmap(*r, *pm, *p);
}

//  QPaintEngine::Type QPreviewPaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK19QPreviewPaintEngine4typeEv(
    const QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::type();
}

//  void QPreviewPaintEngine::setProperty(PrintEnginePropertyKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPreviewPaintEngine11setPropertyEN12QPrintEngine22PrintEnginePropertyKeyERK8QVariant(
    QPreviewPaintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key,
    const QVariant *value) {
  self->QPreviewPaintEngine::setProperty(key, *value);
}

//  QVariant QPreviewPaintEngine::property(PrintEnginePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QPreviewPaintEngine8propertyEN12QPrintEngine22PrintEnginePropertyKeyE(
    const QPreviewPaintEngine *self,
    QPrintEngine::PrintEnginePropertyKey key) {
  return new QVariant(self->QPreviewPaintEngine::property(key));
}

//  bool QPreviewPaintEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QPreviewPaintEngine7newPageEv(
    QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::newPage();
}

//  bool QPreviewPaintEngine::abort()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QPreviewPaintEngine5abortEv(QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::abort();
}

//  int QPreviewPaintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QPreviewPaintEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPreviewPaintEngine *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->QPreviewPaintEngine::metric(a0);
}

//  QPrinter::PrinterState QPreviewPaintEngine::printerState() const
extern "C" Q_DECL_EXPORT
QPrinter::PrinterState ritual_own_ZNK19QPreviewPaintEngine12printerStateEv(
    const QPreviewPaintEngine *self) {
  return self->QPreviewPaintEngine::printerState();
}

//  a QList<const QPicture *> a ritual of QPreviewPaintEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPreviewPaintEngine__QList_const_QPicture(
    QList<const QPicture *> *self) {
  delete self;
}

#endif  // QT_CONFIG(printpreviewwidget)
#endif  // QT_CONFIG(printpreviewwidget)
