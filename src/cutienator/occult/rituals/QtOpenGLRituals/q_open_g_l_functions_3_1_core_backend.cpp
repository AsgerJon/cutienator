//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_3_1_CoreBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN32QOpenGLFunctions_3_1_CoreBackend13versionStatusEv() {
  return QOpenGLFunctions_3_1_CoreBackend::versionStatus();
}

//  QOpenGLFunctions_3_1_CoreBackend::~QOpenGLFunctions_3_1_CoreBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLFunctions_3_1_CoreBackendD1Ev(
    QOpenGLFunctions_3_1_CoreBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
