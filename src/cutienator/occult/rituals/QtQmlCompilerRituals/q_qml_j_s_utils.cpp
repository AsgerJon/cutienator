//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsutils_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 5. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <optional>
#include <QtCore/QStringView>
#include <QtCore/QString>
#include <QtCore/QList>
#include <variant>

//  QString QQmlJSUtils::constRefify(QString type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils11constRefifyE7QString(const QString *type) {
  return new QString(QQmlJSUtils::constRefify(*type));
}

//  std::optional<QQmlJSMetaProperty>
//      QQmlJSUtils::changeHandlerProperty(const QQmlJSScope::ConstPtr
//      &scope, QStringView signalName)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJSMetaProperty> *ritual_ZN11QQmlJSUtils21changeHandlerPropertyERK22QDeferredSharedPointerIK11QQmlJSScopeE11QStringView(
    const QQmlJSScope::ConstPtr *scope,
    const QString *signalName) {
  return new std::optional<QQmlJSMetaProperty>(
      QQmlJSUtils::changeHandlerProperty(
          *scope,
          QStringView(*signalName)));
}

//  std::optional<QQmlJSMetaProperty>
//      QQmlJSUtils::propertyFromChangedHandler(const QQmlJSScope::ConstPtr
//      &scope, QStringView changedHandler)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJSMetaProperty> *ritual_ZN11QQmlJSUtils26propertyFromChangedHandlerERK22QDeferredSharedPointerIK11QQmlJSScopeE11QStringView(
    const QQmlJSScope::ConstPtr *scope,
    const QString *changedHandler) {
  return new std::optional<QQmlJSMetaProperty>(
      QQmlJSUtils::propertyFromChangedHandler(
          *scope,
          QStringView(*changedHandler)));
}

//  bool QQmlJSUtils::hasCompositeBase(const QQmlJSScope::ConstPtr &scope)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlJSUtils16hasCompositeBaseERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSScope::ConstPtr *scope) {
  return QQmlJSUtils::hasCompositeBase(*scope);
}

//  bool QQmlJSUtils::bindablePropertyHasDefaultAccessor(const
//      QQmlJSMetaProperty &p, PropertyAccessor accessor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlJSUtils34bindablePropertyHasDefaultAccessorERK18QQmlJSMetaPropertyNS_16PropertyAccessorE(
    const QQmlJSMetaProperty *p,
    QQmlJSUtils::PropertyAccessor accessor) {
  return QQmlJSUtils::bindablePropertyHasDefaultAccessor(*p, accessor);
}

//  ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSTypeResolver
//      *typeResolver, const QQmlJSMetaProperty &property, const
//      QQmlJSScope::ConstPtr &owner, const AliasResolutionVisitor &visitor)
extern "C" Q_DECL_EXPORT
QQmlJSUtils::ResolvedAlias *ritual_ZN11QQmlJSUtils12resolveAliasEPK18QQmlJSTypeResolverRK18QQmlJSMetaPropertyRK22QDeferredSharedPointerIK11QQmlJSScopeERKNS_22AliasResolutionVisitorE(
    const QQmlJSTypeResolver *typeResolver,
    const QQmlJSMetaProperty *property,
    const QQmlJSScope::ConstPtr *owner,
    const QQmlJSUtils::AliasResolutionVisitor *visitor) {
  return new QQmlJSUtils::ResolvedAlias(
      QQmlJSUtils::resolveAlias(
          typeResolver,
          *property,
          *owner,
          *visitor));
}

//  ResolvedAlias QQmlJSUtils::resolveAlias(const QQmlJSScopesById &idScopes,
//      const QQmlJSMetaProperty &property, const QQmlJSScope::ConstPtr
//      &owner, const AliasResolutionVisitor &visitor)
extern "C" Q_DECL_EXPORT
QQmlJSUtils::ResolvedAlias *ritual_ZN11QQmlJSUtils12resolveAliasERK16QQmlJSScopesByIdRK18QQmlJSMetaPropertyRK22QDeferredSharedPointerIK11QQmlJSScopeERKNS_22AliasResolutionVisitorE(
    const QQmlJSScopesById *idScopes,
    const QQmlJSMetaProperty *property,
    const QQmlJSScope::ConstPtr *owner,
    const QQmlJSUtils::AliasResolutionVisitor *visitor) {
  return new QQmlJSUtils::ResolvedAlias(
      QQmlJSUtils::resolveAlias(
          *idScopes,
          *property,
          *owner,
          *visitor));
}

//  std::optional<QQmlJSFixSuggestion> QQmlJSUtils::didYouMean(const QString
//      &userInput, QStringList candidates, const QString &filename, const
//      QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
std::optional<QQmlJSFixSuggestion> *ritual_ZN11QQmlJSUtils10didYouMeanERK7QString5QListIS0_ES2_RKN6QQmlJS14SourceLocationE(
    const QString *userInput,
    const QList<QString> *candidates,
    const QString *filename,
    const QQmlJS::SourceLocation *location) {
  return new std::optional<QQmlJSFixSuggestion>(
      QQmlJSUtils::didYouMean(
          *userInput,
          *candidates,
          *filename,
          *location));
}

