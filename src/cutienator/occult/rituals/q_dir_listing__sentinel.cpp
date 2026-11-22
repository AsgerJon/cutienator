//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>

//  bool operator==(sentinel a0, sentinel a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN11QDirListing8sentinelES0_(
    const QDirListing::sentinel *a0,
    const QDirListing::sentinel *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(sentinel a0, sentinel a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN11QDirListing8sentinelES0_(
    const QDirListing::sentinel *a0,
    const QDirListing::sentinel *a1) {
  return operator!=(*a0, *a1);
}

//  QDirListing::sentinel::~sentinel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing8sentinelD1Ev(QDirListing::sentinel *self) {
  delete self;
}
