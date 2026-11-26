//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4internalclass_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4memberdata_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4proxy_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qloggingcategory.h>
#include <stdint.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 304, as _ZN3QV44Heap13InternalClass12changeMemberEPNS_6ObjectENS_11PropertyKeyENS_18PropertyAttributesEPNS_18InternalClassEntryE
namespace QV4::Heap {
inline void InternalClass::changeMember(QV4::Object *object, PropertyKey id, PropertyAttributes data, InternalClassEntry *entry)
{
    Q_ASSERT(id.isStringOrSymbol());

    Heap::InternalClass *oldClass = object->internalClass();
    Heap::InternalClass *newClass = oldClass->changeMember(id, data, entry);
    object->setInternalClass(newClass);
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4internalclass.cpp, line 427, as _ZN3QV44Heap13InternalClass12changeMemberENS_11PropertyKeyENS_18PropertyAttributesEPNS_18InternalClassEntryE
namespace QV4::Heap {
inline Heap::InternalClass *InternalClass::changeMember(
        PropertyKey identifier, PropertyAttributes data, InternalClassEntry *entry)
{
    if (!data.isEmpty())
        data.resolve();
    PropertyHash::Entry *e = findEntry(identifier);
    Q_ASSERT(e && e->index != UINT_MAX);
    uint idx = e->index;
    Q_ASSERT(idx != UINT_MAX);

    if (entry) {
        entry->index = idx;
        entry->setterIndex = e->setterIndex;
        entry->attributes = data;
    }

    if (data == propertyData.at(idx))
        return this;

    Transition temp = { { identifier }, nullptr, int(data.all()) };
    Transition &t = lookupOrInsertTransition(temp);
    if (t.lookup)
        return t.lookup;

    // create a new class and add it to the tree
    Scope scope(engine);
    Scoped<QV4::InternalClass> scopedNewClass(scope, engine->newClass(this));
    auto newClass = scopedNewClass->d();
    if (data.isAccessor() && e->setterIndex == UINT_MAX) {
        Q_ASSERT(!propertyData.at(idx).isAccessor());

        // add a dummy entry for the accessor
        if (entry)
            entry->setterIndex = newClass->size;
        e->setterIndex = newClass->size;
        addDummyEntry(newClass, *e);
    }

    newClass->propertyData.set(idx, data);

    t.lookup = newClass;
    Q_ASSERT(t.lookup);

    Heap::InternalClass *cleanedIC = cleanInternalClass(newClass);
    // cleanInternalClass might have invalidated the index
    if (newClass == cleanedIC)
        return cleanedIC; // IC stayed as is, no index invalidation
    // in that case, we refetch the entry if needed
    if (entry) {
        auto updatedEntry = cleanedIC->findEntry(identifier);
        Q_ASSERT(updatedEntry); // cleanup must not remove the entry
        entry->index = updatedEntry->index;
        entry->setterIndex = updatedEntry->setterIndex;
        // entry->attributes is still valid, doesn't depend on the IC
    }
    return cleanedIC;
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4object.cpp, line 1181, as _ZN3QV411ArrayObject16virtualGetLengthEPKNS_7ManagedE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline qint64 ArrayObject::virtualGetLength(const Managed *m)
{
    const ArrayObject *a = static_cast<const ArrayObject *>(m);
    return a->propertyData(Heap::ArrayObject::LengthPropertyIndex)->toLength();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4object.cpp, line 1187, as _ZNK3QV411ArrayObject13toQStringListEv
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline QStringList ArrayObject::toQStringList() const
{
    QStringList result;

    QV4::ExecutionEngine *engine = internalClass()->engine;
    Scope scope(engine);
    ScopedValue v(scope);

    uint length = getLength();
    result.reserve(length);
    for (uint i = 0; i < length; ++i) {
        v = const_cast<ArrayObject *>(this)->get(i);
        result.append(v->toQStringNoThrow());
    }
    return result;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ArrayObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ArrayObject10__dataTestEv(QV4::ArrayObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayObject *QV4::ArrayObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZNK3QV411ArrayObject11d_uncheckedEv(
    const QV4::ArrayObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayObject *QV4::ArrayObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZNK3QV411ArrayObject1dEv(
    const QV4::ArrayObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ArrayObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ArrayObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ArrayObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::ArrayObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV411ArrayObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ArrayObject::defaultPrototype(e);
}

//  qint64 QV4::ArrayObject::virtualGetLength(const Managed *m)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV411ArrayObject16virtualGetLengthEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::ArrayObject::virtualGetLength(m);
}

//  QStringList QV4::ArrayObject::toQStringList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK3QV411ArrayObject13toQStringListEv(
    const QV4::ArrayObject *self) {
  return new QList<QString>(self->toQStringList());
}
