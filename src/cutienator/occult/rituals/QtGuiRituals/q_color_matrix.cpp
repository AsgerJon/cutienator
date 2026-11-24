//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolormatrix_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolormatrix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QColorMatrix::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorMatrix6isNullEv(const QColorMatrix *self) {
  return self->isNull();
}

//  float QColorMatrix::determinant() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QColorMatrix11determinantEv(const QColorMatrix *self) {
  return self->determinant();
}

//  bool QColorMatrix::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorMatrix7isValidEv(const QColorMatrix *self) {
  return self->isValid();
}

//  bool QColorMatrix::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorMatrix10isIdentityEv(const QColorMatrix *self) {
  return self->isIdentity();
}

//  QColorMatrix QColorMatrix::inverted() const
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZNK12QColorMatrix8invertedEv(const QColorMatrix *self) {
  return new QColorMatrix(self->inverted());
}

//  QColorMatrix operator*(const QColorMatrix &a, const QColorMatrix &o)
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZmlRK12QColorMatrixS1_(
    const QColorMatrix *a,
    const QColorMatrix *o) {
  return new QColorMatrix(operator*(*a, *o));
}

//  QColorVector QColorMatrix::map(const QColorVector &c) const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorMatrix3mapERK12QColorVector(
    const QColorMatrix *self,
    const QColorVector *c) {
  return new QColorVector(self->map(*c));
}

//  QColorMatrix QColorMatrix::transposed() const
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZNK12QColorMatrix10transposedEv(
    const QColorMatrix *self) {
  return new QColorMatrix(self->transposed());
}

//  QColorMatrix QColorMatrix::identity()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix8identityEv() {
  return new QColorMatrix(QColorMatrix::identity());
}

//  QColorMatrix QColorMatrix::fromScale(QColorVector v)
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix9fromScaleE12QColorVector(
    const QColorVector *v) {
  return new QColorMatrix(QColorMatrix::fromScale(*v));
}

//  QColorMatrix QColorMatrix::chromaticAdaptation(const QColorVector
//      &whitePoint)
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix19chromaticAdaptationERK12QColorVector(
    const QColorVector *whitePoint) {
  return new QColorMatrix(QColorMatrix::chromaticAdaptation(*whitePoint));
}

//  QColorMatrix QColorMatrix::toXyzFromSRgb()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix13toXyzFromSRgbEv() {
  return new QColorMatrix(QColorMatrix::toXyzFromSRgb());
}

//  QColorMatrix QColorMatrix::toXyzFromAdobeRgb()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix17toXyzFromAdobeRgbEv() {
  return new QColorMatrix(QColorMatrix::toXyzFromAdobeRgb());
}

//  QColorMatrix QColorMatrix::toXyzFromDciP3D65()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix17toXyzFromDciP3D65Ev() {
  return new QColorMatrix(QColorMatrix::toXyzFromDciP3D65());
}

//  QColorMatrix QColorMatrix::toXyzFromProPhotoRgb()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix20toXyzFromProPhotoRgbEv() {
  return new QColorMatrix(QColorMatrix::toXyzFromProPhotoRgb());
}

//  QColorMatrix QColorMatrix::toXyzFromBt2020()
extern "C" Q_DECL_EXPORT
QColorMatrix *ritual_ZN12QColorMatrix15toXyzFromBt2020Ev() {
  return new QColorMatrix(QColorMatrix::toXyzFromBt2020());
}

//  bool operator==(const QColorMatrix &lhs, const QColorMatrix &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QColorMatrixS1_(
    const QColorMatrix *lhs,
    const QColorMatrix *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QColorMatrix &lhs, const QColorMatrix &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QColorMatrixS1_(
    const QColorMatrix *lhs,
    const QColorMatrix *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QColorMatrix::~QColorMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorMatrixD1Ev(QColorMatrix *self) {
  delete self;
}
