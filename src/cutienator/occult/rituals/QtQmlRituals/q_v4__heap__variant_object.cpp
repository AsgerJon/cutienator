//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4variantobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantobject.cpp, line 16, as _ZN3QV44Heap13VariantObject4initEv
namespace QV4 {
inline void Heap::VariantObject::init()
{
    Object::init();
    scarceData = new ExecutionEngine::ScarceResourceData;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::VariantObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13VariantObject4initEv(
    QV4::Heap::VariantObject *self) {
  self->init();
}

//  const QVariant &QV4::Heap::VariantObject::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Heap13VariantObject4dataEv(
    const QV4::Heap::VariantObject *self) {
  return new QVariant(self->data());
}

//  QVariant &QV4::Heap::VariantObject::data()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN3QV44Heap13VariantObject4dataEv(
    QV4::Heap::VariantObject *self) {
  return &(self->data());
}

//  void QV4::Heap::VariantObject::addVmePropertyReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13VariantObject23addVmePropertyReferenceEv(
    QV4::Heap::VariantObject *self) {
  self->addVmePropertyReference();
}

//  void QV4::Heap::VariantObject::removeVmePropertyReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13VariantObject26removeVmePropertyReferenceEv(
    QV4::Heap::VariantObject *self) {
  self->removeVmePropertyReference();
}
