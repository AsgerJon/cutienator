//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebEngineFaviconDBProvider that Python can take functions over in. Every QQuickWebEngineFaviconDBProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickWebEngineFaviconDBProviderCall0)(const void *, int *);
typedef void * (*CuteQQuickWebEngineFaviconDBProviderCall1)(const void *, const QString *, const QSize *, int *);
typedef int (*CuteQQuickWebEngineFaviconDBProviderCall2)(const void *, int *);
typedef int (*CuteQQuickWebEngineFaviconDBProviderCall3)(const void *, int *);
typedef const QImage * (*CuteQQuickWebEngineFaviconDBProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteQQuickWebEngineFaviconDBProviderCall5)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickWebEngineFaviconDBProviderCall6)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFaviconDBProviderCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFaviconDBProviderCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconDBProviderCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconDBProviderCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconDBProviderCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconDBProviderCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconDBProviderCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineFaviconDBProvider : public QQuickWebEngineFaviconDBProvider {
public:
  using QQuickWebEngineFaviconDBProvider::QQuickWebEngineFaviconDBProvider;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickAsyncImageProvider20requestImageResponseERK7QStringRK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase9imageTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase5flagsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickWebEngineFaviconDBProvider::isIconUrl() const
  bool isIconUrl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall0 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickWebEngineFaviconDBProvider::isIconUrl();
  }

  //  QQuickImageResponse
  //      *QQuickWebEngineFaviconProvider::requestImageResponse(const
  //      QString &id, const QSize &requestedSize)
  QQuickImageResponse *requestImageResponse(
      const QString &id,
      const QSize &requestedSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall1 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall1>(taken[1]);
      void * given = call(this, &id, &requestedSize, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickWebEngineFaviconProvider::requestImageResponse(id, requestedSize);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall2 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall3 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall4 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall5 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall6 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall6>(taken[6]);
      void * given = call(this, &id, size, &requestedSize, &handled);
      if (handled) return static_cast<QQuickTextureFactory *>(given);
    }
    return QQuickImageProvider::requestTexture(id, size, requestedSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall7 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall8 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall9 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall10 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall11 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall12 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconDBProviderCall13 call = reinterpret_cast<CuteQQuickWebEngineFaviconDBProviderCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineFaviconDBProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickWebEngineFaviconDBProvider10metaObjectEv(
    const QQuickWebEngineFaviconDBProvider *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineFaviconDBProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickWebEngineFaviconDBProvider11qt_metacastEPKc(
    QQuickWebEngineFaviconDBProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineFaviconDBProvider::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickWebEngineFaviconDBProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineFaviconDBProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineFaviconDBProvider::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickWebEngineFaviconDBProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineFaviconDBProvider::tr(s, c, n));
}

//  QString QQuickWebEngineFaviconDBProvider::identifier()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickWebEngineFaviconDBProvider10identifierEv() {
  return new QString(QQuickWebEngineFaviconDBProvider::identifier());
}

//  QUrl QQuickWebEngineFaviconDBProvider::faviconProviderUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN32QQuickWebEngineFaviconDBProvider18faviconProviderUrlERK4QUrl(
    const QUrl *a0) {
  return new QUrl(QQuickWebEngineFaviconDBProvider::faviconProviderUrl(*a0));
}

//  QQuickWebEngineFaviconDBProvider::QQuickWebEngineFaviconDBProvider()
extern "C" Q_DECL_EXPORT
QQuickWebEngineFaviconDBProvider *ritual_ZN32QQuickWebEngineFaviconDBProviderC1Ev() {
  return new CuteQQuickWebEngineFaviconDBProvider();
}

//  bool QQuickWebEngineFaviconDBProvider::isIconUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickWebEngineFaviconDBProvider9isIconUrlEv(
    const QQuickWebEngineFaviconDBProvider *self) {
  return self->isIconUrl();
}

//  a Python function taken by a CuteQQuickWebEngineFaviconDBProvider, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineFaviconDBProvider(
    QQuickWebEngineFaviconDBProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineFaviconDBProvider *>(self)->take(key, call);
}

//  bool QQuickWebEngineFaviconDBProvider::isIconUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK32QQuickWebEngineFaviconDBProvider9isIconUrlEv(
    const QQuickWebEngineFaviconDBProvider *self) {
  return self->QQuickWebEngineFaviconDBProvider::isIconUrl();
}
