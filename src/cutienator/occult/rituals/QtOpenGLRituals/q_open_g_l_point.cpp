//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QOpenGLPoint::QOpenGLPoint(GLfloat new_x, GLfloat new_y)
extern "C" Q_DECL_EXPORT
QOpenGLPoint *ritual_ZN12QOpenGLPointC1Eff(GLfloat new_x, GLfloat new_y) {
  return new QOpenGLPoint(new_x, new_y);
}

//  QOpenGLPoint::QOpenGLPoint(const QPointF &p)
extern "C" Q_DECL_EXPORT
QOpenGLPoint *ritual_ZN12QOpenGLPointC1ERK7QPointF(const QPointF *p) {
  return new QOpenGLPoint(*p);
}

//  QOpenGLPoint::QOpenGLPoint(const QPointF *p)
extern "C" Q_DECL_EXPORT
QOpenGLPoint *ritual_ZN12QOpenGLPointC1EPK7QPointF(const QPointF *p) {
  return new QOpenGLPoint(p);
}

//  QPointF QOpenGLPoint::operator QPointF()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12QOpenGLPointcv7QPointFEv(QOpenGLPoint *self) {
  return new QPointF(self->operator QPointF());
}

//  QPointF QOpenGLPoint::operator QPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QOpenGLPointcv7QPointFEv(const QOpenGLPoint *self) {
  return new QPointF(self->operator QPointF());
}

//  QOpenGLPoint::~QOpenGLPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QOpenGLPointD1Ev(QOpenGLPoint *self) {
  delete self;
}
