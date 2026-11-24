//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>

//  QSSGSceneDesc::TextureData::TextureData(const QByteArray &textureData,
//      QSize size, const QByteArray &format, quint8 flags, QByteArray name)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::TextureData *ritual_ZN13QSSGSceneDesc11TextureDataC1ERK10QByteArray5QSizeS3_hS1_(
    const QByteArray *textureData,
    const QSize *size,
    const QByteArray *format,
    quint8 flags,
    const QByteArray *name) {
  return new QSSGSceneDesc::TextureData(
      *textureData,
      *size,
      *format,
      flags,
      *name);
}

//  QSSGSceneDesc::TextureData::~TextureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc11TextureDataD1Ev(
    QSSGSceneDesc::TextureData *self) {
  delete self;
}
