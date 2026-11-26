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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 224, as _ZN16QQmlTypeCompiler14propertyCachesEv
inline QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
{
    return &m_propertyCaches;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 219, as _ZNK16QQmlTypeCompiler10qmlObjectsEv
inline QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const
{
    return &document->objects;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 174, as _ZNK16QQmlTypeCompiler8stringAtEi
inline QString QQmlTypeCompiler::stringAt(int idx) const
{
    return document->stringAt(idx);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 691, as _ZN18QQmlAliasAnnotatorC1EP16QQmlTypeCompiler
inline QQmlAliasAnnotator::QQmlAliasAnnotator(QQmlTypeCompiler *typeCompiler)
    : QQmlCompilePass(typeCompiler)
    , qmlObjects(*typeCompiler->qmlObjects())
    , propertyCaches(typeCompiler->propertyCaches())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 698, as _ZN18QQmlAliasAnnotator25annotateBindingsToAliasesEv
inline void QQmlAliasAnnotator::annotateBindingsToAliases()
{
    for (int i = 0; i < qmlObjects.size(); ++i) {
        QQmlPropertyCache::ConstPtr propertyCache = propertyCaches->at(i);
        if (!propertyCache)
            continue;

        const QmlIR::Object *obj = qmlObjects.at(i);

        QQmlPropertyResolver resolver(propertyCache);
        const QQmlPropertyData *defaultProperty = obj->indexOfDefaultPropertyOrAlias != -1 ? propertyCache->parent()->defaultProperty() : propertyCache->defaultProperty();

        for (QmlIR::Binding *binding = obj->firstBinding(); binding; binding = binding->next) {
            if (!binding->isValueBinding())
                continue;
            bool notInRevision = false;
            const QQmlPropertyData *pd = binding->propertyNameIndex != quint32(0) ? resolver.property(stringAt(binding->propertyNameIndex), &notInRevision) : defaultProperty;
            if (pd && pd->isAlias())
                binding->setFlag(QV4::CompiledData::Binding::IsBindingToAlias);
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlAliasAnnotator::QQmlAliasAnnotator(QQmlTypeCompiler *typeCompiler)
extern "C" Q_DECL_EXPORT
QQmlAliasAnnotator *ritual_ZN18QQmlAliasAnnotatorC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new QQmlAliasAnnotator(typeCompiler);
}

//  void QQmlAliasAnnotator::annotateBindingsToAliases()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAliasAnnotator25annotateBindingsToAliasesEv(
    QQmlAliasAnnotator *self) {
  self->annotateBindingsToAliases();
}

//  QQmlAliasAnnotator::~QQmlAliasAnnotator()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAliasAnnotatorD1Ev(QQmlAliasAnnotator *self) {
  delete self;
}
