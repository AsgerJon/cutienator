//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

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

//  sentinel QDirListing::constEnd() const
extern "C" Q_DECL_EXPORT
QDirListing::sentinel *ritual_ZNK11QDirListing8constEndEv(
    const QDirListing *self) {
  return new QDirListing::sentinel(self->constEnd());
}
