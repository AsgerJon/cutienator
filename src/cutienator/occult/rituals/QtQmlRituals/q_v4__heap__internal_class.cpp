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

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 324, as local:qv4internalclass.cpp:addDummyEntry
namespace QV4::Heap {
static void addDummyEntry(InternalClass *newClass, PropertyHash::Entry e)
{
    // add a dummy entry, since we need two entries for accessors
    newClass->propertyTable.addEntry(e, newClass->size);
    newClass->nameMap.add(newClass->size, PropertyKey::invalid());
    newClass->propertyData.add(newClass->size, PropertyAttributes());
    ++newClass->size;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 333, as local:qv4internalclass.cpp:attributesFromFlags
namespace QV4::Heap {
static PropertyAttributes attributesFromFlags(int flags)
{
    PropertyAttributes attributes;
    attributes.m_all = uchar(flags);
    return attributes;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 340, as local:qv4internalclass.cpp:cleanInternalClass
namespace QV4::Heap {
static Heap::InternalClass *cleanInternalClass(Heap::InternalClass *orig)
{
    if (++orig->numRedundantTransitions < Heap::InternalClass::MaxRedundantTransitions)
        return orig;

    // We will generally add quite a few transitions here. We have 255 redundant ones.
    // We can expect at least as many significant ones in addition.
    QVarLengthArray<InternalClassTransition, 1> transitions;

    Scope scope(orig->engine);
    Scoped<QV4::InternalClass> child(scope, orig);

    {
        quint8 remainingRedundantTransitions = orig->numRedundantTransitions;
        QSet<PropertyKey> properties;
        int structureChanges = 0;

        Scoped<QV4::InternalClass> parent(scope, orig->parent);
        while (parent && remainingRedundantTransitions > 0) {
            Q_ASSERT(child->d() != scope.engine->classes[ExecutionEngine::Class_Empty]);
            const auto it = std::find_if(
                        parent->d()->transitions.begin(), parent->d()->transitions.end(),
                        [&child](const InternalClassTransition &t) {
                return child->d() == t.lookup;
            });
            Q_ASSERT(it != parent->d()->transitions.end());

            if (it->flags & InternalClassTransition::StructureChange) {
                // A structural change. Each kind of structural change has to be recorded only once.
                if ((structureChanges & it->flags) != it->flags) {
                    transitions.push_back(*it);
                    structureChanges |= it->flags;
                } else {
                    --remainingRedundantTransitions;
                }
            } else if (!properties.contains(it->id)) {
                // We only need the final state of the property.
                properties.insert(it->id);

                // Property removal creates _two_ redundant transitions.
                // We don't have to replay either, but numRedundantTransitions only records one.
                if (it->flags != 0)
                    transitions.push_back(*it);
            } else {
                --remainingRedundantTransitions;
            }

            child = parent->d();
            parent = child->d()->parent;
            Q_ASSERT(child->d() != parent->d());
        }
    }

    for (auto it = transitions.rbegin(); it != transitions.rend(); ++it) {
        switch (it->flags) {
        case InternalClassTransition::NotExtensible:
            child = child->d()->nonExtensible();
            continue;
        case InternalClassTransition::VTableChange:
            child = child->d()->changeVTable(it->vtable);
            continue;
        case InternalClassTransition::PrototypeChange:
            child = child->d()->changePrototype(it->prototype);
            continue;
        case InternalClassTransition::ProtoClass:
            child = child->d()->asProtoClass();
            continue;
        case InternalClassTransition::Sealed:
            child = child->d()->sealed();
            continue;
        case InternalClassTransition::Frozen:
            child = child->d()->frozen();
            continue;
        case InternalClassTransition::Locked:
            child = child->d()->locked();
            continue;
        default:
            Q_ASSERT(it->flags != 0);
            Q_ASSERT(it->flags < InternalClassTransition::StructureChange);
            child = child->addMember(it->id, attributesFromFlags(it->flags));
            continue;
        }
    }

    return child->d();
}
}  // namespace QV4::Heap

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 313, as _ZN3QV44Heap13InternalClass24lookupOrInsertTransitionERKNS_23InternalClassTransitionE
namespace QV4::Heap {
inline InternalClassTransition &InternalClass::lookupOrInsertTransition(const InternalClassTransition &t)
{
    QVarLengthArray<Transition, 1>::iterator it = std::lower_bound(transitions.begin(), transitions.end(), t);
    if (it != transitions.end() && *it == t) {
        return *it;
    } else {
        it = transitions.insert(it, t);
        return *it;
    }
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 246, as _ZN3QV44Heap13InternalClass4initEPS1_
namespace QV4::Heap {
inline void InternalClass::init(Heap::InternalClass *other)
{
    Base::init();
    new (&propertyTable) PropertyHash(other->propertyTable);
    new (&nameMap) SharedInternalClassData<PropertyKey>(other->nameMap);
    new (&propertyData) SharedInternalClassData<PropertyAttributes>(other->propertyData);
    new (&transitions) QVarLengthArray<Transition, 1>();

    engine = other->engine;
    vtable = other->vtable;
    prototype = other->prototype;
    parent = other;
    size = other->size;
    numRedundantTransitions = other->numRedundantTransitions;
    flags = other->flags;
    protoId = engine->newProtoId();

    internalClass.set(engine, other->internalClass);
    QV4::WriteBarrier::markCustom(engine, [&](QV4::MarkStack *stack) {
        if constexpr (QV4::WriteBarrier::isInsertionBarrier) {
            other->mark(stack);
        }
    });
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 539, as _ZN3QV44Heap13InternalClass13nonExtensibleEv
namespace QV4::Heap {
inline Heap::InternalClass *InternalClass::nonExtensible()
{
    if (!isExtensible())
        return this;

    Transition temp = { { PropertyKey::invalid() }, nullptr, Transition::NotExtensible};
    Transition &t = lookupOrInsertTransition(temp);
    if (t.lookup)
        return t.lookup;

    Scope scope(engine);
    Scoped<QV4::InternalClass> scopedNewClass(scope, engine->newClass(this));
    auto newClass = scopedNewClass->d();
    newClass->flags |= NotExtensible;

    t.lookup = newClass;
    Q_ASSERT(t.lookup);
    return newClass;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 559, as _ZN3QV44Heap13InternalClass6lockedEv
namespace QV4::Heap {
inline InternalClass *InternalClass::locked()
{
    if (isLocked())
        return this;

    Transition temp = { { PropertyKey::invalid() }, nullptr, Transition::Locked};
    Transition &t = lookupOrInsertTransition(temp);
    if (t.lookup)
        return t.lookup;

    Scope scope(engine);
    Scoped<QV4::InternalClass> scopedNewClass(scope, engine->newClass(this));
    auto newClass = scopedNewClass->d();
    newClass->flags |= Locked;

    t.lookup = newClass;
    Q_ASSERT(t.lookup);
    return newClass;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 742, as _ZNK3QV44Heap13InternalClass18isImplicitlyFrozenEv
namespace QV4::Heap {
inline bool InternalClass::isImplicitlyFrozen() const
{
    if (isFrozen())
        return true;

    for (uint i = 0; i < size; ++i) {
        const PropertyAttributes attrs = propertyData.at(i);
        if (attrs.isEmpty())
            continue;
        if ((attrs.isData() && attrs.isWritable()) || attrs.isConfigurable())
            return false;
    }

    return true;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 758, as _ZN3QV44Heap13InternalClass12asProtoClassEv
namespace QV4::Heap {
inline Heap::InternalClass *InternalClass::asProtoClass()
{
    if (isUsedAsProto())
        return this;

    Transition temp = { { PropertyKey::invalid() }, nullptr, Transition::ProtoClass };
    Transition &t = lookupOrInsertTransition(temp);
    if (t.lookup)
        return t.lookup;

    Scope scope(engine);
    Scoped<QV4::InternalClass> scopedNewClass(scope, engine->newClass(this));
    auto newClass = scopedNewClass->d();
    newClass->flags |= UsedAsProto;

    t.lookup = newClass;
    Q_ASSERT(t.lookup);
    return newClass;
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 632, as _ZN3QV44Heap13InternalClass16removeChildEntryEPS1_
namespace QV4::Heap {
inline void InternalClass::removeChildEntry(InternalClass *child)
{
    Q_ASSERT(engine);
    for (auto &t : transitions) {
        if (t.lookup == child) {
            t.lookup = nullptr;
            return;
        }
    }
    Q_UNREACHABLE();

}
}  // namespace QV4::Heap
//  -----------------------------------------------------------------------

//  InternalClassTransition
//      &QV4::Heap::InternalClass::lookupOrInsertTransition(const
//      InternalClassTransition &t)
extern "C" Q_DECL_EXPORT
QV4::InternalClassTransition *ritual_ZN3QV44Heap13InternalClass24lookupOrInsertTransitionERKNS_23InternalClassTransitionE(
    QV4::Heap::InternalClass *self,
    const QV4::InternalClassTransition *t) {
  return &(self->lookupOrInsertTransition(*t));
}

//  bool QV4::Heap::InternalClass::isExtensible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass12isExtensibleEv(
    const QV4::Heap::InternalClass *self) {
  return self->isExtensible();
}

//  bool QV4::Heap::InternalClass::isSealed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isSealedEv(
    const QV4::Heap::InternalClass *self) {
  return self->isSealed();
}

//  bool QV4::Heap::InternalClass::isFrozen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isFrozenEv(
    const QV4::Heap::InternalClass *self) {
  return self->isFrozen();
}

//  bool QV4::Heap::InternalClass::isUsedAsProto() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass13isUsedAsProtoEv(
    const QV4::Heap::InternalClass *self) {
  return self->isUsedAsProto();
}

//  bool QV4::Heap::InternalClass::isLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isLockedEv(
    const QV4::Heap::InternalClass *self) {
  return self->isLocked();
}

//  void QV4::Heap::InternalClass::init(InternalClass *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13InternalClass4initEPS1_(
    QV4::Heap::InternalClass *self,
    QV4::Heap::InternalClass *other) {
  self->init(other);
}

//  ReturnedValue QV4::Heap::InternalClass::keyAt(uint index) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV44Heap13InternalClass5keyAtEj(
    const QV4::Heap::InternalClass *self,
    uint index) {
  return self->keyAt(index);
}

//  InternalClass *QV4::Heap::InternalClass::nonExtensible()
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass13nonExtensibleEv(
    QV4::Heap::InternalClass *self) {
  return self->nonExtensible();
}

//  InternalClass *QV4::Heap::InternalClass::locked()
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass6lockedEv(
    QV4::Heap::InternalClass *self) {
  return self->locked();
}

//  PropertyHash::Entry *QV4::Heap::InternalClass::findEntry(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::PropertyHash::Entry *ritual_ZN3QV44Heap13InternalClass9findEntryENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return self->findEntry(*id);
}

//  InternalClassEntry QV4::Heap::InternalClass::find(const PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::InternalClassEntry *ritual_ZN3QV44Heap13InternalClass4findENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::InternalClassEntry(self->find(*id));
}

//  IndexAndAttribute QV4::Heap::InternalClass::findValueOrGetter(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass::IndexAndAttribute *ritual_ZN3QV44Heap13InternalClass17findValueOrGetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::Heap::InternalClass::IndexAndAttribute(
      self->findValueOrGetter(
          *id));
}

//  IndexAndAttribute QV4::Heap::InternalClass::findValueOrSetter(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass::IndexAndAttribute *ritual_ZN3QV44Heap13InternalClass17findValueOrSetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::Heap::InternalClass::IndexAndAttribute(
      self->findValueOrSetter(
          *id));
}

//  uint QV4::Heap::InternalClass::indexOfValueOrGetter(const PropertyKey id)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV44Heap13InternalClass20indexOfValueOrGetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return self->indexOfValueOrGetter(*id);
}

//  bool QV4::Heap::InternalClass::verifyIndex(const PropertyKey id, uint
//      index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap13InternalClass11verifyIndexENS_11PropertyKeyEj(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id,
    uint index) {
  return self->verifyIndex(*id, index);
}

//  bool QV4::Heap::InternalClass::isImplicitlyFrozen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass18isImplicitlyFrozenEv(
    const QV4::Heap::InternalClass *self) {
  return self->isImplicitlyFrozen();
}

