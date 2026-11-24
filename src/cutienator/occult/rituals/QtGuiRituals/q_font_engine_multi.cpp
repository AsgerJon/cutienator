//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qlatin1stringview.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFontEngineMulti may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFontEngineMulti : QFontEngineMulti {
  using QFontEngineMulti::ensureFallbackFamiliesQueried;
  using QFontEngineMulti::shouldLoadFontEngineForCharacter;
  using QFontEngineMulti::loadEngine;
};

//  A QFontEngineMulti that Python can take functions over in. Every QFontEngineMulti
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQFontEngineMultiCall0)(const void *, int *);
typedef glyph_t (*CuteQFontEngineMultiCall1)(const void *, uint, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiCall2)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiCall3)(const void *, glyph_t, int *);
typedef void (*CuteQFontEngineMultiCall4)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineMultiCall5)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineMultiCall6)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall7)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall8)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall9)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall10)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall11)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall12)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall13)(const void *, int *);
typedef const QImage * (*CuteQFontEngineMultiCall14)(const void *, glyph_t, int *);
typedef const QImage * (*CuteQFontEngineMultiCall15)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineMultiCall16)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineMultiCall17)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineMultiCall18)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall19)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineMultiCall20)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiCall21)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiCall22)(const void *, int *);
typedef qreal (*CuteQFontEngineMultiCall23)(const void *, int *);
typedef bool (*CuteQFontEngineMultiCall24)(const void *, const QChar *, int, int *);
typedef QString * (*CuteQFontEngineMultiCall25)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQFontEngineMultiCall26)(const void *, const QLatin1String *, int *);
typedef void (*CuteQFontEngineMultiCall27)(const void *, int *);
typedef bool (*CuteQFontEngineMultiCall28)(const void *, int, uint, int *);
typedef void * (*CuteQFontEngineMultiCall29)(const void *, int, int *);
typedef const QFontEngine::Properties * (*CuteQFontEngineMultiCall30)(const void *, int *);
typedef void (*CuteQFontEngineMultiCall31)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQFontEngineMultiCall32)(const void *, int *);
typedef int (*CuteQFontEngineMultiCall33)(const void *, int *);
typedef bool (*CuteQFontEngineMultiCall34)(const void *, int *);
typedef bool (*CuteQFontEngineMultiCall35)(const void *, int *);
typedef const QFixedPoint * (*CuteQFontEngineMultiCall36)(const void *, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineMultiCall37)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQFontEngineMultiCall38)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQFontEngineMultiCall39)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiCall40)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQFontEngineMultiCall41)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineMultiCall42)(const void *, glyph_t, const QTransform *, int *);
typedef bool (*CuteQFontEngineMultiCall43)(const void *, const QTransform *, int *);
typedef int (*CuteQFontEngineMultiCall44)(const void *, int, int *);
typedef void * (*CuteQFontEngineMultiCall45)(const void *, qreal, int *);
typedef bool (*CuteQFontEngineMultiCall46)(const void *, int *);
typedef bool (*CuteQFontEngineMultiCall47)(const void *, int, int *);
typedef void (*CuteQFontEngineMultiCall48)(const void *, int, int *);
typedef void (*CuteQFontEngineMultiCall49)(const void *, int *);
class CuteQFontEngineMulti : public QFontEngineMulti {
public:
  using QFontEngineMulti::QFontEngineMulti;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphCountEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphIndexEj")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxERK12QGlyphLayout")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEj")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12emSquareSizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6ascentEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9capHeightEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7descentEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7leadingEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7xHeightEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine16averageCharWidthEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEj")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13lineThicknessEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine17underlinePositionEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12maxCharWidthEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14minLeftBearingEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine15minRightBearingEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9canRenderEPK5QChari")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9glyphNameEj")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9findGlyphE13QLatin1String")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij")) {
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

  //  int QFontEngineMulti::glyphCount() const
  int glyphCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontEngineMultiCall0 call = reinterpret_cast<CuteQFontEngineMultiCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::glyphCount();
  }

  //  glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontEngineMultiCall1 call = reinterpret_cast<CuteQFontEngineMultiCall1>(taken[1]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::glyphIndex(ucs4);
  }

  //  glyph_metrics_t QFontEngineMulti::boundingBox(const QGlyphLayout
  //      &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontEngineMultiCall2 call = reinterpret_cast<CuteQFontEngineMultiCall2>(taken[2]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontEngineMultiCall3 call = reinterpret_cast<CuteQFontEngineMultiCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQFontEngineMultiCall4 call = reinterpret_cast<CuteQFontEngineMultiCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQFontEngineMultiCall5 call = reinterpret_cast<CuteQFontEngineMultiCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQFontEngineMultiCall6 call = reinterpret_cast<CuteQFontEngineMultiCall6>(taken[6]);
      call(this, a0, a1, &a2, a3, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineMulti::addOutlineToPath(a0, a1, a2, a3, flags);
  }

  //  QFixed QFontEngineMulti::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontEngineMultiCall7 call = reinterpret_cast<CuteQFontEngineMultiCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::emSquareSize();
  }

  //  QFixed QFontEngineMulti::ascent() const
  QFixed ascent() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontEngineMultiCall8 call = reinterpret_cast<CuteQFontEngineMultiCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::ascent();
  }

  //  QFixed QFontEngineMulti::capHeight() const
  QFixed capHeight() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontEngineMultiCall9 call = reinterpret_cast<CuteQFontEngineMultiCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::capHeight();
  }

  //  QFixed QFontEngineMulti::descent() const
  QFixed descent() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontEngineMultiCall10 call = reinterpret_cast<CuteQFontEngineMultiCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::descent();
  }

  //  QFixed QFontEngineMulti::leading() const
  QFixed leading() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontEngineMultiCall11 call = reinterpret_cast<CuteQFontEngineMultiCall11>(taken[11]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::leading();
  }

  //  QFixed QFontEngineMulti::xHeight() const
  QFixed xHeight() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontEngineMultiCall12 call = reinterpret_cast<CuteQFontEngineMultiCall12>(taken[12]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::xHeight();
  }

  //  QFixed QFontEngineMulti::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontEngineMultiCall13 call = reinterpret_cast<CuteQFontEngineMultiCall13>(taken[13]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::averageCharWidth();
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontEngineMultiCall14 call = reinterpret_cast<CuteQFontEngineMultiCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQFontEngineMultiCall15 call = reinterpret_cast<CuteQFontEngineMultiCall15>(taken[15]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
  //      QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontEngineMultiCall16 call = reinterpret_cast<CuteQFontEngineMultiCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQFontEngineMultiCall17 call = reinterpret_cast<CuteQFontEngineMultiCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQFontEngineMultiCall18 call = reinterpret_cast<CuteQFontEngineMultiCall18>(taken[18]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QFixed QFontEngineMulti::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontEngineMultiCall19 call = reinterpret_cast<CuteQFontEngineMultiCall19>(taken[19]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::lineThickness();
  }

  //  QFixed QFontEngineMulti::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontEngineMultiCall20 call = reinterpret_cast<CuteQFontEngineMultiCall20>(taken[20]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineMulti::underlinePosition();
  }

  //  qreal QFontEngineMulti::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontEngineMultiCall21 call = reinterpret_cast<CuteQFontEngineMultiCall21>(taken[21]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::maxCharWidth();
  }

  //  qreal QFontEngineMulti::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontEngineMultiCall22 call = reinterpret_cast<CuteQFontEngineMultiCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::minLeftBearing();
  }

  //  qreal QFontEngineMulti::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontEngineMultiCall23 call = reinterpret_cast<CuteQFontEngineMultiCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::minRightBearing();
  }

  //  bool QFontEngineMulti::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontEngineMultiCall24 call = reinterpret_cast<CuteQFontEngineMultiCall24>(taken[24]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::canRender(string, len);
  }

  //  QString QFontEngineMulti::glyphName(glyph_t glyph) const
  QString glyphName(glyph_t glyph) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontEngineMultiCall25 call = reinterpret_cast<CuteQFontEngineMultiCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQFontEngineMultiCall26 call = reinterpret_cast<CuteQFontEngineMultiCall26>(taken[26]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::findGlyph(name);
  }

  //  void QFontEngineMulti::ensureFallbackFamiliesQueried()
  void ensureFallbackFamiliesQueried() override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontEngineMultiCall27 call = reinterpret_cast<CuteQFontEngineMultiCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngineMulti::ensureFallbackFamiliesQueried();
  }

  //  bool QFontEngineMulti::shouldLoadFontEngineForCharacter(int at, uint
  //      ucs4) const
  bool shouldLoadFontEngineForCharacter(int at, uint ucs4) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontEngineMultiCall28 call = reinterpret_cast<CuteQFontEngineMultiCall28>(taken[28]);
      bool given = call(this, at, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineMulti::shouldLoadFontEngineForCharacter(at, ucs4);
  }

  //  QFontEngine *QFontEngineMulti::loadEngine(int at)
  QFontEngine *loadEngine(int at) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontEngineMultiCall29 call = reinterpret_cast<CuteQFontEngineMultiCall29>(taken[29]);
      void * given = call(this, at, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngineMulti::loadEngine(at);
  }

  //  Properties QFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontEngineMultiCall30 call = reinterpret_cast<CuteQFontEngineMultiCall30>(taken[30]);
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
      CuteQFontEngineMultiCall31 call = reinterpret_cast<CuteQFontEngineMultiCall31>(taken[31]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontEngineMultiCall32 call = reinterpret_cast<CuteQFontEngineMultiCall32>(taken[32]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::faceId();
  }

  //  int QFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontEngineMultiCall33 call = reinterpret_cast<CuteQFontEngineMultiCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::synthesized();
  }

  //  bool QFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontEngineMultiCall34 call = reinterpret_cast<CuteQFontEngineMultiCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontEngineMultiCall35 call = reinterpret_cast<CuteQFontEngineMultiCall35>(taken[35]);
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
      CuteQFontEngineMultiCall36 call = reinterpret_cast<CuteQFontEngineMultiCall36>(taken[36]);
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
      CuteQFontEngineMultiCall37 call = reinterpret_cast<CuteQFontEngineMultiCall37>(taken[37]);
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
      CuteQFontEngineMultiCall38 call = reinterpret_cast<CuteQFontEngineMultiCall38>(taken[38]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontEngineMultiCall39 call = reinterpret_cast<CuteQFontEngineMultiCall39>(taken[39]);
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
      CuteQFontEngineMultiCall40 call = reinterpret_cast<CuteQFontEngineMultiCall40>(taken[40]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontEngineMultiCall41 call = reinterpret_cast<CuteQFontEngineMultiCall41>(taken[41]);
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
      CuteQFontEngineMultiCall42 call = reinterpret_cast<CuteQFontEngineMultiCall42>(taken[42]);
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
      CuteQFontEngineMultiCall43 call = reinterpret_cast<CuteQFontEngineMultiCall43>(taken[43]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsTransformation(transform);
  }

  //  int QFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontEngineMultiCall44 call = reinterpret_cast<CuteQFontEngineMultiCall44>(taken[44]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphMargin(format);
  }

  //  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
  QFontEngine *cloneWithSize(qreal a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontEngineMultiCall45 call = reinterpret_cast<CuteQFontEngineMultiCall45>(taken[45]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngine::cloneWithSize(a0);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontEngineMultiCall46 call = reinterpret_cast<CuteQFontEngineMultiCall46>(taken[46]);
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
      CuteQFontEngineMultiCall47 call = reinterpret_cast<CuteQFontEngineMultiCall47>(taken[47]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQFontEngineMultiCall48 call = reinterpret_cast<CuteQFontEngineMultiCall48>(taken[48]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQFontEngineMultiCall49 call = reinterpret_cast<CuteQFontEngineMultiCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngine::initializeHeightMetrics();
  }
};

//  QFontEngineMulti::QFontEngineMulti(QFontEngine *engine, int script, const
//      QStringList &fallbackFamilies)
extern "C" Q_DECL_EXPORT
QFontEngineMulti *ritual_ZN16QFontEngineMultiC1EP11QFontEngineiRK5QListI7QStringE(
    QFontEngine *engine,
    int script,
    const QList<QString> *fallbackFamilies) {
  return new CuteQFontEngineMulti(engine, script, *fallbackFamilies);
}

//  QFontEngineMulti::~QFontEngineMulti()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMultiD1Ev(QFontEngineMulti *self) {
  delete self;
}

//  int QFontEngineMulti::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFontEngineMulti10glyphCountEv(
    const QFontEngineMulti *self) {
  return self->glyphCount();
}

//  glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK16QFontEngineMulti10glyphIndexEj(
    const QFontEngineMulti *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  int QFontEngineMulti::stringToCMap(const QChar *str, int len,
//      QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFontEngineMulti12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineMulti *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str,
      len,
      glyphs,
      nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  glyph_metrics_t QFontEngineMulti::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN16QFontEngineMulti11boundingBoxERK12QGlyphLayout(
    QFontEngineMulti *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN16QFontEngineMulti11boundingBoxEj(
    QFontEngineMulti *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->boundingBox(glyph));
}

//  void QFontEngineMulti::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFontEngineMulti14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineMulti *self,
    QGlyphLayout *a0,
    int a1) {
  self->recalcAdvances(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineMulti::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFontEngineMulti9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineMulti *self,
    QGlyphLayout *a0,
    int a1) {
  self->doKerning(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineMulti::addOutlineToPath(qreal a0, qreal a1, const
//      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMulti16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineMulti *self,
    qreal a0,
    qreal a1,
    const QGlyphLayout *a2,
    QPainterPath *a3,
    int flags) {
  self->addOutlineToPath(
      a0,
      a1,
      *a2,
      a3,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  void QFontEngineMulti::getGlyphBearings(glyph_t glyph, qreal
//      *leftBearing, qreal *rightBearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMulti16getGlyphBearingsEjPdS0_(
    QFontEngineMulti *self,
    glyph_t glyph,
    qreal *leftBearing,
    qreal *rightBearing) {
  self->getGlyphBearings(glyph, leftBearing, rightBearing);
}

//  QFixed QFontEngineMulti::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti12emSquareSizeEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->emSquareSize());
}

//  QFixed QFontEngineMulti::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti6ascentEv(const QFontEngineMulti *self) {
  return new QFixed(self->ascent());
}

//  QFixed QFontEngineMulti::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti9capHeightEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QFontEngineMulti::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti7descentEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->descent());
}

//  QFixed QFontEngineMulti::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti7leadingEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->leading());
}

//  QFixed QFontEngineMulti::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti7xHeightEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->xHeight());
}

//  QFixed QFontEngineMulti::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti16averageCharWidthEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->averageCharWidth());
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QFontEngineMulti16alphaMapForGlyphEj(
    QFontEngineMulti *self,
    glyph_t a0) {
  return new QImage(self->alphaMapForGlyph(a0));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t glyph, const
//      QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngineMulti *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const QTransform
//      &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(a0, *t));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(a0, *subPixelPosition, *t));
}

//  QImage QFontEngineMulti::alphaRGBMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN16QFontEngineMulti19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  QFixed QFontEngineMulti::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti13lineThicknessEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->lineThickness());
}

