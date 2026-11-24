//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgflatcolormaterial.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgflatcolormaterial.h>
#include <QtGui/qcolor.h>

//  QSGFlatColorMaterial::QSGFlatColorMaterial()
extern "C" Q_DECL_EXPORT
QSGFlatColorMaterial *ritual_ZN20QSGFlatColorMaterialC1Ev() {
  return new QSGFlatColorMaterial();
}

//  QSGMaterialType *QSGFlatColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK20QSGFlatColorMaterial4typeEv(
    const QSGFlatColorMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGFlatColorMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK20QSGFlatColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGFlatColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  void QSGFlatColorMaterial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGFlatColorMaterial8setColorERK6QColor(
    QSGFlatColorMaterial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  const QColor &QSGFlatColorMaterial::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QSGFlatColorMaterial5colorEv(
    const QSGFlatColorMaterial *self) {
  return new QColor(self->color());
}

//  int QSGFlatColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGFlatColorMaterial7compareEPK11QSGMaterial(
    const QSGFlatColorMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialType *QSGFlatColorMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK20QSGFlatColorMaterial4typeEv(
    const QSGFlatColorMaterial *self) {
  return self->QSGFlatColorMaterial::type();
}

//  QSGMaterialShader
//      *QSGFlatColorMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK20QSGFlatColorMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGFlatColorMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QSGFlatColorMaterial::createShader(renderMode);
}

//  int QSGFlatColorMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QSGFlatColorMaterial7compareEPK11QSGMaterial(
    const QSGFlatColorMaterial *self,
    const QSGMaterial *other) {
  return self->QSGFlatColorMaterial::compare(other);
}
