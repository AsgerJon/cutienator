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

//  A QImageTextureGlyphCache that Python can take functions over in. Every QImageTextureGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQImageTextureGlyphCacheCall0)(const void *, int, int, int *);
typedef void (*CuteQImageTextureGlyphCacheCall1)(const void *, int, int, int *);
typedef void (*CuteQImageTextureGlyphCacheCall2)(const void *, const QTextureGlyphCache::Coord *, glyph_t, const QFixedPoint *, int *);
typedef int (*CuteQImageTextureGlyphCacheCall3)(const void *, int *);
typedef void (*CuteQImageTextureGlyphCacheCall4)(const void *, int *);
typedef void (*CuteQImageTextureGlyphCacheCall5)(const void *, int *);
typedef int (*CuteQImageTextureGlyphCacheCall6)(const void *, int *);
typedef int (*CuteQImageTextureGlyphCacheCall7)(const void *, int *);
class CuteQImageTextureGlyphCache : public QImageTextureGlyphCache {
public:
  using QImageTextureGlyphCache::QImageTextureGlyphCache;
  CuteQImageTextureGlyphCache(const QImageTextureGlyphCache &other) : QImageTextureGlyphCache(other) {}
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
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixedPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache12glyphPaddingEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache16beginFillTextureEv")) {
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

  //  void QImageTextureGlyphCache::createTextureData(int width, int
  //      height)
  void createTextureData(int width, int height) override {
    if (taken[0]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall0 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall0>(taken[0]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QImageTextureGlyphCache::createTextureData(width, height);
  }

  //  void QImageTextureGlyphCache::resizeTextureData(int width, int
  //      height)
  void resizeTextureData(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall1 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QImageTextureGlyphCache::resizeTextureData(width, height);
  }

  //  void QImageTextureGlyphCache::fillTexture(const Coord &c, glyph_t
  //      glyph, const QFixedPoint &subPixelPosition)
  void fillTexture(
      const QTextureGlyphCache::Coord &c,
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall2 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall2>(taken[2]);
      call(this, &c, glyph, &subPixelPosition, &handled);
      if (handled) return;
    }
    QImageTextureGlyphCache::fillTexture(c, glyph, subPixelPosition);
  }

  //  int QTextureGlyphCache::glyphPadding() const
  int glyphPadding() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall3 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::glyphPadding();
  }

  //  void QTextureGlyphCache::beginFillTexture()
  void beginFillTexture() override {
    if (taken[4]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall4 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::beginFillTexture();
  }

  //  void QTextureGlyphCache::endFillTexture()
  void endFillTexture() override {
    if (taken[5]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall5 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::endFillTexture();
  }

  //  int QTextureGlyphCache::maxTextureWidth() const
  int maxTextureWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall6 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::maxTextureWidth();
  }

  //  int QTextureGlyphCache::maxTextureHeight() const
  int maxTextureHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQImageTextureGlyphCacheCall7 call = reinterpret_cast<CuteQImageTextureGlyphCacheCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTextureGlyphCache::maxTextureHeight();
  }
};

//  QImageTextureGlyphCache::QImageTextureGlyphCache(QFontEngine::GlyphFormat
//      format, const QTransform &matrix, const QColor &color)
extern "C" Q_DECL_EXPORT
QImageTextureGlyphCache *ritual_ZN23QImageTextureGlyphCacheC1EN11QFontEngine11GlyphFormatERK10QTransformRK6QColor(
    QFontEngine::GlyphFormat format,
    const QTransform *matrix,
    const QColor *color) {
  return new CuteQImageTextureGlyphCache(format, *matrix, *color);
}

//  QImageTextureGlyphCache::~QImageTextureGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QImageTextureGlyphCacheD1Ev(QImageTextureGlyphCache *self) {
  delete self;
}

//  void QImageTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QImageTextureGlyphCache17createTextureDataEii(
    QImageTextureGlyphCache *self,
    int width,
    int height) {
  self->createTextureData(width, height);
}

//  void QImageTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QImageTextureGlyphCache17resizeTextureDataEii(
    QImageTextureGlyphCache *self,
    int width,
    int height) {
  self->resizeTextureData(width, height);
}

//  void QImageTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QImageTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QImageTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->fillTexture(*c, glyph, *subPixelPosition);
}

//  const QImage &QImageTextureGlyphCache::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK23QImageTextureGlyphCache5imageEv(
    const QImageTextureGlyphCache *self) {
  return new QImage(self->image());
}

//  a Python function taken by a CuteQImageTextureGlyphCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QImageTextureGlyphCache(
    QImageTextureGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQImageTextureGlyphCache *>(self)->take(key, call);
}

//  void QImageTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QImageTextureGlyphCache17createTextureDataEii(
    QImageTextureGlyphCache *self,
    int width,
    int height) {
  self->QImageTextureGlyphCache::createTextureData(width, height);
}

//  void QImageTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QImageTextureGlyphCache17resizeTextureDataEii(
    QImageTextureGlyphCache *self,
    int width,
    int height) {
  self->QImageTextureGlyphCache::resizeTextureData(width, height);
}

//  void QImageTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QImageTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QImageTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->QImageTextureGlyphCache::fillTexture(*c, glyph, *subPixelPosition);
}
