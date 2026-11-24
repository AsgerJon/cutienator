//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceobject_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/surfaceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractobjecthelper_p.h>
#include <QtDataVisualization/private/surfaceobject_p.h>
#include <QtDataVisualization/private/surface3drenderer_p.h>
#include <QtGui/QVector2D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 899, as _ZN13SurfaceObject19createCoarseIndicesEPiRiiii
inline void SurfaceObject::createCoarseIndices(GLint *indices, int &p, int row, int upperRow, int j)
{
     if ((m_dataDimension == BothAscending) || (m_dataDimension == BothDescending)) {
        // Left triangle
        indices[p++] = row + j + 1;
        indices[p++] = upperRow + j;
        indices[p++] = row + j;

        // Right triangle
        indices[p++] = upperRow + j + 1;
        indices[p++] = upperRow + j;
        indices[p++] = row + j + 1;
    } else if (m_dataDimension == XDescending) {
        indices[p++] = upperRow + j;
        indices[p++] = upperRow + j + 1;
        indices[p++] = row + j;

        indices[p++] = row + j;
        indices[p++] = upperRow + j + 1;
        indices[p++] = row + j + 1;
    } else {
        // Left triangle
        indices[p++] = upperRow + j;
        indices[p++] = upperRow + j + 1;
        indices[p++] = row + j;

        // Right triangle
        indices[p++] = row + j;
        indices[p++] = upperRow + j + 1;
        indices[p++] = row + j + 1;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 783, as _ZN13SurfaceObject13createBuffersERK5QListI9QVector3DERKS0_I9QVector2DES4_PKi
inline void SurfaceObject::createBuffers(const QList<QVector3D> &vertices, const QList<QVector2D> &uvs,
                                  const QList<QVector3D> &normals, const GLint *indices)
{
    // Move to buffers
    glBindBuffer(GL_ARRAY_BUFFER, m_vertexbuffer);
    glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(QVector3D),
                 &vertices.at(0), GL_DYNAMIC_DRAW);

    glBindBuffer(GL_ARRAY_BUFFER, m_normalbuffer);
    glBufferData(GL_ARRAY_BUFFER, normals.size() * sizeof(QVector3D),
                 &normals.at(0), GL_DYNAMIC_DRAW);

    if (uvs.size()) {
        glBindBuffer(GL_ARRAY_BUFFER, m_uvbuffer);
        glBufferData(GL_ARRAY_BUFFER, uvs.size() * sizeof(QVector2D),
                     &uvs.at(0), GL_STATIC_DRAW);
    }

    if (indices) {
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_elementbuffer);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, m_indexCount * sizeof(GLint),
                     indices, GL_STATIC_DRAW);
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    m_meshDataLoaded = true;
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 391, as _ZN13SurfaceObject19createSmoothIndicesEiiii
inline void SurfaceObject::createSmoothIndices(int x, int y, int endX, int endY)
{
    if (endX >= m_columns)
        endX = m_columns - 1;
    if (endY >= m_rows)
        endY = m_rows - 1;
    if (x > endX)
        x = endX - 1;
    if (y > endY)
        y = endY - 1;

    m_indexCount = 6 * (endX - x) * (endY - y);
    GLint *indices = new GLint[m_indexCount];
    int p = 0;
    int rowEnd = endY * m_columns;
    for (int row = y * m_columns; row < rowEnd; row += m_columns) {
        for (int j = x; j < endX; j++) {
            if ((m_dataDimension == BothAscending) || (m_dataDimension == BothDescending)) {
                // Left triangle
                indices[p++] = row + j + 1;
                indices[p++] = row + m_columns + j;
                indices[p++] = row + j;

                // Right triangle
                indices[p++] = row + m_columns + j + 1;
                indices[p++] = row + m_columns + j;
                indices[p++] = row + j + 1;
            } else if (m_dataDimension == XDescending) {
                // Right triangle
                indices[p++] = row + m_columns + j;
                indices[p++] = row + m_columns + j + 1;
                indices[p++] = row + j;

                // Left triangle
                indices[p++] = row + j;
                indices[p++] = row + m_columns + j + 1;
                indices[p++] = row + j + 1;
            } else {
                // Left triangle
                indices[p++] = row + m_columns + j;
                indices[p++] = row + m_columns + j + 1;
                indices[p++] = row + j;

                // Right triangle
                indices[p++] = row + j;
                indices[p++] = row + m_columns + j + 1;
                indices[p++] = row + j + 1;

            }
        }
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_elementbuffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, m_indexCount * sizeof(GLint),
                 indices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

    delete[] indices;
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 693, as _ZN13SurfaceObject22createCoarseSubSectionEiiii
inline void SurfaceObject::createCoarseSubSection(int x, int y, int columns, int rows)
{
    if (columns > m_columns)
        columns = m_columns;
    if (rows > m_rows)
        rows = m_rows;
    if (x > columns)
        x = columns - 1;
    if (y > rows)
        y = rows - 1;

    int rowLimit = rows - 1;
    int doubleColumns = m_columns * 2 - 2;
    int doubleColumnsLimit = columns * 2 - 2;
    int rowColLimit = rowLimit * doubleColumns;
    m_indexCount = 6 * (columns - 1 - x) * (rowLimit - y);

    int p = 0;
    GLint *indices = new GLint[m_indexCount];
    for (int row = y * doubleColumns, upperRow = (y + 1) * doubleColumns;
         row < rowColLimit;
         row += doubleColumns, upperRow += doubleColumns) {
        for (int j = 2 * x; j < doubleColumnsLimit; j += 2)
            createCoarseIndices(indices, p, row, upperRow, j);
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_elementbuffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, m_indexCount * sizeof(GLint),
                 indices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

    delete[] indices;
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 452, as _ZN13SurfaceObject27createSmoothGridlineIndicesEiiii
inline void SurfaceObject::createSmoothGridlineIndices(int x, int y, int endX, int endY)
{
    if (endX >= m_columns)
        endX = m_columns - 1;
    if (endY >= m_rows)
        endY = m_rows - 1;
    if (x > endX)
        x = endX - 1;
    if (y > endY)
        y = endY - 1;

    int nColumns = endX - x + 1;
    int nRows = endY - y + 1;
    m_gridIndexCount = 2 * nColumns * (nRows - 1) + 2 * nRows * (nColumns - 1);
    GLint *gridIndices = new GLint[m_gridIndexCount];
    int p = 0;
    for (int i = y, row = m_columns * y; i <= endY; i++, row += m_columns) {
        for (int j = x; j < endX; j++) {
            gridIndices[p++] = row + j;
            gridIndices[p++] = row + j + 1;
        }
    }
    for (int i = y, row = m_columns * y; i < endY; i++, row += m_columns) {
        for (int j = x; j <= endX; j++) {
            gridIndices[p++] = row + j;
            gridIndices[p++] = row + j + m_columns;
        }
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_gridElementbuffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, m_gridIndexCount * sizeof(GLint),
                 gridIndices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

    delete[] gridIndices;
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 728, as _ZN13SurfaceObject27createCoarseGridlineIndicesEiiii
inline void SurfaceObject::createCoarseGridlineIndices(int x, int y, int endX, int endY)
{
    if (endX >= m_columns)
        endX = m_columns - 1;
    if (endY >= m_rows)
        endY = m_rows - 1;
    if (x > endX)
        x = endX - 1;
    if (y > endY)
        y = endY - 1;

    int nColumns = endX - x + 1;
    int nRows = endY - y + 1;
    int doubleEndX = endX * 2;
    int doubleColumns = m_columns * 2 - 2;
    int rowColLimit = endY * doubleColumns;

    m_gridIndexCount = 2 * nColumns * (nRows - 1) + 2 * nRows * (nColumns - 1);
    GLint *gridIndices = new GLint[m_gridIndexCount];
    int p = 0;

    for (int row = y * doubleColumns; row <= rowColLimit; row += doubleColumns) {
        for (int j = x * 2; j < doubleEndX; j += 2) {
            // Horizontal line
            gridIndices[p++] = row + j;
            gridIndices[p++] = row + j + 1;

            if (row < rowColLimit) {
                // Vertical line
                gridIndices[p++] = row + j;
                gridIndices[p++] = row + j + doubleColumns;
            }
        }
    }
    // The rightmost line separately, since there isn't double vertice
    for (int i = y * doubleColumns + doubleEndX - 1; i < rowColLimit; i += doubleColumns) {
        gridIndices[p++] = i;
        gridIndices[p++] = i  + doubleColumns;
    }

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_gridElementbuffer);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, m_gridIndexCount * sizeof(GLint),
                 gridIndices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);

    delete[] gridIndices;
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 777, as _ZN13SurfaceObject13uploadBuffersEv
inline void SurfaceObject::uploadBuffers()
{
    QList<QVector2D> uvs; // Empty dummy
    createBuffers(m_vertices, uvs, m_normals, 0);
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 877, as _ZN13SurfaceObject8vertexAtEii
inline QVector3D SurfaceObject::vertexAt(int column, int row)
{
    int pos = 0;
    if (m_surfaceType == Undefined || !m_vertices.size())
        return zeroVector;

    if (m_surfaceType == SurfaceFlat)
        pos = row * (m_columns * 2 - 2) + column * 2 - (column > 0);
    else
        pos = row * m_columns + column;
    return m_vertices.at(pos);
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 890, as _ZN13SurfaceObject5clearEv
inline void SurfaceObject::clear()
{
    m_gridIndexCount = 0;
    m_indexCount = 0;
    m_surfaceType = Undefined;
    m_vertices.clear();
    m_normals.clear();
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 932, as _ZN13SurfaceObject13createNormalsERiiii
inline void SurfaceObject::createNormals(int &p, int row, int upperRow, int j)
{
    if ((m_dataDimension == BothAscending) || (m_dataDimension == BothDescending)) {
        m_normals[p++] = normal(m_vertices.at(row + j),
                                m_vertices.at(row + j + 1),
                                m_vertices.at(upperRow + j));

        m_normals[p++] = normal(m_vertices.at(row + j + 1),
                                m_vertices.at(upperRow + j + 1),
                                m_vertices.at(upperRow + j));
    } else if (m_dataDimension == XDescending) {
        m_normals[p++] = normal(m_vertices.at(row + j),
                                m_vertices.at(upperRow + j),
                                m_vertices.at(upperRow + j + 1));

        m_normals[p++] = normal(m_vertices.at(row + j + 1),
                                m_vertices.at(row + j),
                                m_vertices.at(upperRow + j + 1));
    } else {
        m_normals[p++] = normal(m_vertices.at(row + j),
                                m_vertices.at(upperRow + j),
                                m_vertices.at(upperRow + j + 1));

        m_normals[p++] = normal(m_vertices.at(row + j + 1),
                                m_vertices.at(row + j),
                                m_vertices.at(upperRow + j + 1));
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 109, as _ZN13SurfaceObject26createSmoothNormalBodyLineERii
inline void SurfaceObject::createSmoothNormalBodyLine(int &totalIndex, int column)
{
    int colLimit = m_columns - 1;

    if (m_dataDimension == BothAscending) {
        int end = colLimit + column;
        for (int j = column; j < end; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j + 1),
                                             m_vertices.at(j + m_columns));
        }
        m_normals[totalIndex++] = normal(m_vertices.at(end),
                                         m_vertices.at(end + m_columns),
                                         m_vertices.at(end - 1));
    } else if (m_dataDimension == XDescending) {
        m_normals[totalIndex++] = normal(m_vertices.at(column),
                                         m_vertices.at(column + m_columns),
                                         m_vertices.at(column + 1));
        int end = column + m_columns;
        for (int j = column + 1; j < end; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j - 1),
                                             m_vertices.at(j + m_columns));
        }
    } else if (m_dataDimension == ZDescending) {
        int end = colLimit + column;
        for (int j = column; j < end; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j + 1),
                                             m_vertices.at(j - m_columns));
        }
        m_normals[totalIndex++] = normal(m_vertices.at(end),
                                         m_vertices.at(end - m_columns),
                                         m_vertices.at(end - 1));
    } else { // BothDescending
        m_normals[totalIndex++] = normal(m_vertices.at(column),
                                         m_vertices.at(column - m_columns),
                                         m_vertices.at(column + 1));
        int end = column + m_columns;
        for (int j = column + 1; j < end; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j - 1),
                                             m_vertices.at(j - m_columns));
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 156, as _ZN13SurfaceObject27createSmoothNormalUpperLineERi
inline void SurfaceObject::createSmoothNormalUpperLine(int &totalIndex)
{
    if (m_dataDimension == BothAscending) {
        int lineEnd = m_rows * m_columns - 1;
        for (int j = (m_rows - 1) * m_columns; j < lineEnd; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j - m_columns),
                                             m_vertices.at(j + 1));
        }
        m_normals[totalIndex++] = normal(m_vertices.at(lineEnd),
                                         m_vertices.at(lineEnd - 1),
                                         m_vertices.at(lineEnd - m_columns));
    } else if (m_dataDimension == XDescending) {
        int lineStart = (m_rows - 1) * m_columns;
        int lineEnd = m_rows * m_columns;
        m_normals[totalIndex++] = normal(m_vertices.at(lineStart),
                                         m_vertices.at(lineStart + 1),
                                         m_vertices.at(lineStart - m_columns));
        for (int j = lineStart + 1; j < lineEnd; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j - m_columns),
                                             m_vertices.at(j - 1));
        }
    } else if (m_dataDimension == ZDescending) {
        int colLimit = m_columns - 1;
        for (int j = 0; j < colLimit; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j + m_columns),
                                             m_vertices.at(j + 1));
        }
        m_normals[totalIndex++] = normal(m_vertices.at(colLimit),
                                         m_vertices.at(colLimit - 1),
                                         m_vertices.at(colLimit + m_columns));
    } else { // BothDescending
        m_normals[totalIndex++] = normal(m_vertices.at(0),
                                         m_vertices.at(1),
                                         m_vertices.at(m_columns));
        for (int j = 1; j < m_columns; j++) {
            m_normals[totalIndex++] = normal(m_vertices.at(j),
                                             m_vertices.at(j + m_columns),
                                             m_vertices.at(j - 1));
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 201, as _ZN13SurfaceObject30createSmoothNormalBodyLineItemEii
inline QVector3D SurfaceObject::createSmoothNormalBodyLineItem(int x, int y)
{
    int p = y * m_columns + x;
    if (m_dataDimension == BothAscending) {
        if (x < m_columns - 1) {
            return normal(m_vertices.at(p), m_vertices.at(p + 1),
                          m_vertices.at(p + m_columns));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p + m_columns),
                          m_vertices.at(p - 1));
        }
    } else if (m_dataDimension == XDescending) {
        if (x == 0) {
            return normal(m_vertices.at(p), m_vertices.at(p + m_columns),
                          m_vertices.at(p + 1));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - 1),
                          m_vertices.at(p + m_columns));
        }
    } else if (m_dataDimension == ZDescending) {
        if (x < m_columns - 1) {
            return normal(m_vertices.at(p), m_vertices.at(p + 1),
                          m_vertices.at(p - m_columns));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - m_columns),
                          m_vertices.at(p - 1));
        }
    } else { // BothDescending
        if (x == 0) {
            return normal(m_vertices.at(p), m_vertices.at(p - m_columns),
                          m_vertices.at(p + 1));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - 1),
                          m_vertices.at(p - m_columns));
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 239, as _ZN13SurfaceObject31createSmoothNormalUpperLineItemEii
inline QVector3D SurfaceObject::createSmoothNormalUpperLineItem(int x, int y)
{
    int p = y * m_columns + x;
    if (m_dataDimension == BothAscending) {
        if (x < m_columns - 1) {
            return normal(m_vertices.at(p), m_vertices.at(p - m_columns),
                          m_vertices.at(p + 1));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - 1),
                          m_vertices.at(p - m_columns));
        }
    } else if (m_dataDimension == XDescending) {
        if (x == 0) {
            return normal(m_vertices.at(p), m_vertices.at(p + 1),
                          m_vertices.at(p - m_columns));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - m_columns),
                          m_vertices.at(p - 1));
        }
    } else if (m_dataDimension == ZDescending) {
        if (x < m_columns - 1) {
            return normal(m_vertices.at(p), m_vertices.at(p + m_columns),
                          m_vertices.at(p + 1));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p - 1),
                          m_vertices.at(p + m_columns));
        }
    } else { // BothDescending
        if (x == 0) {
            return normal(m_vertices.at(0), m_vertices.at(1),
                          m_vertices.at(m_columns));
        } else {
            return normal(m_vertices.at(p), m_vertices.at(p + m_columns),
                          m_vertices.at(p - 1));
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/surfaceobject.cpp, line 961, as _ZN13SurfaceObject6normalERK9QVector3DS2_S2_
inline QVector3D SurfaceObject::normal(const QVector3D &a, const QVector3D &b, const QVector3D &c)
{
    QVector3D v1 = b - a;
    QVector3D v2 = c - a;
    QVector3D normal = QVector3D::crossProduct(v1, v2);

    return normal;
}
//  -----------------------------------------------------------------------

//  SurfaceObject::~SurfaceObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObjectD1Ev(SurfaceObject *self) {
  delete self;
}

//  void SurfaceObject::createSmoothIndices(int x, int y, int endX, int endY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject19createSmoothIndicesEiiii(
    SurfaceObject *self,
    int x,
    int y,
    int endX,
    int endY) {
  self->createSmoothIndices(x, y, endX, endY);
}

