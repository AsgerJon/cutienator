//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PDF)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qimage.h>
#include <QtCore/qurl.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPdfEngine that Python can take functions over in. Every QPdfEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PDF)
typedef bool (*CuteQPdfEngineCall0)(const void *, QPaintDevice *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef bool (*CuteQPdfEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall2)(const void *, const QPointF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall3)(const void *, const QLineF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall4)(const void *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall5)(const void *, const QPointF *, int, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall6)(const void *, const QPainterPath *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall7)(const void *, const QPointF *, const QTextItem *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall8)(const void *, const QRectF *, const QPixmap *, const QRectF *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall9)(const void *, const QRectF *, const QImage *, const QRectF *, int, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall10)(const void *, const QRectF *, const QPixmap *, const QPointF *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall11)(const void *, const QPaintEngineState *, int *);
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
typedef int (*CuteQPdfEngineCall12)(const void *, int *);
#endif  // !defined(QT_NO_PDF)
typedef void (*CuteQPdfEngineCall13)(const void *, const QRect *, int, int *);
typedef void (*CuteQPdfEngineCall14)(const void *, const QLine *, int, int *);
typedef void (*CuteQPdfEngineCall15)(const void *, const QRectF *, int *);
typedef void (*CuteQPdfEngineCall16)(const void *, const QRect *, int *);
typedef void (*CuteQPdfEngineCall17)(const void *, const QPoint *, int, int *);
typedef void (*CuteQPdfEngineCall18)(const void *, const QPoint *, int, int, int *);
typedef const QPoint * (*CuteQPdfEngineCall19)(const void *, int *);
typedef const QPixmap * (*CuteQPdfEngineCall20)(const void *, const QSize *, int *);
typedef const QPixmap * (*CuteQPdfEngineCall21)(const void *, const QImage *, int, int *);
class CuteQPdfEngine : public QPdfEngine {
public:
  using QPdfEngine::QPdfEngine;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine5beginEP12QPaintDevice")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine3endEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPointsEPK7QPointFi")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK6QLineFi")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK6QRectFi")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawPolygonEPK7QPointFiNS_15PolygonDrawModeE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine8drawPathERK12QPainterPath")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine12drawTextItemERK7QPointFRK9QTextItem")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine10drawPixmapERK6QRectFRK7QPixmapS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine11updateStateERK17QPaintEngineState")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
#if !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZNK12QPaintEngine4typeEv")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_PDF)
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawRectsEPK5QRecti")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine9drawLinesEPK5QLinei")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK6QRectF")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QPaintEngine11drawEllipseERK5QRect")) {
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

#if !defined(QT_NO_PDF)
  //  bool QPdfEngine::begin(QPaintDevice *pdev)
  bool begin(QPaintDevice *pdev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfEngineCall0 call = reinterpret_cast<CuteQPdfEngineCall0>(taken[0]);
      bool given = call(this, pdev, &handled);
      if (handled) return given;
    }
    return QPdfEngine::begin(pdev);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  bool QPdfEngine::end()
  bool end() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfEngineCall1 call = reinterpret_cast<CuteQPdfEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPdfEngine::end();
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPoints(const QPointF *points, int pointCount)
  void drawPoints(const QPointF *points, int pointCount) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfEngineCall2 call = reinterpret_cast<CuteQPdfEngineCall2>(taken[2]);
      call(this, points, pointCount, &handled);
      if (handled) return;
    }
    QPdfEngine::drawPoints(points, pointCount);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawLines(const QLineF *lines, int lineCount)
  void drawLines(const QLineF *lines, int lineCount) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfEngineCall3 call = reinterpret_cast<CuteQPdfEngineCall3>(taken[3]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPdfEngine::drawLines(lines, lineCount);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawRects(const QRectF *rects, int rectCount)
  void drawRects(const QRectF *rects, int rectCount) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPdfEngineCall4 call = reinterpret_cast<CuteQPdfEngineCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQPdfEngineCall5 call = reinterpret_cast<CuteQPdfEngineCall5>(taken[5]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPdfEngine::drawPolygon(points, pointCount, mode);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::drawPath(const QPainterPath &path)
  void drawPath(const QPainterPath &path) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPdfEngineCall6 call = reinterpret_cast<CuteQPdfEngineCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQPdfEngineCall7 call = reinterpret_cast<CuteQPdfEngineCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQPdfEngineCall8 call = reinterpret_cast<CuteQPdfEngineCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQPdfEngineCall9 call = reinterpret_cast<CuteQPdfEngineCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQPdfEngineCall10 call = reinterpret_cast<CuteQPdfEngineCall10>(taken[10]);
      call(this, &rectangle, &pixmap, &point, &handled);
      if (handled) return;
    }
    QPdfEngine::drawTiledPixmap(rectangle, pixmap, point);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  void QPdfEngine::updateState(const QPaintEngineState &state)
  void updateState(const QPaintEngineState &state) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPdfEngineCall11 call = reinterpret_cast<CuteQPdfEngineCall11>(taken[11]);
      call(this, &state, &handled);
      if (handled) return;
    }
    QPdfEngine::updateState(state);
  }
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
  //  Type QPdfEngine::type() const
  QPaintEngine::Type type() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPdfEngineCall12 call = reinterpret_cast<CuteQPdfEngineCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine::Type>(given);
    }
    return QPdfEngine::type();
  }
