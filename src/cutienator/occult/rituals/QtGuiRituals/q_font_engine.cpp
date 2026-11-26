//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFontEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFontEngine : QFontEngine {
  using QFontEngine::initializeHeightMetrics;
};

//  A QFontEngine that Python can take functions over in. Every QFontEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QFontEngine::Properties * (*CuteQFontEngineCall0)(const void *, int *);
typedef void (*CuteQFontEngineCall1)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQFontEngineCall2)(const void *, int *);
typedef int (*CuteQFontEngineCall3)(const void *, int *);
typedef bool (*CuteQFontEngineCall4)(const void *, int *);
typedef bool (*CuteQFontEngineCall5)(const void *, int *);
typedef const QFixedPoint * (*CuteQFontEngineCall6)(const void *, const QFixedPoint *, int *);
typedef const QFixed * (*CuteQFontEngineCall7)(const void *, int *);
typedef glyph_t (*CuteQFontEngineCall8)(const void *, uint, int *);
typedef void (*CuteQFontEngineCall9)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineCall10)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineCall11)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const QImage * (*CuteQFontEngineCall12)(const void *, glyph_t, int *);
typedef const QImage * (*CuteQFontEngineCall13)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineCall14)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineCall15)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineCall16)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineCall17)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQFontEngineCall18)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQFontEngineCall19)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineCall20)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQFontEngineCall21)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineCall22)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineCall23)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineCall24)(const void *, glyph_t, const QTransform *, int *);
typedef const QFixed * (*CuteQFontEngineCall25)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall26)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall27)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall28)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall29)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall30)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall31)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineCall32)(const void *, int *);
typedef qreal (*CuteQFontEngineCall33)(const void *, int *);
typedef qreal (*CuteQFontEngineCall34)(const void *, int *);
typedef qreal (*CuteQFontEngineCall35)(const void *, int *);
typedef bool (*CuteQFontEngineCall36)(const void *, const QChar *, int, int *);
typedef bool (*CuteQFontEngineCall37)(const void *, const QTransform *, int *);
typedef int (*CuteQFontEngineCall38)(const void *, int *);
typedef int (*CuteQFontEngineCall39)(const void *, int, int *);
typedef void * (*CuteQFontEngineCall40)(const void *, qreal, int *);
typedef void * (*CuteQFontEngineCall41)(const void *, int *);
typedef QString * (*CuteQFontEngineCall42)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQFontEngineCall43)(const void *, const QLatin1String *, int *);
typedef bool (*CuteQFontEngineCall44)(const void *, int *);
typedef bool (*CuteQFontEngineCall45)(const void *, int, int *);
typedef void (*CuteQFontEngineCall46)(const void *, int, int *);
typedef void (*CuteQFontEngineCall47)(const void *, int *);
class CuteQFontEngine : public QFontEngine {
public:
  using QFontEngine::QFontEngine;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QFontEngine10propertiesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6faceIdEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine11synthesizedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12emSquareSizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphIndexEj")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEj")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine18hasInternalCachingEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine20removeGlyphFromCacheEj")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxERK12QGlyphLayout")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEj")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEjRK10QTransform")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6ascentEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9capHeightEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7descentEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7leadingEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7xHeightEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine16averageCharWidthEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13lineThicknessEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine17underlinePositionEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12maxCharWidthEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14minLeftBearingEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine15minRightBearingEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9canRenderEPK5QChari")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine22supportsTransformationERK10QTransform")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphCountEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13cloneWithSizeEd")) {
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

  //  Properties QFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontEngineCall0 call = reinterpret_cast<CuteQFontEngineCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQFontEngineCall1 call = reinterpret_cast<CuteQFontEngineCall1>(taken[1]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontEngineCall2 call = reinterpret_cast<CuteQFontEngineCall2>(taken[2]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::faceId();
  }

  //  int QFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontEngineCall3 call = reinterpret_cast<CuteQFontEngineCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::synthesized();
  }

  //  bool QFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontEngineCall4 call = reinterpret_cast<CuteQFontEngineCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontEngineCall5 call = reinterpret_cast<CuteQFontEngineCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontEngineCall6 call = reinterpret_cast<CuteQFontEngineCall6>(taken[6]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  QFixed QFontEngine::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontEngineCall7 call = reinterpret_cast<CuteQFontEngineCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::emSquareSize();
  }

  //  glyph_t QFontEngine::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontEngineCall8 call = reinterpret_cast<CuteQFontEngineCall8>(taken[8]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontEngineCall9 call = reinterpret_cast<CuteQFontEngineCall9>(taken[9]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::recalcAdvances(a0, a1);
  }

  //  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontEngineCall10 call = reinterpret_cast<CuteQFontEngineCall10>(taken[10]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::doKerning(a0, a1);
  }

  //  void QFontEngine::addOutlineToPath(qreal a0, qreal a1, const
  //      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
  void addOutlineToPath(
      qreal a0,
      qreal a1,
      const QGlyphLayout &a2,
      QPainterPath *a3,
      QTextItem::RenderFlags flags) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontEngineCall11 call = reinterpret_cast<CuteQFontEngineCall11>(taken[11]);
      call(this, a0, a1, &a2, a3, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::addOutlineToPath(a0, a1, a2, a3, flags);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontEngineCall12 call = reinterpret_cast<CuteQFontEngineCall12>(taken[12]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontEngineCall13 call = reinterpret_cast<CuteQFontEngineCall13>(taken[13]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontEngineCall14 call = reinterpret_cast<CuteQFontEngineCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQFontEngineCall15 call = reinterpret_cast<CuteQFontEngineCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQFontEngineCall16 call = reinterpret_cast<CuteQFontEngineCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQFontEngineCall17 call = reinterpret_cast<CuteQFontEngineCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQFontEngineCall18 call = reinterpret_cast<CuteQFontEngineCall18>(taken[18]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontEngineCall19 call = reinterpret_cast<CuteQFontEngineCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQFontEngineCall20 call = reinterpret_cast<CuteQFontEngineCall20>(taken[20]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontEngineCall21 call = reinterpret_cast<CuteQFontEngineCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontEngine::removeGlyphFromCache(a0);
  }

  //  glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontEngineCall22 call = reinterpret_cast<CuteQFontEngineCall22>(taken[22]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontEngineCall23 call = reinterpret_cast<CuteQFontEngineCall23>(taken[23]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const
  //      QTransform &matrix)
  glyph_metrics_t boundingBox(
      glyph_t glyph,
      const QTransform &matrix) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontEngineCall24 call = reinterpret_cast<CuteQFontEngineCall24>(taken[24]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyph, matrix);
  }

  //  QFixed QFontEngine::ascent() const
  QFixed ascent() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontEngineCall25 call = reinterpret_cast<CuteQFontEngineCall25>(taken[25]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::ascent();
  }

  //  QFixed QFontEngine::capHeight() const
  QFixed capHeight() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontEngineCall26 call = reinterpret_cast<CuteQFontEngineCall26>(taken[26]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QFixed QFontEngine::descent() const
  QFixed descent() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontEngineCall27 call = reinterpret_cast<CuteQFontEngineCall27>(taken[27]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::descent();
  }

  //  QFixed QFontEngine::leading() const
  QFixed leading() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontEngineCall28 call = reinterpret_cast<CuteQFontEngineCall28>(taken[28]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::leading();
  }

  //  QFixed QFontEngine::xHeight() const
  QFixed xHeight() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontEngineCall29 call = reinterpret_cast<CuteQFontEngineCall29>(taken[29]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::xHeight();
  }

  //  QFixed QFontEngine::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontEngineCall30 call = reinterpret_cast<CuteQFontEngineCall30>(taken[30]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::averageCharWidth();
  }

  //  QFixed QFontEngine::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQFontEngineCall31 call = reinterpret_cast<CuteQFontEngineCall31>(taken[31]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::lineThickness();
  }

  //  QFixed QFontEngine::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontEngineCall32 call = reinterpret_cast<CuteQFontEngineCall32>(taken[32]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::underlinePosition();
  }

  //  qreal QFontEngine::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontEngineCall33 call = reinterpret_cast<CuteQFontEngineCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qreal QFontEngine::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontEngineCall34 call = reinterpret_cast<CuteQFontEngineCall34>(taken[34]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minLeftBearing();
  }

  //  qreal QFontEngine::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontEngineCall35 call = reinterpret_cast<CuteQFontEngineCall35>(taken[35]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minRightBearing();
  }

  //  bool QFontEngine::canRender(const QChar *str, int len) const
  bool canRender(const QChar *str, int len) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontEngineCall36 call = reinterpret_cast<CuteQFontEngineCall36>(taken[36]);
      bool given = call(this, str, len, &handled);
      if (handled) return given;
    }
    return QFontEngine::canRender(str, len);
  }

  //  bool QFontEngine::supportsTransformation(const QTransform &transform)
  //      const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontEngineCall37 call = reinterpret_cast<CuteQFontEngineCall37>(taken[37]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsTransformation(transform);
  }

  //  int QFontEngine::glyphCount() const
  int glyphCount() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQFontEngineCall38 call = reinterpret_cast<CuteQFontEngineCall38>(taken[38]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphCount();
  }

  //  int QFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontEngineCall39 call = reinterpret_cast<CuteQFontEngineCall39>(taken[39]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphMargin(format);
  }

  //  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
  QFontEngine *cloneWithSize(qreal a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFontEngineCall40 call = reinterpret_cast<CuteQFontEngineCall40>(taken[40]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngine::cloneWithSize(a0);
  }

  //  Qt::HANDLE QFontEngine::handle() const
  Qt::HANDLE handle() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontEngineCall41 call = reinterpret_cast<CuteQFontEngineCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return QFontEngine::handle();
  }

  //  QString QFontEngine::glyphName(glyph_t index) const
  QString glyphName(glyph_t index) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFontEngineCall42 call = reinterpret_cast<CuteQFontEngineCall42>(taken[42]);
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
      CuteQFontEngineCall43 call = reinterpret_cast<CuteQFontEngineCall43>(taken[43]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngine::findGlyph(name);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontEngineCall44 call = reinterpret_cast<CuteQFontEngineCall44>(taken[44]);
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
      CuteQFontEngineCall45 call = reinterpret_cast<CuteQFontEngineCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontEngineCall46 call = reinterpret_cast<CuteQFontEngineCall46>(taken[46]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQFontEngineCall47 call = reinterpret_cast<CuteQFontEngineCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngine::initializeHeightMetrics();
  }
};

