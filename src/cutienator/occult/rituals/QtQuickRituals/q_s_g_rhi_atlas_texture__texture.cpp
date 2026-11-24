//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRhiAtlasTexture::Texture that Python can take functions over in. Every QSGRhiAtlasTexture::Texture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSGRhiAtlasTexture_TextureCall0)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall1)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall2)(const void *, int *);
typedef const QRectF * (*CuteQSGRhiAtlasTexture_TextureCall3)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureCall4)(const void *, QRhiResourceUpdateBatch *, int *);
typedef qint64 (*CuteQSGRhiAtlasTexture_TextureCall5)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureCall6)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_TextureCall7)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_Texture : public QSGRhiAtlasTexture::Texture {
public:
  using QSGRhiAtlasTexture::Texture::Texture;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
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

  //  QSize QSGRhiAtlasTexture::Texture::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiAtlasTexture::Texture::textureSize();
  }

  //  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Texture::hasAlphaChannel();
  }

  //  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Texture::hasMipmaps();
  }

  //  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiAtlasTexture::Texture::normalizedTextureSubRect();
  }

  //  QSGTexture *QSGRhiAtlasTexture::Texture::removedFromAtlas(QRhiResourc
  //      eUpdateBatch *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall4>(taken[4]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGRhiAtlasTexture::Texture::removedFromAtlas(resourceUpdates);
  }

  //  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::comparisonKey();
  }

  //  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGRhiAtlasTexture::TextureBase::rhiTexture();
  }

  //  void QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi
  //      *rhi, QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall7>(taken[7]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(rhi, resourceUpdates);
  }

  //  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureCall9 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall9>(taken[9]);
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
      CuteQSGRhiAtlasTexture_TextureCall10 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall10>(taken[10]);
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
      CuteQSGRhiAtlasTexture_TextureCall11 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall11>(taken[11]);
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
      CuteQSGRhiAtlasTexture_TextureCall12 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall12>(taken[12]);
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
      CuteQSGRhiAtlasTexture_TextureCall13 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall13>(taken[13]);
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
      CuteQSGRhiAtlasTexture_TextureCall14 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall14>(taken[14]);
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
      CuteQSGRhiAtlasTexture_TextureCall15 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::Texture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture7Texture10metaObjectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->metaObject();
}

//  QSize QSGRhiAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QSize(self->textureSize());
}

//  void QSGRhiAtlasTexture::Texture::setHasAlphaChannel(bool alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7Texture18setHasAlphaChannelEb(
    QSGRhiAtlasTexture::Texture *self,
    bool alpha) {
  self->setHasAlphaChannel(alpha);
}

//  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->hasMipmaps();
}

//  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRectF(self->normalizedTextureSubRect());
}

//  QRect QSGRhiAtlasTexture::Texture::atlasSubRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture7Texture12atlasSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRect(self->atlasSubRect());
}

//  QRect QSGRhiAtlasTexture::Texture::atlasSubRectWithoutPadding() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture7Texture26atlasSubRectWithoutPaddingEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRect(self->atlasSubRectWithoutPadding());
}

//  void QSGRhiAtlasTexture::Texture::releaseImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGRhiAtlasTexture7Texture12releaseImageEv(
    QSGRhiAtlasTexture::Texture *self) {
  self->releaseImage();
}

//  const QImage &QSGRhiAtlasTexture::Texture::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK18QSGRhiAtlasTexture7Texture5imageEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QImage(self->image());
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_Texture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_Texture(
    QSGRhiAtlasTexture::Texture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_Texture *>(self)->take(key, call);
}

//  QSize QSGRhiAtlasTexture::Texture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QSGRhiAtlasTexture7Texture11textureSizeEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QSize(self->QSGRhiAtlasTexture::Texture::textureSize());
}

//  bool QSGRhiAtlasTexture::Texture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture7Texture15hasAlphaChannelEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->QSGRhiAtlasTexture::Texture::hasAlphaChannel();
}

//  bool QSGRhiAtlasTexture::Texture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture7Texture10hasMipmapsEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return self->QSGRhiAtlasTexture::Texture::hasMipmaps();
}

//  QRectF QSGRhiAtlasTexture::Texture::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK18QSGRhiAtlasTexture7Texture24normalizedTextureSubRectEv(
    const QSGRhiAtlasTexture::Texture *self) {
  return new QRectF(
      self->QSGRhiAtlasTexture::Texture::normalizedTextureSubRect());
}
