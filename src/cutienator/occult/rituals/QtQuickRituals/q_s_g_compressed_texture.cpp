//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGCompressedTexture that Python can take functions over in. Every QSGCompressedTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQSGCompressedTextureCall0)(const void *, int *);
typedef bool (*CuteQSGCompressedTextureCall1)(const void *, int *);
typedef bool (*CuteQSGCompressedTextureCall2)(const void *, int *);
typedef qint64 (*CuteQSGCompressedTextureCall3)(const void *, int *);
typedef void * (*CuteQSGCompressedTextureCall4)(const void *, int *);
typedef void (*CuteQSGCompressedTextureCall5)(const void *, QRhi *, QRhiResourceUpdateBatch *, int *);
typedef const QRectF * (*CuteQSGCompressedTextureCall6)(const void *, int *);
typedef bool (*CuteQSGCompressedTextureCall7)(const void *, int *);
typedef void * (*CuteQSGCompressedTextureCall8)(const void *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedTextureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedTextureCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGCompressedTexture : public QSGCompressedTexture {
public:
  using QSGCompressedTexture::QSGCompressedTexture;
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

  //  QSize QSGCompressedTexture::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCompressedTextureCall0 call = reinterpret_cast<CuteQSGCompressedTextureCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGCompressedTexture::textureSize();
  }

  //  bool QSGCompressedTexture::hasAlphaChannel() const
  bool hasAlphaChannel() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCompressedTextureCall1 call = reinterpret_cast<CuteQSGCompressedTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedTexture::hasAlphaChannel();
  }

  //  bool QSGCompressedTexture::hasMipmaps() const
  bool hasMipmaps() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCompressedTextureCall2 call = reinterpret_cast<CuteQSGCompressedTextureCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedTexture::hasMipmaps();
  }

  //  qint64 QSGCompressedTexture::comparisonKey() const
  qint64 comparisonKey() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCompressedTextureCall3 call = reinterpret_cast<CuteQSGCompressedTextureCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedTexture::comparisonKey();
  }

  //  QRhiTexture *QSGCompressedTexture::rhiTexture() const
  QRhiTexture *rhiTexture() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGCompressedTextureCall4 call = reinterpret_cast<CuteQSGCompressedTextureCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QSGCompressedTexture::rhiTexture();
  }

  //  void QSGCompressedTexture::commitTextureOperations(QRhi *rhi,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void commitTextureOperations(
      QRhi *rhi,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGCompressedTextureCall5 call = reinterpret_cast<CuteQSGCompressedTextureCall5>(taken[5]);
      call(this, rhi, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGCompressedTexture::commitTextureOperations(rhi, resourceUpdates);
  }

  //  QRectF QSGTexture::normalizedTextureSubRect() const
  QRectF normalizedTextureSubRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGCompressedTextureCall6 call = reinterpret_cast<CuteQSGCompressedTextureCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGTexture::normalizedTextureSubRect();
  }

  //  bool QSGTexture::isAtlasTexture() const
  bool isAtlasTexture() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGCompressedTextureCall7 call = reinterpret_cast<CuteQSGCompressedTextureCall7>(taken[7]);
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
      CuteQSGCompressedTextureCall8 call = reinterpret_cast<CuteQSGCompressedTextureCall8>(taken[8]);
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
      CuteQSGCompressedTextureCall9 call = reinterpret_cast<CuteQSGCompressedTextureCall9>(taken[9]);
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
      CuteQSGCompressedTextureCall10 call = reinterpret_cast<CuteQSGCompressedTextureCall10>(taken[10]);
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
      CuteQSGCompressedTextureCall11 call = reinterpret_cast<CuteQSGCompressedTextureCall11>(taken[11]);
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
      CuteQSGCompressedTextureCall12 call = reinterpret_cast<CuteQSGCompressedTextureCall12>(taken[12]);
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
      CuteQSGCompressedTextureCall13 call = reinterpret_cast<CuteQSGCompressedTextureCall13>(taken[13]);
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
      CuteQSGCompressedTextureCall14 call = reinterpret_cast<CuteQSGCompressedTextureCall14>(taken[14]);
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
      CuteQSGCompressedTextureCall15 call = reinterpret_cast<CuteQSGCompressedTextureCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGCompressedTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QSGCompressedTexture10metaObjectEv(
    const QSGCompressedTexture *self) {
  return self->metaObject();
}

