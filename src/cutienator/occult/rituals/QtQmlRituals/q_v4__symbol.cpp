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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 148, as _ZNK3QV46Symbol17descriptiveStringEv
namespace QV4 {
inline QString Symbol::descriptiveString() const
{
    return QLatin1String("Symbol(") + QStringView{toQString()}.mid(1) + QLatin1String(")");
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Symbol::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Symbol10__dataTestEv(QV4::Symbol *self) {
  self->__dataTest();
}

//  QV4::Heap::Symbol *QV4::Symbol::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZNK3QV46Symbol11d_uncheckedEv(
    const QV4::Symbol *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Symbol *QV4::Symbol::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Symbol *ritual_ZNK3QV46Symbol1dEv(const QV4::Symbol *self) {
  return self->d();
}

//  Heap::InternalClass *QV4::Symbol::defaultInternalClass(QV4::EngineBase
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV46Symbol20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::Symbol::defaultInternalClass(e);
}

//  void QV4::Symbol::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Symbol14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::Symbol::virtualDestroy(b);
}

//  QString QV4::Symbol::descriptiveString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV46Symbol17descriptiveStringEv(
    const QV4::Symbol *self) {
  return new QString(self->descriptiveString());
}
