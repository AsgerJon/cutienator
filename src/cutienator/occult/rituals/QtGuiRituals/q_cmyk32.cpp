//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcmyk_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcmyk_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>

//  QCmyk32::QCmyk32()
extern "C" Q_DECL_EXPORT
QCmyk32 *ritual_ZN7QCmyk32C1Ev() {
  return new QCmyk32();
}

//  QCmyk32::QCmyk32(int cyan, int magenta, int yellow, int black)
extern "C" Q_DECL_EXPORT
QCmyk32 *ritual_ZN7QCmyk32C1Eiiii(
    int cyan,
    int magenta,
    int yellow,
    int black) {
  return new QCmyk32(cyan, magenta, yellow, black);
}

#if !(Q_BYTE_ORDER == Q_BIG_ENDIAN)
//  int QCmyk32::cyan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCmyk324cyanEv(const QCmyk32 *self) {
  return self->cyan();
}
#endif  // !(Q_BYTE_ORDER == Q_BIG_ENDIAN)

#if !(Q_BYTE_ORDER == Q_BIG_ENDIAN)
//  int QCmyk32::magenta() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCmyk327magentaEv(const QCmyk32 *self) {
  return self->magenta();
}
#endif  // !(Q_BYTE_ORDER == Q_BIG_ENDIAN)

#if !(Q_BYTE_ORDER == Q_BIG_ENDIAN)
//  int QCmyk32::yellow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCmyk326yellowEv(const QCmyk32 *self) {
  return self->yellow();
}
#endif  // !(Q_BYTE_ORDER == Q_BIG_ENDIAN)

#if !(Q_BYTE_ORDER == Q_BIG_ENDIAN)
//  int QCmyk32::black() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QCmyk325blackEv(const QCmyk32 *self) {
  return self->black();
}
#endif  // !(Q_BYTE_ORDER == Q_BIG_ENDIAN)

//  QColor QCmyk32::toColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QCmyk327toColorEv(const QCmyk32 *self) {
  return new QColor(self->toColor());
}

//  uint QCmyk32::toUint() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QCmyk326toUintEv(const QCmyk32 *self) {
  return self->toUint();
}

//  QCmyk32 QCmyk32::fromCmyk32(uint cmyk)
extern "C" Q_DECL_EXPORT
QCmyk32 *ritual_ZN7QCmyk3210fromCmyk32Ej(uint cmyk) {
  return new QCmyk32(QCmyk32::fromCmyk32(cmyk));
}

//  QCmyk32 QCmyk32::fromRgba(QRgb rgba)
extern "C" Q_DECL_EXPORT
QCmyk32 *ritual_ZN7QCmyk328fromRgbaEj(QRgb rgba) {
  return new QCmyk32(QCmyk32::fromRgba(rgba));
}

//  QCmyk32 QCmyk32::fromColor(const QColor &color)
extern "C" Q_DECL_EXPORT
QCmyk32 *ritual_ZN7QCmyk329fromColorERK6QColor(const QColor *color) {
  return new QCmyk32(QCmyk32::fromColor(*color));
}

//  bool operator==(const QCmyk32 &lhs, const QCmyk32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QCmyk32S1_(const QCmyk32 *lhs, const QCmyk32 *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCmyk32 &lhs, const QCmyk32 &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QCmyk32S1_(const QCmyk32 *lhs, const QCmyk32 *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QCmyk32::~QCmyk32()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCmyk32D1Ev(QCmyk32 *self) {
  delete self;
}