//  InternalClass *QV4::Heap::InternalClass::asProtoClass()
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass12asProtoClassEv(
    QV4::Heap::InternalClass *self) {
  return self->asProtoClass();
}

//  InternalClass *QV4::Heap::InternalClass::changeVTable(const VTable *vt)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass12changeVTableEPKNS_6VTableE(
    QV4::Heap::InternalClass *self,
    const QV4::VTable *vt) {
  return self->changeVTable(vt);
}

//  InternalClass *QV4::Heap::InternalClass::changePrototype(Heap::Object
//      *proto)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass15changePrototypeEPNS0_6ObjectE(
    QV4::Heap::InternalClass *self,
    QV4::Heap::Object *proto) {
  return self->changePrototype(proto);
}

//  InternalClass *QV4::Heap::InternalClass::changeVTableImpl(const VTable
//      *vt)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass16changeVTableImplEPKNS_6VTableE(
    QV4::Heap::InternalClass *self,
    const QV4::VTable *vt) {
  return self->changeVTableImpl(vt);
}

//  InternalClass *QV4::Heap::InternalClass::changePrototypeImpl(Heap::Object
//      *proto)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass19changePrototypeImplEPNS0_6ObjectE(
    QV4::Heap::InternalClass *self,
    QV4::Heap::Object *proto) {
  return self->changePrototypeImpl(proto);
}

//  void QV4::Heap::InternalClass::removeChildEntry(InternalClass *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13InternalClass16removeChildEntryEPS1_(
    QV4::Heap::InternalClass *self,
    QV4::Heap::InternalClass *child) {
  self->removeChildEntry(child);
}
