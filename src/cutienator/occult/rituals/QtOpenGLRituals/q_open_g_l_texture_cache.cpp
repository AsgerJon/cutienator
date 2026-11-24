//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QOpenGLTextureCache that Python can take functions over in. Every QOpenGLTextureCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLTextureCacheCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLTextureCacheCall1)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLTextureCache : public QOpenGLTextureCache {
public:
  using QOpenGLTextureCache::QOpenGLTextureCache;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource18invalidateResourceEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLTextureCache::invalidateResource()
  void invalidateResource() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLTextureCacheCall0 call = reinterpret_cast<CuteQOpenGLTextureCacheCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLTextureCache::invalidateResource();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLTextureCache::freeResource(QOpenGLContext *ctx)
  void freeResource(QOpenGLContext *ctx) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLTextureCacheCall1 call = reinterpret_cast<CuteQOpenGLTextureCacheCall1>(taken[1]);
      call(this, ctx, &handled);
      if (handled) return;
    }
    QOpenGLTextureCache::freeResource(ctx);
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLTextureCache *QOpenGLTextureCache::cacheForContext(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLTextureCache *ritual_ZN19QOpenGLTextureCache15cacheForContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLTextureCache::cacheForContext(context);
}

//  QOpenGLTextureCache::QOpenGLTextureCache(QOpenGLContext *a0)
extern "C" Q_DECL_EXPORT
QOpenGLTextureCache *ritual_ZN19QOpenGLTextureCacheC1EP14QOpenGLContext(
    QOpenGLContext *a0) {
  return new CuteQOpenGLTextureCache(a0);
}

//  QOpenGLTextureCache::~QOpenGLTextureCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLTextureCacheD1Ev(QOpenGLTextureCache *self) {
  delete self;
}

//  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
//      const QPixmap &pixmap, QOpenGLTextureUploader::BindOptions options)
extern "C" Q_DECL_EXPORT
QOpenGLTextureCache::BindResult *ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextRK7QPixmap6QFlagsIN22QOpenGLTextureUploader10BindOptionEE(
    QOpenGLTextureCache *self,
    QOpenGLContext *context,
    const QPixmap *pixmap,
    int options) {
  return new QOpenGLTextureCache::BindResult(
      self->bindTexture(
          context,
          *pixmap,
          QFlags<QOpenGLTextureUploader::BindOption>::fromInt(options)));
}

//  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
//      const QImage &image, QOpenGLTextureUploader::BindOptions options)
extern "C" Q_DECL_EXPORT
QOpenGLTextureCache::BindResult *ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextRK6QImage6QFlagsIN22QOpenGLTextureUploader10BindOptionEE(
    QOpenGLTextureCache *self,
    QOpenGLContext *context,
    const QImage *image,
    int options) {
  return new QOpenGLTextureCache::BindResult(
      self->bindTexture(
          context,
          *image,
          QFlags<QOpenGLTextureUploader::BindOption>::fromInt(options)));
}

//  void QOpenGLTextureCache::invalidate(qint64 key)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLTextureCache10invalidateEx(
    QOpenGLTextureCache *self,
    qint64 key) {
  self->invalidate(key);
}

//  void QOpenGLTextureCache::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLTextureCache18invalidateResourceEv(
    QOpenGLTextureCache *self) {
  self->invalidateResource();
}

//  void QOpenGLTextureCache::freeResource(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLTextureCache12freeResourceEP14QOpenGLContext(
    QOpenGLTextureCache *self,
    QOpenGLContext *ctx) {
  self->freeResource(ctx);
}

//  BindResult QOpenGLTextureCache::bindTexture(QOpenGLContext *context,
//      qint64 key, const QImage &image, QOpenGLTextureUploader::BindOptions
//      options)
extern "C" Q_DECL_EXPORT
QOpenGLTextureCache::BindResult *ritual_ZN19QOpenGLTextureCache11bindTextureEP14QOpenGLContextxRK6QImage6QFlagsIN22QOpenGLTextureUploader10BindOptionEE(
    QOpenGLTextureCache *self,
    QOpenGLContext *context,
    qint64 key,
    const QImage *image,
    int options) {
  return new QOpenGLTextureCache::BindResult(
      self->bindTexture(
          context,
          key,
          *image,
          QFlags<QOpenGLTextureUploader::BindOption>::fromInt(options)));
}

//  a Python function taken by a CuteQOpenGLTextureCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLTextureCache(
    QOpenGLTextureCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLTextureCache *>(self)->take(key, call);
}

//  void QOpenGLTextureCache::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QOpenGLTextureCache18invalidateResourceEv(
    QOpenGLTextureCache *self) {
  self->QOpenGLTextureCache::invalidateResource();
}

//  void QOpenGLTextureCache::freeResource(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QOpenGLTextureCache12freeResourceEP14QOpenGLContext(
    QOpenGLTextureCache *self,
    QOpenGLContext *ctx) {
  self->QOpenGLTextureCache::freeResource(ctx);
}
