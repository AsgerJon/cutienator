//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalimagenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QSGSmoothTextureMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGSmoothTextureMaterial : QSGSmoothTextureMaterial {
  using QSGSmoothTextureMaterial::type;
  using QSGSmoothTextureMaterial::createShader;
};

//  A QSGSmoothTextureMaterial that Python can take functions over in. Every QSGSmoothTextureMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGSmoothTextureMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGSmoothTextureMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGSmoothTextureMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGSmoothTextureMaterial : public QSGSmoothTextureMaterial {
public:
  using QSGSmoothTextureMaterial::QSGSmoothTextureMaterial;
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

  //  QSGMaterialType *QSGSmoothTextureMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSmoothTextureMaterialCall0 call = reinterpret_cast<CuteQSGSmoothTextureMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGSmoothTextureMaterial::type();
  }

  //  QSGMaterialShader *QSGSmoothTextureMaterial::createShader(QSGRenderer
  //      Interface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSmoothTextureMaterialCall1 call = reinterpret_cast<CuteQSGSmoothTextureMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGSmoothTextureMaterial::createShader(renderMode);
  }

  //  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSmoothTextureMaterialCall2 call = reinterpret_cast<CuteQSGSmoothTextureMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGOpaqueTextureMaterial::compare(other);
  }
};

//  QSGSmoothTextureMaterial::QSGSmoothTextureMaterial()
extern "C" Q_DECL_EXPORT
QSGSmoothTextureMaterial *ritual_ZN24QSGSmoothTextureMaterialC1Ev() {
  return new CuteQSGSmoothTextureMaterial();
}

//  void QSGSmoothTextureMaterial::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSmoothTextureMaterial10setTextureEP10QSGTexture(
    QSGSmoothTextureMaterial *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGMaterialType *QSGSmoothTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK24QSGSmoothTextureMaterial4typeEv(
    const QSGSmoothTextureMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGSmoothTextureMaterial::createShader(QSGRendererInterface::RenderM
//      ode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK24QSGSmoothTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGSmoothTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGSmoothTextureMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSmoothTextureMaterial(
    QSGSmoothTextureMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSmoothTextureMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGSmoothTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK24QSGSmoothTextureMaterial4typeEv(
    const QSGSmoothTextureMaterial *self) {
  return static_cast<const OwnQSGSmoothTextureMaterial *>(self)->OwnQSGSmoothTextureMaterial::type();
}

//  QSGMaterialShader
//      *QSGSmoothTextureMaterial::createShader(QSGRendererInterface::RenderM
//      ode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK24QSGSmoothTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGSmoothTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return static_cast<const OwnQSGSmoothTextureMaterial *>(self)->OwnQSGSmoothTextureMaterial::createShader(
      renderMode);
}
