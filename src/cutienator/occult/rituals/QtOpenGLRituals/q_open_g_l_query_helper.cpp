//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglqueryhelper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !QT_CONFIG(opengles2)
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

//  void QOpenGLQueryHelper::glGetQueryObjectuiv(GLuint id, GLenum pname,
//      GLuint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper19glGetQueryObjectuivEjjPj(
    QOpenGLQueryHelper *self,
    GLuint id,
    GLenum pname,
    GLuint *params) {
  self->glGetQueryObjectuiv(id, pname, params);
}

//  void QOpenGLQueryHelper::glGetQueryObjectiv(GLuint id, GLenum pname,
//      GLint *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper18glGetQueryObjectivEjjPi(
    QOpenGLQueryHelper *self,
    GLuint id,
    GLenum pname,
    GLint *params) {
  self->glGetQueryObjectiv(id, pname, params);
}

//  void QOpenGLQueryHelper::glGetQueryiv(GLenum target, GLenum pname, GLint
//      *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper12glGetQueryivEjjPi(
    QOpenGLQueryHelper *self,
    GLenum target,
    GLenum pname,
    GLint *params) {
  self->glGetQueryiv(target, pname, params);
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

//  GLboolean QOpenGLQueryHelper::glIsQuery(GLuint id)
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZN18QOpenGLQueryHelper9glIsQueryEj(
    QOpenGLQueryHelper *self,
    GLuint id) {
  return self->glIsQuery(id);
}

//  void QOpenGLQueryHelper::glDeleteQueries(GLsizei n, const GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper15glDeleteQueriesEiPKj(
    QOpenGLQueryHelper *self,
    GLsizei n,
    const GLuint *ids) {
  self->glDeleteQueries(n, ids);
}

//  void QOpenGLQueryHelper::glGenQueries(GLsizei n, GLuint *ids)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper12glGenQueriesEiPj(
    QOpenGLQueryHelper *self,
    GLsizei n,
    GLuint *ids) {
  self->glGenQueries(n, ids);
}

//  void QOpenGLQueryHelper::glGetInteger64v(GLenum pname, GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper15glGetInteger64vEjPl(
    QOpenGLQueryHelper *self,
    GLenum pname,
    GLint64 *params) {
  self->glGetInteger64v(pname, params);
}

//  void QOpenGLQueryHelper::glGetQueryObjectui64v(GLuint id, GLenum pname,
//      GLuint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper21glGetQueryObjectui64vEjjPm(
    QOpenGLQueryHelper *self,
    GLuint id,
    GLenum pname,
    GLuint64 *params) {
  self->glGetQueryObjectui64v(id, pname, params);
}

//  void QOpenGLQueryHelper::glGetQueryObjecti64v(GLuint id, GLenum pname,
//      GLint64 *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLQueryHelper20glGetQueryObjecti64vEjjPl(
    QOpenGLQueryHelper *self,
    GLuint id,
    GLenum pname,
    GLint64 *params) {
  self->glGetQueryObjecti64v(id, pname, params);
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
#endif  // !QT_CONFIG(opengles2)
