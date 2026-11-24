//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  TextureOp QRhiResourceUpdateBatchPrivate::TextureOp::upload(QRhiTexture
//      *tex, const QRhiTextureUploadDescription &desc)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::TextureOp *ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp6uploadEP11QRhiTextureRK28QRhiTextureUploadDescription(
    QRhiTexture *tex,
    const QRhiTextureUploadDescription *desc) {
  return new QRhiResourceUpdateBatchPrivate::TextureOp(
      QRhiResourceUpdateBatchPrivate::TextureOp::upload(
          tex,
          *desc));
}

//  TextureOp QRhiResourceUpdateBatchPrivate::TextureOp::copy(QRhiTexture
//      *dst, QRhiTexture *src, const QRhiTextureCopyDescription &desc)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::TextureOp *ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp4copyEP11QRhiTextureS2_RK26QRhiTextureCopyDescription(
    QRhiTexture *dst,
    QRhiTexture *src,
    const QRhiTextureCopyDescription *desc) {
  return new QRhiResourceUpdateBatchPrivate::TextureOp(
      QRhiResourceUpdateBatchPrivate::TextureOp::copy(
          dst,
          src,
          *desc));
}

//  TextureOp QRhiResourceUpdateBatchPrivate::TextureOp::read(const
//      QRhiReadbackDescription &rb, QRhiReadbackResult *result)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::TextureOp *ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp4readERK23QRhiReadbackDescriptionP18QRhiReadbackResult(
    const QRhiReadbackDescription *rb,
    QRhiReadbackResult *result) {
  return new QRhiResourceUpdateBatchPrivate::TextureOp(
      QRhiResourceUpdateBatchPrivate::TextureOp::read(
          *rb,
          result));
}

//  TextureOp QRhiResourceUpdateBatchPrivate::TextureOp::genMips(QRhiTexture
//      *tex)
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatchPrivate::TextureOp *ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp7genMipsEP11QRhiTexture(
    QRhiTexture *tex) {
  return new QRhiResourceUpdateBatchPrivate::TextureOp(
      QRhiResourceUpdateBatchPrivate::TextureOp::genMips(
          tex));
}

//  QRhiResourceUpdateBatchPrivate::TextureOp::~TextureOp()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOpD1Ev(
    QRhiResourceUpdateBatchPrivate::TextureOp *self) {
  delete self;
}
