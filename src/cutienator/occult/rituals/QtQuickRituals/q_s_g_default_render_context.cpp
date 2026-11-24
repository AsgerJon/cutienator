//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultrendercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/qquickgraphicsconfiguration.h>
#include <QtGui/qrawfont.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGDefaultRenderContext that Python can take functions over in. Every QSGDefaultRenderContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGDefaultRenderContextCall0)(const void *, int *);
typedef bool (*CuteQSGDefaultRenderContextCall1)(const void *, int *);
typedef void (*CuteQSGDefaultRenderContextCall2)(const void *, const QSGRenderContext::InitParams *, int *);
typedef void (*CuteQSGDefaultRenderContextCall3)(const void *, int *);
typedef void (*CuteQSGDefaultRenderContextCall4)(const void *, qreal, QRhiCommandBuffer *, const QQuickGraphicsConfiguration *, int *);
typedef void (*CuteQSGDefaultRenderContextCall5)(const void *, QSGRenderer *, int *);
typedef void (*CuteQSGDefaultRenderContextCall6)(const void *, QSGRenderer *, int *);
typedef void (*CuteQSGDefaultRenderContextCall7)(const void *, int *);
typedef void (*CuteQSGDefaultRenderContextCall8)(const void *, int *);
typedef void (*CuteQSGDefaultRenderContextCall9)(const void *, int *);
typedef void * (*CuteQSGDefaultRenderContextCall10)(const void *, const QRawFont *, int, int *);
typedef void * (*CuteQSGDefaultRenderContextCall11)(const void *, const QRawFont *, int *);
typedef void * (*CuteQSGDefaultRenderContextCall12)(const void *, const QImage *, uint, int *);
typedef void * (*CuteQSGDefaultRenderContextCall13)(const void *, int, int *);
typedef void * (*CuteQSGDefaultRenderContextCall14)(const void *, const QSGCompressedTextureFactory *, int *);
typedef void (*CuteQSGDefaultRenderContextCall15)(const void *, QSGMaterialShader *, int, int *);
typedef int (*CuteQSGDefaultRenderContextCall16)(const void *, int *);
typedef void (*CuteQSGDefaultRenderContextCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDefaultRenderContextCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDefaultRenderContextCall19)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultRenderContextCall20)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultRenderContextCall21)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultRenderContextCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultRenderContextCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultRenderContextCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGDefaultRenderContext : public QSGDefaultRenderContext {
public:
  using QSGDefaultRenderContext::QSGDefaultRenderContext;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QSGRenderContext3rhiEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext7isValidEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10invalidateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10preprocessEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext21invalidateGlyphCachesEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext16flushGlyphCachesEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext13createTextureERK6QImagej")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext14createRendererEN20QSGRendererInterface10RenderModeE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17QSGMaterialShaderN7QShader7VariantE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext14maxTextureSizeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext7endSyncEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QRhi *QSGDefaultRenderContext::rhi() const
  QRhi *rhi() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall0 call = reinterpret_cast<CuteQSGDefaultRenderContextCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhi *>(given);
    }
    return QSGDefaultRenderContext::rhi();
  }

  //  bool QSGDefaultRenderContext::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall1 call = reinterpret_cast<CuteQSGDefaultRenderContextCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGDefaultRenderContext::isValid();
  }

  //  void QSGDefaultRenderContext::initialize(const
  //      QSGRenderContext::InitParams *params)
  void initialize(const QSGRenderContext::InitParams *params) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall2 call = reinterpret_cast<CuteQSGDefaultRenderContextCall2>(taken[2]);
      call(this, params, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::initialize(params);
  }

  //  void QSGDefaultRenderContext::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall3 call = reinterpret_cast<CuteQSGDefaultRenderContextCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::invalidate();
  }

  //  void QSGDefaultRenderContext::prepareSync(qreal devicePixelRatio,
  //      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
  void prepareSync(
      qreal devicePixelRatio,
      QRhiCommandBuffer *cb,
      const QQuickGraphicsConfiguration &config) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall4 call = reinterpret_cast<CuteQSGDefaultRenderContextCall4>(taken[4]);
      call(this, devicePixelRatio, cb, &config, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::prepareSync(devicePixelRatio, cb, config);
  }

  //  void QSGDefaultRenderContext::renderNextFrame(QSGRenderer *renderer)
  void renderNextFrame(QSGRenderer *renderer) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall5 call = reinterpret_cast<CuteQSGDefaultRenderContextCall5>(taken[5]);
      call(this, renderer, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::renderNextFrame(renderer);
  }

  //  void QSGDefaultRenderContext::endNextFrame(QSGRenderer *renderer)
  void endNextFrame(QSGRenderer *renderer) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall6 call = reinterpret_cast<CuteQSGDefaultRenderContextCall6>(taken[6]);
      call(this, renderer, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::endNextFrame(renderer);
  }

  //  void QSGDefaultRenderContext::preprocess()
  void preprocess() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall7 call = reinterpret_cast<CuteQSGDefaultRenderContextCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::preprocess();
  }

  //  void QSGDefaultRenderContext::invalidateGlyphCaches()
  void invalidateGlyphCaches() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall8 call = reinterpret_cast<CuteQSGDefaultRenderContextCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::invalidateGlyphCaches();
  }

  //  void QSGDefaultRenderContext::flushGlyphCaches()
  void flushGlyphCaches() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall9 call = reinterpret_cast<CuteQSGDefaultRenderContextCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::flushGlyphCaches();
  }

  //  QSGDistanceFieldGlyphCache
  //      *QSGDefaultRenderContext::distanceFieldGlyphCache(const QRawFont
  //      &font, int renderTypeQuality)
  QSGDistanceFieldGlyphCache *distanceFieldGlyphCache(
      const QRawFont &font,
      int renderTypeQuality) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall10 call = reinterpret_cast<CuteQSGDefaultRenderContextCall10>(taken[10]);
      void * given = call(this, &font, renderTypeQuality, &handled);
      if (handled) return static_cast<QSGDistanceFieldGlyphCache *>(given);
    }
    return QSGDefaultRenderContext::distanceFieldGlyphCache(font, renderTypeQuality);
  }

  //  QSGCurveGlyphAtlas *QSGDefaultRenderContext::curveGlyphAtlas(const
  //      QRawFont &font)
  QSGCurveGlyphAtlas *curveGlyphAtlas(const QRawFont &font) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall11 call = reinterpret_cast<CuteQSGDefaultRenderContextCall11>(taken[11]);
      void * given = call(this, &font, &handled);
      if (handled) return static_cast<QSGCurveGlyphAtlas *>(given);
    }
    return QSGDefaultRenderContext::curveGlyphAtlas(font);
  }

  //  QSGTexture *QSGDefaultRenderContext::createTexture(const QImage
  //      &image, uint flags) const
  QSGTexture *createTexture(const QImage &image, uint flags) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall12 call = reinterpret_cast<CuteQSGDefaultRenderContextCall12>(taken[12]);
      void * given = call(this, &image, flags, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGDefaultRenderContext::createTexture(image, flags);
  }

  //  QSGRenderer *QSGDefaultRenderContext::createRenderer(QSGRendererInter
  //      face::RenderMode renderMode)
  QSGRenderer *createRenderer(
      QSGRendererInterface::RenderMode renderMode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall13 call = reinterpret_cast<CuteQSGDefaultRenderContextCall13>(taken[13]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGRenderer *>(given);
    }
    return QSGDefaultRenderContext::createRenderer(renderMode);
  }

  //  QSGTexture
  //      *QSGDefaultRenderContext::compressedTextureForFactory(const
  //      QSGCompressedTextureFactory *factory) const
  QSGTexture *compressedTextureForFactory(
      const QSGCompressedTextureFactory *factory) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall14 call = reinterpret_cast<CuteQSGDefaultRenderContextCall14>(taken[14]);
      void * given = call(this, factory, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGDefaultRenderContext::compressedTextureForFactory(factory);
  }

  //  void QSGDefaultRenderContext::initializeRhiShader(QSGMaterialShader
  //      *shader, QShader::Variant shaderVariant)
  void initializeRhiShader(
      QSGMaterialShader *shader,
      QShader::Variant shaderVariant) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall15 call = reinterpret_cast<CuteQSGDefaultRenderContextCall15>(taken[15]);
      call(this, shader, static_cast<int>(shaderVariant), &handled);
      if (handled) return;
    }
    QSGDefaultRenderContext::initializeRhiShader(shader, shaderVariant);
  }

  //  int QSGDefaultRenderContext::maxTextureSize() const
  int maxTextureSize() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall16 call = reinterpret_cast<CuteQSGDefaultRenderContextCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGDefaultRenderContext::maxTextureSize();
  }

  //  void QSGRenderContext::endSync()
  void endSync() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall17 call = reinterpret_cast<CuteQSGDefaultRenderContextCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::endSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall18 call = reinterpret_cast<CuteQSGDefaultRenderContextCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall19 call = reinterpret_cast<CuteQSGDefaultRenderContextCall19>(taken[19]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall20 call = reinterpret_cast<CuteQSGDefaultRenderContextCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall21 call = reinterpret_cast<CuteQSGDefaultRenderContextCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall22 call = reinterpret_cast<CuteQSGDefaultRenderContextCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall23 call = reinterpret_cast<CuteQSGDefaultRenderContextCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGDefaultRenderContextCall24 call = reinterpret_cast<CuteQSGDefaultRenderContextCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGDefaultRenderContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QSGDefaultRenderContext10metaObjectEv(
    const QSGDefaultRenderContext *self) {
  return self->metaObject();
}

//  QString QSGDefaultRenderContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QSGDefaultRenderContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGDefaultRenderContext::tr(s, c, n));
}

