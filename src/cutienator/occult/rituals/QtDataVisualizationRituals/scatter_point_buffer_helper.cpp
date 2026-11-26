//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/scatterpointbufferhelper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/scatterpointbufferhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#include <QtDataVisualization/private/scatterpointbufferhelper_p.h>
#include <QtGui/QVector2D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 43, as _ZN20AbstractObjectHelper5uvBufEv
inline GLuint AbstractObjectHelper::uvBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_uvbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 8, as _ZN20AbstractObjectHelperC2Ev
inline AbstractObjectHelper::AbstractObjectHelper()
    : m_vertexbuffer(0),
      m_normalbuffer(0),
      m_uvbuffer(0),
      m_elementbuffer(0),
      m_indexCount(0),
      m_meshDataLoaded(false)
{
    initializeOpenGLFunctions();
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterpointbufferhelper.cpp, line 17, as _ZN24ScatterPointBufferHelperD2Ev
inline ScatterPointBufferHelper::~ScatterPointBufferHelper()
{
    if (QOpenGLContext::currentContext())
        glDeleteBuffers(1, &m_pointbuffer);
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterpointbufferhelper.cpp, line 23, as _ZN24ScatterPointBufferHelper8pointBufEv
inline GLuint ScatterPointBufferHelper::pointBuf()
{
    if (!m_meshDataLoaded)
        qFatal("No loaded object");
    return m_pointbuffer;
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterpointbufferhelper.cpp, line 49, as _ZN24ScatterPointBufferHelper8popPointEv
inline void ScatterPointBufferHelper::popPoint()
{
    if (m_oldRemoveIndex >= 0) {
        glBindBuffer(GL_ARRAY_BUFFER, m_pointbuffer);
        glBufferSubData(GL_ARRAY_BUFFER, m_oldRemoveIndex * sizeof(QVector3D),
                        sizeof(QVector3D), &m_bufferedPoints.at(m_oldRemoveIndex));
        glBindBuffer(GL_ARRAY_BUFFER, 0);
    }

    m_oldRemoveIndex = -1;
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterpointbufferhelper.cpp, line 142, as _ZN24ScatterPointBufferHelper9updateUVsEP24ScatterSeriesRenderCache
inline void ScatterPointBufferHelper::updateUVs(ScatterSeriesRenderCache *cache)
{
    // It may be that the buffer hasn't yet been initialized, in case the entire series was
    // hidden items. No need to update in that case.
    if (m_indexCount > 0) {
        QList<QVector2D> buffered_uvs;
        createRangeGradientUVs(cache, buffered_uvs);

        if (buffered_uvs.size()) {
            if (!m_uvbuffer)
                glGenBuffers(1, &m_uvbuffer);

            int updateSize = cache->updateIndices().size();
            glBindBuffer(GL_ARRAY_BUFFER, m_uvbuffer);
            if (updateSize) {
                for (int i = 0; i < updateSize; i++) {
                    int index = cache->updateIndices().at(i);
                    glBufferSubData(GL_ARRAY_BUFFER, index * sizeof(QVector2D),
                                    sizeof(QVector2D), &buffered_uvs.at(i));

                }
            } else {
                glBufferData(GL_ARRAY_BUFFER, buffered_uvs.size() * sizeof(QVector2D),
                             &buffered_uvs.at(0), GL_STATIC_DRAW);
            }

            glBindBuffer(GL_ARRAY_BUFFER, 0);
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterpointbufferhelper.cpp, line 173, as _ZN24ScatterPointBufferHelper22createRangeGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DE
inline void ScatterPointBufferHelper::createRangeGradientUVs(ScatterSeriesRenderCache *cache,
                                                      QList<QVector2D> &buffered_uvs)
{
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const bool updateAll = (cache->updateIndices().size() == 0);
    const int updateSize = updateAll ? renderArray.size() : cache->updateIndices().size();
    buffered_uvs.resize(updateSize);

    QVector2D uv;
    uv.setX(0.0f);
    for (int i = 0; i < updateSize; i++) {
        int index = updateAll ? i : cache->updateIndices().at(i);
        const ScatterRenderItem &item = renderArray.at(index);

        float y = ((item.translation().y() + m_scaleY) * 0.5f) / m_scaleY;
        uv.setY(y);
        buffered_uvs[i] = uv;
    }
}
//  -----------------------------------------------------------------------

//  A ScatterPointBufferHelper that Python can take functions over in. Every ScatterPointBufferHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef GLuint (*CuteScatterPointBufferHelperCall0)(const void *, int *);
class CuteScatterPointBufferHelper : public ScatterPointBufferHelper {
public:
  using ScatterPointBufferHelper::ScatterPointBufferHelper;
  CuteScatterPointBufferHelper(const ScatterPointBufferHelper & other) : ScatterPointBufferHelper(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20AbstractObjectHelper5uvBufEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  GLuint AbstractObjectHelper::uvBuf()
  GLuint uvBuf() override {
    if (taken[0]) {
      int handled = 0;
      CuteScatterPointBufferHelperCall0 call = reinterpret_cast<CuteScatterPointBufferHelperCall0>(taken[0]);
      GLuint given = call(this, &handled);
      if (handled) return given;
    }
    return AbstractObjectHelper::uvBuf();
  }
};

//  ScatterPointBufferHelper::~ScatterPointBufferHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterPointBufferHelperD1Ev(
    ScatterPointBufferHelper *self) {
  delete self;
}

//  GLuint ScatterPointBufferHelper::pointBuf()
extern "C" Q_DECL_EXPORT
GLuint ritual_ZN24ScatterPointBufferHelper8pointBufEv(
    ScatterPointBufferHelper *self) {
  return self->pointBuf();
}

//  void ScatterPointBufferHelper::popPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterPointBufferHelper8popPointEv(
    ScatterPointBufferHelper *self) {
  self->popPoint();
}

//  void ScatterPointBufferHelper::setScaleY(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterPointBufferHelper9setScaleYEf(
    ScatterPointBufferHelper *self,
    float scale) {
  self->setScaleY(scale);
}

//  void ScatterPointBufferHelper::updateUVs(ScatterSeriesRenderCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterPointBufferHelper9updateUVsEP24ScatterSeriesRenderCache(
    ScatterPointBufferHelper *self,
    ScatterSeriesRenderCache *cache) {
  self->updateUVs(cache);
}

//  void
//      ScatterPointBufferHelper::createRangeGradientUVs(ScatterSeriesRenderC
//      ache *cache, QList<QVector2D> &buffered_uvs)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ScatterPointBufferHelper22createRangeGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DE(
    ScatterPointBufferHelper *self,
    ScatterSeriesRenderCache *cache,
    QList<QVector2D> *buffered_uvs) {
  self->createRangeGradientUVs(cache, *buffered_uvs);
}

//  a Python function taken by a CuteScatterPointBufferHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ScatterPointBufferHelper(
    ScatterPointBufferHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteScatterPointBufferHelper *>(self)->take(key, call);
}
