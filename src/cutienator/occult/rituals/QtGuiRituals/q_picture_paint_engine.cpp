//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_pic_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PICTURE)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_pic_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpaintengine_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qpicture_p.h>
#include <QtGui/private/qfont_p.h>
#ifndef QT_NO_PICTURE
#include <QtCore/qbuffer.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qpaintengine_pic_p.h>
#include <QtGui/qpicture.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qrect.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/qdebug.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qpaintengine_pic.cpp, line 28, as local:qpaintengine_pic.cpp:QPicturePaintEnginePrivate
#if !defined(QT_NO_PICTURE)
class QPicturePaintEnginePrivate : public QPaintEnginePrivate
{
    Q_DECLARE_PUBLIC(QPicturePaintEngine)
public:
    QDataStream s;
    QPainter *pt;
    QPicturePrivate *pic_d;
    bool sizeLimitExceeded = false;
};
#endif  // !defined(QT_NO_PICTURE)

//  from src/gui/image/qpaintengine_pic.cpp, line 56, as _ZN19QPicturePaintEngine5beginEP12QPaintDevice
#if !defined(QT_NO_PICTURE)
inline bool QPicturePaintEngine::begin(QPaintDevice *pd)
{
    Q_D(QPicturePaintEngine);
#ifdef QT_PICTURE_DEBUG
    qDebug("QPicturePaintEngine::begin()");
#endif
    Q_ASSERT(pd);
    QPicture *pic = static_cast<QPicture *>(pd);

    d->pdev = pd;
    d->pic_d = pic->d_func();
    Q_ASSERT(d->pic_d);

    d->s.setDevice(&d->pic_d->pictb);
    d->s.setVersion(d->pic_d->formatMajor);

    d->pic_d->pictb.open(QIODevice::WriteOnly | QIODevice::Truncate);
    d->sizeLimitExceeded = false;
    d->s.writeRawData(qt_mfhdr_tag, 4);
    d->s << (quint16) 0 << (quint16) d->pic_d->formatMajor << (quint16) d->pic_d->formatMinor;
    d->s << (quint8) QPicturePrivate::PdcBegin << (quint8) sizeof(qint32);
    d->pic_d->brect = QRect();
    if (d->pic_d->formatMajor >= 4) {
        QRect r = pic->boundingRect();
        d->s << (qint32) r.left() << (qint32) r.top() << (qint32) r.width()
             << (qint32) r.height();
    }
    d->pic_d->trecs = 0;
    d->s << (quint32)d->pic_d->trecs; // total number of records
    d->pic_d->formatOk = false;
    setActive(true);
    return true;
}
#endif  // !defined(QT_NO_PICTURE)

//  from src/gui/image/qpaintengine_pic.cpp, line 90, as _ZN19QPicturePaintEngine3endEv
#if !defined(QT_NO_PICTURE)
inline bool QPicturePaintEngine::end()
{
    Q_D(QPicturePaintEngine);
#ifdef QT_PICTURE_DEBUG
    qDebug("QPicturePaintEngine::end()");
#endif
    d->pic_d->trecs++;
    d->s << (quint8) QPicturePrivate::PdcEnd << (quint8) 0;
    int cs_start = sizeof(quint32);                // pos of checksum word
    int data_start = cs_start + sizeof(quint16);
    int brect_start = data_start + 2*sizeof(qint16) + 2*sizeof(quint8);
    int pos = d->pic_d->pictb.pos();
    d->pic_d->pictb.seek(brect_start);
    if (d->pic_d->formatMajor >= 4) { // bounding rectangle
        QRect r = static_cast<QPicture *>(d->pdev)->boundingRect();
        d->s << (qint32) r.left() << (qint32) r.top() << (qint32) r.width()
             << (qint32) r.height();
    }
    d->s << (quint32) d->pic_d->trecs;                        // write number of records
    d->pic_d->pictb.seek(cs_start);
    const QByteArray buf = d->pic_d->pictb.buffer();
    quint16 cs = (quint16) qChecksum(QByteArrayView(buf.constData() + data_start, pos - data_start));
    d->s << cs;                                // write checksum
    d->pic_d->pictb.close();
    setActive(false);
    return !d->sizeLimitExceeded;
}
#endif  // !defined(QT_NO_PICTURE)

