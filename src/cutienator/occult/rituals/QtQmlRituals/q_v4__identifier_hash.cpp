//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  4. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 15, as _ZN3QV414IdentifierHashC1EPNS_15ExecutionEngineE
namespace QV4 {
inline IdentifierHash::IdentifierHash(ExecutionEngine *engine)
{
    d = new IdentifierHashData(engine->identifierTable, 3);
    Q_ASSERT(isValid());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 113, as _ZN3QV414IdentifierHashC1ERKS0_
inline QV4::IdentifierHash::IdentifierHash(const IdentifierHash &other)
{
    d = other.d;
    if (d)
        d->refCount.ref();
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 136, as _ZNK3QV414IdentifierHash4sizeEv
namespace QV4 {
inline int IdentifierHash::size() const
{
    return d ? d->size : 0;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 21, as _ZN3QV414IdentifierHash8addEntryENS_11PropertyKeyEi
namespace QV4 {
inline void IdentifierHash::addEntry(PropertyKey identifier, int value)
{
    Q_ASSERT(identifier.isStringOrSymbol());

    // fill up to max 50%
    bool grow = (d->alloc <= d->size*2);

    if (grow) {
        ++d->numBits;
        int newAlloc = qPrimeForNumBits(d->numBits);
        IdentifierHashEntry *newEntries = (IdentifierHashEntry *)malloc(newAlloc * sizeof(IdentifierHashEntry));
        memset(newEntries, 0, newAlloc*sizeof(IdentifierHashEntry));
        for (int i = 0; i < d->alloc; ++i) {
            const IdentifierHashEntry &e = d->entries[i];
            if (!e.identifier.isValid())
                continue;
            uint idx = e.identifier.id() % newAlloc;
            while (newEntries[idx].identifier.isValid()) {
                ++idx;
                idx %= newAlloc;
            }
            newEntries[idx] = e;
        }
        free(d->entries);
        d->entries = newEntries;
        d->alloc = newAlloc;
    }

    uint idx = identifier.id() % d->alloc;
    while (d->entries[idx].identifier.isValid()) {
        Q_ASSERT(d->entries[idx].identifier != identifier);
        ++idx;
        idx %= d->alloc;
    }
    d->entries[idx].identifier = identifier;
    ++d->size;
    (d->entries + idx)->value = value;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 60, as _ZNK3QV414IdentifierHash6lookupENS_11PropertyKeyE
namespace QV4 {
inline int IdentifierHash::lookup(PropertyKey identifier) const
{
    if (!d || !identifier.isStringOrSymbol())
        return -1;
    Q_ASSERT(d->entries);

    uint idx = identifier.id() % d->alloc;
    while (1) {
        if (!d->entries[idx].identifier.isValid())
            return -1;
        if (d->entries[idx].identifier == identifier)
            return (d->entries + idx)->value;
        ++idx;
        idx %= d->alloc;
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 89, as _ZNK3QV414IdentifierHash13reverseLookupEi
namespace QV4 {
inline PropertyKey IdentifierHash::reverseLookup(int value) const
{
    IdentifierHashEntry *e = d->entries;
    IdentifierHashEntry *end = e + d->alloc;
    while (e < end) {
        if (e->identifier.isValid() && e->value == value)
            return e->identifier;
        ++e;
    }
    return PropertyKey::invalid();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 77, as _ZNK3QV414IdentifierHash12toIdentifierERK7QString
namespace QV4 {
inline PropertyKey IdentifierHash::toIdentifier(const QString &str) const
{
    Q_ASSERT(d);
    return d->identifierTable->asPropertyKey(str, IdentifierTable::ForceConversionToId);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 83, as _ZNK3QV414IdentifierHash12toIdentifierEPNS_4Heap6StringE
namespace QV4 {
inline PropertyKey IdentifierHash::toIdentifier(Heap::String *str) const
{
    Q_ASSERT(d);
    return d->identifierTable->asPropertyKey(str);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::IdentifierHash::IdentifierHash()
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashC1Ev() {
  return new QV4::IdentifierHash();
}

//  QV4::IdentifierHash::IdentifierHash(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QV4::IdentifierHash(engine);
}

//  QV4::IdentifierHash::IdentifierHash(const IdentifierHash &other)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashC1ERKS0_(
    const QV4::IdentifierHash *other) {
  return new QV4::IdentifierHash(*other);
}

//  QV4::IdentifierHash::IdentifierHash(IdentifierHash &&other)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashC1EOS0_(
    QV4::IdentifierHash *other) {
  return new QV4::IdentifierHash(std::move(*other));
}

//  QV4::IdentifierHash::~IdentifierHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHashD1Ev(QV4::IdentifierHash *self) {
  delete self;
}

//  void QV4::IdentifierHash::swap(IdentifierHash &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHash4swapERS0_(
    QV4::IdentifierHash *self,
    QV4::IdentifierHash *other) {
  self->swap(*other);
}

//  IdentifierHash &QV4::IdentifierHash::operator=(IdentifierHash &&other)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashaSEOS0_(
    QV4::IdentifierHash *self,
    QV4::IdentifierHash *other) {
  return &(self->operator=(std::move(*other)));
}

//  bool QV4::IdentifierHash::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414IdentifierHash7isValidEv(
    const QV4::IdentifierHash *self) {
  return self->isValid();
}

//  int QV4::IdentifierHash::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV414IdentifierHash4sizeEv(const QV4::IdentifierHash *self) {
  return self->size();
}

//  void QV4::IdentifierHash::add(const QString &str, int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHash3addERK7QStringi(
    QV4::IdentifierHash *self,
    const QString *str,
    int value) {
  self->add(*str, value);
}

//  void QV4::IdentifierHash::add(Heap::String *str, int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHash3addEPNS_4Heap6StringEi(
    QV4::IdentifierHash *self,
    QV4::Heap::String *str,
    int value) {
  self->add(str, value);
}

//  int QV4::IdentifierHash::value(const QString &str) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV414IdentifierHash5valueERK7QString(
    const QV4::IdentifierHash *self,
    const QString *str) {
  return self->value(*str);
}

//  int QV4::IdentifierHash::value(Heap::String *str) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV414IdentifierHash5valueEPNS_4Heap6StringE(
    const QV4::IdentifierHash *self,
    QV4::Heap::String *str) {
  return self->value(str);
}

//  void QV4::IdentifierHash::addEntry(PropertyKey i, int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHash8addEntryENS_11PropertyKeyEi(
    QV4::IdentifierHash *self,
    const QV4::PropertyKey *i,
    int value) {
  self->addEntry(*i, value);
}

//  int QV4::IdentifierHash::lookup(PropertyKey identifier) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV414IdentifierHash6lookupENS_11PropertyKeyE(
    const QV4::IdentifierHash *self,
    const QV4::PropertyKey *identifier) {
  return self->lookup(*identifier);
}

//  PropertyKey QV4::IdentifierHash::reverseLookup(int value) const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV414IdentifierHash13reverseLookupEi(
    const QV4::IdentifierHash *self,
    int value) {
  return new QV4::PropertyKey(self->reverseLookup(value));
}

//  PropertyKey QV4::IdentifierHash::toIdentifier(const QString &str) const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV414IdentifierHash12toIdentifierERK7QString(
    const QV4::IdentifierHash *self,
    const QString *str) {
  return new QV4::PropertyKey(self->toIdentifier(*str));
}

