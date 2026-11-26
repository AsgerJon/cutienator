//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <optional>
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

//  from ../qtdeclarative/src/qmlcompiler/qqmljscontextualtypes.cpp, line 88, as _ZNK6QQmlJS15ContextualTypes19fileSelectedTypeForERK7QStringS3_
namespace QQmlJS {
inline std::optional<ContextualType>
ContextualTypes::fileSelectedTypeFor(const QString &name, const QString &selector) const
{
    Q_ASSERT(!selector.isEmpty());
    for (auto [it, end] = m_fileSelectedTypes.equal_range(name); it != end; ++it) {
        if (it->fileSelector == selector)
            return it->type;
    }
    return std::nullopt;
}
}  // namespace QQmlJS
//  -----------------------------------------------------------------------

//  QQmlJS::ContextualTypes::ContextualTypes(CompileContext context, const
//      QHash<QString, ContextualType> &types, const
//      QMultiHash<QQmlJSScope::ConstPtr, QString> &names, const
//      QQmlJSScope::ConstPtr &arrayType)
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualTypes *ritual_ZN6QQmlJS15ContextualTypesC1ENS0_14CompileContextERK5QHashI7QStringNS_14ContextualTypeEERK10QMultiHashI22QDeferredSharedPointerIK11QQmlJSScopeES3_ERKSC_(
    QQmlJS::ContextualTypes::CompileContext context,
    const QHash<QString, QQmlJS::ContextualType> *types,
    const QMultiHash<QQmlJSScope::ConstPtr, QString> *names,
    const QQmlJSScope::ConstPtr *arrayType) {
  return new QQmlJS::ContextualTypes(context, *types, *names, *arrayType);
}

//  CompileContext QQmlJS::ContextualTypes::context() const
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualTypes::CompileContext ritual_ZNK6QQmlJS15ContextualTypes7contextEv(
    const QQmlJS::ContextualTypes *self) {
  return self->context();
}

//  QQmlJSScope::ConstPtr QQmlJS::ContextualTypes::arrayType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK6QQmlJS15ContextualTypes9arrayTypeEv(
    const QQmlJS::ContextualTypes *self) {
  return new QQmlJSScope::ConstPtr(self->arrayType());
}

//  bool QQmlJS::ContextualTypes::hasType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes7hasTypeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return self->hasType(*name);
}

//  ContextualType QQmlJS::ContextualTypes::type(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJS::ContextualType *ritual_ZNK6QQmlJS15ContextualTypes4typeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return new QQmlJS::ContextualType(self->type(*name));
}

//  QString QQmlJS::ContextualTypes::name(const QQmlJSScope::ConstPtr &type)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS15ContextualTypes4nameERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJS::ContextualTypes *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->name(*type));
}

//  void QQmlJS::ContextualTypes::setType(const QString &name, const
//      ContextualType &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes7setTypeERK7QStringRKNS_14ContextualTypeE(
    QQmlJS::ContextualTypes *self,
    const QString *name,
    const QQmlJS::ContextualType *type) {
  self->setType(*name, *type);
}

//  void QQmlJS::ContextualTypes::setFileSelectedType(const QString
//      &fileSelector, const QString &name, const ContextualType &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes19setFileSelectedTypeERK7QStringS3_RKNS_14ContextualTypeE(
    QQmlJS::ContextualTypes *self,
    const QString *fileSelector,
    const QString *name,
    const QQmlJS::ContextualType *type) {
  self->setFileSelectedType(*fileSelector, *name, *type);
}

//  void QQmlJS::ContextualTypes::clearType(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes9clearTypeERK7QString(
    QQmlJS::ContextualTypes *self,
    const QString *name) {
  self->clearType(*name);
}

//  bool QQmlJS::ContextualTypes::isNullType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes10isNullTypeERK7QString(
    const QQmlJS::ContextualTypes *self,
    const QString *name) {
  return self->isNullType(*name);
}

//  void QQmlJS::ContextualTypes::addTypes(const ContextualTypes &types)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes8addTypesERKS0_(
    QQmlJS::ContextualTypes *self,
    const QQmlJS::ContextualTypes *types) {
  self->addTypes(*types);
}

//  const QHash<QString, ContextualType> &QQmlJS::ContextualTypes::types()
//      const
extern "C" Q_DECL_EXPORT
const QHash<QString, QQmlJS::ContextualType> *ritual_ZNK6QQmlJS15ContextualTypes5typesEv(
    const QQmlJS::ContextualTypes *self) {
  return &(self->types());
}

//  bool QQmlJS::ContextualTypes::hasFileSelectors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS15ContextualTypes16hasFileSelectorsEv(
    const QQmlJS::ContextualTypes *self) {
  return self->hasFileSelectors();
}

//  FileSelectorInfo QQmlJS::ContextualTypes::fileSelectorInfoFor(const
//      QQmlJSScope::ConstPtr &scope) const
extern "C" Q_DECL_EXPORT
QQmlJS::FileSelectorInfo *ritual_ZNK6QQmlJS15ContextualTypes19fileSelectorInfoForERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJS::ContextualTypes *self,
    const QQmlJSScope::ConstPtr *scope) {
  return new QQmlJS::FileSelectorInfo(self->fileSelectorInfoFor(*scope));
}

//  const QMultiHash<QQmlJSScope::ConstPtr, QString>
//      &QQmlJS::ContextualTypes::names() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QQmlJSScope::ConstPtr, QString> *ritual_ZNK6QQmlJS15ContextualTypes5namesEv(
    const QQmlJS::ContextualTypes *self) {
  return &(self->names());
}

//  QString QQmlJS::ContextualTypes::currentFileSelector() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS15ContextualTypes19currentFileSelectorEv(
    const QQmlJS::ContextualTypes *self) {
  return new QString(self->currentFileSelector());
}

//  void QQmlJS::ContextualTypes::setCurrentFileSelector(const QString
//      &selector)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes22setCurrentFileSelectorERK7QString(
    QQmlJS::ContextualTypes *self,
    const QString *selector) {
  self->setCurrentFileSelector(*selector);
}

//  std::optional<ContextualType>
//      QQmlJS::ContextualTypes::fileSelectedTypeFor(const QString &name,
//      const QString &selector) const
extern "C" Q_DECL_EXPORT
std::optional<QQmlJS::ContextualType> *ritual_ZNK6QQmlJS15ContextualTypes19fileSelectedTypeForERK7QStringS3_(
    const QQmlJS::ContextualTypes *self,
    const QString *name,
    const QString *selector) {
  return new std::optional<QQmlJS::ContextualType>(
      self->fileSelectedTypeFor(
          *name,
          *selector));
}

//  void QQmlJS::ContextualTypes::clearTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypes10clearTypesEv(
    QQmlJS::ContextualTypes *self) {
  self->clearTypes();
}

//  QQmlJS::ContextualTypes::~ContextualTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS15ContextualTypesD1Ev(QQmlJS::ContextualTypes *self) {
  delete self;
}

//  a QQmlJSScope::ConstPtr a ritual of QQmlJS::ContextualTypes gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJS_ContextualTypes__QQmlJSScope_ConstPtr(
    QQmlJSScope::ConstPtr *self) {
  delete self;
}

//  a std::optional<QQmlJS::ContextualType> a ritual of
//      QQmlJS::ContextualTypes gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJS_ContextualTypes__std_optional_QQmlJS_ContextualType(
    std::optional<QQmlJS::ContextualType> *self) {
  delete self;
}
