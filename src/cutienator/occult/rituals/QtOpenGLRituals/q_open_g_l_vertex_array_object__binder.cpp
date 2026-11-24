//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglvertexarrayobject.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglvertexarrayobject.h>

//  QOpenGLVertexArrayObject::Binder::Binder(QOpenGLVertexArrayObject *v)
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObject::Binder *ritual_ZN24QOpenGLVertexArrayObject6BinderC1EPS_(
    QOpenGLVertexArrayObject *v) {
  return new QOpenGLVertexArrayObject::Binder(v);
}

//  QOpenGLVertexArrayObject::Binder::~Binder()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject6BinderD1Ev(
    QOpenGLVertexArrayObject::Binder *self) {
  delete self;
}

//  void QOpenGLVertexArrayObject::Binder::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject6Binder7releaseEv(
    QOpenGLVertexArrayObject::Binder *self) {
  self->release();
}

//  void QOpenGLVertexArrayObject::Binder::rebind()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject6Binder6rebindEv(
    QOpenGLVertexArrayObject::Binder *self) {
  self->rebind();
}

#endif  // !defined(QT_NO_OPENGL)