//  QSGDefaultRenderContext::QSGDefaultRenderContext(QSGContext *context)
extern "C" Q_DECL_EXPORT
QSGDefaultRenderContext *ritual_ZN23QSGDefaultRenderContextC1EP10QSGContext(
    QSGContext *context) {
  return new CuteQSGDefaultRenderContext(context);
}

//  QRhi *QSGDefaultRenderContext::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK23QSGDefaultRenderContext3rhiEv(
    const QSGDefaultRenderContext *self) {
  return self->rhi();
}

//  bool QSGDefaultRenderContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSGDefaultRenderContext7isValidEv(
    const QSGDefaultRenderContext *self) {
  return self->isValid();
}

//  void QSGDefaultRenderContext::initialize(const
//      QSGRenderContext::InitParams *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext10initializeEPKN16QSGRenderContext10InitParamsE(
    QSGDefaultRenderContext *self,
    const QSGRenderContext::InitParams *params) {
  self->initialize(params);
}

//  void QSGDefaultRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext10invalidateEv(
    QSGDefaultRenderContext *self) {
  self->invalidate();
}

//  void QSGDefaultRenderContext::prepareSync(qreal devicePixelRatio,
//      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration(
    QSGDefaultRenderContext *self,
    qreal devicePixelRatio,
    QRhiCommandBuffer *cb,
    const QQuickGraphicsConfiguration *config) {
  self->prepareSync(devicePixelRatio, cb, *config);
}

