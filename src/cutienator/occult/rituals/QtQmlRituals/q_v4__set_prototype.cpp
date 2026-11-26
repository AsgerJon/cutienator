//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4object_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------
