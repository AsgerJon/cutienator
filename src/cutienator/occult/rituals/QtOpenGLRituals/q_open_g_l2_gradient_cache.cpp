//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglgradientcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglgradientcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qopenglgradientcache_p.h"
#include <private/qdrawhelper_p.h>
#include <private/qopenglcontext_p.h>
#include <private/qrgba64_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qrandom.h>
#include "qopenglfunctions.h"
#include <private/qopenglextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopenglgradientcache.cpp, line 35, as _ZN21QOpenGL2GradientCacheC1EP14QOpenGLContext
inline QOpenGL2GradientCache::QOpenGL2GradientCache(QOpenGLContext *ctx)
    : QOpenGLSharedResource(ctx->shareGroup())
{
}

//  from src/opengl/qopenglgradientcache.cpp, line 40, as _ZN21QOpenGL2GradientCacheD1Ev
inline QOpenGL2GradientCache::~QOpenGL2GradientCache()
{
    cache.clear();
}

//  from src/opengl/qopenglgradientcache.cpp, line 50, as _ZN21QOpenGL2GradientCache18invalidateResourceEv
inline void QOpenGL2GradientCache::invalidateResource()
{
    QMutexLocker lock(&m_mutex);
    cache.clear();
}

//  from src/opengl/qopenglgradientcache.cpp, line 56, as _ZN21QOpenGL2GradientCache12freeResourceEP14QOpenGLContext
inline void QOpenGL2GradientCache::freeResource(QOpenGLContext *)
{
    cleanCache();
}

//  from src/opengl/qopenglgradientcache.cpp, line 137, as _ZNK21QOpenGL2GradientCache26generateGradientColorTableERK9QGradientP7QRgba64id
inline void QOpenGL2GradientCache::generateGradientColorTable(const QGradient& gradient, QRgba64 *colorTable, int size, qreal opacity) const
{
    int pos = 0;
    const QGradientStops s = gradient.stops();

    bool colorInterpolation = (gradient.interpolationMode() == QGradient::ColorInterpolation);

    uint alpha = qRound(opacity * 256);
    QRgba64 current_color = combineAlpha256(s[0].second.rgba64(), alpha);
    qreal incr = 1.0 / qreal(size);
    qreal fpos = 1.5 * incr;
    colorTable[pos++] = qPremultiply(current_color);

    while (pos < size && fpos <= s.first().first) {
        colorTable[pos] = colorTable[pos - 1];
        pos++;
        fpos += incr;
    }

    if (colorInterpolation)
        current_color = qPremultiply(current_color);

    const int sLast = s.size() - 1;
    for (int i = 0; i < sLast; ++i) {
        qreal delta = 1/(s[i+1].first - s[i].first);
        QRgba64 next_color = combineAlpha256(s[i + 1].second.rgba64(), alpha);
        if (colorInterpolation)
            next_color = qPremultiply(next_color);

        while (fpos < s[i+1].first && pos < size) {
            int dist = int(256 * ((fpos - s[i].first) * delta));
            int idist = 256 - dist;
            if (colorInterpolation)
                colorTable[pos] = interpolate256(current_color, idist, next_color, dist);
            else
                colorTable[pos] = qPremultiply(interpolate256(current_color, idist, next_color, dist));
            ++pos;
            fpos += incr;
        }
        current_color = next_color;
    }

    Q_ASSERT(s.size() > 0);

    QRgba64 last_color = qPremultiply(combineAlpha256(s[sLast].second.rgba64(), alpha));
    for (;pos < size; ++pos)
        colorTable[pos] = last_color;

    // Make sure the last color stop is represented at the end of the table
    colorTable[size-1] = last_color;
}

//  from src/opengl/qopenglgradientcache.cpp, line 189, as _ZNK21QOpenGL2GradientCache26generateGradientColorTableERK9QGradientPjid
inline void QOpenGL2GradientCache::generateGradientColorTable(const QGradient& gradient, uint *colorTable, int size, qreal opacity) const
{
    int pos = 0;
    const QGradientStops s = gradient.stops();

    bool colorInterpolation = (gradient.interpolationMode() == QGradient::ColorInterpolation);

    uint alpha = qRound(opacity * 256);
    // Qt LIES! It returns ARGB (on little-endian AND on big-endian)
    uint current_color = ARGB_COMBINE_ALPHA(s[0].second.rgba(), alpha);
    qreal incr = 1.0 / qreal(size);
    qreal fpos = 1.5 * incr;
    colorTable[pos++] = ARGB2RGBA(qPremultiply(current_color));

    while (pos < size && fpos <= s.first().first) {
        colorTable[pos] = colorTable[pos - 1];
        pos++;
        fpos += incr;
    }

    if (colorInterpolation)
        current_color = qPremultiply(current_color);

    const int sLast = s.size() - 1;
    for (int i = 0; i < sLast; ++i) {
        qreal delta = 1/(s[i+1].first - s[i].first);
        uint next_color = ARGB_COMBINE_ALPHA(s[i + 1].second.rgba(), alpha);
        if (colorInterpolation)
            next_color = qPremultiply(next_color);

        while (fpos < s[i+1].first && pos < size) {
            int dist = int(256 * ((fpos - s[i].first) * delta));
            int idist = 256 - dist;
            if (colorInterpolation)
                colorTable[pos] = ARGB2RGBA(INTERPOLATE_PIXEL_256(current_color, idist, next_color, dist));
            else
                colorTable[pos] = ARGB2RGBA(qPremultiply(INTERPOLATE_PIXEL_256(current_color, idist, next_color, dist)));
            ++pos;
            fpos += incr;
        }
        current_color = next_color;
    }

    Q_ASSERT(s.size() > 0);

    uint last_color = ARGB2RGBA(qPremultiply(ARGB_COMBINE_ALPHA(s[sLast].second.rgba(), alpha)));
    for (;pos < size; ++pos)
        colorTable[pos] = last_color;

    // Make sure the last color stop is represented at the end of the table
    colorTable[size-1] = last_color;
}

