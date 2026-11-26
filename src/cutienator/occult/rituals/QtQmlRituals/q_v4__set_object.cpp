//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4setobject_p.h>
#include <QtQml/private/qv4setiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 177, as _ZN3QV44Heap9SetObject7destroyEv
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::SetObject::destroy()
{
    delete esTable;
    esTable = 0;
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
//  -----------------------------------------------------------------------

//  void QV4::SetObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49SetObject10__dataTestEv(QV4::SetObject *self) {
  self->__dataTest();
}

//  QV4::Heap::SetObject *QV4::SetObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetObject *ritual_ZNK3QV49SetObject11d_uncheckedEv(
    const QV4::SetObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SetObject *QV4::SetObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetObject *ritual_ZNK3QV49SetObject1dEv(
    const QV4::SetObject *self) {
  return self->d();
}

//  QV4::Object *QV4::SetObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49SetObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SetObject::defaultPrototype(e);
}

//  void QV4::SetObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49SetObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::SetObject::virtualDestroy(b);
}
