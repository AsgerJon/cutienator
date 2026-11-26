//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/seriesrendercache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/seriesrendercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/seriesrendercache_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
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

//  from ../qtdatavis3d/src/datavisualization/engine/seriesrendercache.cpp, line 30, as _ZN17SeriesRenderCacheD2Ev
inline SeriesRenderCache::~SeriesRenderCache()
{
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

//  A SeriesRenderCache that Python can take functions over in. Every SeriesRenderCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteSeriesRenderCacheCall0)(const void *, bool, int *);
typedef void (*CuteSeriesRenderCacheCall1)(const void *, TextureHelper *, int *);
class CuteSeriesRenderCache : public SeriesRenderCache {
public:
  using SeriesRenderCache::SeriesRenderCache;
  CuteSeriesRenderCache(const SeriesRenderCache & other) : SeriesRenderCache(other) {}
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

  //  void SeriesRenderCache::populate(bool newSeries)
  void populate(bool newSeries) override {
    if (taken[0]) {
      int handled = 0;
      CuteSeriesRenderCacheCall0 call = reinterpret_cast<CuteSeriesRenderCacheCall0>(taken[0]);
      call(this, newSeries, &handled);
      if (handled) return;
    }
    SeriesRenderCache::populate(newSeries);
  }

  //  void SeriesRenderCache::cleanup(TextureHelper *texHelper)
  void cleanup(TextureHelper *texHelper) override {
    if (taken[1]) {
      int handled = 0;
      CuteSeriesRenderCacheCall1 call = reinterpret_cast<CuteSeriesRenderCacheCall1>(taken[1]);
      call(this, texHelper, &handled);
      if (handled) return;
    }
    SeriesRenderCache::cleanup(texHelper);
  }
};

//  SeriesRenderCache::~SeriesRenderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCacheD1Ev(SeriesRenderCache *self) {
  delete self;
}

//  void SeriesRenderCache::populate(bool newSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache8populateEb(
    SeriesRenderCache *self,
    bool newSeries) {
  self->populate(newSeries);
}

//  void SeriesRenderCache::cleanup(TextureHelper *texHelper)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache7cleanupEP13TextureHelper(
    SeriesRenderCache *self,
    TextureHelper *texHelper) {
  self->cleanup(texHelper);
}

//  QAbstract3DSeries *SeriesRenderCache::series() const
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_ZNK17SeriesRenderCache6seriesEv(
    const SeriesRenderCache *self) {
  return self->series();
}

//  const QAbstract3DSeries::Mesh &SeriesRenderCache::mesh() const
extern "C" Q_DECL_EXPORT
const QAbstract3DSeries::Mesh *ritual_ZNK17SeriesRenderCache4meshEv(
    const SeriesRenderCache *self) {
  return &(self->mesh());
}

//  const QQuaternion &SeriesRenderCache::meshRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK17SeriesRenderCache12meshRotationEv(
    const SeriesRenderCache *self) {
  return new QQuaternion(self->meshRotation());
}

//  void SeriesRenderCache::setMeshRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache15setMeshRotationERK11QQuaternion(
    SeriesRenderCache *self,
    const QQuaternion *rotation) {
  self->setMeshRotation(*rotation);
}

//  ObjectHelper *SeriesRenderCache::object() const
extern "C" Q_DECL_EXPORT
ObjectHelper *ritual_ZNK17SeriesRenderCache6objectEv(
    const SeriesRenderCache *self) {
  return self->object();
}

//  const Q3DTheme::ColorStyle &SeriesRenderCache::colorStyle() const
extern "C" Q_DECL_EXPORT
const Q3DTheme::ColorStyle *ritual_ZNK17SeriesRenderCache10colorStyleEv(
    const SeriesRenderCache *self) {
  return &(self->colorStyle());
}

//  const QVector4D &SeriesRenderCache::baseColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK17SeriesRenderCache9baseColorEv(
    const SeriesRenderCache *self) {
  return new QVector4D(self->baseColor());
}

//  const GLuint &SeriesRenderCache::baseUniformTexture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK17SeriesRenderCache18baseUniformTextureEv(
    const SeriesRenderCache *self) {
  return self->baseUniformTexture();
}

//  const GLuint &SeriesRenderCache::baseGradientTexture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK17SeriesRenderCache19baseGradientTextureEv(
    const SeriesRenderCache *self) {
  return self->baseGradientTexture();
}

//  const QImage &SeriesRenderCache::gradientImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK17SeriesRenderCache13gradientImageEv(
    const SeriesRenderCache *self) {
  return new QImage(self->gradientImage());
}

//  const QVector4D &SeriesRenderCache::singleHighlightColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK17SeriesRenderCache20singleHighlightColorEv(
    const SeriesRenderCache *self) {
  return new QVector4D(self->singleHighlightColor());
}

//  const GLuint &SeriesRenderCache::singleHighlightGradientTexture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK17SeriesRenderCache30singleHighlightGradientTextureEv(
    const SeriesRenderCache *self) {
  return self->singleHighlightGradientTexture();
}

//  const QVector4D &SeriesRenderCache::multiHighlightColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK17SeriesRenderCache19multiHighlightColorEv(
    const SeriesRenderCache *self) {
  return new QVector4D(self->multiHighlightColor());
}

//  const GLuint &SeriesRenderCache::multiHighlightGradientTexture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK17SeriesRenderCache29multiHighlightGradientTextureEv(
    const SeriesRenderCache *self) {
  return self->multiHighlightGradientTexture();
}

//  const QString &SeriesRenderCache::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17SeriesRenderCache4nameEv(
    const SeriesRenderCache *self) {
  return new QString(self->name());
}

//  const QString &SeriesRenderCache::itemLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17SeriesRenderCache9itemLabelEv(
    const SeriesRenderCache *self) {
  return new QString(self->itemLabel());
}

//  void SeriesRenderCache::setValid(bool valid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache8setValidEb(
    SeriesRenderCache *self,
    bool valid) {
  self->setValid(valid);
}

//  bool SeriesRenderCache::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17SeriesRenderCache7isValidEv(const SeriesRenderCache *self) {
  return self->isValid();
}

//  bool SeriesRenderCache::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17SeriesRenderCache9isVisibleEv(
    const SeriesRenderCache *self) {
  return self->isVisible();
}

//  void SeriesRenderCache::setDataDirty(bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache12setDataDirtyEb(
    SeriesRenderCache *self,
    bool state) {
  self->setDataDirty(state);
}

//  bool SeriesRenderCache::dataDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17SeriesRenderCache9dataDirtyEv(
    const SeriesRenderCache *self) {
  return self->dataDirty();
}

//  void SeriesRenderCache::setStaticObjectUVDirty(bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17SeriesRenderCache22setStaticObjectUVDirtyEb(
    SeriesRenderCache *self,
    bool state) {
  self->setStaticObjectUVDirty(state);
}

//  bool SeriesRenderCache::staticObjectUVDirty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17SeriesRenderCache19staticObjectUVDirtyEv(
    SeriesRenderCache *self) {
  return self->staticObjectUVDirty();
}

//  a Python function taken by a CuteSeriesRenderCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SeriesRenderCache(
    SeriesRenderCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteSeriesRenderCache *>(self)->take(key, call);
}
