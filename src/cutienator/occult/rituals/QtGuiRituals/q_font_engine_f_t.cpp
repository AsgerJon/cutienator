//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h, Qt 6.12.0, as the Qt
//  of macOS and the Qt of Windows install it. Its header needs
//  FreeType's, which these two install with Qt's, in the folder
//  'QtFreetype'.
//  FreeType's faces are passed as addresses. Not written: the 'create'
//  that takes a 'QMap', and 'traverseColr1', which takes a 'QSet' of
//  'std::pair'.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
#include <QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QFontEngineFT that Python can take functions over in. Every
//  QFontEngineFT Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef glyph_t (*CuteQFontEngineFTCall0)(const void *, uint, int *);
typedef void (*CuteQFontEngineFTCall1)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineFTCall2)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineFTCall3)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineFTCall4)(const void *, glyph_t, int *);
typedef void * (*CuteQFontEngineFTCall5)(const void *, qreal, int *);
typedef const QFixed * (*CuteQFontEngineFTCall6)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall7)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall8)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall9)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall10)(const void *, int *);
typedef qreal (*CuteQFontEngineFTCall11)(const void *, int *);
typedef qreal (*CuteQFontEngineFTCall12)(const void *, int *);
typedef qreal (*CuteQFontEngineFTCall13)(const void *, int *);
typedef const QImage * (*CuteQFontEngineFTCall14)(const void *, glyph_t, int *);
typedef bool (*CuteQFontEngineFTCall15)(const void *, const QChar *, int, int *);
typedef const QFontEngine::Properties * (*CuteQFontEngineFTCall16)(const void *, int *);
typedef void (*CuteQFontEngineFTCall17)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQFontEngineFTCall18)(const void *, int *);
typedef int (*CuteQFontEngineFTCall19)(const void *, int *);
typedef bool (*CuteQFontEngineFTCall20)(const void *, int *);
typedef bool (*CuteQFontEngineFTCall21)(const void *, int *);
typedef const QFixedPoint * (*CuteQFontEngineFTCall22)(const void *, const QFixedPoint *, int *);
typedef void (*CuteQFontEngineFTCall23)(const void *, QGlyphLayout *, int, int *);
typedef const QImage * (*CuteQFontEngineFTCall24)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineFTCall25)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineFTCall26)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineFTCall27)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineFTCall28)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQFontEngineFTCall29)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQFontEngineFTCall30)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineFTCall31)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQFontEngineFTCall32)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineFTCall33)(const void *, glyph_t, const QTransform *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall34)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall35)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall36)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineFTCall37)(const void *, int *);
typedef bool (*CuteQFontEngineFTCall38)(const void *, const QTransform *, int *);
typedef int (*CuteQFontEngineFTCall39)(const void *, int *);
typedef int (*CuteQFontEngineFTCall40)(const void *, int, int *);
typedef QString * (*CuteQFontEngineFTCall41)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQFontEngineFTCall42)(const void *, const QLatin1String *, int *);
typedef bool (*CuteQFontEngineFTCall43)(const void *, int *);
typedef bool (*CuteQFontEngineFTCall44)(const void *, int, int *);
typedef void (*CuteQFontEngineFTCall45)(const void *, int, int *);
typedef void (*CuteQFontEngineFTCall46)(const void *, int *);
class CuteQFontEngineFT : public QFontEngineFT {
public:
  using QFontEngineFT::QFontEngineFT;
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

