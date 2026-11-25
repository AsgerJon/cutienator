//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_coretext_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Core Text's fonts, Core Graphics' fonts and contexts and a
//  'void *' are passed as addresses. Not written: 'create', which takes
//  a 'QMap', and 'loadAdvancesForGlyphs', which takes a
//  'QVarLengthArray &'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qfontengine_coretext_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QCoreTextFontEngine that Python can take functions over in. Every
//  QCoreTextFontEngine Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef glyph_t (*CuteQCoreTextFontEngineCall0)(const void *, uint, int *);
typedef void (*CuteQCoreTextFontEngineCall1)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQCoreTextFontEngineCall2)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const glyph_metrics_t * (*CuteQCoreTextFontEngineCall3)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQCoreTextFontEngineCall4)(const void *, glyph_t, int *);
typedef void * (*CuteQCoreTextFontEngineCall5)(const void *, qreal, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall6)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall7)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall8)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall9)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall10)(const void *, int *);
typedef qreal (*CuteQCoreTextFontEngineCall11)(const void *, int *);
typedef qreal (*CuteQCoreTextFontEngineCall12)(const void *, int *);
typedef qreal (*CuteQCoreTextFontEngineCall13)(const void *, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall14)(const void *, glyph_t, int *);
typedef bool (*CuteQCoreTextFontEngineCall15)(const void *, const QChar *, int, int *);
typedef const QFontEngine::Properties * (*CuteQCoreTextFontEngineCall16)(const void *, int *);
typedef void (*CuteQCoreTextFontEngineCall17)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQCoreTextFontEngineCall18)(const void *, int *);
typedef int (*CuteQCoreTextFontEngineCall19)(const void *, int *);
typedef bool (*CuteQCoreTextFontEngineCall20)(const void *, int *);
typedef bool (*CuteQCoreTextFontEngineCall21)(const void *, int *);
typedef const QFixedPoint * (*CuteQCoreTextFontEngineCall22)(const void *, const QFixedPoint *, int *);
typedef void (*CuteQCoreTextFontEngineCall23)(const void *, QGlyphLayout *, int, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall24)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall25)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall26)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall27)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQCoreTextFontEngineCall28)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQCoreTextFontEngineCall29)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQCoreTextFontEngineCall30)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQCoreTextFontEngineCall31)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQCoreTextFontEngineCall32)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQCoreTextFontEngineCall33)(const void *, glyph_t, const QTransform *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall34)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall35)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall36)(const void *, int *);
typedef const QFixed * (*CuteQCoreTextFontEngineCall37)(const void *, int *);
typedef bool (*CuteQCoreTextFontEngineCall38)(const void *, const QTransform *, int *);
typedef int (*CuteQCoreTextFontEngineCall39)(const void *, int *);
typedef int (*CuteQCoreTextFontEngineCall40)(const void *, int, int *);
typedef QString * (*CuteQCoreTextFontEngineCall41)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQCoreTextFontEngineCall42)(const void *, const QLatin1String *, int *);
typedef bool (*CuteQCoreTextFontEngineCall43)(const void *, int *);
typedef bool (*CuteQCoreTextFontEngineCall44)(const void *, int, int *);
typedef void (*CuteQCoreTextFontEngineCall45)(const void *, int, int *);
typedef void (*CuteQCoreTextFontEngineCall46)(const void *, int *);
class CuteQCoreTextFontEngine : public QCoreTextFontEngine {
public:
  using QCoreTextFontEngine::QCoreTextFontEngine;
  void *taken[47] = {};

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
    if (!std::strcmp(key, "_ZNK11QFontEngine9glyphNameEj")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9findGlyphE13QLatin1String")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine23initializeHeightMetricsEv")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  glyph_t QCoreTextFontEngine::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall0 call = reinterpret_cast<CuteQCoreTextFontEngineCall0>(taken[0]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::glyphIndex(ucs4);
  }

