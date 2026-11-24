//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qsizetype QLocaleData::DataRange::stringSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QLocaleData9DataRange10stringSizeEv(
    const QLocaleData::DataRange *self) {
  return self->stringSize();
}

//  QLocaleData::DataRange::~DataRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData9DataRangeD1Ev(QLocaleData::DataRange *self) {
  delete self;
}
