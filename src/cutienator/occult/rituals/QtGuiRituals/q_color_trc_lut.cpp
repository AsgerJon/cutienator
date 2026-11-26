//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortrclut_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortrclut_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortrc_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransferfunction_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransfertable_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransfergeneric_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrgba64.h>
#include <memory>

//  std::shared_ptr<QColorTrcLut> QColorTrcLut::fromGamma(float gamma,
//      Direction dir)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QColorTrcLut> *ritual_ZN12QColorTrcLut9fromGammaEfNS_9DirectionE(
    float gamma,
    QColorTrcLut::Direction dir) {
  return new std::shared_ptr<QColorTrcLut>(
      QColorTrcLut::fromGamma(
          gamma,
          dir));
}

//  std::shared_ptr<QColorTrcLut> QColorTrcLut::fromTrc(const QColorTrc &trc,
//      Direction dir)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QColorTrcLut> *ritual_ZN12QColorTrcLut7fromTrcERK9QColorTrcNS_9DirectionE(
    const QColorTrc *trc,
    QColorTrcLut::Direction dir) {
  return new std::shared_ptr<QColorTrcLut>(QColorTrcLut::fromTrc(*trc, dir));
}

//  void QColorTrcLut::setFromGamma(float gamma, Direction dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorTrcLut12setFromGammaEfNS_9DirectionE(
    QColorTrcLut *self,
    float gamma,
    QColorTrcLut::Direction dir) {
  self->setFromGamma(gamma, dir);
}

//  void QColorTrcLut::setFromTransferFunction(const QColorTransferFunction
//      &transFn, Direction dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorTrcLut23setFromTransferFunctionERK22QColorTransferFunctionNS_9DirectionE(
    QColorTrcLut *self,
    const QColorTransferFunction *transFn,
    QColorTrcLut::Direction dir) {
  self->setFromTransferFunction(*transFn, dir);
}

//  void QColorTrcLut::setFromTransferTable(const QColorTransferTable
//      &transTable, Direction dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorTrcLut20setFromTransferTableERK19QColorTransferTableNS_9DirectionE(
    QColorTrcLut *self,
    const QColorTransferTable *transTable,
    QColorTrcLut::Direction dir) {
  self->setFromTransferTable(*transTable, dir);
}

//  void QColorTrcLut::setFromTransferGenericFunction(const
//      QColorTransferGenericFunction &transfn, Direction dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorTrcLut30setFromTransferGenericFunctionERK29QColorTransferGenericFunctionNS_9DirectionE(
    QColorTrcLut *self,
    const QColorTransferGenericFunction *transfn,
    QColorTrcLut::Direction dir) {
  self->setFromTransferGenericFunction(*transfn, dir);
}

//  void QColorTrcLut::setFromTrc(const QColorTrc &trc, Direction dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorTrcLut10setFromTrcERK9QColorTrcNS_9DirectionE(
    QColorTrcLut *self,
    const QColorTrc *trc,
    QColorTrcLut::Direction dir) {
  self->setFromTrc(*trc, dir);
}

//  QRgba64 QColorTrcLut::toLinear64(QRgb rgb32) const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK12QColorTrcLut10toLinear64Ej(
    const QColorTrcLut *self,
    QRgb rgb32) {
  return new QRgba64(self->toLinear64(rgb32));
}

//  QRgb QColorTrcLut::toLinear(QRgb rgb32) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK12QColorTrcLut8toLinearEj(
    const QColorTrcLut *self,
    QRgb rgb32) {
  return self->toLinear(rgb32);
}

//  QRgba64 QColorTrcLut::toLinear(QRgba64 rgb64) const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK12QColorTrcLut8toLinearE7QRgba64(
    const QColorTrcLut *self,
    const QRgba64 *rgb64) {
  return new QRgba64(self->toLinear(*rgb64));
}

//  float QColorTrcLut::u8ToLinearF32(int c) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QColorTrcLut13u8ToLinearF32Ei(
    const QColorTrcLut *self,
    int c) {
  return self->u8ToLinearF32(c);
}

//  float QColorTrcLut::u16ToLinearF32(int c) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QColorTrcLut14u16ToLinearF32Ei(
    const QColorTrcLut *self,
    int c) {
  return self->u16ToLinearF32(c);
}

//  float QColorTrcLut::toLinear(float f) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QColorTrcLut8toLinearEf(
    const QColorTrcLut *self,
    float f) {
  return self->toLinear(f);
}

//  QRgb QColorTrcLut::fromLinear64(QRgba64 rgb64) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK12QColorTrcLut12fromLinear64E7QRgba64(
    const QColorTrcLut *self,
    const QRgba64 *rgb64) {
  return self->fromLinear64(*rgb64);
}

//  QRgb QColorTrcLut::fromLinear(QRgb rgb32) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK12QColorTrcLut10fromLinearEj(
    const QColorTrcLut *self,
    QRgb rgb32) {
  return self->fromLinear(rgb32);
}

//  QRgba64 QColorTrcLut::fromLinear(QRgba64 rgb64) const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK12QColorTrcLut10fromLinearE7QRgba64(
    const QColorTrcLut *self,
    const QRgba64 *rgb64) {
  return new QRgba64(self->fromLinear(*rgb64));
}

//  int QColorTrcLut::u8FromLinearF32(float f) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QColorTrcLut15u8FromLinearF32Ef(
    const QColorTrcLut *self,
    float f) {
  return self->u8FromLinearF32(f);
}

//  int QColorTrcLut::u16FromLinearF32(float f) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QColorTrcLut16u16FromLinearF32Ef(
    const QColorTrcLut *self,
    float f) {
  return self->u16FromLinearF32(f);
}

//  float QColorTrcLut::fromLinear(float f) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QColorTrcLut10fromLinearEf(
    const QColorTrcLut *self,
    float f) {
  return self->fromLinear(f);
}

//  QColorTrcLut::QColorTrcLut()
extern "C" Q_DECL_EXPORT
QColorTrcLut *ritual_ZN12QColorTrcLutC1Ev() {
  return new QColorTrcLut();
}

//  std::shared_ptr<QColorTrcLut> QColorTrcLut::create()
extern "C" Q_DECL_EXPORT
std::shared_ptr<QColorTrcLut> *ritual_ZN12QColorTrcLut6createEv() {
  return new std::shared_ptr<QColorTrcLut>(QColorTrcLut::create());
}

//  QRgb QColorTrcLut::convertWithTable(QRgb rgb32, const ushort *table)
extern "C" Q_DECL_EXPORT
QRgb ritual_ZN12QColorTrcLut16convertWithTableEjPKt(
    QRgb rgb32,
    const ushort *table) {
  return QColorTrcLut::convertWithTable(rgb32, table);
}

//  QRgba64 QColorTrcLut::convertWithTable(QRgba64 rgb64, const ushort
//      *table)
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZN12QColorTrcLut16convertWithTableE7QRgba64PKt(
    const QRgba64 *rgb64,
    const ushort *table) {
  return new QRgba64(QColorTrcLut::convertWithTable(*rgb64, table));
}

//  a std::shared_ptr<QColorTrcLut> a ritual of QColorTrcLut gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QColorTrcLut__std_shared_ptr_QColorTrcLut(
    std::shared_ptr<QColorTrcLut> *self) {
  delete self;
}
