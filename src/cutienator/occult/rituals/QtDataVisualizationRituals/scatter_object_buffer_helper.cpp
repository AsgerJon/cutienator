//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/scatterobjectbufferhelper_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals whose code, copied from
//  Qt's source, reads constant data Qt keeps to itself
//  ('ScatterObjectBufferHelper::itemScaler'), copied with it 'inline' from
//  Qt's source, drafted by a copy of the generator that takes it along. Kept
//  as it is when the generator runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/scatterobjectbufferhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#include <QtDataVisualization/private/scatterobjectbufferhelper_p.h>
#include <QtDataVisualization/private/objecthelper_p.h>
#include <QtGui/QVector2D>
#include <QtGui/QMatrix4x4>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
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

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 22, as _ZN25ScatterObjectBufferHelperD2Ev
inline ScatterObjectBufferHelper::~ScatterObjectBufferHelper()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 15, as _ZN25ScatterObjectBufferHelper10itemScalerE
inline const GLfloat ScatterObjectBufferHelper::itemScaler = 3.0f;

//  from ../qtdatavis3d/src/datavisualization/utils/abstractobjecthelper.cpp, line 19, as _ZN20AbstractObjectHelperD2Ev
inline AbstractObjectHelper::~AbstractObjectHelper()
{
    if (QOpenGLContext::currentContext()) {
        glDeleteBuffers(1, &m_vertexbuffer);
        glDeleteBuffers(1, &m_uvbuffer);
        glDeleteBuffers(1, &m_normalbuffer);
        glDeleteBuffers(1, &m_elementbuffer);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 17, as _ZN25ScatterObjectBufferHelperC1Ev
inline ScatterObjectBufferHelper::ScatterObjectBufferHelper()
    : m_scaleY(0.0f)
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 26, as _ZN25ScatterObjectBufferHelper8fullLoadEP24ScatterSeriesRenderCached
inline void ScatterObjectBufferHelper::fullLoad(ScatterSeriesRenderCache *cache, qreal dotScale)
{
    m_indexCount = 0;

    ObjectHelper *dotObj = cache->object();
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const uint renderArraySize = renderArray.size();

    if (renderArraySize == 0)
        return;  // No use to go forward

    uint itemCount = 0;
    QQuaternion seriesRotation(cache->meshRotation());

    if (m_meshDataLoaded) {
        // Delete old data
        glDeleteBuffers(1, &m_vertexbuffer);
        glDeleteBuffers(1, &m_uvbuffer);
        glDeleteBuffers(1, &m_normalbuffer);
        glDeleteBuffers(1, &m_elementbuffer);
        m_vertexbuffer = 0;
        m_uvbuffer = 0;
        m_normalbuffer = 0;
        m_elementbuffer = 0;
        m_meshDataLoaded = false;
    }

    // Index vertices
    const QList<GLuint> indices = dotObj->indices();
    const QList<QVector3D> indexed_vertices = dotObj->indexedvertices();
    const QList<QVector2D> indexed_uvs = dotObj->indexedUVs();
    const QList<QVector3D> indexed_normals = dotObj->indexedNormals();
    const int indicesCount = indices.size();
    const int verticeCount = indexed_vertices.size();
    const int uvsCount = indexed_uvs.size();
    const int normalsCount = indexed_normals.size();

    float itemSize = cache->itemSize() / itemScaler;
    if (itemSize == 0.0f)
        itemSize = dotScale;
    QVector3D modelScaler(itemSize, itemSize, itemSize);
    QMatrix4x4 modelMatrix;
    if (!seriesRotation.isIdentity()) {
        QMatrix4x4 matrix;
        matrix.rotate(seriesRotation);
        modelMatrix = matrix.transposed();
    }
    modelMatrix.scale(modelScaler);

    QList<QVector3D> scaled_vertices;
    scaled_vertices.resize(verticeCount);
    for (int i = 0; i < verticeCount; i++)
        scaled_vertices[i] = (QVector4D(indexed_vertices[i]) * modelMatrix).toVector3D();

    QList<GLuint> buffered_indices;
    QList<QVector3D> buffered_vertices;
    QList<QVector2D> buffered_uvs;
    QList<QVector3D> buffered_normals;

    buffered_indices.resize(indicesCount * renderArraySize);
    buffered_vertices.resize(verticeCount * renderArraySize);
    buffered_normals.resize(normalsCount * renderArraySize);
    buffered_uvs.resize(uvsCount * renderArraySize);

    if (cache->colorStyle() == Q3DTheme::ColorStyleRangeGradient)
        createRangeGradientUVs(cache, buffered_uvs);
    else if (cache->colorStyle() == Q3DTheme::ColorStyleObjectGradient)
        createObjectGradientUVs(cache, buffered_uvs, indexed_vertices);

    QVector2D dummyUV(0.0f, 0.0f);

    cache->bufferIndices().resize(renderArraySize);

    for (uint i = 0; i < renderArraySize; i++) {
        const ScatterRenderItem &item = renderArray.at(i);
        if (!item.isVisible())
            continue;
        else
            cache->bufferIndices()[i] = itemCount;

        int offset = itemCount * verticeCount;
        if (item.rotation().isIdentity()) {
            for (int j = 0; j < verticeCount; j++) {
                buffered_vertices[j + offset] = scaled_vertices[j] + item.translation();
                buffered_normals[j + offset] = indexed_normals[j];
            }
        } else {
            QMatrix4x4 matrix;
            QQuaternion totalRotation = seriesRotation * item.rotation();
            matrix.rotate(totalRotation);
            matrix.scale(modelScaler);
            QMatrix4x4 itModelMatrix = matrix.inverted();
            modelMatrix = matrix.transposed(); // Because of row-column major difference

            for (int j = 0; j < verticeCount; j++) {
                buffered_vertices[j + offset]
                        = (QVector4D(indexed_vertices[j]) * modelMatrix).toVector3D()
                        + item.translation();
                buffered_normals[j + offset]
                        = (QVector4D(indexed_normals[j]) * itModelMatrix).toVector3D();
            }
        }

        if (cache->colorStyle() == Q3DTheme::ColorStyleUniform) {
            offset = itemCount * uvsCount;
            for (int j = 0; j < uvsCount; j++)
                buffered_uvs[j + offset] = dummyUV;
        }

        int offsetVertice = itemCount * verticeCount;
        offset = itemCount * indicesCount;
        for (int j = 0; j < indicesCount; j++)
            buffered_indices[j + offset] = GLuint(indices[j] + offsetVertice);

        itemCount++;
    }

    m_indexCount = indicesCount * itemCount;

    if (itemCount > 0) {
        glGenBuffers(1, &m_vertexbuffer);
        glBindBuffer(GL_ARRAY_BUFFER, m_vertexbuffer);
        glBufferData(GL_ARRAY_BUFFER, verticeCount * itemCount * sizeof(QVector3D),
                     &buffered_vertices.at(0),
                     GL_STATIC_DRAW);

        glGenBuffers(1, &m_normalbuffer);
        glBindBuffer(GL_ARRAY_BUFFER, m_normalbuffer);
        glBufferData(GL_ARRAY_BUFFER, normalsCount * itemCount * sizeof(QVector3D),
                     &buffered_normals.at(0),
                     GL_STATIC_DRAW);

        glGenBuffers(1, &m_uvbuffer);
        glBindBuffer(GL_ARRAY_BUFFER, m_uvbuffer);
        glBufferData(GL_ARRAY_BUFFER, uvsCount * itemCount * sizeof(QVector2D),
                     &buffered_uvs.at(0), GL_STATIC_DRAW);

        glGenBuffers(1, &m_elementbuffer);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_elementbuffer);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indicesCount * itemCount * sizeof(GLint),
                     &buffered_indices.at(0), GL_STATIC_DRAW);

        glBindBuffer(GL_ARRAY_BUFFER, 0);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

        m_meshDataLoaded = true;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 286, as _ZN25ScatterObjectBufferHelper6updateEP24ScatterSeriesRenderCached
inline void ScatterObjectBufferHelper::update(ScatterSeriesRenderCache *cache, qreal dotScale)
{
    ObjectHelper *dotObj = cache->object();
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const bool updateAll = (cache->updateIndices().size() == 0);
    const int updateSize = updateAll ? renderArray.size() : cache->updateIndices().size();
    QQuaternion seriesRotation(cache->meshRotation());

    if (!updateSize)
        return;

    // Index vertices
    const QList<QVector3D> indexed_vertices = dotObj->indexedvertices();
    int verticeCount = indexed_vertices.size();

    float itemSize = cache->itemSize() / itemScaler;
    if (itemSize == 0.0f)
        itemSize = dotScale;
    QVector3D modelScaler(itemSize, itemSize, itemSize);
    QMatrix4x4 modelMatrix;
    if (!seriesRotation.isIdentity()) {
        QMatrix4x4 matrix;
        matrix.rotate(seriesRotation);
        modelMatrix = matrix.transposed();
    }
    modelMatrix.scale(modelScaler);

    QList<QVector3D> scaled_vertices;
    scaled_vertices.resize(verticeCount);
    for (int i = 0; i < verticeCount; i++)
        scaled_vertices[i] = (QVector4D(indexed_vertices[i]) * modelMatrix).toVector3D();

    QList<QVector3D> buffered_vertices;
    buffered_vertices.resize(verticeCount * updateSize);

    int itemCount = 0;
    for (int i = 0; i < updateSize; i++) {
        int index = updateAll ? i : cache->updateIndices().at(i);
        const ScatterRenderItem &item = renderArray.at(index);
        if (!item.isVisible())
            continue;

        const int offset = itemCount * verticeCount;
        if (item.rotation().isIdentity()) {
            for (int j = 0; j < verticeCount; j++)
                buffered_vertices[j + offset] = scaled_vertices[j] + item.translation();
        } else {
            QMatrix4x4 matrix;
            matrix.rotate(seriesRotation * item.rotation());
            modelMatrix = matrix.transposed();
            modelMatrix.scale(modelScaler);

            for (int j = 0; j < verticeCount; j++) {
                buffered_vertices[j + offset]
                        = (QVector4D(indexed_vertices[j]) * modelMatrix).toVector3D()
                        + item.translation();
            }
        }
        itemCount++;
    }

    glBindBuffer(GL_ARRAY_BUFFER, m_vertexbuffer);
    int sizeOfItem = verticeCount * sizeof(QVector3D);
    if (updateAll) {
        if (itemCount) {
            glBufferData(GL_ARRAY_BUFFER, itemCount * sizeOfItem,
                         &buffered_vertices.at(0), GL_STATIC_DRAW);
        }
    } else {
        itemCount = 0;
        for (int i = 0; i < updateSize; i++) {
            int index = updateAll ? i : cache->updateIndices().at(i);
            if (renderArray.at(index).isVisible()) {
                glBufferSubData(GL_ARRAY_BUFFER, cache->bufferIndices().at(index) * sizeOfItem,
                                sizeOfItem, &buffered_vertices.at(itemCount * verticeCount));
                itemCount++;
            }
        }
    }
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    m_meshDataLoaded = true;
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 175, as _ZN25ScatterObjectBufferHelper9updateUVsEP24ScatterSeriesRenderCache
inline void ScatterObjectBufferHelper::updateUVs(ScatterSeriesRenderCache *cache)
{
    ObjectHelper *dotObj = cache->object();
    const int uvsCount = dotObj->indexedUVs().size();
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const bool updateAll = (cache->updateIndices().size() == 0);
    const int updateSize = updateAll ? renderArray.size() : cache->updateIndices().size();

    if (!updateSize)
        return;

    QList<QVector2D> buffered_uvs;
    buffered_uvs.resize(uvsCount * updateSize);

    uint itemCount = 0;
    if (cache->colorStyle() == Q3DTheme::ColorStyleRangeGradient) {
        itemCount = createRangeGradientUVs(cache, buffered_uvs);
    } else if (cache->colorStyle() == Q3DTheme::ColorStyleObjectGradient) {
        const QList<QVector3D> indexed_vertices = dotObj->indexedvertices();
        itemCount = createObjectGradientUVs(cache, buffered_uvs, indexed_vertices);
    }

    glBindBuffer(GL_ARRAY_BUFFER, m_uvbuffer);
    int itemSize = uvsCount * sizeof(QVector2D);
    if (cache->updateIndices().size()) {
        int pos = 0;
        for (int i = 0; i < updateSize; i++) {
            int index = cache->updateIndices().at(i);
            if (renderArray.at(index).isVisible()) {
                int dataPos = cache->bufferIndices().at(index);
                glBufferSubData(GL_ARRAY_BUFFER, itemSize * dataPos, itemSize,
                                &buffered_uvs.at(uvsCount * pos++));
            }
        }
    } else {
        glBufferData(GL_ARRAY_BUFFER, itemSize * itemCount, &buffered_uvs.at(0), GL_STATIC_DRAW);
    }
    glBindBuffer(GL_ARRAY_BUFFER, 0);
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 215, as _ZN25ScatterObjectBufferHelper22createRangeGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DE
inline uint ScatterObjectBufferHelper::createRangeGradientUVs(ScatterSeriesRenderCache *cache,
                                                       QList<QVector2D> &buffered_uvs)
{
    ObjectHelper *dotObj = cache->object();
    const int uvsCount = dotObj->indexedUVs().size();
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const bool updateAll = (cache->updateIndices().size() == 0);
    const int updateSize = updateAll ? renderArray.size() : cache->updateIndices().size();
    const float yAdjustment = 0.1f;
    const float flippedYAdjustment = 0.9f;

    QVector2D uv;
    uv.setX(0.0f);
    uint pos = 0;
    for (int i = 0; i < updateSize; i++) {
        int index = updateAll ? i : cache->updateIndices().at(i);
        const ScatterRenderItem &item = renderArray.at(index);
        if (!item.isVisible())
            continue;

        float y = ((item.translation().y() + m_scaleY) * 0.5f) / m_scaleY;

        // Avoid values near gradient texel boundary, as this causes artifacts
        // with some graphics cards.
        const float floorY = float(qFloor(y * gradientTextureHeight));
        const float diff = (y * gradientTextureHeight) - floorY;
        if (diff < yAdjustment)
            y += yAdjustment / gradientTextureHeight;
        else if (diff > flippedYAdjustment)
            y -= yAdjustment / gradientTextureHeight;
        uv.setY(y);

        int offset = pos * uvsCount;
        for (int j = 0; j < uvsCount; j++)
            buffered_uvs[j + offset] = uv;

        pos++;
    }

    return pos;
}

//  from ../qtdatavis3d/src/datavisualization/utils/scatterobjectbufferhelper.cpp, line 257, as _ZN25ScatterObjectBufferHelper23createObjectGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DERKS2_I9QVector3DE
inline uint ScatterObjectBufferHelper::createObjectGradientUVs(ScatterSeriesRenderCache *cache,
                                                        QList<QVector2D> &buffered_uvs,
                                                        const QList<QVector3D> &indexed_vertices)
{
    ObjectHelper *dotObj = cache->object();
    const int uvsCount = dotObj->indexedUVs().size();
    const ScatterRenderItemArray &renderArray = cache->renderArray();
    const uint renderArraySize = renderArray.size();

    QVector2D uv;
    uv.setX(0.0f);
    uint pos = 0;
    for (uint i = 0; i < renderArraySize; i++) {
        const ScatterRenderItem &item = renderArray.at(i);
        if (!item.isVisible())
            continue;

        int offset = pos * uvsCount;
        for (int j = 0; j < uvsCount; j++) {
            uv.setY((indexed_vertices.at(j).y() + 1.0f) / 2.0f);
            buffered_uvs[j + offset] = uv;
        }

        pos++;
    }

    return pos;
}
//  -----------------------------------------------------------------------

//  A ScatterObjectBufferHelper that Python can take functions over in. Every ScatterObjectBufferHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef GLuint (*CuteScatterObjectBufferHelperCall0)(const void *, int *);
class CuteScatterObjectBufferHelper : public ScatterObjectBufferHelper {
public:
  using ScatterObjectBufferHelper::ScatterObjectBufferHelper;
  CuteScatterObjectBufferHelper(const ScatterObjectBufferHelper & other) : ScatterObjectBufferHelper(other) {}
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
      CuteScatterObjectBufferHelperCall0 call = reinterpret_cast<CuteScatterObjectBufferHelperCall0>(taken[0]);
      GLuint given = call(this, &handled);
      if (handled) return given;
    }
    return AbstractObjectHelper::uvBuf();
  }
};

//  ScatterObjectBufferHelper::ScatterObjectBufferHelper()
extern "C" Q_DECL_EXPORT
ScatterObjectBufferHelper *ritual_ZN25ScatterObjectBufferHelperC1Ev() {
  return new CuteScatterObjectBufferHelper();
}

//  ScatterObjectBufferHelper::~ScatterObjectBufferHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN25ScatterObjectBufferHelperD1Ev(
    ScatterObjectBufferHelper *self) {
  delete self;
}

//  void ScatterObjectBufferHelper::fullLoad(ScatterSeriesRenderCache *cache,
//      qreal dotScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN25ScatterObjectBufferHelper8fullLoadEP24ScatterSeriesRenderCached(
    ScatterObjectBufferHelper *self,
    ScatterSeriesRenderCache *cache,
    qreal dotScale) {
  self->fullLoad(cache, dotScale);
}

