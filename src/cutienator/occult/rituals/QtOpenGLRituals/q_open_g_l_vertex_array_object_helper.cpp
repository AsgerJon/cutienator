//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglvertexarrayobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglvertexarrayobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLVertexArrayObjectHelper::QOpenGLVertexArrayObjectHelper(QOpenGLCon
//      text *context)
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObjectHelper *ritual_ZN30QOpenGLVertexArrayObjectHelperC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLVertexArrayObjectHelper(context);
}

//  void QOpenGLVertexArrayObjectHelper::initializeFromContext(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLVertexArrayObjectHelper21initializeFromContextEP14QOpenGLContext(
    QOpenGLVertexArrayObjectHelper *self,
    QOpenGLContext *context) {
  self->initializeFromContext(context);
}

//  QOpenGLVertexArrayObjectHelper *QOpenGLVertexArrayObjectHelper::vertexArr
//      ayObjectHelperForContext(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObjectHelper *ritual_ZN30QOpenGLVertexArrayObjectHelper33vertexArrayObjectHelperForContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVertexArrayObjectHelper::vertexArrayObjectHelperForContext(
      context);
}

//  bool QOpenGLVertexArrayObjectHelper::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QOpenGLVertexArrayObjectHelper7isValidEv(
    const QOpenGLVertexArrayObjectHelper *self) {
  return self->isValid();
}

//  void QOpenGLVertexArrayObjectHelper::glGenVertexArrays(GLsizei n, GLuint
//      *arrays) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QOpenGLVertexArrayObjectHelper17glGenVertexArraysEiPj(
    const QOpenGLVertexArrayObjectHelper *self,
    GLsizei n,
    GLuint *arrays) {
  self->glGenVertexArrays(n, arrays);
}

//  void QOpenGLVertexArrayObjectHelper::glDeleteVertexArrays(GLsizei n,
//      const GLuint *arrays) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QOpenGLVertexArrayObjectHelper20glDeleteVertexArraysEiPKj(
    const QOpenGLVertexArrayObjectHelper *self,
    GLsizei n,
    const GLuint *arrays) {
  self->glDeleteVertexArrays(n, arrays);
}

//  void QOpenGLVertexArrayObjectHelper::glBindVertexArray(GLuint array)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QOpenGLVertexArrayObjectHelper17glBindVertexArrayEj(
    const QOpenGLVertexArrayObjectHelper *self,
    GLuint array) {
  self->glBindVertexArray(array);
}

//  GLboolean QOpenGLVertexArrayObjectHelper::glIsVertexArray(GLuint array)
//      const
extern "C" Q_DECL_EXPORT
GLboolean ritual_ZNK30QOpenGLVertexArrayObjectHelper15glIsVertexArrayEj(
    const QOpenGLVertexArrayObjectHelper *self,
    GLuint array) {
  return self->glIsVertexArray(array);
}