//  QFontEngine::~QFontEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngineD1Ev(QFontEngine *self) {
  delete self;
}

//  Type QFontEngine::type() const
extern "C" Q_DECL_EXPORT
QFontEngine::Type ritual_ZNK11QFontEngine4typeEv(const QFontEngine *self) {
  return self->type();
}

//  Properties QFontEngine::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK11QFontEngine10propertiesEv(
    const QFontEngine *self) {
  return new QFontEngine::Properties(self->properties());
}

//  void QFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
//      glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QFontEngine *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->getUnscaledGlyph(glyph, path, metrics);
}

//  QByteArray QFontEngine::getSfntTable(uint tag) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QFontEngine12getSfntTableEj(
    const QFontEngine *self,
    uint tag) {
  return new QByteArray(self->getSfntTable(tag));
}

//  bool QFontEngine::getSfntTableData(uint tag, uchar *buffer, uint *length)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine16getSfntTableDataEjPhPj(
    const QFontEngine *self,
    uint tag,
    uchar *buffer,
    uint *length) {
  return self->getSfntTableData(tag, buffer, length);
}

//  FaceId QFontEngine::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_ZNK11QFontEngine6faceIdEv(
    const QFontEngine *self) {
  return new QFontEngine::FaceId(self->faceId());
}

