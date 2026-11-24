//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QSGSmoothColorMaterial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGSmoothColorMaterial : QSGSmoothColorMaterial {
  using QSGSmoothColorMaterial::type;
  using QSGSmoothColorMaterial::createShader;
};

//  A QSGSmoothColorMaterial that Python can take functions over in. Every QSGSmoothColorMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGSmoothColorMaterialCall0)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQSGSmoothColorMaterialCall1)(const void *, int *);
typedef void * (*CuteQSGSmoothColorMaterialCall2)(const void *, int, int *);
class CuteQSGSmoothColorMaterial : public QSGSmoothColorMaterial {
public:
  using QSGSmoothColorMaterial::QSGSmoothColorMaterial;
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

  //  int QSGSmoothColorMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSmoothColorMaterialCall0 call = reinterpret_cast<CuteQSGSmoothColorMaterialCall0>(taken[0]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGSmoothColorMaterial::compare(other);
  }

  //  QSGMaterialType *QSGSmoothColorMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSmoothColorMaterialCall1 call = reinterpret_cast<CuteQSGSmoothColorMaterialCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGSmoothColorMaterial::type();
  }

  //  QSGMaterialShader *QSGSmoothColorMaterial::createShader(QSGRendererIn
  //      terface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSmoothColorMaterialCall2 call = reinterpret_cast<CuteQSGSmoothColorMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGSmoothColorMaterial::createShader(renderMode);
  }
};

//  QSGSmoothColorMaterial::QSGSmoothColorMaterial()
extern "C" Q_DECL_EXPORT
QSGSmoothColorMaterial *ritual_ZN22QSGSmoothColorMaterialC1Ev() {
  return new CuteQSGSmoothColorMaterial();
}

//  int QSGSmoothColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QSGSmoothColorMaterial7compareEPK11QSGMaterial(
    const QSGSmoothColorMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialType *QSGSmoothColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK22QSGSmoothColorMaterial4typeEv(
    const QSGSmoothColorMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGSmoothColorMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK22QSGSmoothColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGSmoothColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGSmoothColorMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSmoothColorMaterial(
    QSGSmoothColorMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSmoothColorMaterial *>(self)->take(key, call);
}

//  int QSGSmoothColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QSGSmoothColorMaterial7compareEPK11QSGMaterial(
    const QSGSmoothColorMaterial *self,
    const QSGMaterial *other) {
  return self->QSGSmoothColorMaterial::compare(other);
}

//  QSGMaterialType *QSGSmoothColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK22QSGSmoothColorMaterial4typeEv(
    const QSGSmoothColorMaterial *self) {
  return static_cast<const OwnQSGSmoothColorMaterial *>(self)->OwnQSGSmoothColorMaterial::type();
}

//  QSGMaterialShader
//      *QSGSmoothColorMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK22QSGSmoothColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGSmoothColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return static_cast<const OwnQSGSmoothColorMaterial *>(self)->OwnQSGSmoothColorMaterial::createShader(
      renderMode);
}