//  QFixed QFontEngineMulti::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK16QFontEngineMulti17underlinePositionEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->underlinePosition());
}

//  qreal QFontEngineMulti::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QFontEngineMulti12maxCharWidthEv(
    const QFontEngineMulti *self) {
  return self->maxCharWidth();
}

//  qreal QFontEngineMulti::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QFontEngineMulti14minLeftBearingEv(
    const QFontEngineMulti *self) {
  return self->minLeftBearing();
}

//  qreal QFontEngineMulti::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QFontEngineMulti15minRightBearingEv(
    const QFontEngineMulti *self) {
  return self->minRightBearing();
}

//  QList<QFontVariableAxis> QFontEngineMulti::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK16QFontEngineMulti12variableAxesEv(
    const QFontEngineMulti *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  bool QFontEngineMulti::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFontEngineMulti9canRenderEPK5QChari(
    const QFontEngineMulti *self,
    const QChar *string,
    int len) {
  return self->canRender(string, len);
}

//  QString QFontEngineMulti::glyphName(glyph_t glyph) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFontEngineMulti9glyphNameEj(
    const QFontEngineMulti *self,
    glyph_t glyph) {
  return new QString(self->glyphName(glyph));
}

//  glyph_t QFontEngineMulti::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK16QFontEngineMulti9findGlyphE13QLatin1String(
    const QFontEngineMulti *self,
    const QLatin1String *name) {
  return self->findGlyph(*name);
}

