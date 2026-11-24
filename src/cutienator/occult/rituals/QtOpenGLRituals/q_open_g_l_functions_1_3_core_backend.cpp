//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_1_3_CoreBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN32QOpenGLFunctions_1_3_CoreBackend13versionStatusEv() {
  return QOpenGLFunctions_1_3_CoreBackend::versionStatus();
}

//  QOpenGLFunctions_1_3_CoreBackend::~QOpenGLFunctions_1_3_CoreBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLFunctions_1_3_CoreBackendD1Ev(
    QOpenGLFunctions_1_3_CoreBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