//  std::variant<QString, QQmlJS::DiagnosticMessage>
//      QQmlJSUtils::sourceDirectoryPath(const QQmlJSImporter *importer,
//      const QString &buildDirectoryPath)
extern "C" Q_DECL_EXPORT
std::variant<QString, QQmlJS::DiagnosticMessage> *ritual_ZN11QQmlJSUtils19sourceDirectoryPathEPK14QQmlJSImporterRK7QString(
    const QQmlJSImporter *importer,
    const QString *buildDirectoryPath) {
  return new std::variant<QString, QQmlJS::DiagnosticMessage>(
      QQmlJSUtils::sourceDirectoryPath(
          importer,
          *buildDirectoryPath));
}

//  QStringList QQmlJSUtils::cleanPaths(QStringList &&paths)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QQmlJSUtils10cleanPathsEO5QListI7QStringE(
    QStringList *paths) {
  return new QList<QString>(QQmlJSUtils::cleanPaths(std::move(*paths)));
}

//  QStringList QQmlJSUtils::resourceFilesFromBuildFolders(const QStringList
//      &buildFolders)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QQmlJSUtils29resourceFilesFromBuildFoldersERK5QListI7QStringE(
    const QList<QString> *buildFolders) {
  return new QList<QString>(
      QQmlJSUtils::resourceFilesFromBuildFolders(
          *buildFolders));
}

//  QString QQmlJSUtils::qmlSourcePathFromBuildPath(const
//      QQmlJSResourceFileMapper *mapper, const QString &pathInBuildFolder)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils26qmlSourcePathFromBuildPathEPK24QQmlJSResourceFileMapperRK7QString(
    const QQmlJSResourceFileMapper *mapper,
    const QString *pathInBuildFolder) {
  return new QString(
      QQmlJSUtils::qmlSourcePathFromBuildPath(
          mapper,
          *pathInBuildFolder));
}

//  QString QQmlJSUtils::qmlBuildPathFromSourcePath(const
//      QQmlJSResourceFileMapper *mapper, const QString &pathInBuildFolder)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils26qmlBuildPathFromSourcePathEPK24QQmlJSResourceFileMapperRK7QString(
    const QQmlJSResourceFileMapper *mapper,
    const QString *pathInBuildFolder) {
  return new QString(
      QQmlJSUtils::qmlBuildPathFromSourcePath(
          mapper,
          *pathInBuildFolder));
}

//  QString QQmlJSUtils::getScopeName(const QQmlJSScope::ConstPtr &scope,
//      QQmlJSScope::ScopeType type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils12getScopeNameERK22QDeferredSharedPointerIK11QQmlJSScopeEN6QQmlSA9ScopeTypeE(
    const QQmlJSScope::ConstPtr *scope,
    QQmlJSScope::ScopeType type) {
  return new QString(QQmlJSUtils::getScopeName(*scope, type));
}

//  QString QQmlJSUtils::fileSelectorFor(const QQmlJSScope::ConstPtr &scope1)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils15fileSelectorForERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSScope::ConstPtr *scope1) {
  return new QString(QQmlJSUtils::fileSelectorFor(*scope1));
}

//  QQmlJSUtils::~QQmlJSUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSUtilsD1Ev(QQmlJSUtils *self) {
  delete self;
}

//  a std::optional<QQmlJSMetaProperty> a ritual of QQmlJSUtils gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSUtils__std_optional_QQmlJSMetaProperty(
    std::optional<QQmlJSMetaProperty> *self) {
  delete self;
}

//  a std::optional<QQmlJSFixSuggestion> a ritual of QQmlJSUtils gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSUtils__std_optional_QQmlJSFixSuggestion(
    std::optional<QQmlJSFixSuggestion> *self) {
  delete self;
}

//  a std::variant<QString, QQmlJS::DiagnosticMessage> a ritual of
//      QQmlJSUtils gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSUtils__std_variant_QString_QQmlJS_DiagnosticMessage(
    std::variant<QString, QQmlJS::DiagnosticMessage> *self) {
  delete self;
}

//  static QString QQmlJSUtils::escapeString<QString, QLatin1Char,
//      QLatin1StringView>(QString s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils12escapeStringI7QString11QLatin1Char13QLatin1StringEET_S4_(
    const QString *s) {
  return new QString(QQmlJSUtils::escapeString<QString, QLatin1Char,
      QLatin1StringView>(*s));
}

//  static QString QQmlJSUtils::toLiteral<QString, QLatin1Char,
//      QLatin1StringView>(const QString &s, QLatin1StringView ctor)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils9toLiteralI7QString11QLatin1Char13QLatin1StringEET_RKS4_T1_(
    const QString *s,
    const QLatin1StringView *ctor) {
  return new QString(QQmlJSUtils::toLiteral<QString, QLatin1Char,
      QLatin1StringView>(*s, *ctor));
}

//  static void QQmlJSUtils::deduplicate<QList<QString>>(QList<QString>
//      &container)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSUtils11deduplicateI5QListI7QStringEEEvRT_(
    QList<QString> *container) {
  QQmlJSUtils::deduplicate<QList<QString>>(*container);
}

//  static void QQmlJSUtils::deduplicate<QList<int>>(QList<int> &container)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSUtils11deduplicateI5QListIiEEEvRT_(
    QList<int> *container) {
  QQmlJSUtils::deduplicate<QList<int>>(*container);
}

//  static void QQmlJSUtils::deduplicate<QList<double>>(QList<double>
//      &container)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSUtils11deduplicateI5QListIdEEEvRT_(
    QList<double> *container) {
  QQmlJSUtils::deduplicate<QList<double>>(*container);
}