//  int QFontEngineMulti::fallbackFamilyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QFontEngineMulti19fallbackFamilyCountEv(
    const QFontEngineMulti *self) {
  return self->fallbackFamilyCount();
}

//  QString QFontEngineMulti::fallbackFamilyAt(int at) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QFontEngineMulti16fallbackFamilyAtEi(
    const QFontEngineMulti *self,
    int at) {
  return new QString(self->fallbackFamilyAt(at));
}

//  void QFontEngineMulti::setFallbackFamiliesList(const QStringList
//      &fallbackFamilies)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMulti23setFallbackFamiliesListERK5QListI7QStringE(
    QFontEngineMulti *self,
    const QList<QString> *fallbackFamilies) {
  self->setFallbackFamiliesList(*fallbackFamilies);
}

//  uchar QFontEngineMulti::highByte(glyph_t glyph)
extern "C" Q_DECL_EXPORT
uchar ritual_ZN16QFontEngineMulti8highByteEj(glyph_t glyph) {
  return QFontEngineMulti::highByte(glyph);
}

//  QFontEngine *QFontEngineMulti::engine(int at) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK16QFontEngineMulti6engineEi(
    const QFontEngineMulti *self,
    int at) {
  return self->engine(at);
}

//  void QFontEngineMulti::ensureEngineAt(int at)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMulti14ensureEngineAtEi(
    QFontEngineMulti *self,
    int at) {
  self->ensureEngineAt(at);
}

