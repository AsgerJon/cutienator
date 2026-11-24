//  Written by dev_tooling.RitualGenerator from the records of QtLabsSharedIm
//  age/6.12.0/QtLabsSharedImage/private/qsharedimageprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qtlabssharedimageglobal_p.h>
#include <QtLabsSharedImage/QtLabsSharedImage>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qsharedimageprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A SharedImageProvider that Python can take functions over in. Every SharedImageProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteSharedImageProviderCall0)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef const QImage * (*CuteSharedImageProviderCall1)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteSharedImageProviderCall2)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteSharedImageProviderCall3)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteSharedImageProviderCall4)(const void *, const QString *, const QSize *, int *);
typedef const QPixmap * (*CuteSharedImageProviderCall5)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef void * (*CuteSharedImageProviderCall6)(const void *, const QString *, QSize *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef void * (*CuteSharedImageProviderCall7)(const void *, const QString *, const QSize *, const QQuickImageProviderOptions *, int *);
typedef int (*CuteSharedImageProviderCall8)(const void *, int *);
typedef int (*CuteSharedImageProviderCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSharedImageProviderCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSharedImageProviderCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSharedImageProviderCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSharedImageProviderCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSharedImageProviderCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSharedImageProviderCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSharedImageProviderCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSharedImageProvider : public SharedImageProvider {
public:
  using SharedImageProvider::SharedImageProvider;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuickImageProviderWithOptions12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringRK5QSize")) {
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

  //  QImage SharedImageProvider::requestImage(const QString &id, QSize
  //      *size, const QSize &requestedSize, const
  //      QQuickImageProviderOptions &options)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize,
      const QQuickImageProviderOptions &options) override {
    if (taken[0]) {
      int handled = 0;
      CuteSharedImageProviderCall0 call = reinterpret_cast<CuteSharedImageProviderCall0>(taken[0]);
      const QImage * given = call(this, &id, size, &requestedSize, &options, &handled);
      if (handled && given) return *given;
    }
    return SharedImageProvider::requestImage(id, size, requestedSize, options);
  }

  //  QImage QQuickImageProviderWithOptions::requestImage(const QString
  //      &id, QSize *size, const QSize &requestedSize)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteSharedImageProviderCall1 call = reinterpret_cast<CuteSharedImageProviderCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteSharedImageProviderCall2 call = reinterpret_cast<CuteSharedImageProviderCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteSharedImageProviderCall3 call = reinterpret_cast<CuteSharedImageProviderCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteSharedImageProviderCall4 call = reinterpret_cast<CuteSharedImageProviderCall4>(taken[4]);
      void * given = call(this, &id, &requestedSize, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickImageProviderWithOptions::requestImageResponse(id, requestedSize);
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
      CuteSharedImageProviderCall5 call = reinterpret_cast<CuteSharedImageProviderCall5>(taken[5]);
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
      CuteSharedImageProviderCall6 call = reinterpret_cast<CuteSharedImageProviderCall6>(taken[6]);
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
      CuteSharedImageProviderCall7 call = reinterpret_cast<CuteSharedImageProviderCall7>(taken[7]);
      void * given = call(this, &id, &requestedSize, &options, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickImageProviderWithOptions::requestImageResponse(id, requestedSize, options);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteSharedImageProviderCall8 call = reinterpret_cast<CuteSharedImageProviderCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[9]) {
      int handled = 0;
      CuteSharedImageProviderCall9 call = reinterpret_cast<CuteSharedImageProviderCall9>(taken[9]);
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
      CuteSharedImageProviderCall10 call = reinterpret_cast<CuteSharedImageProviderCall10>(taken[10]);
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
      CuteSharedImageProviderCall11 call = reinterpret_cast<CuteSharedImageProviderCall11>(taken[11]);
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
      CuteSharedImageProviderCall12 call = reinterpret_cast<CuteSharedImageProviderCall12>(taken[12]);
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
      CuteSharedImageProviderCall13 call = reinterpret_cast<CuteSharedImageProviderCall13>(taken[13]);
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
      CuteSharedImageProviderCall14 call = reinterpret_cast<CuteSharedImageProviderCall14>(taken[14]);
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
      CuteSharedImageProviderCall15 call = reinterpret_cast<CuteSharedImageProviderCall15>(taken[15]);
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
      CuteSharedImageProviderCall16 call = reinterpret_cast<CuteSharedImageProviderCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  SharedImageProvider::SharedImageProvider()
extern "C" Q_DECL_EXPORT
SharedImageProvider *ritual_ZN19SharedImageProviderC1Ev() {
  return new CuteSharedImageProvider();
}

//  QImage SharedImageProvider::requestImage(const QString &id, QSize *size,
//      const QSize &requestedSize, const QQuickImageProviderOptions
//      &options)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19SharedImageProvider12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    SharedImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QImage(self->requestImage(*id, size, *requestedSize, *options));
}

//  a Python function taken by a CuteSharedImageProvider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SharedImageProvider(
    SharedImageProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteSharedImageProvider *>(self)->take(key, call);
}

//  QImage SharedImageProvider::requestImage(const QString &id, QSize *size,
//      const QSize &requestedSize, const QQuickImageProviderOptions
//      &options)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19SharedImageProvider12requestImageERK7QStringP5QSizeRKS3_RK26QQuickImageProviderOptions(
    SharedImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize,
    const QQuickImageProviderOptions *options) {
  return new QImage(
      self->SharedImageProvider::requestImage(
          *id,
          size,
          *requestedSize,
          *options));
}
