//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(translation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/debugger/qqmldebugserviceinterfaces.cpp, line 55, as _ZN29TranslationBindingInformation6createERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEEPKNS1_12CompiledData7BindingEP7QObjectS0_I15QQmlContextDataE
#if QT_CONFIG(translation)
inline const TranslationBindingInformation TranslationBindingInformation::create(
        const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
        const QV4::CompiledData::Binding *binding, QObject *scopeObject,
        QQmlRefPointer<QQmlContextData> ctxt)
{
    QQmlTranslation translation;
    if (binding->type() == QV4::CompiledData::Binding::Type_TranslationById) {
        const QV4::CompiledData::TranslationData data =
                compilationUnit->unitData()->translations()[binding->value.translationDataIndex];
        const QString id = compilationUnit->stringAt(data.stringIndex);
        const int n = data.number;

        translation = QQmlTranslation(QQmlTranslation::QsTrIdData(id, n));
    } else {
        Q_ASSERT(binding->type() == QV4::CompiledData::Binding::Type_Translation);

        const QV4::CompiledData::TranslationData data =
                compilationUnit->unitData()->translations()[binding->value.translationDataIndex];
        const QString text = compilationUnit->stringAt(data.stringIndex);
        const QString comment = compilationUnit->stringAt(data.commentIndex);
        const bool hasContext
                = data.contextIndex != QV4::CompiledData::TranslationData::NoContextIndex;
        const int n = data.number;

        translation = QQmlTranslation(
                    QQmlTranslation::QsTrData(
                        hasContext
                                ? compilationUnit->stringAt(data.contextIndex)
                                : QQmlTranslation::contextFromQmlFilename(
                                        compilationUnit->fileName()),
                        text, comment, n));
    }

    return { compilationUnit,
             scopeObject,
             ctxt,

             compilationUnit->stringAt(binding->propertyNameIndex),
             translation,

             binding->location.line(),
             binding->location.column() };
}
#endif  // QT_CONFIG(translation)
//  -----------------------------------------------------------------------

#if QT_CONFIG(translation)
//  const TranslationBindingInformation
//      TranslationBindingInformation::create(const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QV4::CompiledData::Binding *binding, QObject *scopeObject,
//      QQmlRefPointer<QQmlContextData> ctxt)
extern "C" Q_DECL_EXPORT
TranslationBindingInformation *ritual_ZN29TranslationBindingInformation6createERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEEPKNS1_12CompiledData7BindingEP7QObjectS0_I15QQmlContextDataE(
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QV4::CompiledData::Binding *binding,
    QObject *scopeObject,
    const QQmlRefPointer<QQmlContextData> *ctxt) {
  return new TranslationBindingInformation(
      TranslationBindingInformation::create(
          *compilationUnit,
          binding,
          scopeObject,
          *ctxt));
}
#endif  // QT_CONFIG(translation)

//  TranslationBindingInformation::~TranslationBindingInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN29TranslationBindingInformationD1Ev(
    TranslationBindingInformation *self) {
  delete self;
}

#endif  // QT_CONFIG(translation)
#endif  // !(!QT_CONFIG(qml_debug))
