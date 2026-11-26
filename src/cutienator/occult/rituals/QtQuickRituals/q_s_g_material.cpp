//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgmaterial.h>
#include <cstring>

//  A QSGMaterial that Python can take functions over in. Every QSGMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGMaterial : public QSGMaterial {
public:
  using QSGMaterial::QSGMaterial;
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

  //  QSGMaterialType *QSGMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGMaterialCall0 call = reinterpret_cast<CuteQSGMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return {};
  }

  //  QSGMaterialShader
  //      *QSGMaterial::createShader(QSGRendererInterface::RenderMode
  //      renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGMaterialCall1 call = reinterpret_cast<CuteQSGMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return {};
  }

  //  int QSGMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGMaterialCall2 call = reinterpret_cast<CuteQSGMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGMaterial::compare(other);
  }
};

//  QSGMaterial::QSGMaterial()
extern "C" Q_DECL_EXPORT
QSGMaterial *ritual_ZN11QSGMaterialC1Ev() {
  return new CuteQSGMaterial();
}

//  QSGMaterial::~QSGMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGMaterialD1Ev(QSGMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK11QSGMaterial4typeEv(const QSGMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGMaterial7compareEPKS_(
    const QSGMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterial::Flags QSGMaterial::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGMaterial5flagsEv(const QSGMaterial *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QSGMaterial::setFlag(Flags flags, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGMaterial7setFlagE6QFlagsINS_4FlagEEb(
    QSGMaterial *self,
    int flags,
    bool on) {
  self->setFlag(QFlags<QSGMaterial::Flag>::fromInt(flags), on);
}

//  int QSGMaterial::viewCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGMaterial9viewCountEv(const QSGMaterial *self) {
  return self->viewCount();
}

//  a Python function taken by a CuteQSGMaterial, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGMaterial(
    QSGMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGMaterial *>(self)->take(key, call);
}

//  int QSGMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QSGMaterial7compareEPKS_(
    const QSGMaterial *self,
    const QSGMaterial *other) {
  return self->QSGMaterial::compare(other);
}
