//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QPathSegments::Intersection::operator<(const Intersection &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPathSegments12IntersectionltERKS0_(
    const QPathSegments::Intersection *self,
    const QPathSegments::Intersection *o) {
  return self->operator<(*o);
}

//  QPathSegments::Intersection::~Intersection()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPathSegments12IntersectionD1Ev(
    QPathSegments::Intersection *self) {
  delete self;
}
