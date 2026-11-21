//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdirlisting.h>

//  QDirListing::const_iterator::const_iterator()
extern "C" Q_DECL_EXPORT
QDirListing::const_iterator *ritual_ZN11QDirListing14const_iteratorC1Ev() {
  return new QDirListing::const_iterator();
}

//  void QDirListing::const_iterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDirListing14const_iteratorppEi(
    QDirListing::const_iterator *self,
    int a0) {
  self->operator++(a0);
}
