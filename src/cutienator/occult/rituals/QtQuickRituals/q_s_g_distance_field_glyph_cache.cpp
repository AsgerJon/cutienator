//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdistancefield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSGDistanceFieldGlyphCache that Python can take functions over in. Every QSGDistanceFieldGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDistanceFieldGlyphCacheCall0)(const void *, int *);
typedef bool (*CuteQSGDistanceFieldGlyphCacheCall1)(const void *, int *);
typedef bool (*CuteQSGDistanceFieldGlyphCacheCall2)(const void *, int *);
typedef bool (*CuteQSGDistanceFieldGlyphCacheCall3)(const void *, int *);
class CuteQSGDistanceFieldGlyphCache : public QSGDistanceFieldGlyphCache {
public:
  using QSGDistanceFieldGlyphCache::QSGDistanceFieldGlyphCache;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv")) {
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
    if (!std::strcmp(key, "_ZNK26QSGDistanceFieldGlyphCache8isActiveEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSGDistanceFieldGlyphCache::processPendingGlyphs()
  void processPendingGlyphs() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphCacheCall0 call = reinterpret_cast<CuteQSGDistanceFieldGlyphCacheCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphCache::processPendingGlyphs();
  }

  //  bool QSGDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled()
  //      const
  bool eightBitFormatIsAlphaSwizzled() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphCacheCall1 call = reinterpret_cast<CuteQSGDistanceFieldGlyphCacheCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
  //      const
  bool screenSpaceDerivativesSupported() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphCacheCall2 call = reinterpret_cast<CuteQSGDistanceFieldGlyphCacheCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGDistanceFieldGlyphCache::isActive() const
  bool isActive() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphCacheCall3 call = reinterpret_cast<CuteQSGDistanceFieldGlyphCacheCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldGlyphCache::isActive();
  }
};

//  QSGDistanceFieldGlyphCache::~QSGDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCacheD1Ev(
    QSGDistanceFieldGlyphCache *self) {
  delete self;
}

//  const QRawFont &QSGDistanceFieldGlyphCache::referenceFont() const
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZNK26QSGDistanceFieldGlyphCache13referenceFontEv(
    const QSGDistanceFieldGlyphCache *self) {
  return new QRawFont(self->referenceFont());
}

//  qreal QSGDistanceFieldGlyphCache::fontScale(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QSGDistanceFieldGlyphCache9fontScaleEd(
    const QSGDistanceFieldGlyphCache *self,
    qreal pixelSize) {
  return self->fontScale(pixelSize);
}

//  qreal QSGDistanceFieldGlyphCache::distanceFieldRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QSGDistanceFieldGlyphCache19distanceFieldRadiusEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->distanceFieldRadius();
}

//  int QSGDistanceFieldGlyphCache::glyphCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QSGDistanceFieldGlyphCache10glyphCountEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->glyphCount();
}

//  bool QSGDistanceFieldGlyphCache::doubleGlyphResolution() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGDistanceFieldGlyphCache21doubleGlyphResolutionEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->doubleGlyphResolution();
}

//  int QSGDistanceFieldGlyphCache::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QSGDistanceFieldGlyphCache17renderTypeQualityEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->renderTypeQuality();
}

//  Metrics QSGDistanceFieldGlyphCache::glyphMetrics(glyph_t glyph, qreal
//      pixelSize)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache::Metrics *ritual_ZN26QSGDistanceFieldGlyphCache12glyphMetricsEjd(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph,
    qreal pixelSize) {
  return new QSGDistanceFieldGlyphCache::Metrics(
      self->glyphMetrics(
          glyph,
          pixelSize));
}

//  TexCoord QSGDistanceFieldGlyphCache::glyphTexCoord(glyph_t glyph)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache::TexCoord *ritual_ZN26QSGDistanceFieldGlyphCache13glyphTexCoordEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  return new QSGDistanceFieldGlyphCache::TexCoord(
      self->glyphTexCoord(
          glyph));
}

//  const Texture *QSGDistanceFieldGlyphCache::glyphTexture(glyph_t glyph)
extern "C" Q_DECL_EXPORT
const QSGDistanceFieldGlyphCache::Texture *ritual_ZN26QSGDistanceFieldGlyphCache12glyphTextureEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  return self->glyphTexture(glyph);
}

//  void QSGDistanceFieldGlyphCache::populate(const QList<glyph_t> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache8populateERK5QListIjE(
    QSGDistanceFieldGlyphCache *self,
    const QList<glyph_t> *glyphs) {
  self->populate(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::release(const QList<glyph_t> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache7releaseERK5QListIjE(
    QSGDistanceFieldGlyphCache *self,
    const QList<glyph_t> *glyphs) {
  self->release(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache6updateEv(
    QSGDistanceFieldGlyphCache *self) {
  self->update();
}

//  void QSGDistanceFieldGlyphCache::registerGlyphNode(QSGDistanceFieldGlyphC
//      onsumer *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache17registerGlyphNodeEP29QSGDistanceFieldGlyphConsumer(
    QSGDistanceFieldGlyphCache *self,
    QSGDistanceFieldGlyphConsumer *node) {
  self->registerGlyphNode(node);
}

//  void QSGDistanceFieldGlyphCache::unregisterGlyphNode(QSGDistanceFieldGlyp
//      hConsumer *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache19unregisterGlyphNodeEP29QSGDistanceFieldGlyphConsumer(
    QSGDistanceFieldGlyphCache *self,
    QSGDistanceFieldGlyphConsumer *node) {
  self->unregisterGlyphNode(node);
}

//  void QSGDistanceFieldGlyphCache::processPendingGlyphs()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv(
    QSGDistanceFieldGlyphCache *self) {
  self->processPendingGlyphs();
}

//  bool QSGDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizzledEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->eightBitFormatIsAlphaSwizzled();
}

//  bool QSGDistanceFieldGlyphCache::screenSpaceDerivativesSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGDistanceFieldGlyphCache31screenSpaceDerivativesSupportedEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->screenSpaceDerivativesSupported();
}