//  void SurfaceObject::createCoarseSubSection(int x, int y, int columns, int
//      rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject22createCoarseSubSectionEiiii(
    SurfaceObject *self,
    int x,
    int y,
    int columns,
    int rows) {
  self->createCoarseSubSection(x, y, columns, rows);
}

//  void SurfaceObject::createSmoothGridlineIndices(int x, int y, int endX,
//      int endY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject27createSmoothGridlineIndicesEiiii(
    SurfaceObject *self,
    int x,
    int y,
    int endX,
    int endY) {
  self->createSmoothGridlineIndices(x, y, endX, endY);
}

//  void SurfaceObject::createCoarseGridlineIndices(int x, int y, int endX,
//      int endY)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject27createCoarseGridlineIndicesEiiii(
    SurfaceObject *self,
    int x,
    int y,
    int endX,
    int endY) {
  self->createCoarseGridlineIndices(x, y, endX, endY);
}

//  void SurfaceObject::uploadBuffers()
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject13uploadBuffersEv(SurfaceObject *self) {
  self->uploadBuffers();
}

//  QVector3D SurfaceObject::vertexAt(int column, int row)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN13SurfaceObject8vertexAtEii(
    SurfaceObject *self,
    int column,
    int row) {
  return new QVector3D(self->vertexAt(column, row));
}

