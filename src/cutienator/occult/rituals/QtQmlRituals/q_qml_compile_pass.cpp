//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmltypecompiler_p.h"
#include <private/qqmlobjectcreator_p.h>
#include <private/qqmlcustomparser_p.h>
#include <private/qqmlvmemetaobject_p.h>
#include <private/qqmlcomponent_p.h>
#include <private/qqmlpropertyresolver_p.h>
#include <private/qqmlcomponentandaliasresolver_p.h>
#include <private/qqmlsignalnames_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 174, as _ZNK16QQmlTypeCompiler8stringAtEi
inline QString QQmlTypeCompiler::stringAt(int idx) const
{
    return document->stringAt(idx);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 147, as _ZN16QQmlTypeCompiler11recordErrorERKN3QV412CompiledData8LocationERK7QString
inline void QQmlTypeCompiler::recordError(const QV4::CompiledData::Location &location, const QString &description)
{
    QQmlError error;
    error.setLine(qmlConvertSourceCoordinate<quint32, int>(location.line()));
    error.setColumn(qmlConvertSourceCoordinate<quint32, int>(location.column()));
    error.setDescription(description);
    error.setUrl(url());
    errors << error;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 280, as _ZN15QQmlCompilePassC1EP16QQmlTypeCompiler
inline QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)
    : compiler(typeCompiler)
{
}
//  -----------------------------------------------------------------------

//  QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)
extern "C" Q_DECL_EXPORT
QQmlCompilePass *ritual_ZN15QQmlCompilePassC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new QQmlCompilePass(typeCompiler);
}

//  QString QQmlCompilePass::stringAt(int idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlCompilePass8stringAtEi(
    const QQmlCompilePass *self,
    int idx) {
  return new QString(self->stringAt(idx));
}

//  void QQmlCompilePass::recordError(const QV4::CompiledData::Location
//      &location, const QString &description) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlCompilePass11recordErrorERKN3QV412CompiledData8LocationERK7QString(
    const QQmlCompilePass *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  self->recordError(*location, *description);
}

//  QV4::ResolvedTypeReference *QQmlCompilePass::resolvedType(int id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK15QQmlCompilePass12resolvedTypeEi(
    const QQmlCompilePass *self,
    int id) {
  return self->resolvedType(id);
}

//  QQmlCompilePass::~QQmlCompilePass()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlCompilePassD1Ev(QQmlCompilePass *self) {
  delete self;
}
