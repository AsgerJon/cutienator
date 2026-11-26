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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4object.cpp, line 1162, as _ZN3QV44Heap11ArrayObject4initERK5QListI7QStringE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::ArrayObject::init(const QStringList &list)
{
    Object::init();
    commonInit();
    Scope scope(internalClass->engine);
    ScopedObject a(scope, this);

    // Converts a QStringList to JS.
    // The result is a new Array object with length equal to the length
    // of the QStringList, and the elements being the QStringList's
    // elements converted to JS Strings.
    int len = list.size();
    a->arrayReserve(len);
    ScopedValue v(scope);
    for (int ii = 0; ii < len; ++ii)
        a->arrayPut(ii, (v = scope.engine->newString(list.at(ii))));
    a->setArrayLengthUnchecked(len);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ArrayObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ArrayObject4initEv(QV4::Heap::ArrayObject *self) {
  self->init();
}

//  void QV4::Heap::ArrayObject::init(const QStringList &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ArrayObject4initERK5QListI7QStringE(
    QV4::Heap::ArrayObject *self,
    const QList<QString> *list) {
  self->init(*list);
}

//  void QV4::Heap::ArrayObject::commonInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ArrayObject10commonInitEv(
    QV4::Heap::ArrayObject *self) {
  self->commonInit();
}