//  from src/gui/image/qpaintengine_pic.cpp, line 505, as _ZN19QPicturePaintEngine11updateStateERK17QPaintEngineState
#if !defined(QT_NO_PICTURE)
inline void QPicturePaintEngine::updateState(const QPaintEngineState &state)
{
    QPaintEngine::DirtyFlags flags = state.state();
    if (flags & DirtyPen) updatePen(state.pen());
    if (flags & DirtyBrush) updateBrush(state.brush());
    if (flags & DirtyBrushOrigin) updateBrushOrigin(state.brushOrigin());
    if (flags & DirtyFont) updateFont(state.font());
    if (flags & DirtyBackground) updateBackground(state.backgroundMode(), state.backgroundBrush());
    if (flags & DirtyTransform) updateMatrix(state.transform());
    if (flags & DirtyClipEnabled) updateClipEnabled(state.isClipEnabled());
    if (flags & DirtyClipRegion) updateClipRegion(state.clipRegion(), state.clipOperation());
    if (flags & DirtyClipPath) updateClipPath(state.clipPath(), state.clipOperation());
    if (flags & DirtyHints) updateRenderHints(state.renderHints());
    if (flags & DirtyCompositionMode) updateCompositionMode(state.compositionMode());
    if (flags & DirtyOpacity) updateOpacity(state.opacity());
}
#endif  // !defined(QT_NO_PICTURE)

//  from src/gui/image/qpaintengine_pic.cpp, line 52, as _ZN19QPicturePaintEngineD1Ev
#if !defined(QT_NO_PICTURE)
inline QPicturePaintEngine::~QPicturePaintEngine()
{
}
#endif  // !defined(QT_NO_PICTURE)
//  -----------------------------------------------------------------------

