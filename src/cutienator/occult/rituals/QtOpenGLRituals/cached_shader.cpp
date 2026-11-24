//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglshadercache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglshadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  CachedShader::CachedShader(const QByteArray &a0, const QByteArray &a1)
extern "C" Q_DECL_EXPORT
CachedShader *ritual_ZN12CachedShaderC1ERK10QByteArrayS2_(
    const QByteArray *a0,
    const QByteArray *a1) {
  return new CachedShader(*a0, *a1);
}

//  bool CachedShader::isCached()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12CachedShader8isCachedEv(CachedShader *self) {
  return self->isCached();
}

//  bool CachedShader::load(QOpenGLShaderProgram *a0, QOpenGLContext *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12CachedShader4loadEP20QOpenGLShaderProgramP14QOpenGLContext(
    CachedShader *self,
    QOpenGLShaderProgram *a0,
    QOpenGLContext *a1) {
  return self->load(a0, a1);
}

//  bool CachedShader::store(QOpenGLShaderProgram *a0, QOpenGLContext *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12CachedShader5storeEP20QOpenGLShaderProgramP14QOpenGLContext(
    CachedShader *self,
    QOpenGLShaderProgram *a0,
    QOpenGLContext *a1) {
  return self->store(a0, a1);
}

//  CachedShader::~CachedShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12CachedShaderD1Ev(CachedShader *self) {
  delete self;
}
