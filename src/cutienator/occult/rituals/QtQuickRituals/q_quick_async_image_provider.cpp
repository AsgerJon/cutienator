//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickimageprovider.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickAsyncImageProvider that Python can take functions over in. Every QQuickAsyncImageProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickAsyncImageProviderCall0)(const void *, const QString *, const QSize *, int *);
typedef int (*CuteQQuickAsyncImageProviderCall1)(const void *, int *);
typedef int (*CuteQQuickAsyncImageProviderCall2)(const void *, int *);
typedef const QImage * (*CuteQQuickAsyncImageProviderCall3)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteQQuickAsyncImageProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickAsyncImageProviderCall5)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAsyncImageProviderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAsyncImageProviderCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAsyncImageProviderCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAsyncImageProviderCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAsyncImageProviderCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAsyncImageProviderCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAsyncImageProviderCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAsyncImageProvider : public QQuickAsyncImageProvider {
public:
  using QQuickAsyncImageProvider::QQuickAsyncImageProvider;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringRK5QSize")) {
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
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QQuickImageResponse
  //      *QQuickAsyncImageProvider::requestImageResponse(const QString
  //      &id, const QSize &requestedSize)
  QQuickImageResponse *requestImageResponse(
      const QString &id,
      const QSize &requestedSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall0 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall0>(taken[0]);
      void * given = call(this, &id, &requestedSize, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return {};
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall1 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall2 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQmlImageProviderBase::Flag>::fromInt(given);
    }
    return QQuickImageProvider::flags();
  }

  //  QImage QQuickImageProvider::requestImage(const QString &id, QSize
  //      *size, const QSize &requestedSize)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall3 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall3>(taken[3]);
      const QImage * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickImageProvider::requestImage(id, size, requestedSize);
  }

  //  QPixmap QQuickImageProvider::requestPixmap(const QString &id, QSize
  //      *size, const QSize &requestedSize)
  QPixmap requestPixmap(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall4 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall5 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall5>(taken[5]);
      void * given = call(this, &id, size, &requestedSize, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QQuickImageProvider::requestTexture(id, size, requestedSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall6 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall7 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall8 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall9 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall10 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall11 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAsyncImageProviderCall12 call = reinterpret_cast<CuteQQuickAsyncImageProviderCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QQuickAsyncImageProvider::QQuickAsyncImageProvider()
extern "C" Q_DECL_EXPORT
QQuickAsyncImageProvider *ritual_ZN24QQuickAsyncImageProviderC1Ev() {
  return new CuteQQuickAsyncImageProvider();
}

//  QQuickAsyncImageProvider::~QQuickAsyncImageProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAsyncImageProviderD1Ev(
    QQuickAsyncImageProvider *self) {
  delete self;
}

//  QQuickImageResponse *QQuickAsyncImageProvider::requestImageResponse(const
//      QString &id, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringRK5QSize(
    QQuickAsyncImageProvider *self,
    const QString *id,
    const QSize *requestedSize) {
  return self->requestImageResponse(*id, *requestedSize);
}

//  a Python function taken by a CuteQQuickAsyncImageProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAsyncImageProvider(
    QQuickAsyncImageProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAsyncImageProvider *>(self)->take(key, call);
}
