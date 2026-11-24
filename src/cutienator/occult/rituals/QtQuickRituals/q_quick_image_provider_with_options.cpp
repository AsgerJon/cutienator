//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickImageProviderWithOptions that Python can take functions over in. Every QQuickImageProviderWithOptions
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteQQuickImageProviderWithOptionsCall0)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteQQuickImageProviderWithOptionsCall1)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickImageProviderWithOptionsCall2)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickImageProviderWithOptionsCall3)(const void *, const QString *, const QSize *, int *);
typedef const QImage * (*CuteQQuickImageProviderWithOptionsCall4)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef const QPixmap * (*CuteQQuickImageProviderWithOptionsCall5)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef void * (*CuteQQuickImageProviderWithOptionsCall6)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef void * (*CuteQQuickImageProviderWithOptionsCall7)(const void *, const QString *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef int (*CuteQQuickImageProviderWithOptionsCall8)(const void *, int *);
typedef int (*CuteQQuickImageProviderWithOptionsCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageProviderWithOptionsCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageProviderWithOptionsCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderWithOptionsCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderWithOptionsCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderWithOptionsCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderWithOptionsCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderWithOptionsCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageProviderWithOptions : public QQuickImageProviderWithOptions {
public:
  using QQuickImageProviderWithOptions::QQuickImageProviderWithOptions;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringRK5QSize")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QStringRK5QSizeRK26QQuickImageProviderOptions")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase9imageTypeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase5flagsEv")) {
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

  //  QImage QQuickImageProviderWithOptions::requestImage(const QString
  //      &id, QSize *size, const QSize &requestedSize)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall0 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall0>(taken[0]);
      const QImage * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProviderWithOptions::requestImage(id, size, requestedSize);
  }

  //  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString
  //      &id, QSize *size, const QSize &requestedSize)
  QPixmap requestPixmap(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall1 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall1>(taken[1]);
      const QPixmap * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProviderWithOptions::requestPixmap(id, size, requestedSize);
  }

  //  QQuickTextureFactory
  //      *QQuickImageProviderWithOptions::requestTexture(const QString
  //      &id, QSize *size, const QSize &requestedSize)
  QQuickTextureFactory *requestTexture(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall2 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall2>(taken[2]);
      void * given = call(this, &id, size, &requestedSize, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QQuickImageProviderWithOptions::requestTexture(id, size, requestedSize);
  }

  //  QQuickImageResponse
  //      *QQuickImageProviderWithOptions::requestImageResponse(const
  //      QString &id, const QSize &requestedSize)
  QQuickImageResponse *requestImageResponse(
      const QString &id,
      const QSize &requestedSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall3 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall3>(taken[3]);
      void * given = call(this, &id, &requestedSize, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickImageProviderWithOptions::requestImageResponse(id, requestedSize);
  }

  //  QImage QQuickImageProviderWithOptions::requestImage(const QString
  //      &id, QSize *size, const QSize &requestedSize, const
  //      QQuickImageProviderOptions &options)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize,
      const QQuickImageProviderOptions &options) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall4 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall4>(taken[4]);
      const QImage * given = call(this, &id, size, &requestedSize, &options, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProviderWithOptions::requestImage(id, size, requestedSize, options);
  }

  //  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString
  //      &id, QSize *size, const QSize &requestedSize, const
  //      QQuickImageProviderOptions &options)
  QPixmap requestPixmap(
      const QString &id,
      QSize *size,
      const QSize &requestedSize,
      const QQuickImageProviderOptions &options) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall5 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall5>(taken[5]);
      const QPixmap * given = call(this, &id, size, &requestedSize, &options, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProviderWithOptions::requestPixmap(id, size, requestedSize, options);
  }

  //  QQuickTextureFactory
  //      *QQuickImageProviderWithOptions::requestTexture(const QString
  //      &id, QSize *size, const QSize &requestedSize, const
  //      QQuickImageProviderOptions &options)
  QQuickTextureFactory *requestTexture(
      const QString &id,
      QSize *size,
      const QSize &requestedSize,
      const QQuickImageProviderOptions &options) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall6 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall6>(taken[6]);
      void * given = call(this, &id, size, &requestedSize, &options, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QQuickImageProviderWithOptions::requestTexture(id, size, requestedSize, options);
  }

  //  QQuickImageResponse
  //      *QQuickImageProviderWithOptions::requestImageResponse(const
  //      QString &id, const QSize &requestedSize, const
  //      QQuickImageProviderOptions &options)
  QQuickImageResponse *requestImageResponse(
      const QString &id,
      const QSize &requestedSize,
      const QQuickImageProviderOptions &options) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall7 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall7>(taken[7]);
      void * given = call(this, &id, &requestedSize, &options, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickImageProviderWithOptions::requestImageResponse(id, requestedSize, options);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall8 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall9 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQmlImageProviderBase::Flag>::fromInt(given);
    }
    return QQuickImageProvider::flags();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickImageProviderWithOptionsCall10 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall10>(taken[10]);
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
      CuteQQuickImageProviderWithOptionsCall11 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall11>(taken[11]);
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
      CuteQQuickImageProviderWithOptionsCall12 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall12>(taken[12]);
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
      CuteQQuickImageProviderWithOptionsCall13 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall13>(taken[13]);
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
      CuteQQuickImageProviderWithOptionsCall14 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall14>(taken[14]);
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
      CuteQQuickImageProviderWithOptionsCall15 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall15>(taken[15]);
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
      CuteQQuickImageProviderWithOptionsCall16 call = reinterpret_cast<CuteQQuickImageProviderWithOptionsCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QQuickImageProviderWithOptions::QQuickImageProviderWithOptions(ImageType
//      type, Flags flags)
extern "C" Q_DECL_EXPORT
QQuickImageProviderWithOptions *ritual_ZN30QQuickImageProviderWithOptionsC1EN21QQmlImageProviderBase9ImageTypeE6QFlagsINS0_4FlagEE(
    QQmlImageProviderBase::ImageType type,
    int flags) {
  return new CuteQQuickImageProviderWithOptions(
      type,
      QFlags<QQmlImageProviderBase::Flag>::fromInt(flags));
}

//  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(self->requestImage(*id, size, *requestedSize));
}

//  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QPixmap(self->requestPixmap(*id, size, *requestedSize));
}

//  QQuickTextureFactory
//      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return self->requestTexture(*id, size, *requestedSize);
}

