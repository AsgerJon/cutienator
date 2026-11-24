//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGDynamicTexture that Python can take functions over in. Every QSGDynamicTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGDynamicTextureCall0)(const void *, int *);
typedef qint64 (*CuteQSGDynamicTextureCall1)(const void *, int *);
typedef void * (*CuteQSGDynamicTextureCall2)(const void *, int *);
typedef const QSize * (*CuteQSGDynamicTextureCall3)(const void *, int *);
typedef bool (*CuteQSGDynamicTextureCall4)(const void *, int *);
typedef bool (*CuteQSGDynamicTextureCall5)(const void *, int *);
typedef const QRectF * (*CuteQSGDynamicTextureCall6)(const void *, int *);
typedef bool (*CuteQSGDynamicTextureCall7)(const void *, int *);
typedef void * (*CuteQSGDynamicTextureCall8)(const void *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQSGDynamicTextureCall9)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDynamicTextureCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDynamicTextureCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDynamicTextureCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDynamicTextureCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDynamicTextureCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDynamicTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDynamicTextureCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGDynamicTexture : public QSGDynamicTexture {
public:
  using QSGDynamicTexture::QSGDynamicTexture;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QSGDynamicTexture13updateTextureEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture13comparisonKeyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10rhiTextureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture11textureSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture15hasAlphaChannelEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGTexture10hasMipmapsEv")) {
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
    if (!std::strcmp(key, "_ZN10QSGTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSGDynamicTexture::updateTexture()
  bool updateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDynamicTextureCall0 call = reinterpret_cast<CuteQSGDynamicTextureCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QSGTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDynamicTextureCall1 call = reinterpret_cast<CuteQSGDynamicTextureCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhiTexture *QSGTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDynamicTextureCall2 call = reinterpret_cast<CuteQSGDynamicTextureCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGTexture::rhiTexture();
  }

  //  QSize QSGTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDynamicTextureCall3 call = reinterpret_cast<CuteQSGDynamicTextureCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDynamicTextureCall4 call = reinterpret_cast<CuteQSGDynamicTextureCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDynamicTextureCall5 call = reinterpret_cast<CuteQSGDynamicTextureCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDynamicTextureCall6 call = reinterpret_cast<CuteQSGDynamicTextureCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDynamicTextureCall7 call = reinterpret_cast<CuteQSGDynamicTextureCall7>(taken[7]);
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
      CuteQSGDynamicTextureCall8 call = reinterpret_cast<CuteQSGDynamicTextureCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQSGDynamicTextureCall9 call = reinterpret_cast<CuteQSGDynamicTextureCall9>(taken[9]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGTexture::commitTextureOperations(rhi, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDynamicTextureCall10 call = reinterpret_cast<CuteQSGDynamicTextureCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDynamicTextureCall11 call = reinterpret_cast<CuteQSGDynamicTextureCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDynamicTextureCall12 call = reinterpret_cast<CuteQSGDynamicTextureCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDynamicTextureCall13 call = reinterpret_cast<CuteQSGDynamicTextureCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGDynamicTextureCall14 call = reinterpret_cast<CuteQSGDynamicTextureCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGDynamicTextureCall15 call = reinterpret_cast<CuteQSGDynamicTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGDynamicTextureCall16 call = reinterpret_cast<CuteQSGDynamicTextureCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGDynamicTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QSGDynamicTexture10metaObjectEv(
    const QSGDynamicTexture *self) {
  return self->metaObject();
}

//  QString QSGDynamicTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSGDynamicTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGDynamicTexture::tr(s, c, n));
}

//  QSGDynamicTexture::~QSGDynamicTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGDynamicTextureD1Ev(QSGDynamicTexture *self) {
  delete self;
}

//  bool QSGDynamicTexture::updateTexture()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSGDynamicTexture13updateTextureEv(QSGDynamicTexture *self) {
  return self->updateTexture();
}

//  a Python function taken by a CuteQSGDynamicTexture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDynamicTexture(
    QSGDynamicTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDynamicTexture *>(self)->take(key, call);
}
