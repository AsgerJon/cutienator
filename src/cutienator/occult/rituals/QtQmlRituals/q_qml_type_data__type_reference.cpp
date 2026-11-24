//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypedata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qqmlcomponentandaliasresolver_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlirbuilder_p.h>
#include <private/qqmlirloader_p.h>
#include <private/qqmlpropertycachecreator_p.h>
#include <private/qqmlpropertyvalidator_p.h>
#include <private/qqmlscriptblob_p.h>
#include <private/qqmlscriptdata_p.h>
#include <private/qqmltypecompiler_p.h>
#include <private/qqmltypedata_p.h>
#include <private/qqmltypeloaderqmldircontent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qcryptographichash.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 26, as _ZNK12QQmlTypeData13TypeReference13qualifiedNameEv
inline QString QQmlTypeData::TypeReference::qualifiedName() const
{
    QString result;
    if (!prefix.isEmpty()) {
        result = prefix + QLatin1Char('.');
    }
    result.append(type.qmlTypeName());
    return result;
}
//  -----------------------------------------------------------------------

//  QString QQmlTypeData::TypeReference::qualifiedName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlTypeData13TypeReference13qualifiedNameEv(
    const QQmlTypeData::TypeReference *self) {
  return new QString(self->qualifiedName());
}

//  QQmlTypeData::TypeReference::~TypeReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlTypeData13TypeReferenceD1Ev(
    QQmlTypeData::TypeReference *self) {
  delete self;
}
