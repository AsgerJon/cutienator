//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qrhiwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qrhiwidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qrhiwidget_p.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>

//  A QRhiWidgetPrivate that Python can take functions over in. Every QRhiWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QWidgetPrivate::TextureData * (*CuteQRhiWidgetPrivateCall0)(const void *, int *);
typedef int (*CuteQRhiWidgetPrivateCall1)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQRhiWidgetPrivateCall2)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall3)(const void *, int *);
typedef const QImage * (*CuteQRhiWidgetPrivateCall4)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall5)(const void *, bool, int *);
typedef void (*CuteQRhiWidgetPrivateCall6)(const void *, int, int *);
typedef void (*CuteQRhiWidgetPrivateCall7)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall8)(const void *, int *);
typedef void * (*CuteQRhiWidgetPrivateCall9)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall10)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall11)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall12)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall13)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall14)(const void *, int *);
typedef void (*CuteQRhiWidgetPrivateCall15)(const void *, int *);
typedef bool (*CuteQRhiWidgetPrivateCall16)(const void *, int *);
typedef bool (*CuteQRhiWidgetPrivateCall17)(const void *, int *);
class CuteQRhiWidgetPrivate : public QRhiWidgetPrivate {
public:
  using QRhiWidgetPrivate::QRhiWidgetPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  TextureData QRhiWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall0 call = reinterpret_cast<CuteQRhiWidgetPrivateCall0>(taken[0]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QRhiWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall1 call = reinterpret_cast<CuteQRhiWidgetPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QRhiWidgetPrivate::textureListFlags();
  }

  //  QPlatformBackingStoreRhiConfig QRhiWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall2 call = reinterpret_cast<CuteQRhiWidgetPrivateCall2>(taken[2]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiWidgetPrivate::rhiConfig();
  }

  //  void QRhiWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall3 call = reinterpret_cast<CuteQRhiWidgetPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiWidgetPrivate::endCompose();
  }

  //  QImage QRhiWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall4 call = reinterpret_cast<CuteQRhiWidgetPrivateCall4>(taken[4]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall5 call = reinterpret_cast<CuteQRhiWidgetPrivateCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall6 call = reinterpret_cast<CuteQRhiWidgetPrivateCall6>(taken[6]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[7]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall7 call = reinterpret_cast<CuteQRhiWidgetPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall8 call = reinterpret_cast<CuteQRhiWidgetPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall9 call = reinterpret_cast<CuteQRhiWidgetPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall10 call = reinterpret_cast<CuteQRhiWidgetPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall11 call = reinterpret_cast<CuteQRhiWidgetPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall12 call = reinterpret_cast<CuteQRhiWidgetPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall13 call = reinterpret_cast<CuteQRhiWidgetPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall14 call = reinterpret_cast<CuteQRhiWidgetPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall15 call = reinterpret_cast<CuteQRhiWidgetPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall16 call = reinterpret_cast<CuteQRhiWidgetPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQRhiWidgetPrivateCall17 call = reinterpret_cast<CuteQRhiWidgetPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QRhiWidget *QRhiWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRhiWidget *ritual_ZN17QRhiWidgetPrivate6q_funcEv(QRhiWidgetPrivate *self) {
  return self->q_func();
}

//  const QRhiWidget *QRhiWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRhiWidget *ritual_ZNK17QRhiWidgetPrivate6q_funcEv(
    const QRhiWidgetPrivate *self) {
  return self->q_func();
}

//  TextureData QRhiWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_ZNK17QRhiWidgetPrivate7textureEv(
    const QRhiWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(self->texture());
}

//  QPlatformTextureList::Flags QRhiWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN17QRhiWidgetPrivate16textureListFlagsEv(
    QRhiWidgetPrivate *self) {
  return static_cast<int>(self->textureListFlags().toInt());
}

//  QPlatformBackingStoreRhiConfig QRhiWidgetPrivate::rhiConfig() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_ZNK17QRhiWidgetPrivate9rhiConfigEv(
    const QRhiWidgetPrivate *self) {
  return new QPlatformBackingStoreRhiConfig(self->rhiConfig());
}

//  void QRhiWidgetPrivate::endCompose()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate10endComposeEv(QRhiWidgetPrivate *self) {
  self->endCompose();
}

//  QImage QRhiWidgetPrivate::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN17QRhiWidgetPrivate15grabFramebufferEv(
    QRhiWidgetPrivate *self) {
  return new QImage(self->grabFramebuffer());
}

//  void QRhiWidgetPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate4initEv(QRhiWidgetPrivate *self) {
  self->init();
}

//  void QRhiWidgetPrivate::ensureRhi()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate9ensureRhiEv(QRhiWidgetPrivate *self) {
  self->ensureRhi();
}

//  void QRhiWidgetPrivate::ensureTexture(bool *changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate13ensureTextureEPb(
    QRhiWidgetPrivate *self,
    bool *changed) {
  self->ensureTexture(changed);
}

//  bool QRhiWidgetPrivate::invokeInitialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QRhiWidgetPrivate16invokeInitializeEP17QRhiCommandBuffer(
    QRhiWidgetPrivate *self,
    QRhiCommandBuffer *cb) {
  return self->invokeInitialize(cb);
}

//  void QRhiWidgetPrivate::resetColorBufferObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate23resetColorBufferObjectsEv(
    QRhiWidgetPrivate *self) {
  self->resetColorBufferObjects();
}

//  void QRhiWidgetPrivate::resetRenderTargetObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate24resetRenderTargetObjectsEv(
    QRhiWidgetPrivate *self) {
  self->resetRenderTargetObjects();
}

//  void QRhiWidgetPrivate::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRhiWidgetPrivate16releaseResourcesEv(
    QRhiWidgetPrivate *self) {
  self->releaseResources();
}

//  a Python function taken by a CuteQRhiWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiWidgetPrivate(
    QRhiWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiWidgetPrivate *>(self)->take(key, call);
}

//  TextureData QRhiWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_own_ZNK17QRhiWidgetPrivate7textureEv(
    const QRhiWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(self->QRhiWidgetPrivate::texture());
}

//  QPlatformTextureList::Flags QRhiWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QRhiWidgetPrivate16textureListFlagsEv(
    QRhiWidgetPrivate *self) {
  return static_cast<int>(
      self->QRhiWidgetPrivate::textureListFlags().toInt());
}

//  QPlatformBackingStoreRhiConfig QRhiWidgetPrivate::rhiConfig() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_own_ZNK17QRhiWidgetPrivate9rhiConfigEv(
    const QRhiWidgetPrivate *self) {
  return new QPlatformBackingStoreRhiConfig(
      self->QRhiWidgetPrivate::rhiConfig());
}

//  void QRhiWidgetPrivate::endCompose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QRhiWidgetPrivate10endComposeEv(
    QRhiWidgetPrivate *self) {
  self->QRhiWidgetPrivate::endCompose();
}

//  QImage QRhiWidgetPrivate::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN17QRhiWidgetPrivate15grabFramebufferEv(
    QRhiWidgetPrivate *self) {
  return new QImage(self->QRhiWidgetPrivate::grabFramebuffer());
}
