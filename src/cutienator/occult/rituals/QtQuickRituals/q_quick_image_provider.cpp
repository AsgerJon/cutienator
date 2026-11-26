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

//  A QQuickImageProvider that Python can take functions over in. Every QQuickImageProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickImageProviderCall0)(const void *, int *);
typedef int (*CuteQQuickImageProviderCall1)(const void *, int *);
typedef const QImage * (*CuteQQuickImageProviderCall2)(const void *, const QString *, QSize *, const QSize *, int *);
typedef const QPixmap * (*CuteQQuickImageProviderCall3)(const void *, const QString *, QSize *, const QSize *, int *);
typedef void * (*CuteQQuickImageProviderCall4)(const void *, const QString *, QSize *, const QSize *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageProviderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageProviderCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageProviderCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageProvider : public QQuickImageProvider {
public:
  using QQuickImageProvider::QQuickImageProvider;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase9imageTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase5flagsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_")) {
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

  //  ImageType QQuickImageProvider::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageProviderCall0 call = reinterpret_cast<CuteQQuickImageProviderCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return QQuickImageProvider::imageType();
  }

  //  Flags QQuickImageProvider::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageProviderCall1 call = reinterpret_cast<CuteQQuickImageProviderCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageProviderCall2 call = reinterpret_cast<CuteQQuickImageProviderCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageProviderCall3 call = reinterpret_cast<CuteQQuickImageProviderCall3>(taken[3]);
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
      CuteQQuickImageProviderCall4 call = reinterpret_cast<CuteQQuickImageProviderCall4>(taken[4]);
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
      CuteQQuickImageProviderCall5 call = reinterpret_cast<CuteQQuickImageProviderCall5>(taken[5]);
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
      CuteQQuickImageProviderCall6 call = reinterpret_cast<CuteQQuickImageProviderCall6>(taken[6]);
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
      CuteQQuickImageProviderCall7 call = reinterpret_cast<CuteQQuickImageProviderCall7>(taken[7]);
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
      CuteQQuickImageProviderCall8 call = reinterpret_cast<CuteQQuickImageProviderCall8>(taken[8]);
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
      CuteQQuickImageProviderCall9 call = reinterpret_cast<CuteQQuickImageProviderCall9>(taken[9]);
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
      CuteQQuickImageProviderCall10 call = reinterpret_cast<CuteQQuickImageProviderCall10>(taken[10]);
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
      CuteQQuickImageProviderCall11 call = reinterpret_cast<CuteQQuickImageProviderCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickImageProvider10metaObjectEv(
    const QQuickImageProvider *self) {
  return self->metaObject();
}

//  void *QQuickImageProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickImageProvider11qt_metacastEPKc(
    QQuickImageProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageProvider::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickImageProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickImageProvider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickImageProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageProvider::tr(s, c, n));
}

//  QQuickImageProvider::QQuickImageProvider(ImageType type, Flags flags)
extern "C" Q_DECL_EXPORT
QQuickImageProvider *ritual_ZN19QQuickImageProviderC1EN21QQmlImageProviderBase9ImageTypeE6QFlagsINS0_4FlagEE(
    QQmlImageProviderBase::ImageType type,
    int flags) {
  return new CuteQQuickImageProvider(
      type,
      QFlags<QQmlImageProviderBase::Flag>::fromInt(flags));
}

//  QQuickImageProvider::~QQuickImageProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickImageProviderD1Ev(QQuickImageProvider *self) {
  delete self;
}

//  ImageType QQuickImageProvider::imageType() const
extern "C" Q_DECL_EXPORT
QQmlImageProviderBase::ImageType ritual_ZNK19QQuickImageProvider9imageTypeEv(
    const QQuickImageProvider *self) {
  return self->imageType();
}

//  Flags QQuickImageProvider::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickImageProvider5flagsEv(
    const QQuickImageProvider *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QImage QQuickImageProvider::requestImage(const QString &id, QSize *size,
//      const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(self->requestImage(*id, size, *requestedSize));
}

//  QPixmap QQuickImageProvider::requestPixmap(const QString &id, QSize
//      *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QPixmap(self->requestPixmap(*id, size, *requestedSize));
}

//  QQuickTextureFactory *QQuickImageProvider::requestTexture(const QString
//      &id, QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return self->requestTexture(*id, size, *requestedSize);
}

//  a Python function taken by a CuteQQuickImageProvider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageProvider(
    QQuickImageProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageProvider *>(self)->take(key, call);
}

//  ImageType QQuickImageProvider::imageType() const
extern "C" Q_DECL_EXPORT
QQmlImageProviderBase::ImageType ritual_own_ZNK19QQuickImageProvider9imageTypeEv(
    const QQuickImageProvider *self) {
  return self->QQuickImageProvider::imageType();
}

//  Flags QQuickImageProvider::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickImageProvider5flagsEv(
    const QQuickImageProvider *self) {
  return static_cast<int>(self->QQuickImageProvider::flags().toInt());
}

//  QImage QQuickImageProvider::requestImage(const QString &id, QSize *size,
//      const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN19QQuickImageProvider12requestImageERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QImage(
      self->QQuickImageProvider::requestImage(
          *id,
          size,
          *requestedSize));
}

//  QPixmap QQuickImageProvider::requestPixmap(const QString &id, QSize
//      *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN19QQuickImageProvider13requestPixmapERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return new QPixmap(
      self->QQuickImageProvider::requestPixmap(
          *id,
          size,
          *requestedSize));
}

//  QQuickTextureFactory *QQuickImageProvider::requestTexture(const QString
//      &id, QSize *size, const QSize &requestedSize)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_own_ZN19QQuickImageProvider14requestTextureERK7QStringP5QSizeRKS3_(
    QQuickImageProvider *self,
    const QString *id,
    QSize *size,
    const QSize *requestedSize) {
  return self->QQuickImageProvider::requestTexture(
      *id,
      size,
      *requestedSize);
}
