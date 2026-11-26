//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>

//  A QTextureGlyphCache that Python can take functions over in. Every QTextureGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextureGlyphCacheCall0)(const void *, int, int, int *);
typedef void (*CuteQTextureGlyphCacheCall1)(const void *, int, int, int *);
typedef int (*CuteQTextureGlyphCacheCall2)(const void *, int *);
typedef void (*CuteQTextureGlyphCacheCall3)(const void *, int *);
typedef void (*CuteQTextureGlyphCacheCall4)(const void *, const QTextureGlyphCache::Coord *, glyph_t, const QFixedPoint *, int *);
typedef void (*CuteQTextureGlyphCacheCall5)(const void *, int *);
typedef int (*CuteQTextureGlyphCacheCall6)(const void *, int *);
typedef int (*CuteQTextureGlyphCacheCall7)(const void *, int *);
class CuteQTextureGlyphCache : public QTextureGlyphCache {
public:
  using QTextureGlyphCache::QTextureGlyphCache;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache17createTextureDataEii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache17resizeTextureDataEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache12glyphPaddingEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache16beginFillTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixedPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache14endFillTextureEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache15maxTextureWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache16maxTextureHeightEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QTextureGlyphCache::createTextureData(int width, int height)
  void createTextureData(int width, int height) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall0 call = reinterpret_cast<CuteQTextureGlyphCacheCall0>(taken[0]);
      call(this, width, height, &handled);
      if (handled) return;
    }
  }

  //  void QTextureGlyphCache::resizeTextureData(int width, int height)
  void resizeTextureData(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall1 call = reinterpret_cast<CuteQTextureGlyphCacheCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
  }

  //  int QTextureGlyphCache::glyphPadding() const
  int glyphPadding() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall2 call = reinterpret_cast<CuteQTextureGlyphCacheCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::glyphPadding();
  }

  //  void QTextureGlyphCache::beginFillTexture()
  void beginFillTexture() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall3 call = reinterpret_cast<CuteQTextureGlyphCacheCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::beginFillTexture();
  }

  //  void QTextureGlyphCache::fillTexture(const Coord &coord, glyph_t
  //      glyph, const QFixedPoint &subPixelPosition)
  void fillTexture(
      const QTextureGlyphCache::Coord &coord,
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall4 call = reinterpret_cast<CuteQTextureGlyphCacheCall4>(taken[4]);
      call(this, &coord, glyph, &subPixelPosition, &handled);
      if (handled) return;
    }
  }

  //  void QTextureGlyphCache::endFillTexture()
  void endFillTexture() override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall5 call = reinterpret_cast<CuteQTextureGlyphCacheCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::endFillTexture();
  }

  //  int QTextureGlyphCache::maxTextureWidth() const
  int maxTextureWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall6 call = reinterpret_cast<CuteQTextureGlyphCacheCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::maxTextureWidth();
  }

  //  int QTextureGlyphCache::maxTextureHeight() const
  int maxTextureHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextureGlyphCacheCall7 call = reinterpret_cast<CuteQTextureGlyphCacheCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::maxTextureHeight();
  }
};

//  QTextureGlyphCache::QTextureGlyphCache(QFontEngine::GlyphFormat format,
//      const QTransform &matrix, const QColor &color)
extern "C" Q_DECL_EXPORT
QTextureGlyphCache *ritual_ZN18QTextureGlyphCacheC1EN11QFontEngine11GlyphFormatERK10QTransformRK6QColor(
    QFontEngine::GlyphFormat format,
    const QTransform *matrix,
    const QColor *color) {
  return new CuteQTextureGlyphCache(format, *matrix, *color);
}

//  QTextureGlyphCache::~QTextureGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCacheD1Ev(QTextureGlyphCache *self) {
  delete self;
}

//  bool QTextureGlyphCache::populate(QFontEngine *fontEngine, qsizetype
//      numGlyphs, const glyph_t *glyphs, const QFixedPoint *positions,
//      QPainter::RenderHints renderHints, bool includeGlyphCacheScale)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextureGlyphCache8populateEP11QFontEnginexPKjPK11QFixedPoint6QFlagsIN8QPainter10RenderHintEEb(
    QTextureGlyphCache *self,
    QFontEngine *fontEngine,
    qsizetype numGlyphs,
    const glyph_t *glyphs,
    const QFixedPoint *positions,
    int renderHints,
    bool includeGlyphCacheScale) {
  return self->populate(
      fontEngine,
      numGlyphs,
      glyphs,
      positions,
      QFlags<QPainter::RenderHint>::fromInt(renderHints),
      includeGlyphCacheScale);
}

