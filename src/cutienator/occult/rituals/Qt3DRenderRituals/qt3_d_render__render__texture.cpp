//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qtexturedataupdate.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>

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

//  Qt3DRender::Render::Texture::Texture()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Texture *ritual_ZN10Qt3DRender6Render7TextureC1Ev() {
  return new CuteQt3DRender_Render_Texture();
}

//  Qt3DRender::Render::Texture::~Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7TextureD1Ev(
    Qt3DRender::Render::Texture *self) {
  delete self;
}

//  void Qt3DRender::Render::Texture::addDirtyFlag(DirtyFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture12addDirtyFlagE6QFlagsINS1_9DirtyFlagEE(
    Qt3DRender::Render::Texture *self,
    int flags) {
  self->addDirtyFlag(
      QFlags<Qt3DRender::Render::Texture::DirtyFlag>::fromInt(flags));
}

//  DirtyFlags Qt3DRender::Render::Texture::dirtyFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render7Texture10dirtyFlagsEv(
    Qt3DRender::Render::Texture *self) {
  return static_cast<int>(self->dirtyFlags().toInt());
}

//  void Qt3DRender::Render::Texture::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture10unsetDirtyEv(
    Qt3DRender::Render::Texture *self) {
  self->unsetDirty();
}

//  void Qt3DRender::Render::Texture::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture7cleanupEv(
    Qt3DRender::Render::Texture *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Texture::addTextureDataUpdate(const
//      QTextureDataUpdate &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture20addTextureDataUpdateERKNS_18QTextureDataUpdateE(
    Qt3DRender::Render::Texture *self,
    const Qt3DRender::QTextureDataUpdate *update) {
  self->addTextureDataUpdate(*update);
}

//  std::vector<QTextureDataUpdate>
//      Qt3DRender::Render::Texture::takePendingTextureDataUpdates()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::QTextureDataUpdate> *ritual_ZN10Qt3DRender6Render7Texture29takePendingTextureDataUpdatesEv(
    Qt3DRender::Render::Texture *self) {
  return new std::vector<Qt3DRender::QTextureDataUpdate>(
      self->takePendingTextureDataUpdates());
}

//  void Qt3DRender::Render::Texture::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Texture *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

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

//  const Qt3DCore::QNodeIdVector
//      Qt3DRender::Render::Texture::textureImageIds() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK10Qt3DRender6Render7Texture15textureImageIdsEv(
    const Qt3DRender::Render::Texture *self) {
  return new Qt3DCore::QNodeIdVector(self->textureImageIds());
}

//  const QTextureGeneratorPtr &Qt3DRender::Render::Texture::dataGenerator()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureGeneratorPtr *ritual_ZNK10Qt3DRender6Render7Texture13dataGeneratorEv(
    const Qt3DRender::Render::Texture *self) {
  return &(self->dataGenerator());
}

//  int Qt3DRender::Render::Texture::sharedTextureId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render7Texture15sharedTextureIdEv(
    const Qt3DRender::Render::Texture *self) {
  return self->sharedTextureId();
}

//  void Qt3DRender::Render::Texture::setDataGenerator(const
//      QTextureGeneratorPtr &generator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render7Texture16setDataGeneratorERK14QSharedPointerINS_17QTextureGeneratorEE(
    Qt3DRender::Render::Texture *self,
    const Qt3DRender::QTextureGeneratorPtr *generator) {
  self->setDataGenerator(*generator);
}

//  bool Qt3DRender::Render::Texture::isValid(TextureImageManager *manager)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render7Texture7isValidEPNS0_19TextureImageManagerE(
    const Qt3DRender::Render::Texture *self,
    Qt3DRender::Render::TextureImageManager *manager) {
  return self->isValid(manager);
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

//  a std::vector<Qt3DRender::QTextureDataUpdate> a ritual of
//      Qt3DRender::Render::Texture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Texture__std_vector_Qt3DRender_QTextureDataUpdate(
    std::vector<Qt3DRender::QTextureDataUpdate> *self) {
  delete self;
}

//  a Qt3DCore::QNodeIdVector a ritual of Qt3DRender::Render::Texture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Texture__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}