  //  void QCoreTextFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags
  //      a1) const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall1 call = reinterpret_cast<CuteQCoreTextFontEngineCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QCoreTextFontEngine::recalcAdvances(a0, a1);
  }

  //  void QFontEngine::addOutlineToPath(qreal x, qreal y, const QGlyphLayout
  //      &glyphs, QPainterPath *path, QTextItem::RenderFlags flags)
  void addOutlineToPath(
      qreal x,
      qreal y,
      const QGlyphLayout &glyphs,
      QPainterPath *path,
      QTextItem::RenderFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall2 call = reinterpret_cast<CuteQCoreTextFontEngineCall2>(taken[2]);
      call(this, x, y, &glyphs, path, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::addOutlineToPath(x, y, glyphs, path, flags);
  }

  //  glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall3 call = reinterpret_cast<CuteQCoreTextFontEngineCall3>(taken[3]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyphs);
  }

  //  glyph_metrics_t QCoreTextFontEngine::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall4 call = reinterpret_cast<CuteQCoreTextFontEngineCall4>(taken[4]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::boundingBox(glyph);
  }

  //  QFontEngine *QCoreTextFontEngine::cloneWithSize(qreal pixelSize) const
  QFontEngine *cloneWithSize(qreal pixelSize) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall5 call = reinterpret_cast<CuteQCoreTextFontEngineCall5>(taken[5]);
      void * given = call(this, pixelSize, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QCoreTextFontEngine::cloneWithSize(pixelSize);
  }

  //  QFixed QCoreTextFontEngine::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall6 call = reinterpret_cast<CuteQCoreTextFontEngineCall6>(taken[6]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::emSquareSize();
  }

  //  QFixed QFontEngine::ascent() const
  QFixed ascent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall7 call = reinterpret_cast<CuteQCoreTextFontEngineCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::ascent();
  }

  //  QFixed QCoreTextFontEngine::capHeight() const
  QFixed capHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall8 call = reinterpret_cast<CuteQCoreTextFontEngineCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::capHeight();
  }

  //  QFixed QFontEngine::descent() const
  QFixed descent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall9 call = reinterpret_cast<CuteQCoreTextFontEngineCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::descent();
  }

  //  QFixed QFontEngine::leading() const
  QFixed leading() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall10 call = reinterpret_cast<CuteQCoreTextFontEngineCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::leading();
  }

  //  qreal QCoreTextFontEngine::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall11 call = reinterpret_cast<CuteQCoreTextFontEngineCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::maxCharWidth();
  }

  //  qreal QFontEngine::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall12 call = reinterpret_cast<CuteQCoreTextFontEngineCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minLeftBearing();
  }

  //  qreal QFontEngine::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall13 call = reinterpret_cast<CuteQCoreTextFontEngineCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minRightBearing();
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall14 call = reinterpret_cast<CuteQCoreTextFontEngineCall14>(taken[14]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0);
  }

  //  bool QCoreTextFontEngine::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall15 call = reinterpret_cast<CuteQCoreTextFontEngineCall15>(taken[15]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::canRender(string, len);
  }

  //  Properties QCoreTextFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall16 call = reinterpret_cast<CuteQCoreTextFontEngineCall16>(taken[16]);
      const QFontEngine::Properties * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::properties();
  }

  //  void QCoreTextFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath
  //      *path, glyph_metrics_t *metrics)
  void getUnscaledGlyph(
      glyph_t glyph,
      QPainterPath *path,
      glyph_metrics_t *metrics) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall17 call = reinterpret_cast<CuteQCoreTextFontEngineCall17>(taken[17]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QCoreTextFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QCoreTextFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall18 call = reinterpret_cast<CuteQCoreTextFontEngineCall18>(taken[18]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::faceId();
  }

  //  int QCoreTextFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall19 call = reinterpret_cast<CuteQCoreTextFontEngineCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::synthesized();
  }

  //  bool QCoreTextFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall20 call = reinterpret_cast<CuteQCoreTextFontEngineCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QCoreTextFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall21 call = reinterpret_cast<CuteQCoreTextFontEngineCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall22 call = reinterpret_cast<CuteQCoreTextFontEngineCall22>(taken[22]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  void QCoreTextFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall23 call = reinterpret_cast<CuteQCoreTextFontEngineCall23>(taken[23]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QCoreTextFontEngine::doKerning(a0, a1);
  }

  //  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t glyph, const
  //      QFixedPoint &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall24 call = reinterpret_cast<CuteQCoreTextFontEngineCall24>(taken[24]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall25 call = reinterpret_cast<CuteQCoreTextFontEngineCall25>(taken[25]);
      const QImage * given = call(this, a0, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, t);
  }

  //  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t a0, const
  //      QFixedPoint &subPixelPosition, const QTransform &t)
  QImage alphaMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall26 call = reinterpret_cast<CuteQCoreTextFontEngineCall26>(taken[26]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::alphaMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QCoreTextFontEngine::alphaRGBMapForGlyph(glyph_t a0, const
  //      QFixedPoint &subPixelPosition, const QTransform &t)
  QImage alphaRGBMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall27 call = reinterpret_cast<CuteQCoreTextFontEngineCall27>(taken[27]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QCoreTextFontEngine::bitmapForGlyph(glyph_t a0, const
  //      QFixedPoint &subPixelPosition, const QTransform &t, const QColor
  //      &color)
  QImage bitmapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t,
      const QColor &color) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall28 call = reinterpret_cast<CuteQCoreTextFontEngineCall28>(taken[28]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &color, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::bitmapForGlyph(a0, subPixelPosition, t, color);
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
      CuteQCoreTextFontEngineCall29 call = reinterpret_cast<CuteQCoreTextFontEngineCall29>(taken[29]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall30 call = reinterpret_cast<CuteQCoreTextFontEngineCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasInternalCaching();
  }

  //  glyph_metrics_t QCoreTextFontEngine::alphaMapBoundingBox(glyph_t glyph,
  //      const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
  glyph_metrics_t alphaMapBoundingBox(
      glyph_t glyph,
      const QFixedPoint &a1,
      const QTransform &matrix,
      QFontEngine::GlyphFormat a3) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall31 call = reinterpret_cast<CuteQCoreTextFontEngineCall31>(taken[31]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall32 call = reinterpret_cast<CuteQCoreTextFontEngineCall32>(taken[32]);
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
      CuteQCoreTextFontEngineCall33 call = reinterpret_cast<CuteQCoreTextFontEngineCall33>(taken[33]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyph, matrix);
  }

  //  QFixed QCoreTextFontEngine::xHeight() const
  QFixed xHeight() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall34 call = reinterpret_cast<CuteQCoreTextFontEngineCall34>(taken[34]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::xHeight();
  }

  //  QFixed QCoreTextFontEngine::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall35 call = reinterpret_cast<CuteQCoreTextFontEngineCall35>(taken[35]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::averageCharWidth();
  }

  //  QFixed QCoreTextFontEngine::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall36 call = reinterpret_cast<CuteQCoreTextFontEngineCall36>(taken[36]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::lineThickness();
  }

  //  QFixed QCoreTextFontEngine::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall37 call = reinterpret_cast<CuteQCoreTextFontEngineCall37>(taken[37]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCoreTextFontEngine::underlinePosition();
  }

  //  bool QCoreTextFontEngine::supportsTransformation(const QTransform
  //      &transform) const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall38 call = reinterpret_cast<CuteQCoreTextFontEngineCall38>(taken[38]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::supportsTransformation(transform);
  }

  //  int QCoreTextFontEngine::glyphCount() const
  int glyphCount() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall39 call = reinterpret_cast<CuteQCoreTextFontEngineCall39>(taken[39]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::glyphCount();
  }

  //  int QCoreTextFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[40]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall40 call = reinterpret_cast<CuteQCoreTextFontEngineCall40>(taken[40]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::glyphMargin(format);
  }

  //  QString QCoreTextFontEngine::glyphName(glyph_t index) const
  QString glyphName(glyph_t index) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall41 call = reinterpret_cast<CuteQCoreTextFontEngineCall41>(taken[41]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCoreTextFontEngine::glyphName(index);
  }

  //  glyph_t QCoreTextFontEngine::findGlyph(QLatin1StringView name) const
  glyph_t findGlyph(QLatin1StringView name) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall42 call = reinterpret_cast<CuteQCoreTextFontEngineCall42>(taken[42]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::findGlyph(name);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall43 call = reinterpret_cast<CuteQCoreTextFontEngineCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasUnreliableGlyphOutline();
  }

  //  bool QCoreTextFontEngine::expectsGammaCorrectedBlending(QFontEngine::Gl
  //      yphForm at format) const
  bool expectsGammaCorrectedBlending(
      QFontEngine::GlyphFormat format) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall44 call = reinterpret_cast<CuteQCoreTextFontEngineCall44>(taken[44]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QCoreTextFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall45 call = reinterpret_cast<CuteQCoreTextFontEngineCall45>(taken[45]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QCoreTextFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQCoreTextFontEngineCall46 call = reinterpret_cast<CuteQCoreTextFontEngineCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QCoreTextFontEngine::initializeHeightMetrics();
  }
};