//  A QPicturePaintEngine that Python can take functions over in. Every QPicturePaintEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PICTURE)
typedef bool (*CuteQPicturePaintEngineCall0)(const void *, QPaintDevice *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef bool (*CuteQPicturePaintEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall2)(const void *, const QPaintEngineState *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall3)(const void *, const QRectF *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall4)(const void *, const QPainterPath *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall5)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall6)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall7)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall8)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall9)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
typedef int (*CuteQPicturePaintEngineCall10)(const void *, int *);
#endif  // !defined(QT_NO_PICTURE)
typedef void (*CuteQPicturePaintEngineCall11)(const void *, const QRect *, int, int *);
typedef void (*CuteQPicturePaintEngineCall12)(const void *, const QRectF *, int, int *);
typedef void (*CuteQPicturePaintEngineCall13)(const void *, const QLine *, int, int *);
typedef void (*CuteQPicturePaintEngineCall14)(const void *, const QLineF *, int, int *);
typedef void (*CuteQPicturePaintEngineCall15)(const void *, const QRect *, int *);
typedef void (*CuteQPicturePaintEngineCall16)(const void *, const QPointF *, int, int *);
typedef void (*CuteQPicturePaintEngineCall17)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPicturePaintEngineCall18)(const void *, const QPoint *, int, int, int *);
typedef const QPoint * (*CuteQPicturePaintEngineCall19)(const void *, int *);
typedef const QPixmap * (*CuteQPicturePaintEngineCall20)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQPicturePaintEngineCall21)(const void *, const QImage *, int, int *);
class CuteQPicturePaintEngine : public QPicturePaintEngine {
public:
  using QPicturePaintEngine::QPicturePaintEngine;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
#if !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_PICTURE)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK6QPointi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK6QPointiNS_15PolygonDrawModeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintEngine16coordinateOffsetEv")) {
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

#if !defined(QT_NO_PICTURE)
  //  bool QPicturePaintEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPicturePaintEngineCall0 call = reinterpret_cast<CuteQPicturePaintEngineCall0>(taken[0]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QPicturePaintEngine::begin(pdev);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  bool QPicturePaintEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPicturePaintEngineCall1 call = reinterpret_cast<CuteQPicturePaintEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPicturePaintEngine::end();
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPicturePaintEngineCall2 call = reinterpret_cast<CuteQPicturePaintEngineCall2>(taken[2]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::updateState(state);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawEllipse(const QRectF &rect)
  void drawEllipse(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPicturePaintEngineCall3 call = reinterpret_cast<CuteQPicturePaintEngineCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawEllipse(rect);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPicturePaintEngineCall4 call = reinterpret_cast<CuteQPicturePaintEngineCall4>(taken[4]);
      call(this, &path, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawPath(path);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawPolygon(const QPointF *points, int
  //      numPoints, PolygonDrawMode mode)
  void drawPolygon(
      const QPointF *points,
      int numPoints,
      QPaintEngine::PolygonDrawMode mode) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPicturePaintEngineCall5 call = reinterpret_cast<CuteQPicturePaintEngineCall5>(taken[5]);
      call(this, points, numPoints, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawPolygon(points, numPoints, mode);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawPixmap(const QRectF &r, const QPixmap
  //      &pm, const QRectF &sr)
  void drawPixmap(
      const QRectF &r,
      const QPixmap &pm,
      const QRectF &sr) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPicturePaintEngineCall6 call = reinterpret_cast<CuteQPicturePaintEngineCall6>(taken[6]);
      call(this, &r, &pm, &sr, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawPixmap(r, pm, sr);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawTiledPixmap(const QRectF &r, const
  //      QPixmap &pixmap, const QPointF &s)
  void drawTiledPixmap(
      const QRectF &r,
      const QPixmap &pixmap,
      const QPointF &s) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPicturePaintEngineCall7 call = reinterpret_cast<CuteQPicturePaintEngineCall7>(taken[7]);
      call(this, &r, &pixmap, &s, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawTiledPixmap(r, pixmap, s);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawImage(const QRectF &r, const QImage
  //      &image, const QRectF &sr, Qt::ImageConversionFlags flags)
  void drawImage(
      const QRectF &r,
      const QImage &image,
      const QRectF &sr,
      Qt::ImageConversionFlags flags) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPicturePaintEngineCall8 call = reinterpret_cast<CuteQPicturePaintEngineCall8>(taken[8]);
      call(this, &r, &image, &sr, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawImage(r, image, sr, flags);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  void QPicturePaintEngine::drawTextItem(const QPointF &p, const
  //      QTextItem &ti)
  void drawTextItem(const QPointF &p, const QTextItem &ti) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPicturePaintEngineCall9 call = reinterpret_cast<CuteQPicturePaintEngineCall9>(taken[9]);
      call(this, &p, &ti, &handled);
      if (handled) return;
    }
    QPicturePaintEngine::drawTextItem(p, ti);
  }
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
  //  Type QPicturePaintEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPicturePaintEngineCall10 call = reinterpret_cast<CuteQPicturePaintEngineCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QPicturePaintEngine::type();
  }
#endif  // !defined(QT_NO_PICTURE)

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPicturePaintEngineCall11 call = reinterpret_cast<CuteQPicturePaintEngineCall11>(taken[11]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPicturePaintEngineCall12 call = reinterpret_cast<CuteQPicturePaintEngineCall12>(taken[12]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPicturePaintEngineCall13 call = reinterpret_cast<CuteQPicturePaintEngineCall13>(taken[13]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPicturePaintEngineCall14 call = reinterpret_cast<CuteQPicturePaintEngineCall14>(taken[14]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPicturePaintEngineCall15 call = reinterpret_cast<CuteQPicturePaintEngineCall15>(taken[15]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPicturePaintEngineCall16 call = reinterpret_cast<CuteQPicturePaintEngineCall16>(taken[16]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawPoints(points, pointCount);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPicturePaintEngineCall17 call = reinterpret_cast<CuteQPicturePaintEngineCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQPicturePaintEngineCall18 call = reinterpret_cast<CuteQPicturePaintEngineCall18>(taken[18]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPicturePaintEngineCall19 call = reinterpret_cast<CuteQPicturePaintEngineCall19>(taken[19]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPicturePaintEngineCall20 call = reinterpret_cast<CuteQPicturePaintEngineCall20>(taken[20]);
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
      CuteQPicturePaintEngineCall21 call = reinterpret_cast<CuteQPicturePaintEngineCall21>(taken[21]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QPicturePaintEnginePrivate *QPicturePaintEngine::d_func()
extern "C" Q_DECL_EXPORT
QPicturePaintEnginePrivate *ritual_ZN19QPicturePaintEngine6d_funcEv(
    QPicturePaintEngine *self) {
  return self->d_func();
}

//  const QPicturePaintEnginePrivate *QPicturePaintEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QPicturePaintEnginePrivate *ritual_ZNK19QPicturePaintEngine6d_funcEv(
    const QPicturePaintEngine *self) {
  return self->d_func();
}

//  QPicturePaintEngine::~QPicturePaintEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngineD1Ev(QPicturePaintEngine *self) {
  delete self;
}

//  bool QPicturePaintEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPicturePaintEngine5beginEP12QPaintDevice(
    QPicturePaintEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QPicturePaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QPicturePaintEngine3endEv(QPicturePaintEngine *self) {
  return self->end();
}

//  void QPicturePaintEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine11updateStateERK17QPaintEngineState(
    QPicturePaintEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  void QPicturePaintEngine::drawEllipse(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine11drawEllipseERK6QRectF(
    QPicturePaintEngine *self,
    const QRectF *rect) {
  self->drawEllipse(*rect);
}

//  void QPicturePaintEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine8drawPathERK12QPainterPath(
    QPicturePaintEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPicturePaintEngine::drawPolygon(const QPointF *points, int
//      numPoints, PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPicturePaintEngine *self,
    const QPointF *points,
    int numPoints,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, numPoints, mode);
}

//  void QPicturePaintEngine::drawPixmap(const QRectF &r, const QPixmap &pm,
//      const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPicturePaintEngine *self,
    const QRectF *r,
    const QPixmap *pm,
    const QRectF *sr) {
  self->drawPixmap(*r, *pm, *sr);
}

//  void QPicturePaintEngine::drawTiledPixmap(const QRectF &r, const QPixmap
//      &pixmap, const QPointF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPicturePaintEngine *self,
    const QRectF *r,
    const QPixmap *pixmap,
    const QPointF *s) {
  self->drawTiledPixmap(*r, *pixmap, *s);
}

//  void QPicturePaintEngine::drawImage(const QRectF &r, const QImage &image,
//      const QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPicturePaintEngine *self,
    const QRectF *r,
    const QImage *image,
    const QRectF *sr,
    int flags) {
  self->drawImage(
      *r,
      *image,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPicturePaintEngine::drawTextItem(const QPointF &p, const QTextItem
//      &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPicturePaintEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPicturePaintEngine *self,
    const QPointF *p,
    const QTextItem *ti) {
  self->drawTextItem(*p, *ti);
}

//  Type QPicturePaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK19QPicturePaintEngine4typeEv(
    const QPicturePaintEngine *self) {
  return self->type();
}

//  a Python function taken by a CuteQPicturePaintEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPicturePaintEngine(
    QPicturePaintEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPicturePaintEngine *>(self)->take(key, call);
}

#if !defined(QT_NO_PICTURE)
//  bool QPicturePaintEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QPicturePaintEngine3endEv(QPicturePaintEngine *self) {
  return self->QPicturePaintEngine::end();
}
#endif  // !defined(QT_NO_PICTURE)

//  Type QPicturePaintEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK19QPicturePaintEngine4typeEv(
    const QPicturePaintEngine *self) {
  return self->QPicturePaintEngine::type();
}

#endif  // !defined(QT_NO_PICTURE)
