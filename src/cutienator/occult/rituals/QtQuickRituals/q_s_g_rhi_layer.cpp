//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhilayer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhilayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRhiLayer that Python can take functions over in. Every QSGRhiLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRhiLayerCall0)(const void *, int *);
typedef bool (*CuteQSGRhiLayerCall1)(const void *, int *);
typedef bool (*CuteQSGRhiLayerCall2)(const void *, int *);
typedef const QSize * (*CuteQSGRhiLayerCall3)(const void *, int *);
typedef qint64 (*CuteQSGRhiLayerCall4)(const void *, int *);
typedef void * (*CuteQSGRhiLayerCall5)(const void *, int *);
typedef void (*CuteQSGRhiLayerCall6)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGRhiLayerCall7)(const void *, QSGNode *, int *);
typedef void (*CuteQSGRhiLayerCall8)(const void *, const QRectF *, int *);
typedef void (*CuteQSGRhiLayerCall9)(const void *, const QSize *, int *);
typedef void (*CuteQSGRhiLayerCall10)(const void *, bool, int *);
typedef void (*CuteQSGRhiLayerCall11)(const void *, int, int *);
typedef void (*CuteQSGRhiLayerCall12)(const void *, bool, int *);
typedef void (*CuteQSGRhiLayerCall13)(const void *, bool, int *);
typedef void (*CuteQSGRhiLayerCall14)(const void *, qreal, int *);
typedef void (*CuteQSGRhiLayerCall15)(const void *, bool, int *);
typedef void (*CuteQSGRhiLayerCall16)(const void *, bool, int *);
typedef const QRectF * (*CuteQSGRhiLayerCall17)(const void *, int *);
typedef void (*CuteQSGRhiLayerCall18)(const void *, int, int *);
typedef void (*CuteQSGRhiLayerCall19)(const void *, int *);
typedef const QImage * (*CuteQSGRhiLayerCall20)(const void *, int *);
typedef void (*CuteQSGRhiLayerCall21)(const void *, int *);
typedef void (*CuteQSGRhiLayerCall22)(const void *, int *);
typedef bool (*CuteQSGRhiLayerCall23)(const void *, int *);
typedef void * (*CuteQSGRhiLayerCall24)(const void *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiLayerCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiLayerCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiLayerCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiLayerCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiLayerCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiLayerCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiLayerCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiLayer : public QSGRhiLayer {
public:
  using QSGRhiLayer::QSGRhiLayer;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QSGDynamicTexture13updateTextureEv")) {
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
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setItemEP7QSGNode")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setRectERK6QRectF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setSizeERK5QSize")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer13setHasMipmapsEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer9setFormatENS_6FormatE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setLiveEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer12setRecursiveEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setDevicePixelRatioEd")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setMirrorHorizontalEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer17setMirrorVerticalEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer10setSamplesEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer14scheduleUpdateEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSGLayer7toImageEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer16markDirtyTextureEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer11invalidatedEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSGRhiLayer::updateTexture()
  bool updateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiLayerCall0 call = reinterpret_cast<CuteQSGRhiLayerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiLayer::updateTexture();
  }

  //  bool QSGRhiLayer::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiLayerCall1 call = reinterpret_cast<CuteQSGRhiLayerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiLayer::hasAlphaChannel();
  }

  //  bool QSGRhiLayer::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiLayerCall2 call = reinterpret_cast<CuteQSGRhiLayerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiLayer::hasMipmaps();
  }

  //  QSize QSGRhiLayer::textureSize() const
  QSize textureSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiLayerCall3 call = reinterpret_cast<CuteQSGRhiLayerCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiLayer::textureSize();
  }

  //  qint64 QSGRhiLayer::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiLayerCall4 call = reinterpret_cast<CuteQSGRhiLayerCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiLayer::comparisonKey();
  }

  //  QRhiTexture *QSGRhiLayer::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiLayerCall5 call = reinterpret_cast<CuteQSGRhiLayerCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGRhiLayer::rhiTexture();
  }

  //  void QSGRhiLayer::commitTextureOperations(QRhi *rhi,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiLayerCall6 call = reinterpret_cast<CuteQSGRhiLayerCall6>(taken[6]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiLayer::commitTextureOperations(rhi, resourceUpdates);
  }

  //  void QSGRhiLayer::setItem(QSGNode *item)
  void setItem(QSGNode *item) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiLayerCall7 call = reinterpret_cast<CuteQSGRhiLayerCall7>(taken[7]);
      call(this, item, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setItem(item);
  }

  //  void QSGRhiLayer::setRect(const QRectF &logicalRect)
  void setRect(const QRectF &logicalRect) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiLayerCall8 call = reinterpret_cast<CuteQSGRhiLayerCall8>(taken[8]);
      call(this, &logicalRect, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setRect(logicalRect);
  }

  //  void QSGRhiLayer::setSize(const QSize &pixelSize)
  void setSize(const QSize &pixelSize) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiLayerCall9 call = reinterpret_cast<CuteQSGRhiLayerCall9>(taken[9]);
      call(this, &pixelSize, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setSize(pixelSize);
  }

  //  void QSGRhiLayer::setHasMipmaps(bool mipmap)
  void setHasMipmaps(bool mipmap) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRhiLayerCall10 call = reinterpret_cast<CuteQSGRhiLayerCall10>(taken[10]);
      call(this, mipmap, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setHasMipmaps(mipmap);
  }

  //  void QSGRhiLayer::setFormat(Format format)
  void setFormat(QSGLayer::Format format) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGRhiLayerCall11 call = reinterpret_cast<CuteQSGRhiLayerCall11>(taken[11]);
      call(this, static_cast<int>(format), &handled);
      if (handled) return;
    }
    QSGRhiLayer::setFormat(format);
  }

  //  void QSGRhiLayer::setLive(bool live)
  void setLive(bool live) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGRhiLayerCall12 call = reinterpret_cast<CuteQSGRhiLayerCall12>(taken[12]);
      call(this, live, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setLive(live);
  }

  //  void QSGRhiLayer::setRecursive(bool recursive)
  void setRecursive(bool recursive) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGRhiLayerCall13 call = reinterpret_cast<CuteQSGRhiLayerCall13>(taken[13]);
      call(this, recursive, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setRecursive(recursive);
  }

  //  void QSGRhiLayer::setDevicePixelRatio(qreal ratio)
  void setDevicePixelRatio(qreal ratio) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGRhiLayerCall14 call = reinterpret_cast<CuteQSGRhiLayerCall14>(taken[14]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setDevicePixelRatio(ratio);
  }

  //  void QSGRhiLayer::setMirrorHorizontal(bool mirror)
  void setMirrorHorizontal(bool mirror) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGRhiLayerCall15 call = reinterpret_cast<CuteQSGRhiLayerCall15>(taken[15]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setMirrorHorizontal(mirror);
  }

  //  void QSGRhiLayer::setMirrorVertical(bool mirror)
  void setMirrorVertical(bool mirror) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGRhiLayerCall16 call = reinterpret_cast<CuteQSGRhiLayerCall16>(taken[16]);
      call(this, mirror, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setMirrorVertical(mirror);
  }

  //  QRectF QSGRhiLayer::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGRhiLayerCall17 call = reinterpret_cast<CuteQSGRhiLayerCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiLayer::normalizedTextureSubRect();
  }

  //  void QSGRhiLayer::setSamples(int samples)
  void setSamples(int samples) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGRhiLayerCall18 call = reinterpret_cast<CuteQSGRhiLayerCall18>(taken[18]);
      call(this, samples, &handled);
      if (handled) return;
    }
    QSGRhiLayer::setSamples(samples);
  }

  //  void QSGRhiLayer::scheduleUpdate()
  void scheduleUpdate() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGRhiLayerCall19 call = reinterpret_cast<CuteQSGRhiLayerCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRhiLayer::scheduleUpdate();
  }

  //  QImage QSGRhiLayer::toImage() const
  QImage toImage() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGRhiLayerCall20 call = reinterpret_cast<CuteQSGRhiLayerCall20>(taken[20]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRhiLayer::toImage();
  }

  //  void QSGRhiLayer::markDirtyTexture()
  void markDirtyTexture() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGRhiLayerCall21 call = reinterpret_cast<CuteQSGRhiLayerCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRhiLayer::markDirtyTexture();
  }

  //  void QSGRhiLayer::invalidated()
  void invalidated() override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGRhiLayerCall22 call = reinterpret_cast<CuteQSGRhiLayerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRhiLayer::invalidated();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGRhiLayerCall23 call = reinterpret_cast<CuteQSGRhiLayerCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexture::isAtlasTexture();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGRhiLayerCall24 call = reinterpret_cast<CuteQSGRhiLayerCall24>(taken[24]);
      void * given = call(this, resourceUpdates, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGTexture::removedFromAtlas(resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGRhiLayerCall25 call = reinterpret_cast<CuteQSGRhiLayerCall25>(taken[25]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGRhiLayerCall26 call = reinterpret_cast<CuteQSGRhiLayerCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGRhiLayerCall27 call = reinterpret_cast<CuteQSGRhiLayerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGRhiLayerCall28 call = reinterpret_cast<CuteQSGRhiLayerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGRhiLayerCall29 call = reinterpret_cast<CuteQSGRhiLayerCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSGRhiLayerCall30 call = reinterpret_cast<CuteQSGRhiLayerCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSGRhiLayerCall31 call = reinterpret_cast<CuteQSGRhiLayerCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGRhiLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QSGRhiLayer10metaObjectEv(
    const QSGRhiLayer *self) {
  return self->metaObject();
}

//  void *QSGRhiLayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QSGRhiLayer11qt_metacastEPKc(
    QSGRhiLayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGRhiLayer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QSGRhiLayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGRhiLayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGRhiLayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QSGRhiLayer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGRhiLayer::tr(s, c, n));
}

//  QSGRhiLayer::QSGRhiLayer(QSGRenderContext *context)
extern "C" Q_DECL_EXPORT
QSGRhiLayer *ritual_ZN11QSGRhiLayerC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGRhiLayer(context);
}