//  void QSGDefaultRenderContext::renderNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext15renderNextFrameEP11QSGRenderer(
    QSGDefaultRenderContext *self,
    QSGRenderer *renderer) {
  self->renderNextFrame(renderer);
}

//  void QSGDefaultRenderContext::endNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext12endNextFrameEP11QSGRenderer(
    QSGDefaultRenderContext *self,
    QSGRenderer *renderer) {
  self->endNextFrame(renderer);
}

//  void QSGDefaultRenderContext::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext10preprocessEv(
    QSGDefaultRenderContext *self) {
  self->preprocess();
}

//  void QSGDefaultRenderContext::invalidateGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext21invalidateGlyphCachesEv(
    QSGDefaultRenderContext *self) {
  self->invalidateGlyphCaches();
}

//  void QSGDefaultRenderContext::flushGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext16flushGlyphCachesEv(
    QSGDefaultRenderContext *self) {
  self->flushGlyphCaches();
}

//  QSGDistanceFieldGlyphCache
//      *QSGDefaultRenderContext::distanceFieldGlyphCache(const QRawFont
//      &font, int renderTypeQuality)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache *ritual_ZN23QSGDefaultRenderContext23distanceFieldGlyphCacheERK8QRawFonti(
    QSGDefaultRenderContext *self,
    const QRawFont *font,
    int renderTypeQuality) {
  return self->distanceFieldGlyphCache(*font, renderTypeQuality);
}

//  QSGCurveGlyphAtlas *QSGDefaultRenderContext::curveGlyphAtlas(const
//      QRawFont &font)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphAtlas *ritual_ZN23QSGDefaultRenderContext15curveGlyphAtlasERK8QRawFont(
    QSGDefaultRenderContext *self,
    const QRawFont *font) {
  return self->curveGlyphAtlas(*font);
}

//  QSGTexture *QSGDefaultRenderContext::createTexture(const QImage &image,
//      uint flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK23QSGDefaultRenderContext13createTextureERK6QImagej(
    const QSGDefaultRenderContext *self,
    const QImage *image,
    uint flags) {
  return self->createTexture(*image, flags);
}

