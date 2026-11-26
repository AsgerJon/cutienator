//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4mapobject_p.h>
#include <QtQml/private/qv4mapiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 36, as _ZN3QV47ESTable11markObjectsEPNS_9MarkStackEb
namespace QV4 {
inline void ESTable::markObjects(MarkStack *s, bool isWeakMap)
{
    for (uint i = 0; i < m_size; ++i) {
        if (!isWeakMap)
            m_keys[i].mark(s);
        m_values[i].mark(s);
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 17, as _ZN3QV47ESTableC1Ev
namespace QV4 {
inline ESTable::ESTable()
    : m_capacity(8)
{
    m_keys = (Value*)malloc(m_capacity * sizeof(Value));
    m_values = (Value*)malloc(m_capacity * sizeof(Value));
    memset(m_keys, 0, m_capacity);
    memset(m_values, 0, m_capacity);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 26, as _ZN3QV47ESTableD1Ev
namespace QV4 {
inline ESTable::~ESTable()
{
    free(m_keys);
    free(m_values);
    m_size = 0;
    m_capacity = 0;
    m_keys = nullptr;
    m_values = nullptr;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 158, as _ZN3QV47ESTable18removeUnmarkedKeysEv
namespace QV4 {
inline void ESTable::removeUnmarkedKeys()
{
    uint idx = 0;
    uint toIdx = 0;
    for (; idx < m_size; ++idx) {
        Q_ASSERT(m_keys[idx].isObject());
        Object &o = static_cast<Object &>(m_keys[idx]);
        if (o.d()->isMarked()) {
            m_keys[toIdx] = m_keys[idx];
            m_values[toIdx] = m_values[idx];
            ++toIdx;
        }
    }
    m_size = toIdx;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 166, as _ZN3QV44Heap9MapObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE
namespace QV4 {
inline void Heap::MapObject::markObjects(Heap::Base *that, MarkStack *markStack)
{
    MapObject *m = static_cast<MapObject *>(that);
    m->esTable->markObjects(markStack, m->isWeakMap);
    Object::markObjects(that, markStack);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 149, as _ZN3QV44Heap9MapObject4initEv
namespace QV4 {
inline void Heap::MapObject::init()
{
    Object::init();
    esTable = new ESTable();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 155, as _ZN3QV44Heap9MapObject7destroyEv
namespace QV4 {
inline void Heap::MapObject::destroy()
{
    delete esTable;
    esTable = nullptr;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 161, as _ZN3QV44Heap9MapObject18removeUnmarkedKeysEv
namespace QV4 {
inline void Heap::MapObject::removeUnmarkedKeys()
{
    esTable->removeUnmarkedKeys();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::MapObject::markObjects(Heap::Base *that, MarkStack
//      *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9MapObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *that,
    QV4::MarkStack *markStack) {
  QV4::Heap::MapObject::markObjects(that, markStack);
}

//  void QV4::Heap::MapObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9MapObject4initEv(QV4::Heap::MapObject *self) {
  self->init();
}

//  void QV4::Heap::MapObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9MapObject7destroyEv(QV4::Heap::MapObject *self) {
  self->destroy();
}

//  void QV4::Heap::MapObject::removeUnmarkedKeys()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9MapObject18removeUnmarkedKeysEv(
    QV4::Heap::MapObject *self) {
  self->removeUnmarkedKeys();
}