//  void ScatterObjectBufferHelper::update(ScatterSeriesRenderCache *cache,
//      qreal dotScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN25ScatterObjectBufferHelper6updateEP24ScatterSeriesRenderCached(
    ScatterObjectBufferHelper *self,
    ScatterSeriesRenderCache *cache,
    qreal dotScale) {
  self->update(cache, dotScale);
}

//  void ScatterObjectBufferHelper::updateUVs(ScatterSeriesRenderCache
//      *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN25ScatterObjectBufferHelper9updateUVsEP24ScatterSeriesRenderCache(
    ScatterObjectBufferHelper *self,
    ScatterSeriesRenderCache *cache) {
  self->updateUVs(cache);
}

//  void ScatterObjectBufferHelper::setScaleY(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN25ScatterObjectBufferHelper9setScaleYEf(
    ScatterObjectBufferHelper *self,
    float scale) {
  self->setScaleY(scale);
}

//  uint ScatterObjectBufferHelper::createRangeGradientUVs(ScatterSeriesRende
//      rCache *cache, QList<QVector2D> &buffered_uvs)
extern "C" Q_DECL_EXPORT
uint ritual_ZN25ScatterObjectBufferHelper22createRangeGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DE(
    ScatterObjectBufferHelper *self,
    ScatterSeriesRenderCache *cache,
    QList<QVector2D> *buffered_uvs) {
  return self->createRangeGradientUVs(cache, *buffered_uvs);
}

//  uint ScatterObjectBufferHelper::createObjectGradientUVs(ScatterSeriesRend
//      erCache *cache, QList<QVector2D> &buffered_uvs, const
//      QList<QVector3D> &indexed_vertices)
extern "C" Q_DECL_EXPORT
uint ritual_ZN25ScatterObjectBufferHelper23createObjectGradientUVsEP24ScatterSeriesRenderCacheR5QListI9QVector2DERKS2_I9QVector3DE(
    ScatterObjectBufferHelper *self,
    ScatterSeriesRenderCache *cache,
    QList<QVector2D> *buffered_uvs,
    const QList<QVector3D> *indexed_vertices) {
  return self->createObjectGradientUVs(
      cache,
      *buffered_uvs,
      *indexed_vertices);
}

//  a Python function taken by a CuteScatterObjectBufferHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ScatterObjectBufferHelper(
    ScatterObjectBufferHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteScatterObjectBufferHelper *>(self)->take(key, call);
}
