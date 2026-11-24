//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_4_2_CoreBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN32QOpenGLFunctions_4_2_CoreBackend13versionStatusEv() {
  return QOpenGLFunctions_4_2_CoreBackend::versionStatus();
}

//  QOpenGLFunctions_4_2_CoreBackend::~QOpenGLFunctions_4_2_CoreBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpenGLFunctions_4_2_CoreBackendD1Ev(
    QOpenGLFunctions_4_2_CoreBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
