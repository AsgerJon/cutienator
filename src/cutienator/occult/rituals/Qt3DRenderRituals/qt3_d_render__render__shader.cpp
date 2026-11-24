//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A Qt3DRender::Render::Shader that Python can take functions over in. Every Qt3DRender::Render::Shader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_ShaderCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Shader : public Qt3DRender::Render::Shader {
public:
  using Qt3DRender::Render::Shader::Shader;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Shader::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ShaderCall0 call = reinterpret_cast<CuteQt3DRender_Render_ShaderCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Shader::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  QString Qt3DRender::Render::Shader::log() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render6Shader3logEv(
    const Qt3DRender::Render::Shader *self) {
  return new QString(self->log());
}

//  QShaderProgram::Status Qt3DRender::Render::Shader::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram::Status ritual_ZNK10Qt3DRender6Render6Shader6statusEv(
    const Qt3DRender::Render::Shader *self) {
  return self->status();
}

//  QShaderProgram::Format Qt3DRender::Render::Shader::format() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram::Format ritual_ZNK10Qt3DRender6Render6Shader6formatEv(
    const Qt3DRender::Render::Shader *self) {
  return self->format();
}

//  bool Qt3DRender::Render::Shader::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Shader7isDirtyEv(
    const Qt3DRender::Render::Shader *self) {
  return self->isDirty();
}

//  void Qt3DRender::Render::Shader::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Shader10unsetDirtyEv(
    Qt3DRender::Render::Shader *self) {
  self->unsetDirty();
}

//  bool Qt3DRender::Render::Shader::requiresFrontendSync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Shader20requiresFrontendSyncEv(
    const Qt3DRender::Render::Shader *self) {
  return self->requiresFrontendSync();
}

//  void Qt3DRender::Render::Shader::unsetRequiresFrontendSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Shader25unsetRequiresFrontendSyncEv(
    Qt3DRender::Render::Shader *self) {
  self->unsetRequiresFrontendSync();
}

//  a Python function taken by a CuteQt3DRender_Render_Shader, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Shader(
    Qt3DRender::Render::Shader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Shader *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Shader::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render6Shader16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Shader *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Shader::syncFromFrontEnd(frontEnd, firstTime);
}
