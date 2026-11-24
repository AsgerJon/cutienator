//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglqueryhelper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !QT_CONFIG(opengles2)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglqueryhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLQueryHelper::QOpenGLQueryHelper(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLQueryHelper *ritual_ZN18QOpenGLQueryHelperC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLQueryHelper(context);
}

//  void QOpenGLQueryHelper::glEndQuery(GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper10glEndQueryEj(
    QOpenGLQueryHelper *self,
    GLenum target) {
  self->glEndQuery(target);
}

//  void QOpenGLQueryHelper::glBeginQuery(GLenum target, GLuint id)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper12glBeginQueryEjj(
    QOpenGLQueryHelper *self,
    GLenum target,
    GLuint id) {
  self->glBeginQuery(target, id);
}

//  void QOpenGLQueryHelper::glQueryCounter(GLuint id, GLenum target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper14glQueryCounterEjj(
    QOpenGLQueryHelper *self,
    GLuint id,
    GLenum target) {
  self->glQueryCounter(id, target);
}

//  QOpenGLQueryHelper::~QOpenGLQueryHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelperD1Ev(QOpenGLQueryHelper *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
