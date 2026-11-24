//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QNullRenderTargetData::QNullRenderTargetData(QRhiImplementation *a0)
extern "C" Q_DECL_EXPORT
QNullRenderTargetData *ritual_ZN21QNullRenderTargetDataC1EP18QRhiImplementation(
    QRhiImplementation *a0) {
  return new QNullRenderTargetData(a0);
}

//  QNullRenderTargetData::~QNullRenderTargetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNullRenderTargetDataD1Ev(QNullRenderTargetData *self) {
  delete self;
}
