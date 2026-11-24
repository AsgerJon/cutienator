//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qimage_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QImageData::ImageSizeParameters::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QImageData19ImageSizeParameters7isValidEv(
    const QImageData::ImageSizeParameters *self) {
  return self->isValid();
}

//  QImageData::ImageSizeParameters::~ImageSizeParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QImageData19ImageSizeParametersD1Ev(
    QImageData::ImageSizeParameters *self) {
  delete self;
}
