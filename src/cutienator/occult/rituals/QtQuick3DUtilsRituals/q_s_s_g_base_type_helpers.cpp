//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGBaseTypeHelpers::QSSGBaseTypeHelpers()
extern "C" Q_DECL_EXPORT
QSSGBaseTypeHelpers *ritual_ZN19QSSGBaseTypeHelpersC1Ev() {
  return new QSSGBaseTypeHelpers();
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureCubeFace
//      value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE25QSSGRenderTextureCubeFace(
    QSSGRenderTextureCubeFace value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureTypeValue
//      value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE26QSSGRenderTextureTypeValue(
    QSSGRenderTextureTypeValue value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGDepthDrawMode value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE17QSSGDepthDrawMode(
    QSSGDepthDrawMode value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderWinding value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE17QSSGRenderWinding(
    QSSGRenderWinding value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGCullFaceMode value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE16QSSGCullFaceMode(
    QSSGCullFaceMode value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderComponentType value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE23QSSGRenderComponentType(
    QSSGRenderComponentType value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureFormat::Format
//      value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringEN23QSSGRenderTextureFormat6FormatE(
    QSSGRenderTextureFormat::Format value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureCoordOp value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE24QSSGRenderTextureCoordOp(
    QSSGRenderTextureCoordOp value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureFilterOp
//      value)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers8toStringE25QSSGRenderTextureFilterOp(
    QSSGRenderTextureFilterOp value) {
  return QSSGBaseTypeHelpers::toString(value);
}

//  QByteArray QSSGBaseTypeHelpers::toString(QSSGRenderSamplerType value)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN19QSSGBaseTypeHelpers8toStringE21QSSGRenderSamplerType(
    QSSGRenderSamplerType value) {
  return new QByteArray(QSSGBaseTypeHelpers::toString(value));
}

//  const char *QSSGBaseTypeHelpers::displayName(QSSGRenderTextureCubeFace
//      face)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN19QSSGBaseTypeHelpers11displayNameE25QSSGRenderTextureCubeFace(
    QSSGRenderTextureCubeFace face) {
  return QSSGBaseTypeHelpers::displayName(face);
}

//  QSSGRenderTextureCubeFace
//      QSSGBaseTypeHelpers::next(QSSGRenderTextureCubeFace face)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureCubeFace ritual_ZN19QSSGBaseTypeHelpers4nextE25QSSGRenderTextureCubeFace(
    QSSGRenderTextureCubeFace face) {
  return QSSGBaseTypeHelpers::next(face);
}

//  QSSGRenderTextureCubeFace
//      QSSGBaseTypeHelpers::prev(QSSGRenderTextureCubeFace face)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureCubeFace ritual_ZN19QSSGBaseTypeHelpers4prevE25QSSGRenderTextureCubeFace(
    QSSGRenderTextureCubeFace face) {
  return QSSGBaseTypeHelpers::prev(face);
}

//  QSSGRenderTextureCubeFaceT
//      QSSGBaseTypeHelpers::indexOfCubeFace(QSSGRenderTextureCubeFace face)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureCubeFaceT ritual_ZN19QSSGBaseTypeHelpers15indexOfCubeFaceE25QSSGRenderTextureCubeFace(
    QSSGRenderTextureCubeFace face) {
  return QSSGBaseTypeHelpers::indexOfCubeFace(face);
}

//  QSSGBaseTypeHelpers::~QSSGBaseTypeHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGBaseTypeHelpersD1Ev(QSSGBaseTypeHelpers *self) {
  delete self;
}
