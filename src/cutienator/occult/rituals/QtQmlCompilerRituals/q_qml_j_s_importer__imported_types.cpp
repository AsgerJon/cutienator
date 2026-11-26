//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/private/qqmljscontextualtypes_p.h>
#include <QtQmlCompiler/private/qqmljsutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlcompiler/qqmljscontextualtypes.cpp, line 12, as _ZN6QQmlJS15ContextualTypes7setTypeERK7QStringRKNS_14ContextualTypeE
namespace QQmlJS {
inline void ContextualTypes::setType(const QString &name, const ContextualType &type)
{
    const auto it = m_types.find(name);
    auto insertName = [this, &name, &type]() {
        if (!name.startsWith(u'$')) {
            if (!m_names.contains(type.scope, name))
                m_names.insert(type.scope, name);
        }
    };
    if (const QString fileSelector = QQmlJSUtils::fileSelectorFor(type.scope);
        !fileSelector.isEmpty()) {
        setFileSelectedType(fileSelector, name, type);
        // If a non-selected variant was already added, we're done;
        // file-selected variants don't replace a main entry. Otherwise we still
        // need to add the type, in case _all_ variants use file selectors
        // this assumes that at least one file selector will actually be active
        if (it == m_types.end()) {
            m_types.insert(name, type);
            insertName();
        }
        return;
    }

    if (it == m_types.end()) {
        m_types.insert(name, type);
        insertName();
        return;
    }

    if (it->m_precedence < type.m_precedence)
        return;
    // The old scope keeps its (scope, name) link in m_names only if it remains
    // referenced via m_fileSelectedTypes for the same name.
    const QQmlJSScope::ConstPtr oldScope = it->scope;
    *it = type;
    const bool isOldScopeStillRefencedAsFileSelected = [&]() {
        for (auto [it, end] = m_fileSelectedTypes.equal_range(name); it != end; ++it) {
            if (it->type.scope == oldScope)
                return true;
        }
        return false;
    }();
    if (!isOldScopeStillRefencedAsFileSelected)
        m_names.remove(oldScope, name);
    insertName();
}
}  // namespace QQmlJS

//  from ../qtdeclarative/src/qmlcompiler/qqmljscontextualtypes.cpp, line 59, as _ZN6QQmlJS15ContextualTypes19setFileSelectedTypeERK7QStringS3_RKNS_14ContextualTypeE
namespace QQmlJS {
inline void ContextualTypes::setFileSelectedType(const QString &fileSelector, const QString &name,
                                          const ContextualType &type)
{
    auto insertName = [this, &name, &type]() {
        if (!name.startsWith(u'$')) {
            if (!m_names.contains(type.scope, name))
                m_names.insert(type.scope, name);
        }
    };

    auto [it, end] = m_fileSelectedTypes.equal_range(name);
    auto match = std::find_if(it, end, [&fileSelector](const FileSelectedType &entry) {
        return entry.fileSelector == fileSelector;
    });
    if (match == end) {
        insertName();
        m_fileSelectedTypes.insert(name, { fileSelector, type });
        return;
    }

    if (match->type.m_precedence < type.m_precedence)
        return;

    m_names.remove(type.scope, name);
    *it = { fileSelector, type };

    insertName();
}
}  // namespace QQmlJS
//  -----------------------------------------------------------------------

//  QQmlJSImporter::ImportedTypes::ImportedTypes(QQmlJS::ContextualTypes
//      &&types, QList<QQmlJS::DiagnosticMessage> &&warnings)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesC1EON6QQmlJS15ContextualTypesEO5QListINS1_17DiagnosticMessageEE(
    QQmlJS::ContextualTypes *types,
    QList<QQmlJS::DiagnosticMessage> *warnings) {
  return new QQmlJSImporter::ImportedTypes(
      std::move(*types),
      std::move(*warnings));
}

//  QQmlJSImporter::ImportedTypes::ImportedTypes(const ImportedTypes &a0)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesC1ERKS0_(
    const QQmlJSImporter::ImportedTypes *a0) {
  return new QQmlJSImporter::ImportedTypes(*a0);
}

//  QQmlJSImporter::ImportedTypes::ImportedTypes(ImportedTypes &&a0)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesC1EOS0_(
    QQmlJSImporter::ImportedTypes *a0) {
  return new QQmlJSImporter::ImportedTypes(std::move(*a0));
}

//  ImportedTypes &QQmlJSImporter::ImportedTypes::operator=(const
//      ImportedTypes &a0)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesaSERKS0_(
    QQmlJSImporter::ImportedTypes *self,
    const QQmlJSImporter::ImportedTypes *a0) {
  return &(self->operator=(*a0));
}

//  ImportedTypes &QQmlJSImporter::ImportedTypes::operator=(ImportedTypes
//      &&a0)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesaSEOS0_(
    QQmlJSImporter::ImportedTypes *self,
    QQmlJSImporter::ImportedTypes *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlJSImporter::ImportedTypes::~ImportedTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypesD1Ev(
    QQmlJSImporter::ImportedTypes *self) {
  delete self;
}

