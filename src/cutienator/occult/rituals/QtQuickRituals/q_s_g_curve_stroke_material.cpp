//  Written by hand on 2026-11-25 from
//  QtQuick/6.12.0/QtQuick/private/qsgcurvestrokenode_p_p.h, Qt 6.12.0, the same
//  text on every system. Kept as it is when the generator runs
//  again. Its inline code compiles only with
//  'QT_USE_QSTRINGBUILDER' defined, which 'Summon' tells the
//  compiler.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurvestrokenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGCurveStrokeMaterial that Python can take functions over in. Every
//  QSGCurveStrokeMaterial Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef int (*CuteQSGCurveStrokeMaterialCall0)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQSGCurveStrokeMaterialCall1)(const void *, int *);
typedef void * (*CuteQSGCurveStrokeMaterialCall2)(const void *, int, int *);
class CuteQSGCurveStrokeMaterial : public QSGCurveStrokeMaterial {
public:
  using QSGCurveStrokeMaterial::QSGCurveStrokeMaterial;
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

  //  int QSGCurveStrokeMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCurveStrokeMaterialCall0 call = reinterpret_cast<CuteQSGCurveStrokeMaterialCall0>(taken[0]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGCurveStrokeMaterial::compare(other);
  }

  //  QSGMaterialType *QSGCurveStrokeMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCurveStrokeMaterialCall1 call = reinterpret_cast<CuteQSGCurveStrokeMaterialCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGCurveStrokeMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGCurveStrokeMaterial::createShader(QSGRendererInterface::RenderM
  //      ode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCurveStrokeMaterialCall2 call = reinterpret_cast<CuteQSGCurveStrokeMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGCurveStrokeMaterial::createShader(renderMode);
  }
};

//  QSGCurveStrokeMaterial::QSGCurveStrokeMaterial(QSGCurveStrokeNode *node,
//      bool strokeExpanding)
extern "C" Q_DECL_EXPORT
QSGCurveStrokeMaterial *ritual_ZN22QSGCurveStrokeMaterialC1EP18QSGCurveStrokeNodeb(
    QSGCurveStrokeNode *node,
    bool strokeExpanding) {
  return new CuteQSGCurveStrokeMaterial(node, strokeExpanding);
}

//  int QSGCurveStrokeMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QSGCurveStrokeMaterial7compareEPK11QSGMaterial(
    const QSGCurveStrokeMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGCurveStrokeNode *QSGCurveStrokeMaterial::node() const
extern "C" Q_DECL_EXPORT
QSGCurveStrokeNode *ritual_ZNK22QSGCurveStrokeMaterial4nodeEv(
    const QSGCurveStrokeMaterial *self) {
  return self->node();
}

//  QSGMaterialType *QSGCurveStrokeMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK22QSGCurveStrokeMaterial4typeEv(
    const QSGCurveStrokeMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGCurveStrokeMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK22QSGCurveStrokeMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGCurveStrokeMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGCurveStrokeMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCurveStrokeMaterial(
    QSGCurveStrokeMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCurveStrokeMaterial *>(self)->take(key, call);
}

//  int QSGCurveStrokeMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QSGCurveStrokeMaterial7compareEPK11QSGMaterial(
    const QSGCurveStrokeMaterial *self,
    const QSGMaterial *other) {
  return self->QSGCurveStrokeMaterial::compare(other);
}

//  QSGMaterialType *QSGCurveStrokeMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK22QSGCurveStrokeMaterial4typeEv(
    const QSGCurveStrokeMaterial *self) {
  return self->QSGCurveStrokeMaterial::type();
}

//  QSGMaterialShader
//      *QSGCurveStrokeMaterial::createShader(QSGRendererInterface::RenderMod
//      e renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK22QSGCurveStrokeMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGCurveStrokeMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGCurveStrokeMaterial::createShader(renderMode);
}