//  QFontEngine *QFontEngineMulti::createMultiFontEngine(QFontEngine *fe, int
//      script)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN16QFontEngineMulti21createMultiFontEngineEP11QFontEnginei(
    QFontEngine *fe,
    int script) {
  return QFontEngineMulti::createMultiFontEngine(fe, script);
}

//  void QFontEngineMulti::ensureFallbackFamiliesQueried()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv(
    QFontEngineMulti *self) {
  self->ensureFallbackFamiliesQueried();
}

//  bool QFontEngineMulti::shouldLoadFontEngineForCharacter(int at, uint
//      ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij(
    const QFontEngineMulti *self,
    int at,
    uint ucs4) {
  return self->shouldLoadFontEngineForCharacter(at, ucs4);
}

//  QFontEngine *QFontEngineMulti::loadEngine(int at)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZN16QFontEngineMulti10loadEngineEi(
    QFontEngineMulti *self,
    int at) {
  return self->loadEngine(at);
}

//  a Python function taken by a CuteQFontEngineMulti, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontEngineMulti(
    QFontEngineMulti *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontEngineMulti *>(self)->take(key, call);
}

//  int QFontEngineMulti::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QFontEngineMulti10glyphCountEv(
    const QFontEngineMulti *self) {
  return self->QFontEngineMulti::glyphCount();
}

