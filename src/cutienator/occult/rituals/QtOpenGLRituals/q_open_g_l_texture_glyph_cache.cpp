//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QOpenGLTextureGlyphCache that Python can take functions over in. Every QOpenGLTextureGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOpenGLTextureGlyphCacheCall0)(const void *, int, int, int *);
typedef void (*CuteQOpenGLTextureGlyphCacheCall1)(const void *, int, int, int *);
typedef void (*CuteQOpenGLTextureGlyphCacheCall2)(const void *, const QTextureGlyphCache::Coord *, glyph_t, const QFixedPoint *, int *);
typedef int (*CuteQOpenGLTextureGlyphCacheCall3)(const void *, int *);
typedef int (*CuteQOpenGLTextureGlyphCacheCall4)(const void *, int *);
typedef int (*CuteQOpenGLTextureGlyphCacheCall5)(const void *, int *);
typedef void (*CuteQOpenGLTextureGlyphCacheCall6)(const void *, int *);
typedef void (*CuteQOpenGLTextureGlyphCacheCall7)(const void *, int *);
class CuteQOpenGLTextureGlyphCache : public QOpenGLTextureGlyphCache {
public:
  using QOpenGLTextureGlyphCache::QOpenGLTextureGlyphCache;
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
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache15maxTextureWidthEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache16maxTextureHeightEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache16beginFillTextureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache14endFillTextureEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QOpenGLTextureGlyphCache::createTextureData(int width, int
  //      height)
  void createTextureData(int width, int height) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall0 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall0>(taken[0]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QOpenGLTextureGlyphCache::createTextureData(width, height);
  }

  //  void QOpenGLTextureGlyphCache::resizeTextureData(int width, int
  //      height)
  void resizeTextureData(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall1 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QOpenGLTextureGlyphCache::resizeTextureData(width, height);
  }

  //  void QOpenGLTextureGlyphCache::fillTexture(const Coord &c, glyph_t
  //      glyph, const QFixedPoint &subPixelPosition)
  void fillTexture(
      const QTextureGlyphCache::Coord &c,
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall2 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall2>(taken[2]);
      call(this, &c, glyph, &subPixelPosition, &handled);
      if (handled) return;
    }
    QOpenGLTextureGlyphCache::fillTexture(c, glyph, subPixelPosition);
  }

  //  int QOpenGLTextureGlyphCache::glyphPadding() const
  int glyphPadding() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall3 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLTextureGlyphCache::glyphPadding();
  }

  //  int QOpenGLTextureGlyphCache::maxTextureWidth() const
  int maxTextureWidth() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall4 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLTextureGlyphCache::maxTextureWidth();
  }

  //  int QOpenGLTextureGlyphCache::maxTextureHeight() const
  int maxTextureHeight() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall5 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QOpenGLTextureGlyphCache::maxTextureHeight();
  }

  //  void QTextureGlyphCache::beginFillTexture()
  void beginFillTexture() override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall6 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::beginFillTexture();
  }

  //  void QTextureGlyphCache::endFillTexture()
  void endFillTexture() override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGLTextureGlyphCacheCall7 call = reinterpret_cast<CuteQOpenGLTextureGlyphCacheCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QTextureGlyphCache::endFillTexture();
  }
};

//  QOpenGLTextureGlyphCache::QOpenGLTextureGlyphCache(QFontEngine::GlyphForm
//      at glyphFormat, const QTransform &matrix, const QColor &color)
extern "C" Q_DECL_EXPORT
QOpenGLTextureGlyphCache *ritual_ZN24QOpenGLTextureGlyphCacheC1EN11QFontEngine11GlyphFormatERK10QTransformRK6QColor(
    QFontEngine::GlyphFormat glyphFormat,
    const QTransform *matrix,
    const QColor *color) {
  return new CuteQOpenGLTextureGlyphCache(glyphFormat, *matrix, *color);
}

//  QOpenGLTextureGlyphCache::~QOpenGLTextureGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCacheD1Ev(
    QOpenGLTextureGlyphCache *self) {
  delete self;
}

//  void QOpenGLTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache17createTextureDataEii(
    QOpenGLTextureGlyphCache *self,
    int width,
    int height) {
  self->createTextureData(width, height);
}