  //  glyph_t QFontEngineFT::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontEngineFTCall0 call = reinterpret_cast<CuteQFontEngineFTCall0>(taken[0]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::glyphIndex(ucs4);
  }

  //  void QFontEngineFT::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontEngineFTCall1 call = reinterpret_cast<CuteQFontEngineFTCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineFT::recalcAdvances(a0, a1);
  }

  //  void QFontEngineFT::addOutlineToPath(qreal x, qreal y, const
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
      CuteQFontEngineFTCall2 call = reinterpret_cast<CuteQFontEngineFTCall2>(taken[2]);
      call(this, x, y, &glyphs, path, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineFT::addOutlineToPath(x, y, glyphs, path, flags);
  }

  //  glyph_metrics_t QFontEngineFT::boundingBox(const QGlyphLayout &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontEngineFTCall3 call = reinterpret_cast<CuteQFontEngineFTCall3>(taken[3]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontEngineFTCall4 call = reinterpret_cast<CuteQFontEngineFTCall4>(taken[4]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::boundingBox(glyph);
  }

  //  QFontEngine *QFontEngineFT::cloneWithSize(qreal pixelSize) const
  QFontEngine *cloneWithSize(qreal pixelSize) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontEngineFTCall5 call = reinterpret_cast<CuteQFontEngineFTCall5>(taken[5]);
      void * given = call(this, pixelSize, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngineFT::cloneWithSize(pixelSize);
  }

  //  QFixed QFontEngineFT::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontEngineFTCall6 call = reinterpret_cast<CuteQFontEngineFTCall6>(taken[6]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::emSquareSize();
  }

  //  QFixed QFontEngine::ascent() const
  QFixed ascent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontEngineFTCall7 call = reinterpret_cast<CuteQFontEngineFTCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::ascent();
  }

  //  QFixed QFontEngineFT::capHeight() const
  QFixed capHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontEngineFTCall8 call = reinterpret_cast<CuteQFontEngineFTCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::capHeight();
  }

  //  QFixed QFontEngine::descent() const
  QFixed descent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontEngineFTCall9 call = reinterpret_cast<CuteQFontEngineFTCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::descent();
  }

  //  QFixed QFontEngine::leading() const
  QFixed leading() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontEngineFTCall10 call = reinterpret_cast<CuteQFontEngineFTCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::leading();
  }

  //  qreal QFontEngineFT::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontEngineFTCall11 call = reinterpret_cast<CuteQFontEngineFTCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::maxCharWidth();
  }

  //  qreal QFontEngine::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontEngineFTCall12 call = reinterpret_cast<CuteQFontEngineFTCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minLeftBearing();
  }

  //  qreal QFontEngine::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontEngineFTCall13 call = reinterpret_cast<CuteQFontEngineFTCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::minRightBearing();
  }

  //  QImage QFontEngineFT::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontEngineFTCall14 call = reinterpret_cast<CuteQFontEngineFTCall14>(taken[14]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::alphaMapForGlyph(a0);
  }

  //  bool QFontEngine::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontEngineFTCall15 call = reinterpret_cast<CuteQFontEngineFTCall15>(taken[15]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QFontEngine::canRender(string, len);
  }

  //  Properties QFontEngineFT::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontEngineFTCall16 call = reinterpret_cast<CuteQFontEngineFTCall16>(taken[16]);
      const QFontEngine::Properties * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::properties();
  }

  //  void QFontEngineFT::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
  //      glyph_metrics_t *metrics)
  void getUnscaledGlyph(
      glyph_t glyph,
      QPainterPath *path,
      glyph_metrics_t *metrics) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontEngineFTCall17 call = reinterpret_cast<CuteQFontEngineFTCall17>(taken[17]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngineFT::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngineFT::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontEngineFTCall18 call = reinterpret_cast<CuteQFontEngineFTCall18>(taken[18]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::faceId();
  }

  //  int QFontEngineFT::synthesized() const
  int synthesized() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontEngineFTCall19 call = reinterpret_cast<CuteQFontEngineFTCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::synthesized();
  }

  //  bool QFontEngineFT::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontEngineFTCall20 call = reinterpret_cast<CuteQFontEngineFTCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngineFT::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontEngineFTCall21 call = reinterpret_cast<CuteQFontEngineFTCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontEngineFTCall22 call = reinterpret_cast<CuteQFontEngineFTCall22>(taken[22]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  void QFontEngineFT::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontEngineFTCall23 call = reinterpret_cast<CuteQFontEngineFTCall23>(taken[23]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineFT::doKerning(a0, a1);
  }

  //  QImage QFontEngineFT::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontEngineFTCall24 call = reinterpret_cast<CuteQFontEngineFTCall24>(taken[24]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontEngineFTCall25 call = reinterpret_cast<CuteQFontEngineFTCall25>(taken[25]);
      const QImage * given = call(this, a0, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, t);
  }

  //  QImage QFontEngineFT::alphaMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontEngineFTCall26 call = reinterpret_cast<CuteQFontEngineFTCall26>(taken[26]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::alphaMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngineFT::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaRGBMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontEngineFTCall27 call = reinterpret_cast<CuteQFontEngineFTCall27>(taken[27]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngineFT::bitmapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t, const QColor &color)
  QImage bitmapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t,
      const QColor &color) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontEngineFTCall28 call = reinterpret_cast<CuteQFontEngineFTCall28>(taken[28]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &color, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::bitmapForGlyph(a0, subPixelPosition, t, color);
  }

  //  Glyph *QFontEngineFT::glyphData(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
  QFontEngine::Glyph *glyphData(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition,
      QFontEngine::GlyphFormat neededFormat,
      const QTransform &t) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontEngineFTCall29 call = reinterpret_cast<CuteQFontEngineFTCall29>(taken[29]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngineFT::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngineFT::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontEngineFTCall30 call = reinterpret_cast<CuteQFontEngineFTCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::hasInternalCaching();
  }

  //  glyph_metrics_t QFontEngineFT::alphaMapBoundingBox(glyph_t glyph, const
  //      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
  glyph_metrics_t alphaMapBoundingBox(
      glyph_t glyph,
      const QFixedPoint &a1,
      const QTransform &matrix,
      QFontEngine::GlyphFormat a3) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFontEngineFTCall31 call = reinterpret_cast<CuteQFontEngineFTCall31>(taken[31]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngineFT::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontEngineFTCall32 call = reinterpret_cast<CuteQFontEngineFTCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontEngineFT::removeGlyphFromCache(a0);
  }

  //  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph, const
  //      QTransform &matrix)
  glyph_metrics_t boundingBox(
      glyph_t glyph,
      const QTransform &matrix) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontEngineFTCall33 call = reinterpret_cast<CuteQFontEngineFTCall33>(taken[33]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::boundingBox(glyph, matrix);
  }

  //  QFixed QFontEngineFT::xHeight() const
  QFixed xHeight() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontEngineFTCall34 call = reinterpret_cast<CuteQFontEngineFTCall34>(taken[34]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::xHeight();
  }

  //  QFixed QFontEngineFT::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontEngineFTCall35 call = reinterpret_cast<CuteQFontEngineFTCall35>(taken[35]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::averageCharWidth();
  }

  //  QFixed QFontEngineFT::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontEngineFTCall36 call = reinterpret_cast<CuteQFontEngineFTCall36>(taken[36]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::lineThickness();
  }

  //  QFixed QFontEngineFT::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontEngineFTCall37 call = reinterpret_cast<CuteQFontEngineFTCall37>(taken[37]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineFT::underlinePosition();
  }

  //  bool QFontEngineFT::supportsTransformation(const QTransform &transform)
  //      const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQFontEngineFTCall38 call = reinterpret_cast<CuteQFontEngineFTCall38>(taken[38]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::supportsTransformation(transform);
  }

  //  int QFontEngineFT::glyphCount() const
  int glyphCount() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontEngineFTCall39 call = reinterpret_cast<CuteQFontEngineFTCall39>(taken[39]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineFT::glyphCount();
  }

  //  int QFontEngineFT::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[40]) {
      int handled = 0;
      CuteQFontEngineFTCall40 call = reinterpret_cast<CuteQFontEngineFTCall40>(taken[40]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngineFT::glyphMargin(format);
  }

  //  QString QFontEngineFT::glyphName(glyph_t index) const
  QString glyphName(glyph_t index) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontEngineFTCall41 call = reinterpret_cast<CuteQFontEngineFTCall41>(taken[41]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontEngineFT::glyphName(index);
  }

  //  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
  glyph_t findGlyph(QLatin1StringView name) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFontEngineFTCall42 call = reinterpret_cast<CuteQFontEngineFTCall42>(taken[42]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngine::findGlyph(name);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQFontEngineFTCall43 call = reinterpret_cast<CuteQFontEngineFTCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasUnreliableGlyphOutline();
  }

  //  bool
  //      QFontEngineFT::expectsGammaCorrectedBlending(QFontEngine::GlyphForm
  //      at format) const
  bool expectsGammaCorrectedBlending(
      QFontEngine::GlyphFormat format) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontEngineFTCall44 call = reinterpret_cast<CuteQFontEngineFTCall44>(taken[44]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngineFT::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngineFT::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontEngineFTCall45 call = reinterpret_cast<CuteQFontEngineFTCall45>(taken[45]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngineFT::setDefaultHintStyle(a0);
  }

  //  void QFontEngineFT::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontEngineFTCall46 call = reinterpret_cast<CuteQFontEngineFTCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngineFT::initializeHeightMetrics();
  }
};

