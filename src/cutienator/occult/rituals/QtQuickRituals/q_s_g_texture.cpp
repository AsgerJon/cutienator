//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQuick/qsgtexture_platform.h>

//  A QSGTexture that Python can take functions over in. Every QSGTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSGTextureCall0)(const void *, int *);
typedef void * (*CuteQSGTextureCall1)(const void *, int *);
typedef const QSize * (*CuteQSGTextureCall2)(const void *, int *);
typedef bool (*CuteQSGTextureCall3)(const void *, int *);
typedef bool (*CuteQSGTextureCall4)(const void *, int *);
typedef const QRectF * (*CuteQSGTextureCall5)(const void *, int *);
typedef bool (*CuteQSGTextureCall6)(const void *, int *);
typedef void * (*CuteQSGTextureCall7)(const void *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGTextureCall8)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGTextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGTexture : public QSGTexture {
public:
  using QSGTexture::QSGTexture;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  qint64 QSGTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTextureCall0 call = reinterpret_cast<CuteQSGTextureCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhiTexture *QSGTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTextureCall1 call = reinterpret_cast<CuteQSGTextureCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGTexture::rhiTexture();
  }

  //  QSize QSGTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGTextureCall2 call = reinterpret_cast<CuteQSGTextureCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGTextureCall3 call = reinterpret_cast<CuteQSGTextureCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGTextureCall4 call = reinterpret_cast<CuteQSGTextureCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGTextureCall5 call = reinterpret_cast<CuteQSGTextureCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGTextureCall6 call = reinterpret_cast<CuteQSGTextureCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexture::isAtlasTexture();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGTextureCall7 call = reinterpret_cast<CuteQSGTextureCall7>(taken[7]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGTexture::removedFromAtlas(resourceUpdates);
  }

  //  void QSGTexture::commitTextureOperations(QRhi *rhi,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGTextureCall8 call = reinterpret_cast<CuteQSGTextureCall8>(taken[8]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGTexture::commitTextureOperations(rhi, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGTextureCall9 call = reinterpret_cast<CuteQSGTextureCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGTextureCall10 call = reinterpret_cast<CuteQSGTextureCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGTextureCall11 call = reinterpret_cast<CuteQSGTextureCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGTextureCall12 call = reinterpret_cast<CuteQSGTextureCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGTextureCall13 call = reinterpret_cast<CuteQSGTextureCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGTextureCall14 call = reinterpret_cast<CuteQSGTextureCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGTextureCall15 call = reinterpret_cast<CuteQSGTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSGTexture10metaObjectEv(
    const QSGTexture *self) {
  return self->metaObject();
}

//  void *QSGTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QSGTexture11qt_metacastEPKc(
    QSGTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGTexture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSGTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSGTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGTexture::tr(s, c, n));
}

//  QSGTexturePrivate *QSGTexture::d_func()
extern "C" Q_DECL_EXPORT
QSGTexturePrivate *ritual_ZN10QSGTexture6d_funcEv(QSGTexture *self) {
  return self->d_func();
}

//  const QSGTexturePrivate *QSGTexture::d_func() const
extern "C" Q_DECL_EXPORT
const QSGTexturePrivate *ritual_ZNK10QSGTexture6d_funcEv(
    const QSGTexture *self) {
  return self->d_func();
}

//  QSGTexture::QSGTexture()
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN10QSGTextureC1Ev() {
  return new CuteQSGTexture();
}

//  QSGTexture::~QSGTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTextureD1Ev(QSGTexture *self) {
  delete self;
}

//  qint64 QSGTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QSGTexture13comparisonKeyEv(const QSGTexture *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK10QSGTexture10rhiTextureEv(const QSGTexture *self) {
  return self->rhiTexture();
}

//  QSize QSGTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QSGTexture11textureSizeEv(const QSGTexture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSGTexture15hasAlphaChannelEv(const QSGTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSGTexture10hasMipmapsEv(const QSGTexture *self) {
  return self->hasMipmaps();
}

//  QRectF QSGTexture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QSGTexture24normalizedTextureSubRectEv(
    const QSGTexture *self) {
  return new QRectF(self->normalizedTextureSubRect());
}

//  bool QSGTexture::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSGTexture14isAtlasTextureEv(const QSGTexture *self) {
  return self->isAtlasTexture();
}

//  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
//      *resourceUpdates) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGTexture *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  return self->removedFromAtlas(resourceUpdates);
}

//  void QSGTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  void QSGTexture::setMipmapFiltering(Filtering filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture18setMipmapFilteringENS_9FilteringE(
    QSGTexture *self,
    QSGTexture::Filtering filter) {
  self->setMipmapFiltering(filter);
}

//  QSGTexture::Filtering QSGTexture::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK10QSGTexture15mipmapFilteringEv(
    const QSGTexture *self) {
  return self->mipmapFiltering();
}

//  void QSGTexture::setFiltering(Filtering filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture12setFilteringENS_9FilteringE(
    QSGTexture *self,
    QSGTexture::Filtering filter) {
  self->setFiltering(filter);
}

//  QSGTexture::Filtering QSGTexture::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK10QSGTexture9filteringEv(
    const QSGTexture *self) {
  return self->filtering();
}

//  void QSGTexture::setAnisotropyLevel(AnisotropyLevel level)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture18setAnisotropyLevelENS_15AnisotropyLevelE(
    QSGTexture *self,
    QSGTexture::AnisotropyLevel level) {
  self->setAnisotropyLevel(level);
}

