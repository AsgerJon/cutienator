//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtextureimagedata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtextureimagedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>
#include <functional>

//  Qt3DRender::QTextureImageDataPrivate::QTextureImageDataPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataPrivate *ritual_ZN10Qt3DRender24QTextureImageDataPrivateC1Ev() {
  return new Qt3DRender::QTextureImageDataPrivate();
}

//  void Qt3DRender::QTextureImageDataPrivate::setData(const QByteArray
//      &data, int blockSize, bool isCompressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender24QTextureImageDataPrivate7setDataERK10QByteArrayib(
    Qt3DRender::QTextureImageDataPrivate *self,
    const QByteArray *data,
    int blockSize,
    bool isCompressed) {
  self->setData(*data, blockSize, isCompressed);
}

//  void Qt3DRender::QTextureImageDataPrivate::setData(const QByteArray
//      &data, std::function<QByteArray (QByteArray, int, int, int)>
//      dataExtractor, bool isCompressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender24QTextureImageDataPrivate7setDataERK10QByteArraySt8functionIFS1_S1_iiiEEb(
    Qt3DRender::QTextureImageDataPrivate *self,
    const QByteArray *data,
    const std::function<QByteArray (QByteArray, int, int, int)> *dataExtractor,
    bool isCompressed) {
  self->setData(*data, *dataExtractor, isCompressed);
}

//  QByteArray Qt3DRender::QTextureImageDataPrivate::data(int layer, int
//      face, int mipmapLevel) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender24QTextureImageDataPrivate4dataEiii(
    const Qt3DRender::QTextureImageDataPrivate *self,
    int layer,
    int face,
    int mipmapLevel) {
  return new QByteArray(self->data(layer, face, mipmapLevel));
}

//  QTextureImageDataPrivate
//      *Qt3DRender::QTextureImageDataPrivate::get(QTextureImageData
//      *imageData)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataPrivate *ritual_ZN10Qt3DRender24QTextureImageDataPrivate3getEPNS_17QTextureImageDataE(
    Qt3DRender::QTextureImageData *imageData) {
  return Qt3DRender::QTextureImageDataPrivate::get(imageData);
}

//  int Qt3DRender::QTextureImageDataPrivate::ddsLayerSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender24QTextureImageDataPrivate12ddsLayerSizeEv(
    const Qt3DRender::QTextureImageDataPrivate *self) {
  return self->ddsLayerSize();
}

//  int Qt3DRender::QTextureImageDataPrivate::ddsFaceSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender24QTextureImageDataPrivate11ddsFaceSizeEv(
    const Qt3DRender::QTextureImageDataPrivate *self) {
  return self->ddsFaceSize();
}

//  int Qt3DRender::QTextureImageDataPrivate::mipmapLevelSize(int level)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender24QTextureImageDataPrivate15mipmapLevelSizeEi(
    const Qt3DRender::QTextureImageDataPrivate *self,
    int level) {
  return self->mipmapLevelSize(level);
}

//  QByteArray Qt3DRender::QTextureImageDataPrivate::ktxData(int layer, int
//      face, int mipmapLevel) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender24QTextureImageDataPrivate7ktxDataEiii(
    const Qt3DRender::QTextureImageDataPrivate *self,
    int layer,
    int face,
    int mipmapLevel) {
  return new QByteArray(self->ktxData(layer, face, mipmapLevel));
}

//  Qt3DRender::QTextureImageDataPrivate::~QTextureImageDataPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender24QTextureImageDataPrivateD1Ev(
    Qt3DRender::QTextureImageDataPrivate *self) {
  delete self;
}
