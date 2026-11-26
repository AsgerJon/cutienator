//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 116, as _ZN3QV412StringObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline PropertyAttributes StringObject::virtualGetOwnProperty(const Managed *m, PropertyKey id, Property *p)
{
    PropertyAttributes attributes = Object::virtualGetOwnProperty(m, id, p);
    if (attributes != Attr_Invalid)
        return attributes;

    if (id.isArrayIndex()) {
        const uint index = id.asArrayIndex();
        const auto s = static_cast<const StringObject *>(m);
        if (index < uint(s->d()->string->toQString().size())) {
            if (p)
                p->value = s->getIndex(index);
            return Attr_NotConfigurable|Attr_NotWritable;
        }
    }
    return Object::virtualGetOwnProperty(m, id, p);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::StringObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412StringObject10__dataTestEv(QV4::StringObject *self) {
  self->__dataTest();
}

//  QV4::Heap::StringObject *QV4::StringObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObject *ritual_ZNK3QV412StringObject11d_uncheckedEv(
    const QV4::StringObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::StringObject *QV4::StringObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObject *ritual_ZNK3QV412StringObject1dEv(
    const QV4::StringObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::StringObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV412StringObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::StringObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::StringObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV412StringObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::StringObject::defaultPrototype(e);
}

//  Heap::String *QV4::StringObject::getIndex(uint index) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV412StringObject8getIndexEj(
    const QV4::StringObject *self,
    uint index) {
  return self->getIndex(index);
}

//  uint QV4::StringObject::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV412StringObject6lengthEv(const QV4::StringObject *self) {
  return self->length();
}

//  PropertyAttributes QV4::StringObject::virtualGetOwnProperty(const Managed
//      *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV412StringObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::StringObject::virtualGetOwnProperty(
          m,
          *id,
          p));
}
