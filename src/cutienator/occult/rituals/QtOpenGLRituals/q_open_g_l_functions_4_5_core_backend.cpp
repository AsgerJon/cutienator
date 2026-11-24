//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_4_5_CoreBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN32QOpenGLFunctions_4_5_CoreBackend13versionStatusEv() {
  return QOpenGLFunctions_4_5_CoreBackend::versionStatus();
}

//  QOpenGLFunctions_4_5_CoreBackend::~QOpenGLFunctions_4_5_CoreBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLFunctions_4_5_CoreBackendD1Ev(
    QOpenGLFunctions_4_5_CoreBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
