//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortransferfunction_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortransferfunction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorTransferFunction::QColorTransferFunction()
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunctionC1Ev() {
  return new QColorTransferFunction();
}

//  QColorTransferFunction::QColorTransferFunction(float a, float b, float c,
//      float d, float e, float f, float g)
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunctionC1Efffffff(
    float a,
    float b,
    float c,
    float d,
    float e,
    float f,
    float g) {
  return new QColorTransferFunction(a, b, c, d, e, f, g);
}

//  bool QColorTransferFunction::isGamma() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QColorTransferFunction7isGammaEv(
    const QColorTransferFunction *self) {
  return self->isGamma();
}

//  bool QColorTransferFunction::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QColorTransferFunction10isIdentityEv(
    const QColorTransferFunction *self) {
  return self->isIdentity();
}

//  bool QColorTransferFunction::isSRgb() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QColorTransferFunction6isSRgbEv(
    const QColorTransferFunction *self) {
  return self->isSRgb();
}

//  float QColorTransferFunction::apply(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QColorTransferFunction5applyEf(
    const QColorTransferFunction *self,
    float x) {
  return self->apply(x);
}

//  QColorTransferFunction QColorTransferFunction::inverted() const
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZNK22QColorTransferFunction8invertedEv(
    const QColorTransferFunction *self) {
  return new QColorTransferFunction(self->inverted());
}

//  QColorTransferFunction QColorTransferFunction::fromGamma(float gamma)
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunction9fromGammaEf(
    float gamma) {
  return new QColorTransferFunction(
      QColorTransferFunction::fromGamma(
          gamma));
}

//  QColorTransferFunction QColorTransferFunction::fromSRgb()
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunction8fromSRgbEv() {
  return new QColorTransferFunction(QColorTransferFunction::fromSRgb());
}

//  QColorTransferFunction QColorTransferFunction::fromProPhotoRgb()
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunction15fromProPhotoRgbEv() {
  return new QColorTransferFunction(
      QColorTransferFunction::fromProPhotoRgb());
}

//  QColorTransferFunction QColorTransferFunction::fromBt2020()
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunction10fromBt2020Ev() {
  return new QColorTransferFunction(QColorTransferFunction::fromBt2020());
}

//  bool QColorTransferFunction::matches(const QColorTransferFunction &o)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QColorTransferFunction7matchesERKS_(
    const QColorTransferFunction *self,
    const QColorTransferFunction *o) {
  return self->matches(*o);
}

//  bool operator==(const QColorTransferFunction &f1, const
//      QColorTransferFunction &f2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK22QColorTransferFunctionS1_(
    const QColorTransferFunction *f1,
    const QColorTransferFunction *f2) {
  return operator==(*f1, *f2);
}

//  bool operator!=(const QColorTransferFunction &f1, const
//      QColorTransferFunction &f2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK22QColorTransferFunctionS1_(
    const QColorTransferFunction *f1,
    const QColorTransferFunction *f2) {
  return operator!=(*f1, *f2);
}

//  QColorTransferFunction::QColorTransferFunction(float a, float b, float c,
//      float d, float e, float f, float g, Hints flags)
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZN22QColorTransferFunctionC1Efffffff6QFlagsINS_4HintEE(
    float a,
    float b,
    float c,
    float d,
    float e,
    float f,
    float g,
    int flags) {
  return new QColorTransferFunction(
      a,
      b,
      c,
      d,
      e,
      f,
      g,
      QFlags<QColorTransferFunction::Hint>::fromInt(flags));
}

//  bool QColorTransferFunction::paramCompare(float p1, float p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QColorTransferFunction12paramCompareEff(float p1, float p2) {
  return QColorTransferFunction::paramCompare(p1, p2);
}

//  void QColorTransferFunction::updateHints() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QColorTransferFunction11updateHintsEv(
    const QColorTransferFunction *self) {
  self->updateHints();
}

//  QColorTransferFunction::~QColorTransferFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QColorTransferFunctionD1Ev(QColorTransferFunction *self) {
  delete self;
}
