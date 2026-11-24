//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRhiAtlasTexture::TextureBase that Python can take functions over in. Every QSGRhiAtlasTexture::TextureBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSGRhiAtlasTexture_TextureBaseCall0)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureBaseCall1)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall2)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall3)(const void *, int *);
typedef const QSize * (*CuteQSGRhiAtlasTexture_TextureBaseCall4)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall5)(const void *, int *);
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall6)(const void *, int *);
typedef const QRectF * (*CuteQSGRhiAtlasTexture_TextureBaseCall7)(const void *, int *);
typedef void * (*CuteQSGRhiAtlasTexture_TextureBaseCall8)(const void *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_TextureBaseCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_TextureBaseCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_TextureBase : public QSGRhiAtlasTexture::TextureBase {
public:
  using QSGRhiAtlasTexture::TextureBase::TextureBase;
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
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
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

  //  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::comparisonKey();
  }

  //  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall2>(taken[2]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(rhi, resourceUpdates);
  }

  //  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
  }

  //  QSize QSGTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall8>(taken[8]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGTexture::removedFromAtlas(resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_TextureBaseCall9 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall9>(taken[9]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall10 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall10>(taken[10]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall11 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall11>(taken[11]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall12 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall12>(taken[12]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall13 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall13>(taken[13]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall14 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall14>(taken[14]);
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
      CuteQSGRhiAtlasTexture_TextureBaseCall15 call = reinterpret_cast<CuteQSGRhiAtlasTexture_TextureBaseCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiAtlasTexture::TextureBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGRhiAtlasTexture11TextureBase10metaObjectEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->metaObject();
}

//  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->isAtlasTexture();
}

//  QRect QSGRhiAtlasTexture::TextureBase::atlasSubRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QSGRhiAtlasTexture11TextureBase12atlasSubRectEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return new QRect(self->atlasSubRect());
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_TextureBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_TextureBase(
    QSGRhiAtlasTexture::TextureBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_TextureBase *>(self)->take(key, call);
}

//  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureEv(
    const QSGRhiAtlasTexture::TextureBase *self) {
  return self->QSGRhiAtlasTexture::TextureBase::isAtlasTexture();
}
