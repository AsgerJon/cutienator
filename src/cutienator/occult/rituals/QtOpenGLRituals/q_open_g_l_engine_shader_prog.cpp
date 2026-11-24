//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpenGLEngineShaderProg::QOpenGLEngineShaderProg()
extern "C" Q_DECL_EXPORT
QOpenGLEngineShaderProg *ritual_ZN23QOpenGLEngineShaderProgC1Ev() {
  return new QOpenGLEngineShaderProg();
}

//  QOpenGLEngineShaderProg::~QOpenGLEngineShaderProg()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLEngineShaderProgD1Ev(QOpenGLEngineShaderProg *self) {
  delete self;
}

//  bool QOpenGLEngineShaderProg::operator==(const QOpenGLEngineShaderProg
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QOpenGLEngineShaderProgeqERKS_(
    const QOpenGLEngineShaderProg *self,
    const QOpenGLEngineShaderProg *other) {
  return self->operator==(*other);
}
