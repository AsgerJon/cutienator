//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 17, as local:qqmltypecompiler.cpp:COMPILE_EXCEPTION
#define COMPILE_EXCEPTION(token, desc) \

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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 214, as _ZNK16QQmlTypeCompiler7importsEv
inline const QQmlImports *QQmlTypeCompiler::imports() const
{
    return typeData->imports();
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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 465, as _ZN20QQmlEnumTypeResolverC1EP16QQmlTypeCompiler
inline QQmlEnumTypeResolver::QQmlEnumTypeResolver(QQmlTypeCompiler *typeCompiler)
    : QQmlCompilePass(typeCompiler)
    , qmlObjects(*typeCompiler->qmlObjects())
    , propertyCaches(typeCompiler->propertyCaches())
    , imports(typeCompiler->imports())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 473, as _ZN20QQmlEnumTypeResolver19resolveEnumBindingsEv
inline bool QQmlEnumTypeResolver::resolveEnumBindings()
{
    for (int i = 0; i < qmlObjects.size(); ++i) {
        QQmlPropertyCache::ConstPtr propertyCache = propertyCaches->at(i);
        if (!propertyCache)
            continue;
        const QmlIR::Object *obj = qmlObjects.at(i);

        QQmlPropertyResolver resolver(propertyCache);

        for (QmlIR::Binding *binding = obj->firstBinding(); binding; binding = binding->next) {
            const QV4::CompiledData::Binding::Flags bindingFlags = binding->flags();
            if (bindingFlags & QV4::CompiledData::Binding::IsSignalHandlerExpression
                    || bindingFlags & QV4::CompiledData::Binding::IsSignalHandlerObject
                    || bindingFlags & QV4::CompiledData::Binding::IsPropertyObserver)
                continue;

            if (binding->type() != QV4::CompiledData::Binding::Type_Script)
                continue;

            const QString propertyName = stringAt(binding->propertyNameIndex);
            bool notInRevision = false;
            const QQmlPropertyData *pd = resolver.property(propertyName, &notInRevision);
            if (!pd || pd->isQList())
                continue;

            if (!pd->isEnum() && pd->propType().id() != QMetaType::Int)
                continue;

            if (!tryQualifiedEnumAssignment(obj, propertyCache, pd, binding))
                return false;
        }
    }

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 510, as _ZN20QQmlEnumTypeResolver19assignEnumToBindingEPN5QmlIR7BindingE11QStringViewi
inline bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding *binding, QStringView, int enumValue)
{
    binding->setType(QV4::CompiledData::Binding::Type_Number);
    // Enum values are integers (for now). This keeps the fold independent of the constant table,
    // which is not regenerated when an ahead-of-time-compiled unit is loaded and its enum bindings
    // are folded against the run-time-resolved types.
    // TODO: Filter out long enums when we get to use them
    binding->value.resolvedEnumValue = enumValue;
    binding->setFlag(QV4::CompiledData::Binding::IsResolvedEnum);
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 522, as _ZN20QQmlEnumTypeResolver26tryQualifiedEnumAssignmentEPKN5QmlIR6ObjectERKN17QQmlPropertyCache8ConstPtrEPK16QQmlPropertyDataPNS0_7BindingE
inline bool QQmlEnumTypeResolver::tryQualifiedEnumAssignment(
        const QmlIR::Object *obj, const QQmlPropertyCache::ConstPtr &propertyCache,
        const QQmlPropertyData *prop, QmlIR::Binding *binding)
{
    bool isIntProp = (prop->propType().id() == QMetaType::Int) && !prop->isEnum();
    if (!prop->isEnum() && !isIntProp)
        return true;

    if (!prop->isWritable()
            && !(binding->hasFlag(QV4::CompiledData::Binding::InitializerForReadOnlyDeclaration))) {
        COMPILE_EXCEPTION(binding, tr("Invalid property assignment: \"%1\" is a read-only property")
                                           .arg(stringAt(binding->propertyNameIndex)));
    }

    Q_ASSERT(binding->type() == QV4::CompiledData::Binding::Type_Script);
    const QString string = compiler->bindingAsString(obj, binding->value.compiledScriptIndex);
    const int dot = QmlIR::qualifiedEnumDot(string);
    if (dot == -1)
        return true;

    int dot2 = string.indexOf(QLatin1Char('.'), dot+1);
    if (dot2 != -1 && dot2 != string.size()-1) {
        if (!string.at(dot+1).isUpper())
            return true;
        if (string.indexOf(QLatin1Char('.'), dot2+1) != -1)
            return true;
    }

    QHashedStringRef typeName(string.constData(), dot);
    const bool isQtObject = (typeName == QLatin1String("Qt"));
    const QStringView scopedEnumName = (dot2 != -1 ? QStringView{string}.mid(dot + 1, dot2 - dot - 1) : QStringView());
    // ### consider supporting scoped enums in Qt namespace
    const QStringView enumValue = QStringView{string}.mid(!isQtObject && dot2 != -1 ? dot2 + 1 : dot + 1);

    if (isIntProp) { // ### C++11 allows enums to be other integral types. Should we support other integral types here?
        // Allow enum assignment to ints.
        bool ok;
        int enumval = evaluateEnum(typeName.toString(), scopedEnumName, enumValue, &ok);
        if (ok) {
            if (!assignEnumToBinding(binding, enumValue, enumval))
                return false;
        }
        return true;
    }
    QQmlType type;
    imports->resolveType(compiler->typeLoader(), typeName, &type, nullptr, nullptr);

    if (!type.isValid() && !isQtObject)
        return true;

    int value = 0;
    bool ok = false;

    auto *tr = resolvedType(obj->inheritedTypeNameIndex);

    // When these two match, we can short cut the search, unless...
    bool useFastPath = type.isValid() && tr && tr->type() == type;
    QMetaProperty mprop;
    QMetaEnum menum;
    if (useFastPath) {
        mprop = propertyCache->firstCppMetaObject()->property(prop->coreIndex());
        menum = mprop.enumerator();
        // ...the enumerator merely comes from a related metaobject, but the enum scope does not match
        // the typename we resolved
        if (!menum.isScoped() && scopedEnumName.isEmpty() && typeName != QString::fromUtf8(menum.scope()))
            useFastPath = false;;
    }
    if (useFastPath) {
        QByteArray enumName = enumValue.toUtf8();
        if (menum.isScoped() && !scopedEnumName.isEmpty() && enumName != scopedEnumName.toUtf8())
            return true;

        if (mprop.isFlagType()) {
            value = menum.keysToValue(enumName.constData(), &ok);
        } else {
            value = menum.keyToValue(enumName.constData(), &ok);
        }
    } else {
        // Otherwise we have to search the whole type
        if (type.isValid()) {
            if (!scopedEnumName.isEmpty()) {
                value = type.scopedEnumValue(
                        compiler->typeLoader(), scopedEnumName, enumValue, &ok);
            } else {
                value = type.enumValue(compiler->typeLoader(), QHashedStringRef(enumValue), &ok);
            }
        } else {
            QByteArray enumName = enumValue.toUtf8();
            const QMetaObject *metaObject = &Qt::staticMetaObject;
            for (int ii = metaObject->enumeratorCount() - 1; !ok && ii >= 0; --ii) {
                QMetaEnum e = metaObject->enumerator(ii);
                value = e.keyToValue(enumName.constData(), &ok);
            }
        }
    }

    if (!ok)
        return true;

    return assignEnumToBinding(binding, enumValue, value);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 624, as _ZNK20QQmlEnumTypeResolver12evaluateEnumERK7QString11QStringViewS3_Pb
inline int QQmlEnumTypeResolver::evaluateEnum(const QString &scope, QStringView enumName, QStringView enumValue, bool *ok) const
{
    Q_ASSERT_X(ok, "QQmlEnumTypeResolver::evaluateEnum", "ok must not be a null pointer");
    *ok = false;

    if (scope != QLatin1String("Qt")) {
        QQmlType type;
        imports->resolveType(compiler->typeLoader(), scope, &type, nullptr, nullptr);
        if (!type.isValid())
            return -1;
        if (!enumName.isEmpty())
            return type.scopedEnumValue(compiler->typeLoader(), enumName, enumValue, ok);
        return type.enumValue(
                compiler->typeLoader(),
                QHashedStringRef(enumValue.constData(), enumValue.size()), ok);
    }

    const QMetaObject *mo = &Qt::staticMetaObject;
    int i = mo->enumeratorCount();
    const QByteArray ba = enumValue.toUtf8();
    while (i--) {
        int v = mo->enumerator(i).keyToValue(ba.constData(), ok);
        if (*ok)
            return v;
    }
    return -1;
}
//  -----------------------------------------------------------------------

//  QString QQmlEnumTypeResolver::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlEnumTypeResolver2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlEnumTypeResolver::tr(
          sourceText,
          disambiguation,
          n));
}

