//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideotexturehelper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideotexturehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  int QVideoTextureHelper::TextureDescription::strideForWidth(int width)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QVideoTextureHelper18TextureDescription14strideForWidthEi(
    const QVideoTextureHelper::TextureDescription *self,
    int width) {
  return self->strideForWidth(width);
}

//  int QVideoTextureHelper::TextureDescription::bytesForSize(QSize s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QVideoTextureHelper18TextureDescription12bytesForSizeE5QSize(
    const QVideoTextureHelper::TextureDescription *self,
    const QSize *s) {
  return self->bytesForSize(*s);
}

//  int QVideoTextureHelper::TextureDescription::widthForPlane(int width, int
//      plane) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QVideoTextureHelper18TextureDescription13widthForPlaneEii(
    const QVideoTextureHelper::TextureDescription *self,
    int width,
    int plane) {
  return self->widthForPlane(width, plane);
}

//  int QVideoTextureHelper::TextureDescription::heightForPlane(int height,
//      int plane) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QVideoTextureHelper18TextureDescription14heightForPlaneEii(
    const QVideoTextureHelper::TextureDescription *self,
    int height,
    int plane) {
  return self->heightForPlane(height, plane);
}

//  SizeScale QVideoTextureHelper::TextureDescription::rhiSizeScale(int
//      plane, QRhi *rhi) const
extern "C" Q_DECL_EXPORT
QVideoTextureHelper::TextureDescription::SizeScale *ritual_ZNK19QVideoTextureHelper18TextureDescription12rhiSizeScaleEiP4QRhi(
    const QVideoTextureHelper::TextureDescription *self,
    int plane,
    QRhi *rhi) {
  return new QVideoTextureHelper::TextureDescription::SizeScale(
      self->rhiSizeScale(
          plane,
          rhi));
}

//  QSize QVideoTextureHelper::TextureDescription::rhiPlaneSize(QSize
//      frameSize, int plane, QRhi *rhi) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QVideoTextureHelper18TextureDescription12rhiPlaneSizeE5QSizeiP4QRhi(
    const QVideoTextureHelper::TextureDescription *self,
    const QSize *frameSize,
    int plane,
    QRhi *rhi) {
  return new QSize(self->rhiPlaneSize(*frameSize, plane, rhi));
}

//  bool
//      QVideoTextureHelper::TextureDescription::hasTextureFormat(TextureForm
//      at format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QVideoTextureHelper18TextureDescription16hasTextureFormatENS0_13TextureFormatE(
    const QVideoTextureHelper::TextureDescription *self,
    QVideoTextureHelper::TextureDescription::TextureFormat format) {
  return self->hasTextureFormat(format);
}

//  QVideoTextureHelper::TextureDescription::~TextureDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoTextureHelper18TextureDescriptionD1Ev(
    QVideoTextureHelper::TextureDescription *self) {
  delete self;
}
