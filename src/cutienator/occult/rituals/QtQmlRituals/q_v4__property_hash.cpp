//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 28, as _ZN3QV412PropertyHash8addEntryERKNS0_5EntryEi
namespace QV4 {
inline void PropertyHash::addEntry(const PropertyHash::Entry &entry, int classSize)
{
    // fill up to max 50%
    bool grow = (d->alloc <= d->size*2);

    if (classSize < d->size || grow)
        detach(grow, classSize);

    uint idx = entry.identifier.id() % d->alloc;
    while (d->entries[idx].identifier.isValid()) {
        ++idx;
        idx %= d->alloc;
    }
    d->entries[idx] = entry;
    ++d->size;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 45, as _ZN3QV412PropertyHash6detachEbi
namespace QV4 {
inline void PropertyHash::detach(bool grow, int classSize)
{
    if (d->refCount == 1 && !grow)
        return;

    PropertyHashData *dd = new PropertyHashData(grow ? d->numBits + 1 : d->numBits);
    for (int i = 0; i < d->alloc; ++i) {
        const Entry &e = d->entries[i];
        if (!e.identifier.isValid() || e.index >= static_cast<unsigned>(classSize))
            continue;
        uint idx = e.identifier.id() % dd->alloc;
        while (dd->entries[idx].identifier.isValid()) {
            ++idx;
            idx %= dd->alloc;
        }
        dd->entries[idx] = e;
    }
    dd->size = classSize;
    if (!--d->refCount)
        delete d;
    d = dd;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::PropertyHash::PropertyHash()
extern "C" Q_DECL_EXPORT
QV4::PropertyHash *ritual_ZN3QV412PropertyHashC1Ev() {
  return new QV4::PropertyHash();
}

//  QV4::PropertyHash::PropertyHash(const PropertyHash &other)
extern "C" Q_DECL_EXPORT
QV4::PropertyHash *ritual_ZN3QV412PropertyHashC1ERKS0_(
    const QV4::PropertyHash *other) {
  return new QV4::PropertyHash(*other);
}

//  QV4::PropertyHash::~PropertyHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412PropertyHashD1Ev(QV4::PropertyHash *self) {
  delete self;
}

//  PropertyHash &QV4::PropertyHash::operator=(const PropertyHash &other)
extern "C" Q_DECL_EXPORT
QV4::PropertyHash *ritual_ZN3QV412PropertyHashaSERKS0_(
    QV4::PropertyHash *self,
    const QV4::PropertyHash *other) {
  return &(self->operator=(*other));
}

//  void QV4::PropertyHash::addEntry(const Entry &entry, int classSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412PropertyHash8addEntryERKNS0_5EntryEi(
    QV4::PropertyHash *self,
    const QV4::PropertyHash::Entry *entry,
    int classSize) {
  self->addEntry(*entry, classSize);
}

//  Entry *QV4::PropertyHash::lookup(PropertyKey identifier) const
extern "C" Q_DECL_EXPORT
QV4::PropertyHash::Entry *ritual_ZNK3QV412PropertyHash6lookupENS_11PropertyKeyE(
    const QV4::PropertyHash *self,
    const QV4::PropertyKey *identifier) {
  return self->lookup(*identifier);
}

//  void QV4::PropertyHash::detach(bool grow, int classSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412PropertyHash6detachEbi(
    QV4::PropertyHash *self,
    bool grow,
    int classSize) {
  self->detach(grow, classSize);
}
