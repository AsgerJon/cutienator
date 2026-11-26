//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <cstring>

//  A QSGDistanceFieldStyledTextMaterial that Python can take functions over in. Every QSGDistanceFieldStyledTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGDistanceFieldStyledTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGDistanceFieldStyledTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGDistanceFieldStyledTextMaterialCall2)(const void *, const QSGMaterial *, int *);
typedef void (*CuteQSGDistanceFieldStyledTextMaterialCall3)(const void *, const QColor *, int *);
class CuteQSGDistanceFieldStyledTextMaterial : public QSGDistanceFieldStyledTextMaterial {
public:
  using QSGDistanceFieldStyledTextMaterial::QSGDistanceFieldStyledTextMaterial;
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

  //  QSGMaterialType *QSGDistanceFieldStyledTextMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldStyledTextMaterialCall0 call = reinterpret_cast<CuteQSGDistanceFieldStyledTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return {};
  }

  //  QSGMaterialShader *QSGDistanceFieldStyledTextMaterial::createShader(Q
  //      SGRendererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldStyledTextMaterialCall1 call = reinterpret_cast<CuteQSGDistanceFieldStyledTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return {};
  }

  //  int QSGDistanceFieldStyledTextMaterial::compare(const QSGMaterial
  //      *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldStyledTextMaterialCall2 call = reinterpret_cast<CuteQSGDistanceFieldStyledTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldStyledTextMaterial::compare(other);
  }

  //  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldStyledTextMaterialCall3 call = reinterpret_cast<CuteQSGDistanceFieldStyledTextMaterialCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldTextMaterial::setColor(color);
  }
};

//  QSGDistanceFieldStyledTextMaterial::QSGDistanceFieldStyledTextMaterial()
extern "C" Q_DECL_EXPORT
QSGDistanceFieldStyledTextMaterial *ritual_ZN34QSGDistanceFieldStyledTextMaterialC1Ev() {
  return new CuteQSGDistanceFieldStyledTextMaterial();
}

//  QSGDistanceFieldStyledTextMaterial::~QSGDistanceFieldStyledTextMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSGDistanceFieldStyledTextMaterialD1Ev(
    QSGDistanceFieldStyledTextMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGDistanceFieldStyledTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK34QSGDistanceFieldStyledTextMaterial4typeEv(
    const QSGDistanceFieldStyledTextMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGDistanceFieldStyledTextMaterial::createShader(QSGRe
//      ndererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK34QSGDistanceFieldStyledTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldStyledTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGDistanceFieldStyledTextMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QSGDistanceFieldStyledTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldStyledTextMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  void QSGDistanceFieldStyledTextMaterial::setStyleColor(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSGDistanceFieldStyledTextMaterial13setStyleColorERK6QColor(
    QSGDistanceFieldStyledTextMaterial *self,
    const QColor *color) {
  self->setStyleColor(*color);
}

//  const QVector4D &QSGDistanceFieldStyledTextMaterial::styleColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK34QSGDistanceFieldStyledTextMaterial10styleColorEv(
    const QSGDistanceFieldStyledTextMaterial *self) {
  return new QVector4D(self->styleColor());
}

//  a Python function taken by a CuteQSGDistanceFieldStyledTextMaterial, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldStyledTextMaterial(
    QSGDistanceFieldStyledTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldStyledTextMaterial *>(self)->take(key, call);
}

//  int QSGDistanceFieldStyledTextMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK34QSGDistanceFieldStyledTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldStyledTextMaterial *self,
    const QSGMaterial *other) {
  return self->QSGDistanceFieldStyledTextMaterial::compare(other);
}
