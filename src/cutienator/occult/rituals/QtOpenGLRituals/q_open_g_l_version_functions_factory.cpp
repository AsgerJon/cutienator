//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctionsfactory.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtOpenGL/qopenglversionfunctionsfactory.h>
#include <QtOpenGL/qopenglversionprofile.h>

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
