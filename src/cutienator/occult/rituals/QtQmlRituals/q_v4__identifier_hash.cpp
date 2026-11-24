//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}
//  -----------------------------------------------------------------------

//  QV4::IdentifierHash::IdentifierHash()
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV414IdentifierHashC1Ev() {
  return new QV4::IdentifierHash();
}

//  QV4::IdentifierHash::~IdentifierHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414IdentifierHashD1Ev(QV4::IdentifierHash *self) {
  delete self;
}

//  bool QV4::IdentifierHash::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414IdentifierHash7isValidEv(
    const QV4::IdentifierHash *self) {
  return self->isValid();
}