//  QQmlEnumTypeResolver::QQmlEnumTypeResolver(QQmlTypeCompiler
//      *typeCompiler)
extern "C" Q_DECL_EXPORT
QQmlEnumTypeResolver *ritual_ZN20QQmlEnumTypeResolverC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new QQmlEnumTypeResolver(typeCompiler);
}

//  bool QQmlEnumTypeResolver::resolveEnumBindings()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlEnumTypeResolver19resolveEnumBindingsEv(
    QQmlEnumTypeResolver *self) {
  return self->resolveEnumBindings();
}

//  bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding *binding,
//      QStringView enumName, int enumValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlEnumTypeResolver19assignEnumToBindingEPN5QmlIR7BindingE11QStringViewi(
    QQmlEnumTypeResolver *self,
    QmlIR::Binding *binding,
    const QString *enumName,
    int enumValue) {
  return self->assignEnumToBinding(
      binding,
      QStringView(*enumName),
      enumValue);
}

//  bool QQmlEnumTypeResolver::assignEnumToBinding(QmlIR::Binding *binding,
//      const QString &enumName, int enumValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlEnumTypeResolver19assignEnumToBindingEPN5QmlIR7BindingERK7QStringi(
    QQmlEnumTypeResolver *self,
    QmlIR::Binding *binding,
    const QString *enumName,
    int enumValue) {
  return self->assignEnumToBinding(binding, *enumName, enumValue);
}

