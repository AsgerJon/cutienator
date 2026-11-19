//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qrgba64.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qrgba64.h>

//  QRgba64::QRgba64()
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN7QRgba64C1Ev() {
  return new QRgba64();
}

//  QRgba64 QRgba64::fromRgba64(quint64 c)
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN7QRgba6410fromRgba64Ey(quint64 c) {
  return new QRgba64(QRgba64::fromRgba64(c));
}

//  QRgba64 QRgba64::fromRgba64(quint16 red, quint16 green, quint16 blue,
//      quint16 alpha)
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN7QRgba6410fromRgba64Etttt(
    quint16 red,
    quint16 green,
    quint16 blue,
    quint16 alpha) {
  return new QRgba64(QRgba64::fromRgba64(red, green, blue, alpha));
}

//  QRgba64 QRgba64::fromRgba(quint8 red, quint8 green, quint8 blue, quint8
//      alpha)
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN7QRgba648fromRgbaEhhhh(
    quint8 red,
    quint8 green,
    quint8 blue,
    quint8 alpha) {
  return new QRgba64(QRgba64::fromRgba(red, green, blue, alpha));
}

//  QRgba64 QRgba64::fromArgb32(uint rgb)
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN7QRgba6410fromArgb32Ej(uint rgb) {
  return new QRgba64(QRgba64::fromArgb32(rgb));
}

//  bool QRgba64::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRgba648isOpaqueEv(const QRgba64 *self) {
  return self->isOpaque();
}

//  bool QRgba64::isTransparent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRgba6413isTransparentEv(const QRgba64 *self) {
  return self->isTransparent();
}

//  quint16 QRgba64::red() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK7QRgba643redEv(const QRgba64 *self) {
  return self->red();
}

//  quint16 QRgba64::green() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK7QRgba645greenEv(const QRgba64 *self) {
  return self->green();
}

//  quint16 QRgba64::blue() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK7QRgba644blueEv(const QRgba64 *self) {
  return self->blue();
}

//  quint16 QRgba64::alpha() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK7QRgba645alphaEv(const QRgba64 *self) {
  return self->alpha();
}

//  void QRgba64::setRed(quint16 _red)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRgba646setRedEt(QRgba64 *self, quint16 _red) {
  self->setRed(_red);
}

//  void QRgba64::setGreen(quint16 _green)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRgba648setGreenEt(QRgba64 *self, quint16 _green) {
  self->setGreen(_green);
}

//  void QRgba64::setBlue(quint16 _blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRgba647setBlueEt(QRgba64 *self, quint16 _blue) {
  self->setBlue(_blue);
}

//  void QRgba64::setAlpha(quint16 _alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRgba648setAlphaEt(QRgba64 *self, quint16 _alpha) {
  self->setAlpha(_alpha);
}

//  quint8 QRgba64::red8() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK7QRgba644red8Ev(const QRgba64 *self) {
  return self->red8();
}

//  quint8 QRgba64::green8() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK7QRgba646green8Ev(const QRgba64 *self) {
  return self->green8();
}

//  quint8 QRgba64::blue8() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK7QRgba645blue8Ev(const QRgba64 *self) {
  return self->blue8();
}

//  quint8 QRgba64::alpha8() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK7QRgba646alpha8Ev(const QRgba64 *self) {
  return self->alpha8();
}

//  uint QRgba64::toArgb32() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QRgba648toArgb32Ev(const QRgba64 *self) {
  return self->toArgb32();
}

//  ushort QRgba64::toRgb16() const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK7QRgba647toRgb16Ev(const QRgba64 *self) {
  return self->toRgb16();
}

//  QRgba64 QRgba64::premultiplied() const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK7QRgba6413premultipliedEv(const QRgba64 *self) {
  return new QRgba64(self->premultiplied());
}

//  QRgba64 QRgba64::unpremultiplied() const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK7QRgba6415unpremultipliedEv(const QRgba64 *self) {
  return new QRgba64(self->unpremultiplied());
}

//  quint64 QRgba64::operator unsigned long long() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK7QRgba64cvyEv(const QRgba64 *self) {
  return self->operator quint64();
}

//  QRgba64::~QRgba64()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRgba64D1Ev(QRgba64 *self) {
  delete self;
}