//  QSGRhiLayer::~QSGRhiLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayerD1Ev(QSGRhiLayer *self) {
  delete self;
}

//  bool QSGRhiLayer::updateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSGRhiLayer13updateTextureEv(QSGRhiLayer *self) {
  return self->updateTexture();
}

//  bool QSGRhiLayer::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSGRhiLayer15hasAlphaChannelEv(const QSGRhiLayer *self) {
  return self->hasAlphaChannel();
}

//  bool QSGRhiLayer::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSGRhiLayer10hasMipmapsEv(const QSGRhiLayer *self) {
  return self->hasMipmaps();
}

//  QSize QSGRhiLayer::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSGRhiLayer11textureSizeEv(const QSGRhiLayer *self) {
  return new QSize(self->textureSize());
}

//  qint64 QSGRhiLayer::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QSGRhiLayer13comparisonKeyEv(const QSGRhiLayer *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGRhiLayer::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK11QSGRhiLayer10rhiTextureEv(const QSGRhiLayer *self) {
  return self->rhiTexture();
}

//  void QSGRhiLayer::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGRhiLayer *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  void QSGRhiLayer::setItem(QSGNode *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer7setItemEP7QSGNode(
    QSGRhiLayer *self,
    QSGNode *item) {
  self->setItem(item);
}

