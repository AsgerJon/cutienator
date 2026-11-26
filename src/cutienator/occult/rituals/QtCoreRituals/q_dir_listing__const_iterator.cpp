//  Written by hand on 2026-11-25 from QtCore/qdirlisting.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its inline
//  functions are written. Not written: the constructors and
//  'operator=', which the class has only by default or as moves of
//  itself. The 'operator==' and 'operator!=' against a 'sentinel' are
//  friends of the class, written as the functions of the namespace
//  they are; the three after the first stand only where the compiler
//  has no three-way comparison, as Qt's header says.
//  Completed by hand on 2026-11-25: the inline default constructor,
//  and the destructor that frees what it gives.
#include <QtCore/qglobal.h>
#include <QtCore/qdirlisting.h>

//  QDirListing::const_iterator::const_iterator()
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZN11QDirListing14const_iteratorC1Ev() {
  return new QDirListing::const_iterator();
}

//  QDirListing::const_iterator::~const_iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing14const_iteratorD1Ev(
    QDirListing::const_iterator *self) {
  delete self;
}

//  reference QDirListing::const_iterator::operator*() const
extern "C" Q_DECL_EXPORT
const QDirListing::DirEntry *ritual_ZNK11QDirListing14const_iteratordeEv(
    const QDirListing::const_iterator *self) {
  return &(self->operator*());
}

//  pointer QDirListing::const_iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QDirListing::DirEntry *ritual_ZNK11QDirListing14const_iteratorptEv(
    const QDirListing::const_iterator *self) {
  return self->operator->();
}

//  const_iterator &QDirListing::const_iterator::operator++()
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZN11QDirListing14const_iteratorppEv(
    QDirListing::const_iterator *self) {
  return &(self->operator++());
}

//  void QDirListing::const_iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing14const_iteratorppEi(
    QDirListing::const_iterator *self,
    int a0) {
  self->operator++(a0);
}

//  bool QDirListing::const_iterator::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDirListing14const_iterator5atEndEv(
    const QDirListing::const_iterator *self) {
  return self->atEnd();
}

//  bool operator==(const const_iterator &lhs, sentinel a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QDirListing14const_iteratorENS_8sentinelE(
    const QDirListing::const_iterator *lhs,
    const QDirListing::sentinel *a0) {
  return operator==(*lhs, *a0);
}

#ifndef __cpp_impl_three_way_comparison
//  bool operator!=(const const_iterator &lhs, sentinel a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN11QDirListing14const_iteratorENS_8sentinelE(
    const QDirListing::const_iterator *lhs,
    const QDirListing::sentinel *a0) {
  return operator!=(*lhs, *a0);
}

//  bool operator==(sentinel a0, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN11QDirListing8sentinelERKNS_14const_iteratorE(
    const QDirListing::sentinel *a0,
    const QDirListing::const_iterator *rhs) {
  return operator==(*a0, *rhs);
}

//  bool operator!=(sentinel a0, const const_iterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN11QDirListing8sentinelERKNS_14const_iteratorE(
    const QDirListing::sentinel *a0,
    const QDirListing::const_iterator *rhs) {
  return operator!=(*a0, *rhs);
}
#endif  // __cpp_impl_three_way_comparison
