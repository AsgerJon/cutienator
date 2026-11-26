//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 15, as _ZN3QV44Heap6Symbol4initERK7QString
namespace QV4 {
inline void Heap::Symbol::init(const QString &s)
{
    Q_ASSERT(s.at(0) == QLatin1Char('@'));
    QString desc(s);
    StringOrSymbol::init(desc.data_ptr());
    identifier = PropertyKey::fromStringOrSymbol(internalClass->engine, this);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::Symbol::init(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Symbol4initERK7QString(
    QV4::Heap::Symbol *self,
    const QString *s) {
  self->init(*s);
}