//  int QFontEngine::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFontEngine11synthesizedEv(const QFontEngine *self) {
  return self->synthesized();
}

//  bool QFontEngine::supportsSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine25supportsSubPixelPositionsEv(
    const QFontEngine *self) {
  return self->supportsSubPixelPositions();
}

//  bool QFontEngine::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv(
    const QFontEngine *self) {
  return self->supportsHorizontalSubPixelPositions();
}

//  bool QFontEngine::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv(
    const QFontEngine *self) {
  return self->supportsVerticalSubPixelPositions();
}

//  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint &position)
//      const
extern "C" Q_DECL_EXPORT
QFixedPoint *ritual_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint(
    const QFontEngine *self,
    const QFixedPoint *position) {
  return new QFixedPoint(self->subPixelPositionFor(*position));
}

//  QFixed QFontEngine::subPixelPositionForX(QFixed x) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine20subPixelPositionForXE6QFixed(
    const QFontEngine *self,
    const QFixed *x) {
  return new QFixed(self->subPixelPositionForX(*x));
}

//  bool QFontEngine::preferTypoLineMetrics() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine21preferTypoLineMetricsEv(
    const QFontEngine *self) {
  return self->preferTypoLineMetrics();
}

//  bool QFontEngine::isColorFont() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine11isColorFontEv(const QFontEngine *self) {
  return self->isColorFont();
}

//  bool QFontEngine::isIgnorableChar(char32_t ucs4)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontEngine15isIgnorableCharEDi(char32_t ucs4) {
  return QFontEngine::isIgnorableChar(ucs4);
}

//  int QFontEngine::maxCachedGlyphSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QFontEngine18maxCachedGlyphSizeEv() {
  return QFontEngine::maxCachedGlyphSize();
}

