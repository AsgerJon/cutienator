//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgplaintexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgplaintexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGPlainTexture that Python can take functions over in. Every QSGPlainTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSGPlainTextureCall0)(const void *, int *);
typedef bool (*CuteQSGPlainTextureCall1)(const void *, int *);
typedef bool (*CuteQSGPlainTextureCall2)(const void *, int *);
typedef qint64 (*CuteQSGPlainTextureCall3)(const void *, int *);
typedef void * (*CuteQSGPlainTextureCall4)(const void *, int *);
typedef void (*CuteQSGPlainTextureCall5)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef const QRectF * (*CuteQSGPlainTextureCall6)(const void *, int *);
typedef bool (*CuteQSGPlainTextureCall7)(const void *, int *);
typedef void * (*CuteQSGPlainTextureCall8)(const void *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGPlainTextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGPlainTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGPlainTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGPlainTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGPlainTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGPlainTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGPlainTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGPlainTexture : public QSGPlainTexture {
public:
  using QSGPlainTexture::QSGPlainTexture;
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
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
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

  //  QSize QSGPlainTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGPlainTextureCall0 call = reinterpret_cast<CuteQSGPlainTextureCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGPlainTexture::textureSize();
  }

  //  bool QSGPlainTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGPlainTextureCall1 call = reinterpret_cast<CuteQSGPlainTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGPlainTexture::hasAlphaChannel();
  }

  //  bool QSGPlainTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGPlainTextureCall2 call = reinterpret_cast<CuteQSGPlainTextureCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGPlainTexture::hasMipmaps();
  }

  //  qint64 QSGPlainTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGPlainTextureCall3 call = reinterpret_cast<CuteQSGPlainTextureCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGPlainTexture::comparisonKey();
  }

  //  QRhiTexture *QSGPlainTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGPlainTextureCall4 call = reinterpret_cast<CuteQSGPlainTextureCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGPlainTexture::rhiTexture();
  }

  //  void QSGPlainTexture::commitTextureOperations(QRhi *rhi,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGPlainTextureCall5 call = reinterpret_cast<CuteQSGPlainTextureCall5>(taken[5]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGPlainTexture::commitTextureOperations(rhi, resourceUpdates);
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGPlainTextureCall6 call = reinterpret_cast<CuteQSGPlainTextureCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGPlainTextureCall7 call = reinterpret_cast<CuteQSGPlainTextureCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexture::isAtlasTexture();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGPlainTextureCall8 call = reinterpret_cast<CuteQSGPlainTextureCall8>(taken[8]);
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
      CuteQSGPlainTextureCall9 call = reinterpret_cast<CuteQSGPlainTextureCall9>(taken[9]);
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
      CuteQSGPlainTextureCall10 call = reinterpret_cast<CuteQSGPlainTextureCall10>(taken[10]);
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
      CuteQSGPlainTextureCall11 call = reinterpret_cast<CuteQSGPlainTextureCall11>(taken[11]);
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
      CuteQSGPlainTextureCall12 call = reinterpret_cast<CuteQSGPlainTextureCall12>(taken[12]);
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
      CuteQSGPlainTextureCall13 call = reinterpret_cast<CuteQSGPlainTextureCall13>(taken[13]);
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
      CuteQSGPlainTextureCall14 call = reinterpret_cast<CuteQSGPlainTextureCall14>(taken[14]);
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
      CuteQSGPlainTextureCall15 call = reinterpret_cast<CuteQSGPlainTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGPlainTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSGPlainTexture10metaObjectEv(
    const QSGPlainTexture *self) {
  return self->metaObject();
}

//  QString QSGPlainTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSGPlainTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGPlainTexture::tr(s, c, n));
}

//  QSGPlainTexturePrivate *QSGPlainTexture::d_func()
extern "C" Q_DECL_EXPORT
QSGPlainTexturePrivate *ritual_ZN15QSGPlainTexture6d_funcEv(
    QSGPlainTexture *self) {
  return self->d_func();
}

//  const QSGPlainTexturePrivate *QSGPlainTexture::d_func() const
extern "C" Q_DECL_EXPORT
const QSGPlainTexturePrivate *ritual_ZNK15QSGPlainTexture6d_funcEv(
    const QSGPlainTexture *self) {
  return self->d_func();
}

//  QSGPlainTexture::QSGPlainTexture()
extern "C" Q_DECL_EXPORT
QSGPlainTexture *ritual_ZN15QSGPlainTextureC1Ev() {
  return new CuteQSGPlainTexture();
}