//  glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK16QFontEngineMulti10glyphIndexEj(
    const QFontEngineMulti *self,
    uint ucs4) {
  return self->QFontEngineMulti::glyphIndex(ucs4);
}

//  glyph_metrics_t QFontEngineMulti::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN16QFontEngineMulti11boundingBoxERK12QGlyphLayout(
    QFontEngineMulti *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->QFontEngineMulti::boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN16QFontEngineMulti11boundingBoxEj(
    QFontEngineMulti *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->QFontEngineMulti::boundingBox(glyph));
}

//  void QFontEngineMulti::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK16QFontEngineMulti14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineMulti *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngineMulti::recalcAdvances(
      a0,
      QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineMulti::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK16QFontEngineMulti9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineMulti *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngineMulti::doKerning(
      a0,
      QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineMulti::addOutlineToPath(qreal a0, qreal a1, const
//      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QFontEngineMulti16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineMulti *self,
    qreal a0,
    qreal a1,
    const QGlyphLayout *a2,
    QPainterPath *a3,
    int flags) {
  self->QFontEngineMulti::addOutlineToPath(
      a0,
      a1,
      *a2,
      a3,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  QFixed QFontEngineMulti::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti12emSquareSizeEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::emSquareSize());
}

//  QFixed QFontEngineMulti::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti6ascentEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::ascent());
}