//  QFontEngineFT::QFontEngineFT(const QFontDef &fd)
extern "C" Q_DECL_EXPORT
QFontEngineFT *ritual_ZN13QFontEngineFTC1ERK8QFontDef(const QFontDef *fd) {
  return new CuteQFontEngineFT(*fd);
}

//  QFontEngineFT::~QFontEngineFT()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFTD1Ev(QFontEngineFT *self) {
  delete self;
}

//  QFontEngine::FaceId QFontEngineFT::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_ZNK13QFontEngineFT6faceIdEv(
    const QFontEngineFT *self) {
  return new QFontEngine::FaceId(self->faceId());
}

//  QFontEngine::Properties QFontEngineFT::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK13QFontEngineFT10propertiesEv(
    const QFontEngineFT *self) {
  return new QFontEngine::Properties(self->properties());
}

//  QFixed QFontEngineFT::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT12emSquareSizeEv(
    const QFontEngineFT *self) {
  return new QFixed(self->emSquareSize());
}

//  bool QFontEngineFT::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT35supportsHorizontalSubPixelPositionsEv(
    const QFontEngineFT *self) {
  return self->supportsHorizontalSubPixelPositions();
}

//  bool QFontEngineFT::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT33supportsVerticalSubPixelPositionsEv(
    const QFontEngineFT *self) {
  return self->supportsVerticalSubPixelPositions();
}

//  bool QFontEngineFT::getSfntTableData(uint tag, uchar *buffer, uint
//      *length) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT16getSfntTableDataEjPhPj(
    const QFontEngineFT *self,
    uint tag,
    uchar *buffer,
    uint *length) {
  return self->getSfntTableData(tag, buffer, length);
}

