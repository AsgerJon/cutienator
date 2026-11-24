//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGCurveFillMaterial that Python can take functions over in. Every QSGCurveFillMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGCurveFillMaterialCall0)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQSGCurveFillMaterialCall1)(const void *, int *);
typedef void * (*CuteQSGCurveFillMaterialCall2)(const void *, int, int *);
class CuteQSGCurveFillMaterial : public QSGCurveFillMaterial {
public:
  using QSGCurveFillMaterial::QSGCurveFillMaterial;
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

  //  int QSGCurveFillMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCurveFillMaterialCall0 call = reinterpret_cast<CuteQSGCurveFillMaterialCall0>(taken[0]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGCurveFillMaterial::compare(other);
  }

  //  QSGMaterialType *QSGCurveFillMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCurveFillMaterialCall1 call = reinterpret_cast<CuteQSGCurveFillMaterialCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGCurveFillMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGCurveFillMaterial::createShader(QSGRendererInterface::RenderM
  //      ode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCurveFillMaterialCall2 call = reinterpret_cast<CuteQSGCurveFillMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGCurveFillMaterial::createShader(renderMode);
  }
};

//  QSGCurveFillMaterial::QSGCurveFillMaterial(QSGCurveFillNode *node)
extern "C" Q_DECL_EXPORT
QSGCurveFillMaterial *ritual_ZN20QSGCurveFillMaterialC1EP16QSGCurveFillNode(
    QSGCurveFillNode *node) {
  return new CuteQSGCurveFillMaterial(node);
}

//  QSGCurveFillMaterial::~QSGCurveFillMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCurveFillMaterialD1Ev(QSGCurveFillMaterial *self) {
  delete self;
}

//  int QSGCurveFillMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGCurveFillMaterial7compareEPK11QSGMaterial(
    const QSGCurveFillMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGCurveFillNode *QSGCurveFillMaterial::node() const
extern "C" Q_DECL_EXPORT
QSGCurveFillNode *ritual_ZNK20QSGCurveFillMaterial4nodeEv(
    const QSGCurveFillMaterial *self) {
  return self->node();
}

//  QSGPlainTexture *QSGCurveFillMaterial::dummyTexture() const
extern "C" Q_DECL_EXPORT
QSGPlainTexture *ritual_ZNK20QSGCurveFillMaterial12dummyTextureEv(
    const QSGCurveFillMaterial *self) {
  return self->dummyTexture();
}

//  void QSGCurveFillMaterial::setDummyTexture(QSGPlainTexture *dummyTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCurveFillMaterial15setDummyTextureEP15QSGPlainTexture(
    QSGCurveFillMaterial *self,
    QSGPlainTexture *dummyTexture) {
  self->setDummyTexture(dummyTexture);
}

//  QSGMaterialType *QSGCurveFillMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK20QSGCurveFillMaterial4typeEv(
    const QSGCurveFillMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGCurveFillMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK20QSGCurveFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGCurveFillMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGCurveFillMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCurveFillMaterial(
    QSGCurveFillMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCurveFillMaterial *>(self)->take(key, call);
}

//  int QSGCurveFillMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QSGCurveFillMaterial7compareEPK11QSGMaterial(
    const QSGCurveFillMaterial *self,
    const QSGMaterial *other) {
  return self->QSGCurveFillMaterial::compare(other);
}

//  QSGMaterialType *QSGCurveFillMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK20QSGCurveFillMaterial4typeEv(
    const QSGCurveFillMaterial *self) {
  return self->QSGCurveFillMaterial::type();
}

//  QSGMaterialShader
//      *QSGCurveFillMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK20QSGCurveFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGCurveFillMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGCurveFillMaterial::createShader(renderMode);
}
