//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/qquickgraphicsconfiguration.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRenderContext that Python can take functions over in. Every QSGRenderContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRenderContextCall0)(const void *, int *);
typedef void (*CuteQSGRenderContextCall1)(const void *, const QSGRenderContext::InitParams *, int *);
typedef void (*CuteQSGRenderContextCall2)(const void *, int *);
typedef void (*CuteQSGRenderContextCall3)(const void *, qreal, QRhiCommandBuffer *, const QQuickGraphicsConfiguration *, int *);
typedef void (*CuteQSGRenderContextCall4)(const void *, QSGRenderer *, int *);
typedef void (*CuteQSGRenderContextCall5)(const void *, QSGRenderer *, int *);
typedef void (*CuteQSGRenderContextCall6)(const void *, int *);
typedef void (*CuteQSGRenderContextCall7)(const void *, int *);
typedef void (*CuteQSGRenderContextCall8)(const void *, int *);
typedef void (*CuteQSGRenderContextCall9)(const void *, int *);
typedef void * (*CuteQSGRenderContextCall10)(const void *, const QRawFont *, int, int *);
typedef void * (*CuteQSGRenderContextCall11)(const void *, const QRawFont *, int *);
typedef void * (*CuteQSGRenderContextCall12)(const void *, const QImage *, uint, int *);
typedef void * (*CuteQSGRenderContextCall13)(const void *, int, int *);
typedef void * (*CuteQSGRenderContextCall14)(const void *, const QSGCompressedTextureFactory *, int *);
typedef int (*CuteQSGRenderContextCall15)(const void *, int *);
typedef void * (*CuteQSGRenderContextCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRenderContextCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRenderContextCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderContextCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderContextCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderContextCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderContextCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRenderContextCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRenderContext : public QSGRenderContext {
public:
  using QSGRenderContext::QSGRenderContext;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QSGRenderContext7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext10invalidateEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRenderContext7endSyncEv")) {
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
    if (!std::strcmp(key, "_ZNK16QSGRenderContext14maxTextureSizeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRenderContext3rhiEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSGRenderContext::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRenderContextCall0 call = reinterpret_cast<CuteQSGRenderContextCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderContext::isValid();
  }

  //  void QSGRenderContext::initialize(const InitParams *params)
  void initialize(const QSGRenderContext::InitParams *params) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRenderContextCall1 call = reinterpret_cast<CuteQSGRenderContextCall1>(taken[1]);
      call(this, params, &handled);
      if (handled) return;
    }
    QSGRenderContext::initialize(params);
  }

  //  void QSGRenderContext::invalidate()
  void invalidate() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRenderContextCall2 call = reinterpret_cast<CuteQSGRenderContextCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::invalidate();
  }

  //  void QSGRenderContext::prepareSync(qreal devicePixelRatio,
  //      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
  void prepareSync(
      qreal devicePixelRatio,
      QRhiCommandBuffer *cb,
      const QQuickGraphicsConfiguration &config) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRenderContextCall3 call = reinterpret_cast<CuteQSGRenderContextCall3>(taken[3]);
      call(this, devicePixelRatio, cb, &config, &handled);
      if (handled) return;
    }
    QSGRenderContext::prepareSync(devicePixelRatio, cb, config);
  }

  //  void QSGRenderContext::renderNextFrame(QSGRenderer *renderer)
  void renderNextFrame(QSGRenderer *renderer) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRenderContextCall4 call = reinterpret_cast<CuteQSGRenderContextCall4>(taken[4]);
      call(this, renderer, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderContext::endNextFrame(QSGRenderer *renderer)
  void endNextFrame(QSGRenderer *renderer) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRenderContextCall5 call = reinterpret_cast<CuteQSGRenderContextCall5>(taken[5]);
      call(this, renderer, &handled);
      if (handled) return;
    }
    QSGRenderContext::endNextFrame(renderer);
  }

  //  void QSGRenderContext::endSync()
  void endSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRenderContextCall6 call = reinterpret_cast<CuteQSGRenderContextCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::endSync();
  }

  //  void QSGRenderContext::preprocess()
  void preprocess() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRenderContextCall7 call = reinterpret_cast<CuteQSGRenderContextCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::preprocess();
  }

  //  void QSGRenderContext::invalidateGlyphCaches()
  void invalidateGlyphCaches() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRenderContextCall8 call = reinterpret_cast<CuteQSGRenderContextCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::invalidateGlyphCaches();
  }

  //  void QSGRenderContext::flushGlyphCaches()
  void flushGlyphCaches() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRenderContextCall9 call = reinterpret_cast<CuteQSGRenderContextCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderContext::flushGlyphCaches();
  }

  //  QSGDistanceFieldGlyphCache
  //      *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font,
  //      int renderTypeQuality)
  QSGDistanceFieldGlyphCache *distanceFieldGlyphCache(
      const QRawFont &font,
      int renderTypeQuality) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRenderContextCall10 call = reinterpret_cast<CuteQSGRenderContextCall10>(taken[10]);
      void * given = call(this, &font, renderTypeQuality, &handled);
      if (handled) return static_cast<QSGDistanceFieldGlyphCache *>(given);
    }
    return QSGRenderContext::distanceFieldGlyphCache(font, renderTypeQuality);
  }

  //  QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const QRawFont
  //      &font)
  QSGCurveGlyphAtlas *curveGlyphAtlas(const QRawFont &font) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGRenderContextCall11 call = reinterpret_cast<CuteQSGRenderContextCall11>(taken[11]);
      void * given = call(this, &font, &handled);
      if (handled) return static_cast<QSGCurveGlyphAtlas *>(given);
    }
    return QSGRenderContext::curveGlyphAtlas(font);
  }

  //  QSGTexture *QSGRenderContext::createTexture(const QImage &image, uint
  //      flags) const
  QSGTexture *createTexture(const QImage &image, uint flags) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGRenderContextCall12 call = reinterpret_cast<CuteQSGRenderContextCall12>(taken[12]);
      void * given = call(this, &image, flags, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }

  //  QSGRenderer
  //      *QSGRenderContext::createRenderer(QSGRendererInterface::RenderMod
  //      e renderMode)
  QSGRenderer *createRenderer(
      QSGRendererInterface::RenderMode renderMode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGRenderContextCall13 call = reinterpret_cast<CuteQSGRenderContextCall13>(taken[13]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGRenderer *>(given);
    }
    return {};
  }

  //  QSGTexture *QSGRenderContext::compressedTextureForFactory(const
  //      QSGCompressedTextureFactory *a0) const
  QSGTexture *compressedTextureForFactory(
      const QSGCompressedTextureFactory *a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGRenderContextCall14 call = reinterpret_cast<CuteQSGRenderContextCall14>(taken[14]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGRenderContext::compressedTextureForFactory(a0);
  }

  //  int QSGRenderContext::maxTextureSize() const
  int maxTextureSize() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGRenderContextCall15 call = reinterpret_cast<CuteQSGRenderContextCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhi *QSGRenderContext::rhi() const
  QRhi *rhi() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGRenderContextCall16 call = reinterpret_cast<CuteQSGRenderContextCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhi *>(given);
    }
    return QSGRenderContext::rhi();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGRenderContextCall17 call = reinterpret_cast<CuteQSGRenderContextCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGRenderContextCall18 call = reinterpret_cast<CuteQSGRenderContextCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGRenderContextCall19 call = reinterpret_cast<CuteQSGRenderContextCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGRenderContextCall20 call = reinterpret_cast<CuteQSGRenderContextCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGRenderContextCall21 call = reinterpret_cast<CuteQSGRenderContextCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGRenderContextCall22 call = reinterpret_cast<CuteQSGRenderContextCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGRenderContextCall23 call = reinterpret_cast<CuteQSGRenderContextCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRenderContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSGRenderContext10metaObjectEv(
    const QSGRenderContext *self) {
  return self->metaObject();
}