//  int QFontEngineFT::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontEngineFT11synthesizedEv(const QFontEngineFT *self) {
  return self->synthesized();
}

//  void QFontEngineFT::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QFontEngineFT23initializeHeightMetricsEv(
    const QFontEngineFT *self) {
  self->initializeHeightMetrics();
}

//  QFixed QFontEngineFT::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT9capHeightEv(const QFontEngineFT *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QFontEngineFT::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT7xHeightEv(const QFontEngineFT *self) {
  return new QFixed(self->xHeight());
}

//  QFixed QFontEngineFT::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT16averageCharWidthEv(
    const QFontEngineFT *self) {
  return new QFixed(self->averageCharWidth());
}

//  qreal QFontEngineFT::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontEngineFT12maxCharWidthEv(const QFontEngineFT *self) {
  return self->maxCharWidth();
}

//  QFixed QFontEngineFT::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT13lineThicknessEv(
    const QFontEngineFT *self) {
  return new QFixed(self->lineThickness());
}

//  QFixed QFontEngineFT::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT17underlinePositionEv(
    const QFontEngineFT *self) {
  return new QFixed(self->underlinePosition());
}

//  glyph_t QFontEngineFT::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK13QFontEngineFT10glyphIndexEj(
    const QFontEngineFT *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  QString QFontEngineFT::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontEngineFT9glyphNameEj(
    const QFontEngineFT *self,
    glyph_t index) {
  return new QString(self->glyphName(index));
}

//  void QFontEngineFT::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QFontEngineFT9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    QGlyphLayout *a0,
    int a1) {
  self->doKerning(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineFT::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
//      glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QFontEngineFT *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->getUnscaledGlyph(glyph, path, metrics);
}

//  bool QFontEngineFT::supportsTransformation(const QTransform &transform)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT22supportsTransformationERK10QTransform(
    const QFontEngineFT *self,
    const QTransform *transform) {
  return self->supportsTransformation(*transform);
}

//  void QFontEngineFT::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
//      *positions, int nglyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT15addGlyphsToPathEPjP11QFixedPointiP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineFT *self,
    glyph_t *glyphs,
    QFixedPoint *positions,
    int nglyphs,
    QPainterPath *path,
    int flags) {
  self->addGlyphsToPath(
      glyphs, positions, nglyphs, path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  void QFontEngineFT::addOutlineToPath(qreal x, qreal y, const QGlyphLayout
//      &glyphs, QPainterPath *path, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineFT *self,
    qreal x,
    qreal y,
    const QGlyphLayout *glyphs,
    QPainterPath *path,
    int flags) {
  self->addOutlineToPath(
      x, y, *glyphs, path, QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  int QFontEngineFT::stringToCMap(const QChar *str, int len, QGlyphLayout
//      *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontEngineFT12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str, len, glyphs, nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN13QFontEngineFT11boundingBoxERK12QGlyphLayout(
    QFontEngineFT *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN13QFontEngineFT11boundingBoxEj(
    QFontEngineFT *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->boundingBox(glyph));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph, const
//      QTransform &matrix)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN13QFontEngineFT11boundingBoxEjRK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QTransform *matrix) {
  return new glyph_metrics_t(self->boundingBox(glyph, *matrix));
}

//  void QFontEngineFT::recalcAdvances(QGlyphLayout *glyphs, ShaperFlags
//      flags) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QFontEngineFT14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    QGlyphLayout *glyphs,
    int flags) {
  self->recalcAdvances(glyphs, QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t g)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QFontEngineFT16alphaMapForGlyphEj(
    QFontEngineFT *self,
    glyph_t g) {
  return new QImage(self->alphaMapForGlyph(g));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t a0, const QFixedPoint &a1)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QFontEngineFT16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *a1) {
  return new QImage(self->alphaMapForGlyph(a0, *a1));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QFontEngineFT16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition, *t));
}

//  QImage QFontEngineFT::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QFontEngineFT19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  QImage QFontEngineFT::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QFontEngineFT14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  glyph_metrics_t QFontEngineFT::alphaMapBoundingBox(glyph_t glyph, const
//      QFixedPoint &subPixelPosition, const QTransform &matrix,
//      QFontEngine::GlyphFormat format)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN13QFontEngineFT19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *matrix,
    QFontEngine::GlyphFormat format) {
  return new glyph_metrics_t(
      self->alphaMapBoundingBox(glyph, *subPixelPosition, *matrix, format));
}

//  Glyph *QFontEngineFT::glyphData(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZN13QFontEngineFT9glyphDataEjRK11QFixedPointN11QFontEngine11GlyphFormatERK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat neededFormat,
    const QTransform *t) {
  return self->glyphData(glyph, *subPixelPosition, neededFormat, *t);
}

//  bool QFontEngineFT::hasInternalCaching() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT18hasInternalCachingEv(
    const QFontEngineFT *self) {
  return self->hasInternalCaching();
}

