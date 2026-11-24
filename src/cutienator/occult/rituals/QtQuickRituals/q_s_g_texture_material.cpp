//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexturematerial.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexturematerial.h>
#include <cstring>

//  A QSGTextureMaterial that Python can take functions over in. Every QSGTextureMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGTextureMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGTextureMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGTextureMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGTextureMaterial : public QSGTextureMaterial {
public:
  using QSGTextureMaterial::QSGTextureMaterial;
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

  //  QSGMaterialType *QSGTextureMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTextureMaterialCall0 call = reinterpret_cast<CuteQSGTextureMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGTextureMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGTextureMaterial::createShader(QSGRendererInterface::RenderMod
  //      e renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTextureMaterialCall1 call = reinterpret_cast<CuteQSGTextureMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGTextureMaterial::createShader(renderMode);
  }

  //  int QSGOpaqueTextureMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGTextureMaterialCall2 call = reinterpret_cast<CuteQSGTextureMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGOpaqueTextureMaterial::compare(other);
  }
};

//  QSGMaterialType *QSGTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK18QSGTextureMaterial4typeEv(
    const QSGTextureMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGTextureMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK18QSGTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGTextureMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTextureMaterial(
    QSGTextureMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTextureMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGTextureMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK18QSGTextureMaterial4typeEv(
    const QSGTextureMaterial *self) {
  return self->QSGTextureMaterial::type();
}

//  QSGMaterialShader
//      *QSGTextureMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK18QSGTextureMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGTextureMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGTextureMaterial::createShader(renderMode);
}
