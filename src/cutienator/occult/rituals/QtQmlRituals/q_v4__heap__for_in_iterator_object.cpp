//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 91, as _ZN3QV44Heap19ForInIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE
namespace QV4 {
inline void Heap::ForInIteratorObject::markObjects(Heap::Base *that, MarkStack *markStack)
{
    ForInIteratorObject *o = static_cast<ForInIteratorObject *>(that);
    if (o->object)
        o->object->mark(markStack);
    if (o->current)
        o->current->mark(markStack);
    if (o->target)
        o->target->mark(markStack);
    o->workArea[0].mark(markStack);
    o->workArea[1].mark(markStack);
    Object::markObjects(that, markStack);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectiterator.cpp, line 105, as _ZN3QV44Heap19ForInIteratorObject7destroyEv
namespace QV4 {
inline void Heap::ForInIteratorObject::destroy()
{
    delete iterator;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ForInIteratorObject::init(QV4::Object *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ForInIteratorObject4initEPNS_6ObjectE(
    QV4::Heap::ForInIteratorObject *self,
    QV4::Object *o) {
  self->init(o);
}

//  void QV4::Heap::ForInIteratorObject::markObjects(Heap::Base *that,
//      MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ForInIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *that,
    QV4::MarkStack *markStack) {
  QV4::Heap::ForInIteratorObject::markObjects(that, markStack);
}

//  void QV4::Heap::ForInIteratorObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ForInIteratorObject7destroyEv(
    QV4::Heap::ForInIteratorObject *self) {
  self->destroy();
}

//  QV4::Heap::ForInIteratorObject as the QV4::Heap::ForInIteratorObjectData
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObjectData *ritual_cast_QV4_Heap_ForInIteratorObject_QV4_Heap_ForInIteratorObjectData(
    QV4::Heap::ForInIteratorObject *self) {
  return static_cast<QV4::Heap::ForInIteratorObjectData *>(self);
}