//  QFixed QFontEngine::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine12emSquareSizeEv(const QFontEngine *self) {
  return new QFixed(self->emSquareSize());
}

//  glyph_t QFontEngine::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK11QFontEngine10glyphIndexEj(
    const QFontEngine *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  int QFontEngine::stringToCMap(const QChar *str, int len, QGlyphLayout
//      *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFontEngine12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsINS_10ShaperFlagEE(
    const QFontEngine *self,
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

//  void QFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE(
    const QFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->recalcAdvances(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE(
    const QFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->doKerning(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
//      *positions, int nglyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine15addGlyphsToPathEPjP11QFixedPointiP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngine *self,
    glyph_t *glyphs,
    QFixedPoint *positions,
    int nglyphs,
    QPainterPath *path,
    int flags) {
  self->addGlyphsToPath(
      glyphs,
      positions,
      nglyphs,
      path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  void QFontEngine::getGlyphPositions(const QGlyphLayout &glyphs, const
//      QTransform &matrix, QTextItem::RenderFlags flags,
//      QVarLengthArray<glyph_t> &glyphs_out, QVarLengthArray<QFixedPoint>
//      &positions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine17getGlyphPositionsERK12QGlyphLayoutRK10QTransform6QFlagsIN9QTextItem10RenderFlagEER15QVarLengthArrayIjLx256EERSA_I11QFixedPointLx256EE(
    QFontEngine *self,
    const QGlyphLayout *glyphs,
    const QTransform *matrix,
    int flags,
    QVarLengthArray<glyph_t> *glyphs_out,
    QVarLengthArray<QFixedPoint> *positions) {
  self->getGlyphPositions(
      *glyphs,
      *matrix,
      QFlags<QTextItem::RenderFlag>::fromInt(flags),
      *glyphs_out,
      *positions);
}

//  void QFontEngine::addOutlineToPath(qreal a0, qreal a1, const QGlyphLayout
//      &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngine *self,
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

//  void QFontEngine::addBitmapFontToPath(qreal x, qreal y, const
//      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine19addBitmapFontToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngine *self,
    qreal x,
    qreal y,
    const QGlyphLayout *a2,
    QPainterPath *a3,
    int a4) {
  self->addBitmapFontToPath(
      x,
      y,
      *a2,
      a3,
      QFlags<QTextItem::RenderFlag>::fromInt(a4));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine16alphaMapForGlyphEj(
    QFontEngine *self,
    glyph_t a0) {
  return new QImage(self->alphaMapForGlyph(a0));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
//      &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(a0, *t));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(a0, *subPixelPosition, *t));
}

//  QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  QImage QFontEngine::renderedPathForGlyph(glyph_t glyph, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QFontEngine20renderedPathForGlyphEjRK6QColor(
    QFontEngine *self,
    glyph_t glyph,
    const QColor *color) {
  return new QImage(self->renderedPathForGlyph(glyph, *color));
}

//  qreal QFontEngine::effectivePixelSizeSquared(const QTransform &transform)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QFontEngine25effectivePixelSizeSquaredERK10QTransform(
    const QFontEngine *self,
    const QTransform *transform) {
  return self->effectivePixelSizeSquared(*transform);
}

//  bool QFontEngine::glyphBoundingBoxExceedsLimit(qreal glyphWidth, qreal
//      glyphHeight, qreal effectivePixelSizeSquared)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontEngine28glyphBoundingBoxExceedsLimitEddd(
    qreal glyphWidth,
    qreal glyphHeight,
    qreal effectivePixelSizeSquared) {
  return QFontEngine::glyphBoundingBoxExceedsLimit(
      glyphWidth,
      glyphHeight,
      effectivePixelSizeSquared);
}

//  bool QFontEngine::glyphTransformExceedsLimit(glyph_t glyph, const
//      QTransform &transform)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontEngine26glyphTransformExceedsLimitEjRK10QTransform(
    QFontEngine *self,
    glyph_t glyph,
    const QTransform *transform) {
  return self->glyphTransformExceedsLimit(glyph, *transform);
}

//  Glyph *QFontEngine::glyphData(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat neededFormat,
    const QTransform *t) {
  return self->glyphData(glyph, *subPixelPosition, neededFormat, *t);
}

//  bool QFontEngine::hasInternalCaching() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine18hasInternalCachingEv(const QFontEngine *self) {
  return self->hasInternalCaching();
}

//  glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t glyph, const
//      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->alphaMapBoundingBox(
          glyph,
          *a1,
          *matrix,
          a3));
}

