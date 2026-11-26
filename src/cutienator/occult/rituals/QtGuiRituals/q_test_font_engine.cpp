//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <cstring>

//  A QTestFontEngine that Python can take functions over in. Every QTestFontEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef glyph_t (*CuteQTestFontEngineCall0)(const void *, uint, int *);
typedef void (*CuteQTestFontEngineCall1)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQTestFontEngineCall2)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const glyph_metrics_t * (*CuteQTestFontEngineCall3)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQTestFontEngineCall4)(const void *, glyph_t, int *);
typedef void * (*CuteQTestFontEngineCall5)(const void *, qreal, int *);
typedef const QFixed * (*CuteQTestFontEngineCall6)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall7)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall8)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall9)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall10)(const void *, int *);
typedef qreal (*CuteQTestFontEngineCall11)(const void *, int *);
typedef qreal (*CuteQTestFontEngineCall12)(const void *, int *);
typedef qreal (*CuteQTestFontEngineCall13)(const void *, int *);
typedef const QImage * (*CuteQTestFontEngineCall14)(const void *, glyph_t, int *);
typedef bool (*CuteQTestFontEngineCall15)(const void *, const QChar *, int, int *);
typedef const QFontEngine::Properties * (*CuteQTestFontEngineCall16)(const void *, int *);
typedef void (*CuteQTestFontEngineCall17)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQTestFontEngineCall18)(const void *, int *);
typedef int (*CuteQTestFontEngineCall19)(const void *, int *);
typedef bool (*CuteQTestFontEngineCall20)(const void *, int *);
typedef bool (*CuteQTestFontEngineCall21)(const void *, int *);
typedef const QFixedPoint * (*CuteQTestFontEngineCall22)(const void *, const QFixedPoint *, int *);
typedef void (*CuteQTestFontEngineCall23)(const void *, QGlyphLayout *, int, int *);
typedef const QImage * (*CuteQTestFontEngineCall24)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQTestFontEngineCall25)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQTestFontEngineCall26)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQTestFontEngineCall27)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQTestFontEngineCall28)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQTestFontEngineCall29)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQTestFontEngineCall30)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQTestFontEngineCall31)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQTestFontEngineCall32)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQTestFontEngineCall33)(const void *, glyph_t, const QTransform *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall34)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall35)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall36)(const void *, int *);
typedef const QFixed * (*CuteQTestFontEngineCall37)(const void *, int *);
typedef bool (*CuteQTestFontEngineCall38)(const void *, const QTransform *, int *);
typedef int (*CuteQTestFontEngineCall39)(const void *, int *);
typedef int (*CuteQTestFontEngineCall40)(const void *, int, int *);
typedef void * (*CuteQTestFontEngineCall41)(const void *, int *);
typedef QString * (*CuteQTestFontEngineCall42)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQTestFontEngineCall43)(const void *, const QLatin1String *, int *);
typedef bool (*CuteQTestFontEngineCall44)(const void *, int *);
typedef bool (*CuteQTestFontEngineCall45)(const void *, int, int *);
typedef void (*CuteQTestFontEngineCall46)(const void *, int, int *);
typedef void (*CuteQTestFontEngineCall47)(const void *, int *);
class CuteQTestFontEngine : public QTestFontEngine {
public:
  using QTestFontEngine::QTestFontEngine;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphIndexEj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxERK12QGlyphLayout")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEj")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13cloneWithSizeEd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12emSquareSizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6ascentEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9capHeightEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7descentEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7leadingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12maxCharWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14minLeftBearingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine15minRightBearingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEj")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9canRenderEPK5QChari")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10propertiesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6faceIdEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine11synthesizedEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine18hasInternalCachingEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine20removeGlyphFromCacheEj")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEjRK10QTransform")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7xHeightEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine16averageCharWidthEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13lineThicknessEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine17underlinePositionEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine22supportsTransformationERK10QTransform")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphCountEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6handleEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9glyphNameEj")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9findGlyphE13QLatin1String")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine23initializeHeightMetricsEv")) {
      taken[47] = call;
      return true;
    }
    return false;
  }

  //  glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTestFontEngineCall0 call = reinterpret_cast<CuteQTestFontEngineCall0>(taken[0]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::glyphIndex(ucs4);
  }

  //  void QFontEngineBox::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTestFontEngineCall1 call = reinterpret_cast<CuteQTestFontEngineCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineBox::recalcAdvances(a0, a1);
  }

  //  void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
  //      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
  //      flags)
  void addOutlineToPath(
      qreal x,
      qreal y,
      const QGlyphLayout &glyphs,
      QPainterPath *path,
      QTextItem::RenderFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTestFontEngineCall2 call = reinterpret_cast<CuteQTestFontEngineCall2>(taken[2]);
      call(this, x, y, &glyphs, path, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineBox::addOutlineToPath(x, y, glyphs, path, flags);
  }

  //  glyph_metrics_t QFontEngineBox::boundingBox(const QGlyphLayout
  //      &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTestFontEngineCall3 call = reinterpret_cast<CuteQTestFontEngineCall3>(taken[3]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngineBox::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTestFontEngineCall4 call = reinterpret_cast<CuteQTestFontEngineCall4>(taken[4]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::boundingBox(glyph);
  }

  //  QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize) const
  QFontEngine *cloneWithSize(qreal pixelSize) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTestFontEngineCall5 call = reinterpret_cast<CuteQTestFontEngineCall5>(taken[5]);
      void * given = call(this, pixelSize, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngineBox::cloneWithSize(pixelSize);
  }

  //  QFixed QFontEngineBox::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTestFontEngineCall6 call = reinterpret_cast<CuteQTestFontEngineCall6>(taken[6]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::emSquareSize();
  }

  //  QFixed QFontEngineBox::ascent() const
  QFixed ascent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTestFontEngineCall7 call = reinterpret_cast<CuteQTestFontEngineCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::ascent();
  }

  //  QFixed QFontEngineBox::capHeight() const
  QFixed capHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTestFontEngineCall8 call = reinterpret_cast<CuteQTestFontEngineCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::capHeight();
  }

  //  QFixed QFontEngineBox::descent() const
  QFixed descent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTestFontEngineCall9 call = reinterpret_cast<CuteQTestFontEngineCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::descent();
  }

  //  QFixed QFontEngineBox::leading() const
  QFixed leading() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTestFontEngineCall10 call = reinterpret_cast<CuteQTestFontEngineCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::leading();
  }

  //  qreal QFontEngineBox::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTestFontEngineCall11 call = reinterpret_cast<CuteQTestFontEngineCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::maxCharWidth();
  }

  //  qreal QFontEngineBox::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTestFontEngineCall12 call = reinterpret_cast<CuteQTestFontEngineCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::minLeftBearing();
  }

  //  qreal QFontEngineBox::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTestFontEngineCall13 call = reinterpret_cast<CuteQTestFontEngineCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::minRightBearing();
  }

  //  QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTestFontEngineCall14 call = reinterpret_cast<CuteQTestFontEngineCall14>(taken[14]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::alphaMapForGlyph(a0);
  }

  //  bool QFontEngineBox::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTestFontEngineCall15 call = reinterpret_cast<CuteQTestFontEngineCall15>(taken[15]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::canRender(string, len);
  }

  //  Properties QFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTestFontEngineCall16 call = reinterpret_cast<CuteQTestFontEngineCall16>(taken[16]);
      const QFontEngine::Properties * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::properties();
  }

  //  void QFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
  //      glyph_metrics_t *metrics)
  void getUnscaledGlyph(
      glyph_t glyph,
      QPainterPath *path,
      glyph_metrics_t *metrics) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTestFontEngineCall17 call = reinterpret_cast<CuteQTestFontEngineCall17>(taken[17]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTestFontEngineCall18 call = reinterpret_cast<CuteQTestFontEngineCall18>(taken[18]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::faceId();
  }

  //  int QFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQTestFontEngineCall19 call = reinterpret_cast<CuteQTestFontEngineCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::synthesized();
  }

  //  bool QFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTestFontEngineCall20 call = reinterpret_cast<CuteQTestFontEngineCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTestFontEngineCall21 call = reinterpret_cast<CuteQTestFontEngineCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTestFontEngineCall22 call = reinterpret_cast<CuteQTestFontEngineCall22>(taken[22]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTestFontEngineCall23 call = reinterpret_cast<CuteQTestFontEngineCall23>(taken[23]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::doKerning(a0, a1);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTestFontEngineCall24 call = reinterpret_cast<CuteQTestFontEngineCall24>(taken[24]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTestFontEngineCall25 call = reinterpret_cast<CuteQTestFontEngineCall25>(taken[25]);
      const QImage * given = call(this, a0, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, t);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTestFontEngineCall26 call = reinterpret_cast<CuteQTestFontEngineCall26>(taken[26]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaRGBMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTestFontEngineCall27 call = reinterpret_cast<CuteQTestFontEngineCall27>(taken[27]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t, const QColor &color)
  QImage bitmapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t,
      const QColor &color) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTestFontEngineCall28 call = reinterpret_cast<CuteQTestFontEngineCall28>(taken[28]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &color, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::bitmapForGlyph(a0, subPixelPosition, t, color);
  }

  //  Glyph *QFontEngine::glyphData(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
  QFontEngine::Glyph *glyphData(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition,
      QFontEngine::GlyphFormat neededFormat,
      const QTransform &t) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTestFontEngineCall29 call = reinterpret_cast<CuteQTestFontEngineCall29>(taken[29]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQTestFontEngineCall30 call = reinterpret_cast<CuteQTestFontEngineCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasInternalCaching();
  }

  //  glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t glyph, const
  //      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
  glyph_metrics_t alphaMapBoundingBox(
      glyph_t glyph,
      const QFixedPoint &a1,
      const QTransform &matrix,
      QFontEngine::GlyphFormat a3) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTestFontEngineCall31 call = reinterpret_cast<CuteQTestFontEngineCall31>(taken[31]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTestFontEngineCall32 call = reinterpret_cast<CuteQTestFontEngineCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontEngine::removeGlyphFromCache(a0);
  }

  //  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const
  //      QTransform &matrix)
  glyph_metrics_t boundingBox(
      glyph_t glyph,
      const QTransform &matrix) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTestFontEngineCall33 call = reinterpret_cast<CuteQTestFontEngineCall33>(taken[33]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyph, matrix);
  }

  //  QFixed QFontEngine::xHeight() const
  QFixed xHeight() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQTestFontEngineCall34 call = reinterpret_cast<CuteQTestFontEngineCall34>(taken[34]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::xHeight();
  }

  //  QFixed QFontEngine::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQTestFontEngineCall35 call = reinterpret_cast<CuteQTestFontEngineCall35>(taken[35]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::averageCharWidth();
  }

  //  QFixed QFontEngine::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQTestFontEngineCall36 call = reinterpret_cast<CuteQTestFontEngineCall36>(taken[36]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::lineThickness();
  }

  //  QFixed QFontEngine::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQTestFontEngineCall37 call = reinterpret_cast<CuteQTestFontEngineCall37>(taken[37]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::underlinePosition();
  }

  //  bool QFontEngine::supportsTransformation(const QTransform &transform)
  //      const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQTestFontEngineCall38 call = reinterpret_cast<CuteQTestFontEngineCall38>(taken[38]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsTransformation(transform);
  }

  //  int QFontEngine::glyphCount() const
  int glyphCount() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQTestFontEngineCall39 call = reinterpret_cast<CuteQTestFontEngineCall39>(taken[39]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphCount();
  }

  //  int QFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[40]) {
      int handled = 0;
      CuteQTestFontEngineCall40 call = reinterpret_cast<CuteQTestFontEngineCall40>(taken[40]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphMargin(format);
  }

  //  Qt::HANDLE QFontEngine::handle() const
  Qt::HANDLE handle() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQTestFontEngineCall41 call = reinterpret_cast<CuteQTestFontEngineCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return QFontEngine::handle();
  }

  //  QString QFontEngine::glyphName(glyph_t index) const
  QString glyphName(glyph_t index) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQTestFontEngineCall42 call = reinterpret_cast<CuteQTestFontEngineCall42>(taken[42]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontEngine::glyphName(index);
  }

  //  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
  glyph_t findGlyph(QLatin1StringView name) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQTestFontEngineCall43 call = reinterpret_cast<CuteQTestFontEngineCall43>(taken[43]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngine::findGlyph(name);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQTestFontEngineCall44 call = reinterpret_cast<CuteQTestFontEngineCall44>(taken[44]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasUnreliableGlyphOutline();
  }

  //  bool
  //      QFontEngine::expectsGammaCorrectedBlending(QFontEngine::GlyphForm
  //      at format) const
  bool expectsGammaCorrectedBlending(
      QFontEngine::GlyphFormat format) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQTestFontEngineCall45 call = reinterpret_cast<CuteQTestFontEngineCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTestFontEngineCall46 call = reinterpret_cast<CuteQTestFontEngineCall46>(taken[46]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQTestFontEngineCall47 call = reinterpret_cast<CuteQTestFontEngineCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngine::initializeHeightMetrics();
  }
};

//  a Python function taken by a CuteQTestFontEngine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTestFontEngine(
    QTestFontEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTestFontEngine *>(self)->take(key, call);
}
