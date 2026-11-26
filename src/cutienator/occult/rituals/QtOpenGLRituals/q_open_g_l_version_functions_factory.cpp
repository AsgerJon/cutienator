//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctionsfactory.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 5. Kept
//  as it is when the generator runs again.
#include <QtOpenGL/qopenglversionfunctionsfactory.h>
#include <QtOpenGL/qopenglversionprofile.h>
#include <QtOpenGL/qtopenglglobal.h>
#include <QtOpenGL/qopenglfunctions_2_0.h>
#include <QtOpenGL/qopenglfunctions_3_3_core.h>
#include <QtOpenGL/qopenglfunctions_4_1_core.h>
#include <QtOpenGL/qopenglfunctions_4_5_core.h>
#include <QtOpenGL/qopenglfunctions_4_5_compatibility.h>

//  QAbstractOpenGLFunctions *QOpenGLVersionFunctionsFactory::get(const
//      QOpenGLVersionProfile &versionProfile, QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QAbstractOpenGLFunctions *ritual_ZN30QOpenGLVersionFunctionsFactory3getERK21QOpenGLVersionProfileP14QOpenGLContext(
    const QOpenGLVersionProfile *versionProfile,
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get(*versionProfile, context);
}

//  QOpenGLVersionFunctionsFactory::~QOpenGLVersionFunctionsFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOpenGLVersionFunctionsFactoryD1Ev(
    QOpenGLVersionFunctionsFactory *self) {
  delete self;
}

#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
//  QOpenGLFunctions_2_0 *
//      QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_2_0>(
//      QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_2_0 *ritual_ZN30QOpenGLVersionFunctionsFactory3getI20QOpenGLFunctions_2_0EEPT_P14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_2_0>(
      context);
}

//  QOpenGLFunctions_3_3_Core *
//      QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_3_3_Core>(
//      QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_3_3_Core *ritual_ZN30QOpenGLVersionFunctionsFactory3getI25QOpenGLFunctions_3_3_CoreEEPT_P14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_3_3_Core>(
      context);
}

//  QOpenGLFunctions_4_1_Core *
//      QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_1_Core>(
//      QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_1_Core *ritual_ZN30QOpenGLVersionFunctionsFactory3getI25QOpenGLFunctions_4_1_CoreEEPT_P14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_1_Core>(
      context);
}

//  QOpenGLFunctions_4_5_Core *
//      QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_5_Core>(
//      QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_5_Core *ritual_ZN30QOpenGLVersionFunctionsFactory3getI25QOpenGLFunctions_4_5_CoreEEPT_P14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_5_Core>(
      context);
}

//  QOpenGLFunctions_4_5_Compatibility *
//      QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_5_Compatibility>(
//      QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
QOpenGLFunctions_4_5_Compatibility *ritual_ZN30QOpenGLVersionFunctionsFactory3getI34QOpenGLFunctions_4_5_CompatibilityEEPT_P14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLVersionFunctionsFactory::get<QOpenGLFunctions_4_5_Compatibility>(
      context);
}
#endif