//  void QSGRhiLayer::setRect(const QRectF &logicalRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer7setRectERK6QRectF(
    QSGRhiLayer *self,
    const QRectF *logicalRect) {
  self->setRect(*logicalRect);
}

//  void QSGRhiLayer::setSize(const QSize &pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer7setSizeERK5QSize(
    QSGRhiLayer *self,
    const QSize *pixelSize) {
  self->setSize(*pixelSize);
}

//  void QSGRhiLayer::setHasMipmaps(bool mipmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer13setHasMipmapsEb(
    QSGRhiLayer *self,
    bool mipmap) {
  self->setHasMipmaps(mipmap);
}

//  void QSGRhiLayer::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer9setFormatEN8QSGLayer6FormatE(
    QSGRhiLayer *self,
    QSGLayer::Format format) {
  self->setFormat(format);
}

//  void QSGRhiLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer7setLiveEb(QSGRhiLayer *self, bool live) {
  self->setLive(live);
}

//  void QSGRhiLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer12setRecursiveEb(
    QSGRhiLayer *self,
    bool recursive) {
  self->setRecursive(recursive);
}

//  void QSGRhiLayer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer19setDevicePixelRatioEd(
    QSGRhiLayer *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGRhiLayer::setMirrorHorizontal(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer19setMirrorHorizontalEb(
    QSGRhiLayer *self,
    bool mirror) {
  self->setMirrorHorizontal(mirror);
}

//  void QSGRhiLayer::setMirrorVertical(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer17setMirrorVerticalEb(
    QSGRhiLayer *self,
    bool mirror) {
  self->setMirrorVertical(mirror);
}

//  QRectF QSGRhiLayer::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QSGRhiLayer24normalizedTextureSubRectEv(
    const QSGRhiLayer *self) {
  return new QRectF(self->normalizedTextureSubRect());
}

//  void QSGRhiLayer::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer10setSamplesEi(QSGRhiLayer *self, int samples) {
  self->setSamples(samples);
}

//  void QSGRhiLayer::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer14scheduleUpdateEv(QSGRhiLayer *self) {
  self->scheduleUpdate();
}

//  QImage QSGRhiLayer::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK11QSGRhiLayer7toImageEv(const QSGRhiLayer *self) {
  return new QImage(self->toImage());
}

//  void QSGRhiLayer::markDirtyTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer16markDirtyTextureEv(QSGRhiLayer *self) {
  self->markDirtyTexture();
}

//  void QSGRhiLayer::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer11invalidatedEv(QSGRhiLayer *self) {
  self->invalidated();
}

//  void QSGRhiLayer::grab()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer4grabEv(QSGRhiLayer *self) {
  self->grab();
}

//  void QSGRhiLayer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer16releaseResourcesEv(QSGRhiLayer *self) {
  self->releaseResources();
}

//  void QSGRhiLayer::clearMainTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRhiLayer16clearMainTextureEv(QSGRhiLayer *self) {
  self->clearMainTexture();
}