//  bool
//      QFontEngineFT::expectsGammaCorrectedBlending(QFontEngine::GlyphFormat
//      format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT29expectsGammaCorrectedBlendingEN11QFontEngine11GlyphFormatE(
    const QFontEngineFT *self,
    QFontEngine::GlyphFormat format) {
  return self->expectsGammaCorrectedBlending(format);
}

//  void QFontEngineFT::removeGlyphFromCache(glyph_t glyph)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT20removeGlyphFromCacheEj(
    QFontEngineFT *self,
    glyph_t glyph) {
  self->removeGlyphFromCache(glyph);
}

//  int QFontEngineFT::glyphMargin(QFontEngine::GlyphFormat a0)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFontEngineFT11glyphMarginEN11QFontEngine11GlyphFormatE(
    QFontEngineFT *self,
    QFontEngine::GlyphFormat a0) {
  return self->glyphMargin(a0);
}

//  int QFontEngineFT::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontEngineFT10glyphCountEv(const QFontEngineFT *self) {
  return self->glyphCount();
}

//  QList<QFontVariableAxis> QFontEngineFT::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK13QFontEngineFT12variableAxesEv(
    const QFontEngineFT *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  FT_Face QFontEngineFT::lockFace(Scaling scale) const
extern "C" Q_DECL_EXPORT
FT_Face ritual_ZNK13QFontEngineFT8lockFaceENS_7ScalingE(
    const QFontEngineFT *self,
    QFontEngineFT::Scaling scale) {
  return self->lockFace(scale);
}

//  void QFontEngineFT::unlockFace() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QFontEngineFT10unlockFaceEv(const QFontEngineFT *self) {
  self->unlockFace();
}

//  FT_Face QFontEngineFT::non_locked_face() const
extern "C" Q_DECL_EXPORT
FT_Face ritual_ZNK13QFontEngineFT15non_locked_faceEv(
    const QFontEngineFT *self) {
  return self->non_locked_face();
}

//  bool QFontEngineFT::drawAntialiased() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT15drawAntialiasedEv(
    const QFontEngineFT *self) {
  return self->drawAntialiased();
}

//  bool QFontEngineFT::invalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT7invalidEv(const QFontEngineFT *self) {
  return self->invalid();
}

//  bool QFontEngineFT::isBitmapFont() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT12isBitmapFontEv(const QFontEngineFT *self) {
  return self->isBitmapFont();
}

//  bool QFontEngineFT::isScalableBitmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT16isScalableBitmapEv(
    const QFontEngineFT *self) {
  return self->isScalableBitmap();
}

//  Glyph *QFontEngineFT::loadGlyph(uint glyph, const QFixedPoint
//      &subPixelPosition, GlyphFormat format, bool fetchMetricsOnly, bool
//      disableOutlineDrawing) const
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZNK13QFontEngineFT9loadGlyphEjRK11QFixedPointN11QFontEngine11GlyphFormatEbb(
    const QFontEngineFT *self,
    uint glyph,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat format,
    bool fetchMetricsOnly,
    bool disableOutlineDrawing) {
  return self->loadGlyph(
      glyph, *subPixelPosition, format, fetchMetricsOnly,
      disableOutlineDrawing);
}

//  Glyph *QFontEngineFT::loadGlyph(QGlyphSet *set, uint glyph, const
//      QFixedPoint &subPixelPosition, QColor color, GlyphFormat a4, bool
//      fetchMetricsOnly, bool disableOutlineDrawing) const
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZNK13QFontEngineFT9loadGlyphEPNS_9QGlyphSetEjRK11QFixedPoint6QColorN11QFontEngine11GlyphFormatEbb(
    const QFontEngineFT *self,
    QFontEngineFT::QGlyphSet *set,
    uint glyph,
    const QFixedPoint *subPixelPosition,
    const QColor *color,
    QFontEngine::GlyphFormat a4,
    bool fetchMetricsOnly,
    bool disableOutlineDrawing) {
  return self->loadGlyph(
      set, glyph, *subPixelPosition, *color, a4, fetchMetricsOnly,
      disableOutlineDrawing);
}

//  Glyph *QFontEngineFT::loadGlyphFor(glyph_t g, const QFixedPoint
//      &subPixelPosition, GlyphFormat format, const QTransform &t, QColor
//      color, bool fetchBoundingBox, bool disableOutlineDrawing)
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZN13QFontEngineFT12loadGlyphForEjRK11QFixedPointN11QFontEngine11GlyphFormatERK10QTransform6QColorbb(
    QFontEngineFT *self,
    glyph_t g,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat format,
    const QTransform *t,
    const QColor *color,
    bool fetchBoundingBox,
    bool disableOutlineDrawing) {
  return self->loadGlyphFor(
      g, *subPixelPosition, format, *t, *color, fetchBoundingBox,
      disableOutlineDrawing);
}

