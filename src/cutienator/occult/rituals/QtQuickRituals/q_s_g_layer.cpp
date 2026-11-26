//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGLayer that Python can take functions over in. Every QSGLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGLayerCall0)(const void *, QSGNode *, int *);
typedef void (*CuteQSGLayerCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQSGLayerCall2)(const void *, const QSize *, int *);
typedef void (*CuteQSGLayerCall3)(const void *, int *);
typedef const QImage * (*CuteQSGLayerCall4)(const void *, int *);
typedef void (*CuteQSGLayerCall5)(const void *, bool, int *);
typedef void (*CuteQSGLayerCall6)(const void *, bool, int *);
typedef void (*CuteQSGLayerCall7)(const void *, int, int *);
typedef void (*CuteQSGLayerCall8)(const void *, bool, int *);
typedef void (*CuteQSGLayerCall9)(const void *, qreal, int *);
typedef void (*CuteQSGLayerCall10)(const void *, bool, int *);
typedef void (*CuteQSGLayerCall11)(const void *, bool, int *);
typedef void (*CuteQSGLayerCall12)(const void *, int, int *);
typedef void (*CuteQSGLayerCall13)(const void *, int *);
typedef void (*CuteQSGLayerCall14)(const void *, int *);
typedef bool (*CuteQSGLayerCall15)(const void *, int *);
typedef qint64 (*CuteQSGLayerCall16)(const void *, int *);
typedef void * (*CuteQSGLayerCall17)(const void *, int *);
typedef const QSize * (*CuteQSGLayerCall18)(const void *, int *);
typedef bool (*CuteQSGLayerCall19)(const void *, int *);
typedef bool (*CuteQSGLayerCall20)(const void *, int *);
typedef const QRectF * (*CuteQSGLayerCall21)(const void *, int *);
typedef bool (*CuteQSGLayerCall22)(const void *, int *);
typedef void * (*CuteQSGLayerCall23)(const void *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGLayerCall24)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGLayerCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGLayerCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGLayerCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGLayerCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGLayerCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGLayerCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGLayerCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGLayer : public QSGLayer {
public:
  using QSGLayer::QSGLayer;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8QSGLayer7setItemEP7QSGNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setRectERK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setSizeERK5QSize")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer14scheduleUpdateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSGLayer7toImageEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer7setLiveEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer12setRecursiveEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer9setFormatENS_6FormatE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer13setHasMipmapsEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setDevicePixelRatioEd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer19setMirrorHorizontalEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer17setMirrorVerticalEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer10setSamplesEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer16markDirtyTextureEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8QSGLayer11invalidatedEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QSGDynamicTexture13updateTextureEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture24normalizedTextureSubRectEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture14isAtlasTextureEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture16removedFromAtlasEP23QRhiResourceUpdateBatch")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
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

  //  void QSGLayer::setItem(QSGNode *item)
  void setItem(QSGNode *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGLayerCall0 call = reinterpret_cast<CuteQSGLayerCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setRect(const QRectF &logicalRect)
  void setRect(const QRectF &logicalRect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGLayerCall1 call = reinterpret_cast<CuteQSGLayerCall1>(taken[1]);
      call(this, &logicalRect, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setSize(const QSize &pixelSize)
  void setSize(const QSize &pixelSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGLayerCall2 call = reinterpret_cast<CuteQSGLayerCall2>(taken[2]);
      call(this, &pixelSize, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::scheduleUpdate()
  void scheduleUpdate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGLayerCall3 call = reinterpret_cast<CuteQSGLayerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QImage QSGLayer::toImage() const
  QImage toImage() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGLayerCall4 call = reinterpret_cast<CuteQSGLayerCall4>(taken[4]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGLayer::setLive(bool live)
  void setLive(bool live) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGLayerCall5 call = reinterpret_cast<CuteQSGLayerCall5>(taken[5]);
      call(this, live, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setRecursive(bool recursive)
  void setRecursive(bool recursive) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGLayerCall6 call = reinterpret_cast<CuteQSGLayerCall6>(taken[6]);
      call(this, recursive, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setFormat(Format format)
  void setFormat(QSGLayer::Format format) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGLayerCall7 call = reinterpret_cast<CuteQSGLayerCall7>(taken[7]);
      call(this, static_cast<int>(format), &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setHasMipmaps(bool mipmap)
  void setHasMipmaps(bool mipmap) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGLayerCall8 call = reinterpret_cast<CuteQSGLayerCall8>(taken[8]);
      call(this, mipmap, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setDevicePixelRatio(qreal ratio)
  void setDevicePixelRatio(qreal ratio) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGLayerCall9 call = reinterpret_cast<CuteQSGLayerCall9>(taken[9]);
      call(this, ratio, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setMirrorHorizontal(bool mirror)
  void setMirrorHorizontal(bool mirror) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGLayerCall10 call = reinterpret_cast<CuteQSGLayerCall10>(taken[10]);
      call(this, mirror, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setMirrorVertical(bool mirror)
  void setMirrorVertical(bool mirror) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGLayerCall11 call = reinterpret_cast<CuteQSGLayerCall11>(taken[11]);
      call(this, mirror, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::setSamples(int samples)
  void setSamples(int samples) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGLayerCall12 call = reinterpret_cast<CuteQSGLayerCall12>(taken[12]);
      call(this, samples, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::markDirtyTexture()
  void markDirtyTexture() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGLayerCall13 call = reinterpret_cast<CuteQSGLayerCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGLayer::invalidated()
  void invalidated() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGLayerCall14 call = reinterpret_cast<CuteQSGLayerCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QSGDynamicTexture::updateTexture()
  bool updateTexture() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGLayerCall15 call = reinterpret_cast<CuteQSGLayerCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QSGTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGLayerCall16 call = reinterpret_cast<CuteQSGLayerCall16>(taken[16]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhiTexture *QSGTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGLayerCall17 call = reinterpret_cast<CuteQSGLayerCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGTexture::rhiTexture();
  }

  //  QSize QSGTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGLayerCall18 call = reinterpret_cast<CuteQSGLayerCall18>(taken[18]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGLayerCall19 call = reinterpret_cast<CuteQSGLayerCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGLayerCall20 call = reinterpret_cast<CuteQSGLayerCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGLayerCall21 call = reinterpret_cast<CuteQSGLayerCall21>(taken[21]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGLayerCall22 call = reinterpret_cast<CuteQSGLayerCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexture::isAtlasTexture();
  }

  //  QSGTexture *QSGTexture::removedFromAtlas(QRhiResourceUpdateBatch
  //      *resourceUpdates) const
  QSGTexture *removedFromAtlas(
      QRhiResourceUpdateBatch *resourceUpdates) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGLayerCall23 call = reinterpret_cast<CuteQSGLayerCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQSGLayerCall24 call = reinterpret_cast<CuteQSGLayerCall24>(taken[24]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGTexture::commitTextureOperations(rhi, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGLayerCall25 call = reinterpret_cast<CuteQSGLayerCall25>(taken[25]);
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
      CuteQSGLayerCall26 call = reinterpret_cast<CuteQSGLayerCall26>(taken[26]);
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
      CuteQSGLayerCall27 call = reinterpret_cast<CuteQSGLayerCall27>(taken[27]);
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
      CuteQSGLayerCall28 call = reinterpret_cast<CuteQSGLayerCall28>(taken[28]);
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
      CuteQSGLayerCall29 call = reinterpret_cast<CuteQSGLayerCall29>(taken[29]);
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
      CuteQSGLayerCall30 call = reinterpret_cast<CuteQSGLayerCall30>(taken[30]);
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
      CuteQSGLayerCall31 call = reinterpret_cast<CuteQSGLayerCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QSGLayer10metaObjectEv(const QSGLayer *self) {
  return self->metaObject();
}

//  void *QSGLayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QSGLayer11qt_metacastEPKc(QSGLayer *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGLayer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QSGLayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGLayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGLayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSGLayer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSGLayer::tr(s, c, n));
}

//  QSGLayer::~QSGLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayerD1Ev(QSGLayer *self) {
  delete self;
}

//  void QSGLayer::setItem(QSGNode *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer7setItemEP7QSGNode(QSGLayer *self, QSGNode *item) {
  self->setItem(item);
}

//  void QSGLayer::setRect(const QRectF &logicalRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer7setRectERK6QRectF(
    QSGLayer *self,
    const QRectF *logicalRect) {
  self->setRect(*logicalRect);
}

//  void QSGLayer::setSize(const QSize &pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer7setSizeERK5QSize(
    QSGLayer *self,
    const QSize *pixelSize) {
  self->setSize(*pixelSize);
}

//  void QSGLayer::scheduleUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer14scheduleUpdateEv(QSGLayer *self) {
  self->scheduleUpdate();
}

//  QImage QSGLayer::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK8QSGLayer7toImageEv(const QSGLayer *self) {
  return new QImage(self->toImage());
}

//  void QSGLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer7setLiveEb(QSGLayer *self, bool live) {
  self->setLive(live);
}

//  void QSGLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer12setRecursiveEb(QSGLayer *self, bool recursive) {
  self->setRecursive(recursive);
}

//  void QSGLayer::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer9setFormatENS_6FormatE(
    QSGLayer *self,
    QSGLayer::Format format) {
  self->setFormat(format);
}

//  void QSGLayer::setHasMipmaps(bool mipmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer13setHasMipmapsEb(QSGLayer *self, bool mipmap) {
  self->setHasMipmaps(mipmap);
}

//  void QSGLayer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer19setDevicePixelRatioEd(QSGLayer *self, qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGLayer::setMirrorHorizontal(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer19setMirrorHorizontalEb(QSGLayer *self, bool mirror) {
  self->setMirrorHorizontal(mirror);
}

//  void QSGLayer::setMirrorVertical(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer17setMirrorVerticalEb(QSGLayer *self, bool mirror) {
  self->setMirrorVertical(mirror);
}

//  void QSGLayer::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer10setSamplesEi(QSGLayer *self, int samples) {
  self->setSamples(samples);
}

//  void QSGLayer::markDirtyTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer16markDirtyTextureEv(QSGLayer *self) {
  self->markDirtyTexture();
}

//  void QSGLayer::invalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer11invalidatedEv(QSGLayer *self) {
  self->invalidated();
}

//  void QSGLayer::updateRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer15updateRequestedEv(QSGLayer *self) {
  self->updateRequested();
}

//  void QSGLayer::scheduledUpdateCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSGLayer24scheduledUpdateCompletedEv(QSGLayer *self) {
  self->scheduledUpdateCompleted();
}

//  QSGLayer::QSGLayer(QSGTexturePrivate &dd)
extern "C" Q_DECL_EXPORT
QSGLayer *ritual_ZN8QSGLayerC1ER17QSGTexturePrivate(QSGTexturePrivate *dd) {
  return new CuteQSGLayer(*dd);
}

//  a Python function taken by a CuteQSGLayer, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGLayer(QSGLayer *self, const char *key, void *call) {
  return static_cast<CuteQSGLayer *>(self)->take(key, call);
}
