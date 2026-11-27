//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginetouchhandleprovider_p_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginetouchhandleprovider_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQuickWebEngineTouchHandleProvider that Python can take functions over in. Every QQuickWebEngineTouchHandleProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteQQuickWebEngineTouchHandleProviderCall0)(const void *, const QString *, QSize *, const QSize *, int *);
typedef int (*CuteQQuickWebEngineTouchHandleProviderCall1)(const void *, int *);
typedef int (*CuteQQuickWebEngineTouchHandleProviderCall2)(const void *, int *);
typedef const QPixmap * (*CuteQQuickWebEngineTouchHandleProviderCall3)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickWebEngineTouchHandleProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineTouchHandleProviderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineTouchHandleProviderCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTouchHandleProviderCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTouchHandleProviderCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTouchHandleProviderCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTouchHandleProviderCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTouchHandleProviderCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineTouchHandleProvider : public QQuickWebEngineTouchHandleProvider {
public:
  using QQuickWebEngineTouchHandleProvider::QQuickWebEngineTouchHandleProvider;
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

  //  QImage QQuickWebEngineTouchHandleProvider::requestImage(const QString
  //      &id, QSize *size, const QSize &requestedSize)
  QImage requestImage(
      const QString &id,
      QSize *size,
      const QSize &requestedSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineTouchHandleProviderCall0 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall0>(taken[0]);
      const QImage * given = call(this, &id, size, &requestedSize, &handled);
      if (handled && given) return *given;
    }
    return QQuickWebEngineTouchHandleProvider::requestImage(id, size, requestedSize);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineTouchHandleProviderCall1 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineTouchHandleProviderCall2 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall2>(taken[2]);
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
      CuteQQuickWebEngineTouchHandleProviderCall3 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall3>(taken[3]);
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
      CuteQQuickWebEngineTouchHandleProviderCall4 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall4>(taken[4]);
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
      CuteQQuickWebEngineTouchHandleProviderCall5 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall5>(taken[5]);
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
      CuteQQuickWebEngineTouchHandleProviderCall6 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall6>(taken[6]);
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
      CuteQQuickWebEngineTouchHandleProviderCall7 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall7>(taken[7]);
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
      CuteQQuickWebEngineTouchHandleProviderCall8 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall8>(taken[8]);
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
      CuteQQuickWebEngineTouchHandleProviderCall9 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall9>(taken[9]);
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
      CuteQQuickWebEngineTouchHandleProviderCall10 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall10>(taken[10]);
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
      CuteQQuickWebEngineTouchHandleProviderCall11 call = reinterpret_cast<CuteQQuickWebEngineTouchHandleProviderCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QString QQuickWebEngineTouchHandleProvider::identifier()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN34QQuickWebEngineTouchHandleProvider10identifierEv() {
  return new QString(QQuickWebEngineTouchHandleProvider::identifier());
}

//  QUrl QQuickWebEngineTouchHandleProvider::url(int orientation)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN34QQuickWebEngineTouchHandleProvider3urlEi(int orientation) {
  return new QUrl(QQuickWebEngineTouchHandleProvider::url(orientation));
}

//  QQuickWebEngineTouchHandleProvider::QQuickWebEngineTouchHandleProvider()
extern "C" Q_DECL_EXPORT
QQuickWebEngineTouchHandleProvider *ritual_ZN34QQuickWebEngineTouchHandleProviderC1Ev() {
  return new CuteQQuickWebEngineTouchHandleProvider();
}

//  QQuickWebEngineTouchHandleProvider::~QQuickWebEngineTouchHandleProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuickWebEngineTouchHandleProviderD1Ev(
    QQuickWebEngineTouchHandleProvider *self) {
  delete self;
}

//  void QQuickWebEngineTouchHandleProvider::init(const QMap<int, QImage>
//      &images)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuickWebEngineTouchHandleProvider4initERK4QMapIi6QImageE(
    QQuickWebEngineTouchHandleProvider *self,
    const QMap<int, QImage> *images) {
  self->init(*images);
}

//  QImage QQuickWebEngineTouchHandleProvider::requestImage(const QString
//      &id, QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN34QQuickWebEngineTouchHandleProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickWebEngineTouchHandleProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(self->requestImage(*id, size, *requestedSize));
}

//  a Python function taken by a CuteQQuickWebEngineTouchHandleProvider, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineTouchHandleProvider(
    QQuickWebEngineTouchHandleProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineTouchHandleProvider *>(self)->take(key, call);
}

//  QImage QQuickWebEngineTouchHandleProvider::requestImage(const QString
//      &id, QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN34QQuickWebEngineTouchHandleProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickWebEngineTouchHandleProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(
      self->QQuickWebEngineTouchHandleProvider::requestImage(
          *id,
          size,
          *requestedSize));
}
