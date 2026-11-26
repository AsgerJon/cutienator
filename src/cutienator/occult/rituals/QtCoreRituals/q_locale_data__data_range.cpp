//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QString QLocaleData::DataRange::getData(const char16_t *table) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData9DataRange7getDataEPKDs(
    const QLocaleData::DataRange *self,
    const char16_t *table) {
  return new QString(self->getData(table));
}

//  QStringView QLocaleData::DataRange::viewData(const char16_t *table) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData9DataRange8viewDataEPKDs(
    const QLocaleData::DataRange *self,
    const char16_t *table) {
  return new QString(self->viewData(table).toString());
}

//  QString QLocaleData::DataRange::getListEntry(const char16_t *table,
//      qsizetype index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData9DataRange12getListEntryEPKDsx(
    const QLocaleData::DataRange *self,
    const char16_t *table,
    qsizetype index) {
  return new QString(self->getListEntry(table, index));
}

//  QStringView QLocaleData::DataRange::viewListEntry(const char16_t *table,
//      qsizetype index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData9DataRange13viewListEntryEPKDsx(
    const QLocaleData::DataRange *self,
    const char16_t *table,
    qsizetype index) {
  return new QString(self->viewListEntry(table, index).toString());
}

//  char32_t QLocaleData::DataRange::ucsFirst(const char16_t *table) const
extern "C" Q_DECL_EXPORT
char32_t ritual_ZNK11QLocaleData9DataRange8ucsFirstEPKDs(
    const QLocaleData::DataRange *self,
    const char16_t *table) {
  return self->ucsFirst(table);
}

//  const QChar *QLocaleData::DataRange::stringStart(const char16_t *table)
//      const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK11QLocaleData9DataRange11stringStartEPKDs(
    const QLocaleData::DataRange *self,
    const char16_t *table) {
  return self->stringStart(table);
}

//  qsizetype QLocaleData::DataRange::stringSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QLocaleData9DataRange10stringSizeEv(
    const QLocaleData::DataRange *self) {
  return self->stringSize();
}

//  DataRange QLocaleData::DataRange::listEntry(const char16_t *table,
//      qsizetype index) const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData9DataRange9listEntryEPKDsx(
    const QLocaleData::DataRange *self,
    const char16_t *table,
    qsizetype index) {
  return new QLocaleData::DataRange(self->listEntry(table, index));
}

//  QLocaleData::DataRange::~DataRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData9DataRangeD1Ev(QLocaleData::DataRange *self) {
  delete self;
}
