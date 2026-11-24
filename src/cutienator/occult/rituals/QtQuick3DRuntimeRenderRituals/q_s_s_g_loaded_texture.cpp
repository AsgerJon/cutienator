//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderloadedtexture_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderloadedtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGLoadedTexture::~QSSGLoadedTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGLoadedTextureD1Ev(QSSGLoadedTexture *self) {
  delete self;
}

//  void QSSGLoadedTexture::setFormatFromComponents()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGLoadedTexture23setFormatFromComponentsEv(
    QSSGLoadedTexture *self) {
  self->setFormatFromComponents();
}

//  bool QSSGLoadedTexture::scanForTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSSGLoadedTexture19scanForTransparencyEv(
    const QSSGLoadedTexture *self) {
  return self->scanForTransparency();
}

//  QSSGLoadedTexture *QSSGLoadedTexture::load(const QString &inPath, const
//      QSSGRenderTextureFormat &inFormat, bool inFlipY)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN17QSSGLoadedTexture4loadERK7QStringRK23QSSGRenderTextureFormatb(
    const QString *inPath,
    const QSSGRenderTextureFormat *inFormat,
    bool inFlipY) {
  return QSSGLoadedTexture::load(*inPath, *inFormat, inFlipY);
}

//  QSSGLoadedTexture *QSSGLoadedTexture::loadQImage(const QString &inPath,
//      qint32 flipVertical)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN17QSSGLoadedTexture10loadQImageERK7QStringi(
    const QString *inPath,
    qint32 flipVertical) {
  return QSSGLoadedTexture::loadQImage(*inPath, flipVertical);
}

//  QSSGLoadedTexture *QSSGLoadedTexture::loadCompressedImage(const QString
//      &inPath)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN17QSSGLoadedTexture19loadCompressedImageERK7QString(
    const QString *inPath) {
  return QSSGLoadedTexture::loadCompressedImage(*inPath);
}

//  QSSGLoadedTexture
//      *QSSGLoadedTexture::loadTextureData(QSSGRenderTextureData
//      *textureData)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN17QSSGLoadedTexture15loadTextureDataEP21QSSGRenderTextureData(
    QSSGRenderTextureData *textureData) {
  return QSSGLoadedTexture::loadTextureData(textureData);
}

//  QSSGLoadedTexture *QSSGLoadedTexture::loadLightmapImage(const QString
//      &inPath, const QSSGRenderTextureFormat &inFormat, const QString &key)
extern "C" Q_DECL_EXPORT
QSSGLoadedTexture *ritual_ZN17QSSGLoadedTexture17loadLightmapImageERK7QStringRK23QSSGRenderTextureFormatS2_(
    const QString *inPath,
    const QSSGRenderTextureFormat *inFormat,
    const QString *key) {
  return QSSGLoadedTexture::loadLightmapImage(*inPath, *inFormat, *key);
}