//  QGlyphSet *QFontEngineFT::loadGlyphSet(const QTransform &matrix)
extern "C" Q_DECL_EXPORT
QFontEngineFT::QGlyphSet *ritual_ZN13QFontEngineFT12loadGlyphSetERK10QTransform(
    QFontEngineFT *self,
    const QTransform *matrix) {
  return self->loadGlyphSet(*matrix);
}

//  bool QFontEngineFT::init(FaceId faceId, bool antiaalias, GlyphFormat
//      defaultFormat, const QByteArray &fontData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontEngineFT4initEN11QFontEngine6FaceIdEbNS0_11GlyphFormatERK10QByteArray(
    QFontEngineFT *self,
    const QFontEngine::FaceId *faceId,
    bool antiaalias,
    QFontEngine::GlyphFormat defaultFormat,
    const QByteArray *fontData) {
  return self->init(*faceId, antiaalias, defaultFormat, *fontData);
}

//  bool QFontEngineFT::init(FaceId faceId, bool antialias, GlyphFormat
//      format, QFreetypeFace *freetypeFace)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontEngineFT4initEN11QFontEngine6FaceIdEbNS0_11GlyphFormatEP13QFreetypeFace(
    QFontEngineFT *self,
    const QFontEngine::FaceId *faceId,
    bool antialias,
    QFontEngine::GlyphFormat format,
    QFreetypeFace *freetypeFace) {
  return self->init(*faceId, antialias, format, freetypeFace);
}

//  int QFontEngineFT::getPointInOutline(glyph_t glyph, int flags, quint32
//      point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFontEngineFT17getPointInOutlineEjijP6QFixedS1_Pj(
    QFontEngineFT *self,
    glyph_t glyph,
    int flags,
    quint32 point,
    QFixed *xpos,
    QFixed *ypos,
    quint32 *nPoints) {
  return self->getPointInOutline(glyph, flags, point, xpos, ypos, nPoints);
}

//  void QFontEngineFT::setQtDefaultHintStyle(QFont::HintingPreference
//      hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT21setQtDefaultHintStyleEN5QFont17HintingPreferenceE(
    QFontEngineFT *self,
    QFont::HintingPreference hintingPreference) {
  self->setQtDefaultHintStyle(hintingPreference);
}

//  void QFontEngineFT::setDefaultHintStyle(HintStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT19setDefaultHintStyleEN11QFontEngine9HintStyleE(
    QFontEngineFT *self,
    QFontEngine::HintStyle style) {
  self->setDefaultHintStyle(style);
}

//  QFontEngine *QFontEngineFT::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK13QFontEngineFT13cloneWithSizeEd(
    const QFontEngineFT *self,
    qreal pixelSize) {
  return self->cloneWithSize(pixelSize);
}

//  Qt::HANDLE QFontEngineFT::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK13QFontEngineFT6handleEv(const QFontEngineFT *self) {
  return self->handle();
}

//  bool QFontEngineFT::initFromFontEngine(const QFontEngineFT *fontEngine)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontEngineFT18initFromFontEngineEPKS_(
    QFontEngineFT *self,
    const QFontEngineFT *fontEngine) {
  return self->initFromFontEngine(fontEngine);
}

//  HintStyle QFontEngineFT::defaultHintStyle() const
extern "C" Q_DECL_EXPORT
QFontEngine::HintStyle ritual_ZNK13QFontEngineFT16defaultHintStyleEv(
    const QFontEngineFT *self) {
  return self->defaultHintStyle();
}

//  QFontEngineFT *QFontEngineFT::create(const QFontDef &fontDef, FaceId
//      faceId, const QByteArray &fontData)
extern "C" Q_DECL_EXPORT
QFontEngineFT *ritual_ZN13QFontEngineFT6createERK8QFontDefN11QFontEngine6FaceIdERK10QByteArray(
    const QFontDef *fontDef,
    const QFontEngine::FaceId *faceId,
    const QByteArray *fontData) {
  return QFontEngineFT::create(*fontDef, *faceId, *fontData);
}

//  int QFontEngineFT::loadFlags(QGlyphSet *set, GlyphFormat format, int
//      flags, bool &hsubpixel, int &vfactor) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontEngineFT9loadFlagsEPNS_9QGlyphSetEN11QFontEngine11GlyphFormatEiRbRi(
    const QFontEngineFT *self,
    QFontEngineFT::QGlyphSet *set,
    QFontEngine::GlyphFormat format,
    int flags,
    bool *hsubpixel,
    int *vfactor) {
  return self->loadFlags(set, format, flags, *hsubpixel, *vfactor);
}