//  QSGPlainTexture::~QSGPlainTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTextureD1Ev(QSGPlainTexture *self) {
  delete self;
}

//  void QSGPlainTexture::setOwnsTexture(bool owns)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture14setOwnsTextureEb(
    QSGPlainTexture *self,
    bool owns) {
  self->setOwnsTexture(owns);
}

//  bool QSGPlainTexture::ownsTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSGPlainTexture11ownsTextureEv(
    const QSGPlainTexture *self) {
  return self->ownsTexture();
}

//  void QSGPlainTexture::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture14setTextureSizeERK5QSize(
    QSGPlainTexture *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  QSize QSGPlainTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QSGPlainTexture11textureSizeEv(
    const QSGPlainTexture *self) {
  return new QSize(self->textureSize());
}

//  void QSGPlainTexture::setHasAlphaChannel(bool alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture18setHasAlphaChannelEb(
    QSGPlainTexture *self,
    bool alpha) {
  self->setHasAlphaChannel(alpha);
}

//  bool QSGPlainTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSGPlainTexture15hasAlphaChannelEv(
    const QSGPlainTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGPlainTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSGPlainTexture10hasMipmapsEv(const QSGPlainTexture *self) {
  return self->hasMipmaps();
}

//  void QSGPlainTexture::setImage(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture8setImageERK6QImage(
    QSGPlainTexture *self,
    const QImage *image) {
  self->setImage(*image);
}

//  const QImage &QSGPlainTexture::image()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN15QSGPlainTexture5imageEv(QSGPlainTexture *self) {
  return new QImage(self->image());
}

//  qint64 QSGPlainTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QSGPlainTexture13comparisonKeyEv(
    const QSGPlainTexture *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGPlainTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK15QSGPlainTexture10rhiTextureEv(
    const QSGPlainTexture *self) {
  return self->rhiTexture();
}

//  void QSGPlainTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGPlainTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  void QSGPlainTexture::setTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture10setTextureEP11QRhiTexture(
    QSGPlainTexture *self,
    QRhiTexture *texture) {
  self->setTexture(texture);
}

//  void QSGPlainTexture::setTextureFromNativeTexture(QRhi *rhi, quint64
//      nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat, const
//      QSize &size, QQuickWindow::CreateTextureOptions options,
//      QQuickWindowPrivate::TextureFromNativeTextureFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGPlainTexture27setTextureFromNativeTextureEP4QRhiyijRK5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES5_IN19QQuickWindowPrivate28TextureFromNativeTextureFlagEE(
    QSGPlainTexture *self,
    QRhi *rhi,
    quint64 nativeObjectHandle,
    int nativeLayoutOrState,
    uint nativeFormat,
    const QSize *size,
    int options,
    int flags) {
  self->setTextureFromNativeTexture(
      rhi,
      nativeObjectHandle,
      nativeLayoutOrState,
      nativeFormat,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options),
      QFlags<QQuickWindowPrivate::TextureFromNativeTextureFlag>::fromInt(flags));
}

//  QSGPlainTexture *QSGPlainTexture::fromImage(const QImage &image)
extern "C" Q_DECL_EXPORT
QSGPlainTexture *ritual_ZN15QSGPlainTexture9fromImageERK6QImage(
    const QImage *image) {
  return QSGPlainTexture::fromImage(*image);
}

//  a Python function taken by a CuteQSGPlainTexture, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGPlainTexture(
    QSGPlainTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGPlainTexture *>(self)->take(key, call);
}

//  QSize QSGPlainTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QSGPlainTexture11textureSizeEv(
    const QSGPlainTexture *self) {
  return new QSize(self->QSGPlainTexture::textureSize());
}

//  bool QSGPlainTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSGPlainTexture15hasAlphaChannelEv(
    const QSGPlainTexture *self) {
  return self->QSGPlainTexture::hasAlphaChannel();
}

//  bool QSGPlainTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSGPlainTexture10hasMipmapsEv(
    const QSGPlainTexture *self) {
  return self->QSGPlainTexture::hasMipmaps();
}

//  qint64 QSGPlainTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK15QSGPlainTexture13comparisonKeyEv(
    const QSGPlainTexture *self) {
  return self->QSGPlainTexture::comparisonKey();
}

//  QRhiTexture *QSGPlainTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK15QSGPlainTexture10rhiTextureEv(
    const QSGPlainTexture *self) {
  return self->QSGPlainTexture::rhiTexture();
}

//  void QSGPlainTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSGPlainTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGPlainTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGPlainTexture::commitTextureOperations(rhi, resourceUpdates);
}