//  void QFontEngine::removeGlyphFromCache(glyph_t a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine20removeGlyphFromCacheEj(
    QFontEngine *self,
    glyph_t a0) {
  self->removeGlyphFromCache(a0);
}

//  glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN11QFontEngine11boundingBoxERK12QGlyphLayout(
    QFontEngine *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN11QFontEngine11boundingBoxEj(
    QFontEngine *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->boundingBox(glyph));
}

//  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const QTransform
//      &matrix)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN11QFontEngine11boundingBoxEjRK10QTransform(
    QFontEngine *self,
    glyph_t glyph,
    const QTransform *matrix) {
  return new glyph_metrics_t(self->boundingBox(glyph, *matrix));
}

//  glyph_metrics_t QFontEngine::tightBoundingBox(const QGlyphLayout &glyphs,
//      QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN11QFontEngine16tightBoundingBoxERK12QGlyphLayout6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngine *self,
    const QGlyphLayout *glyphs,
    int flags) {
  return new glyph_metrics_t(
      self->tightBoundingBox(
          *glyphs,
          QFlags<QTextItem::RenderFlag>::fromInt(flags)));
}

//  QFixed QFontEngine::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine6ascentEv(const QFontEngine *self) {
  return new QFixed(self->ascent());
}

//  QFixed QFontEngine::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine9capHeightEv(const QFontEngine *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QFontEngine::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine7descentEv(const QFontEngine *self) {
  return new QFixed(self->descent());
}

//  QFixed QFontEngine::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine7leadingEv(const QFontEngine *self) {
  return new QFixed(self->leading());
}

//  QFixed QFontEngine::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine7xHeightEv(const QFontEngine *self) {
  return new QFixed(self->xHeight());
}

//  QFixed QFontEngine::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine16averageCharWidthEv(
    const QFontEngine *self) {
  return new QFixed(self->averageCharWidth());
}

//  QFixed QFontEngine::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine13lineThicknessEv(const QFontEngine *self) {
  return new QFixed(self->lineThickness());
}

//  QFixed QFontEngine::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine17underlinePositionEv(
    const QFontEngine *self) {
  return new QFixed(self->underlinePosition());
}

//  qreal QFontEngine::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QFontEngine12maxCharWidthEv(const QFontEngine *self) {
  return self->maxCharWidth();
}

//  qreal QFontEngine::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QFontEngine14minLeftBearingEv(const QFontEngine *self) {
  return self->minLeftBearing();
}

//  qreal QFontEngine::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QFontEngine15minRightBearingEv(const QFontEngine *self) {
  return self->minRightBearing();
}

//  void QFontEngine::getGlyphBearings(glyph_t glyph, qreal *leftBearing,
//      qreal *rightBearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine16getGlyphBearingsEjPdS0_(
    QFontEngine *self,
    glyph_t glyph,
    qreal *leftBearing,
    qreal *rightBearing) {
  self->getGlyphBearings(glyph, leftBearing, rightBearing);
}

//  bool QFontEngine::canRender(uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine9canRenderEj(
    const QFontEngine *self,
    uint ucs4) {
  return self->canRender(ucs4);
}

//  bool QFontEngine::canRender(const QChar *str, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine9canRenderEPK5QChari(
    const QFontEngine *self,
    const QChar *str,
    int len) {
  return self->canRender(str, len);
}

//  bool QFontEngine::supportsTransformation(const QTransform &transform)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine22supportsTransformationERK10QTransform(
    const QFontEngine *self,
    const QTransform *transform) {
  return self->supportsTransformation(*transform);
}

//  int QFontEngine::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFontEngine10glyphCountEv(const QFontEngine *self) {
  return self->glyphCount();
}

//  int QFontEngine::glyphMargin(GlyphFormat format)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE(
    QFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->glyphMargin(format);
}

//  bool QFontEngine::hasHinting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine10hasHintingEv(const QFontEngine *self) {
  return self->hasHinting();
}

//  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK11QFontEngine13cloneWithSizeEd(
    const QFontEngine *self,
    qreal a0) {
  return self->cloneWithSize(a0);
}

//  Qt::HANDLE QFontEngine::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK11QFontEngine6handleEv(const QFontEngine *self) {
  return self->handle();
}

//  QList<QFontVariableAxis> QFontEngine::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK11QFontEngine12variableAxesEv(
    const QFontEngine *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  QString QFontEngine::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFontEngine9glyphNameEj(
    const QFontEngine *self,
    glyph_t index) {
  return new QString(self->glyphName(index));
}

