//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/barseriesrendercache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/barseriesrendercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/seriesrendercache_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/barseriesrendercache_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 16, as local:objecthelper.cpp:ObjectHelperRef
struct ObjectHelperRef {
    int refCount;
    ObjectHelper *obj;
};

//  from ../qtdatavis3d/src/datavisualization/engine/seriesrendercache.cpp, line 13, as _ZN17SeriesRenderCacheC2EP17QAbstract3DSeriesP18Abstract3DRenderer
inline SeriesRenderCache::SeriesRenderCache(QAbstract3DSeries *series, Abstract3DRenderer *renderer)
    : m_series(series),
      m_object(0),
      m_mesh(QAbstract3DSeries::MeshCube),
      m_baseUniformTexture(0),
      m_baseGradientTexture(0),
      m_gradientImage(0),
      m_singleHighlightGradientTexture(0),
      m_multiHighlightGradientTexture(0),
      m_valid(false),
      m_visible(false),
      m_renderer(renderer),
      m_objectDirty(true),
      m_staticObjectUVDirty(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/barseriesrendercache.cpp, line 19, as _ZN20BarSeriesRenderCache7cleanupEP13TextureHelper
inline void BarSeriesRenderCache::cleanup(TextureHelper *texHelper)
{
    m_renderArray.clear();
    m_sliceArray.clear();

    SeriesRenderCache::cleanup(texHelper);
}

//  from ../qtdatavis3d/src/datavisualization/engine/barseriesrendercache.cpp, line 15, as _ZN20BarSeriesRenderCacheD2Ev
inline BarSeriesRenderCache::~BarSeriesRenderCache()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/seriesrendercache.cpp, line 172, as _ZN17SeriesRenderCache7cleanupEP13TextureHelper
inline void SeriesRenderCache::cleanup(TextureHelper *texHelper)
{
    ObjectHelper::releaseObjectHelper(m_renderer, m_object);
    if (QOpenGLContext::currentContext()) {
        texHelper->deleteTexture(&m_baseUniformTexture);
        texHelper->deleteTexture(&m_baseGradientTexture);
        texHelper->deleteTexture(&m_singleHighlightGradientTexture);
        texHelper->deleteTexture(&m_multiHighlightGradientTexture);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 325, as _ZN13TextureHelper13deleteTextureEPj
inline void TextureHelper::deleteTexture(GLuint *texture)
{
    if (texture && *texture) {
        if (QOpenGLContext::currentContext())
            glDeleteTextures(1, texture);
        *texture = 0;
    }
}
//  -----------------------------------------------------------------------

//  A BarSeriesRenderCache that Python can take functions over in. Every BarSeriesRenderCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteBarSeriesRenderCacheCall0)(const void *, TextureHelper *, int *);
typedef void (*CuteBarSeriesRenderCacheCall1)(const void *, bool, int *);
class CuteBarSeriesRenderCache : public BarSeriesRenderCache {
public:
  using BarSeriesRenderCache::BarSeriesRenderCache;
  CuteBarSeriesRenderCache(const BarSeriesRenderCache & other) : BarSeriesRenderCache(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17SeriesRenderCache7cleanupEP13TextureHelper")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17SeriesRenderCache8populateEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void BarSeriesRenderCache::cleanup(TextureHelper *texHelper)
  void cleanup(TextureHelper *texHelper) override {
    if (taken[0]) {
      int handled = 0;
      CuteBarSeriesRenderCacheCall0 call = reinterpret_cast<CuteBarSeriesRenderCacheCall0>(taken[0]);
      call(this, texHelper, &handled);
      if (handled) return;
    }
    BarSeriesRenderCache::cleanup(texHelper);
  }

  //  void SeriesRenderCache::populate(bool newSeries)
  void populate(bool newSeries) override {
    if (taken[1]) {
      int handled = 0;
      CuteBarSeriesRenderCacheCall1 call = reinterpret_cast<CuteBarSeriesRenderCacheCall1>(taken[1]);
      call(this, newSeries, &handled);
      if (handled) return;
    }
    SeriesRenderCache::populate(newSeries);
  }
};

//  BarSeriesRenderCache::~BarSeriesRenderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN20BarSeriesRenderCacheD1Ev(BarSeriesRenderCache *self) {
  delete self;
}

//  void BarSeriesRenderCache::cleanup(TextureHelper *texHelper)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BarSeriesRenderCache7cleanupEP13TextureHelper(
    BarSeriesRenderCache *self,
    TextureHelper *texHelper) {
  self->cleanup(texHelper);
}

//  BarRenderItemArray &BarSeriesRenderCache::renderArray()
extern "C" Q_DECL_EXPORT
BarRenderItemArray *ritual_ZN20BarSeriesRenderCache11renderArrayEv(
    BarSeriesRenderCache *self) {
  return &(self->renderArray());
}

//  QBar3DSeries *BarSeriesRenderCache::series() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK20BarSeriesRenderCache6seriesEv(
    const BarSeriesRenderCache *self) {
  return self->series();
}

//  QList<BarRenderSliceItem> &BarSeriesRenderCache::sliceArray()
extern "C" Q_DECL_EXPORT
QList<BarRenderSliceItem> *ritual_ZN20BarSeriesRenderCache10sliceArrayEv(
    BarSeriesRenderCache *self) {
  return &(self->sliceArray());
}

//  void BarSeriesRenderCache::setVisualIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BarSeriesRenderCache14setVisualIndexEi(
    BarSeriesRenderCache *self,
    int index) {
  self->setVisualIndex(index);
}

//  int BarSeriesRenderCache::visualIndex()
extern "C" Q_DECL_EXPORT
int ritual_ZN20BarSeriesRenderCache11visualIndexEv(
    BarSeriesRenderCache *self) {
  return self->visualIndex();
}

//  a Python function taken by a CuteBarSeriesRenderCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BarSeriesRenderCache(
    BarSeriesRenderCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteBarSeriesRenderCache *>(self)->take(key, call);
}
