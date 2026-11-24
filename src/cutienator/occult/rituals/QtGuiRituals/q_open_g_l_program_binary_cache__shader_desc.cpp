//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglprogrambinarycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc()
extern "C" Q_DECL_EXPORT
QOpenGLProgramBinaryCache::ShaderDesc *ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescC1Ev() {
  return new QOpenGLProgramBinaryCache::ShaderDesc();
}

//  QOpenGLProgramBinaryCache::ShaderDesc::ShaderDesc(QShader::Stage stage,
//      const QByteArray &source)
extern "C" Q_DECL_EXPORT
QOpenGLProgramBinaryCache::ShaderDesc *ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescC1EN7QShader5StageERK10QByteArray(
    QShader::Stage stage,
    const QByteArray *source) {
  return new QOpenGLProgramBinaryCache::ShaderDesc(stage, *source);
}

//  QOpenGLProgramBinaryCache::ShaderDesc::~ShaderDesc()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpenGLProgramBinaryCache10ShaderDescD1Ev(
    QOpenGLProgramBinaryCache::ShaderDesc *self) {
  delete self;
}
