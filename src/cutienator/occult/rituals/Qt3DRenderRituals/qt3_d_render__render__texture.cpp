//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::Texture that Python can take functions over in. Every Qt3DRender::Render::Texture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_TextureCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Texture : public Qt3DRender::Render::Texture {
public:
  using Qt3DRender::Render::Texture::Texture;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Texture::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_TextureCall0 call = reinterpret_cast<CuteQt3DRender_Render_TextureCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Texture::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  const TextureProperties &Qt3DRender::Render::Texture::properties() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureProperties *ritual_ZNK10Qt3DRender6Render7Texture10propertiesEv(
    const Qt3DRender::Render::Texture *self) {
  return new Qt3DRender::Render::TextureProperties(self->properties());
}

//  const TextureParameters &Qt3DRender::Render::Texture::parameters() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureParameters *ritual_ZNK10Qt3DRender6Render7Texture10parametersEv(
    const Qt3DRender::Render::Texture *self) {
  return new Qt3DRender::Render::TextureParameters(self->parameters());
}

//  int Qt3DRender::Render::Texture::sharedTextureId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render7Texture15sharedTextureIdEv(
    const Qt3DRender::Render::Texture *self) {
  return self->sharedTextureId();
}

//  a Python function taken by a CuteQt3DRender_Render_Texture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Texture(
    Qt3DRender::Render::Texture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Texture *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Texture::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render7Texture16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Texture *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Texture::syncFromFrontEnd(frontEnd, firstTime);
}
