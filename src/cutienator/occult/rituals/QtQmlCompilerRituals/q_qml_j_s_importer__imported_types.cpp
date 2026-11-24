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

//  QQmlJSImporter::ImportedTypes::ImportedTypes(const ImportedTypes &a0)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter13ImportedTypesC1ERKS0_(
    const QQmlJSImporter::ImportedTypes *a0) {
  return new QQmlJSImporter::ImportedTypes(*a0);
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

//  bool QQmlJSImporter::ImportedTypes::isNullType(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter13ImportedTypes10isNullTypeERK7QString(
    const QQmlJSImporter::ImportedTypes *self,
    const QString *name) {
  return self->isNullType(*name);
}