//  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK11QFontEngine9findGlyphE13QLatin1String(
    const QFontEngine *self,
    const QLatin1String *name) {
  return self->findGlyph(*name);
}

//  void *QFontEngine::harfbuzzFont() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QFontEngine12harfbuzzFontEv(const QFontEngine *self) {
  return self->harfbuzzFont();
}

//  void *QFontEngine::harfbuzzFace() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QFontEngine12harfbuzzFaceEv(const QFontEngine *self) {
  return self->harfbuzzFace();
}

//  bool QFontEngine::supportsScript(QChar::Script script) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine14supportsScriptEN5QChar6ScriptE(
    const QFontEngine *self,
    QChar::Script script) {
  return self->supportsScript(script);
}

//  bool QFontEngine::scriptRequiresOpenType(QChar::Script script)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontEngine22scriptRequiresOpenTypeEN5QChar6ScriptE(
    QChar::Script script) {
  return QFontEngine::scriptRequiresOpenType(script);
}

//  int QFontEngine::getPointInOutline(glyph_t glyph, int flags, quint32
//      point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QFontEngine17getPointInOutlineEjijP6QFixedS1_Pj(
    QFontEngine *self,
    glyph_t glyph,
    int flags,
    quint32 point,
    QFixed *xpos,
    QFixed *ypos,
    quint32 *nPoints) {
  return self->getPointInOutline(glyph, flags, point, xpos, ypos, nPoints);
}

//  void QFontEngine::clearGlyphCache(const void *key)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine15clearGlyphCacheEPKv(
    QFontEngine *self,
    const void *key) {
  self->clearGlyphCache(key);
}

//  void QFontEngine::setGlyphCache(const void *key, QFontEngineGlyphCache
//      *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine13setGlyphCacheEPKvP21QFontEngineGlyphCache(
    QFontEngine *self,
    const void *key,
    QFontEngineGlyphCache *data) {
  self->setGlyphCache(key, data);
}

//  QFontEngineGlyphCache *QFontEngine::glyphCache(const void *key,
//      GlyphFormat format, const QTransform &transform, const QColor &color)
//      const
extern "C" Q_DECL_EXPORT
QFontEngineGlyphCache *ritual_ZNK11QFontEngine10glyphCacheEPKvNS_11GlyphFormatERK10QTransformRK6QColor(
    const QFontEngine *self,
    const void *key,
    QFontEngine::GlyphFormat format,
    const QTransform *transform,
    const QColor *color) {
  return self->glyphCache(key, format, *transform, *color);
}

//  const uchar *QFontEngine::getCMap(const uchar *table, uint tableSize,
//      bool *isSymbolFont, int *cmapSize)
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZN11QFontEngine7getCMapEPKhjPbPi(
    const uchar *table,
    uint tableSize,
    bool *isSymbolFont,
    int *cmapSize) {
  return QFontEngine::getCMap(table, tableSize, isSymbolFont, cmapSize);
}

//  quint32 QFontEngine::getTrueTypeGlyphIndex(const uchar *cmap, int
//      cmapSize, uint unicode)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN11QFontEngine21getTrueTypeGlyphIndexEPKhij(
    const uchar *cmap,
    int cmapSize,
    uint unicode) {
  return QFontEngine::getTrueTypeGlyphIndex(cmap, cmapSize, unicode);
}

//  QByteArray QFontEngine::convertToPostscriptFontFamilyName(const
//      QByteArray &fontFamily)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QFontEngine33convertToPostscriptFontFamilyNameERK10QByteArray(
    const QByteArray *fontFamily) {
  return new QByteArray(
      QFontEngine::convertToPostscriptFontFamilyName(
          *fontFamily));
}

//  bool QFontEngine::hasUnreliableGlyphOutline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv(
    const QFontEngine *self) {
  return self->hasUnreliableGlyphOutline();
}

//  bool QFontEngine::expectsGammaCorrectedBlending(QFontEngine::GlyphFormat
//      format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE(
    const QFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->expectsGammaCorrectedBlending(format);
}

//  bool QFontEngine::disableEmojiSegmenter()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFontEngine21disableEmojiSegmenterEv() {
  return QFontEngine::disableEmojiSegmenter();
}

//  void QFontEngine::setDefaultHintStyle(HintStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE(
    QFontEngine *self,
    QFontEngine::HintStyle a0) {
  self->setDefaultHintStyle(a0);
}

//  void QFontEngine::loadKerningPairs(QFixed scalingFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine16loadKerningPairsE6QFixed(
    QFontEngine *self,
    const QFixed *scalingFactor) {
  self->loadKerningPairs(*scalingFactor);
}

