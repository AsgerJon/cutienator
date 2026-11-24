//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickimageparticle_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickimageparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A ImageMaterial that Python can take functions over in. Every ImageMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteImageMaterialCall0)(const void *, int *);
typedef void * (*CuteImageMaterialCall1)(const void *, int, int *);
typedef int (*CuteImageMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteImageMaterial : public ImageMaterial {
public:
  using ImageMaterial::ImageMaterial;
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

  //  QSGMaterialType *QSGMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteImageMaterialCall0 call = reinterpret_cast<CuteImageMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return {};
  }

  //  QSGMaterialShader
  //      *QSGMaterial::createShader(QSGRendererInterface::RenderMode
  //      renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteImageMaterialCall1 call = reinterpret_cast<CuteImageMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return {};
  }

  //  int QSGMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteImageMaterialCall2 call = reinterpret_cast<CuteImageMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGMaterial::compare(other);
  }
};

//  a Python function taken by a CuteImageMaterial, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ImageMaterial(
    ImageMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteImageMaterial *>(self)->take(key, call);
}