#endif  // !defined(QT_NO_PDF)

  //  void QPaintEngine::drawRects(const QRect *rects, int rectCount)
  void drawRects(const QRect *rects, int rectCount) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPdfEngineCall13 call = reinterpret_cast<CuteQPdfEngineCall13>(taken[13]);
      call(this, rects, rectCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawRects(rects, rectCount);
  }

  //  void QPaintEngine::drawLines(const QLine *lines, int lineCount)
  void drawLines(const QLine *lines, int lineCount) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPdfEngineCall14 call = reinterpret_cast<CuteQPdfEngineCall14>(taken[14]);
      call(this, lines, lineCount, &handled);
      if (handled) return;
    }
    QPaintEngine::drawLines(lines, lineCount);
  }

  //  void QPaintEngine::drawEllipse(const QRectF &r)
  void drawEllipse(const QRectF &r) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPdfEngineCall15 call = reinterpret_cast<CuteQPdfEngineCall15>(taken[15]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawEllipse(const QRect &r)
  void drawEllipse(const QRect &r) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPdfEngineCall16 call = reinterpret_cast<CuteQPdfEngineCall16>(taken[16]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QPaintEngine::drawEllipse(r);
  }

  //  void QPaintEngine::drawPoints(const QPoint *points, int pointCount)
  void drawPoints(const QPoint *points, int pointCount) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPdfEngineCall17 call = reinterpret_cast<CuteQPdfEngineCall17>(taken[17]);
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
      CuteQPdfEngineCall18 call = reinterpret_cast<CuteQPdfEngineCall18>(taken[18]);
      call(this, points, pointCount, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPaintEngine::drawPolygon(points, pointCount, mode);
  }

  //  QPoint QPaintEngine::coordinateOffset() const
  QPoint coordinateOffset() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPdfEngineCall19 call = reinterpret_cast<CuteQPdfEngineCall19>(taken[19]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::coordinateOffset();
  }

  //  QPixmap QPaintEngine::createPixmap(QSize size)
  QPixmap createPixmap(QSize size) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPdfEngineCall20 call = reinterpret_cast<CuteQPdfEngineCall20>(taken[20]);
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
      CuteQPdfEngineCall21 call = reinterpret_cast<CuteQPdfEngineCall21>(taken[21]);
      const QPixmap * given = call(this, &image, static_cast<int>(flags.toInt()), &handled);
      if (handled && given) return *given;
    }
    return QPaintEngine::createPixmapFromImage(image, flags);
  }
};