//  void *QSGRenderContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSGRenderContext11qt_metacastEPKc(
    QSGRenderContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRenderContext::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSGRenderContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRenderContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGRenderContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSGRenderContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGRenderContext::tr(s, c, n));
}

//  QSGRenderContext::QSGRenderContext(QSGContext *context)
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZN16QSGRenderContextC1EP10QSGContext(
    QSGContext *context) {
  return new CuteQSGRenderContext(context);
}

//  QSGRenderContext::~QSGRenderContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContextD1Ev(QSGRenderContext *self) {
  delete self;
}

//  QSGContext *QSGRenderContext::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK16QSGRenderContext17sceneGraphContextEv(
    const QSGRenderContext *self) {
  return self->sceneGraphContext();
}

//  bool QSGRenderContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGRenderContext7isValidEv(const QSGRenderContext *self) {
  return self->isValid();
}

//  void QSGRenderContext::initialize(const InitParams *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE(
    QSGRenderContext *self,
    const QSGRenderContext::InitParams *params) {
  self->initialize(params);
}

//  void QSGRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext10invalidateEv(QSGRenderContext *self) {
  self->invalidate();
}

//  void QSGRenderContext::prepareSync(qreal devicePixelRatio,
//      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration(
    QSGRenderContext *self,
    qreal devicePixelRatio,
    QRhiCommandBuffer *cb,
    const QQuickGraphicsConfiguration *config) {
  self->prepareSync(devicePixelRatio, cb, *config);
}