//  QFixed QFontEngine::firstLeftBearing(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN11QFontEngine16firstLeftBearingERK12QGlyphLayout(
    QFontEngine *self,
    const QGlyphLayout *glyphs) {
  return new QFixed(self->firstLeftBearing(*glyphs));
}

//  QFixed QFontEngine::lastRightBearing(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN11QFontEngine16lastRightBearingERK12QGlyphLayout(
    QFontEngine *self,
    const QGlyphLayout *glyphs) {
  return new QFixed(self->lastRightBearing(*glyphs));
}

//  QFixed QFontEngine::calculatedCapHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QFontEngine19calculatedCapHeightEv(
    const QFontEngine *self) {
  return new QFixed(self->calculatedCapHeight());
}

//  void QFontEngine::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QFontEngine23initializeHeightMetricsEv(
    const QFontEngine *self) {
  self->initializeHeightMetrics();
}

//  bool QFontEngine::processHheaTable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine16processHheaTableEv(const QFontEngine *self) {
  return self->processHheaTable();
}

//  bool QFontEngine::processOS2Table() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine15processOS2TableEv(const QFontEngine *self) {
  return self->processOS2Table();
}

//  a Python function taken by a CuteQFontEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontEngine(
    QFontEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontEngine *>(self)->take(key, call);
}

//  Properties QFontEngine::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_own_ZNK11QFontEngine10propertiesEv(
    const QFontEngine *self) {
  return new QFontEngine::Properties(self->QFontEngine::properties());
}

//  void QFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
//      glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QFontEngine *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->QFontEngine::getUnscaledGlyph(glyph, path, metrics);
}

//  FaceId QFontEngine::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_own_ZNK11QFontEngine6faceIdEv(
    const QFontEngine *self) {
  return new QFontEngine::FaceId(self->QFontEngine::faceId());
}

//  int QFontEngine::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFontEngine11synthesizedEv(const QFontEngine *self) {
  return self->QFontEngine::synthesized();
}

//  bool QFontEngine::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv(
    const QFontEngine *self) {
  return self->QFontEngine::supportsHorizontalSubPixelPositions();
}

//  bool QFontEngine::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv(
    const QFontEngine *self) {
  return self->QFontEngine::supportsVerticalSubPixelPositions();
}

//  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint &position)
//      const
extern "C" Q_DECL_EXPORT
QFixedPoint *ritual_own_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint(
    const QFontEngine *self,
    const QFixedPoint *position) {
  return new QFixedPoint(self->QFontEngine::subPixelPositionFor(*position));
}

//  QFixed QFontEngine::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine12emSquareSizeEv(
    const QFontEngine *self) {
  return new QFixed(self->QFontEngine::emSquareSize());
}

//  void QFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE(
    const QFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngine::recalcAdvances(
      a0,
      QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE(
    const QFontEngine *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngine::doKerning(
      a0,
      QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngine::addOutlineToPath(qreal a0, qreal a1, const QGlyphLayout
//      &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngine *self,
    qreal a0,
    qreal a1,
    const QGlyphLayout *a2,
    QPainterPath *a3,
    int flags) {
  self->QFontEngine::addOutlineToPath(
      a0,
      a1,
      *a2,
      a3,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine16alphaMapForGlyphEj(
    QFontEngine *self,
    glyph_t a0) {
  return new QImage(self->QFontEngine::alphaMapForGlyph(a0));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
//      &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  return new QImage(
      self->QFontEngine::alphaMapForGlyph(
          glyph,
          *subPixelPosition));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QTransform *t) {
  return new QImage(self->QFontEngine::alphaMapForGlyph(a0, *t));
}

//  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(
      self->QFontEngine::alphaMapForGlyph(
          a0,
          *subPixelPosition,
          *t));
}

//  QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(
      self->QFontEngine::alphaRGBMapForGlyph(
          a0,
          *subPixelPosition,
          *t));
}

//  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QFontEngine *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(
      self->QFontEngine::bitmapForGlyph(
          a0,
          *subPixelPosition,
          *t,
          *color));
}

//  Glyph *QFontEngine::glyphData(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_own_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat neededFormat,
    const QTransform *t) {
  return self->QFontEngine::glyphData(
      glyph,
      *subPixelPosition,
      neededFormat,
      *t);
}

//  bool QFontEngine::hasInternalCaching() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine18hasInternalCachingEv(
    const QFontEngine *self) {
  return self->QFontEngine::hasInternalCaching();
}

