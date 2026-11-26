//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmlobjectcreator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 280, as _ZN15QQmlCompilePassC2EP16QQmlTypeCompiler
inline QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)
    : compiler(typeCompiler)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 219, as _ZNK16QQmlTypeCompiler10qmlObjectsEv
inline QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const
{
    return &document->objects;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 179, as _ZN16QQmlTypeCompiler14registerStringERK7QString
inline int QQmlTypeCompiler::registerString(const QString &str)
{
    return document->jsGenerator.registerString(str);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 249, as _ZNK16QQmlTypeCompiler15bindingAsStringEPKN5QmlIR6ObjectEi
inline QString QQmlTypeCompiler::bindingAsString(const QmlIR::Object *object, int scriptIndex) const
{
    return object->bindingAsString(document, scriptIndex);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 652, as _ZN29QQmlCustomParserScriptIndexerC1EP16QQmlTypeCompiler
inline QQmlCustomParserScriptIndexer::QQmlCustomParserScriptIndexer(QQmlTypeCompiler *typeCompiler)
    : QQmlCompilePass(typeCompiler)
    , qmlObjects(*typeCompiler->qmlObjects())
    , customParsers(typeCompiler->customParserCache())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 659, as _ZN29QQmlCustomParserScriptIndexer33annotateBindingsWithScriptStringsEv
inline void QQmlCustomParserScriptIndexer::annotateBindingsWithScriptStrings()
{
    scanObjectRecursively(/*root object*/0);
    for (int i = 0; i < qmlObjects.size(); ++i)
        if (qmlObjects.at(i)->flags & QV4::CompiledData::Object::IsInlineComponentRoot)
            scanObjectRecursively(i);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 667, as _ZN29QQmlCustomParserScriptIndexer21scanObjectRecursivelyEib
inline void QQmlCustomParserScriptIndexer::scanObjectRecursively(int objectIndex, bool annotateScriptBindings)
{
    const QmlIR::Object * const obj = qmlObjects.at(objectIndex);
    if (!annotateScriptBindings)
        annotateScriptBindings = customParsers.contains(obj->inheritedTypeNameIndex);
    for (QmlIR::Binding *binding = obj->firstBinding(); binding; binding = binding->next) {
        switch (binding->type()) {
        case QV4::CompiledData::Binding::Type_Script:
            if (annotateScriptBindings) {
                binding->stringIndex = compiler->registerString(
                        compiler->bindingAsString(obj, binding->value.compiledScriptIndex));
            }
            break;
        case QV4::CompiledData::Binding::Type_Object:
        case QV4::CompiledData::Binding::Type_AttachedProperty:
        case QV4::CompiledData::Binding::Type_GroupProperty:
            scanObjectRecursively(binding->value.objectIndex, annotateScriptBindings);
            break;
        default:
            break;
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlCustomParserScriptIndexer::QQmlCustomParserScriptIndexer(QQmlTypeComp
//      iler *typeCompiler)
extern "C" Q_DECL_EXPORT
QQmlCustomParserScriptIndexer *ritual_ZN29QQmlCustomParserScriptIndexerC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new QQmlCustomParserScriptIndexer(typeCompiler);
}

//  void QQmlCustomParserScriptIndexer::annotateBindingsWithScriptStrings()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlCustomParserScriptIndexer33annotateBindingsWithScriptStringsEv(
    QQmlCustomParserScriptIndexer *self) {
  self->annotateBindingsWithScriptStrings();
}

//  void QQmlCustomParserScriptIndexer::scanObjectRecursively(int
//      objectIndex, bool annotateScriptBindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlCustomParserScriptIndexer21scanObjectRecursivelyEib(
    QQmlCustomParserScriptIndexer *self,
    int objectIndex,
    bool annotateScriptBindings) {
  self->scanObjectRecursively(objectIndex, annotateScriptBindings);
}

//  QQmlCustomParserScriptIndexer::~QQmlCustomParserScriptIndexer()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlCustomParserScriptIndexerD1Ev(
    QQmlCustomParserScriptIndexer *self) {
  delete self;
}
