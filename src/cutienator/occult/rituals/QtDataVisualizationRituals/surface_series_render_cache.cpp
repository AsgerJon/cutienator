//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/surfaceseriesrendercache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceseriesrendercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qmatrix4x4.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/surfaceobject_p.h>
#include <QtDataVisualization/private/surface3drenderer_p.h>
#include <QtGui/QVector2D>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#include <QtDataVisualization/private/seriesrendercache_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/surfaceseriesrendercache_p.h>
#include <QtDataVisualization/private/surface3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 11, as _ZN13SurfaceObjectC1EP17Surface3DRenderer
inline SurfaceObject::SurfaceObject(Surface3DRenderer *renderer)
    : m_axisCacheX(renderer->m_axisCacheX),
      m_axisCacheY(renderer->m_axisCacheY),
      m_axisCacheZ(renderer->m_axisCacheZ),
      m_renderer(renderer)
{
    glGenBuffers(1, &m_vertexbuffer);
    glGenBuffers(1, &m_normalbuffer);
    glGenBuffers(1, &m_uvbuffer);
    glGenBuffers(1, &m_elementbuffer);
    glGenBuffers(1, &m_gridElementbuffer);
    glGenBuffers(1, &m_uvTextureBuffer);
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

//  from ../qtdatavis3d/src/datavisualization/engine/seriesrendercache.cpp, line 30, as _ZN17SeriesRenderCacheD2Ev
inline SeriesRenderCache::~SeriesRenderCache()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/surfaceseriesrendercache.cpp, line 32, as _ZN24SurfaceSeriesRenderCacheD2Ev
inline SurfaceSeriesRenderCache::~SurfaceSeriesRenderCache()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/surfaceseriesrendercache.cpp, line 36, as _ZN24SurfaceSeriesRenderCache8populateEb
inline void SurfaceSeriesRenderCache::populate(bool newSeries)
{
    SeriesRenderCache::populate(newSeries);

    QSurface3DSeries::DrawFlags drawMode = series()->drawMode();
    m_surfaceVisible = drawMode.testFlag(QSurface3DSeries::DrawSurface);
    m_surfaceGridVisible = drawMode.testFlag(QSurface3DSeries::DrawWireframe);
    QColor lineColor = series()->wireframeColor();
    m_surfaceObj->setLineColor(lineColor);
    m_sliceSurfaceObj->setLineColor(lineColor);

    if (m_flatChangeAllowed && m_surfaceFlatShading != series()->isFlatShadingEnabled()) {
        m_surfaceFlatShading = series()->isFlatShadingEnabled();
        m_flatStatusDirty = true;
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/surfaceseriesrendercache.cpp, line 53, as _ZN24SurfaceSeriesRenderCache7cleanupEP13TextureHelper
inline void SurfaceSeriesRenderCache::cleanup(TextureHelper *texHelper)
{
    if (QOpenGLContext::currentContext()) {
        texHelper->deleteTexture(&m_selectionTexture);
        texHelper->deleteTexture(&m_surfaceTexture);
    }

    delete m_surfaceObj;
    delete m_sliceSurfaceObj;
    for (int i = 0; i < m_dataArray.size(); i++)
        delete m_dataArray.at(i);
    m_dataArray.clear();

    for (int i = 0; i < m_sliceDataArray.size(); i++)
        delete m_sliceDataArray.at(i);
    m_sliceDataArray.clear();

    delete m_sliceSelectionPointer;
    delete m_mainSelectionPointer;

    SeriesRenderCache::cleanup(texHelper);
}
//  -----------------------------------------------------------------------

//  A SurfaceSeriesRenderCache that Python can take functions over in. Every SurfaceSeriesRenderCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteSurfaceSeriesRenderCacheCall0)(const void *, bool, int *);
typedef void (*CuteSurfaceSeriesRenderCacheCall1)(const void *, TextureHelper *, int *);
class CuteSurfaceSeriesRenderCache : public SurfaceSeriesRenderCache {
public:
  using SurfaceSeriesRenderCache::SurfaceSeriesRenderCache;
  CuteSurfaceSeriesRenderCache(const SurfaceSeriesRenderCache &other) : SurfaceSeriesRenderCache(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17SeriesRenderCache8populateEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17SeriesRenderCache7cleanupEP13TextureHelper")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void SurfaceSeriesRenderCache::populate(bool newSeries)
  void populate(bool newSeries) override {
    if (taken[0]) {
      int handled = 0;
      CuteSurfaceSeriesRenderCacheCall0 call = reinterpret_cast<CuteSurfaceSeriesRenderCacheCall0>(taken[0]);
      call(this, newSeries, &handled);
      if (handled) return;
    }
    SurfaceSeriesRenderCache::populate(newSeries);
  }

  //  void SurfaceSeriesRenderCache::cleanup(TextureHelper *texHelper)
  void cleanup(TextureHelper *texHelper) override {
    if (taken[1]) {
      int handled = 0;
      CuteSurfaceSeriesRenderCacheCall1 call = reinterpret_cast<CuteSurfaceSeriesRenderCacheCall1>(taken[1]);
      call(this, texHelper, &handled);
      if (handled) return;
    }
    SurfaceSeriesRenderCache::cleanup(texHelper);
  }
};

//  SurfaceSeriesRenderCache::~SurfaceSeriesRenderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCacheD1Ev(
    SurfaceSeriesRenderCache *self) {
  delete self;
}

//  void SurfaceSeriesRenderCache::populate(bool newSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache8populateEb(
    SurfaceSeriesRenderCache *self,
    bool newSeries) {
  self->populate(newSeries);
}

//  void SurfaceSeriesRenderCache::cleanup(TextureHelper *texHelper)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache7cleanupEP13TextureHelper(
    SurfaceSeriesRenderCache *self,
    TextureHelper *texHelper) {
  self->cleanup(texHelper);
}

//  bool SurfaceSeriesRenderCache::surfaceVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache14surfaceVisibleEv(
    const SurfaceSeriesRenderCache *self) {
  return self->surfaceVisible();
}