//  QCoreTextFontEngine::QCoreTextFontEngine(CTFontRef font, const QFontDef
//      &def)
extern "C" Q_DECL_EXPORT
QCoreTextFontEngine *ritual_ZN19QCoreTextFontEngineC1EPK8__CTFontRK8QFontDef(
    CTFontRef font,
    const QFontDef *def) {
  return new CuteQCoreTextFontEngine(font, *def);
}

//  QCoreTextFontEngine::QCoreTextFontEngine(CGFontRef font, const QFontDef
//      &def)
extern "C" Q_DECL_EXPORT
QCoreTextFontEngine *ritual_ZN19QCoreTextFontEngineC1EP6CGFontRK8QFontDef(
    CGFontRef font,
    const QFontDef *def) {
  return new CuteQCoreTextFontEngine(font, *def);
}

//  QCoreTextFontEngine::QCoreTextFontEngine(const QFontDef &def)
extern "C" Q_DECL_EXPORT
QCoreTextFontEngine *ritual_ZN19QCoreTextFontEngineC1ERK8QFontDef(
    const QFontDef *def) {
  return new CuteQCoreTextFontEngine(*def);
}

//  QCoreTextFontEngine::~QCoreTextFontEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoreTextFontEngineD1Ev(QCoreTextFontEngine *self) {
  delete self;
}

