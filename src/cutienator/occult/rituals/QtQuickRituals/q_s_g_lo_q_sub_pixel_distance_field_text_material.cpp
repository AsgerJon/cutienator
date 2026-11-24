//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSGLoQSubPixelDistanceFieldTextMaterial that Python can take functions over in. Every QSGLoQSubPixelDistanceFieldTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGLoQSubPixelDistanceFieldTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGLoQSubPixelDistanceFieldTextMaterialCall1)(const void *, int, int *);
typedef void (*CuteQSGLoQSubPixelDistanceFieldTextMaterialCall2)(const void *, const QColor *, int *);
typedef int (*CuteQSGLoQSubPixelDistanceFieldTextMaterialCall3)(const void *, const QSGMaterial *, int *);
class CuteQSGLoQSubPixelDistanceFieldTextMaterial : public QSGLoQSubPixelDistanceFieldTextMaterial {
public:
  using QSGLoQSubPixelDistanceFieldTextMaterial::QSGLoQSubPixelDistanceFieldTextMaterial;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QSGLoQSubPixelDistanceFieldTextMaterial::type()
  //      const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGLoQSubPixelDistanceFieldTextMaterialCall0 call = reinterpret_cast<CuteQSGLoQSubPixelDistanceFieldTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGLoQSubPixelDistanceFieldTextMaterial::type();
  }

  //  QSGMaterialShader *QSGLoQSubPixelDistanceFieldTextMaterial::createSha
  //      der(QSGRendererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGLoQSubPixelDistanceFieldTextMaterialCall1 call = reinterpret_cast<CuteQSGLoQSubPixelDistanceFieldTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGLoQSubPixelDistanceFieldTextMaterial::createShader(renderMode);
  }

  //  void QSGLoQSubPixelDistanceFieldTextMaterial::setColor(const QColor
  //      &color)
  void setColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGLoQSubPixelDistanceFieldTextMaterialCall2 call = reinterpret_cast<CuteQSGLoQSubPixelDistanceFieldTextMaterialCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGLoQSubPixelDistanceFieldTextMaterial::setColor(color);
  }

  //  int QSGDistanceFieldTextMaterial::compare(const QSGMaterial *other)
  //      const
  int compare(const QSGMaterial *other) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGLoQSubPixelDistanceFieldTextMaterialCall3 call = reinterpret_cast<CuteQSGLoQSubPixelDistanceFieldTextMaterialCall3>(taken[3]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldTextMaterial::compare(other);
  }
};

//  QSGMaterialType *QSGLoQSubPixelDistanceFieldTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK39QSGLoQSubPixelDistanceFieldTextMaterial4typeEv(
    const QSGLoQSubPixelDistanceFieldTextMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGLoQSubPixelDistanceFieldTextMaterial::createShader(
//      QSGRendererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK39QSGLoQSubPixelDistanceFieldTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGLoQSubPixelDistanceFieldTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  void QSGLoQSubPixelDistanceFieldTextMaterial::setColor(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QSGLoQSubPixelDistanceFieldTextMaterial8setColorERK6QColor(
    QSGLoQSubPixelDistanceFieldTextMaterial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  a Python function taken by a CuteQSGLoQSubPixelDistanceFieldTextMaterial,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGLoQSubPixelDistanceFieldTextMaterial(
    QSGLoQSubPixelDistanceFieldTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGLoQSubPixelDistanceFieldTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGLoQSubPixelDistanceFieldTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK39QSGLoQSubPixelDistanceFieldTextMaterial4typeEv(
    const QSGLoQSubPixelDistanceFieldTextMaterial *self) {
  return self->QSGLoQSubPixelDistanceFieldTextMaterial::type();
}

//  QSGMaterialShader *QSGLoQSubPixelDistanceFieldTextMaterial::createShader(
//      QSGRendererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK39QSGLoQSubPixelDistanceFieldTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGLoQSubPixelDistanceFieldTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGLoQSubPixelDistanceFieldTextMaterial::createShader(
      renderMode);
}

//  void QSGLoQSubPixelDistanceFieldTextMaterial::setColor(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN39QSGLoQSubPixelDistanceFieldTextMaterial8setColorERK6QColor(
    QSGLoQSubPixelDistanceFieldTextMaterial *self,
    const QColor *color) {
  self->QSGLoQSubPixelDistanceFieldTextMaterial::setColor(*color);
}
