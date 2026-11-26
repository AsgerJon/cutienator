//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
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

//  from ../qtdeclarative/src/qml/compiler/qqmlirbuilder.cpp, line 421, as _ZNK5QmlIR6Signal19parameterStringListEPKN3QV48Compiler20StringTableGeneratorE
namespace QmlIR {
using namespace Qt::StringLiterals;
using namespace QQmlJS;
inline QStringList Signal::parameterStringList(const QV4::Compiler::StringTableGenerator *stringPool) const
{
    QStringList result;
    result.reserve(parameters->count);
    for (Parameter *param = parameters->first; param; param = param->next)
        result << stringPool->stringForIndex(param->nameIndex);
    return result;
}
}  // namespace QmlIR
//  -----------------------------------------------------------------------

//  QStringList QmlIR::Signal::parameterStringList(const
//      QV4::Compiler::StringTableGenerator *stringPool) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK5QmlIR6Signal19parameterStringListEPKN3QV48Compiler20StringTableGeneratorE(
    const QmlIR::Signal *self,
    const QV4::Compiler::StringTableGenerator *stringPool) {
  return new QList<QString>(self->parameterStringList(stringPool));
}

//  int QmlIR::Signal::parameterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR6Signal14parameterCountEv(const QmlIR::Signal *self) {
  return self->parameterCount();
}

//  QmlIR::Signal::~Signal()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR6SignalD1Ev(QmlIR::Signal *self) {
  delete self;
}
