//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolormatrix_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolormatrix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QColorVector::QColorVector()
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN12QColorVectorC1Ev() {
  return new QColorVector();
}

//  QColorVector::QColorVector(float x, float y, float z, float w)
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN12QColorVectorC1Effff(
    float x,
    float y,
    float z,
    float w) {
  return new QColorVector(x, y, z, w);
}

//  QColorVector QColorVector::fromXYChromaticity(QPointF chr)
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN12QColorVector18fromXYChromaticityE7QPointF(
    const QPointF *chr) {
  return new QColorVector(QColorVector::fromXYChromaticity(*chr));
}

//  bool QColorVector::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorVector6isNullEv(const QColorVector *self) {
  return self->isNull();
}

//  bool QColorVector::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorVector7isValidEv(const QColorVector *self) {
  return self->isValid();
}

//  bool QColorVector::isValidChromaticity(const QPointF &chr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QColorVector19isValidChromaticityERK7QPointF(
    const QPointF *chr) {
  return QColorVector::isValidChromaticity(*chr);
}

//  QColorVector QColorVector::operator*(float f) const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorVectormlEf(
    const QColorVector *self,
    float f) {
  return new QColorVector(self->operator*(f));
}

//  QColorVector QColorVector::operator+(const QColorVector &v) const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorVectorplERKS_(
    const QColorVector *self,
    const QColorVector *v) {
  return new QColorVector(self->operator+(*v));
}

//  QColorVector QColorVector::operator-(const QColorVector &v) const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorVectormiERKS_(
    const QColorVector *self,
    const QColorVector *v) {
  return new QColorVector(self->operator-(*v));
}

//  void QColorVector::operator+=(const QColorVector &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorVectorpLERKS_(
    QColorVector *self,
    const QColorVector *v) {
  self->operator+=(*v);
}

//  QPointF QColorVector::toChromaticity() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QColorVector14toChromaticityEv(
    const QColorVector *self) {
  return new QPointF(self->toChromaticity());
}

//  QPointF QColorVector::D50Chromaticity()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12QColorVector15D50ChromaticityEv() {
  return new QPointF(QColorVector::D50Chromaticity());
}

//  QPointF QColorVector::D65Chromaticity()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12QColorVector15D65ChromaticityEv() {
  return new QPointF(QColorVector::D65Chromaticity());
}

//  QColorVector QColorVector::D50()
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN12QColorVector3D50Ev() {
  return new QColorVector(QColorVector::D50());
}

//  QColorVector QColorVector::D65()
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN12QColorVector3D65Ev() {
  return new QColorVector(QColorVector::D65());
}

//  QColorVector QColorVector::xyzToLab() const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorVector8xyzToLabEv(const QColorVector *self) {
  return new QColorVector(self->xyzToLab());
}

//  QColorVector QColorVector::labToXyz() const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK12QColorVector8labToXyzEv(const QColorVector *self) {
  return new QColorVector(self->labToXyz());
}

//  bool operator==(const QColorVector &lhs, const QColorVector &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QColorVectorS1_(
    const QColorVector *lhs,
    const QColorVector *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QColorVector &lhs, const QColorVector &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QColorVectorS1_(
    const QColorVector *lhs,
    const QColorVector *rhs) {
  return operator!=(*lhs, *rhs);
}

//  float QColorVector::fastCbrt(float x)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QColorVector8fastCbrtEf(float x) {
  return QColorVector::fastCbrt(x);
}

//  QColorVector::~QColorVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorVectorD1Ev(QColorVector *self) {
  delete self;
}