//  void QSGRenderContext::beginNextFrame(QSGRenderer *renderer, const
//      QSGRenderTarget &renderTarget, RenderPassCallback
//      mainPassRecordingStart, RenderPassCallback mainPassRecordingEnd, void
//      *callbackUserData)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext14beginNextFrameEP11QSGRendererRK15QSGRenderTargetPFvPvES7_S5_(
    QSGRenderContext *self,
    QSGRenderer *renderer,
    const QSGRenderTarget *renderTarget,
    void *mainPassRecordingStart,
    void *mainPassRecordingEnd,
    void *callbackUserData) {
  self->beginNextFrame(
      renderer,
      *renderTarget,
      reinterpret_cast<QSGRenderContext::RenderPassCallback>(mainPassRecordingStart),
      reinterpret_cast<QSGRenderContext::RenderPassCallback>(mainPassRecordingEnd),
      callbackUserData);
}

//  void QSGRenderContext::renderNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext15renderNextFrameEP11QSGRenderer(
    QSGRenderContext *self,
    QSGRenderer *renderer) {
  self->renderNextFrame(renderer);
}

//  void QSGRenderContext::endNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer(
    QSGRenderContext *self,
    QSGRenderer *renderer) {
  self->endNextFrame(renderer);
}

//  void QSGRenderContext::endSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext7endSyncEv(QSGRenderContext *self) {
  self->endSync();
}

//  void QSGRenderContext::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext10preprocessEv(QSGRenderContext *self) {
  self->preprocess();
}

//  void QSGRenderContext::invalidateGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext21invalidateGlyphCachesEv(
    QSGRenderContext *self) {
  self->invalidateGlyphCaches();
}

//  void QSGRenderContext::flushGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext16flushGlyphCachesEv(
    QSGRenderContext *self) {
  self->flushGlyphCaches();
}

//  QSGDistanceFieldGlyphCache
//      *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font, int
//      renderTypeQuality)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache *ritual_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti(
    QSGRenderContext *self,
    const QRawFont *font,
    int renderTypeQuality) {
  return self->distanceFieldGlyphCache(*font, renderTypeQuality);
}

//  QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const QRawFont
//      &font)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphAtlas *ritual_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont(
    QSGRenderContext *self,
    const QRawFont *font) {
  return self->curveGlyphAtlas(*font);
}

//  QSGTexture *QSGRenderContext::textureForFactory(QQuickTextureFactory
//      *factory, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QSGRenderContext17textureForFactoryEP20QQuickTextureFactoryP12QQuickWindow(
    QSGRenderContext *self,
    QQuickTextureFactory *factory,
    QQuickWindow *window) {
  return self->textureForFactory(factory, window);
}

//  QSGTexture *QSGRenderContext::createTexture(const QImage &image, uint
//      flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK16QSGRenderContext13createTextureERK6QImagej(
    const QSGRenderContext *self,
    const QImage *image,
    uint flags) {
  return self->createTexture(*image, flags);
}

//  QSGRenderer
//      *QSGRenderContext::createRenderer(QSGRendererInterface::RenderMode
//      renderMode)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_ZN16QSGRenderContext14createRendererEN20QSGRendererInterface10RenderModeE(
    QSGRenderContext *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createRenderer(renderMode);
}

//  QSGTexture *QSGRenderContext::compressedTextureForFactory(const
//      QSGCompressedTextureFactory *a0) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory(
    const QSGRenderContext *self,
    const QSGCompressedTextureFactory *a0) {
  return self->compressedTextureForFactory(a0);
}

//  int QSGRenderContext::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSGRenderContext14maxTextureSizeEv(
    const QSGRenderContext *self) {
  return self->maxTextureSize();
}

//  void QSGRenderContext::unregisterFontengineForCleanup(QFontEngine
//      *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext30unregisterFontengineForCleanupEP11QFontEngine(
    QSGRenderContext *self,
    QFontEngine *engine) {
  self->unregisterFontengineForCleanup(engine);
}

//  void QSGRenderContext::registerFontengineForCleanup(QFontEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext28registerFontengineForCleanupEP11QFontEngine(
    QSGRenderContext *self,
    QFontEngine *engine) {
  self->registerFontengineForCleanup(engine);
}

//  QRhi *QSGRenderContext::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK16QSGRenderContext3rhiEv(const QSGRenderContext *self) {
  return self->rhi();
}

