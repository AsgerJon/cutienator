//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideotexture_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideotexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGVideoTexture that Python can take functions over in. Every QSGVideoTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQSGVideoTextureCall0)(const void *, int *);
typedef void * (*CuteQSGVideoTextureCall1)(const void *, int *);
typedef const QSize * (*CuteQSGVideoTextureCall2)(const void *, int *);
typedef bool (*CuteQSGVideoTextureCall3)(const void *, int *);
typedef bool (*CuteQSGVideoTextureCall4)(const void *, int *);
typedef const QRectF * (*CuteQSGVideoTextureCall5)(const void *, int *);
typedef bool (*CuteQSGVideoTextureCall6)(const void *, int *);
typedef void * (*CuteQSGVideoTextureCall7)(const void *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGVideoTextureCall8)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGVideoTextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGVideoTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGVideoTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGVideoTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGVideoTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGVideoTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGVideoTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGVideoTexture : public QSGVideoTexture {
public:
  using QSGVideoTexture::QSGVideoTexture;
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

  //  qint64 QSGVideoTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGVideoTextureCall0 call = reinterpret_cast<CuteQSGVideoTextureCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGVideoTexture::comparisonKey();
  }

  //  QRhiTexture *QSGVideoTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGVideoTextureCall1 call = reinterpret_cast<CuteQSGVideoTextureCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGVideoTexture::rhiTexture();
  }

  //  QSize QSGVideoTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGVideoTextureCall2 call = reinterpret_cast<CuteQSGVideoTextureCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGVideoTexture::textureSize();
  }

  //  bool QSGVideoTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGVideoTextureCall3 call = reinterpret_cast<CuteQSGVideoTextureCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGVideoTexture::hasAlphaChannel();
  }

  //  bool QSGVideoTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGVideoTextureCall4 call = reinterpret_cast<CuteQSGVideoTextureCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGVideoTexture::hasMipmaps();
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGVideoTextureCall5 call = reinterpret_cast<CuteQSGVideoTextureCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGVideoTextureCall6 call = reinterpret_cast<CuteQSGVideoTextureCall6>(taken[6]);
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
      CuteQSGVideoTextureCall7 call = reinterpret_cast<CuteQSGVideoTextureCall7>(taken[7]);
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
      CuteQSGVideoTextureCall8 call = reinterpret_cast<CuteQSGVideoTextureCall8>(taken[8]);
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
      CuteQSGVideoTextureCall9 call = reinterpret_cast<CuteQSGVideoTextureCall9>(taken[9]);
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
      CuteQSGVideoTextureCall10 call = reinterpret_cast<CuteQSGVideoTextureCall10>(taken[10]);
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
      CuteQSGVideoTextureCall11 call = reinterpret_cast<CuteQSGVideoTextureCall11>(taken[11]);
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
      CuteQSGVideoTextureCall12 call = reinterpret_cast<CuteQSGVideoTextureCall12>(taken[12]);
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
      CuteQSGVideoTextureCall13 call = reinterpret_cast<CuteQSGVideoTextureCall13>(taken[13]);
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
      CuteQSGVideoTextureCall14 call = reinterpret_cast<CuteQSGVideoTextureCall14>(taken[14]);
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
      CuteQSGVideoTextureCall15 call = reinterpret_cast<CuteQSGVideoTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGVideoTexturePrivate *QSGVideoTexture::d_func()
extern "C" Q_DECL_EXPORT
QSGVideoTexturePrivate *ritual_ZN15QSGVideoTexture6d_funcEv(
    QSGVideoTexture *self) {
  return self->d_func();
}

//  const QSGVideoTexturePrivate *QSGVideoTexture::d_func() const
extern "C" Q_DECL_EXPORT
const QSGVideoTexturePrivate *ritual_ZNK15QSGVideoTexture6d_funcEv(
    const QSGVideoTexture *self) {
  return self->d_func();
}

//  QSGVideoTexture::QSGVideoTexture()
extern "C" Q_DECL_EXPORT
QSGVideoTexture *ritual_ZN15QSGVideoTextureC1Ev() {
  return new CuteQSGVideoTexture();
}

//  QSGVideoTexture::~QSGVideoTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGVideoTextureD1Ev(QSGVideoTexture *self) {
  delete self;
}

//  qint64 QSGVideoTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QSGVideoTexture13comparisonKeyEv(
    const QSGVideoTexture *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGVideoTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK15QSGVideoTexture10rhiTextureEv(
    const QSGVideoTexture *self) {
  return self->rhiTexture();
}

//  QSize QSGVideoTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QSGVideoTexture11textureSizeEv(
    const QSGVideoTexture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGVideoTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSGVideoTexture15hasAlphaChannelEv(
    const QSGVideoTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGVideoTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSGVideoTexture10hasMipmapsEv(const QSGVideoTexture *self) {
  return self->hasMipmaps();
}

//  void QSGVideoTexture::setRhiTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGVideoTexture13setRhiTextureEP11QRhiTexture(
    QSGVideoTexture *self,
    QRhiTexture *texture) {
  self->setRhiTexture(texture);
}

//  void QSGVideoTexture::setData(QRhiTexture::Format f, const QSize &s,
//      const uchar *data, int bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGVideoTexture7setDataEN11QRhiTexture6FormatERK5QSizePKhi(
    QSGVideoTexture *self,
    QRhiTexture::Format f,
    const QSize *s,
    const uchar *data,
    int bytes) {
  self->setData(f, *s, data, bytes);
}

//  a Python function taken by a CuteQSGVideoTexture, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGVideoTexture(
    QSGVideoTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGVideoTexture *>(self)->take(key, call);
}

//  qint64 QSGVideoTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK15QSGVideoTexture13comparisonKeyEv(
    const QSGVideoTexture *self) {
  return self->QSGVideoTexture::comparisonKey();
}

//  QRhiTexture *QSGVideoTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK15QSGVideoTexture10rhiTextureEv(
    const QSGVideoTexture *self) {
  return self->QSGVideoTexture::rhiTexture();
}

//  QSize QSGVideoTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QSGVideoTexture11textureSizeEv(
    const QSGVideoTexture *self) {
  return new QSize(self->QSGVideoTexture::textureSize());
}

//  bool QSGVideoTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSGVideoTexture15hasAlphaChannelEv(
    const QSGVideoTexture *self) {
  return self->QSGVideoTexture::hasAlphaChannel();
}

//  bool QSGVideoTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSGVideoTexture10hasMipmapsEv(
    const QSGVideoTexture *self) {
  return self->QSGVideoTexture::hasMipmaps();
}
