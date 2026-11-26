//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4stringiterator_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtCore/QStringList>
#include <QtQml/private/qv4runtime_p.h>
#include <cassert>
#ifndef Q_OS_WIN
#  include <time.h>
#  ifndef Q_OS_VXWORKS
#    include <sys/time.h>
#  else
#    include "qplatformdefs.h"
#  endif
#else
#  include <QtCore/qt_windows.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 46, as _ZN3QV44Heap12StringObject4initEPKNS_6StringE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::StringObject::init(const QV4::String *str)
{
    Object::init();
    string.set(internalClass->engine, str->d());
    setProperty(internalClass->engine, LengthPropertyIndex, Value::fromInt32(length()));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 53, as _ZNK3QV44Heap12StringObject8getIndexEj
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline Heap::String *Heap::StringObject::getIndex(uint index) const
{
    QString str = string->toQString();
    if (index >= (uint)str.size())
        return nullptr;
    return internalClass->engine->newString(str.mid(index, 1));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 61, as _ZNK3QV44Heap12StringObject6lengthEv
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline uint Heap::StringObject::length() const
{
    return string->length();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::StringObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12StringObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::StringObject::markObjects(b, stack);
}

//  void QV4::Heap::StringObject::init(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12StringObject4initEb(
    QV4::Heap::StringObject *self,
    bool a0) {
  self->init(a0);
}

//  void QV4::Heap::StringObject::init(const QV4::String *string)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12StringObject4initEPKNS_6StringE(
    QV4::Heap::StringObject *self,
    const QV4::String *string) {
  self->init(string);
}

//  Heap::String *QV4::Heap::StringObject::getIndex(uint index) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV44Heap12StringObject8getIndexEj(
    const QV4::Heap::StringObject *self,
    uint index) {
  return self->getIndex(index);
}

//  uint QV4::Heap::StringObject::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap12StringObject6lengthEv(
    const QV4::Heap::StringObject *self) {
  return self->length();
}

//  QV4::Heap::StringObject as the QV4::Heap::StringObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObjectData *ritual_cast_QV4_Heap_StringObject_QV4_Heap_StringObjectData(
    QV4::Heap::StringObject *self) {
  return static_cast<QV4::Heap::StringObjectData *>(self);
}