//  QPdfEnginePrivate *QPdfEngine::d_func()
extern "C" Q_DECL_EXPORT
QPdfEnginePrivate *ritual_ZN10QPdfEngine6d_funcEv(QPdfEngine *self) {
  return self->d_func();
}

//  const QPdfEnginePrivate *QPdfEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QPdfEnginePrivate *ritual_ZNK10QPdfEngine6d_funcEv(
    const QPdfEngine *self) {
  return self->d_func();
}

//  QPdfEngine::QPdfEngine()
extern "C" Q_DECL_EXPORT
QPdfEngine *ritual_ZN10QPdfEngineC1Ev() {
  return new CuteQPdfEngine();
}

//  QPdfEngine::~QPdfEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngineD1Ev(QPdfEngine *self) {
  delete self;
}

//  void QPdfEngine::setOutputFilename(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine17setOutputFilenameERK7QString(
    QPdfEngine *self,
    const QString *filename) {
  self->setOutputFilename(*filename);
}

//  void QPdfEngine::setResolution(int resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine13setResolutionEi(
    QPdfEngine *self,
    int resolution) {
  self->setResolution(resolution);
}

//  int QPdfEngine::resolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QPdfEngine10resolutionEv(const QPdfEngine *self) {
  return self->resolution();
}

//  void QPdfEngine::setPdfVersion(PdfVersion version)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine13setPdfVersionENS_10PdfVersionE(
    QPdfEngine *self,
    QPdfEngine::PdfVersion version) {
  self->setPdfVersion(version);
}

//  void QPdfEngine::setDocumentXmpMetadata(const QByteArray &xmpMetadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine22setDocumentXmpMetadataERK10QByteArray(
    QPdfEngine *self,
    const QByteArray *xmpMetadata) {
  self->setDocumentXmpMetadata(*xmpMetadata);
}

//  QByteArray QPdfEngine::documentXmpMetadata() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QPdfEngine19documentXmpMetadataEv(
    const QPdfEngine *self) {
  return new QByteArray(self->documentXmpMetadata());
}

//  void QPdfEngine::addFileAttachment(const QString &fileName, const
//      QByteArray &data, const QString &mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine17addFileAttachmentERK7QStringRK10QByteArrayS2_(
    QPdfEngine *self,
    const QString *fileName,
    const QByteArray *data,
    const QString *mimeType) {
  self->addFileAttachment(*fileName, *data, *mimeType);
}

//  bool QPdfEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPdfEngine5beginEP12QPaintDevice(
    QPdfEngine *self,
    QPaintDevice *pdev) {
  return self->begin(pdev);
}

//  bool QPdfEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPdfEngine3endEv(QPdfEngine *self) {
  return self->end();
}

//  void QPdfEngine::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine10drawPointsEPK7QPointFi(
    QPdfEngine *self,
    const QPointF *points,
    int pointCount) {
  self->drawPoints(points, pointCount);
}

//  void QPdfEngine::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine9drawLinesEPK6QLineFi(
    QPdfEngine *self,
    const QLineF *lines,
    int lineCount) {
  self->drawLines(lines, lineCount);
}

//  void QPdfEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine9drawRectsEPK6QRectFi(
    QPdfEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->drawRects(rects, rectCount);
}

//  void QPdfEngine::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPdfEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->drawPolygon(points, pointCount, mode);
}

//  void QPdfEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine8drawPathERK12QPainterPath(
    QPdfEngine *self,
    const QPainterPath *path) {
  self->drawPath(*path);
}

//  void QPdfEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPdfEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->drawTextItem(*p, *textItem);
}

//  void QPdfEngine::drawPixmap(const QRectF &rectangle, const QPixmap
//      &pixmap, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPdfEngine *self,
    const QRectF *rectangle,
    const QPixmap *pixmap,
    const QRectF *sr) {
  self->drawPixmap(*rectangle, *pixmap, *sr);
}

