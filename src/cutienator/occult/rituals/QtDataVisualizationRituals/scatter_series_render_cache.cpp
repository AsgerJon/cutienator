//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/scatterseriesrendercache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/scatterseriesrendercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/seriesrendercache_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/scatterseriesrendercache_p.h>
#include <QtDataVisualization/private/scatterobjectbufferhelper_p.h>
#include <QtDataVisualization/private/scatterpointbufferhelper_p.h>
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

//  from ../qtdatavis3d/src/datavisualization/engine/scatterseriesrendercache.cpp, line 24, as _ZN24ScatterSeriesRenderCacheD2Ev
inline ScatterSeriesRenderCache::~ScatterSeriesRenderCache()
{
    delete m_scatterBufferObj;
    delete m_scatterBufferPoints;
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

//  from ../qtdatavis3d/src/datavisualization/engine/scatterseriesrendercache.cpp, line 30, as _ZN24ScatterSeriesRenderCache7cleanupEP13TextureHelper
inline void ScatterSeriesRenderCache::cleanup(TextureHelper *texHelper)
{
    m_renderArray.clear();

    SeriesRenderCache::cleanup(texHelper);
}
//  -----------------------------------------------------------------------

//  A ScatterSeriesRenderCache that Python can take functions over in. Every ScatterSeriesRenderCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteScatterSeriesRenderCacheCall0)(const void *, TextureHelper *, int *);
typedef void (*CuteScatterSeriesRenderCacheCall1)(const void *, bool, int *);
class CuteScatterSeriesRenderCache : public ScatterSeriesRenderCache {
public:
  using ScatterSeriesRenderCache::ScatterSeriesRenderCache;
  CuteScatterSeriesRenderCache(const ScatterSeriesRenderCache &other) : ScatterSeriesRenderCache(other) {}
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

  //  void ScatterSeriesRenderCache::cleanup(TextureHelper *texHelper)
  void cleanup(TextureHelper *texHelper) override {
    if (taken[0]) {
      int handled = 0;
      CuteScatterSeriesRenderCacheCall0 call = reinterpret_cast<CuteScatterSeriesRenderCacheCall0>(taken[0]);
      call(this, texHelper, &handled);
      if (handled) return;
    }
    ScatterSeriesRenderCache::cleanup(texHelper);
  }

  //  void SeriesRenderCache::populate(bool newSeries)
  void populate(bool newSeries) override {
    if (taken[1]) {
      int handled = 0;
      CuteScatterSeriesRenderCacheCall1 call = reinterpret_cast<CuteScatterSeriesRenderCacheCall1>(taken[1]);
      call(this, newSeries, &handled);
      if (handled) return;
    }
    SeriesRenderCache::populate(newSeries);
  }
};

//  ScatterSeriesRenderCache::~ScatterSeriesRenderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCacheD1Ev(
    ScatterSeriesRenderCache *self) {
  delete self;
}

//  void ScatterSeriesRenderCache::cleanup(TextureHelper *texHelper)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache7cleanupEP13TextureHelper(
    ScatterSeriesRenderCache *self,
    TextureHelper *texHelper) {
  self->cleanup(texHelper);
}

//  QScatter3DSeries *ScatterSeriesRenderCache::series() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK24ScatterSeriesRenderCache6seriesEv(
    const ScatterSeriesRenderCache *self) {
  return self->series();
}

//  void ScatterSeriesRenderCache::setItemSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache11setItemSizeEf(
    ScatterSeriesRenderCache *self,
    float size) {
  self->setItemSize(size);
}

//  float ScatterSeriesRenderCache::itemSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ScatterSeriesRenderCache8itemSizeEv(
    const ScatterSeriesRenderCache *self) {
  return self->itemSize();
}

//  void ScatterSeriesRenderCache::setSelectionIndexOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache23setSelectionIndexOffsetEi(
    ScatterSeriesRenderCache *self,
    int offset) {
  self->setSelectionIndexOffset(offset);
}

//  int ScatterSeriesRenderCache::selectionIndexOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24ScatterSeriesRenderCache20selectionIndexOffsetEv(
    const ScatterSeriesRenderCache *self) {
  return self->selectionIndexOffset();
}

//  void ScatterSeriesRenderCache::setStaticBufferDirty(bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache20setStaticBufferDirtyEb(
    ScatterSeriesRenderCache *self,
    bool state) {
  self->setStaticBufferDirty(state);
}

//  bool ScatterSeriesRenderCache::staticBufferDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24ScatterSeriesRenderCache17staticBufferDirtyEv(
    const ScatterSeriesRenderCache *self) {
  return self->staticBufferDirty();
}

//  int ScatterSeriesRenderCache::oldArraySize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24ScatterSeriesRenderCache12oldArraySizeEv(
    const ScatterSeriesRenderCache *self) {
  return self->oldArraySize();
}

//  void ScatterSeriesRenderCache::setOldArraySize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache15setOldArraySizeEi(
    ScatterSeriesRenderCache *self,
    int size) {
  self->setOldArraySize(size);
}

//  const QString &ScatterSeriesRenderCache::oldMeshFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24ScatterSeriesRenderCache15oldMeshFileNameEv(
    const ScatterSeriesRenderCache *self) {
  return new QString(self->oldMeshFileName());
}

//  void ScatterSeriesRenderCache::setOldMeshFileName(const QString
//      &meshFileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache18setOldMeshFileNameERK7QString(
    ScatterSeriesRenderCache *self,
    const QString *meshFileName) {
  self->setOldMeshFileName(*meshFileName);
}

//  void ScatterSeriesRenderCache::setBufferObject(ScatterObjectBufferHelper
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache15setBufferObjectEP25ScatterObjectBufferHelper(
    ScatterSeriesRenderCache *self,
    ScatterObjectBufferHelper *object) {
  self->setBufferObject(object);
}

//  ScatterObjectBufferHelper *ScatterSeriesRenderCache::bufferObject() const
extern "C" Q_DECL_EXPORT
ScatterObjectBufferHelper *ritual_ZNK24ScatterSeriesRenderCache12bufferObjectEv(
    const ScatterSeriesRenderCache *self) {
  return self->bufferObject();
}

//  void ScatterSeriesRenderCache::setBufferPoints(ScatterPointBufferHelper
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache15setBufferPointsEP24ScatterPointBufferHelper(
    ScatterSeriesRenderCache *self,
    ScatterPointBufferHelper *object) {
  self->setBufferPoints(object);
}

//  ScatterPointBufferHelper *ScatterSeriesRenderCache::bufferPoints() const
extern "C" Q_DECL_EXPORT
ScatterPointBufferHelper *ritual_ZNK24ScatterSeriesRenderCache12bufferPointsEv(
    const ScatterSeriesRenderCache *self) {
  return self->bufferPoints();
}

//  void ScatterSeriesRenderCache::setVisibilityChanged(bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterSeriesRenderCache20setVisibilityChangedEb(
    ScatterSeriesRenderCache *self,
    bool changed) {
  self->setVisibilityChanged(changed);
}

//  bool ScatterSeriesRenderCache::visibilityChanged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24ScatterSeriesRenderCache17visibilityChangedEv(
    const ScatterSeriesRenderCache *self) {
  return self->visibilityChanged();
}

//  a Python function taken by a CuteScatterSeriesRenderCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ScatterSeriesRenderCache(
    ScatterSeriesRenderCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteScatterSeriesRenderCache *>(self)->take(key, call);
}