//  void QOpenGLTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache17resizeTextureDataEii(
    QOpenGLTextureGlyphCache *self,
    int width,
    int height) {
  self->resizeTextureData(width, height);
}

//  void QOpenGLTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QOpenGLTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->fillTexture(*c, glyph, *subPixelPosition);
}

//  int QOpenGLTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache12glyphPaddingEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->glyphPadding();
}

//  int QOpenGLTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache15maxTextureWidthEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->maxTextureWidth();
}

//  int QOpenGLTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache16maxTextureHeightEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->maxTextureHeight();
}

//  int QOpenGLTextureGlyphCache::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache5widthEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->width();
}

//  int QOpenGLTextureGlyphCache::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache6heightEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->height();
}

//  void QOpenGLTextureGlyphCache::setPaintEnginePrivate(QOpenGL2PaintEngineE
//      xPrivate *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache21setPaintEnginePrivateEP28QOpenGL2PaintEngineExPrivate(
    QOpenGLTextureGlyphCache *self,
    QOpenGL2PaintEngineExPrivate *p) {
  self->setPaintEnginePrivate(p);
}

//  const QOpenGLContextGroup *QOpenGLTextureGlyphCache::contextGroup() const
extern "C" Q_DECL_EXPORT
const QOpenGLContextGroup *ritual_ZNK24QOpenGLTextureGlyphCache12contextGroupEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->contextGroup();
}

//  int QOpenGLTextureGlyphCache::serialNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpenGLTextureGlyphCache12serialNumberEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->serialNumber();
}

//  FilterMode QOpenGLTextureGlyphCache::filterMode() const
extern "C" Q_DECL_EXPORT
QOpenGLTextureGlyphCache::FilterMode ritual_ZNK24QOpenGLTextureGlyphCache10filterModeEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->filterMode();
}

//  void QOpenGLTextureGlyphCache::setFilterMode(FilterMode m)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache13setFilterModeENS_10FilterModeE(
    QOpenGLTextureGlyphCache *self,
    QOpenGLTextureGlyphCache::FilterMode m) {
  self->setFilterMode(m);
}

//  void QOpenGLTextureGlyphCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache5clearEv(
    QOpenGLTextureGlyphCache *self) {
  self->clear();
}

//  QOpenGL2PaintEngineExPrivate
//      *QOpenGLTextureGlyphCache::paintEnginePrivate() const
extern "C" Q_DECL_EXPORT
QOpenGL2PaintEngineExPrivate *ritual_ZNK24QOpenGLTextureGlyphCache18paintEnginePrivateEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->paintEnginePrivate();
}

//  void QOpenGLTextureGlyphCache::setupVertexAttribs()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLTextureGlyphCache18setupVertexAttribsEv(
    QOpenGLTextureGlyphCache *self) {
  self->setupVertexAttribs();
}

//  a Python function taken by a CuteQOpenGLTextureGlyphCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLTextureGlyphCache(
    QOpenGLTextureGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLTextureGlyphCache *>(self)->take(key, call);
}

//  void QOpenGLTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QOpenGLTextureGlyphCache17createTextureDataEii(
    QOpenGLTextureGlyphCache *self,
    int width,
    int height) {
  self->QOpenGLTextureGlyphCache::createTextureData(width, height);
}

//  void QOpenGLTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QOpenGLTextureGlyphCache17resizeTextureDataEii(
    QOpenGLTextureGlyphCache *self,
    int width,
    int height) {
  self->QOpenGLTextureGlyphCache::resizeTextureData(width, height);
}

//  void QOpenGLTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QOpenGLTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QOpenGLTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->QOpenGLTextureGlyphCache::fillTexture(*c, glyph, *subPixelPosition);
}

//  int QOpenGLTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QOpenGLTextureGlyphCache12glyphPaddingEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->QOpenGLTextureGlyphCache::glyphPadding();
}

//  int QOpenGLTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QOpenGLTextureGlyphCache15maxTextureWidthEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->QOpenGLTextureGlyphCache::maxTextureWidth();
}

//  int QOpenGLTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QOpenGLTextureGlyphCache16maxTextureHeightEv(
    const QOpenGLTextureGlyphCache *self) {
  return self->QOpenGLTextureGlyphCache::maxTextureHeight();
}