//  QQuickImageResponse
//      *QQuickImageProviderWithOptions::requestImageResponse(const QString
//      &id, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QStringRK5QSize(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    const QSize *requestedSize) {
  return self->requestImageResponse(*id, *requestedSize);
}

//  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QImage(self->requestImage(*id, size, *requestedSize, *options));
}

//  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QPixmap(
      self->requestPixmap(
          *id,
          size,
          *requestedSize,
          *options));
}

//  QQuickTextureFactory
//      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return self->requestTexture(*id, size, *requestedSize, *options);
}

//  QQuickImageResponse
//      *QQuickImageProviderWithOptions::requestImageResponse(const QString
//      &id, const QSize &requestedSize, const QQuickImageProviderOptions
//      &options)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QStringRK5QSizeRK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return self->requestImageResponse(*id, *requestedSize, *options);
}

//  QSize QQuickImageProviderWithOptions::loadSize(const QSize &originalSize,
//      const QSize &requestedSize, const QByteArray &format, const
//      QQuickImageProviderOptions &options, qreal devicePixelRatio)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN30QQuickImageProviderWithOptions8loadSizeERK5QSizeS2_RK10QByteArrayRK26QQuickImageProviderOptionsd(
    const QSize *originalSize,
    const QSize *requestedSize,
    const QByteArray *format,
    const QQuickImageProviderOptions *options,
    qreal devicePixelRatio) {
  return new QSize(
      QQuickImageProviderWithOptions::loadSize(
          *originalSize,
          *requestedSize,
          *format,
          *options,
          devicePixelRatio));
}

//  QQuickImageProviderWithOptions
//      *QQuickImageProviderWithOptions::checkedCast(QQuickImageProvider
//      *provider)
extern "C" Q_DECL_EXPORT
QQuickImageProviderWithOptions *ritual_ZN30QQuickImageProviderWithOptions11checkedCastEP19QQuickImageProvider(
    QQuickImageProvider *provider) {
  return QQuickImageProviderWithOptions::checkedCast(provider);
}

//  a Python function taken by a CuteQQuickImageProviderWithOptions, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageProviderWithOptions(
    QQuickImageProviderWithOptions *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageProviderWithOptions *>(self)->take(key, call);
}

//  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(
      self->QQuickImageProviderWithOptions::requestImage(
          *id,
          size,
          *requestedSize));
}

//  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QPixmap(
      self->QQuickImageProviderWithOptions::requestPixmap(
          *id,
          size,
          *requestedSize));
}

//  QQuickTextureFactory
//      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
//      QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_own_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP5QSizeRKS3_(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return self->QQuickImageProviderWithOptions::requestTexture(
      *id,
      size,
      *requestedSize);
}

//  QQuickImageResponse
//      *QQuickImageProviderWithOptions::requestImageResponse(const QString
//      &id, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_own_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QStringRK5QSize(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    const QSize *requestedSize) {
  return self->QQuickImageProviderWithOptions::requestImageResponse(
      *id,
      *requestedSize);
}

//  QImage QQuickImageProviderWithOptions::requestImage(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QImage(
      self->QQuickImageProviderWithOptions::requestImage(
          *id,
          size,
          *requestedSize,
          *options));
}

//  QPixmap QQuickImageProviderWithOptions::requestPixmap(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN30QQuickImageProviderWithOptions13requestPixmapERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QPixmap(
      self->QQuickImageProviderWithOptions::requestPixmap(
          *id,
          size,
          *requestedSize,
          *options));
}

//  QQuickTextureFactory
//      *QQuickImageProviderWithOptions::requestTexture(const QString &id,
//      QSize *size, const QSize &requestedSize, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_own_ZN30QQuickImageProviderWithOptions14requestTextureERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return self->QQuickImageProviderWithOptions::requestTexture(
      *id,
      size,
      *requestedSize,
      *options);
}

//  QQuickImageResponse
//      *QQuickImageProviderWithOptions::requestImageResponse(const QString
//      &id, const QSize &requestedSize, const QQuickImageProviderOptions
//      &options)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_own_ZN30QQuickImageProviderWithOptions20requestImageResponseERK7QStringRK5QSizeRK26QQuickImageProviderOptions(
    QQuickImageProviderWithOptions *self,
    const QString *id,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return self->QQuickImageProviderWithOptions::requestImageResponse(
      *id,
      *requestedSize,
      *options);
}
