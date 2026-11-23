//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdiriterator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdiriterator.h>
#include <QtCore/qdir.h>
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlist.h>

//  QDirIterator::QDirIterator(const QDir &dir, IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirIterator *ritual_ZN12QDirIteratorC1ERK4QDir6QFlagsINS_12IteratorFlagEE(
    const QDir *dir,
    int flags) {
  return new QDirIterator(
      *dir,
      QFlags<QDirIterator::IteratorFlag>::fromInt(flags));
}

//  QDirIterator::QDirIterator(const QString &path, IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirIterator *ritual_ZN12QDirIteratorC1ERK7QString6QFlagsINS_12IteratorFlagEE(
    const QString *path,
    int flags) {
  return new QDirIterator(
      *path,
      QFlags<QDirIterator::IteratorFlag>::fromInt(flags));
}

//  QDirIterator::QDirIterator(const QString &path, QDir::Filters filter,
//      IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirIterator *ritual_ZN12QDirIteratorC1ERK7QString6QFlagsIN4QDir6FilterEES3_INS_12IteratorFlagEE(
    const QString *path,
    int filter,
    int flags) {
  return new QDirIterator(
      *path,
      QFlags<QDir::Filter>::fromInt(filter),
      QFlags<QDirIterator::IteratorFlag>::fromInt(flags));
}

//  QDirIterator::QDirIterator(const QString &path, const QStringList
//      &nameFilters, QDir::Filters filters, IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirIterator *ritual_ZN12QDirIteratorC1ERK7QStringRK5QListIS0_E6QFlagsIN4QDir6FilterEES7_INS_12IteratorFlagEE(
    const QString *path,
    const QList<QString> *nameFilters,
    int filters,
    int flags) {
  return new QDirIterator(
      *path,
      *nameFilters,
      QFlags<QDir::Filter>::fromInt(filters),
      QFlags<QDirIterator::IteratorFlag>::fromInt(flags));
}

//  QDirIterator::~QDirIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDirIteratorD1Ev(QDirIterator *self) {
  delete self;
}

//  QString QDirIterator::next()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QDirIterator4nextEv(QDirIterator *self) {
  return new QString(self->next());
}

//  QFileInfo QDirIterator::nextFileInfo()
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZN12QDirIterator12nextFileInfoEv(QDirIterator *self) {
  return new QFileInfo(self->nextFileInfo());
}

//  bool QDirIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDirIterator7hasNextEv(const QDirIterator *self) {
  return self->hasNext();
}

//  QString QDirIterator::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDirIterator8fileNameEv(const QDirIterator *self) {
  return new QString(self->fileName());
}

//  QString QDirIterator::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDirIterator8filePathEv(const QDirIterator *self) {
  return new QString(self->filePath());
}

//  QFileInfo QDirIterator::fileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK12QDirIterator8fileInfoEv(const QDirIterator *self) {
  return new QFileInfo(self->fileInfo());
}

//  QString QDirIterator::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDirIterator4pathEv(const QDirIterator *self) {
  return new QString(self->path());
}
