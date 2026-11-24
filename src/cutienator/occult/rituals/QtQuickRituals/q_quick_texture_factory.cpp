//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickimageprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickimageprovider.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickTextureFactory that Python can take functions over in. Every QQuickTextureFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickTextureFactoryCall0)(const void *, QQuickWindow *, int *);
typedef const QSize * (*CuteQQuickTextureFactoryCall1)(const void *, int *);
typedef int (*CuteQQuickTextureFactoryCall2)(const void *, int *);
typedef const QImage * (*CuteQQuickTextureFactoryCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextureFactoryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextureFactoryCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextureFactoryCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextureFactoryCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextureFactoryCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextureFactoryCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextureFactoryCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextureFactory : public QQuickTextureFactory {
public:
  using QQuickTextureFactory::QQuickTextureFactory;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory13createTextureEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory11textureSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory16textureByteCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory5imageEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGTexture *QQuickTextureFactory::createTexture(QQuickWindow *window)
  //      const
  QSGTexture *createTexture(QQuickWindow *window) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall0 call = reinterpret_cast<CuteQQuickTextureFactoryCall0>(taken[0]);
      void * given = call(this, window, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }

  //  QSize QQuickTextureFactory::textureSize() const
  QSize textureSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall1 call = reinterpret_cast<CuteQQuickTextureFactoryCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QQuickTextureFactory::textureByteCount() const
  int textureByteCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall2 call = reinterpret_cast<CuteQQuickTextureFactoryCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QImage QQuickTextureFactory::image() const
  QImage image() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall3 call = reinterpret_cast<CuteQQuickTextureFactoryCall3>(taken[3]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextureFactory::image();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall4 call = reinterpret_cast<CuteQQuickTextureFactoryCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall5 call = reinterpret_cast<CuteQQuickTextureFactoryCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall6 call = reinterpret_cast<CuteQQuickTextureFactoryCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall7 call = reinterpret_cast<CuteQQuickTextureFactoryCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall8 call = reinterpret_cast<CuteQQuickTextureFactoryCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall9 call = reinterpret_cast<CuteQQuickTextureFactoryCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextureFactoryCall10 call = reinterpret_cast<CuteQQuickTextureFactoryCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextureFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickTextureFactory10metaObjectEv(
    const QQuickTextureFactory *self) {
  return self->metaObject();
}

//  QString QQuickTextureFactory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickTextureFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextureFactory::tr(s, c, n));
}

//  QQuickTextureFactory::~QQuickTextureFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextureFactoryD1Ev(QQuickTextureFactory *self) {
  delete self;
}

//  QSGTexture *QQuickTextureFactory::createTexture(QQuickWindow *window)
//      const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK20QQuickTextureFactory13createTextureEP12QQuickWindow(
    const QQuickTextureFactory *self,
    QQuickWindow *window) {
  return self->createTexture(window);
}

//  QSize QQuickTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QQuickTextureFactory11textureSizeEv(
    const QQuickTextureFactory *self) {
  return new QSize(self->textureSize());
}

//  int QQuickTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickTextureFactory16textureByteCountEv(
    const QQuickTextureFactory *self) {
  return self->textureByteCount();
}

//  QImage QQuickTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK20QQuickTextureFactory5imageEv(
    const QQuickTextureFactory *self) {
  return new QImage(self->image());
}

//  QQuickTextureFactory *QQuickTextureFactory::textureFactoryForImage(const
//      QImage &image)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN20QQuickTextureFactory22textureFactoryForImageERK6QImage(
    const QImage *image) {
  return QQuickTextureFactory::textureFactoryForImage(*image);
}

//  a Python function taken by a CuteQQuickTextureFactory, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextureFactory(
    QQuickTextureFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextureFactory *>(self)->take(key, call);
}

//  QImage QQuickTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK20QQuickTextureFactory5imageEv(
    const QQuickTextureFactory *self) {
  return new QImage(self->QQuickTextureFactory::image());
}
