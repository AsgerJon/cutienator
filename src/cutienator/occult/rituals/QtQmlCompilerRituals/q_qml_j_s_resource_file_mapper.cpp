//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsresourcefilemapper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsresourcefilemapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  Filter QQmlJSResourceFileMapper::allQmlJSFilter()
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper::Filter *ritual_ZN24QQmlJSResourceFileMapper14allQmlJSFilterEv() {
  return new QQmlJSResourceFileMapper::Filter(
      QQmlJSResourceFileMapper::allQmlJSFilter());
}

//  Filter QQmlJSResourceFileMapper::localFileFilter(const QString &file)
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper::Filter *ritual_ZN24QQmlJSResourceFileMapper15localFileFilterERK7QString(
    const QString *file) {
  return new QQmlJSResourceFileMapper::Filter(
      QQmlJSResourceFileMapper::localFileFilter(
          *file));
}

//  Filter QQmlJSResourceFileMapper::resourceFileFilter(const QString &file)
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper::Filter *ritual_ZN24QQmlJSResourceFileMapper18resourceFileFilterERK7QString(
    const QString *file) {
  return new QQmlJSResourceFileMapper::Filter(
      QQmlJSResourceFileMapper::resourceFileFilter(
          *file));
}

//  Filter QQmlJSResourceFileMapper::resourceQmlDirectoryFilter(const QString
//      &directory)
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper::Filter *ritual_ZN24QQmlJSResourceFileMapper26resourceQmlDirectoryFilterERK7QString(
    const QString *directory) {
  return new QQmlJSResourceFileMapper::Filter(
      QQmlJSResourceFileMapper::resourceQmlDirectoryFilter(
          *directory));
}

//  QQmlJSResourceFileMapper::QQmlJSResourceFileMapper(const QStringList
//      &resourceFiles)
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper *ritual_ZN24QQmlJSResourceFileMapperC1ERK5QListI7QStringE(
    const QList<QString> *resourceFiles) {
  return new QQmlJSResourceFileMapper(*resourceFiles);
}

//  bool QQmlJSResourceFileMapper::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJSResourceFileMapper7isEmptyEv(
    const QQmlJSResourceFileMapper *self) {
  return self->isEmpty();
}

//  bool QQmlJSResourceFileMapper::isFile(QStringView resourcePath) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlJSResourceFileMapper6isFileE11QStringView(
    const QQmlJSResourceFileMapper *self,
    const QString *resourcePath) {
  return self->isFile(QStringView(*resourcePath));
}

//  QList<Entry> QQmlJSResourceFileMapper::filter(const Filter &filter) const
extern "C" Q_DECL_EXPORT
QList<QQmlJSResourceFileMapper::Entry> *ritual_ZNK24QQmlJSResourceFileMapper6filterERKNS_6FilterE(
    const QQmlJSResourceFileMapper *self,
    const QQmlJSResourceFileMapper::Filter *filter) {
  return new QList<QQmlJSResourceFileMapper::Entry>(self->filter(*filter));
}

//  QStringList QQmlJSResourceFileMapper::filePaths(const Filter &filter)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK24QQmlJSResourceFileMapper9filePathsERKNS_6FilterE(
    const QQmlJSResourceFileMapper *self,
    const QQmlJSResourceFileMapper::Filter *filter) {
  return new QList<QString>(self->filePaths(*filter));
}

//  QStringList QQmlJSResourceFileMapper::resourcePaths(const Filter &filter)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK24QQmlJSResourceFileMapper13resourcePathsERKNS_6FilterE(
    const QQmlJSResourceFileMapper *self,
    const QQmlJSResourceFileMapper::Filter *filter) {
  return new QList<QString>(self->resourcePaths(*filter));
}

//  Entry QQmlJSResourceFileMapper::entry(const Filter &filter) const
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper::Entry *ritual_ZNK24QQmlJSResourceFileMapper5entryERKNS_6FilterE(
    const QQmlJSResourceFileMapper *self,
    const QQmlJSResourceFileMapper::Filter *filter) {
  return new QQmlJSResourceFileMapper::Entry(self->entry(*filter));
}

//  void QQmlJSResourceFileMapper::populateFromQrcFile(QFile &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJSResourceFileMapper19populateFromQrcFileER5QFile(
    QQmlJSResourceFileMapper *self,
    QFile *file) {
  self->populateFromQrcFile(*file);
}

//  QQmlJSResourceFileMapper::~QQmlJSResourceFileMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJSResourceFileMapperD1Ev(
    QQmlJSResourceFileMapper *self) {
  delete self;
}

//  a QList<QQmlJSResourceFileMapper::Entry> a ritual of
//      QQmlJSResourceFileMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSResourceFileMapper__QList_QQmlJSResourceFileMapper_Entry(
    QList<QQmlJSResourceFileMapper::Entry> *self) {
  delete self;
}
