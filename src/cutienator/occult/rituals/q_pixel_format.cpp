//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpixelformat.h>

//  QPixelFormat::QPixelFormat()
extern "C" Q_DECL_EXPORT
QPixelFormat *ritual_ZN12QPixelFormatC1Ev() {
  return new QPixelFormat();
}

//  QPixelFormat::QPixelFormat(ColorModel colorModel, uchar firstSize, uchar
//      secondSize, uchar thirdSize, uchar fourthSize, uchar fifthSize, uchar
//      alphaSize, AlphaUsage alphaUsage, AlphaPosition alphaPosition,
//      AlphaPremultiplied premultiplied, TypeInterpretation
//      typeInterpretation, ByteOrder byteOrder, uchar subEnum)
extern "C" Q_DECL_EXPORT
QPixelFormat *ritual_ZN12QPixelFormatC1ENS_10ColorModelEhhhhhhNS_10AlphaUsageENS_13AlphaPositionENS_18AlphaPremultipliedENS_18TypeInterpretationENS_9ByteOrderEh(
    QPixelFormat::ColorModel colorModel,
    uchar firstSize,
    uchar secondSize,
    uchar thirdSize,
    uchar fourthSize,
    uchar fifthSize,
    uchar alphaSize,
    QPixelFormat::AlphaUsage alphaUsage,
    QPixelFormat::AlphaPosition alphaPosition,
    QPixelFormat::AlphaPremultiplied premultiplied,
    QPixelFormat::TypeInterpretation typeInterpretation,
    QPixelFormat::ByteOrder byteOrder,
    uchar subEnum) {
  return new QPixelFormat(
      colorModel,
      firstSize,
      secondSize,
      thirdSize,
      fourthSize,
      fifthSize,
      alphaSize,
      alphaUsage,
      alphaPosition,
      premultiplied,
      typeInterpretation,
      byteOrder,
      subEnum);
}

//  ColorModel QPixelFormat::colorModel() const
extern "C" Q_DECL_EXPORT
QPixelFormat::ColorModel ritual_ZNK12QPixelFormat10colorModelEv(
    const QPixelFormat *self) {
  return self->colorModel();
}

//  uchar QPixelFormat::channelCount() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat12channelCountEv(const QPixelFormat *self) {
  return self->channelCount();
}

//  uchar QPixelFormat::redSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat7redSizeEv(const QPixelFormat *self) {
  return self->redSize();
}

//  uchar QPixelFormat::greenSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat9greenSizeEv(const QPixelFormat *self) {
  return self->greenSize();
}

//  uchar QPixelFormat::blueSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat8blueSizeEv(const QPixelFormat *self) {
  return self->blueSize();
}

//  uchar QPixelFormat::cyanSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat8cyanSizeEv(const QPixelFormat *self) {
  return self->cyanSize();
}

//  uchar QPixelFormat::magentaSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat11magentaSizeEv(const QPixelFormat *self) {
  return self->magentaSize();
}

//  uchar QPixelFormat::yellowSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat10yellowSizeEv(const QPixelFormat *self) {
  return self->yellowSize();
}

//  uchar QPixelFormat::blackSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat9blackSizeEv(const QPixelFormat *self) {
  return self->blackSize();
}

//  uchar QPixelFormat::hueSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat7hueSizeEv(const QPixelFormat *self) {
  return self->hueSize();
}

//  uchar QPixelFormat::saturationSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat14saturationSizeEv(const QPixelFormat *self) {
  return self->saturationSize();
}

//  uchar QPixelFormat::lightnessSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat13lightnessSizeEv(const QPixelFormat *self) {
  return self->lightnessSize();
}

//  uchar QPixelFormat::brightnessSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat14brightnessSizeEv(const QPixelFormat *self) {
  return self->brightnessSize();
}

//  uchar QPixelFormat::alphaSize() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat9alphaSizeEv(const QPixelFormat *self) {
  return self->alphaSize();
}

//  uchar QPixelFormat::bitsPerPixel() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat12bitsPerPixelEv(const QPixelFormat *self) {
  return self->bitsPerPixel();
}

//  AlphaUsage QPixelFormat::alphaUsage() const
extern "C" Q_DECL_EXPORT
QPixelFormat::AlphaUsage ritual_ZNK12QPixelFormat10alphaUsageEv(
    const QPixelFormat *self) {
  return self->alphaUsage();
}

//  AlphaPosition QPixelFormat::alphaPosition() const
extern "C" Q_DECL_EXPORT
QPixelFormat::AlphaPosition ritual_ZNK12QPixelFormat13alphaPositionEv(
    const QPixelFormat *self) {
  return self->alphaPosition();
}

//  AlphaPremultiplied QPixelFormat::premultiplied() const
extern "C" Q_DECL_EXPORT
QPixelFormat::AlphaPremultiplied ritual_ZNK12QPixelFormat13premultipliedEv(
    const QPixelFormat *self) {
  return self->premultiplied();
}

//  TypeInterpretation QPixelFormat::typeInterpretation() const
extern "C" Q_DECL_EXPORT
QPixelFormat::TypeInterpretation ritual_ZNK12QPixelFormat18typeInterpretationEv(
    const QPixelFormat *self) {
  return self->typeInterpretation();
}

//  ByteOrder QPixelFormat::byteOrder() const
extern "C" Q_DECL_EXPORT
QPixelFormat::ByteOrder ritual_ZNK12QPixelFormat9byteOrderEv(
    const QPixelFormat *self) {
  return self->byteOrder();
}

//  YUVLayout QPixelFormat::yuvLayout() const
extern "C" Q_DECL_EXPORT
QPixelFormat::YUVLayout ritual_ZNK12QPixelFormat9yuvLayoutEv(
    const QPixelFormat *self) {
  return self->yuvLayout();
}

//  uchar QPixelFormat::subEnum() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK12QPixelFormat7subEnumEv(const QPixelFormat *self) {
  return self->subEnum();
}

//  QPixelFormat::~QPixelFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixelFormatD1Ev(QPixelFormat *self) {
  delete self;
}
