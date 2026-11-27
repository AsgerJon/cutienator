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
#include <QtCore/QPointer>

//  A QQuickWebEngineFaviconProvider that Python can take functions over in. Every QQuickWebEngineFaviconProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickWebEngineFaviconProviderCall0)(const void *, int *);
typedef void * (*CuteQQuickWebEngineFaviconProviderCall1)(const void *, const QString *, const QSize *, int *);
typedef int (*CuteQQuickWebEngineFaviconProviderCall2)(const void *, int *);
typedef int (*CuteQQuickWebEngineFaviconProviderCall3)(const void *, int *);
typedef const QImage * (*CuteQQuickWebEngineFaviconProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteQQuickWebEngineFaviconProviderCall5)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickWebEngineFaviconProviderCall6)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFaviconProviderCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFaviconProviderCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconProviderCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconProviderCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconProviderCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconProviderCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFaviconProviderCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineFaviconProvider : public QQuickWebEngineFaviconProvider {
public:
  using QQuickWebEngineFaviconProvider::QQuickWebEngineFaviconProvider;
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

  //  bool QQuickWebEngineFaviconProvider::isIconUrl() const
  bool isIconUrl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconProviderCall0 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickWebEngineFaviconProvider::isIconUrl();
  }

  //  QQuickImageResponse
  //      *QQuickWebEngineFaviconProvider::requestImageResponse(const
  //      QString &id, const QSize &requestedSize)
  QQuickImageResponse *requestImageResponse(
      const QString &id,
      const QSize &requestedSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconProviderCall1 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall1>(taken[1]);
      void * given = call(this, &id, &requestedSize, &handled);
      if (handled) return static_cast<QQuickImageResponse *>(given);
    }
    return QQuickWebEngineFaviconProvider::requestImageResponse(id, requestedSize);
  }

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconProviderCall2 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWebEngineFaviconProviderCall3 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall3>(taken[3]);
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
      CuteQQuickWebEngineFaviconProviderCall4 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall4>(taken[4]);
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
      CuteQQuickWebEngineFaviconProviderCall5 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall5>(taken[5]);
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
      CuteQQuickWebEngineFaviconProviderCall6 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall6>(taken[6]);
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
      CuteQQuickWebEngineFaviconProviderCall7 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall7>(taken[7]);
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
      CuteQQuickWebEngineFaviconProviderCall8 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall8>(taken[8]);
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
      CuteQQuickWebEngineFaviconProviderCall9 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall9>(taken[9]);
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
      CuteQQuickWebEngineFaviconProviderCall10 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall10>(taken[10]);
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
      CuteQQuickWebEngineFaviconProviderCall11 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall11>(taken[11]);
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
      CuteQQuickWebEngineFaviconProviderCall12 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall12>(taken[12]);
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
      CuteQQuickWebEngineFaviconProviderCall13 call = reinterpret_cast<CuteQQuickWebEngineFaviconProviderCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineFaviconProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuickWebEngineFaviconProvider10metaObjectEv(
    const QQuickWebEngineFaviconProvider *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineFaviconProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QQuickWebEngineFaviconProvider11qt_metacastEPKc(
    QQuickWebEngineFaviconProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineFaviconProvider::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QQuickWebEngineFaviconProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineFaviconProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineFaviconProvider::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuickWebEngineFaviconProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineFaviconProvider::tr(s, c, n));
}

//  QString QQuickWebEngineFaviconProvider::identifier()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQuickWebEngineFaviconProvider10identifierEv() {
  return new QString(QQuickWebEngineFaviconProvider::identifier());
}

//  QUrl QQuickWebEngineFaviconProvider::faviconProviderUrlBase(const QUrl
//      &a0, const QString &identifier)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN30QQuickWebEngineFaviconProvider22faviconProviderUrlBaseERK4QUrlRK7QString(
    const QUrl *a0,
    const QString *identifier) {
  return new QUrl(
      QQuickWebEngineFaviconProvider::faviconProviderUrlBase(
          *a0,
          *identifier));
}

//  QUrl QQuickWebEngineFaviconProvider::faviconProviderUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN30QQuickWebEngineFaviconProvider18faviconProviderUrlERK4QUrl(
    const QUrl *a0) {
  return new QUrl(QQuickWebEngineFaviconProvider::faviconProviderUrl(*a0));
}

//  QQuickWebEngineFaviconProvider::QQuickWebEngineFaviconProvider()
extern "C" Q_DECL_EXPORT
QQuickWebEngineFaviconProvider *ritual_ZN30QQuickWebEngineFaviconProviderC1Ev() {
  return new CuteQQuickWebEngineFaviconProvider();
}

//  bool QQuickWebEngineFaviconProvider::isIconUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv(
    const QQuickWebEngineFaviconProvider *self) {
  return self->isIconUrl();
}

//  QQuickImageResponse
//      *QQuickWebEngineFaviconProvider::requestImageResponse(const QString
//      &id, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_ZN30QQuickWebEngineFaviconProvider20requestImageResponseERK7QStringRK5QSize(
    QQuickWebEngineFaviconProvider *self,
    const QString *id,
    const QSize *requestedSize) {
  return self->requestImageResponse(*id, *requestedSize);
}

//  void QQuickWebEngineFaviconProvider::imageResponseRequested(QPointer<Favi
//      conImageResponse> faviconResponse)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickWebEngineFaviconProvider22imageResponseRequestedE8QPointerI20FaviconImageResponseE(
    QQuickWebEngineFaviconProvider *self,
    const QPointer<FaviconImageResponse> *faviconResponse) {
  self->imageResponseRequested(*faviconResponse);
}

//  a Python function taken by a CuteQQuickWebEngineFaviconProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineFaviconProvider(
    QQuickWebEngineFaviconProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineFaviconProvider *>(self)->take(key, call);
}

//  bool QQuickWebEngineFaviconProvider::isIconUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QQuickWebEngineFaviconProvider9isIconUrlEv(
    const QQuickWebEngineFaviconProvider *self) {
  return self->QQuickWebEngineFaviconProvider::isIconUrl();
}

//  QQuickImageResponse
//      *QQuickWebEngineFaviconProvider::requestImageResponse(const QString
//      &id, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickImageResponse *ritual_own_ZN30QQuickWebEngineFaviconProvider20requestImageResponseERK7QStringRK5QSize(
    QQuickWebEngineFaviconProvider *self,
    const QString *id,
    const QSize *requestedSize) {
  return self->QQuickWebEngineFaviconProvider::requestImageResponse(
      *id,
      *requestedSize);
}
