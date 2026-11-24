//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexturematerial.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexturematerial.h>
#include <cstring>

//  A QSGOpaqueTextureMaterial that Python can take functions over in. Every QSGOpaqueTextureMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGOpaqueTextureMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGOpaqueTextureMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGOpaqueTextureMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGOpaqueTextureMaterial : public QSGOpaqueTextureMaterial {
public:
  using QSGOpaqueTextureMaterial::QSGOpaqueTextureMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QSGOpaqueTextureMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGOpaqueTextureMaterialCall0 call = reinterpret_cast<CuteQSGOpaqueTextureMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGOpaqueTextureMaterial::type();
  }

  //  QSGMaterialShader *QSGOpaqueTextureMaterial::createShader(QSGRenderer
  //      Interface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGOpaqueTextureMaterialCall1 call = reinterpret_cast<CuteQSGOpaqueTextureMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGOpaqueTextureMaterial::createShader(renderMode);
  }

  //  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGOpaqueTextureMaterialCall2 call = reinterpret_cast<CuteQSGOpaqueTextureMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGOpaqueTextureMaterial::compare(other);
  }
};

//  QSGOpaqueTextureMaterial::QSGOpaqueTextureMaterial()
extern "C" Q_DECL_EXPORT
QSGOpaqueTextureMaterial *ritual_ZN24QSGOpaqueTextureMaterialC1Ev() {
  return new CuteQSGOpaqueTextureMaterial();
}

//  QSGMaterialType *QSGOpaqueTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK24QSGOpaqueTextureMaterial4typeEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGOpaqueTextureMaterial::createShader(QSGRendererInterface::RenderM
//      ode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK24QSGOpaqueTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGOpaqueTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QSGOpaqueTextureMaterial7compareEPK11QSGMaterial(
    const QSGOpaqueTextureMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  void QSGOpaqueTextureMaterial::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial10setTextureEP10QSGTexture(
    QSGOpaqueTextureMaterial *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *QSGOpaqueTextureMaterial::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK24QSGOpaqueTextureMaterial7textureEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->texture();
}

//  void QSGOpaqueTextureMaterial::setMipmapFiltering(QSGTexture::Filtering
//      filteringType)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGOpaqueTextureMaterial *self,
    QSGTexture::Filtering filteringType) {
  self->setMipmapFiltering(filteringType);
}

//  QSGTexture::Filtering QSGOpaqueTextureMaterial::mipmapFiltering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK24QSGOpaqueTextureMaterial15mipmapFilteringEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->mipmapFiltering();
}

//  void QSGOpaqueTextureMaterial::setFiltering(QSGTexture::Filtering
//      filteringType)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial12setFilteringEN10QSGTexture9FilteringE(
    QSGOpaqueTextureMaterial *self,
    QSGTexture::Filtering filteringType) {
  self->setFiltering(filteringType);
}

//  QSGTexture::Filtering QSGOpaqueTextureMaterial::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK24QSGOpaqueTextureMaterial9filteringEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->filtering();
}

//  void QSGOpaqueTextureMaterial::setHorizontalWrapMode(QSGTexture::WrapMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGOpaqueTextureMaterial *self,
    QSGTexture::WrapMode mode) {
  self->setHorizontalWrapMode(mode);
}

//  QSGTexture::WrapMode QSGOpaqueTextureMaterial::horizontalWrapMode() const
extern "C" Q_DECL_EXPORT
QSGTexture::WrapMode ritual_ZNK24QSGOpaqueTextureMaterial18horizontalWrapModeEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->horizontalWrapMode();
}

//  void QSGOpaqueTextureMaterial::setVerticalWrapMode(QSGTexture::WrapMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGOpaqueTextureMaterial *self,
    QSGTexture::WrapMode mode) {
  self->setVerticalWrapMode(mode);
}

//  QSGTexture::WrapMode QSGOpaqueTextureMaterial::verticalWrapMode() const
extern "C" Q_DECL_EXPORT
QSGTexture::WrapMode ritual_ZNK24QSGOpaqueTextureMaterial16verticalWrapModeEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->verticalWrapMode();
}

//  void
//      QSGOpaqueTextureMaterial::setAnisotropyLevel(QSGTexture::AnisotropyLe
//      vel level)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGOpaqueTextureMaterial18setAnisotropyLevelEN10QSGTexture15AnisotropyLevelE(
    QSGOpaqueTextureMaterial *self,
    QSGTexture::AnisotropyLevel level) {
  self->setAnisotropyLevel(level);
}

//  QSGTexture::AnisotropyLevel QSGOpaqueTextureMaterial::anisotropyLevel()
//      const
extern "C" Q_DECL_EXPORT
QSGTexture::AnisotropyLevel ritual_ZNK24QSGOpaqueTextureMaterial15anisotropyLevelEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->anisotropyLevel();
}

//  a Python function taken by a CuteQSGOpaqueTextureMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGOpaqueTextureMaterial(
    QSGOpaqueTextureMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGOpaqueTextureMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGOpaqueTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK24QSGOpaqueTextureMaterial4typeEv(
    const QSGOpaqueTextureMaterial *self) {
  return self->QSGOpaqueTextureMaterial::type();
}

//  QSGMaterialShader
//      *QSGOpaqueTextureMaterial::createShader(QSGRendererInterface::RenderM
//      ode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK24QSGOpaqueTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGOpaqueTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGOpaqueTextureMaterial::createShader(renderMode);
}

//  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QSGOpaqueTextureMaterial7compareEPK11QSGMaterial(
    const QSGOpaqueTextureMaterial *self,
    const QSGMaterial *other) {
  return self->QSGOpaqueTextureMaterial::compare(other);
}
