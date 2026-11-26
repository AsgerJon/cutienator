//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtexturedataupdate.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qtexturedataupdate.h>
#include <Qt3DRender/Qt3DRender>

//  Qt3DRender::QTextureDataUpdate::QTextureDataUpdate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataUpdate *ritual_ZN10Qt3DRender18QTextureDataUpdateC1Ev() {
  return new Qt3DRender::QTextureDataUpdate();
}

//  Qt3DRender::QTextureDataUpdate::QTextureDataUpdate(const
//      QTextureDataUpdate &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataUpdate *ritual_ZN10Qt3DRender18QTextureDataUpdateC1ERKS0_(
    const Qt3DRender::QTextureDataUpdate *other) {
  return new Qt3DRender::QTextureDataUpdate(*other);
}

//  QTextureDataUpdate &Qt3DRender::QTextureDataUpdate::operator=(const
//      QTextureDataUpdate &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataUpdate *ritual_ZN10Qt3DRender18QTextureDataUpdateaSERKS0_(
    Qt3DRender::QTextureDataUpdate *self,
    const Qt3DRender::QTextureDataUpdate *other) {
  return &(self->operator=(*other));
}

//  QTextureDataUpdate
//      &Qt3DRender::QTextureDataUpdate::operator=(QTextureDataUpdate
//      &&other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataUpdate *ritual_ZN10Qt3DRender18QTextureDataUpdateaSEOS0_(
    Qt3DRender::QTextureDataUpdate *self,
    Qt3DRender::QTextureDataUpdate *other) {
  return &(self->operator=(std::move(*other)));
}

//  Qt3DRender::QTextureDataUpdate::~QTextureDataUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdateD1Ev(
    Qt3DRender::QTextureDataUpdate *self) {
  delete self;
}

//  void Qt3DRender::QTextureDataUpdate::swap(QTextureDataUpdate &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate4swapERS0_(
    Qt3DRender::QTextureDataUpdate *self,
    Qt3DRender::QTextureDataUpdate *other) {
  self->swap(*other);
}

//  int Qt3DRender::QTextureDataUpdate::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QTextureDataUpdate1xEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->x();
}

//  int Qt3DRender::QTextureDataUpdate::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QTextureDataUpdate1yEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->y();
}

//  int Qt3DRender::QTextureDataUpdate::z() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QTextureDataUpdate1zEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->z();
}

//  int Qt3DRender::QTextureDataUpdate::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QTextureDataUpdate5layerEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->layer();
}

//  int Qt3DRender::QTextureDataUpdate::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender18QTextureDataUpdate8mipLevelEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->mipLevel();
}

//  QAbstractTexture::CubeMapFace Qt3DRender::QTextureDataUpdate::face()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::CubeMapFace ritual_ZNK10Qt3DRender18QTextureDataUpdate4faceEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->face();
}

//  QTextureImageDataPtr Qt3DRender::QTextureDataUpdate::data() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataPtr *ritual_ZNK10Qt3DRender18QTextureDataUpdate4dataEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return new Qt3DRender::QTextureImageDataPtr(self->data());
}

//  void Qt3DRender::QTextureDataUpdate::setX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate4setXEi(
    Qt3DRender::QTextureDataUpdate *self,
    int x) {
  self->setX(x);
}

//  void Qt3DRender::QTextureDataUpdate::setY(int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate4setYEi(
    Qt3DRender::QTextureDataUpdate *self,
    int y) {
  self->setY(y);
}

//  void Qt3DRender::QTextureDataUpdate::setZ(int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate4setZEi(
    Qt3DRender::QTextureDataUpdate *self,
    int z) {
  self->setZ(z);
}

//  void Qt3DRender::QTextureDataUpdate::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate8setLayerEi(
    Qt3DRender::QTextureDataUpdate *self,
    int layer) {
  self->setLayer(layer);
}

//  void Qt3DRender::QTextureDataUpdate::setMipLevel(int mipLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate11setMipLevelEi(
    Qt3DRender::QTextureDataUpdate *self,
    int mipLevel) {
  self->setMipLevel(mipLevel);
}

//  void
//      Qt3DRender::QTextureDataUpdate::setFace(QAbstractTexture::CubeMapFace
//      face)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate7setFaceENS_16QAbstractTexture11CubeMapFaceE(
    Qt3DRender::QTextureDataUpdate *self,
    Qt3DRender::QAbstractTexture::CubeMapFace face) {
  self->setFace(face);
}

//  void Qt3DRender::QTextureDataUpdate::setData(const QTextureImageDataPtr
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QTextureDataUpdate7setDataERK14QSharedPointerINS_17QTextureImageDataEE(
    Qt3DRender::QTextureDataUpdate *self,
    const Qt3DRender::QTextureImageDataPtr *data) {
  self->setData(*data);
}

//  bool operator==(const QTextureDataUpdate &lhs, const QTextureDataUpdate
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRendereqERKNS_18QTextureDataUpdateES2_(
    const Qt3DRender::QTextureDataUpdate *lhs,
    const Qt3DRender::QTextureDataUpdate *rhs) {
  return operator==(*lhs, *rhs);
}

//  QTextureDataUpdatePrivate *Qt3DRender::QTextureDataUpdate::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataUpdatePrivate *ritual_ZN10Qt3DRender18QTextureDataUpdate6d_funcEv(
    Qt3DRender::QTextureDataUpdate *self) {
  return self->d_func();
}

//  const QTextureDataUpdatePrivate *Qt3DRender::QTextureDataUpdate::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureDataUpdatePrivate *ritual_ZNK10Qt3DRender18QTextureDataUpdate6d_funcEv(
    const Qt3DRender::QTextureDataUpdate *self) {
  return self->d_func();
}

//  a Qt3DRender::QTextureImageDataPtr a ritual of
//      Qt3DRender::QTextureDataUpdate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QTextureDataUpdate__Qt3DRender_QTextureImageDataPtr(
    Qt3DRender::QTextureImageDataPtr *self) {
  delete self;
}