//  bool QFontEngineFT::shouldUseDesignMetrics(ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT22shouldUseDesignMetricsE6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    int flags) {
  return self->shouldUseDesignMetrics(QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  QFixed QFontEngineFT::scaledBitmapMetrics(QFixed m) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK13QFontEngineFT19scaledBitmapMetricsE6QFixed(
    const QFontEngineFT *self,
    const QFixed *m) {
  return new QFixed(self->scaledBitmapMetrics(*m));
}

//  glyph_metrics_t QFontEngineFT::scaledBitmapMetrics(const glyph_metrics_t
//      &m, const QTransform &matrix) const
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZNK13QFontEngineFT19scaledBitmapMetricsERK15glyph_metrics_tRK10QTransform(
    const QFontEngineFT *self,
    const glyph_metrics_t *m,
    const QTransform *matrix) {
  return new glyph_metrics_t(self->scaledBitmapMetrics(*m, *matrix));
}

#if defined(QFONTENGINE_FT_SUPPORT_COLRV1)
//  Glyph *QFontEngineFT::loadColrv1Glyph(QGlyphSet *set, Glyph *g, uint
//      glyph, const QColor &color, bool fetchMetricsOnly) const
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZNK13QFontEngineFT15loadColrv1GlyphEPNS_9QGlyphSetEPN11QFontEngine5GlyphEjRK6QColorb(
    const QFontEngineFT *self,
    QFontEngineFT::QGlyphSet *set,
    QFontEngine::Glyph *g,
    uint glyph,
    const QColor *color,
    bool fetchMetricsOnly) {
  return self->loadColrv1Glyph(set, g, glyph, *color, fetchMetricsOnly);
}
#endif  // defined(QFONTENGINE_FT_SUPPORT_COLRV1)

//  a Python function taken by a CuteQFontEngineFT, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontEngineFT(
    QFontEngineFT *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontEngineFT *>(self)->take(key, call);
}

//  QFontEngine::FaceId QFontEngineFT::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_own_ZNK13QFontEngineFT6faceIdEv(
    const QFontEngineFT *self) {
  return new QFontEngine::FaceId(self->QFontEngineFT::faceId());
}

//  QFontEngine::Properties QFontEngineFT::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_own_ZNK13QFontEngineFT10propertiesEv(
    const QFontEngineFT *self) {
  return new QFontEngine::Properties(self->QFontEngineFT::properties());
}

//  QFixed QFontEngineFT::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT12emSquareSizeEv(
    const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::emSquareSize());
}

//  bool QFontEngineFT::supportsHorizontalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFontEngineFT35supportsHorizontalSubPixelPositionsEv(
    const QFontEngineFT *self) {
  return self->QFontEngineFT::supportsHorizontalSubPixelPositions();
}

//  bool QFontEngineFT::supportsVerticalSubPixelPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFontEngineFT33supportsVerticalSubPixelPositionsEv(
    const QFontEngineFT *self) {
  return self->QFontEngineFT::supportsVerticalSubPixelPositions();
}

//  int QFontEngineFT::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QFontEngineFT11synthesizedEv(const QFontEngineFT *self) {
  return self->QFontEngineFT::synthesized();
}

//  void QFontEngineFT::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QFontEngineFT23initializeHeightMetricsEv(
    const QFontEngineFT *self) {
  self->QFontEngineFT::initializeHeightMetrics();
}

//  QFixed QFontEngineFT::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT9capHeightEv(
    const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::capHeight());
}

//  QFixed QFontEngineFT::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT7xHeightEv(const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::xHeight());
}

//  QFixed QFontEngineFT::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT16averageCharWidthEv(
    const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::averageCharWidth());
}

//  qreal QFontEngineFT::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK13QFontEngineFT12maxCharWidthEv(
    const QFontEngineFT *self) {
  return self->QFontEngineFT::maxCharWidth();
}

//  QFixed QFontEngineFT::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT13lineThicknessEv(
    const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::lineThickness());
}

//  QFixed QFontEngineFT::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK13QFontEngineFT17underlinePositionEv(
    const QFontEngineFT *self) {
  return new QFixed(self->QFontEngineFT::underlinePosition());
}

//  glyph_t QFontEngineFT::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK13QFontEngineFT10glyphIndexEj(
    const QFontEngineFT *self,
    uint ucs4) {
  return self->QFontEngineFT::glyphIndex(ucs4);
}

//  QString QFontEngineFT::glyphName(glyph_t index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK13QFontEngineFT9glyphNameEj(
    const QFontEngineFT *self,
    glyph_t index) {
  return new QString(self->QFontEngineFT::glyphName(index));
}

//  void QFontEngineFT::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QFontEngineFT9doKerningEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngineFT::doKerning(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineFT::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
//      glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QFontEngineFT16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QFontEngineFT *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->QFontEngineFT::getUnscaledGlyph(glyph, path, metrics);
}

//  bool QFontEngineFT::supportsTransformation(const QTransform &transform)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFontEngineFT22supportsTransformationERK10QTransform(
    const QFontEngineFT *self,
    const QTransform *transform) {
  return self->QFontEngineFT::supportsTransformation(*transform);
}