//  QSGTexture::AnisotropyLevel QSGTexture::anisotropyLevel() const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_ZNK10QSGTexture15anisotropyLevelEv(
    const QSGTexture *self) {
  return self->anisotropyLevel();
}

//  void QSGTexture::setHorizontalWrapMode(WrapMode hwrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture21setHorizontalWrapModeENS_8WrapModeE(
    QSGTexture *self,
    QSGTexture::WrapMode hwrap) {
  self->setHorizontalWrapMode(hwrap);
}

//  QSGTexture::WrapMode QSGTexture::horizontalWrapMode() const
extern "C" Q_DECL_EXPORT
QSGTexture::WrapMode ritual_ZNK10QSGTexture18horizontalWrapModeEv(
    const QSGTexture *self) {
  return self->horizontalWrapMode();
}

//  void QSGTexture::setVerticalWrapMode(WrapMode vwrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGTexture19setVerticalWrapModeENS_8WrapModeE(
    QSGTexture *self,
    QSGTexture::WrapMode vwrap) {
  self->setVerticalWrapMode(vwrap);
}

//  QSGTexture::WrapMode QSGTexture::verticalWrapMode() const
extern "C" Q_DECL_EXPORT
QSGTexture::WrapMode ritual_ZNK10QSGTexture16verticalWrapModeEv(
    const QSGTexture *self) {
  return self->verticalWrapMode();
}

//  QRectF QSGTexture::convertToNormalizedSourceRect(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QSGTexture29convertToNormalizedSourceRectERK6QRectF(
    const QSGTexture *self,
    const QRectF *rect) {
  return new QRectF(self->convertToNormalizedSourceRect(*rect));
}

//  void *QSGTexture::resolveInterface(const char *name, int revision) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK10QSGTexture16resolveInterfaceEPKci(
    const QSGTexture *self,
    const char *name,
    int revision) {
  return self->resolveInterface(name, revision);
}

//  QSGTexture::QSGTexture(QSGTexturePrivate &dd)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN10QSGTextureC1ER17QSGTexturePrivate(
    QSGTexturePrivate *dd) {
  return new CuteQSGTexture(*dd);
}

//  a Python function taken by a CuteQSGTexture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTexture(QSGTexture *self, const char *key, void *call) {
  return static_cast<CuteQSGTexture *>(self)->take(key, call);
}

//  QRhiTexture *QSGTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK10QSGTexture10rhiTextureEv(
    const QSGTexture *self) {
  return self->QSGTexture::rhiTexture();
}

//  QRectF QSGTexture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK10QSGTexture24normalizedTextureSubRectEv(
    const QSGTexture *self) {
  return new QRectF(self->QSGTexture::normalizedTextureSubRect());
}

//  bool QSGTexture::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QSGTexture14isAtlasTextureEv(const QSGTexture *self) {
  return self->QSGTexture::isAtlasTexture();
}

//  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
//      *resourceUpdates) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch(
    const QSGTexture *self,
    QRhiResourceUpdateBatch *resourceUpdates) {
  return self->QSGTexture::removedFromAtlas(resourceUpdates);
}

//  void QSGTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGTexture::commitTextureOperations(rhi, resourceUpdates);
}

#if QT_CONFIG(opengl)
//  QNativeInterface::QSGOpenGLTexture *QSGTexture::nativeInterface<
//      QNativeInterface::QSGOpenGLTexture>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGOpenGLTexture * ritual_ZNK10QSGTexture15nativeInterfaceIN16QNativeInterface16QSGOpenGLTextureENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(const QSGTexture *self) {
  return self->nativeInterface<QNativeInterface::QSGOpenGLTexture>();
}
#endif  // QT_CONFIG(opengl)

#if QT_CONFIG(vulkan)
//  QNativeInterface::QSGVulkanTexture *QSGTexture::nativeInterface<
//      QNativeInterface::QSGVulkanTexture>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGVulkanTexture * ritual_ZNK10QSGTexture15nativeInterfaceIN16QNativeInterface16QSGVulkanTextureENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(const QSGTexture *self) {
  return self->nativeInterface<QNativeInterface::QSGVulkanTexture>();
}
#endif  // QT_CONFIG(vulkan)

#if defined(Q_OS_WIN)
//  QNativeInterface::QSGD3D11Texture *QSGTexture::nativeInterface<
//      QNativeInterface::QSGD3D11Texture>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGD3D11Texture * ritual_ZNK10QSGTexture15nativeInterfaceIN16QNativeInterface15QSGD3D11TextureENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(const QSGTexture *self) {
  return self->nativeInterface<QNativeInterface::QSGD3D11Texture>();
}
#endif  // defined(Q_OS_WIN)

#if defined(Q_OS_WIN)
//  QNativeInterface::QSGD3D12Texture *QSGTexture::nativeInterface<
//      QNativeInterface::QSGD3D12Texture>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGD3D12Texture * ritual_ZNK10QSGTexture15nativeInterfaceIN16QNativeInterface15QSGD3D12TextureENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(const QSGTexture *self) {
  return self->nativeInterface<QNativeInterface::QSGD3D12Texture>();
}
#endif  // defined(Q_OS_WIN)

#if QT_CONFIG(metal)
//  QNativeInterface::QSGMetalTexture *QSGTexture::nativeInterface<
//      QNativeInterface::QSGMetalTexture>() const
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGMetalTexture * ritual_ZNK10QSGTexture15nativeInterfaceIN16QNativeInterface15QSGMetalTextureENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(const QSGTexture *self) {
  return self->nativeInterface<QNativeInterface::QSGMetalTexture>();
}
#endif  // QT_CONFIG(metal)
