//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacesupplier_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacesupplier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacesupplier.h>
#include <QtLocation/private/qplacesupplier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacesupplier.cpp, line 22, as _ZNK21QPlaceSupplierPrivate7isEmptyEv
inline bool QPlaceSupplierPrivate::isEmpty() const
{
    return (name.isEmpty()
            && supplierId.isEmpty()
            && url.isEmpty()
            && icon.isEmpty()
            );
}
//  -----------------------------------------------------------------------

//  bool QPlaceSupplierPrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlaceSupplierPrivate7isEmptyEv(
    const QPlaceSupplierPrivate *self) {
  return self->isEmpty();
}

//  QPlaceSupplierPrivate::~QPlaceSupplierPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlaceSupplierPrivateD1Ev(QPlaceSupplierPrivate *self) {
  delete self;
}