//  int QCoreTextFontEngine::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCoreTextFontEngine10glyphCountEv(
    const QCoreTextFontEngine *self) {
  return self->glyphCount();
}

//  glyph_t QCoreTextFontEngine::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK19QCoreTextFontEngine10glyphIndexEj(
    const QCoreTextFontEngine *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  QString QCoreTextFontEngine::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QCoreTextFontEngine9glyphNameEj(
    const QCoreTextFontEngine *self,
    glyph_t index) {
  return new QString(self->glyphName(index));
}

//  glyph_t QCoreTextFontEngine::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK19QCoreTextFontEngine9findGlyphE13QLatin1String(
    const QCoreTextFontEngine *self,
    const QLatin1String *name) {
  return self->findGlyph(*name);
}

//  int QCoreTextFontEngine::stringToCMap(const QChar *str, int len,
//      QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCoreTextFontEngine12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QCoreTextFontEngine *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str, len, glyphs, nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  void QCoreTextFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags
//      a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCoreTextFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QCoreTextFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->recalcAdvances(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  glyph_metrics_t QCoreTextFontEngine::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN19QCoreTextFontEngine11boundingBoxEj(
    QCoreTextFontEngine *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->boundingBox(glyph));
}

//  QFixed QCoreTextFontEngine::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine9capHeightEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QCoreTextFontEngine::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine7xHeightEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->xHeight());
}

//  qreal QCoreTextFontEngine::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QCoreTextFontEngine12maxCharWidthEv(
    const QCoreTextFontEngine *self) {
  return self->maxCharWidth();
}

//  QFixed QCoreTextFontEngine::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine16averageCharWidthEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->averageCharWidth());
}

//  void QCoreTextFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
//      *positions, int numGlyphs, QPainterPath *path, QTextItem::RenderFlags
//      a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoreTextFontEngine15addGlyphsToPathEPjP11QFixedPointiP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QCoreTextFontEngine *self,
    glyph_t *glyphs,
    QFixedPoint *positions,
    int numGlyphs,
    QPainterPath *path,
    int a4) {
  self->addGlyphsToPath(
      glyphs, positions, numGlyphs, path,
      QFlags<QTextItem::RenderFlag>::fromInt(a4));
}

//  bool QCoreTextFontEngine::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine9canRenderEPK5QChari(
    const QCoreTextFontEngine *self,
    const QChar *string,
    int len) {
  return self->canRender(string, len);
}

//  int QCoreTextFontEngine::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCoreTextFontEngine11synthesizedEv(
    const QCoreTextFontEngine *self) {
  return self->synthesized();
}

//  bool QCoreTextFontEngine::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine35supportsHorizontalSubPixelPositionsEv(
    const QCoreTextFontEngine *self) {
  return self->supportsHorizontalSubPixelPositions();
}

//  bool QCoreTextFontEngine::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine33supportsVerticalSubPixelPositionsEv(
    const QCoreTextFontEngine *self) {
  return self->supportsVerticalSubPixelPositions();
}

//  QFixed QCoreTextFontEngine::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine13lineThicknessEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->lineThickness());
}

