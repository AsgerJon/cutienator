//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QNativeInterface::QSGOpenGLTexture that Python can take functions over in. Every QNativeInterface::QSGOpenGLTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(opengl) || defined(Q_QDOC)
typedef GLuint (*CuteQNativeInterface_QSGOpenGLTextureCall0)(const void *, int *);
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
class CuteQNativeInterface_QSGOpenGLTexture : public QNativeInterface::QSGOpenGLTexture {
public:
  using QNativeInterface::QSGOpenGLTexture::QSGOpenGLTexture;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(opengl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGOpenGLTexture13nativeTextureEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(opengl) || defined(Q_QDOC)
  //  GLuint QNativeInterface::QSGOpenGLTexture::nativeTexture() const
  GLuint nativeTexture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QSGOpenGLTextureCall0 call = reinterpret_cast<CuteQNativeInterface_QSGOpenGLTextureCall0>(taken[0]);
      GLuint given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
};

//  QNativeInterface::QSGOpenGLTexture::~QSGOpenGLTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface16QSGOpenGLTextureD1Ev(
    QNativeInterface::QSGOpenGLTexture *self) {
  delete self;
}

//  QNativeInterface::QSGOpenGLTexture::QSGOpenGLTexture()
extern "C" Q_DECL_EXPORT
QNativeInterface::QSGOpenGLTexture *ritual_ZN16QNativeInterface16QSGOpenGLTextureC1Ev() {
  return new CuteQNativeInterface_QSGOpenGLTexture();
}

//  GLuint QNativeInterface::QSGOpenGLTexture::nativeTexture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK16QNativeInterface16QSGOpenGLTexture13nativeTextureEv(
    const QNativeInterface::QSGOpenGLTexture *self) {
  return self->nativeTexture();
}

//  QSGTexture *QNativeInterface::QSGOpenGLTexture::fromNative(GLuint
//      textureId, QQuickWindow *window, const QSize &size,
//      QQuickWindow::CreateTextureOptions options)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QNativeInterface16QSGOpenGLTexture10fromNativeEjP12QQuickWindowRK5QSize6QFlagsINS1_19CreateTextureOptionEE(
    GLuint textureId,
    QQuickWindow *window,
    const QSize *size,
    int options) {
  return QNativeInterface::QSGOpenGLTexture::fromNative(
      textureId,
      window,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  QSGTexture
//      *QNativeInterface::QSGOpenGLTexture::fromNativeExternalOES(GLuint
//      textureId, QQuickWindow *window, const QSize &size,
//      QQuickWindow::CreateTextureOptions options)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QNativeInterface16QSGOpenGLTexture21fromNativeExternalOESEjP12QQuickWindowRK5QSize6QFlagsINS1_19CreateTextureOptionEE(
    GLuint textureId,
    QQuickWindow *window,
    const QSize *size,
    int options) {
  return QNativeInterface::QSGOpenGLTexture::fromNativeExternalOES(
      textureId,
      window,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  a Python function taken by a CuteQNativeInterface_QSGOpenGLTexture, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QSGOpenGLTexture(
    QNativeInterface::QSGOpenGLTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QSGOpenGLTexture *>(self)->take(key, call);
}

#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
