//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4estable_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4estable_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4object_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 47, as _ZN3QV47ESTable5clearEv
namespace QV4 {
inline void ESTable::clear()
{
    m_size = 0;

    std::for_each(m_observers.begin(), m_observers.end(), [](ShiftObserver* ob){
        Q_ASSERT(ob);
        ob->pivot = ShiftObserver::OUT_OF_TABLE;
    });
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 59, as _ZN3QV47ESTable3setERKNS_5ValueES3_
namespace QV4 {
inline void ESTable::set(const Value &key, const Value &value)
{
    for (uint i = 0; i < m_size; ++i) {
        if (m_keys[i].sameValueZero(key)) {
            m_values[i] = value;
            return;
        }
    }

    if (m_capacity == m_size) {
        uint oldCap = m_capacity;
        m_capacity *= 2;
        m_keys = (Value*)realloc(m_keys, m_capacity * sizeof(Value));
        m_values = (Value*)realloc(m_values, m_capacity * sizeof(Value));
        memset(m_keys + oldCap, 0, m_capacity - oldCap);
        memset(m_values + oldCap, 0, m_capacity - oldCap);
    }

    Value nk = key;
    if (nk.isDouble()) {
        if (nk.doubleValue() == 0 && std::signbit(nk.doubleValue()))
            nk = Value::fromDouble(+0);
    }

    m_keys[m_size] = nk;
    m_values[m_size] = value;

    m_size++;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 90, as _ZNK3QV47ESTable3hasERKNS_5ValueE
namespace QV4 {
inline bool ESTable::has(const Value &key) const
{
    for (uint i = 0; i < m_size; ++i) {
        if (m_keys[i].sameValueZero(key))
            return true;
    }

    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 102, as _ZNK3QV47ESTable3getERKNS_5ValueEPb
namespace QV4 {
inline ReturnedValue ESTable::get(const Value &key, bool *hasValue) const
{
    for (uint i = 0; i < m_size; ++i) {
        if (m_keys[i].sameValueZero(key)) {
            if (hasValue)
                *hasValue = true;
            return m_values[i].asReturnedValue();
        }
    }

    if (hasValue)
        *hasValue = false;
    return Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 118, as _ZN3QV47ESTable6removeERKNS_5ValueE
namespace QV4 {
inline bool ESTable::remove(const Value &key)
{
    for (uint index = 0; index < m_size; ++index) {
        if (m_keys[index].sameValueZero(key)) {
            // Remove the element at |index| by moving all elements to the right
            // of |index| one place to the left.
            size_t count = (m_size - (index + 1)) * sizeof(Value);
            memmove(m_keys + index, m_keys + index + 1, count);
            memmove(m_values + index, m_values + index + 1, count);
            m_size--;

            std::for_each(m_observers.begin(), m_observers.end(), [index](ShiftObserver* ob) {
                Q_ASSERT(ob);
                if (index <= ob->pivot && ob->pivot != ShiftObserver::OUT_OF_TABLE)
                    ob->pivot = ob->pivot == 0 ? ShiftObserver::OUT_OF_TABLE : ob->pivot - 1;
            });

            return true;
        }
    }
    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 142, as _ZNK3QV47ESTable4sizeEv
namespace QV4 {
inline uint ESTable::size() const
{
    return m_size;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4estable.cpp, line 149, as _ZN3QV47ESTable7iterateEjPNS_5ValueES2_
namespace QV4 {
inline void ESTable::iterate(uint idx, Value *key, Value *value)
{
    Q_ASSERT(idx < m_size);
    Q_ASSERT(key);
    Q_ASSERT(value);
    *key = m_keys[idx];
    *value = m_values[idx];
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
//  -----------------------------------------------------------------------

//  QV4::ESTable::ESTable()
extern "C" Q_DECL_EXPORT
QV4::ESTable *ritual_ZN3QV47ESTableC1Ev() {
  return new QV4::ESTable();
}

//  QV4::ESTable::~ESTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTableD1Ev(QV4::ESTable *self) {
  delete self;
}

//  void QV4::ESTable::markObjects(MarkStack *s, bool isWeakMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable11markObjectsEPNS_9MarkStackEb(
    QV4::ESTable *self,
    QV4::MarkStack *s,
    bool isWeakMap) {
  self->markObjects(s, isWeakMap);
}

//  void QV4::ESTable::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable5clearEv(QV4::ESTable *self) {
  self->clear();
}

//  void QV4::ESTable::set(const Value &k, const Value &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable3setERKNS_5ValueES3_(
    QV4::ESTable *self,
    const QV4::Value *k,
    const QV4::Value *v) {
  self->set(*k, *v);
}

//  bool QV4::ESTable::has(const Value &k) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV47ESTable3hasERKNS_5ValueE(
    const QV4::ESTable *self,
    const QV4::Value *k) {
  return self->has(*k);
}

//  ReturnedValue QV4::ESTable::get(const Value &k, bool *hasValue) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV47ESTable3getERKNS_5ValueEPb(
    const QV4::ESTable *self,
    const QV4::Value *k,
    bool *hasValue) {
  return self->get(*k, hasValue);
}

//  bool QV4::ESTable::remove(const Value &k)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV47ESTable6removeERKNS_5ValueE(
    QV4::ESTable *self,
    const QV4::Value *k) {
  return self->remove(*k);
}

//  uint QV4::ESTable::size() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV47ESTable4sizeEv(const QV4::ESTable *self) {
  return self->size();
}

//  void QV4::ESTable::iterate(uint idx, Value *k, Value *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable7iterateEjPNS_5ValueES2_(
    QV4::ESTable *self,
    uint idx,
    QV4::Value *k,
    QV4::Value *v) {
  self->iterate(idx, k, v);
}

//  void QV4::ESTable::removeUnmarkedKeys()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable18removeUnmarkedKeysEv(QV4::ESTable *self) {
  self->removeUnmarkedKeys();
}

//  void QV4::ESTable::observeShifts(ShiftObserver &observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable13observeShiftsERNS0_13ShiftObserverE(
    QV4::ESTable *self,
    QV4::ESTable::ShiftObserver *observer) {
  self->observeShifts(*observer);
}

//  void QV4::ESTable::stopObservingShifts(ShiftObserver &observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47ESTable19stopObservingShiftsERNS0_13ShiftObserverE(
    QV4::ESTable *self,
    QV4::ESTable::ShiftObserver *observer) {
  self->stopObservingShifts(*observer);
}