//  QFixed QCoreTextFontEngine::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine17underlinePositionEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->underlinePosition());
}

//  void QCoreTextFontEngine::draw(CGContextRef ctx, qreal x, qreal y, const
//      QTextItemInt &ti, int paintDeviceHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoreTextFontEngine4drawEP9CGContextddRK12QTextItemInti(
    QCoreTextFontEngine *self,
    CGContextRef ctx,
    qreal x,
    qreal y,
    const QTextItemInt *ti,
    int paintDeviceHeight) {
  self->draw(ctx, x, y, *ti, paintDeviceHeight);
}

//  FaceId QCoreTextFontEngine::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_ZNK19QCoreTextFontEngine6faceIdEv(
    const QCoreTextFontEngine *self) {
  return new QFontEngine::FaceId(self->faceId());
}

//  bool QCoreTextFontEngine::getSfntTableData(uint a0, uchar *a1, uint *a2)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine16getSfntTableDataEjPhPj(
    const QCoreTextFontEngine *self,
    uint a0,
    uchar *a1,
    uint *a2) {
  return self->getSfntTableData(a0, a1, a2);
}

//  void QCoreTextFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath
//      *path, glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoreTextFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->getUnscaledGlyph(glyph, path, metrics);
}

//  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QCoreTextFontEngine16alphaMapForGlyphEjRK11QFixedPoint(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->alphaMapForGlyph(a0, *subPixelPosition));
}

//  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t glyph, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QCoreTextFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition, *t));
}

//  QImage QCoreTextFontEngine::alphaRGBMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QCoreTextFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  glyph_metrics_t QCoreTextFontEngine::alphaMapBoundingBox(glyph_t glyph,
//      const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN19QCoreTextFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->alphaMapBoundingBox(glyph, *a1, *matrix, a3));
}

//  QImage QCoreTextFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QCoreTextFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  QFixed QCoreTextFontEngine::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK19QCoreTextFontEngine12emSquareSizeEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->emSquareSize());
}

//  void QCoreTextFontEngine::doKerning(QGlyphLayout *g, ShaperFlags flags)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCoreTextFontEngine9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QCoreTextFontEngine *self,
    QGlyphLayout *g,
    int flags) {
  self->doKerning(g, QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  bool QCoreTextFontEngine::supportsTransformation(const QTransform
//      &transform) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine22supportsTransformationERK10QTransform(
    const QCoreTextFontEngine *self,
    const QTransform *transform) {
  return self->supportsTransformation(*transform);
}

//  bool QCoreTextFontEngine::expectsGammaCorrectedBlending(QFontEngine::Glyp
//      hFormat format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine29expectsGammaCorrectedBlendingEN11QFontEngine11GlyphFormatE(
    const QCoreTextFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->expectsGammaCorrectedBlending(format);
}

//  QFontEngine *QCoreTextFontEngine::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK19QCoreTextFontEngine13cloneWithSizeEd(
    const QCoreTextFontEngine *self,
    qreal pixelSize) {
  return self->cloneWithSize(pixelSize);
}

//  Qt::HANDLE QCoreTextFontEngine::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK19QCoreTextFontEngine6handleEv(
    const QCoreTextFontEngine *self) {
  return self->handle();
}

//  int QCoreTextFontEngine::glyphMargin(QFontEngine::GlyphFormat format)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QCoreTextFontEngine11glyphMarginEN11QFontEngine11GlyphFormatE(
    QCoreTextFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->glyphMargin(format);
}

//  QFontEngine::Properties QCoreTextFontEngine::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK19QCoreTextFontEngine10propertiesEv(
    const QCoreTextFontEngine *self) {
  return new QFontEngine::Properties(self->properties());
}

//  QList<QFontVariableAxis> QCoreTextFontEngine::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK19QCoreTextFontEngine12variableAxesEv(
    const QCoreTextFontEngine *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  FontSmoothing QCoreTextFontEngine::fontSmoothing()
extern "C" Q_DECL_EXPORT
QCoreTextFontEngine::FontSmoothing ritual_ZN19QCoreTextFontEngine13fontSmoothingEv() {
  return QCoreTextFontEngine::fontSmoothing();
}

//  qreal QCoreTextFontEngine::fontSmoothingGamma()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN19QCoreTextFontEngine18fontSmoothingGammaEv() {
  return QCoreTextFontEngine::fontSmoothingGamma();
}