//  QSGRenderer
//      *QSGDefaultRenderContext::createRenderer(QSGRendererInterface::Render
//      Mode renderMode)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_ZN23QSGDefaultRenderContext14createRendererEN20QSGRendererInterface10RenderModeE(
    QSGDefaultRenderContext *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createRenderer(renderMode);
}

//  QSGTexture *QSGDefaultRenderContext::compressedTextureForFactory(const
//      QSGCompressedTextureFactory *factory) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK23QSGDefaultRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory(
    const QSGDefaultRenderContext *self,
    const QSGCompressedTextureFactory *factory) {
  return self->compressedTextureForFactory(factory);
}

//  void QSGDefaultRenderContext::initializeRhiShader(QSGMaterialShader
//      *shader, QShader::Variant shaderVariant)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17QSGMaterialShaderN7QShader7VariantE(
    QSGDefaultRenderContext *self,
    QSGMaterialShader *shader,
    QShader::Variant shaderVariant) {
  self->initializeRhiShader(shader, shaderVariant);
}

//  int QSGDefaultRenderContext::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGDefaultRenderContext14maxTextureSizeEv(
    const QSGDefaultRenderContext *self) {
  return self->maxTextureSize();
}

//  bool QSGDefaultRenderContext::useDepthBufferFor2D() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSGDefaultRenderContext19useDepthBufferFor2DEv(
    const QSGDefaultRenderContext *self) {
  return self->useDepthBufferFor2D();
}

//  int QSGDefaultRenderContext::msaaSampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGDefaultRenderContext15msaaSampleCountEv(
    const QSGDefaultRenderContext *self) {
  return self->msaaSampleCount();
}

//  QRhiCommandBuffer *QSGDefaultRenderContext::currentFrameCommandBuffer()
//      const
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZNK23QSGDefaultRenderContext25currentFrameCommandBufferEv(
    const QSGDefaultRenderContext *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderPassDescriptor
//      *QSGDefaultRenderContext::currentFrameRenderPass() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK23QSGDefaultRenderContext22currentFrameRenderPassEv(
    const QSGDefaultRenderContext *self) {
  return self->currentFrameRenderPass();
}

//  qreal QSGDefaultRenderContext::currentDevicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QSGDefaultRenderContext23currentDevicePixelRatioEv(
    const QSGDefaultRenderContext *self) {
  return self->currentDevicePixelRatio();
}

//  QRhiResourceUpdateBatch
//      *QSGDefaultRenderContext::maybeGlyphCacheResourceUpdates()
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN23QSGDefaultRenderContext30maybeGlyphCacheResourceUpdatesEv(
    QSGDefaultRenderContext *self) {
  return self->maybeGlyphCacheResourceUpdates();
}

//  QRhiResourceUpdateBatch
//      *QSGDefaultRenderContext::glyphCacheResourceUpdates()
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN23QSGDefaultRenderContext25glyphCacheResourceUpdatesEv(
    QSGDefaultRenderContext *self) {
  return self->glyphCacheResourceUpdates();
}

//  void
//      QSGDefaultRenderContext::deferredReleaseGlyphCacheTexture(QRhiTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext32deferredReleaseGlyphCacheTextureEP11QRhiTexture(
    QSGDefaultRenderContext *self,
    QRhiTexture *texture) {
  self->deferredReleaseGlyphCacheTexture(texture);
}

//  void QSGDefaultRenderContext::resetGlyphCacheResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultRenderContext24resetGlyphCacheResourcesEv(
    QSGDefaultRenderContext *self) {
  self->resetGlyphCacheResources();
}

//  a Python function taken by a CuteQSGDefaultRenderContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultRenderContext(
    QSGDefaultRenderContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultRenderContext *>(self)->take(key, call);
}

//  QRhi *QSGDefaultRenderContext::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_own_ZNK23QSGDefaultRenderContext3rhiEv(
    const QSGDefaultRenderContext *self) {
  return self->QSGDefaultRenderContext::rhi();
}

//  bool QSGDefaultRenderContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QSGDefaultRenderContext7isValidEv(
    const QSGDefaultRenderContext *self) {
  return self->QSGDefaultRenderContext::isValid();
}

//  void QSGDefaultRenderContext::initialize(const
//      QSGRenderContext::InitParams *params)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext10initializeEPKN16QSGRenderContext10InitParamsE(
    QSGDefaultRenderContext *self,
    const QSGRenderContext::InitParams *params) {
  self->QSGDefaultRenderContext::initialize(params);
}

