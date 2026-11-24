//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgmaterialshader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qsgmaterialshader.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgmaterialshader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSGMaterialShader *QSGMaterialShaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZN24QSGMaterialShaderPrivate6q_funcEv(
    QSGMaterialShaderPrivate *self) {
  return self->q_func();
}

//  const QSGMaterialShader *QSGMaterialShaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSGMaterialShader *ritual_ZNK24QSGMaterialShaderPrivate6q_funcEv(
    const QSGMaterialShaderPrivate *self) {
  return self->q_func();
}

//  QSGMaterialShaderPrivate::QSGMaterialShaderPrivate(QSGMaterialShader *q)
extern "C" Q_DECL_EXPORT
QSGMaterialShaderPrivate *ritual_ZN24QSGMaterialShaderPrivateC1EP17QSGMaterialShader(
    QSGMaterialShader *q) {
  return new QSGMaterialShaderPrivate(q);
}

//  QSGMaterialShaderPrivate *QSGMaterialShaderPrivate::get(QSGMaterialShader
//      *s)
extern "C" Q_DECL_EXPORT
QSGMaterialShaderPrivate *ritual_ZN24QSGMaterialShaderPrivate3getEP17QSGMaterialShader(
    QSGMaterialShader *s) {
  return QSGMaterialShaderPrivate::get(s);
}

//  const QSGMaterialShaderPrivate *QSGMaterialShaderPrivate::get(const
//      QSGMaterialShader *s)
extern "C" Q_DECL_EXPORT
const QSGMaterialShaderPrivate *ritual_ZN24QSGMaterialShaderPrivate3getEPK17QSGMaterialShader(
    const QSGMaterialShader *s) {
  return QSGMaterialShaderPrivate::get(s);
}

//  void QSGMaterialShaderPrivate::clearCachedRendererData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGMaterialShaderPrivate23clearCachedRendererDataEv(
    QSGMaterialShaderPrivate *self) {
  self->clearCachedRendererData();
}

//  void QSGMaterialShaderPrivate::prepare(QShader::Variant
//      vertexShaderVariant)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGMaterialShaderPrivate7prepareEN7QShader7VariantE(
    QSGMaterialShaderPrivate *self,
    QShader::Variant vertexShaderVariant) {
  self->prepare(vertexShaderVariant);
}

//  QShader QSGMaterialShaderPrivate::shader(QShader::Stage stage) const
extern "C" Q_DECL_EXPORT
QShader *ritual_ZNK24QSGMaterialShaderPrivate6shaderEN7QShader5StageE(
    const QSGMaterialShaderPrivate *self,
    QShader::Stage stage) {
  return new QShader(self->shader(stage));
}

//  QShader QSGMaterialShaderPrivate::loadShader(const QString &filename)
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN24QSGMaterialShaderPrivate10loadShaderERK7QString(
    const QString *filename) {
  return new QShader(QSGMaterialShaderPrivate::loadShader(*filename));
}

//  QSGMaterialShaderPrivate::~QSGMaterialShaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGMaterialShaderPrivateD1Ev(
    QSGMaterialShaderPrivate *self) {
  delete self;
}
