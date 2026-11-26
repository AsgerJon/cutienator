//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: took out snippetNameStr, a function of Qt's
//  debug build that its library does not offer, and its row. Kept as it is
//  when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QOpenGLEngineSharedShaders::QOpenGLEngineSharedShaders(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLEngineSharedShaders *ritual_ZN26QOpenGLEngineSharedShadersC1EP14QOpenGLContext(
    QOpenGLContext *context) {
  return new QOpenGLEngineSharedShaders(context);
}

//  QOpenGLEngineSharedShaders::~QOpenGLEngineSharedShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineSharedShadersD1Ev(
    QOpenGLEngineSharedShaders *self) {
  delete self;
}

//  QOpenGLShaderProgram *QOpenGLEngineSharedShaders::simpleProgram()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN26QOpenGLEngineSharedShaders13simpleProgramEv(
    QOpenGLEngineSharedShaders *self) {
  return self->simpleProgram();
}

//  QOpenGLShaderProgram *QOpenGLEngineSharedShaders::blitProgram()
extern "C" Q_DECL_EXPORT
QOpenGLShaderProgram *ritual_ZN26QOpenGLEngineSharedShaders11blitProgramEv(
    QOpenGLEngineSharedShaders *self) {
  return self->blitProgram();
}

//  QOpenGLEngineShaderProg
//      *QOpenGLEngineSharedShaders::findProgramInCache(const
//      QOpenGLEngineShaderProg &prog)
extern "C" Q_DECL_EXPORT
QOpenGLEngineShaderProg *ritual_ZN26QOpenGLEngineSharedShaders18findProgramInCacheERK23QOpenGLEngineShaderProg(
    QOpenGLEngineSharedShaders *self,
    const QOpenGLEngineShaderProg *prog) {
  return self->findProgramInCache(*prog);
}

//  QOpenGLEngineSharedShaders
//      *QOpenGLEngineSharedShaders::shadersForContext(QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
QOpenGLEngineSharedShaders *ritual_ZN26QOpenGLEngineSharedShaders17shadersForContextEP14QOpenGLContext(
    QOpenGLContext *context) {
  return QOpenGLEngineSharedShaders::shadersForContext(context);
}

//  void
//      QOpenGLEngineSharedShaders::cleanupCustomStage(QOpenGLCustomShaderSta
//      ge *stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLEngineSharedShaders18cleanupCustomStageEP24QOpenGLCustomShaderStage(
    QOpenGLEngineSharedShaders *self,
    QOpenGLCustomShaderStage *stage) {
  self->cleanupCustomStage(stage);
}
