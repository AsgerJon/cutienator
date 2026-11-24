//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QLocaleData::GroupSizes::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLocaleData10GroupSizes7isValidEv(
    const QLocaleData::GroupSizes *self) {
  return self->isValid();
}

//  QLocaleData::GroupSizes::~GroupSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData10GroupSizesD1Ev(QLocaleData::GroupSizes *self) {
  delete self;
}
