//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtextureimagedata.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qtextureimagedata.h>
#include <QtGui/qimage.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>
#include <functional>

//  Qt3DRender::QTextureImageData::QTextureImageData()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageData *ritual_ZN10Qt3DRender17QTextureImageDataC1Ev() {
  return new Qt3DRender::QTextureImageData();
}

//  Qt3DRender::QTextureImageData::~QTextureImageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageDataD1Ev(
    Qt3DRender::QTextureImageData *self) {
  delete self;
}

//  QTextureImageData &Qt3DRender::QTextureImageData::operator=(const
//      QTextureImageData &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageData *ritual_ZN10Qt3DRender17QTextureImageDataaSERKS0_(
    Qt3DRender::QTextureImageData *self,
    const Qt3DRender::QTextureImageData *other) {
  return &(self->operator=(*other));
}

//  void Qt3DRender::QTextureImageData::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData7cleanupEv(
    Qt3DRender::QTextureImageData *self) {
  self->cleanup();
}

//  bool Qt3DRender::QTextureImageData::isCompressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17QTextureImageData12isCompressedEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->isCompressed();
}

//  int Qt3DRender::QTextureImageData::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData5widthEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->width();
}

//  int Qt3DRender::QTextureImageData::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData6heightEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->height();
}

//  int Qt3DRender::QTextureImageData::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData5depthEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->depth();
}

//  int Qt3DRender::QTextureImageData::layers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData6layersEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->layers();
}

//  int Qt3DRender::QTextureImageData::mipLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData9mipLevelsEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->mipLevels();
}

//  int Qt3DRender::QTextureImageData::faces() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData5facesEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->faces();
}

//  void Qt3DRender::QTextureImageData::setWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData8setWidthEi(
    Qt3DRender::QTextureImageData *self,
    int width) {
  self->setWidth(width);
}

//  void Qt3DRender::QTextureImageData::setHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData9setHeightEi(
    Qt3DRender::QTextureImageData *self,
    int height) {
  self->setHeight(height);
}

//  void Qt3DRender::QTextureImageData::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData8setDepthEi(
    Qt3DRender::QTextureImageData *self,
    int depth) {
  self->setDepth(depth);
}

//  void Qt3DRender::QTextureImageData::setLayers(int layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData9setLayersEi(
    Qt3DRender::QTextureImageData *self,
    int layers) {
  self->setLayers(layers);
}

//  void Qt3DRender::QTextureImageData::setMipLevels(int mipLevels)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData12setMipLevelsEi(
    Qt3DRender::QTextureImageData *self,
    int mipLevels) {
  self->setMipLevels(mipLevels);
}

//  void Qt3DRender::QTextureImageData::setFaces(int faces)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData8setFacesEi(
    Qt3DRender::QTextureImageData *self,
    int faces) {
  self->setFaces(faces);
}

//  int Qt3DRender::QTextureImageData::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender17QTextureImageData9alignmentEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->alignment();
}

//  void Qt3DRender::QTextureImageData::setAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData12setAlignmentEi(
    Qt3DRender::QTextureImageData *self,
    int alignment) {
  self->setAlignment(alignment);
}

//  QOpenGLTexture::Target Qt3DRender::QTextureImageData::target() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::Target ritual_ZNK10Qt3DRender17QTextureImageData6targetEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->target();
}

//  QOpenGLTexture::TextureFormat Qt3DRender::QTextureImageData::format()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::TextureFormat ritual_ZNK10Qt3DRender17QTextureImageData6formatEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->format();
}

//  QOpenGLTexture::PixelFormat Qt3DRender::QTextureImageData::pixelFormat()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::PixelFormat ritual_ZNK10Qt3DRender17QTextureImageData11pixelFormatEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->pixelFormat();
}

//  QOpenGLTexture::PixelType Qt3DRender::QTextureImageData::pixelType()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::PixelType ritual_ZNK10Qt3DRender17QTextureImageData9pixelTypeEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->pixelType();
}

//  void Qt3DRender::QTextureImageData::setTarget(QOpenGLTexture::Target
//      target)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData9setTargetEN14QOpenGLTexture6TargetE(
    Qt3DRender::QTextureImageData *self,
    QOpenGLTexture::Target target) {
  self->setTarget(target);
}

//  void
//      Qt3DRender::QTextureImageData::setFormat(QOpenGLTexture::TextureForma
//      t format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData9setFormatEN14QOpenGLTexture13TextureFormatE(
    Qt3DRender::QTextureImageData *self,
    QOpenGLTexture::TextureFormat format) {
  self->setFormat(format);
}

//  void
//      Qt3DRender::QTextureImageData::setPixelFormat(QOpenGLTexture::PixelFo
//      rmat pixelFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData14setPixelFormatEN14QOpenGLTexture11PixelFormatE(
    Qt3DRender::QTextureImageData *self,
    QOpenGLTexture::PixelFormat pixelFormat) {
  self->setPixelFormat(pixelFormat);
}

//  void
//      Qt3DRender::QTextureImageData::setPixelType(QOpenGLTexture::PixelType
//      pixelType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData12setPixelTypeEN14QOpenGLTexture9PixelTypeE(
    Qt3DRender::QTextureImageData *self,
    QOpenGLTexture::PixelType pixelType) {
  self->setPixelType(pixelType);
}

//  void Qt3DRender::QTextureImageData::setImage(const QImage &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData8setImageERK6QImage(
    Qt3DRender::QTextureImageData *self,
    const QImage *a0) {
  self->setImage(*a0);
}

//  void Qt3DRender::QTextureImageData::setData(const QByteArray &data, int
//      blockSize, bool isCompressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData7setDataERK10QByteArrayib(
    Qt3DRender::QTextureImageData *self,
    const QByteArray *data,
    int blockSize,
    bool isCompressed) {
  self->setData(*data, blockSize, isCompressed);
}

//  void Qt3DRender::QTextureImageData::setData(const QByteArray &data,
//      std::function<QByteArray (QByteArray, int, int, int)> a1, bool
//      isCompressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureImageData7setDataERK10QByteArraySt8functionIFS1_S1_iiiEEb(
    Qt3DRender::QTextureImageData *self,
    const QByteArray *data,
    const std::function<QByteArray (QByteArray, int, int, int)> *a1,
    bool isCompressed) {
  self->setData(*data, *a1, isCompressed);
}

//  QByteArray Qt3DRender::QTextureImageData::data(int layer, int face, int
//      mipmapLevel) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender17QTextureImageData4dataEiii(
    const Qt3DRender::QTextureImageData *self,
    int layer,
    int face,
    int mipmapLevel) {
  return new QByteArray(self->data(layer, face, mipmapLevel));
}

//  Qt3DRender::QTextureImageData::QTextureImageData(QTextureImageDataPrivate
//      &dd)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageData *ritual_ZN10Qt3DRender17QTextureImageDataC1ERNS_24QTextureImageDataPrivateE(
    Qt3DRender::QTextureImageDataPrivate *dd) {
  return new Qt3DRender::QTextureImageData(*dd);
}

//  QTextureImageDataPrivate *Qt3DRender::QTextureImageData::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataPrivate *ritual_ZN10Qt3DRender17QTextureImageData6d_funcEv(
    Qt3DRender::QTextureImageData *self) {
  return self->d_func();
}

//  const QTextureImageDataPrivate *Qt3DRender::QTextureImageData::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureImageDataPrivate *ritual_ZNK10Qt3DRender17QTextureImageData6d_funcEv(
    const Qt3DRender::QTextureImageData *self) {
  return self->d_func();
}