//  bool SurfaceSeriesRenderCache::surfaceGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache18surfaceGridVisibleEv(
    const SurfaceSeriesRenderCache *self) {
  return self->surfaceGridVisible();
}

//  bool SurfaceSeriesRenderCache::isFlatShadingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache20isFlatShadingEnabledEv(
    const SurfaceSeriesRenderCache *self) {
  return self->isFlatShadingEnabled();
}

//  void SurfaceSeriesRenderCache::setFlatShadingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache21setFlatShadingEnabledEb(
    SurfaceSeriesRenderCache *self,
    bool enabled) {
  self->setFlatShadingEnabled(enabled);
}

//  void SurfaceSeriesRenderCache::setFlatChangeAllowed(bool allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache20setFlatChangeAllowedEb(
    SurfaceSeriesRenderCache *self,
    bool allowed) {
  self->setFlatChangeAllowed(allowed);
}

//  SurfaceObject *SurfaceSeriesRenderCache::surfaceObject()
extern "C" Q_DECL_EXPORT
SurfaceObject *ritual_ZN24SurfaceSeriesRenderCache13surfaceObjectEv(
    SurfaceSeriesRenderCache *self) {
  return self->surfaceObject();
}

//  SurfaceObject *SurfaceSeriesRenderCache::sliceSurfaceObject()
extern "C" Q_DECL_EXPORT
SurfaceObject *ritual_ZN24SurfaceSeriesRenderCache18sliceSurfaceObjectEv(
    SurfaceSeriesRenderCache *self) {
  return self->sliceSurfaceObject();
}

//  const QRect &SurfaceSeriesRenderCache::sampleSpace() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24SurfaceSeriesRenderCache11sampleSpaceEv(
    const SurfaceSeriesRenderCache *self) {
  return new QRect(self->sampleSpace());
}

//  void SurfaceSeriesRenderCache::setSampleSpace(const QRect &sampleSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache14setSampleSpaceERK5QRect(
    SurfaceSeriesRenderCache *self,
    const QRect *sampleSpace) {
  self->setSampleSpace(*sampleSpace);
}

//  QSurface3DSeries *SurfaceSeriesRenderCache::series() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK24SurfaceSeriesRenderCache6seriesEv(
    const SurfaceSeriesRenderCache *self) {
  return self->series();
}

//  bool SurfaceSeriesRenderCache::renderable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache10renderableEv(
    const SurfaceSeriesRenderCache *self) {
  return self->renderable();
}

//  void SurfaceSeriesRenderCache::setSelectionTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache19setSelectionTextureEj(
    SurfaceSeriesRenderCache *self,
    GLuint texture) {
  self->setSelectionTexture(texture);
}

