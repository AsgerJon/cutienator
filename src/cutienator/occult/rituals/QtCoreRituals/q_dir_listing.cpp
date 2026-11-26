//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QDirListing>

//  QDirListing::QDirListing(const QString &path, IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirListing *ritual_ZN11QDirListingC1ERK7QString6QFlagsINS_12IteratorFlagEE(
    const QString *path,
    int flags) {
  return new QDirListing(
      *path,
      QFlags<QDirListing::IteratorFlag>::fromInt(flags));
}

//  QDirListing::QDirListing(const QString &path, const QStringList
//      &nameFilters, IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QDirListing *ritual_ZN11QDirListingC1ERK7QStringRK5QListIS0_E6QFlagsINS_12IteratorFlagEE(
    const QString *path,
    const QList<QString> *nameFilters,
    int flags) {
  return new QDirListing(
      *path,
      *nameFilters,
      QFlags<QDirListing::IteratorFlag>::fromInt(flags));
}

//  QDirListing::QDirListing(QDirListing &&other)
extern "C" Q_DECL_EXPORT
QDirListing *ritual_ZN11QDirListingC1EOS_(QDirListing *other) {
  return new QDirListing(std::move(*other));
}

//  QDirListing &QDirListing::operator=(QDirListing &&other)
extern "C" Q_DECL_EXPORT
QDirListing *ritual_ZN11QDirListingaSEOS_(
    QDirListing *self,
    QDirListing *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QDirListing::swap(QDirListing &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing4swapERS_(QDirListing *self, QDirListing *other) {
  self->swap(*other);
}

//  QDirListing::~QDirListing()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListingD1Ev(QDirListing *self) {
  delete self;
}

//  QString QDirListing::iteratorPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDirListing12iteratorPathEv(const QDirListing *self) {
  return new QString(self->iteratorPath());
}

//  IteratorFlags QDirListing::iteratorFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QDirListing13iteratorFlagsEv(const QDirListing *self) {
  return static_cast<int>(self->iteratorFlags().toInt());
}

//  QStringList QDirListing::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QDirListing11nameFiltersEv(
    const QDirListing *self) {
  return new QList<QString>(self->nameFilters());
}

//  const_iterator QDirListing::begin() const
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZNK11QDirListing5beginEv(
    const QDirListing *self) {
  return new QDirListing::const_iterator(self->begin());
}

//  const_iterator QDirListing::cbegin() const
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZNK11QDirListing6cbeginEv(
    const QDirListing *self) {
  return new QDirListing::const_iterator(self->cbegin());
}

//  sentinel QDirListing::end() const
extern "C" Q_DECL_EXPORT
QDirListing::sentinel *ritual_ZNK11QDirListing3endEv(
    const QDirListing *self) {
  return new QDirListing::sentinel(self->end());
}

//  sentinel QDirListing::cend() const
extern "C" Q_DECL_EXPORT
QDirListing::sentinel *ritual_ZNK11QDirListing4cendEv(
    const QDirListing *self) {
  return new QDirListing::sentinel(self->cend());
}

//  const_iterator QDirListing::constBegin() const
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZNK11QDirListing10constBeginEv(
    const QDirListing *self) {
  return new QDirListing::const_iterator(self->constBegin());
}

//  sentinel QDirListing::constEnd() const
extern "C" Q_DECL_EXPORT
QDirListing::sentinel *ritual_ZNK11QDirListing8constEndEv(
    const QDirListing *self) {
  return new QDirListing::sentinel(self->constEnd());
}

//  DirEntry QDirListing::next(DirEntry a0)
extern "C" Q_DECL_EXPORT
QDirListing::DirEntry *ritual_ZN11QDirListing4nextENS_8DirEntryE(
    const QDirListing::DirEntry *a0) {
  return new QDirListing::DirEntry(QDirListing::next(*a0));
}

//  a QDirListing::const_iterator a ritual of QDirListing gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDirListing__QDirListing_const_iterator(
    QDirListing::const_iterator *self) {
  delete self;
}