//  bool QQmlEnumTypeResolver::tryQualifiedEnumAssignment(const QmlIR::Object
//      *obj, const QQmlPropertyCache::ConstPtr &propertyCache, const
//      QQmlPropertyData *prop, QmlIR::Binding *binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlEnumTypeResolver26tryQualifiedEnumAssignmentEPKN5QmlIR6ObjectERKN17QQmlPropertyCache8ConstPtrEPK16QQmlPropertyDataPNS0_7BindingE(
    QQmlEnumTypeResolver *self,
    const QmlIR::Object *obj,
    const QQmlPropertyCache::ConstPtr *propertyCache,
    const QQmlPropertyData *prop,
    QmlIR::Binding *binding) {
  return self->tryQualifiedEnumAssignment(
      obj,
      *propertyCache,
      prop,
      binding);
}

//  int QQmlEnumTypeResolver::evaluateEnum(const QString &scope, QStringView
//      enumName, QStringView enumValue, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlEnumTypeResolver12evaluateEnumERK7QString11QStringViewS3_Pb(
    const QQmlEnumTypeResolver *self,
    const QString *scope,
    const QString *enumName,
    const QString *enumValue,
    bool *ok) {
  return self->evaluateEnum(
      *scope,
      QStringView(*enumName),
      QStringView(*enumValue),
      ok);
}

//  QQmlEnumTypeResolver::~QQmlEnumTypeResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlEnumTypeResolverD1Ev(QQmlEnumTypeResolver *self) {
  delete self;
}
