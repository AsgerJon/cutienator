//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(metal) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QNativeInterface::QSGMetalTexture that Python can take functions over in. Every QNativeInterface::QSGMetalTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(metal) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QSGMetalTextureCall0)(const void *, int *);
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
class CuteQNativeInterface_QSGMetalTexture : public QNativeInterface::QSGMetalTexture {
public:
  using QNativeInterface::QSGMetalTexture::QSGMetalTexture;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(metal) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface15QSGMetalTexture13nativeTextureEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(metal) || defined(Q_QDOC)
  //  id QNativeInterface::QSGMetalTexture::nativeTexture() const
  id nativeTexture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QSGMetalTextureCall0 call = reinterpret_cast<CuteQNativeInterface_QSGMetalTextureCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<id>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
};

//  QNativeInterface::QSGMetalTexture::~QSGMetalTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface15QSGMetalTextureD1Ev(
    QNativeInterface::QSGMetalTexture *self) {
  delete self;
}

//  QNativeInterface::QSGMetalTexture::QSGMetalTexture()
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGMetalTexture *ritual_ZN16QNativeInterface15QSGMetalTextureC1Ev() {
  return new CuteQNativeInterface_QSGMetalTexture();
}

//  id QNativeInterface::QSGMetalTexture::nativeTexture() const
extern "C" Q_DECL_EXPORT
id ritual_ZNK16QNativeInterface15QSGMetalTexture13nativeTextureEv(
    const QNativeInterface::QSGMetalTexture *self) {
  return self->nativeTexture();
}

//  QSGTexture *QNativeInterface::QSGMetalTexture::fromNative(id texture,
//      QQuickWindow *window, const QSize &size,
//      QQuickWindow::CreateTextureOptions options)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QNativeInterface15QSGMetalTexture10fromNativeEP11objc_objectP12QQuickWindowRK5QSize6QFlagsINS3_19CreateTextureOptionEE(
    id texture,
    QQuickWindow *window,
    const QSize *size,
    int options) {
  return QNativeInterface::QSGMetalTexture::fromNative(
      texture,
      window,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  a Python function taken by a CuteQNativeInterface_QSGMetalTexture, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QSGMetalTexture(
    QNativeInterface::QSGMetalTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QSGMetalTexture *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
