//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QMetalShaderResourceBindings::BoundStorageImageData::~BoundStorageImageDa
//      ta()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QMetalShaderResourceBindings21BoundStorageImageDataD1Ev(
    QMetalShaderResourceBindings::BoundStorageImageData *self) {
  delete self;
}

#endif  // QT_CONFIG(metal)
