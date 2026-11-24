//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QString QQmlJSUtils::constRefify(QString type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSUtils11constRefifyE7QString(const QString *type) {
  return new QString(QQmlJSUtils::constRefify(*type));
}

//  bool QQmlJSUtils::bindablePropertyHasDefaultAccessor(const
//      QQmlJSMetaProperty &p, PropertyAccessor accessor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlJSUtils34bindablePropertyHasDefaultAccessorERK18QQmlJSMetaPropertyNS_16PropertyAccessorE(
    const QQmlJSMetaProperty *p,
    QQmlJSUtils::PropertyAccessor accessor) {
  return QQmlJSUtils::bindablePropertyHasDefaultAccessor(*p, accessor);
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

//  QQmlJSUtils::~QQmlJSUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSUtilsD1Ev(QQmlJSUtils *self) {
  delete self;
}
