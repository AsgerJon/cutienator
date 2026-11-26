//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4mapobject_p.h>
#include <QtQml/private/qv4mapiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4object_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 155, as _ZN3QV44Heap9MapObject7destroyEv
namespace QV4 {
inline void Heap::MapObject::destroy()
{
    delete esTable;
    esTable = nullptr;
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

//  void QV4::MapObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MapObject10__dataTestEv(QV4::MapObject *self) {
  self->__dataTest();
}

//  QV4::Heap::MapObject *QV4::MapObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapObject *ritual_ZNK3QV49MapObject11d_uncheckedEv(
    const QV4::MapObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MapObject *QV4::MapObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapObject *ritual_ZNK3QV49MapObject1dEv(
    const QV4::MapObject *self) {
  return self->d();
}

//  QV4::Object *QV4::MapObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49MapObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::MapObject::defaultPrototype(e);
}

//  void QV4::MapObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MapObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::MapObject::virtualDestroy(b);
}
