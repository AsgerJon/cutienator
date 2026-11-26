//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignercustomparserobject_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignercustomparserobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickdesignercustomparserobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomparserobject.cpp, line 11, as _ZN26QQuickDesignerCustomParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE
inline void QQuickDesignerCustomParser::verifyBindings(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &,
        const QList<const QV4::CompiledData::Binding *> &)
{
    /* Nothing to do we accept anything */
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomparserobject.cpp, line 18, as _ZN26QQuickDesignerCustomParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE
inline void QQuickDesignerCustomParser::applyBindings(
        QObject *, const QQmlRefPointer<QV4::ExecutableCompilationUnit> &,
        const QList<const QV4::CompiledData::Binding *> &)
{
    /* Nothing to do we accept anything */
}
//  -----------------------------------------------------------------------

//  QQuickDesignerCustomParser::QQuickDesignerCustomParser()
extern "C" Q_DECL_EXPORT
QQuickDesignerCustomParser *ritual_ZN26QQuickDesignerCustomParserC1Ev() {
  return new QQuickDesignerCustomParser();
}

//  void QQuickDesignerCustomParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &props)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerCustomParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    QQuickDesignerCustomParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *props) {
  self->verifyBindings(*compilationUnit, *props);
}

//  void QQuickDesignerCustomParser::applyBindings(QObject *obj, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerCustomParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    QQuickDesignerCustomParser *self,
    QObject *obj,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->applyBindings(obj, *compilationUnit, *bindings);
}

//  QQuickDesignerCustomParser::~QQuickDesignerCustomParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerCustomParserD1Ev(
    QQuickDesignerCustomParser *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