//  QFixed QFontEngineMulti::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti9capHeightEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::capHeight());
}

//  QFixed QFontEngineMulti::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti7descentEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::descent());
}

//  QFixed QFontEngineMulti::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti7leadingEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::leading());
}

//  QFixed QFontEngineMulti::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti7xHeightEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::xHeight());
}

//  QFixed QFontEngineMulti::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti16averageCharWidthEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::averageCharWidth());
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEj(
    QFontEngineMulti *self,
    glyph_t a0) {
  return new QImage(self->QFontEngineMulti::alphaMapForGlyph(a0));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t glyph, const
//      QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngineMulti *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  return new QImage(
      self->QFontEngineMulti::alphaMapForGlyph(
          glyph,
          *subPixelPosition));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const QTransform
//      &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QTransform *t) {
  return new QImage(self->QFontEngineMulti::alphaMapForGlyph(a0, *t));
}

//  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(
      self->QFontEngineMulti::alphaMapForGlyph(
          a0,
          *subPixelPosition,
          *t));
}

//  QImage QFontEngineMulti::alphaRGBMapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN16QFontEngineMulti19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineMulti *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(
      self->QFontEngineMulti::alphaRGBMapForGlyph(
          a0,
          *subPixelPosition,
          *t));
}

//  QFixed QFontEngineMulti::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti13lineThicknessEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::lineThickness());
}

//  QFixed QFontEngineMulti::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK16QFontEngineMulti17underlinePositionEv(
    const QFontEngineMulti *self) {
  return new QFixed(self->QFontEngineMulti::underlinePosition());
}

//  qreal QFontEngineMulti::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK16QFontEngineMulti12maxCharWidthEv(
    const QFontEngineMulti *self) {
  return self->QFontEngineMulti::maxCharWidth();
}

//  qreal QFontEngineMulti::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK16QFontEngineMulti14minLeftBearingEv(
    const QFontEngineMulti *self) {
  return self->QFontEngineMulti::minLeftBearing();
}

//  qreal QFontEngineMulti::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK16QFontEngineMulti15minRightBearingEv(
    const QFontEngineMulti *self) {
  return self->QFontEngineMulti::minRightBearing();
}

//  bool QFontEngineMulti::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QFontEngineMulti9canRenderEPK5QChari(
    const QFontEngineMulti *self,
    const QChar *string,
    int len) {
  return self->QFontEngineMulti::canRender(string, len);
}

//  QString QFontEngineMulti::glyphName(glyph_t glyph) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QFontEngineMulti9glyphNameEj(
    const QFontEngineMulti *self,
    glyph_t glyph) {
  return new QString(self->QFontEngineMulti::glyphName(glyph));
}

//  glyph_t QFontEngineMulti::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK16QFontEngineMulti9findGlyphE13QLatin1String(
    const QFontEngineMulti *self,
    const QLatin1String *name) {
  return self->QFontEngineMulti::findGlyph(*name);
}

//  void QFontEngineMulti::ensureFallbackFamiliesQueried()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv(
    QFontEngineMulti *self) {
  static_cast<OwnQFontEngineMulti *>(self)->OwnQFontEngineMulti::ensureFallbackFamiliesQueried();
}

//  bool QFontEngineMulti::shouldLoadFontEngineForCharacter(int at, uint
//      ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij(
    const QFontEngineMulti *self,
    int at,
    uint ucs4) {
  return static_cast<const OwnQFontEngineMulti *>(self)->OwnQFontEngineMulti::shouldLoadFontEngineForCharacter(
      at,
      ucs4);
}

//  QFontEngine *QFontEngineMulti::loadEngine(int at)
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZN16QFontEngineMulti10loadEngineEi(
    QFontEngineMulti *self,
    int at) {
  return static_cast<OwnQFontEngineMulti *>(self)->OwnQFontEngineMulti::loadEngine(
      at);
}
