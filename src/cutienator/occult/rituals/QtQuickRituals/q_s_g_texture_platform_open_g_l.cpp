//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGTexturePlatformOpenGL that Python can take functions over in. Every QSGTexturePlatformOpenGL
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#if QT_CONFIG(opengl)
typedef uint (*CuteQSGTexturePlatformOpenGLCall0)(const void *, int *);
#endif  // QT_CONFIG(opengl)
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
class CuteQSGTexturePlatformOpenGL : public QSGTexturePlatformOpenGL {
public:
  using QSGTexturePlatformOpenGL::QSGTexturePlatformOpenGL;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#if QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGOpenGLTexture13nativeTextureEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(opengl)
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(opengl) || defined(Q_QDOC)
#if QT_CONFIG(opengl)
  //  uint QSGTexturePlatformOpenGL::nativeTexture() const
  uint nativeTexture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTexturePlatformOpenGLCall0 call = reinterpret_cast<CuteQSGTexturePlatformOpenGLCall0>(taken[0]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexturePlatformOpenGL::nativeTexture();
  }
#endif  // QT_CONFIG(opengl)
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
};

//  QSGTexturePlatformOpenGL::QSGTexturePlatformOpenGL(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformOpenGL *ritual_ZN24QSGTexturePlatformOpenGLC1EP10QSGTexture(
    QSGTexture *t) {
  return new CuteQSGTexturePlatformOpenGL(t);
}

//  uint QSGTexturePlatformOpenGL::nativeTexture() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK24QSGTexturePlatformOpenGL13nativeTextureEv(
    const QSGTexturePlatformOpenGL *self) {
  return self->nativeTexture();
}

//  a Python function taken by a CuteQSGTexturePlatformOpenGL, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTexturePlatformOpenGL(
    QSGTexturePlatformOpenGL *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTexturePlatformOpenGL *>(self)->take(key, call);
}

//  uint QSGTexturePlatformOpenGL::nativeTexture() const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK24QSGTexturePlatformOpenGL13nativeTextureEv(
    const QSGTexturePlatformOpenGL *self) {
  return self->QSGTexturePlatformOpenGL::nativeTexture();
}

#endif  // QT_CONFIG(opengl)
