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

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 214, as _ZNK16QQmlTypeCompiler7importsEv
inline const QQmlImports *QQmlTypeCompiler::imports() const
{
    return typeData->imports();
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