//  void QFontEngineFT::addOutlineToPath(qreal x, qreal y, const QGlyphLayout
//      &glyphs, QPainterPath *path, QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QFontEngineFT16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineFT *self,
    qreal x,
    qreal y,
    const QGlyphLayout *glyphs,
    QPainterPath *path,
    int flags) {
  self->QFontEngineFT::addOutlineToPath(
      x, y, *glyphs, path, QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN13QFontEngineFT11boundingBoxERK12QGlyphLayout(
    QFontEngineFT *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->QFontEngineFT::boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN13QFontEngineFT11boundingBoxEj(
    QFontEngineFT *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->QFontEngineFT::boundingBox(glyph));
}

//  glyph_metrics_t QFontEngineFT::boundingBox(glyph_t glyph, const
//      QTransform &matrix)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN13QFontEngineFT11boundingBoxEjRK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QTransform *matrix) {
  return new glyph_metrics_t(self->QFontEngineFT::boundingBox(glyph, *matrix));
}

//  void QFontEngineFT::recalcAdvances(QGlyphLayout *glyphs, ShaperFlags
//      flags) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QFontEngineFT14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineFT *self,
    QGlyphLayout *glyphs,
    int flags) {
  self->QFontEngineFT::recalcAdvances(glyphs, QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t g)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN13QFontEngineFT16alphaMapForGlyphEj(
    QFontEngineFT *self,
    glyph_t g) {
  return new QImage(self->QFontEngineFT::alphaMapForGlyph(g));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t a0, const QFixedPoint &a1)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN13QFontEngineFT16alphaMapForGlyphEjRK11QFixedPoint(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *a1) {
  return new QImage(self->QFontEngineFT::alphaMapForGlyph(a0, *a1));
}

//  QImage QFontEngineFT::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN13QFontEngineFT16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->QFontEngineFT::alphaMapForGlyph(glyph, *subPixelPosition, *t));
}

//  QImage QFontEngineFT::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN13QFontEngineFT19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->QFontEngineFT::alphaRGBMapForGlyph(a0, *subPixelPosition, *t));
}

//  QImage QFontEngineFT::bitmapForGlyph(glyph_t a0, const QFixedPoint
//      &subPixelPosition, const QTransform &t, const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN13QFontEngineFT14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QFontEngineFT *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->QFontEngineFT::bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  glyph_metrics_t QFontEngineFT::alphaMapBoundingBox(glyph_t glyph, const
//      QFixedPoint &subPixelPosition, const QTransform &matrix,
//      QFontEngine::GlyphFormat format)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_own_ZN13QFontEngineFT19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *matrix,
    QFontEngine::GlyphFormat format) {
  return new glyph_metrics_t(
      self->QFontEngineFT::alphaMapBoundingBox(glyph, *subPixelPosition, *matrix, format));
}

//  Glyph *QFontEngineFT::glyphData(glyph_t glyph, const QFixedPoint
//      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_own_ZN13QFontEngineFT9glyphDataEjRK11QFixedPointN11QFontEngine11GlyphFormatERK10QTransform(
    QFontEngineFT *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    QFontEngine::GlyphFormat neededFormat,
    const QTransform *t) {
  return self->QFontEngineFT::glyphData(glyph, *subPixelPosition, neededFormat, *t);
}

//  bool QFontEngineFT::hasInternalCaching() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFontEngineFT18hasInternalCachingEv(
    const QFontEngineFT *self) {
  return self->QFontEngineFT::hasInternalCaching();
}

//  bool
//      QFontEngineFT::expectsGammaCorrectedBlending(QFontEngine::GlyphFormat
//      format) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFontEngineFT29expectsGammaCorrectedBlendingEN11QFontEngine11GlyphFormatE(
    const QFontEngineFT *self,
    QFontEngine::GlyphFormat format) {
  return self->QFontEngineFT::expectsGammaCorrectedBlending(format);
}

//  void QFontEngineFT::removeGlyphFromCache(glyph_t glyph)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QFontEngineFT20removeGlyphFromCacheEj(
    QFontEngineFT *self,
    glyph_t glyph) {
  self->QFontEngineFT::removeGlyphFromCache(glyph);
}

//  int QFontEngineFT::glyphMargin(QFontEngine::GlyphFormat a0)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN13QFontEngineFT11glyphMarginEN11QFontEngine11GlyphFormatE(
    QFontEngineFT *self,
    QFontEngine::GlyphFormat a0) {
  return self->QFontEngineFT::glyphMargin(a0);
}

//  int QFontEngineFT::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QFontEngineFT10glyphCountEv(const QFontEngineFT *self) {
  return self->QFontEngineFT::glyphCount();
}

//  void QFontEngineFT::setDefaultHintStyle(HintStyle style)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QFontEngineFT19setDefaultHintStyleEN11QFontEngine9HintStyleE(
    QFontEngineFT *self,
    QFontEngine::HintStyle style) {
  self->QFontEngineFT::setDefaultHintStyle(style);
}

//  QFontEngine *QFontEngineFT::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_own_ZNK13QFontEngineFT13cloneWithSizeEd(
    const QFontEngineFT *self,
    qreal pixelSize) {
  return self->QFontEngineFT::cloneWithSize(pixelSize);
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
