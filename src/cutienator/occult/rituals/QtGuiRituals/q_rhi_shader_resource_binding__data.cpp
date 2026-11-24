//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QRhiShaderResourceBinding::Data::arraySize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QRhiShaderResourceBinding4Data9arraySizeEv(
    const QRhiShaderResourceBinding::Data *self) {
  return self->arraySize();
}

//  QRhiShaderResourceBinding::Data::~Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRhiShaderResourceBinding4DataD1Ev(
    QRhiShaderResourceBinding::Data *self) {
  delete self;
}
