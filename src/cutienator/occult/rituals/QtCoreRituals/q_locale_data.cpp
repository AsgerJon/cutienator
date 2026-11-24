//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  float QLocaleData::convertDoubleToFloat(double d, bool *ok)
extern "C" Q_DECL_EXPORT
float ritual_ZN11QLocaleData20convertDoubleToFloatEdPb(double d, bool *ok) {
  return QLocaleData::convertDoubleToFloat(d, ok);
}

//  ParsingResult QLocaleData::validateChars(QStringView str, NumberMode
//      numMode, int decDigits, QLocale::NumberOptions number_options) const
extern "C" Q_DECL_EXPORT
QLocaleData::ParsingResult *ritual_ZNK11QLocaleData13validateCharsE11QStringViewNS_10NumberModeEi6QFlagsIN7QLocale12NumberOptionEE(
    const QLocaleData *self,
    const QString *str,
    QLocaleData::NumberMode numMode,
    int decDigits,
    int number_options) {
  return new QLocaleData::ParsingResult(
      self->validateChars(
          QStringView(*str),
          numMode,
          decDigits,
          QFlags<QLocale::NumberOption>::fromInt(number_options)));
}

//  QLocaleId QLocaleData::id() const
extern "C" Q_DECL_EXPORT
QLocaleId *ritual_ZNK11QLocaleData2idEv(const QLocaleData *self) {
  return new QLocaleId(self->id());
}

//  GroupSizes QLocaleData::groupSizes() const
extern "C" Q_DECL_EXPORT
QLocaleData::GroupSizes *ritual_ZNK11QLocaleData10groupSizesEv(
    const QLocaleData *self) {
  return new QLocaleData::GroupSizes(self->groupSizes());
}

//  DataRange QLocaleData::startListPattern() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData16startListPatternEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->startListPattern());
}

//  DataRange QLocaleData::midListPattern() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14midListPatternEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->midListPattern());
}

//  DataRange QLocaleData::endListPattern() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14endListPatternEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->endListPattern());
}

//  DataRange QLocaleData::pairListPattern() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData15pairListPatternEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->pairListPattern());
}

//  DataRange QLocaleData::listDelimit() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData11listDelimitEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->listDelimit());
}

//  DataRange QLocaleData::decimalSeparator() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData16decimalSeparatorEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->decimalSeparator());
}

//  DataRange QLocaleData::groupDelim() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData10groupDelimEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->groupDelim());
}

//  DataRange QLocaleData::percent() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData7percentEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->percent());
}

//  DataRange QLocaleData::zero() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData4zeroEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->zero());
}

//  DataRange QLocaleData::minus() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData5minusEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->minus());
}

//  DataRange QLocaleData::plus() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData4plusEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->plus());
}

//  DataRange QLocaleData::exponential() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData11exponentialEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->exponential());
}

//  DataRange QLocaleData::quoteStart() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData10quoteStartEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->quoteStart());
}

//  DataRange QLocaleData::quoteEnd() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData8quoteEndEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->quoteEnd());
}

//  DataRange QLocaleData::quoteStartAlternate() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData19quoteStartAlternateEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->quoteStartAlternate());
}

//  DataRange QLocaleData::quoteEndAlternate() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData17quoteEndAlternateEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->quoteEndAlternate());
}

//  DataRange QLocaleData::longDateFormat() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14longDateFormatEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->longDateFormat());
}

//  DataRange QLocaleData::shortDateFormat() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData15shortDateFormatEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->shortDateFormat());
}

//  DataRange QLocaleData::longTimeFormat() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14longTimeFormatEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->longTimeFormat());
}

//  DataRange QLocaleData::shortTimeFormat() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData15shortTimeFormatEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->shortTimeFormat());
}

//  DataRange QLocaleData::longDayNamesStandalone() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData22longDayNamesStandaloneEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->longDayNamesStandalone());
}

//  DataRange QLocaleData::longDayNames() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData12longDayNamesEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->longDayNames());
}

//  DataRange QLocaleData::shortDayNamesStandalone() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData23shortDayNamesStandaloneEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->shortDayNamesStandalone());
}

//  DataRange QLocaleData::shortDayNames() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData13shortDayNamesEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->shortDayNames());
}

//  DataRange QLocaleData::narrowDayNamesStandalone() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData24narrowDayNamesStandaloneEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->narrowDayNamesStandalone());
}

//  DataRange QLocaleData::narrowDayNames() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14narrowDayNamesEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->narrowDayNames());
}

//  DataRange QLocaleData::anteMeridiem() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData12anteMeridiemEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->anteMeridiem());
}

//  DataRange QLocaleData::postMeridiem() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData12postMeridiemEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->postMeridiem());
}

//  DataRange QLocaleData::byteCount() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData9byteCountEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->byteCount());
}

//  DataRange QLocaleData::byteAmountSI() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData12byteAmountSIEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->byteAmountSI());
}

//  DataRange QLocaleData::byteAmountIEC() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData13byteAmountIECEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->byteAmountIEC());
}

//  DataRange QLocaleData::currencySymbol() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14currencySymbolEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->currencySymbol());
}

//  DataRange QLocaleData::currencyDisplayName() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData19currencyDisplayNameEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->currencyDisplayName());
}

//  DataRange QLocaleData::currencyFormat() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData14currencyFormatEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->currencyFormat());
}

//  DataRange QLocaleData::currencyFormatNegative() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData22currencyFormatNegativeEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->currencyFormatNegative());
}

//  DataRange QLocaleData::endonymLanguage() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData15endonymLanguageEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->endonymLanguage());
}

//  DataRange QLocaleData::endonymTerritory() const
extern "C" Q_DECL_EXPORT
QLocaleData::DataRange *ritual_ZNK11QLocaleData16endonymTerritoryEv(
    const QLocaleData *self) {
  return new QLocaleData::DataRange(self->endonymTerritory());
}

//  QLocaleData::~QLocaleData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleDataD1Ev(QLocaleData *self) {
  delete self;
}