//  PropertyKey QV4::IdentifierHash::toIdentifier(Heap::String *str) const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV414IdentifierHash12toIdentifierEPNS_4Heap6StringE(
    const QV4::IdentifierHash *self,
    QV4::Heap::String *str) {
  return new QV4::PropertyKey(self->toIdentifier(str));
}


//  Qt's own code, taken from ../qtdeclarative/src/qml/jsruntime/
//  qv4identifierhash.cpp, lines 101 and 107, with the word 'inline' put
//  before each, as the package file does: the specializations of
//  toString that key<String> calls. reverseLookup, which key calls, is
//  among the package file's copies already.
namespace QV4 {
template<>
inline QString IdentifierHash::toString<QString>(PropertyKey key) const
{
    return key.isValid() ? key.toQString() : QString();
}

template<>
inline Heap::String *IdentifierHash::toString<Heap::String *>(
    PropertyKey key) const
{
    return key.isString()
        ? static_cast<Heap::String *>(key.asStringOrSymbol())
        : nullptr;
}
}  // namespace QV4

//  QString QV4::IdentifierHash::key<QString>(int value) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV414IdentifierHash3keyI7QStringEET_i(
    const QV4::IdentifierHash *self, int value) {
  return new QString(self->key<QString>(value));
}

//  QV4::Heap::String *QV4::IdentifierHash::key<QV4::Heap::String *>(int
//      value) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV414IdentifierHash3keyIPNS_4Heap6StringEEET_i(
    const QV4::IdentifierHash *self, int value) {
  return self->key<QV4::Heap::String *>(value);
}

//  QString QV4::IdentifierHash::toString<QString>(PropertyKey key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV414IdentifierHash8toStringI7QStringEET_NS_11PropertyKeyE(
    const QV4::IdentifierHash *self, const QV4::PropertyKey *key) {
  return new QString(self->toString<QString>(*key));
}

//  QV4::Heap::String *QV4::IdentifierHash::toString<QV4::Heap::String
//      *>(PropertyKey key) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV414IdentifierHash8toStringIPNS_4Heap6StringEEET_NS_11PropertyKeyE(
    const QV4::IdentifierHash *self, const QV4::PropertyKey *key) {
  return self->toString<QV4::Heap::String *>(*key);
}