//  bool QTextureGlyphCache::hasPendingGlyphs() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTextureGlyphCache16hasPendingGlyphsEv(
    const QTextureGlyphCache *self) {
  return self->hasPendingGlyphs();
}

//  void QTextureGlyphCache::fillInPendingGlyphs()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache19fillInPendingGlyphsEv(
    QTextureGlyphCache *self) {
  self->fillInPendingGlyphs();
}

//  void QTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache17createTextureDataEii(
    QTextureGlyphCache *self,
    int width,
    int height) {
  self->createTextureData(width, height);
}

//  void QTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache17resizeTextureDataEii(
    QTextureGlyphCache *self,
    int width,
    int height) {
  self->resizeTextureData(width, height);
}

//  int QTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTextureGlyphCache12glyphPaddingEv(
    const QTextureGlyphCache *self) {
  return self->glyphPadding();
}

//  void QTextureGlyphCache::beginFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache16beginFillTextureEv(
    QTextureGlyphCache *self) {
  self->beginFillTexture();
}

//  void QTextureGlyphCache::fillTexture(const Coord &coord, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixedPoint(
    QTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *coord,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->fillTexture(*coord, glyph, *subPixelPosition);
}

//  void QTextureGlyphCache::endFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache14endFillTextureEv(
    QTextureGlyphCache *self) {
  self->endFillTexture();
}

//  void QTextureGlyphCache::createCache(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache11createCacheEii(
    QTextureGlyphCache *self,
    int width,
    int height) {
  self->createCache(width, height);
}

//  void QTextureGlyphCache::resizeCache(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache11resizeCacheEii(
    QTextureGlyphCache *self,
    int width,
    int height) {
  self->resizeCache(width, height);
}

//  bool QTextureGlyphCache::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTextureGlyphCache6isNullEv(
    const QTextureGlyphCache *self) {
  return self->isNull();
}

//  int QTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTextureGlyphCache15maxTextureWidthEv(
    const QTextureGlyphCache *self) {
  return self->maxTextureWidth();
}

//  int QTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTextureGlyphCache16maxTextureHeightEv(
    const QTextureGlyphCache *self) {
  return self->maxTextureHeight();
}

//  QImage QTextureGlyphCache::textureMapForGlyph(glyph_t g, const
//      QFixedPoint &subPixelPosition) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK18QTextureGlyphCache18textureMapForGlyphEjRK11QFixedPoint(
    const QTextureGlyphCache *self,
    glyph_t g,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->textureMapForGlyph(g, *subPixelPosition));
}

//  int QTextureGlyphCache::calculateSubPixelPositionCount(glyph_t a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QTextureGlyphCache30calculateSubPixelPositionCountEj(
    const QTextureGlyphCache *self,
    glyph_t a0) {
  return self->calculateSubPixelPositionCount(a0);
}

//  a Python function taken by a CuteQTextureGlyphCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextureGlyphCache(
    QTextureGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextureGlyphCache *>(self)->take(key, call);
}

//  int QTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QTextureGlyphCache12glyphPaddingEv(
    const QTextureGlyphCache *self) {
  return self->QTextureGlyphCache::glyphPadding();
}

//  void QTextureGlyphCache::beginFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QTextureGlyphCache16beginFillTextureEv(
    QTextureGlyphCache *self) {
  self->QTextureGlyphCache::beginFillTexture();
}

//  void QTextureGlyphCache::endFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QTextureGlyphCache14endFillTextureEv(
    QTextureGlyphCache *self) {
  self->QTextureGlyphCache::endFillTexture();
}

//  int QTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QTextureGlyphCache15maxTextureWidthEv(
    const QTextureGlyphCache *self) {
  return self->QTextureGlyphCache::maxTextureWidth();
}

//  int QTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QTextureGlyphCache16maxTextureHeightEv(
    const QTextureGlyphCache *self) {
  return self->QTextureGlyphCache::maxTextureHeight();
}
