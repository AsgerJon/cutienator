//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 174, as _ZNK16QQmlTypeCompiler8stringAtEi
inline QString QQmlTypeCompiler::stringAt(int idx) const
{
    return document->stringAt(idx);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 721, as _ZN23QQmlScriptStringScannerC1EP16QQmlTypeCompiler
inline QQmlScriptStringScanner::QQmlScriptStringScanner(QQmlTypeCompiler *typeCompiler)
    : QQmlCompilePass(typeCompiler)
    , qmlObjects(*typeCompiler->qmlObjects())
    , propertyCaches(typeCompiler->propertyCaches())
{

}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 729, as _ZN23QQmlScriptStringScanner4scanEv
inline void QQmlScriptStringScanner::scan()
{
    const QMetaType scriptStringMetaType = QMetaType::fromType<QQmlScriptString>();
    for (int i = 0; i < qmlObjects.size(); ++i) {
        QQmlPropertyCache::ConstPtr propertyCache = propertyCaches->at(i);
        if (!propertyCache)
            continue;

        const QmlIR::Object *obj = qmlObjects.at(i);

        QQmlPropertyResolver resolver(propertyCache);
        const QQmlPropertyData *defaultProperty = obj->indexOfDefaultPropertyOrAlias != -1 ? propertyCache->parent()->defaultProperty() : propertyCache->defaultProperty();

        for (QmlIR::Binding *binding = obj->firstBinding(); binding; binding = binding->next) {
            if (binding->type() != QV4::CompiledData::Binding::Type_Script)
                continue;
            bool notInRevision = false;
            const QQmlPropertyData *pd = binding->propertyNameIndex != quint32(0) ? resolver.property(stringAt(binding->propertyNameIndex), &notInRevision) : defaultProperty;
            if (!pd || pd->propType() != scriptStringMetaType)
                continue;

            QString script = compiler->bindingAsString(obj, binding->value.compiledScriptIndex);
            binding->stringIndex = compiler->registerString(script);
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlScriptStringScanner::QQmlScriptStringScanner(QQmlTypeCompiler
//      *typeCompiler)
extern "C" Q_DECL_EXPORT
QQmlScriptStringScanner *ritual_ZN23QQmlScriptStringScannerC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new QQmlScriptStringScanner(typeCompiler);
}

//  void QQmlScriptStringScanner::scan()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlScriptStringScanner4scanEv(
    QQmlScriptStringScanner *self) {
  self->scan();
}

//  QQmlScriptStringScanner::~QQmlScriptStringScanner()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlScriptStringScannerD1Ev(QQmlScriptStringScanner *self) {
  delete self;
}