//  void SurfaceObject::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject5clearEv(SurfaceObject *self) {
  self->clear();
}

//  float SurfaceObject::minYValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13SurfaceObject9minYValueEv(const SurfaceObject *self) {
  return self->minYValue();
}

//  float SurfaceObject::maxYValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13SurfaceObject9maxYValueEv(const SurfaceObject *self) {
  return self->maxYValue();
}

//  void SurfaceObject::activateSurfaceTexture(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject22activateSurfaceTextureEb(
    SurfaceObject *self,
    bool value) {
  self->activateSurfaceTexture(value);
}

//  void SurfaceObject::setLineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject12setLineColorERK6QColor(
    SurfaceObject *self,
    const QColor *color) {
  self->setLineColor(*color);
}

//  const QColor &SurfaceObject::wireframeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13SurfaceObject14wireframeColorEv(
    const SurfaceObject *self) {
  return new QColor(self->wireframeColor());
}

//  void SurfaceObject::createNormals(int &p, int row, int upperRow, int j)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject13createNormalsERiiii(
    SurfaceObject *self,
    int *p,
    int row,
    int upperRow,
    int j) {
  self->createNormals(*p, row, upperRow, j);
}

//  void SurfaceObject::createSmoothNormalBodyLine(int &totalIndex, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject26createSmoothNormalBodyLineERii(
    SurfaceObject *self,
    int *totalIndex,
    int column) {
  self->createSmoothNormalBodyLine(*totalIndex, column);
}

//  void SurfaceObject::createSmoothNormalUpperLine(int &totalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SurfaceObject27createSmoothNormalUpperLineERi(
    SurfaceObject *self,
    int *totalIndex) {
  self->createSmoothNormalUpperLine(*totalIndex);
}

//  QVector3D SurfaceObject::createSmoothNormalBodyLineItem(int x, int y)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN13SurfaceObject30createSmoothNormalBodyLineItemEii(
    SurfaceObject *self,
    int x,
    int y) {
  return new QVector3D(self->createSmoothNormalBodyLineItem(x, y));
}

//  QVector3D SurfaceObject::createSmoothNormalUpperLineItem(int x, int y)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN13SurfaceObject31createSmoothNormalUpperLineItemEii(
    SurfaceObject *self,
    int x,
    int y) {
  return new QVector3D(self->createSmoothNormalUpperLineItem(x, y));
}

//  QVector3D SurfaceObject::normal(const QVector3D &a, const QVector3D &b,
//      const QVector3D &c)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN13SurfaceObject6normalERK9QVector3DS2_S2_(
    SurfaceObject *self,
    const QVector3D *a,
    const QVector3D *b,
    const QVector3D *c) {
  return new QVector3D(self->normal(*a, *b, *c));
}
