//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/private/qopengl2pexvertexarray_p.h>
#include <QtGui/private/qbezier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/opengl/qopengl2pexvertexarray.cpp, line 11, as _ZN22QOpenGL2PEXVertexArray5clearEv
inline void QOpenGL2PEXVertexArray::clear()
{
    vertexArray.reset();
    vertexArrayStops.reset();
    boundingRectDirty = true;
}

//  from src/opengl/qopengl2pexvertexarray.cpp, line 19, as _ZNK22QOpenGL2PEXVertexArray12boundingRectEv
inline QOpenGLRect QOpenGL2PEXVertexArray::boundingRect() const
{
    if (boundingRectDirty)
        return QOpenGLRect(0.0, 0.0, 0.0, 0.0);
    else
        return QOpenGLRect(minX, minY, maxX, maxY);
}

//  from src/opengl/qopengl2pexvertexarray.cpp, line 124, as _ZN22QOpenGL2PEXVertexArray11lineToArrayEff
inline void QOpenGL2PEXVertexArray::lineToArray(const GLfloat x, const GLfloat y)
{
    vertexArray.add(QOpenGLPoint(x, y));

    if (x > maxX)
        maxX = x;
    else if (x < minX)
        minX = x;
    if (y > maxY)
        maxY = y;
    else if (y < minY)
        minY = y;
}

//  from src/opengl/qopengl2pexvertexarray.cpp, line 27, as _ZN22QOpenGL2PEXVertexArray14addClosingLineEi
inline void QOpenGL2PEXVertexArray::addClosingLine(int index)
{
    QPointF point(vertexArray.at(index));
    if (point != QPointF(vertexArray.last()))
        vertexArray.add(point);
}
//  -----------------------------------------------------------------------

//  QOpenGL2PEXVertexArray::QOpenGL2PEXVertexArray()
extern "C" Q_DECL_EXPORT
QOpenGL2PEXVertexArray *ritual_ZN22QOpenGL2PEXVertexArrayC1Ev() {
  return new QOpenGL2PEXVertexArray();
}

//  void QOpenGL2PEXVertexArray::addRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray7addRectERK6QRectF(
    QOpenGL2PEXVertexArray *self,
    const QRectF *rect) {
  self->addRect(*rect);
}

//  void QOpenGL2PEXVertexArray::addQuad(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray7addQuadERK6QRectF(
    QOpenGL2PEXVertexArray *self,
    const QRectF *rect) {
  self->addQuad(*rect);
}

//  void QOpenGL2PEXVertexArray::addVertex(const GLfloat x, const GLfloat y)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray9addVertexEff(
    QOpenGL2PEXVertexArray *self,
    GLfloat x,
    GLfloat y) {
  self->addVertex(x, y);
}

//  void QOpenGL2PEXVertexArray::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray5clearEv(
    QOpenGL2PEXVertexArray *self) {
  self->clear();
}

//  QOpenGLPoint *QOpenGL2PEXVertexArray::data()
extern "C" Q_DECL_EXPORT
QOpenGLPoint *ritual_ZN22QOpenGL2PEXVertexArray4dataEv(
    QOpenGL2PEXVertexArray *self) {
  return self->data();
}

//  int QOpenGL2PEXVertexArray::stopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QOpenGL2PEXVertexArray9stopCountEv(
    const QOpenGL2PEXVertexArray *self) {
  return self->stopCount();
}

//  QOpenGLRect QOpenGL2PEXVertexArray::boundingRect() const
extern "C" Q_DECL_EXPORT
QOpenGLRect *ritual_ZNK22QOpenGL2PEXVertexArray12boundingRectEv(
    const QOpenGL2PEXVertexArray *self) {
  return new QOpenGLRect(self->boundingRect());
}

//  int QOpenGL2PEXVertexArray::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QOpenGL2PEXVertexArray11vertexCountEv(
    const QOpenGL2PEXVertexArray *self) {
  return self->vertexCount();
}

//  void QOpenGL2PEXVertexArray::lineToArray(const GLfloat x, const GLfloat
//      y)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray11lineToArrayEff(
    QOpenGL2PEXVertexArray *self,
    GLfloat x,
    GLfloat y) {
  self->lineToArray(x, y);
}

//  void QOpenGL2PEXVertexArray::addClosingLine(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpenGL2PEXVertexArray14addClosingLineEi(
    QOpenGL2PEXVertexArray *self,
    int index) {
  self->addClosingLine(index);
}