//  void QPdfEngine::drawImage(const QRectF &r, const QImage &pm, const
//      QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPdfEngine *self,
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

//  void QPdfEngine::drawTiledPixmap(const QRectF &rectangle, const QPixmap
//      &pixmap, const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPdfEngine *self,
    const QRectF *rectangle,
    const QPixmap *pixmap,
    const QPointF *point) {
  self->drawTiledPixmap(*rectangle, *pixmap, *point);
}

//  void QPdfEngine::drawHyperlink(const QRectF &r, const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine13drawHyperlinkERK6QRectFRK4QUrl(
    QPdfEngine *self,
    const QRectF *r,
    const QUrl *url) {
  self->drawHyperlink(*r, *url);
}

//  void QPdfEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine11updateStateERK17QPaintEngineState(
    QPdfEngine *self,
    const QPaintEngineState *state) {
  self->updateState(*state);
}

//  int QPdfEngine::metric(QPaintDevice::PaintDeviceMetric metricType) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QPdfEngine6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QPdfEngine *self,
    QPaintDevice::PaintDeviceMetric metricType) {
  return self->metric(metricType);
}

//  Type QPdfEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_ZNK10QPdfEngine4typeEv(const QPdfEngine *self) {
  return self->type();
}

//  bool QPdfEngine::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QPdfEngine7newPageEv(QPdfEngine *self) {
  return self->newPage();
}

//  void QPdfEngine::setPageLayout(const QPageLayout &pageLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine13setPageLayoutERK11QPageLayout(
    QPdfEngine *self,
    const QPageLayout *pageLayout) {
  self->setPageLayout(*pageLayout);
}

//  void QPdfEngine::setPageSize(const QPageSize &pageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine11setPageSizeERK9QPageSize(
    QPdfEngine *self,
    const QPageSize *pageSize) {
  self->setPageSize(*pageSize);
}

//  void QPdfEngine::setPageOrientation(QPageLayout::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine18setPageOrientationEN11QPageLayout11OrientationE(
    QPdfEngine *self,
    QPageLayout::Orientation orientation) {
  self->setPageOrientation(orientation);
}

//  void QPdfEngine::setPageMargins(const QMarginsF &margins,
//      QPageLayout::Unit units)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE(
    QPdfEngine *self,
    const QMarginsF *margins,
    QPageLayout::Unit units) {
  self->setPageMargins(*margins, units);
}

//  QPageLayout QPdfEngine::pageLayout() const
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZNK10QPdfEngine10pageLayoutEv(const QPdfEngine *self) {
  return new QPageLayout(self->pageLayout());
}

//  void QPdfEngine::setPen()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine6setPenEv(QPdfEngine *self) {
  self->setPen();
}

//  void QPdfEngine::setBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine8setBrushEv(QPdfEngine *self) {
  self->setBrush();
}

//  void QPdfEngine::setupGraphicsState(QPaintEngine::DirtyFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine18setupGraphicsStateE6QFlagsIN12QPaintEngine9DirtyFlagEE(
    QPdfEngine *self,
    int flags) {
  self->setupGraphicsState(QFlags<QPaintEngine::DirtyFlag>::fromInt(flags));
}

//  void QPdfEngine::updateClipPath(const QPainterPath &path,
//      Qt::ClipOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPdfEngine14updateClipPathERK12QPainterPathN2Qt13ClipOperationE(
    QPdfEngine *self,
    const QPainterPath *path,
    Qt::ClipOperation op) {
  self->updateClipPath(*path, op);
}

//  a Python function taken by a CuteQPdfEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfEngine(QPdfEngine *self, const char *key, void *call) {
  return static_cast<CuteQPdfEngine *>(self)->take(key, call);
}

//  bool QPdfEngine::begin(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QPdfEngine5beginEP12QPaintDevice(
    QPdfEngine *self,
    QPaintDevice *pdev) {
  return self->QPdfEngine::begin(pdev);
}

