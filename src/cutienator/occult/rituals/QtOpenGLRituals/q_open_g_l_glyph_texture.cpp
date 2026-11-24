//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltextureglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QOpenGLGlyphTexture that Python can take functions over in. Every QOpenGLGlyphTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLGlyphTextureCall0)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLGlyphTextureCall1)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLGlyphTexture : public QOpenGLGlyphTexture {
public:
  using QOpenGLGlyphTexture::QOpenGLGlyphTexture;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource18invalidateResourceEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLGlyphTexture::freeResource(QOpenGLContext *context)
  void freeResource(QOpenGLContext *context) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLGlyphTextureCall0 call = reinterpret_cast<CuteQOpenGLGlyphTextureCall0>(taken[0]);
      call(this, context, &handled);
      if (handled) return;
    }
    QOpenGLGlyphTexture::freeResource(context);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLGlyphTexture::invalidateResource()
  void invalidateResource() override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLGlyphTextureCall1 call = reinterpret_cast<CuteQOpenGLGlyphTextureCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLGlyphTexture::invalidateResource();
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLGlyphTexture::QOpenGLGlyphTexture(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
QOpenGLGlyphTexture *ritual_ZN19QOpenGLGlyphTextureC1EP14QOpenGLContext(
    QOpenGLContext *ctx) {
  return new CuteQOpenGLGlyphTexture(ctx);
}

//  void QOpenGLGlyphTexture::freeResource(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLGlyphTexture12freeResourceEP14QOpenGLContext(
    QOpenGLGlyphTexture *self,
    QOpenGLContext *context) {
  self->freeResource(context);
}

//  void QOpenGLGlyphTexture::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLGlyphTexture18invalidateResourceEv(
    QOpenGLGlyphTexture *self) {
  self->invalidateResource();
}

//  a Python function taken by a CuteQOpenGLGlyphTexture, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLGlyphTexture(
    QOpenGLGlyphTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLGlyphTexture *>(self)->take(key, call);
}

//  void QOpenGLGlyphTexture::freeResource(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QOpenGLGlyphTexture12freeResourceEP14QOpenGLContext(
    QOpenGLGlyphTexture *self,
    QOpenGLContext *context) {
  self->QOpenGLGlyphTexture::freeResource(context);
}

//  void QOpenGLGlyphTexture::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QOpenGLGlyphTexture18invalidateResourceEv(
    QOpenGLGlyphTexture *self) {
  self->QOpenGLGlyphTexture::invalidateResource();
}
