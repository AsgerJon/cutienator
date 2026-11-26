//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolorclut_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolorclut_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolormatrix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorVector QColorCLUT::interpolate(const QColorVector &a, const
//      QColorVector &b, float t)
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZN10QColorCLUT11interpolateERK12QColorVectorS2_f(
    const QColorVector *a,
    const QColorVector *b,
    float t) {
  return new QColorVector(QColorCLUT::interpolate(*a, *b, t));
}

//  void QColorCLUT::interpolateIn(QColorVector &a, const QColorVector &b,
//      float t)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorCLUT13interpolateInER12QColorVectorRKS0_f(
    QColorVector *a,
    const QColorVector *b,
    float t) {
  QColorCLUT::interpolateIn(*a, *b, t);
}

//  bool QColorCLUT::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QColorCLUT7isEmptyEv(const QColorCLUT *self) {
  return self->isEmpty();
}

//  QColorVector QColorCLUT::apply(const QColorVector &v) const
extern "C" Q_DECL_EXPORT
QColorVector *ritual_ZNK10QColorCLUT5applyERK12QColorVector(
    const QColorCLUT *self,
    const QColorVector *v) {
  return new QColorVector(self->apply(*v));
}

//  QColorCLUT::~QColorCLUT()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorCLUTD1Ev(QColorCLUT *self) {
  delete self;
}