//  bool QCoreTextFontEngine::ct_getSfntTable(void *user_data, uint tag,
//      uchar *buffer, uint *length)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCoreTextFontEngine15ct_getSfntTableEPvjPhPj(
    void *user_data,
    uint tag,
    uchar *buffer,
    uint *length) {
  return QCoreTextFontEngine::ct_getSfntTable(user_data, tag, buffer, length);
}

//  QFont::Weight QCoreTextFontEngine::qtWeightFromCFWeight(float value)
extern "C" Q_DECL_EXPORT
QFont::Weight ritual_ZN19QCoreTextFontEngine20qtWeightFromCFWeightEf(
    float value) {
  return QCoreTextFontEngine::qtWeightFromCFWeight(value);
}

//  void QCoreTextFontEngine::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoreTextFontEngine4initEv(QCoreTextFontEngine *self) {
  self->init();
}

//  QImage QCoreTextFontEngine::imageForGlyph(glyph_t glyph, const
//      QFixedPoint &subPixelPosition, const QTransform &m, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QCoreTextFontEngine13imageForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *m,
    const QColor *color) {
  return new QImage(self->imageForGlyph(glyph, *subPixelPosition, *m, *color));
}

//  bool QCoreTextFontEngine::hasColorGlyphs() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine14hasColorGlyphsEv(
    const QCoreTextFontEngine *self) {
  return self->hasColorGlyphs();
}

//  bool QCoreTextFontEngine::shouldAntialias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine15shouldAntialiasEv(
    const QCoreTextFontEngine *self) {
  return self->shouldAntialias();
}

//  bool QCoreTextFontEngine::shouldSmoothFont() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCoreTextFontEngine16shouldSmoothFontEv(
    const QCoreTextFontEngine *self) {
  return self->shouldSmoothFont();
}

//  void QCoreTextFontEngine::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCoreTextFontEngine23initializeHeightMetricsEv(
    const QCoreTextFontEngine *self) {
  self->initializeHeightMetrics();
}

//  a Python function taken by a CuteQCoreTextFontEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoreTextFontEngine(
    QCoreTextFontEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoreTextFontEngine *>(self)->take(key, call);
}

//  int QCoreTextFontEngine::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QCoreTextFontEngine10glyphCountEv(
    const QCoreTextFontEngine *self) {
  return self->QCoreTextFontEngine::glyphCount();
}

//  glyph_t QCoreTextFontEngine::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK19QCoreTextFontEngine10glyphIndexEj(
    const QCoreTextFontEngine *self,
    uint ucs4) {
  return self->QCoreTextFontEngine::glyphIndex(ucs4);
}

//  QString QCoreTextFontEngine::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QCoreTextFontEngine9glyphNameEj(
    const QCoreTextFontEngine *self,
    glyph_t index) {
  return new QString(self->QCoreTextFontEngine::glyphName(index));
}

//  glyph_t QCoreTextFontEngine::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK19QCoreTextFontEngine9findGlyphE13QLatin1String(
    const QCoreTextFontEngine *self,
    const QLatin1String *name) {
  return self->QCoreTextFontEngine::findGlyph(*name);
}

//  void QCoreTextFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags
//      a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QCoreTextFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QCoreTextFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->QCoreTextFontEngine::recalcAdvances(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  glyph_metrics_t QCoreTextFontEngine::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN19QCoreTextFontEngine11boundingBoxEj(
    QCoreTextFontEngine *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->QCoreTextFontEngine::boundingBox(glyph));
}

//  QFixed QCoreTextFontEngine::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine9capHeightEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::capHeight());
}

//  QFixed QCoreTextFontEngine::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine7xHeightEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::xHeight());
}

//  qreal QCoreTextFontEngine::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK19QCoreTextFontEngine12maxCharWidthEv(
    const QCoreTextFontEngine *self) {
  return self->QCoreTextFontEngine::maxCharWidth();
}

//  QFixed QCoreTextFontEngine::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine16averageCharWidthEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::averageCharWidth());
}

//  bool QCoreTextFontEngine::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QCoreTextFontEngine9canRenderEPK5QChari(
    const QCoreTextFontEngine *self,
    const QChar *string,
    int len) {
  return self->QCoreTextFontEngine::canRender(string, len);
}

//  int QCoreTextFontEngine::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QCoreTextFontEngine11synthesizedEv(
    const QCoreTextFontEngine *self) {
  return self->QCoreTextFontEngine::synthesized();
}

