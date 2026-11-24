//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolorspace_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolorspace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorSpacePrivate::LUT::LUT()
extern "C" Q_DECL_EXPORT
QColorSpacePrivate::LUT *ritual_ZN18QColorSpacePrivate3LUTC1Ev() {
  return new QColorSpacePrivate::LUT();
}

//  QColorSpacePrivate::LUT::~LUT()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate3LUTD1Ev(QColorSpacePrivate::LUT *self) {
  delete self;
}

//  QColorSpacePrivate::LUT::LUT(const LUT &other)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate::LUT *ritual_ZN18QColorSpacePrivate3LUTC1ERKS0_(
    const QColorSpacePrivate::LUT *other) {
  return new QColorSpacePrivate::LUT(*other);
}