//  bool QPdfEngine::end()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QPdfEngine3endEv(QPdfEngine *self) {
  return self->QPdfEngine::end();
}

//  void QPdfEngine::drawPoints(const QPointF *points, int pointCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine10drawPointsEPK7QPointFi(
    QPdfEngine *self,
    const QPointF *points,
    int pointCount) {
  self->QPdfEngine::drawPoints(points, pointCount);
}

//  void QPdfEngine::drawLines(const QLineF *lines, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine9drawLinesEPK6QLineFi(
    QPdfEngine *self,
    const QLineF *lines,
    int lineCount) {
  self->QPdfEngine::drawLines(lines, lineCount);
}

//  void QPdfEngine::drawRects(const QRectF *rects, int rectCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine9drawRectsEPK6QRectFi(
    QPdfEngine *self,
    const QRectF *rects,
    int rectCount) {
  self->QPdfEngine::drawRects(rects, rectCount);
}

//  void QPdfEngine::drawPolygon(const QPointF *points, int pointCount,
//      PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine11drawPolygonEPK7QPointFiN12QPaintEngine15PolygonDrawModeE(
    QPdfEngine *self,
    const QPointF *points,
    int pointCount,
    QPaintEngine::PolygonDrawMode mode) {
  self->QPdfEngine::drawPolygon(points, pointCount, mode);
}

//  void QPdfEngine::drawPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine8drawPathERK12QPainterPath(
    QPdfEngine *self,
    const QPainterPath *path) {
  self->QPdfEngine::drawPath(*path);
}

//  void QPdfEngine::drawTextItem(const QPointF &p, const QTextItem
//      &textItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine12drawTextItemERK7QPointFRK9QTextItem(
    QPdfEngine *self,
    const QPointF *p,
    const QTextItem *textItem) {
  self->QPdfEngine::drawTextItem(*p, *textItem);
}

//  void QPdfEngine::drawPixmap(const QRectF &rectangle, const QPixmap
//      &pixmap, const QRectF &sr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine10drawPixmapERK6QRectFRK7QPixmapS2_(
    QPdfEngine *self,
    const QRectF *rectangle,
    const QPixmap *pixmap,
    const QRectF *sr) {
  self->QPdfEngine::drawPixmap(*rectangle, *pixmap, *sr);
}

//  void QPdfEngine::drawImage(const QRectF &r, const QImage &pm, const
//      QRectF &sr, Qt::ImageConversionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine9drawImageERK6QRectFRK6QImageS2_6QFlagsIN2Qt19ImageConversionFlagEE(
    QPdfEngine *self,
    const QRectF *r,
    const QImage *pm,
    const QRectF *sr,
    int flags) {
  self->QPdfEngine::drawImage(
      *r,
      *pm,
      *sr,
      QFlags<Qt::ImageConversionFlag>::fromInt(flags));
}

//  void QPdfEngine::drawTiledPixmap(const QRectF &rectangle, const QPixmap
//      &pixmap, const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine15drawTiledPixmapERK6QRectFRK7QPixmapRK7QPointF(
    QPdfEngine *self,
    const QRectF *rectangle,
    const QPixmap *pixmap,
    const QPointF *point) {
  self->QPdfEngine::drawTiledPixmap(*rectangle, *pixmap, *point);
}

//  void QPdfEngine::updateState(const QPaintEngineState &state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QPdfEngine11updateStateERK17QPaintEngineState(
    QPdfEngine *self,
    const QPaintEngineState *state) {
  self->QPdfEngine::updateState(*state);
}

//  Type QPdfEngine::type() const
extern "C" Q_DECL_EXPORT
QPaintEngine::Type ritual_own_ZNK10QPdfEngine4typeEv(
    const QPdfEngine *self) {
  return self->QPdfEngine::type();
}

#endif  // !defined(QT_NO_PDF)