//  void SurfaceSeriesRenderCache::setSelectionIdRange(uint start, uint end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache19setSelectionIdRangeEjj(
    SurfaceSeriesRenderCache *self,
    uint start,
    uint end) {
  self->setSelectionIdRange(start, end);
}

//  uint SurfaceSeriesRenderCache::selectionIdStart() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK24SurfaceSeriesRenderCache16selectionIdStartEv(
    const SurfaceSeriesRenderCache *self) {
  return self->selectionIdStart();
}

//  bool SurfaceSeriesRenderCache::isWithinIdRange(uint selection) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache15isWithinIdRangeEj(
    const SurfaceSeriesRenderCache *self,
    uint selection) {
  return self->isWithinIdRange(selection);
}

//  bool SurfaceSeriesRenderCache::isFlatStatusDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache17isFlatStatusDirtyEv(
    const SurfaceSeriesRenderCache *self) {
  return self->isFlatStatusDirty();
}

//  void SurfaceSeriesRenderCache::setFlatStatusDirty(bool status)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache18setFlatStatusDirtyEb(
    SurfaceSeriesRenderCache *self,
    bool status) {
  self->setFlatStatusDirty(status);
}

//  void SurfaceSeriesRenderCache::setMVPMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache12setMVPMatrixERK10QMatrix4x4(
    SurfaceSeriesRenderCache *self,
    const QMatrix4x4 *matrix) {
  self->setMVPMatrix(*matrix);
}

//  const QMatrix4x4 &SurfaceSeriesRenderCache::MVPMatrix()
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN24SurfaceSeriesRenderCache9MVPMatrixEv(
    SurfaceSeriesRenderCache *self) {
  return new QMatrix4x4(self->MVPMatrix());
}

//  void SurfaceSeriesRenderCache::setSliceSelectionPointer(SelectionPointer
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache24setSliceSelectionPointerEP16SelectionPointer(
    SurfaceSeriesRenderCache *self,
    SelectionPointer *pointer) {
  self->setSliceSelectionPointer(pointer);
}

//  SelectionPointer *SurfaceSeriesRenderCache::sliceSelectionPointer() const
extern "C" Q_DECL_EXPORT
SelectionPointer *ritual_ZNK24SurfaceSeriesRenderCache21sliceSelectionPointerEv(
    const SurfaceSeriesRenderCache *self) {
  return self->sliceSelectionPointer();
}

//  void SurfaceSeriesRenderCache::setMainSelectionPointer(SelectionPointer
//      *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache23setMainSelectionPointerEP16SelectionPointer(
    SurfaceSeriesRenderCache *self,
    SelectionPointer *pointer) {
  self->setMainSelectionPointer(pointer);
}

//  SelectionPointer *SurfaceSeriesRenderCache::mainSelectionPointer() const
extern "C" Q_DECL_EXPORT
SelectionPointer *ritual_ZNK24SurfaceSeriesRenderCache20mainSelectionPointerEv(
    const SurfaceSeriesRenderCache *self) {
  return self->mainSelectionPointer();
}

//  void SurfaceSeriesRenderCache::setSlicePointerActivity(bool activity)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache23setSlicePointerActivityEb(
    SurfaceSeriesRenderCache *self,
    bool activity) {
  self->setSlicePointerActivity(activity);
}

//  bool SurfaceSeriesRenderCache::slicePointerActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache18slicePointerActiveEv(
    const SurfaceSeriesRenderCache *self) {
  return self->slicePointerActive();
}

//  void SurfaceSeriesRenderCache::setMainPointerActivity(bool activity)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache22setMainPointerActivityEb(
    SurfaceSeriesRenderCache *self,
    bool activity) {
  self->setMainPointerActivity(activity);
}

//  bool SurfaceSeriesRenderCache::mainPointerActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24SurfaceSeriesRenderCache17mainPointerActiveEv(
    const SurfaceSeriesRenderCache *self) {
  return self->mainPointerActive();
}

//  void SurfaceSeriesRenderCache::setSurfaceTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24SurfaceSeriesRenderCache17setSurfaceTextureEj(
    SurfaceSeriesRenderCache *self,
    GLuint texture) {
  self->setSurfaceTexture(texture);
}

//  a Python function taken by a CuteSurfaceSeriesRenderCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SurfaceSeriesRenderCache(
    SurfaceSeriesRenderCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteSurfaceSeriesRenderCache *>(self)->take(key, call);
}