//  glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t glyph, const
//      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE(
    QFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->QFontEngine::alphaMapBoundingBox(
          glyph,
          *a1,
          *matrix,
          a3));
}

//  void QFontEngine::removeGlyphFromCache(glyph_t a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontEngine20removeGlyphFromCacheEj(
    QFontEngine *self,
    glyph_t a0) {
  self->QFontEngine::removeGlyphFromCache(a0);
}

//  glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN11QFontEngine11boundingBoxERK12QGlyphLayout(
    QFontEngine *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->QFontEngine::boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const QTransform
//      &matrix)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN11QFontEngine11boundingBoxEjRK10QTransform(
    QFontEngine *self,
    glyph_t glyph,
    const QTransform *matrix) {
  return new glyph_metrics_t(self->QFontEngine::boundingBox(glyph, *matrix));
}

//  QFixed QFontEngine::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine6ascentEv(const QFontEngine *self) {
  return new QFixed(self->QFontEngine::ascent());
}

//  QFixed QFontEngine::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine7descentEv(const QFontEngine *self) {
  return new QFixed(self->QFontEngine::descent());
}

//  QFixed QFontEngine::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine7leadingEv(const QFontEngine *self) {
  return new QFixed(self->QFontEngine::leading());
}

//  QFixed QFontEngine::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine7xHeightEv(const QFontEngine *self) {
  return new QFixed(self->QFontEngine::xHeight());
}

//  QFixed QFontEngine::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine16averageCharWidthEv(
    const QFontEngine *self) {
  return new QFixed(self->QFontEngine::averageCharWidth());
}

//  QFixed QFontEngine::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine13lineThicknessEv(
    const QFontEngine *self) {
  return new QFixed(self->QFontEngine::lineThickness());
}

//  QFixed QFontEngine::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK11QFontEngine17underlinePositionEv(
    const QFontEngine *self) {
  return new QFixed(self->QFontEngine::underlinePosition());
}

//  qreal QFontEngine::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11QFontEngine14minLeftBearingEv(
    const QFontEngine *self) {
  return self->QFontEngine::minLeftBearing();
}

//  qreal QFontEngine::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11QFontEngine15minRightBearingEv(
    const QFontEngine *self) {
  return self->QFontEngine::minRightBearing();
}

//  bool QFontEngine::canRender(const QChar *str, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine9canRenderEPK5QChari(
    const QFontEngine *self,
    const QChar *str,
    int len) {
  return self->QFontEngine::canRender(str, len);
}

//  bool QFontEngine::supportsTransformation(const QTransform &transform)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine22supportsTransformationERK10QTransform(
    const QFontEngine *self,
    const QTransform *transform) {
  return self->QFontEngine::supportsTransformation(*transform);
}

//  int QFontEngine::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFontEngine10glyphCountEv(const QFontEngine *self) {
  return self->QFontEngine::glyphCount();
}

//  int QFontEngine::glyphMargin(GlyphFormat format)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE(
    QFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->QFontEngine::glyphMargin(format);
}

//  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZNK11QFontEngine13cloneWithSizeEd(
    const QFontEngine *self,
    qreal a0) {
  return self->QFontEngine::cloneWithSize(a0);
}

//  Qt::HANDLE QFontEngine::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_own_ZNK11QFontEngine6handleEv(const QFontEngine *self) {
  return self->QFontEngine::handle();
}

//  QString QFontEngine::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QFontEngine9glyphNameEj(
    const QFontEngine *self,
    glyph_t index) {
  return new QString(self->QFontEngine::glyphName(index));
}

//  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK11QFontEngine9findGlyphE13QLatin1String(
    const QFontEngine *self,
    const QLatin1String *name) {
  return self->QFontEngine::findGlyph(*name);
}

//  bool QFontEngine::hasUnreliableGlyphOutline() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv(
    const QFontEngine *self) {
  return self->QFontEngine::hasUnreliableGlyphOutline();
}

//  bool QFontEngine::expectsGammaCorrectedBlending(QFontEngine::GlyphFormat
//      format) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE(
    const QFontEngine *self,
    QFontEngine::GlyphFormat format) {
  return self->QFontEngine::expectsGammaCorrectedBlending(format);
}

//  void QFontEngine::setDefaultHintStyle(HintStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE(
    QFontEngine *self,
    QFontEngine::HintStyle a0) {
  self->QFontEngine::setDefaultHintStyle(a0);
}

//  void QFontEngine::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QFontEngine23initializeHeightMetricsEv(
    const QFontEngine *self) {
  static_cast<const OwnQFontEngine *>(self)->OwnQFontEngine::initializeHeightMetrics();
}
