//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#if !QT_CONFIG(opengles2)
#include <QtOpenGL/qopenglversionfunctions.h>

//  Version QOpenGLFunctions_3_0_DeprecatedBackend::versionStatus()
extern "C" Q_DECL_EXPORT
QOpenGLVersionFunctionsBackend::Version ritual_ZN38QOpenGLFunctions_3_0_DeprecatedBackend13versionStatusEv() {
  return QOpenGLFunctions_3_0_DeprecatedBackend::versionStatus();
}

//  QOpenGLFunctions_3_0_DeprecatedBackend::~QOpenGLFunctions_3_0_DeprecatedB
//      ackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QOpenGLFunctions_3_0_DeprecatedBackendD1Ev(
    QOpenGLFunctions_3_0_DeprecatedBackend *self) {
  delete self;
}

#endif  // !QT_CONFIG(opengles2)
#endif  // !defined(QT_NO_OPENGL)
