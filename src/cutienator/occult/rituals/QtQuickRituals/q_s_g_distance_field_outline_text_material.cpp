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

//  A QSGDistanceFieldOutlineTextMaterial that Python can take functions over in. Every QSGDistanceFieldOutlineTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGDistanceFieldOutlineTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGDistanceFieldOutlineTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGDistanceFieldOutlineTextMaterialCall2)(const void *, const QSGMaterial *, int *);
typedef void (*CuteQSGDistanceFieldOutlineTextMaterialCall3)(const void *, const QColor *, int *);
class CuteQSGDistanceFieldOutlineTextMaterial : public QSGDistanceFieldOutlineTextMaterial {
public:
  using QSGDistanceFieldOutlineTextMaterial::QSGDistanceFieldOutlineTextMaterial;
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
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QSGDistanceFieldOutlineTextMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldOutlineTextMaterialCall0 call = reinterpret_cast<CuteQSGDistanceFieldOutlineTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGDistanceFieldOutlineTextMaterial::type();
  }

  //  QSGMaterialShader *QSGDistanceFieldOutlineTextMaterial::createShader(
  //      QSGRendererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldOutlineTextMaterialCall1 call = reinterpret_cast<CuteQSGDistanceFieldOutlineTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGDistanceFieldOutlineTextMaterial::createShader(renderMode);
  }

  //  int QSGDistanceFieldStyledTextMaterial::compare(const QSGMaterial
  //      *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldOutlineTextMaterialCall2 call = reinterpret_cast<CuteQSGDistanceFieldOutlineTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldStyledTextMaterial::compare(other);
  }

  //  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldOutlineTextMaterialCall3 call = reinterpret_cast<CuteQSGDistanceFieldOutlineTextMaterialCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldTextMaterial::setColor(color);
  }
};

//  QSGDistanceFieldOutlineTextMaterial::QSGDistanceFieldOutlineTextMaterial(
//      )
extern "C" Q_DECL_EXPORT
QSGDistanceFieldOutlineTextMaterial *ritual_ZN35QSGDistanceFieldOutlineTextMaterialC1Ev() {
  return new CuteQSGDistanceFieldOutlineTextMaterial();
}

//  QSGDistanceFieldOutlineTextMaterial::~QSGDistanceFieldOutlineTextMaterial
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QSGDistanceFieldOutlineTextMaterialD1Ev(
    QSGDistanceFieldOutlineTextMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGDistanceFieldOutlineTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK35QSGDistanceFieldOutlineTextMaterial4typeEv(
    const QSGDistanceFieldOutlineTextMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGDistanceFieldOutlineTextMaterial::createShader(QSGR
//      endererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK35QSGDistanceFieldOutlineTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldOutlineTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  a Python function taken by a CuteQSGDistanceFieldOutlineTextMaterial, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldOutlineTextMaterial(
    QSGDistanceFieldOutlineTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldOutlineTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGDistanceFieldOutlineTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK35QSGDistanceFieldOutlineTextMaterial4typeEv(
    const QSGDistanceFieldOutlineTextMaterial *self) {
  return self->QSGDistanceFieldOutlineTextMaterial::type();
}

//  QSGMaterialShader *QSGDistanceFieldOutlineTextMaterial::createShader(QSGR
//      endererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK35QSGDistanceFieldOutlineTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldOutlineTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGDistanceFieldOutlineTextMaterial::createShader(renderMode);
}
