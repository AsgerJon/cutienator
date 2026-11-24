//  Written by dev_tooling.RitualGenerator from the records of QtMultimediaQu
//  ick/6.12.0/QtMultimediaQuick/private/qquickimagepreviewprovider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickimagepreviewprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/quuid.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickImagePreviewProvider that Python can take functions over in. Every QQuickImagePreviewProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteQQuickImagePreviewProviderCall0)(const void *, const QString *, QSize *, const QSize *, int *);
typedef int (*CuteQQuickImagePreviewProviderCall1)(const void *, int *);
typedef int (*CuteQQuickImagePreviewProviderCall2)(const void *, int *);
typedef const QPixmap * (*CuteQQuickImagePreviewProviderCall3)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickImagePreviewProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImagePreviewProviderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImagePreviewProviderCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImagePreviewProviderCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImagePreviewProviderCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImagePreviewProviderCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImagePreviewProviderCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImagePreviewProviderCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImagePreviewProvider : public QQuickImagePreviewProvider {
public:
  using QQuickImagePreviewProvider::QQuickImagePreviewProvider;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase9imageTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase5flagsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QImage QQuickImagePreviewProvider::requestImage(const QString &id,
  //      QSize *size, const QSize &requestedSize)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall0 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall0>(taken[0]);
      const QImage * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickImagePreviewProvider::requestImage(id, size, requestedSize);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall1 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall2 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQmlImageProviderBase::Flag>::fromInt(given);
    }
    return QQuickImageProvider::flags();
  }

  //  QPixmap QQuickImageProvider::requestPixmap(const QString &id, QSize
  //      *size, const QSize &requestedSize)
  QPixmap requestPixmap(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall3 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall3>(taken[3]);
      const QPixmap * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProvider::requestPixmap(id, size, requestedSize);
  }

  //  QQuickTextureFactory *QQuickImageProvider::requestTexture(const
  //      QString &id, QSize *size, const QSize &requestedSize)
  QQuickTextureFactory *requestTexture(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall4 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall4>(taken[4]);
      void * given = call(this, &id, size, &requestedSize, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QQuickImageProvider::requestTexture(id, size, requestedSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall5 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall6 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall7 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall8 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall9 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall10 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickImagePreviewProviderCall11 call = reinterpret_cast<CuteQQuickImagePreviewProviderCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QQuickImagePreviewProvider::QQuickImagePreviewProvider()
extern "C" Q_DECL_EXPORT
QQuickImagePreviewProvider *ritual_ZN26QQuickImagePreviewProviderC1Ev() {
  return new CuteQQuickImagePreviewProvider();
}

//  QQuickImagePreviewProvider::~QQuickImagePreviewProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImagePreviewProviderD1Ev(
    QQuickImagePreviewProvider *self) {
  delete self;
}

//  QImage QQuickImagePreviewProvider::requestImage(const QString &id, QSize
//      *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN26QQuickImagePreviewProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImagePreviewProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(self->requestImage(*id, size, *requestedSize));
}

//  void QQuickImagePreviewProvider::registerPreview(QUuid captureInstance,
//      QString id, QImage a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImagePreviewProvider15registerPreviewE5QUuid7QString6QImage(
    const QUuid *captureInstance,
    const QString *id,
    const QImage *a2) {
  QQuickImagePreviewProvider::registerPreview(*captureInstance, *id, *a2);
}

//  void QQuickImagePreviewProvider::cleanupInstance(QUuid captureInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImagePreviewProvider15cleanupInstanceE5QUuid(
    const QUuid *captureInstance) {
  QQuickImagePreviewProvider::cleanupInstance(*captureInstance);
}

//  a Python function taken by a CuteQQuickImagePreviewProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImagePreviewProvider(
    QQuickImagePreviewProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImagePreviewProvider *>(self)->take(key, call);
}

//  QImage QQuickImagePreviewProvider::requestImage(const QString &id, QSize
//      *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN26QQuickImagePreviewProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImagePreviewProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(
      self->QQuickImagePreviewProvider::requestImage(
          *id,
          size,
          *requestedSize));
}