//  a Python function taken by a CuteQSGRhiLayer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiLayer(
    QSGRhiLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiLayer *>(self)->take(key, call);
}

//  bool QSGRhiLayer::updateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSGRhiLayer13updateTextureEv(QSGRhiLayer *self) {
  return self->QSGRhiLayer::updateTexture();
}

//  bool QSGRhiLayer::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSGRhiLayer15hasAlphaChannelEv(
    const QSGRhiLayer *self) {
  return self->QSGRhiLayer::hasAlphaChannel();
}

//  bool QSGRhiLayer::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSGRhiLayer10hasMipmapsEv(const QSGRhiLayer *self) {
  return self->QSGRhiLayer::hasMipmaps();
}

//  QSize QSGRhiLayer::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QSGRhiLayer11textureSizeEv(const QSGRhiLayer *self) {
  return new QSize(self->QSGRhiLayer::textureSize());
}

//  qint64 QSGRhiLayer::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK11QSGRhiLayer13comparisonKeyEv(
    const QSGRhiLayer *self) {
  return self->QSGRhiLayer::comparisonKey();
}

//  QRhiTexture *QSGRhiLayer::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK11QSGRhiLayer10rhiTextureEv(
    const QSGRhiLayer *self) {
  return self->QSGRhiLayer::rhiTexture();
}

//  void QSGRhiLayer::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGRhiLayer *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGRhiLayer::commitTextureOperations(rhi, resourceUpdates);
}

//  void QSGRhiLayer::setItem(QSGNode *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer7setItemEP7QSGNode(
    QSGRhiLayer *self,
    QSGNode *item) {
  self->QSGRhiLayer::setItem(item);
}

//  void QSGRhiLayer::setRect(const QRectF &logicalRect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer7setRectERK6QRectF(
    QSGRhiLayer *self,
    const QRectF *logicalRect) {
  self->QSGRhiLayer::setRect(*logicalRect);
}

//  void QSGRhiLayer::setSize(const QSize &pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer7setSizeERK5QSize(
    QSGRhiLayer *self,
    const QSize *pixelSize) {
  self->QSGRhiLayer::setSize(*pixelSize);
}

//  void QSGRhiLayer::setHasMipmaps(bool mipmap)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer13setHasMipmapsEb(
    QSGRhiLayer *self,
    bool mipmap) {
  self->QSGRhiLayer::setHasMipmaps(mipmap);
}

//  void QSGRhiLayer::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer9setFormatEN8QSGLayer6FormatE(
    QSGRhiLayer *self,
    QSGLayer::Format format) {
  self->QSGRhiLayer::setFormat(format);
}

//  void QSGRhiLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer7setLiveEb(QSGRhiLayer *self, bool live) {
  self->QSGRhiLayer::setLive(live);
}

//  void QSGRhiLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer12setRecursiveEb(
    QSGRhiLayer *self,
    bool recursive) {
  self->QSGRhiLayer::setRecursive(recursive);
}

//  void QSGRhiLayer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer19setDevicePixelRatioEd(
    QSGRhiLayer *self,
    qreal ratio) {
  self->QSGRhiLayer::setDevicePixelRatio(ratio);
}

//  void QSGRhiLayer::setMirrorHorizontal(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer19setMirrorHorizontalEb(
    QSGRhiLayer *self,
    bool mirror) {
  self->QSGRhiLayer::setMirrorHorizontal(mirror);
}

//  void QSGRhiLayer::setMirrorVertical(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer17setMirrorVerticalEb(
    QSGRhiLayer *self,
    bool mirror) {
  self->QSGRhiLayer::setMirrorVertical(mirror);
}

//  QRectF QSGRhiLayer::normalizedTextureSubRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK11QSGRhiLayer24normalizedTextureSubRectEv(
    const QSGRhiLayer *self) {
  return new QRectF(self->QSGRhiLayer::normalizedTextureSubRect());
}

//  void QSGRhiLayer::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer10setSamplesEi(
    QSGRhiLayer *self,
    int samples) {
  self->QSGRhiLayer::setSamples(samples);
}

//  void QSGRhiLayer::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer14scheduleUpdateEv(QSGRhiLayer *self) {
  self->QSGRhiLayer::scheduleUpdate();
}

//  QImage QSGRhiLayer::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK11QSGRhiLayer7toImageEv(const QSGRhiLayer *self) {
  return new QImage(self->QSGRhiLayer::toImage());
}

//  void QSGRhiLayer::markDirtyTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer16markDirtyTextureEv(QSGRhiLayer *self) {
  self->QSGRhiLayer::markDirtyTexture();
}

//  void QSGRhiLayer::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRhiLayer11invalidatedEv(QSGRhiLayer *self) {
  self->QSGRhiLayer::invalidated();
}
