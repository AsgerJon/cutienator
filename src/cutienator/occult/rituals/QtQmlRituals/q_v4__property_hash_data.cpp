//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4internalclass_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 18, as _ZN3QV416PropertyHashDataC1Ei
namespace QV4 {
inline PropertyHashData::PropertyHashData(int numBits)
    : refCount(1)
    , size(0)
    , numBits(numBits)
{
    alloc = qPrimeForNumBits(numBits);
    entries = (PropertyHash::Entry *)malloc(alloc*sizeof(PropertyHash::Entry));
    memset(entries, 0, alloc*sizeof(PropertyHash::Entry));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::PropertyHashData::PropertyHashData(int numBits)
extern "C" Q_DECL_EXPORT
QV4::PropertyHashData *ritual_ZN3QV416PropertyHashDataC1Ei(int numBits) {
  return new QV4::PropertyHashData(numBits);
}

//  QV4::PropertyHashData::~PropertyHashData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416PropertyHashDataD1Ev(QV4::PropertyHashData *self) {
  delete self;
}
