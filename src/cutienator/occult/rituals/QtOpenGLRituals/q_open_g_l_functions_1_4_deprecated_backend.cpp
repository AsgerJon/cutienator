//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_1_4_DeprecatedBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN38QOpenGLFunctions_1_4_DeprecatedBackend13versionStatusEv() {
  return QOpenGLFunctions_1_4_DeprecatedBackend::versionStatus();
}

//  QOpenGLFunctions_1_4_DeprecatedBackend::~QOpenGLFunctions_1_4_DeprecatedB
//      ackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QOpenGLFunctions_1_4_DeprecatedBackendD1Ev(
    QOpenGLFunctions_1_4_DeprecatedBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
