//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhidistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhidistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdistancefield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QSGRhiDistanceFieldGlyphCache that Python can take functions over in. Every QSGRhiDistanceFieldGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRhiDistanceFieldGlyphCacheCall0)(const void *, int *);
typedef bool (*CuteQSGRhiDistanceFieldGlyphCacheCall1)(const void *, int *);
typedef bool (*CuteQSGRhiDistanceFieldGlyphCacheCall2)(const void *, int *);
typedef void (*CuteQSGRhiDistanceFieldGlyphCacheCall3)(const void *, int *);
class CuteQSGRhiDistanceFieldGlyphCache : public QSGRhiDistanceFieldGlyphCache {
public:
  using QSGRhiDistanceFieldGlyphCache::QSGRhiDistanceFieldGlyphCache;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QSGDistanceFieldGlyphCache8isActiveEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QSGDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizzledEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QSGDistanceFieldGlyphCache31screenSpaceDerivativesSupportedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QSGRhiDistanceFieldGlyphCache::isActive() const
  bool isActive() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiDistanceFieldGlyphCacheCall0 call = reinterpret_cast<CuteQSGRhiDistanceFieldGlyphCacheCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiDistanceFieldGlyphCache::isActive();
  }

  //  bool QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled()
  //      const
  bool eightBitFormatIsAlphaSwizzled() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiDistanceFieldGlyphCacheCall1 call = reinterpret_cast<CuteQSGRhiDistanceFieldGlyphCacheCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled();
  }

  //  bool QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
  //      const
  bool screenSpaceDerivativesSupported() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiDistanceFieldGlyphCacheCall2 call = reinterpret_cast<CuteQSGRhiDistanceFieldGlyphCacheCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported();
  }

  //  void QSGDistanceFieldGlyphCache::processPendingGlyphs()
  void processPendingGlyphs() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiDistanceFieldGlyphCacheCall3 call = reinterpret_cast<CuteQSGRhiDistanceFieldGlyphCacheCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphCache::processPendingGlyphs();
  }
};

//  QSGRhiDistanceFieldGlyphCache::QSGRhiDistanceFieldGlyphCache(QSGDefaultRe
//      nderContext *rc, const QRawFont &font, int renderTypeQuality)
extern "C" Q_DECL_EXPORT
QSGRhiDistanceFieldGlyphCache *ritual_ZN29QSGRhiDistanceFieldGlyphCacheC1EP23QSGDefaultRenderContextRK8QRawFonti(
    QSGDefaultRenderContext *rc,
    const QRawFont *font,
    int renderTypeQuality) {
  return new CuteQSGRhiDistanceFieldGlyphCache(rc, *font, renderTypeQuality);
}

//  QSGRhiDistanceFieldGlyphCache::~QSGRhiDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGRhiDistanceFieldGlyphCacheD1Ev(
    QSGRhiDistanceFieldGlyphCache *self) {
  delete self;
}

//  void QSGRhiDistanceFieldGlyphCache::storeGlyphs(const
//      QList<QDistanceField> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGRhiDistanceFieldGlyphCache11storeGlyphsERK5QListI14QDistanceFieldE(
    QSGRhiDistanceFieldGlyphCache *self,
    const QList<QDistanceField> *glyphs) {
  self->storeGlyphs(*glyphs);
}

//  bool QSGRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGRhiDistanceFieldGlyphCache26useTextureResizeWorkaroundEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->useTextureResizeWorkaround();
}

//  bool QSGRhiDistanceFieldGlyphCache::createFullSizeTextures() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGRhiDistanceFieldGlyphCache22createFullSizeTexturesEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->createFullSizeTextures();
}

//  bool QSGRhiDistanceFieldGlyphCache::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGRhiDistanceFieldGlyphCache8isActiveEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->isActive();
}

//  int QSGRhiDistanceFieldGlyphCache::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QSGRhiDistanceFieldGlyphCache14maxTextureSizeEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->maxTextureSize();
}

//  void QSGRhiDistanceFieldGlyphCache::setMaxTextureCount(int max)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGRhiDistanceFieldGlyphCache18setMaxTextureCountEi(
    QSGRhiDistanceFieldGlyphCache *self,
    int max) {
  self->setMaxTextureCount(max);
}

//  int QSGRhiDistanceFieldGlyphCache::maxTextureCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QSGRhiDistanceFieldGlyphCache15maxTextureCountEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->maxTextureCount();
}

//  void QSGRhiDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpd
//      ateBatch *mergeInto)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGRhiDistanceFieldGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatch(
    QSGRhiDistanceFieldGlyphCache *self,
    QRhiResourceUpdateBatch *mergeInto) {
  self->commitResourceUpdates(mergeInto);
}

//  bool QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGRhiDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizzledEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->eightBitFormatIsAlphaSwizzled();
}

//  bool QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGRhiDistanceFieldGlyphCache31screenSpaceDerivativesSupportedEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->screenSpaceDerivativesSupported();
}

//  bool QSGRhiDistanceFieldGlyphCache::loadPregeneratedCache(const QRawFont
//      &font)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QSGRhiDistanceFieldGlyphCache21loadPregeneratedCacheERK8QRawFont(
    QSGRhiDistanceFieldGlyphCache *self,
    const QRawFont *font) {
  return self->loadPregeneratedCache(*font);
}

//  a Python function taken by a CuteQSGRhiDistanceFieldGlyphCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiDistanceFieldGlyphCache(
    QSGRhiDistanceFieldGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiDistanceFieldGlyphCache *>(self)->take(key, call);
}

//  bool QSGRhiDistanceFieldGlyphCache::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache8isActiveEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->QSGRhiDistanceFieldGlyphCache::isActive();
}

//  bool QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizzledEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->QSGRhiDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled();
}

//  bool QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QSGRhiDistanceFieldGlyphCache31screenSpaceDerivativesSupportedEv(
    const QSGRhiDistanceFieldGlyphCache *self) {
  return self->QSGRhiDistanceFieldGlyphCache::screenSpaceDerivativesSupported();
}
