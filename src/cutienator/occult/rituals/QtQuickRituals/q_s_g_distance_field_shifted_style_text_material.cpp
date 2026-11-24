//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSGDistanceFieldShiftedStyleTextMaterial that Python can take functions over in. Every QSGDistanceFieldShiftedStyleTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGDistanceFieldShiftedStyleTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGDistanceFieldShiftedStyleTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGDistanceFieldShiftedStyleTextMaterialCall2)(const void *, const QSGMaterial *, int *);
typedef void (*CuteQSGDistanceFieldShiftedStyleTextMaterialCall3)(const void *, const QColor *, int *);
class CuteQSGDistanceFieldShiftedStyleTextMaterial : public QSGDistanceFieldShiftedStyleTextMaterial {
public:
  using QSGDistanceFieldShiftedStyleTextMaterial::QSGDistanceFieldShiftedStyleTextMaterial;
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

  //  QSGMaterialType *QSGDistanceFieldShiftedStyleTextMaterial::type()
  //      const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldShiftedStyleTextMaterialCall0 call = reinterpret_cast<CuteQSGDistanceFieldShiftedStyleTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGDistanceFieldShiftedStyleTextMaterial::type();
  }

  //  QSGMaterialShader *QSGDistanceFieldShiftedStyleTextMaterial::createSh
  //      ader(QSGRendererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldShiftedStyleTextMaterialCall1 call = reinterpret_cast<CuteQSGDistanceFieldShiftedStyleTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGDistanceFieldShiftedStyleTextMaterial::createShader(renderMode);
  }

  //  int QSGDistanceFieldShiftedStyleTextMaterial::compare(const
  //      QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldShiftedStyleTextMaterialCall2 call = reinterpret_cast<CuteQSGDistanceFieldShiftedStyleTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldShiftedStyleTextMaterial::compare(other);
  }

  //  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldShiftedStyleTextMaterialCall3 call = reinterpret_cast<CuteQSGDistanceFieldShiftedStyleTextMaterialCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldTextMaterial::setColor(color);
  }
};

//  QSGDistanceFieldShiftedStyleTextMaterial::QSGDistanceFieldShiftedStyleTex
//      tMaterial()
extern "C" Q_DECL_EXPORT
QSGDistanceFieldShiftedStyleTextMaterial *ritual_ZN40QSGDistanceFieldShiftedStyleTextMaterialC1Ev() {
  return new CuteQSGDistanceFieldShiftedStyleTextMaterial();
}

//  QSGDistanceFieldShiftedStyleTextMaterial::~QSGDistanceFieldShiftedStyleTe
//      xtMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QSGDistanceFieldShiftedStyleTextMaterialD1Ev(
    QSGDistanceFieldShiftedStyleTextMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGDistanceFieldShiftedStyleTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial4typeEv(
    const QSGDistanceFieldShiftedStyleTextMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGDistanceFieldShiftedStyleTextMaterial::createShader
//      (QSGRendererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldShiftedStyleTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGDistanceFieldShiftedStyleTextMaterial::compare(const QSGMaterial
//      *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldShiftedStyleTextMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  void QSGDistanceFieldShiftedStyleTextMaterial::setShift(const QPointF
//      &shift)
extern "C" Q_DECL_EXPORT
void ritual_ZN40QSGDistanceFieldShiftedStyleTextMaterial8setShiftERK7QPointF(
    QSGDistanceFieldShiftedStyleTextMaterial *self,
    const QPointF *shift) {
  self->setShift(*shift);
}

//  const QPointF &QSGDistanceFieldShiftedStyleTextMaterial::shift() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial5shiftEv(
    const QSGDistanceFieldShiftedStyleTextMaterial *self) {
  return new QPointF(self->shift());
}

//  a Python function taken by a
//      CuteQSGDistanceFieldShiftedStyleTextMaterial, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldShiftedStyleTextMaterial(
    QSGDistanceFieldShiftedStyleTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldShiftedStyleTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGDistanceFieldShiftedStyleTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial4typeEv(
    const QSGDistanceFieldShiftedStyleTextMaterial *self) {
  return self->QSGDistanceFieldShiftedStyleTextMaterial::type();
}

//  QSGMaterialShader *QSGDistanceFieldShiftedStyleTextMaterial::createShader
//      (QSGRendererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldShiftedStyleTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGDistanceFieldShiftedStyleTextMaterial::createShader(
      renderMode);
}

//  int QSGDistanceFieldShiftedStyleTextMaterial::compare(const QSGMaterial
//      *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldShiftedStyleTextMaterial *self,
    const QSGMaterial *other) {
  return self->QSGDistanceFieldShiftedStyleTextMaterial::compare(other);
}
