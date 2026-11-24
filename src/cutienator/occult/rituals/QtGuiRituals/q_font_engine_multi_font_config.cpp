//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontenginemultifontconfig_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(fontconfig) && QT_CONFIG(freetype) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontenginemultifontconfig_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <cstring>

//  A QFontEngineMultiFontConfig that Python can take functions over in. Every QFontEngineMultiFontConfig
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQFontEngineMultiFontConfigCall0)(const void *, int, uint, int *);
typedef int (*CuteQFontEngineMultiFontConfigCall1)(const void *, int *);
typedef glyph_t (*CuteQFontEngineMultiFontConfigCall2)(const void *, uint, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiFontConfigCall3)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiFontConfigCall4)(const void *, glyph_t, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall5)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall6)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall7)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall8)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall9)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall10)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall11)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall12)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall13)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall14)(const void *, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall15)(const void *, glyph_t, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall16)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall17)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall18)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall19)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall20)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiFontConfigCall21)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiFontConfigCall22)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiFontConfigCall23)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiFontConfigCall24)(const void *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall25)(const void *, const QChar *, int, int *);
typedef QString * (*CuteQFontEngineMultiFontConfigCall26)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQFontEngineMultiFontConfigCall27)(const void *, const QLatin1String *, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall28)(const void *, int *);
typedef void * (*CuteQFontEngineMultiFontConfigCall29)(const void *, int, int *);
typedef const QFontEngine::Properties * (*CuteQFontEngineMultiFontConfigCall30)(const void *, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall31)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQFontEngineMultiFontConfigCall32)(const void *, int *);
typedef int (*CuteQFontEngineMultiFontConfigCall33)(const void *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall34)(const void *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall35)(const void *, int *);
typedef const QFixedPoint * (*CuteQFontEngineMultiFontConfigCall36)(const void *, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineMultiFontConfigCall37)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQFontEngineMultiFontConfigCall38)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall39)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiFontConfigCall40)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall41)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiFontConfigCall42)(const void *, glyph_t, const QTransform *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall43)(const void *, const QTransform *, int *);
typedef int (*CuteQFontEngineMultiFontConfigCall44)(const void *, int, int *);
typedef void * (*CuteQFontEngineMultiFontConfigCall45)(const void *, qreal, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall46)(const void *, int *);
typedef bool (*CuteQFontEngineMultiFontConfigCall47)(const void *, int, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall48)(const void *, int, int *);
typedef void (*CuteQFontEngineMultiFontConfigCall49)(const void *, int *);
class CuteQFontEngineMultiFontConfig : public QFontEngineMultiFontConfig {
public:
  using QFontEngineMultiFontConfig::QFontEngineMultiFontConfig;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphIndexEj")) {
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
    if (!std::strcmp(key, "_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12emSquareSizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6ascentEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9capHeightEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7descentEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7leadingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7xHeightEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine16averageCharWidthEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEj")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13lineThicknessEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine17underlinePositionEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12maxCharWidthEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14minLeftBearingEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine15minRightBearingEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9canRenderEPK5QChari")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9glyphNameEj")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9findGlyphE13QLatin1String")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QFontEngineMulti10loadEngineEi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10propertiesEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6faceIdEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine11synthesizedEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine18hasInternalCachingEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine20removeGlyphFromCacheEj")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEjRK10QTransform")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine22supportsTransformationERK10QTransform")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13cloneWithSizeEd")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine23initializeHeightMetricsEv")) {
      taken[49] = call;
      return true;
    }
    return false;
  }

  //  bool QFontEngineMultiFontConfig::shouldLoadFontEngineForCharacter(int
  //      at, uint ucs4) const
  bool shouldLoadFontEngineForCharacter(int at, uint ucs4) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall0 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall0>(taken[0]);
      bool given = call(this, at, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineMultiFontConfig::shouldLoadFontEngineForCharacter(at, ucs4);
  }

  //  int QFontEngineMulti::glyphCount() const
  int glyphCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall1 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::glyphCount();
  }

  //  glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall2 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall2>(taken[2]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::glyphIndex(ucs4);
  }

  //  glyph_metrics_t QFontEngineMulti::boundingBox(const QGlyphLayout
  //      &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall3 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall3>(taken[3]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall4 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall4>(taken[4]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::boundingBox(glyph);
  }

  //  void QFontEngineMulti::recalcAdvances(QGlyphLayout *a0, ShaperFlags
  //      a1) const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall5 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall5>(taken[5]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineMulti::recalcAdvances(a0, a1);
  }

  //  void QFontEngineMulti::doKerning(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall6 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall6>(taken[6]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineMulti::doKerning(a0, a1);
  }

  //  void QFontEngineMulti::addOutlineToPath(qreal a0, qreal a1, const
  //      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
  void addOutlineToPath(
      qreal a0,
      qreal a1,
      const QGlyphLayout &a2,
      QPainterPath *a3,
      QTextItem::RenderFlags flags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall7 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall7>(taken[7]);
      call(this, a0, a1, &a2, a3, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineMulti::addOutlineToPath(a0, a1, a2, a3, flags);
  }

  //  QFixed QFontEngineMulti::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall8 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::emSquareSize();
  }

  //  QFixed QFontEngineMulti::ascent() const
  QFixed ascent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall9 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::ascent();
  }

  //  QFixed QFontEngineMulti::capHeight() const
  QFixed capHeight() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall10 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::capHeight();
  }

  //  QFixed QFontEngineMulti::descent() const
  QFixed descent() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall11 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall11>(taken[11]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::descent();
  }

  //  QFixed QFontEngineMulti::leading() const
  QFixed leading() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall12 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall12>(taken[12]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::leading();
  }

  //  QFixed QFontEngineMulti::xHeight() const
  QFixed xHeight() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall13 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall13>(taken[13]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::xHeight();
  }

  //  QFixed QFontEngineMulti::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall14 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall14>(taken[14]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::averageCharWidth();
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall15 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall15>(taken[15]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaMapForGlyph(a0);
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t glyph, const
  //      QFixedPoint &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall16 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall16>(taken[16]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
  //      QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall17 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall17>(taken[17]);
      const QImage * given = call(this, a0, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaMapForGlyph(a0, t);
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
  //      QFixedPoint &subPixelPosition, const QTransform &t)
  QImage alphaMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall18 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall18>(taken[18]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngineMulti::alphaRGBMapForGlyph(glyph_t a0, const
  //      QFixedPoint &subPixelPosition, const QTransform &t)
  QImage alphaRGBMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall19 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall19>(taken[19]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QFixed QFontEngineMulti::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall20 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall20>(taken[20]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::lineThickness();
  }

  //  QFixed QFontEngineMulti::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall21 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall21>(taken[21]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::underlinePosition();
  }

  //  qreal QFontEngineMulti::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall22 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::maxCharWidth();
  }

  //  qreal QFontEngineMulti::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall23 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::minLeftBearing();
  }

  //  qreal QFontEngineMulti::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall24 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall24>(taken[24]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::minRightBearing();
  }

  //  bool QFontEngineMulti::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall25 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall25>(taken[25]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::canRender(string, len);
  }

  //  QString QFontEngineMulti::glyphName(glyph_t glyph) const
  QString glyphName(glyph_t glyph) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall26 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall26>(taken[26]);
      QString * given = call(this, glyph, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontEngineMulti::glyphName(glyph);
  }

  //  glyph_t QFontEngineMulti::findGlyph(QLatin1StringView name) const
  glyph_t findGlyph(QLatin1StringView name) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall27 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall27>(taken[27]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::findGlyph(name);
  }

  //  void QFontEngineMulti::ensureFallbackFamiliesQueried()
  void ensureFallbackFamiliesQueried() override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall28 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngineMulti::ensureFallbackFamiliesQueried();
  }

  //  QFontEngine *QFontEngineMulti::loadEngine(int at)
  QFontEngine *loadEngine(int at) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall29 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall29>(taken[29]);
      void * given = call(this, at, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngineMulti::loadEngine(at);
  }

  //  Properties QFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall30 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall31 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall31>(taken[31]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall32 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall32>(taken[32]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::faceId();
  }

  //  int QFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall33 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::synthesized();
  }

  //  bool QFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall34 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall35 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall36 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall36>(taken[36]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t, const QColor &color)
  QImage bitmapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t,
      const QColor &color) override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall37 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall38 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall38>(taken[38]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall39 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall40 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall40>(taken[40]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall41 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall41>(taken[41]);
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
    if (taken[42]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall42 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall42>(taken[42]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyph, matrix);
  }

  //  bool QFontEngine::supportsTransformation(const QTransform &transform)
  //      const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall43 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall43>(taken[43]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsTransformation(transform);
  }

  //  int QFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall44 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall44>(taken[44]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphMargin(format);
  }

  //  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
  QFontEngine *cloneWithSize(qreal a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall45 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall45>(taken[45]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngine::cloneWithSize(a0);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall46 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall47 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall47>(taken[47]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall48 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall48>(taken[48]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQFontEngineMultiFontConfigCall49 call = reinterpret_cast<CuteQFontEngineMultiFontConfigCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngine::initializeHeightMetrics();
  }
};

//  QFontEngineMultiFontConfig::QFontEngineMultiFontConfig(QFontEngine *fe,
//      int script)
extern "C" Q_DECL_EXPORT
QFontEngineMultiFontConfig *ritual_ZN26QFontEngineMultiFontConfigC1EP11QFontEnginei(
    QFontEngine *fe,
    int script) {
  return new CuteQFontEngineMultiFontConfig(fe, script);
}

//  QFontEngineMultiFontConfig::~QFontEngineMultiFontConfig()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QFontEngineMultiFontConfigD1Ev(
    QFontEngineMultiFontConfig *self) {
  delete self;
}

//  bool QFontEngineMultiFontConfig::shouldLoadFontEngineForCharacter(int at,
//      uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QFontEngineMultiFontConfig32shouldLoadFontEngineForCharacterEij(
    const QFontEngineMultiFontConfig *self,
    int at,
    uint ucs4) {
  return self->shouldLoadFontEngineForCharacter(at, ucs4);
}

//  a Python function taken by a CuteQFontEngineMultiFontConfig, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontEngineMultiFontConfig(
    QFontEngineMultiFontConfig *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontEngineMultiFontConfig *>(self)->take(key, call);
}

//  bool QFontEngineMultiFontConfig::shouldLoadFontEngineForCharacter(int at,
//      uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QFontEngineMultiFontConfig32shouldLoadFontEngineForCharacterEij(
    const QFontEngineMultiFontConfig *self,
    int at,
    uint ucs4) {
  return self->QFontEngineMultiFontConfig::shouldLoadFontEngineForCharacter(
      at,
      ucs4);
}

#endif  // QT_CONFIG(fontconfig) && QT_CONFIG(freetype) && defined(Q_OS_UNIX) && !defined(Q_OS_DARWIN)
