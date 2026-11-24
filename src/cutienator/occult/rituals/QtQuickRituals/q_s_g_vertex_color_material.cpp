//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgvertexcolormaterial.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgvertexcolormaterial.h>
#include <cstring>

//  Only a class built on QSGVertexColorMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGVertexColorMaterial : QSGVertexColorMaterial {
  using QSGVertexColorMaterial::type;
  using QSGVertexColorMaterial::createShader;
};

//  A QSGVertexColorMaterial that Python can take functions over in. Every QSGVertexColorMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGVertexColorMaterialCall0)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQSGVertexColorMaterialCall1)(const void *, int *);
typedef void * (*CuteQSGVertexColorMaterialCall2)(const void *, int, int *);
class CuteQSGVertexColorMaterial : public QSGVertexColorMaterial {
public:
  using QSGVertexColorMaterial::QSGVertexColorMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  int QSGVertexColorMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGVertexColorMaterialCall0 call = reinterpret_cast<CuteQSGVertexColorMaterialCall0>(taken[0]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGVertexColorMaterial::compare(other);
  }

  //  QSGMaterialType *QSGVertexColorMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGVertexColorMaterialCall1 call = reinterpret_cast<CuteQSGVertexColorMaterialCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGVertexColorMaterial::type();
  }

  //  QSGMaterialShader *QSGVertexColorMaterial::createShader(QSGRendererIn
  //      terface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGVertexColorMaterialCall2 call = reinterpret_cast<CuteQSGVertexColorMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGVertexColorMaterial::createShader(renderMode);
  }
};

//  QSGVertexColorMaterial::QSGVertexColorMaterial()
extern "C" Q_DECL_EXPORT
QSGVertexColorMaterial *ritual_ZN22QSGVertexColorMaterialC1Ev() {
  return new CuteQSGVertexColorMaterial();
}

//  int QSGVertexColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QSGVertexColorMaterial7compareEPK11QSGMaterial(
    const QSGVertexColorMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialType *QSGVertexColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK22QSGVertexColorMaterial4typeEv(
    const QSGVertexColorMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGVertexColorMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK22QSGVertexColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGVertexColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGVertexColorMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGVertexColorMaterial(
    QSGVertexColorMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGVertexColorMaterial *>(self)->take(key, call);
}

//  int QSGVertexColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QSGVertexColorMaterial7compareEPK11QSGMaterial(
    const QSGVertexColorMaterial *self,
    const QSGMaterial *other) {
  return self->QSGVertexColorMaterial::compare(other);
}

//  QSGMaterialType *QSGVertexColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK22QSGVertexColorMaterial4typeEv(
    const QSGVertexColorMaterial *self) {
  return static_cast<const OwnQSGVertexColorMaterial *>(self)->OwnQSGVertexColorMaterial::type();
}

//  QSGMaterialShader
//      *QSGVertexColorMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK22QSGVertexColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGVertexColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return static_cast<const OwnQSGVertexColorMaterial *>(self)->OwnQSGVertexColorMaterial::createShader(
      renderMode);
}