//  bool QSGDistanceFieldGlyphCache::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QSGDistanceFieldGlyphCache8isActiveEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->isActive();
}

//  void QSGDistanceFieldGlyphCache::requestGlyphs(const QSet<glyph_t>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache13requestGlyphsERK4QSetIjE(
    QSGDistanceFieldGlyphCache *self,
    const QSet<glyph_t> *glyphs) {
  self->requestGlyphs(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::storeGlyphs(const QList<QDistanceField>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache11storeGlyphsERK5QListI14QDistanceFieldE(
    QSGDistanceFieldGlyphCache *self,
    const QList<QDistanceField> *glyphs) {
  self->storeGlyphs(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::referenceGlyphs(const QSet<glyph_t>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache15referenceGlyphsERK4QSetIjE(
    QSGDistanceFieldGlyphCache *self,
    const QSet<glyph_t> *glyphs) {
  self->referenceGlyphs(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::releaseGlyphs(const QSet<glyph_t>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache13releaseGlyphsERK4QSetIjE(
    QSGDistanceFieldGlyphCache *self,
    const QSet<glyph_t> *glyphs) {
  self->releaseGlyphs(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::setGlyphsPosition(const
//      QList<GlyphPosition> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache17setGlyphsPositionERK5QListINS_13GlyphPositionEE(
    QSGDistanceFieldGlyphCache *self,
    const QList<QSGDistanceFieldGlyphCache::GlyphPosition> *glyphs) {
  self->setGlyphsPosition(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::setGlyphsTexture(const QList<glyph_t>
//      &glyphs, const Texture &tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache16setGlyphsTextureERK5QListIjERKNS_7TextureE(
    QSGDistanceFieldGlyphCache *self,
    const QList<glyph_t> *glyphs,
    const QSGDistanceFieldGlyphCache::Texture *tex) {
  self->setGlyphsTexture(*glyphs, *tex);
}

//  void QSGDistanceFieldGlyphCache::markGlyphsToRender(const QList<glyph_t>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache18markGlyphsToRenderERK5QListIjE(
    QSGDistanceFieldGlyphCache *self,
    const QList<glyph_t> *glyphs) {
  self->markGlyphsToRender(*glyphs);
}

//  void QSGDistanceFieldGlyphCache::removeGlyph(glyph_t glyph)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache11removeGlyphEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  self->removeGlyph(glyph);
}

//  void QSGDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture *oldTex,
//      QRhiTexture *newTex, const QSize &newTexSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSGDistanceFieldGlyphCache16updateRhiTextureEP11QRhiTextureS1_RK5QSize(
    QSGDistanceFieldGlyphCache *self,
    QRhiTexture *oldTex,
    QRhiTexture *newTex,
    const QSize *newTexSize) {
  self->updateRhiTexture(oldTex, newTex, *newTexSize);
}

//  bool QSGDistanceFieldGlyphCache::containsGlyph(glyph_t glyph)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QSGDistanceFieldGlyphCache13containsGlyphEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  return self->containsGlyph(glyph);
}

//  GlyphData &QSGDistanceFieldGlyphCache::glyphData(glyph_t glyph)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache::GlyphData *ritual_ZN26QSGDistanceFieldGlyphCache9glyphDataEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  return &(self->glyphData(glyph));
}

//  GlyphData &QSGDistanceFieldGlyphCache::emptyData(glyph_t glyph)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache::GlyphData *ritual_ZN26QSGDistanceFieldGlyphCache9emptyDataEj(
    QSGDistanceFieldGlyphCache *self,
    glyph_t glyph) {
  return &(self->emptyData(glyph));
}

//  int QSGDistanceFieldGlyphCache::baseFontSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QSGDistanceFieldGlyphCache12baseFontSizeEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->baseFontSize();
}

//  a Python function taken by a CuteQSGDistanceFieldGlyphCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldGlyphCache(
    QSGDistanceFieldGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldGlyphCache *>(self)->take(key, call);
}

//  void QSGDistanceFieldGlyphCache::processPendingGlyphs()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv(
    QSGDistanceFieldGlyphCache *self) {
  self->QSGDistanceFieldGlyphCache::processPendingGlyphs();
}

//  bool QSGDistanceFieldGlyphCache::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QSGDistanceFieldGlyphCache8isActiveEv(
    const QSGDistanceFieldGlyphCache *self) {
  return self->QSGDistanceFieldGlyphCache::isActive();
}
