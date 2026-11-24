//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcompressedtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGCompressedTextureFactory that Python can take functions over in. Every QSGCompressedTextureFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGCompressedTextureFactoryCall0)(const void *, QQuickWindow *, int *);
typedef int (*CuteQSGCompressedTextureFactoryCall1)(const void *, int *);
typedef const QSize * (*CuteQSGCompressedTextureFactoryCall2)(const void *, int *);
typedef const QImage * (*CuteQSGCompressedTextureFactoryCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedTextureFactoryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGCompressedTextureFactoryCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureFactoryCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureFactoryCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureFactoryCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureFactoryCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGCompressedTextureFactoryCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGCompressedTextureFactory : public QSGCompressedTextureFactory {
public:
  using QSGCompressedTextureFactory::QSGCompressedTextureFactory;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory13createTextureEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory16textureByteCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickTextureFactory11textureSizeEv")) {
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

  //  QSGTexture *QSGCompressedTextureFactory::createTexture(QQuickWindow
  //      *a0) const
  QSGTexture *createTexture(QQuickWindow *a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCompressedTextureFactoryCall0 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGCompressedTextureFactory::createTexture(a0);
  }

  //  int QSGCompressedTextureFactory::textureByteCount() const
  int textureByteCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCompressedTextureFactoryCall1 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGCompressedTextureFactory::textureByteCount();
  }

  //  QSize QSGCompressedTextureFactory::textureSize() const
  QSize textureSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCompressedTextureFactoryCall2 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGCompressedTextureFactory::textureSize();
  }

  //  QImage QQuickTextureFactory::image() const
  QImage image() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCompressedTextureFactoryCall3 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall3>(taken[3]);
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
      CuteQSGCompressedTextureFactoryCall4 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall4>(taken[4]);
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
      CuteQSGCompressedTextureFactoryCall5 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall5>(taken[5]);
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
      CuteQSGCompressedTextureFactoryCall6 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall6>(taken[6]);
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
      CuteQSGCompressedTextureFactoryCall7 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall7>(taken[7]);
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
      CuteQSGCompressedTextureFactoryCall8 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall8>(taken[8]);
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
      CuteQSGCompressedTextureFactoryCall9 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall9>(taken[9]);
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
      CuteQSGCompressedTextureFactoryCall10 call = reinterpret_cast<CuteQSGCompressedTextureFactoryCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGCompressedTextureFactory::QSGCompressedTextureFactory(const
//      QTextureFileData &texData)
extern "C" Q_DECL_EXPORT
QSGCompressedTextureFactory *ritual_ZN27QSGCompressedTextureFactoryC1ERK16QTextureFileData(
    const QTextureFileData *texData) {
  return new CuteQSGCompressedTextureFactory(*texData);
}

//  QSGTexture *QSGCompressedTextureFactory::createTexture(QQuickWindow *a0)
//      const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK27QSGCompressedTextureFactory13createTextureEP12QQuickWindow(
    const QSGCompressedTextureFactory *self,
    QQuickWindow *a0) {
  return self->createTexture(a0);
}

//  int QSGCompressedTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QSGCompressedTextureFactory16textureByteCountEv(
    const QSGCompressedTextureFactory *self) {
  return self->textureByteCount();
}

//  QSize QSGCompressedTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QSGCompressedTextureFactory11textureSizeEv(
    const QSGCompressedTextureFactory *self) {
  return new QSize(self->textureSize());
}

//  const QTextureFileData *QSGCompressedTextureFactory::textureData() const
extern "C" Q_DECL_EXPORT
const QTextureFileData *ritual_ZNK27QSGCompressedTextureFactory11textureDataEv(
    const QSGCompressedTextureFactory *self) {
  return self->textureData();
}

//  a Python function taken by a CuteQSGCompressedTextureFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCompressedTextureFactory(
    QSGCompressedTextureFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCompressedTextureFactory *>(self)->take(key, call);
}

//  QSGTexture *QSGCompressedTextureFactory::createTexture(QQuickWindow *a0)
//      const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK27QSGCompressedTextureFactory13createTextureEP12QQuickWindow(
    const QSGCompressedTextureFactory *self,
    QQuickWindow *a0) {
  return self->QSGCompressedTextureFactory::createTexture(a0);
}

//  int QSGCompressedTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK27QSGCompressedTextureFactory16textureByteCountEv(
    const QSGCompressedTextureFactory *self) {
  return self->QSGCompressedTextureFactory::textureByteCount();
}

//  QSize QSGCompressedTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK27QSGCompressedTextureFactory11textureSizeEv(
    const QSGCompressedTextureFactory *self) {
  return new QSize(self->QSGCompressedTextureFactory::textureSize());
}
