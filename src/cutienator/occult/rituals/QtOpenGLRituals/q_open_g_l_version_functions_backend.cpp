//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglversionfunctions.h>

//  QOpenGLVersionFunctionsBackend::QOpenGLVersionFunctionsBackend(QOpenGLCon
//      text *ctx)
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend *ritual_ZN30QOpenGLVersionFunctionsBackendC1EP14QOpenGLContext(
    QOpenGLContext *ctx) {
  return new QOpenGLVersionFunctionsBackend(ctx);
}

//  QOpenGLVersionFunctionsBackend::~QOpenGLVersionFunctionsBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLVersionFunctionsBackendD1Ev(
    QOpenGLVersionFunctionsBackend *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