//  void QSGDefaultRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext10invalidateEv(
    QSGDefaultRenderContext *self) {
  self->QSGDefaultRenderContext::invalidate();
}

//  void QSGDefaultRenderContext::prepareSync(qreal devicePixelRatio,
//      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration(
    QSGDefaultRenderContext *self,
    qreal devicePixelRatio,
    QRhiCommandBuffer *cb,
    const QQuickGraphicsConfiguration *config) {
  self->QSGDefaultRenderContext::prepareSync(devicePixelRatio, cb, *config);
}

//  void QSGDefaultRenderContext::renderNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext15renderNextFrameEP11QSGRenderer(
    QSGDefaultRenderContext *self,
    QSGRenderer *renderer) {
  self->QSGDefaultRenderContext::renderNextFrame(renderer);
}

//  void QSGDefaultRenderContext::endNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext12endNextFrameEP11QSGRenderer(
    QSGDefaultRenderContext *self,
    QSGRenderer *renderer) {
  self->QSGDefaultRenderContext::endNextFrame(renderer);
}

//  void QSGDefaultRenderContext::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext10preprocessEv(
    QSGDefaultRenderContext *self) {
  self->QSGDefaultRenderContext::preprocess();
}

//  void QSGDefaultRenderContext::invalidateGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext21invalidateGlyphCachesEv(
    QSGDefaultRenderContext *self) {
  self->QSGDefaultRenderContext::invalidateGlyphCaches();
}

//  void QSGDefaultRenderContext::flushGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext16flushGlyphCachesEv(
    QSGDefaultRenderContext *self) {
  self->QSGDefaultRenderContext::flushGlyphCaches();
}

//  QSGDistanceFieldGlyphCache
//      *QSGDefaultRenderContext::distanceFieldGlyphCache(const QRawFont
//      &font, int renderTypeQuality)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache *ritual_own_ZN23QSGDefaultRenderContext23distanceFieldGlyphCacheERK8QRawFonti(
    QSGDefaultRenderContext *self,
    const QRawFont *font,
    int renderTypeQuality) {
  return self->QSGDefaultRenderContext::distanceFieldGlyphCache(
      *font,
      renderTypeQuality);
}

//  QSGCurveGlyphAtlas *QSGDefaultRenderContext::curveGlyphAtlas(const
//      QRawFont &font)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphAtlas *ritual_own_ZN23QSGDefaultRenderContext15curveGlyphAtlasERK8QRawFont(
    QSGDefaultRenderContext *self,
    const QRawFont *font) {
  return self->QSGDefaultRenderContext::curveGlyphAtlas(*font);
}

//  QSGTexture *QSGDefaultRenderContext::createTexture(const QImage &image,
//      uint flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK23QSGDefaultRenderContext13createTextureERK6QImagej(
    const QSGDefaultRenderContext *self,
    const QImage *image,
    uint flags) {
  return self->QSGDefaultRenderContext::createTexture(*image, flags);
}

//  QSGRenderer
//      *QSGDefaultRenderContext::createRenderer(QSGRendererInterface::Render
//      Mode renderMode)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_own_ZN23QSGDefaultRenderContext14createRendererEN20QSGRendererInterface10RenderModeE(
    QSGDefaultRenderContext *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGDefaultRenderContext::createRenderer(renderMode);
}

//  QSGTexture *QSGDefaultRenderContext::compressedTextureForFactory(const
//      QSGCompressedTextureFactory *factory) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK23QSGDefaultRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory(
    const QSGDefaultRenderContext *self,
    const QSGCompressedTextureFactory *factory) {
  return self->QSGDefaultRenderContext::compressedTextureForFactory(factory);
}

//  void QSGDefaultRenderContext::initializeRhiShader(QSGMaterialShader
//      *shader, QShader::Variant shaderVariant)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultRenderContext19initializeRhiShaderEP17QSGMaterialShaderN7QShader7VariantE(
    QSGDefaultRenderContext *self,
    QSGMaterialShader *shader,
    QShader::Variant shaderVariant) {
  self->QSGDefaultRenderContext::initializeRhiShader(shader, shaderVariant);
}

//  int QSGDefaultRenderContext::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QSGDefaultRenderContext14maxTextureSizeEv(
    const QSGDefaultRenderContext *self) {
  return self->QSGDefaultRenderContext::maxTextureSize();
}