//  void QQmlJSImporter::ImportedTypes::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypes5clearEv(
    QQmlJSImporter::ImportedTypes *self) {
  self->clear();
}

//  const QQmlJS::ContextualTypes
//      &QQmlJSImporter::ImportedTypes::contextualTypes() const
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualTypes *ritual_ZNK14QQmlJSImporter13ImportedTypes15contextualTypesEv(
    const QQmlJSImporter::ImportedTypes *self) {
  return new QQmlJS::ContextualTypes(self->contextualTypes());
}

//  const QList<QQmlJS::DiagnosticMessage>
//      &QQmlJSImporter::ImportedTypes::warnings() const
extern "C" Q_DECL_EXPORT
const QList<QQmlJS::DiagnosticMessage> *ritual_ZNK14QQmlJSImporter13ImportedTypes8warningsEv(
    const QQmlJSImporter::ImportedTypes *self) {
  return &(self->warnings());
}

//  void QQmlJSImporter::ImportedTypes::setCurrentFileSelector(const QString
//      &selector)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypes22setCurrentFileSelectorERK7QString(
    QQmlJSImporter::ImportedTypes *self,
    const QString *selector) {
  self->setCurrentFileSelector(*selector);
}

//  bool QQmlJSImporter::ImportedTypes::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter13ImportedTypes7isEmptyEv(
    const QQmlJSImporter::ImportedTypes *self) {
  return self->isEmpty();
}

//  bool QQmlJSImporter::ImportedTypes::hasType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter13ImportedTypes7hasTypeERK7QString(
    const QQmlJSImporter::ImportedTypes *self,
    const QString *name) {
  return self->hasType(*name);
}

//  QQmlJS::ImportedScope<QQmlJSScope::ConstPtr>
//      QQmlJSImporter::ImportedTypes::type(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJS::ImportedScope<QQmlJSScope::ConstPtr> *ritual_ZNK14QQmlJSImporter13ImportedTypes4typeERK7QString(
    const QQmlJSImporter::ImportedTypes *self,
    const QString *name) {
  return new QQmlJS::ImportedScope<QQmlJSScope::ConstPtr>(self->type(*name));
}

//  QString QQmlJSImporter::ImportedTypes::name(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlJSImporter13ImportedTypes4nameERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSImporter::ImportedTypes *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->name(*type));
}

//  void QQmlJSImporter::ImportedTypes::setType(const QString &name, const
//      QQmlJS::ContextualType &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypes7setTypeERK7QStringRKN6QQmlJS14ContextualTypeE(
    QQmlJSImporter::ImportedTypes *self,
    const QString *name,
    const QQmlJS::ContextualType *type) {
  self->setType(*name, *type);
}

//  bool QQmlJSImporter::ImportedTypes::isNullType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter13ImportedTypes10isNullTypeERK7QString(
    const QQmlJSImporter::ImportedTypes *self,
    const QString *name) {
  return self->isNullType(*name);
}

//  const QHash<QString, QQmlJS::ContextualType>
//      &QQmlJSImporter::ImportedTypes::types() const
extern "C" Q_DECL_EXPORT
const QHash<QString, QQmlJS::ContextualType> *ritual_ZNK14QQmlJSImporter13ImportedTypes5typesEv(
    const QQmlJSImporter::ImportedTypes *self) {
  return &(self->types());
}

//  const QMultiHash<QQmlJSScope::ConstPtr, QString>
//      &QQmlJSImporter::ImportedTypes::names() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QQmlJSScope::ConstPtr, QString> *ritual_ZNK14QQmlJSImporter13ImportedTypes5namesEv(
    const QQmlJSImporter::ImportedTypes *self) {
  return &(self->names());
}

//  void QQmlJSImporter::ImportedTypes::add(ImportedTypes &&other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypes3addEOS0_(
    QQmlJSImporter::ImportedTypes *self,
    QQmlJSImporter::ImportedTypes *other) {
  self->add(std::move(*other));
}

//  void QQmlJSImporter::ImportedTypes::addWarnings(QList<QQmlJS::DiagnosticM
//      essage> &&warnings)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13ImportedTypes11addWarningsEO5QListIN6QQmlJS17DiagnosticMessageEE(
    QQmlJSImporter::ImportedTypes *self,
    QList<QQmlJS::DiagnosticMessage> *warnings) {
  self->addWarnings(std::move(*warnings));
}

//  a QQmlJS::ImportedScope<QQmlJSScope::ConstPtr> a ritual of
//      QQmlJSImporter::ImportedTypes gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter_ImportedTypes__QQmlJS_ImportedScope_QQmlJSScope_ConstPtr(
    QQmlJS::ImportedScope<QQmlJSScope::ConstPtr> *self) {
  delete self;
}
