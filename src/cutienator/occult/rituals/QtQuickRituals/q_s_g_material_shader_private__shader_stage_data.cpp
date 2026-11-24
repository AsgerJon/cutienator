//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgmaterialshader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgmaterialshader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData()
extern "C" Q_DECL_EXPORT
QSGMaterialShaderPrivate::ShaderStageData *ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataC1Ev() {
  return new QSGMaterialShaderPrivate::ShaderStageData();
}

//  QSGMaterialShaderPrivate::ShaderStageData::ShaderStageData(const QShader
//      &shader)
extern "C" Q_DECL_EXPORT
QSGMaterialShaderPrivate::ShaderStageData *ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataC1ERK7QShader(
    const QShader *shader) {
  return new QSGMaterialShaderPrivate::ShaderStageData(*shader);
}

//  QSGMaterialShaderPrivate::ShaderStageData::~ShaderStageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGMaterialShaderPrivate15ShaderStageDataD1Ev(
    QSGMaterialShaderPrivate::ShaderStageData *self) {
  delete self;
}