//  bool QCoreTextFontEngine::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QCoreTextFontEngine35supportsHorizontalSubPixelPositionsEv(
    const QCoreTextFontEngine *self) {
  return self->QCoreTextFontEngine::supportsHorizontalSubPixelPositions();
}

//  bool QCoreTextFontEngine::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QCoreTextFontEngine33supportsVerticalSubPixelPositionsEv(
    const QCoreTextFontEngine *self) {
  return self->QCoreTextFontEngine::supportsVerticalSubPixelPositions();
}

//  QFixed QCoreTextFontEngine::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine13lineThicknessEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::lineThickness());
}

//  QFixed QCoreTextFontEngine::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine17underlinePositionEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::underlinePosition());
}

//  FaceId QCoreTextFontEngine::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_own_ZNK19QCoreTextFontEngine6faceIdEv(
    const QCoreTextFontEngine *self) {
  return new QFontEngine::FaceId(self->QCoreTextFontEngine::faceId());
}

//  void QCoreTextFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath
//      *path, glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCoreTextFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->QCoreTextFontEngine::getUnscaledGlyph(glyph, path, metrics);
}

//  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19QCoreTextFontEngine16alphaMapForGlyphEjRK11QFixedPoint(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->QCoreTextFontEngine::alphaMapForGlyph(a0, *subPixelPosition));
}

//  QImage QCoreTextFontEngine::alphaMapForGlyph(glyph_t glyph, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19QCoreTextFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->QCoreTextFontEngine::alphaMapForGlyph(glyph, *subPixelPosition, *t));
}

//  QImage QCoreTextFontEngine::alphaRGBMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19QCoreTextFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->QCoreTextFontEngine::alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  glyph_metrics_t QCoreTextFontEngine::alphaMapBoundingBox(glyph_t glyph,
//      const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN19QCoreTextFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QCoreTextFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->QCoreTextFontEngine::alphaMapBoundingBox(glyph, *a1, *matrix, a3));
}

//  QImage QCoreTextFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19QCoreTextFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QCoreTextFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->QCoreTextFontEngine::bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  QFixed QCoreTextFontEngine::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK19QCoreTextFontEngine12emSquareSizeEv(
    const QCoreTextFontEngine *self) {
  return new QFixed(self->QCoreTextFontEngine::emSquareSize());
}

//  void QCoreTextFontEngine::doKerning(QGlyphLayout *g, ShaperFlags flags)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QCoreTextFontEngine9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QCoreTextFontEngine *self,
    QGlyphLayout *g,
    int flags) {
  self->QCoreTextFontEngine::doKerning(g, QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  bool QCoreTextFontEngine::supportsTransformation(const QTransform
//      &transform) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QCoreTextFontEngine22supportsTransformationERK10QTransform(
    const QCoreTextFontEngine *self,
    const QTransform *transform) {
  return self->QCoreTextFontEngine::supportsTransformation(*transform);
}

//  bool QCoreTextFontEngine::expectsGammaCorrectedBlending(QFontEngine::Glyp
//      hFormat format) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QCoreTextFontEngine29expectsGammaCorrectedBlendingEN11QFontEngine11GlyphFormatE(
    const QCoreTextFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->QCoreTextFontEngine::expectsGammaCorrectedBlending(format);
}

//  QFontEngine *QCoreTextFontEngine::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZNK19QCoreTextFontEngine13cloneWithSizeEd(
    const QCoreTextFontEngine *self,
    qreal pixelSize) {
  return self->QCoreTextFontEngine::cloneWithSize(pixelSize);
}

//  int QCoreTextFontEngine::glyphMargin(QFontEngine::GlyphFormat format)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN19QCoreTextFontEngine11glyphMarginEN11QFontEngine11GlyphFormatE(
    QCoreTextFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->QCoreTextFontEngine::glyphMargin(format);
}

//  QFontEngine::Properties QCoreTextFontEngine::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_own_ZNK19QCoreTextFontEngine10propertiesEv(
    const QCoreTextFontEngine *self) {
  return new QFontEngine::Properties(self->QCoreTextFontEngine::properties());
}

//  void QCoreTextFontEngine::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QCoreTextFontEngine23initializeHeightMetricsEv(
    const QCoreTextFontEngine *self) {
  self->QCoreTextFontEngine::initializeHeightMetrics();
}

#endif  // defined(Q_OS_DARWIN)
