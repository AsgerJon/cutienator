//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QOpenGLRect::QOpenGLRect(const QRectF &r)
extern "C" Q_DECL_EXPORT
QOpenGLRect *ritual_ZN11QOpenGLRectC1ERK6QRectF(const QRectF *r) {
  return new QOpenGLRect(*r);
}

//  QOpenGLRect::QOpenGLRect(GLfloat l, GLfloat t, GLfloat r, GLfloat b)
extern "C" Q_DECL_EXPORT
QOpenGLRect *ritual_ZN11QOpenGLRectC1Effff(
    GLfloat l,
    GLfloat t,
    GLfloat r,
    GLfloat b) {
  return new QOpenGLRect(l, t, r, b);
}

//  QRectF QOpenGLRect::operator QRectF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QOpenGLRectcv6QRectFEv(const QOpenGLRect *self) {
  return new QRectF(self->operator QRectF());
}

//  QOpenGLRect::~QOpenGLRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QOpenGLRectD1Ev(QOpenGLRect *self) {
  delete self;
}
