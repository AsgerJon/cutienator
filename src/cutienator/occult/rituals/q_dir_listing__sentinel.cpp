//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>

//  QDirListing::sentinel::~sentinel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing8sentinelD1Ev(QDirListing::sentinel *self) {
  delete self;
}
