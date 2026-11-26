//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qv4staticvalue_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4compilerscanfunctions_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QCryptographicHash>
#include <QtCore/qtyperevision.h>
#include <cmath>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/compiler/qqmlirbuilder.cpp, line 181, as _ZN5QmlIR9Parameter19stringToBuiltinTypeERK7QString
namespace QmlIR {
using namespace Qt::StringLiterals;
using namespace QQmlJS;
inline QV4::CompiledData::CommonType Parameter::stringToBuiltinType(const QString &typeName)
{
    static const struct TypeNameToType {
        const char *name;
        size_t nameLength;
        QV4::CompiledData::CommonType type;
    } propTypeNameToTypes[] = {
        { "void", strlen("void"), QV4::CompiledData::CommonType::Void },
        { "int", strlen("int"), QV4::CompiledData::CommonType::Int },
        { "bool", strlen("bool"), QV4::CompiledData::CommonType::Bool },
        { "double", strlen("double"), QV4::CompiledData::CommonType::Real },
        { "real", strlen("real"), QV4::CompiledData::CommonType::Real },
        { "string", strlen("string"), QV4::CompiledData::CommonType::String },
        { "url", strlen("url"), QV4::CompiledData::CommonType::Url },
        { "date", strlen("date"), QV4::CompiledData::CommonType::DateTime },
        { "regexp", strlen("regexp"), QV4::CompiledData::CommonType::RegExp },
        { "rect", strlen("rect"), QV4::CompiledData::CommonType::Rect },
        { "point", strlen("point"), QV4::CompiledData::CommonType::Point },
        { "size", strlen("size"), QV4::CompiledData::CommonType::Size },
        { "variant", strlen("variant"), QV4::CompiledData::CommonType::Var },
        { "var", strlen("var"), QV4::CompiledData::CommonType::Var }
    };
    static const int propTypeNameToTypesCount = sizeof(propTypeNameToTypes) /
                                                sizeof(propTypeNameToTypes[0]);

    for (int typeIndex = 0; typeIndex < propTypeNameToTypesCount; ++typeIndex) {
        const TypeNameToType *t = propTypeNameToTypes + typeIndex;
        if (typeName == QLatin1String(t->name, static_cast<int>(t->nameLength))) {
            return t->type;
        }
    }
    return QV4::CompiledData::CommonType::Invalid;
}
}  // namespace QmlIR

//  from ../qtdeclarative/src/qml/compiler/qqmlirbuilder.cpp, line 160, as _ZN5QmlIR9Parameter8initTypeEPN3QV412CompiledData13ParameterTypeERK7QStringiNS3_4FlagE
namespace QmlIR {
using namespace Qt::StringLiterals;
using namespace QQmlJS;
inline bool Parameter::initType(
        QV4::CompiledData::ParameterType *paramType,
        const QString &typeName, int typeNameIndex,
        QV4::CompiledData::ParameterType::Flag listFlag)
{
    auto builtinType = stringToBuiltinType(typeName);
    if (builtinType == QV4::CompiledData::CommonType::Invalid) {
        if (typeName.isEmpty()) {
            paramType->set(listFlag, 0);
            return false;
        }
        Q_ASSERT(quint32(typeNameIndex) < (1u << 31));
        paramType->set(listFlag, typeNameIndex);
    } else {
        Q_ASSERT(quint32(builtinType) < (1u << 31));
        paramType->set(listFlag | QV4::CompiledData::ParameterType::Common,
                       static_cast<quint32>(builtinType));
    }
    return true;
}
}  // namespace QmlIR
//  -----------------------------------------------------------------------

//  QV4::CompiledData::CommonType QmlIR::Parameter::stringToBuiltinType(const
//      QString &typeName)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CommonType ritual_ZN5QmlIR9Parameter19stringToBuiltinTypeERK7QString(
    const QString *typeName) {
  return QmlIR::Parameter::stringToBuiltinType(*typeName);
}

//  bool QmlIR::Parameter::initType(QV4::CompiledData::ParameterType
//      *paramType, const QString &typeName, int typeNameIndex,
//      QV4::CompiledData::ParameterType::Flag listFlag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QmlIR9Parameter8initTypeEPN3QV412CompiledData13ParameterTypeERK7QStringiNS3_4FlagE(
    QV4::CompiledData::ParameterType *paramType,
    const QString *typeName,
    int typeNameIndex,
    QV4::CompiledData::ParameterType::Flag listFlag) {
  return QmlIR::Parameter::initType(
      paramType,
      *typeName,
      typeNameIndex,
      listFlag);
}

//  QmlIR::Parameter::~Parameter()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR9ParameterD1Ev(QmlIR::Parameter *self) {
  delete self;
}