//  QString QSGCompressedTexture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QSGCompressedTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGCompressedTexture::tr(s, c, n));
}

//  QSGCompressedTexture::QSGCompressedTexture(const QTextureFileData
//      &texData)
extern "C" Q_DECL_EXPORT
QSGCompressedTexture *ritual_ZN20QSGCompressedTextureC1ERK16QTextureFileData(
    const QTextureFileData *texData) {
  return new CuteQSGCompressedTexture(*texData);
}

//  QSGCompressedTexture::~QSGCompressedTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCompressedTextureD1Ev(QSGCompressedTexture *self) {
  delete self;
}

//  QSize QSGCompressedTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QSGCompressedTexture11textureSizeEv(
    const QSGCompressedTexture *self) {
  return new QSize(self->textureSize());
}

//  bool QSGCompressedTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QSGCompressedTexture15hasAlphaChannelEv(
    const QSGCompressedTexture *self) {
  return self->hasAlphaChannel();
}

//  bool QSGCompressedTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QSGCompressedTexture10hasMipmapsEv(
    const QSGCompressedTexture *self) {
  return self->hasMipmaps();
}

//  qint64 QSGCompressedTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QSGCompressedTexture13comparisonKeyEv(
    const QSGCompressedTexture *self) {
  return self->comparisonKey();
}

//  QRhiTexture *QSGCompressedTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK20QSGCompressedTexture10rhiTextureEv(
    const QSGCompressedTexture *self) {
  return self->rhiTexture();
}

//  void QSGCompressedTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCompressedTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGCompressedTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->commitTextureOperations(rhi, resourceUpdates);
}

//  QTextureFileData QSGCompressedTexture::textureData() const
extern "C" Q_DECL_EXPORT
QTextureFileData *ritual_ZNK20QSGCompressedTexture11textureDataEv(
    const QSGCompressedTexture *self) {
  return new QTextureFileData(self->textureData());
}

//  FormatInfo QSGCompressedTexture::formatInfo(quint32 glTextureFormat)
extern "C" Q_DECL_EXPORT
QSGCompressedTexture::FormatInfo *ritual_ZN20QSGCompressedTexture10formatInfoEj(
    quint32 glTextureFormat) {
  return new QSGCompressedTexture::FormatInfo(
      QSGCompressedTexture::formatInfo(
          glTextureFormat));
}

//  bool QSGCompressedTexture::formatIsOpaque(quint32 glTextureFormat)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSGCompressedTexture14formatIsOpaqueEj(
    quint32 glTextureFormat) {
  return QSGCompressedTexture::formatIsOpaque(glTextureFormat);
}

//  a Python function taken by a CuteQSGCompressedTexture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCompressedTexture(
    QSGCompressedTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCompressedTexture *>(self)->take(key, call);
}

//  QSize QSGCompressedTexture::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK20QSGCompressedTexture11textureSizeEv(
    const QSGCompressedTexture *self) {
  return new QSize(self->QSGCompressedTexture::textureSize());
}

//  bool QSGCompressedTexture::hasAlphaChannel() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QSGCompressedTexture15hasAlphaChannelEv(
    const QSGCompressedTexture *self) {
  return self->QSGCompressedTexture::hasAlphaChannel();
}

//  bool QSGCompressedTexture::hasMipmaps() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QSGCompressedTexture10hasMipmapsEv(
    const QSGCompressedTexture *self) {
  return self->QSGCompressedTexture::hasMipmaps();
}

//  qint64 QSGCompressedTexture::comparisonKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK20QSGCompressedTexture13comparisonKeyEv(
    const QSGCompressedTexture *self) {
  return self->QSGCompressedTexture::comparisonKey();
}

//  QRhiTexture *QSGCompressedTexture::rhiTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK20QSGCompressedTexture10rhiTextureEv(
    const QSGCompressedTexture *self) {
  return self->QSGCompressedTexture::rhiTexture();
}

//  void QSGCompressedTexture::commitTextureOperations(QRhi *rhi,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGCompressedTexture23commitTextureOperationsEP4QRhiP23QRhiResourceUpdateBatch(
    QSGCompressedTexture *self,
    QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QSGCompressedTexture::commitTextureOperations(rhi, resourceUpdates);
}