//  void QSGRenderContext::initialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext11initializedEv(QSGRenderContext *self) {
  self->initialized();
}

//  void QSGRenderContext::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext11invalidatedEv(QSGRenderContext *self) {
  self->invalidated();
}

//  void QSGRenderContext::releaseCachedResourcesRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext31releaseCachedResourcesRequestedEv(
    QSGRenderContext *self) {
  self->releaseCachedResourcesRequested();
}

//  void QSGRenderContext::textureFactoryDestroyed(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRenderContext23textureFactoryDestroyedEP7QObject(
    QSGRenderContext *self,
    QObject *o) {
  self->textureFactoryDestroyed(o);
}

//  bool operator==(const QSGRenderContext::FontKey &f1, const
//      QSGRenderContext::FontKey &f2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN16QSGRenderContext7FontKeyES2_(
    const QSGRenderContext::FontKey *f1,
    const QSGRenderContext::FontKey *f2) {
  return operator==(*f1, *f2);
}

//  a Python function taken by a CuteQSGRenderContext, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRenderContext(
    QSGRenderContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRenderContext *>(self)->take(key, call);
}

//  bool QSGRenderContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QSGRenderContext7isValidEv(
    const QSGRenderContext *self) {
  return self->QSGRenderContext::isValid();
}

//  void QSGRenderContext::initialize(const InitParams *params)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext10initializeEPKNS_10InitParamsE(
    QSGRenderContext *self,
    const QSGRenderContext::InitParams *params) {
  self->QSGRenderContext::initialize(params);
}

//  void QSGRenderContext::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext10invalidateEv(QSGRenderContext *self) {
  self->QSGRenderContext::invalidate();
}

//  void QSGRenderContext::prepareSync(qreal devicePixelRatio,
//      QRhiCommandBuffer *cb, const QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext11prepareSyncEdP17QRhiCommandBufferRK27QQuickGraphicsConfiguration(
    QSGRenderContext *self,
    qreal devicePixelRatio,
    QRhiCommandBuffer *cb,
    const QQuickGraphicsConfiguration *config) {
  self->QSGRenderContext::prepareSync(devicePixelRatio, cb, *config);
}

//  void QSGRenderContext::endNextFrame(QSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext12endNextFrameEP11QSGRenderer(
    QSGRenderContext *self,
    QSGRenderer *renderer) {
  self->QSGRenderContext::endNextFrame(renderer);
}

//  void QSGRenderContext::endSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext7endSyncEv(QSGRenderContext *self) {
  self->QSGRenderContext::endSync();
}

//  void QSGRenderContext::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext10preprocessEv(QSGRenderContext *self) {
  self->QSGRenderContext::preprocess();
}

//  void QSGRenderContext::invalidateGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext21invalidateGlyphCachesEv(
    QSGRenderContext *self) {
  self->QSGRenderContext::invalidateGlyphCaches();
}

//  void QSGRenderContext::flushGlyphCaches()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGRenderContext16flushGlyphCachesEv(
    QSGRenderContext *self) {
  self->QSGRenderContext::flushGlyphCaches();
}

//  QSGDistanceFieldGlyphCache
//      *QSGRenderContext::distanceFieldGlyphCache(const QRawFont &font, int
//      renderTypeQuality)
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache *ritual_own_ZN16QSGRenderContext23distanceFieldGlyphCacheERK8QRawFonti(
    QSGRenderContext *self,
    const QRawFont *font,
    int renderTypeQuality) {
  return self->QSGRenderContext::distanceFieldGlyphCache(
      *font,
      renderTypeQuality);
}

//  QSGCurveGlyphAtlas *QSGRenderContext::curveGlyphAtlas(const QRawFont
//      &font)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphAtlas *ritual_own_ZN16QSGRenderContext15curveGlyphAtlasERK8QRawFont(
    QSGRenderContext *self,
    const QRawFont *font) {
  return self->QSGRenderContext::curveGlyphAtlas(*font);
}

//  QSGTexture *QSGRenderContext::compressedTextureForFactory(const
//      QSGCompressedTextureFactory *a0) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK16QSGRenderContext27compressedTextureForFactoryEPK27QSGCompressedTextureFactory(
    const QSGRenderContext *self,
    const QSGCompressedTextureFactory *a0) {
  return self->QSGRenderContext::compressedTextureForFactory(a0);
}

//  QRhi *QSGRenderContext::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_own_ZNK16QSGRenderContext3rhiEv(const QSGRenderContext *self) {
  return self->QSGRenderContext::rhi();
}
