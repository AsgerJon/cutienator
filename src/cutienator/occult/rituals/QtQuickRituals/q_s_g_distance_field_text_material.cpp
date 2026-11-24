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
#include <QtCore/qsize.h>
#include <cstring>

//  A QSGDistanceFieldTextMaterial that Python can take functions over in. Every QSGDistanceFieldTextMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGDistanceFieldTextMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGDistanceFieldTextMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGDistanceFieldTextMaterialCall2)(const void *, const QSGMaterial *, int *);
typedef void (*CuteQSGDistanceFieldTextMaterialCall3)(const void *, const QColor *, int *);
class CuteQSGDistanceFieldTextMaterial : public QSGDistanceFieldTextMaterial {
public:
  using QSGDistanceFieldTextMaterial::QSGDistanceFieldTextMaterial;
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

  //  QSGMaterialType *QSGDistanceFieldTextMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldTextMaterialCall0 call = reinterpret_cast<CuteQSGDistanceFieldTextMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGDistanceFieldTextMaterial::type();
  }

  //  QSGMaterialShader *QSGDistanceFieldTextMaterial::createShader(QSGRend
  //      ererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldTextMaterialCall1 call = reinterpret_cast<CuteQSGDistanceFieldTextMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGDistanceFieldTextMaterial::createShader(renderMode);
  }

  //  int QSGDistanceFieldTextMaterial::compare(const QSGMaterial *other)
  //      const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldTextMaterialCall2 call = reinterpret_cast<CuteQSGDistanceFieldTextMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGDistanceFieldTextMaterial::compare(other);
  }

  //  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldTextMaterialCall3 call = reinterpret_cast<CuteQSGDistanceFieldTextMaterialCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldTextMaterial::setColor(color);
  }
};

//  QSGDistanceFieldTextMaterial::QSGDistanceFieldTextMaterial()
extern "C" Q_DECL_EXPORT
QSGDistanceFieldTextMaterial *ritual_ZN28QSGDistanceFieldTextMaterialC1Ev() {
  return new CuteQSGDistanceFieldTextMaterial();
}

//  QSGDistanceFieldTextMaterial::~QSGDistanceFieldTextMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGDistanceFieldTextMaterialD1Ev(
    QSGDistanceFieldTextMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGDistanceFieldTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK28QSGDistanceFieldTextMaterial4typeEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->type();
}

//  QSGMaterialShader *QSGDistanceFieldTextMaterial::createShader(QSGRenderer
//      Interface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK28QSGDistanceFieldTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGDistanceFieldTextMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QSGDistanceFieldTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldTextMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor(
    QSGDistanceFieldTextMaterial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  const QVector4D &QSGDistanceFieldTextMaterial::color() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK28QSGDistanceFieldTextMaterial5colorEv(
    const QSGDistanceFieldTextMaterial *self) {
  return new QVector4D(self->color());
}

//  void
//      QSGDistanceFieldTextMaterial::setGlyphCache(QSGDistanceFieldGlyphCach
//      e *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGDistanceFieldTextMaterial13setGlyphCacheEP26QSGDistanceFieldGlyphCache(
    QSGDistanceFieldTextMaterial *self,
    QSGDistanceFieldGlyphCache *a) {
  self->setGlyphCache(a);
}

//  QSGDistanceFieldGlyphCache *QSGDistanceFieldTextMaterial::glyphCache()
//      const
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphCache *ritual_ZNK28QSGDistanceFieldTextMaterial10glyphCacheEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->glyphCache();
}

//  void QSGDistanceFieldTextMaterial::setTexture(const
//      QSGDistanceFieldGlyphCache::Texture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGDistanceFieldTextMaterial10setTextureEPKN26QSGDistanceFieldGlyphCache7TextureE(
    QSGDistanceFieldTextMaterial *self,
    const QSGDistanceFieldGlyphCache::Texture *tex) {
  self->setTexture(tex);
}

//  const QSGDistanceFieldGlyphCache::Texture
//      *QSGDistanceFieldTextMaterial::texture() const
extern "C" Q_DECL_EXPORT
const QSGDistanceFieldGlyphCache::Texture *ritual_ZNK28QSGDistanceFieldTextMaterial7textureEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->texture();
}

//  void QSGDistanceFieldTextMaterial::setFontScale(qreal fontScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGDistanceFieldTextMaterial12setFontScaleEd(
    QSGDistanceFieldTextMaterial *self,
    qreal fontScale) {
  self->setFontScale(fontScale);
}

//  qreal QSGDistanceFieldTextMaterial::fontScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QSGDistanceFieldTextMaterial9fontScaleEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->fontScale();
}

//  QSize QSGDistanceFieldTextMaterial::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK28QSGDistanceFieldTextMaterial11textureSizeEv(
    const QSGDistanceFieldTextMaterial *self) {
  return new QSize(self->textureSize());
}

//  bool QSGDistanceFieldTextMaterial::updateTextureSize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGDistanceFieldTextMaterial17updateTextureSizeEv(
    QSGDistanceFieldTextMaterial *self) {
  return self->updateTextureSize();
}

//  bool QSGDistanceFieldTextMaterial::updateTextureSizeAndWrapper()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGDistanceFieldTextMaterial27updateTextureSizeAndWrapperEv(
    QSGDistanceFieldTextMaterial *self) {
  return self->updateTextureSizeAndWrapper();
}

//  QSGTexture *QSGDistanceFieldTextMaterial::wrapperTexture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK28QSGDistanceFieldTextMaterial14wrapperTextureEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->wrapperTexture();
}

//  a Python function taken by a CuteQSGDistanceFieldTextMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldTextMaterial(
    QSGDistanceFieldTextMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldTextMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGDistanceFieldTextMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK28QSGDistanceFieldTextMaterial4typeEv(
    const QSGDistanceFieldTextMaterial *self) {
  return self->QSGDistanceFieldTextMaterial::type();
}

//  QSGMaterialShader *QSGDistanceFieldTextMaterial::createShader(QSGRenderer
//      Interface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK28QSGDistanceFieldTextMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGDistanceFieldTextMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGDistanceFieldTextMaterial::createShader(renderMode);
}

//  int QSGDistanceFieldTextMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QSGDistanceFieldTextMaterial7compareEPK11QSGMaterial(
    const QSGDistanceFieldTextMaterial *self,
    const QSGMaterial *other) {
  return self->QSGDistanceFieldTextMaterial::compare(other);
}

//  void QSGDistanceFieldTextMaterial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGDistanceFieldTextMaterial8setColorERK6QColor(
    QSGDistanceFieldTextMaterial *self,
    const QColor *color) {
  self->QSGDistanceFieldTextMaterial::setColor(*color);
}