//  from src/opengl/qopenglgradientcache.cpp, line 61, as _ZN21QOpenGL2GradientCache10cleanCacheEv
inline void QOpenGL2GradientCache::cleanCache()
{
    QMutexLocker lock(&m_mutex);
    QOpenGLGradientColorTableHash::const_iterator it = cache.constBegin();
    QOpenGLFunctions *funcs = QOpenGLContext::currentContext()->functions();
    for (; it != cache.constEnd(); ++it) {
        const CacheInfo &cache_info = it.value();
        funcs->glDeleteTextures(1, &cache_info.texId);
    }
    cache.clear();
}
//  -----------------------------------------------------------------------

//  A QOpenGL2GradientCache that Python can take functions over in. Every QOpenGL2GradientCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGL2GradientCacheCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGL2GradientCacheCall1)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGL2GradientCache : public QOpenGL2GradientCache {
public:
  using QOpenGL2GradientCache::QOpenGL2GradientCache;
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
  //  void QOpenGL2GradientCache::invalidateResource()
  void invalidateResource() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGL2GradientCacheCall0 call = reinterpret_cast<CuteQOpenGL2GradientCacheCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGL2GradientCache::invalidateResource();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGL2GradientCache::freeResource(QOpenGLContext *ctx)
  void freeResource(QOpenGLContext *ctx) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGL2GradientCacheCall1 call = reinterpret_cast<CuteQOpenGL2GradientCacheCall1>(taken[1]);
      call(this, ctx, &handled);
      if (handled) return;
    }
    QOpenGL2GradientCache::freeResource(ctx);
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGL2GradientCache::QOpenGL2GradientCache(QOpenGLContext *a0)
extern "C" Q_DECL_EXPORT
QOpenGL2GradientCache *ritual_ZN21QOpenGL2GradientCacheC1EP14QOpenGLContext(
    QOpenGLContext *a0) {
  return new CuteQOpenGL2GradientCache(a0);
}

//  QOpenGL2GradientCache::~QOpenGL2GradientCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2GradientCacheD1Ev(QOpenGL2GradientCache *self) {
  delete self;
}

//  int QOpenGL2GradientCache::paletteSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QOpenGL2GradientCache11paletteSizeEv(
    const QOpenGL2GradientCache *self) {
  return self->paletteSize();
}

//  void QOpenGL2GradientCache::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2GradientCache18invalidateResourceEv(
    QOpenGL2GradientCache *self) {
  self->invalidateResource();
}

//  void QOpenGL2GradientCache::freeResource(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2GradientCache12freeResourceEP14QOpenGLContext(
    QOpenGL2GradientCache *self,
    QOpenGLContext *ctx) {
  self->freeResource(ctx);
}

//  int QOpenGL2GradientCache::maxCacheSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QOpenGL2GradientCache12maxCacheSizeEv(
    const QOpenGL2GradientCache *self) {
  return self->maxCacheSize();
}

//  void QOpenGL2GradientCache::generateGradientColorTable(const QGradient
//      &gradient, QRgba64 *colorTable, int size, qreal opacity) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QOpenGL2GradientCache26generateGradientColorTableERK9QGradientP7QRgba64id(
    const QOpenGL2GradientCache *self,
    const QGradient *gradient,
    QRgba64 *colorTable,
    int size,
    qreal opacity) {
  self->generateGradientColorTable(*gradient, colorTable, size, opacity);
}

//  void QOpenGL2GradientCache::generateGradientColorTable(const QGradient
//      &gradient, uint *colorTable, int size, qreal opacity) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QOpenGL2GradientCache26generateGradientColorTableERK9QGradientPjid(
    const QOpenGL2GradientCache *self,
    const QGradient *gradient,
    uint *colorTable,
    int size,
    qreal opacity) {
  self->generateGradientColorTable(*gradient, colorTable, size, opacity);
}

//  void QOpenGL2GradientCache::cleanCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGL2GradientCache10cleanCacheEv(
    QOpenGL2GradientCache *self) {
  self->cleanCache();
}

//  a Python function taken by a CuteQOpenGL2GradientCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGL2GradientCache(
    QOpenGL2GradientCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGL2GradientCache *>(self)->take(key, call);
}

//  void QOpenGL2GradientCache::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2GradientCache18invalidateResourceEv(
    QOpenGL2GradientCache *self) {
  self->QOpenGL2GradientCache::invalidateResource();
}

//  void QOpenGL2GradientCache::freeResource(QOpenGLContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QOpenGL2GradientCache12freeResourceEP14QOpenGLContext(
    QOpenGL2GradientCache *self,
    QOpenGLContext *ctx) {
  self->QOpenGL2GradientCache::freeResource(ctx);
}
