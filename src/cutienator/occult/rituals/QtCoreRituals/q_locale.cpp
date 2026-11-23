//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtCore/qlist.h>

//  QLocale::QLocale()
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1Ev() {
  return new QLocale();
}

//  QLocale::QLocale(const QString &name)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1ERK7QString(const QString *name) {
  return new QLocale(*name);
}

//  QLocale::QLocale(QStringView name)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1E11QStringView(const QString *name) {
  return new QLocale(QStringView(*name));
}

//  QLocale::QLocale(Language language, Territory territory)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1ENS_8LanguageENS_7CountryE(
    QLocale::Language language,
    QLocale::Territory territory) {
  return new QLocale(language, territory);
}

//  QLocale::QLocale(Language language, Script script, Territory territory)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1ENS_8LanguageENS_6ScriptENS_7CountryE(
    QLocale::Language language,
    QLocale::Script script,
    QLocale::Territory territory) {
  return new QLocale(language, script, territory);
}

//  QLocale::QLocale(const QLocale &other)
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocaleC1ERKS_(const QLocale *other) {
  return new QLocale(*other);
}

//  QLocale::~QLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLocaleD1Ev(QLocale *self) {
  delete self;
}

//  Language QLocale::language() const
extern "C" Q_DECL_EXPORT
QLocale::Language ritual_ZNK7QLocale8languageEv(const QLocale *self) {
  return self->language();
}

//  Script QLocale::script() const
extern "C" Q_DECL_EXPORT
QLocale::Script ritual_ZNK7QLocale6scriptEv(const QLocale *self) {
  return self->script();
}

//  Country QLocale::country() const
extern "C" Q_DECL_EXPORT
QLocale::Country ritual_ZNK7QLocale7countryEv(const QLocale *self) {
  return self->country();
}

//  QString QLocale::name(TagSeparator separator) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale4nameENS_12TagSeparatorE(
    const QLocale *self,
    QLocale::TagSeparator separator) {
  return new QString(self->name(separator));
}

//  QString QLocale::bcp47Name(TagSeparator separator) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale9bcp47NameENS_12TagSeparatorE(
    const QLocale *self,
    QLocale::TagSeparator separator) {
  return new QString(self->bcp47Name(separator));
}

//  QString QLocale::nativeLanguageName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale18nativeLanguageNameEv(const QLocale *self) {
  return new QString(self->nativeLanguageName());
}

//  QString QLocale::nativeTerritoryName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale19nativeTerritoryNameEv(const QLocale *self) {
  return new QString(self->nativeTerritoryName());
}

//  QString QLocale::nativeCountryName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale17nativeCountryNameEv(const QLocale *self) {
  return new QString(self->nativeCountryName());
}

//  short QLocale::toShort(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK7QLocale7toShortERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toShort(*s, ok);
}

//  ushort QLocale::toUShort(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK7QLocale8toUShortERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toUShort(*s, ok);
}

//  int QLocale::toInt(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLocale5toIntERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toInt(*s, ok);
}

//  uint QLocale::toUInt(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QLocale6toUIntERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toUInt(*s, ok);
}

//  long QLocale::toLong(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK7QLocale6toLongERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toLong(*s, ok);
}

//  ulong QLocale::toULong(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK7QLocale7toULongERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toULong(*s, ok);
}

//  qlonglong QLocale::toLongLong(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK7QLocale10toLongLongERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toLongLong(*s, ok);
}

//  qulonglong QLocale::toULongLong(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK7QLocale11toULongLongERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toULongLong(*s, ok);
}

//  float QLocale::toFloat(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QLocale7toFloatERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toFloat(*s, ok);
}

//  double QLocale::toDouble(const QString &s, bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QLocale8toDoubleERK7QStringPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toDouble(*s, ok);
}

//  short QLocale::toShort(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK7QLocale7toShortE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toShort(QStringView(*s), ok);
}

//  ushort QLocale::toUShort(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK7QLocale8toUShortE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toUShort(QStringView(*s), ok);
}

//  int QLocale::toInt(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLocale5toIntE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toInt(QStringView(*s), ok);
}

//  uint QLocale::toUInt(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QLocale6toUIntE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toUInt(QStringView(*s), ok);
}

//  long QLocale::toLong(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK7QLocale6toLongE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toLong(QStringView(*s), ok);
}

//  ulong QLocale::toULong(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK7QLocale7toULongE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toULong(QStringView(*s), ok);
}

//  qlonglong QLocale::toLongLong(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK7QLocale10toLongLongE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toLongLong(QStringView(*s), ok);
}

//  qulonglong QLocale::toULongLong(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK7QLocale11toULongLongE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toULongLong(QStringView(*s), ok);
}

//  float QLocale::toFloat(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QLocale7toFloatE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toFloat(QStringView(*s), ok);
}

//  double QLocale::toDouble(QStringView s, bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QLocale8toDoubleE11QStringViewPb(
    const QLocale *self,
    const QString *s,
    bool *ok) {
  return self->toDouble(QStringView(*s), ok);
}

//  QString QLocale::toString(qlonglong i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEx(const QLocale *self, qlonglong i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(qulonglong i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEy(const QLocale *self, qulonglong i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(long i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEl(const QLocale *self, long i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(ulong i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEm(const QLocale *self, ulong i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(short i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEs(const QLocale *self, short i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(ushort i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEt(const QLocale *self, ushort i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(int i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEi(const QLocale *self, int i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(uint i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEj(const QLocale *self, uint i) {
  return new QString(self->toString(i));
}

//  QString QLocale::toString(double f, char format, int precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEdci(
    const QLocale *self,
    double f,
    char format,
    int precision) {
  return new QString(self->toString(f, format, precision));
}

//  QString QLocale::toString(float f, char format, int precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringEfci(
    const QLocale *self,
    float f,
    char format,
    int precision) {
  return new QString(self->toString(f, format, precision));
}

//  QString QLocale::toString(QDate date, const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QDateRK7QString(
    const QLocale *self,
    const QDate *date,
    const QString *format) {
  return new QString(self->toString(*date, *format));
}

//  QString QLocale::toString(QTime time, const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QTimeRK7QString(
    const QLocale *self,
    const QTime *time,
    const QString *format) {
  return new QString(self->toString(*time, *format));
}

//  QString QLocale::toString(const QDateTime &dateTime, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringERK9QDateTimeRK7QString(
    const QLocale *self,
    const QDateTime *dateTime,
    const QString *format) {
  return new QString(self->toString(*dateTime, *format));
}

//  QString QLocale::toString(QDate date, QStringView format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QDate11QStringView(
    const QLocale *self,
    const QDate *date,
    const QString *format) {
  return new QString(self->toString(*date, QStringView(*format)));
}

//  QString QLocale::toString(QTime time, QStringView format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QTime11QStringView(
    const QLocale *self,
    const QTime *time,
    const QString *format) {
  return new QString(self->toString(*time, QStringView(*format)));
}

//  QString QLocale::toString(const QDateTime &dateTime, QStringView format)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringERK9QDateTime11QStringView(
    const QLocale *self,
    const QDateTime *dateTime,
    const QString *format) {
  return new QString(self->toString(*dateTime, QStringView(*format)));
}

//  QString QLocale::toString(QDate date, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QDateNS_10FormatTypeE(
    const QLocale *self,
    const QDate *date,
    QLocale::FormatType format) {
  return new QString(self->toString(*date, format));
}

//  QString QLocale::toString(QTime time, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QTimeNS_10FormatTypeE(
    const QLocale *self,
    const QTime *time,
    QLocale::FormatType format) {
  return new QString(self->toString(*time, format));
}

//  QString QLocale::toString(const QDateTime &dateTime, FormatType format)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringERK9QDateTimeNS_10FormatTypeE(
    const QLocale *self,
    const QDateTime *dateTime,
    QLocale::FormatType format) {
  return new QString(self->toString(*dateTime, format));
}

//  QString QLocale::toString(QDate date, QStringView format, QCalendar cal)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QDate11QStringView9QCalendar(
    const QLocale *self,
    const QDate *date,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(*date, QStringView(*format), *cal));
}

//  QString QLocale::toString(QDate date, FormatType format, QCalendar cal)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringE5QDateNS_10FormatTypeE9QCalendar(
    const QLocale *self,
    const QDate *date,
    QLocale::FormatType format,
    const QCalendar *cal) {
  return new QString(self->toString(*date, format, *cal));
}

//  QString QLocale::toString(const QDateTime &dateTime, FormatType format,
//      QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringERK9QDateTimeNS_10FormatTypeE9QCalendar(
    const QLocale *self,
    const QDateTime *dateTime,
    QLocale::FormatType format,
    const QCalendar *cal) {
  return new QString(self->toString(*dateTime, format, *cal));
}

//  QString QLocale::toString(const QDateTime &dateTime, QStringView format,
//      QCalendar cal) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale8toStringERK9QDateTime11QStringView9QCalendar(
    const QLocale *self,
    const QDateTime *dateTime,
    const QString *format,
    const QCalendar *cal) {
  return new QString(self->toString(*dateTime, QStringView(*format), *cal));
}

//  QString QLocale::dateFormat(FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale10dateFormatENS_10FormatTypeE(
    const QLocale *self,
    QLocale::FormatType format) {
  return new QString(self->dateFormat(format));
}

//  QString QLocale::timeFormat(FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale10timeFormatENS_10FormatTypeE(
    const QLocale *self,
    QLocale::FormatType format) {
  return new QString(self->timeFormat(format));
}

//  QString QLocale::dateTimeFormat(FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale14dateTimeFormatENS_10FormatTypeE(
    const QLocale *self,
    QLocale::FormatType format) {
  return new QString(self->dateTimeFormat(format));
}

//  QTime QLocale::toTime(const QString &string, FormatType a1) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK7QLocale6toTimeERK7QStringNS_10FormatTypeE(
    const QLocale *self,
    const QString *string,
    QLocale::FormatType a1) {
  return new QTime(self->toTime(*string, a1));
}

//  QTime QLocale::toTime(const QString &string, const QString &format) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK7QLocale6toTimeERK7QStringS2_(
    const QLocale *self,
    const QString *string,
    const QString *format) {
  return new QTime(self->toTime(*string, *format));
}

//  QDate QLocale::toDate(const QString &string, FormatType a1, int baseYear)
//      const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK7QLocale6toDateERK7QStringNS_10FormatTypeEi(
    const QLocale *self,
    const QString *string,
    QLocale::FormatType a1,
    int baseYear) {
  return new QDate(self->toDate(*string, a1, baseYear));
}

//  QDate QLocale::toDate(const QString &string, const QString &format, int
//      baseYear) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK7QLocale6toDateERK7QStringS2_i(
    const QLocale *self,
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDate(self->toDate(*string, *format, baseYear));
}

//  QDateTime QLocale::toDateTime(const QString &string, FormatType format,
//      int baseYear) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK7QLocale10toDateTimeERK7QStringNS_10FormatTypeEi(
    const QLocale *self,
    const QString *string,
    QLocale::FormatType format,
    int baseYear) {
  return new QDateTime(self->toDateTime(*string, format, baseYear));
}

//  QDateTime QLocale::toDateTime(const QString &string, const QString
//      &format, int baseYear) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK7QLocale10toDateTimeERK7QStringS2_i(
    const QLocale *self,
    const QString *string,
    const QString *format,
    int baseYear) {
  return new QDateTime(self->toDateTime(*string, *format, baseYear));
}

//  QDate QLocale::toDate(const QString &string, FormatType format, QCalendar
//      cal, int baseYear) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK7QLocale6toDateERK7QStringNS_10FormatTypeE9QCalendari(
    const QLocale *self,
    const QString *string,
    QLocale::FormatType format,
    const QCalendar *cal,
    int baseYear) {
  return new QDate(self->toDate(*string, format, *cal, baseYear));
}

//  QDate QLocale::toDate(const QString &string, const QString &format,
//      QCalendar cal, int baseYear) const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK7QLocale6toDateERK7QStringS2_9QCalendari(
    const QLocale *self,
    const QString *string,
    const QString *format,
    const QCalendar *cal,
    int baseYear) {
  return new QDate(self->toDate(*string, *format, *cal, baseYear));
}

//  QDateTime QLocale::toDateTime(const QString &string, FormatType format,
//      QCalendar cal, int baseYear) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK7QLocale10toDateTimeERK7QStringNS_10FormatTypeE9QCalendari(
    const QLocale *self,
    const QString *string,
    QLocale::FormatType format,
    const QCalendar *cal,
    int baseYear) {
  return new QDateTime(self->toDateTime(*string, format, *cal, baseYear));
}

//  QDateTime QLocale::toDateTime(const QString &string, const QString
//      &format, QCalendar cal, int baseYear) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK7QLocale10toDateTimeERK7QStringS2_9QCalendari(
    const QLocale *self,
    const QString *string,
    const QString *format,
    const QCalendar *cal,
    int baseYear) {
  return new QDateTime(self->toDateTime(*string, *format, *cal, baseYear));
}

//  QString QLocale::decimalPoint() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale12decimalPointEv(const QLocale *self) {
  return new QString(self->decimalPoint());
}

//  QString QLocale::groupSeparator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale14groupSeparatorEv(const QLocale *self) {
  return new QString(self->groupSeparator());
}

//  QString QLocale::percent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale7percentEv(const QLocale *self) {
  return new QString(self->percent());
}

//  QString QLocale::zeroDigit() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale9zeroDigitEv(const QLocale *self) {
  return new QString(self->zeroDigit());
}

//  QString QLocale::negativeSign() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale12negativeSignEv(const QLocale *self) {
  return new QString(self->negativeSign());
}

//  QString QLocale::positiveSign() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale12positiveSignEv(const QLocale *self) {
  return new QString(self->positiveSign());
}

//  QString QLocale::exponential() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale11exponentialEv(const QLocale *self) {
  return new QString(self->exponential());
}

//  QString QLocale::monthName(int a0, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale9monthNameEiNS_10FormatTypeE(
    const QLocale *self,
    int a0,
    QLocale::FormatType format) {
  return new QString(self->monthName(a0, format));
}

//  QString QLocale::standaloneMonthName(int a0, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale19standaloneMonthNameEiNS_10FormatTypeE(
    const QLocale *self,
    int a0,
    QLocale::FormatType format) {
  return new QString(self->standaloneMonthName(a0, format));
}

//  QString QLocale::dayName(int a0, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale7dayNameEiNS_10FormatTypeE(
    const QLocale *self,
    int a0,
    QLocale::FormatType format) {
  return new QString(self->dayName(a0, format));
}

//  QString QLocale::standaloneDayName(int a0, FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale17standaloneDayNameEiNS_10FormatTypeE(
    const QLocale *self,
    int a0,
    QLocale::FormatType format) {
  return new QString(self->standaloneDayName(a0, format));
}

//  Qt::DayOfWeek QLocale::firstDayOfWeek() const
extern "C" Q_DECL_EXPORT
Qt::DayOfWeek ritual_ZNK7QLocale14firstDayOfWeekEv(const QLocale *self) {
  return self->firstDayOfWeek();
}

//  QString QLocale::amText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale6amTextEv(const QLocale *self) {
  return new QString(self->amText());
}

//  QString QLocale::pmText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale6pmTextEv(const QLocale *self) {
  return new QString(self->pmText());
}

//  MeasurementSystem QLocale::measurementSystem() const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK7QLocale17measurementSystemEv(
    const QLocale *self) {
  return self->measurementSystem();
}

//  QLocale QLocale::collation() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK7QLocale9collationEv(const QLocale *self) {
  return new QLocale(self->collation());
}

//  Qt::LayoutDirection QLocale::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK7QLocale13textDirectionEv(
    const QLocale *self) {
  return self->textDirection();
}

//  QString QLocale::toUpper(const QString &str) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale7toUpperERK7QString(
    const QLocale *self,
    const QString *str) {
  return new QString(self->toUpper(*str));
}

//  QString QLocale::toLower(const QString &str) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale7toLowerERK7QString(
    const QLocale *self,
    const QString *str) {
  return new QString(self->toLower(*str));
}

//  QString QLocale::currencySymbol(CurrencySymbolFormat a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale14currencySymbolENS_20CurrencySymbolFormatE(
    const QLocale *self,
    QLocale::CurrencySymbolFormat a0) {
  return new QString(self->currencySymbol(a0));
}

//  QString QLocale::toCurrencyString(qlonglong a0, const QString &symbol)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringExRK7QString(
    const QLocale *self,
    qlonglong a0,
    const QString *symbol) {
  return new QString(self->toCurrencyString(a0, *symbol));
}

//  QString QLocale::toCurrencyString(qulonglong a0, const QString &symbol)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEyRK7QString(
    const QLocale *self,
    qulonglong a0,
    const QString *symbol) {
  return new QString(self->toCurrencyString(a0, *symbol));
}

//  QString QLocale::toCurrencyString(short i, const QString &symbol) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEsRK7QString(
    const QLocale *self,
    short i,
    const QString *symbol) {
  return new QString(self->toCurrencyString(i, *symbol));
}

//  QString QLocale::toCurrencyString(ushort i, const QString &symbol) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEtRK7QString(
    const QLocale *self,
    ushort i,
    const QString *symbol) {
  return new QString(self->toCurrencyString(i, *symbol));
}

//  QString QLocale::toCurrencyString(int i, const QString &symbol) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEiRK7QString(
    const QLocale *self,
    int i,
    const QString *symbol) {
  return new QString(self->toCurrencyString(i, *symbol));
}

//  QString QLocale::toCurrencyString(uint i, const QString &symbol) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEjRK7QString(
    const QLocale *self,
    uint i,
    const QString *symbol) {
  return new QString(self->toCurrencyString(i, *symbol));
}

//  QString QLocale::toCurrencyString(double a0, const QString &symbol, int
//      precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEdRK7QStringi(
    const QLocale *self,
    double a0,
    const QString *symbol,
    int precision) {
  return new QString(self->toCurrencyString(a0, *symbol, precision));
}

//  QString QLocale::toCurrencyString(float i, const QString &symbol, int
//      precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale16toCurrencyStringEfRK7QStringi(
    const QLocale *self,
    float i,
    const QString *symbol,
    int precision) {
  return new QString(self->toCurrencyString(i, *symbol, precision));
}

//  QString QLocale::formattedDataSize(qint64 bytes, int precision,
//      DataSizeFormats format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale17formattedDataSizeExi6QFlagsINS_14DataSizeFormatEE(
    const QLocale *self,
    qint64 bytes,
    int precision,
    int format) {
  return new QString(
      self->formattedDataSize(
          bytes,
          precision,
          QFlags<QLocale::DataSizeFormat>::fromInt(format)));
}

//  QStringList QLocale::uiLanguages(TagSeparator separator) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QLocale11uiLanguagesENS_12TagSeparatorE(
    const QLocale *self,
    QLocale::TagSeparator separator) {
  return new QList<QString>(self->uiLanguages(separator));
}

//  QString QLocale::languageToCode(Language language, LanguageCodeTypes
//      codeTypes)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale14languageToCodeENS_8LanguageE6QFlagsINS_16LanguageCodeTypeEE(
    QLocale::Language language,
    int codeTypes) {
  return new QString(
      QLocale::languageToCode(
          language,
          QFlags<QLocale::LanguageCodeType>::fromInt(codeTypes)));
}

//  Language QLocale::codeToLanguage(QStringView languageCode,
//      LanguageCodeTypes codeTypes)
extern "C" Q_DECL_EXPORT
QLocale::Language ritual_ZN7QLocale14codeToLanguageE11QStringView6QFlagsINS_16LanguageCodeTypeEE(
    const QString *languageCode,
    int codeTypes) {
  return QLocale::codeToLanguage(
      QStringView(*languageCode),
      QFlags<QLocale::LanguageCodeType>::fromInt(codeTypes));
}

//  QString QLocale::territoryToCode(Territory territory)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale15territoryToCodeENS_7CountryE(
    QLocale::Territory territory) {
  return new QString(QLocale::territoryToCode(territory));
}

//  QString QLocale::countryToCode(Country country)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale13countryToCodeENS_7CountryE(
    QLocale::Country country) {
  return new QString(QLocale::countryToCode(country));
}

//  Country QLocale::codeToCountry(QStringView countryCode)
extern "C" Q_DECL_EXPORT
QLocale::Country ritual_ZN7QLocale13codeToCountryE11QStringView(
    const QString *countryCode) {
  return QLocale::codeToCountry(QStringView(*countryCode));
}

//  QString QLocale::scriptToCode(Script script)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale12scriptToCodeENS_6ScriptE(
    QLocale::Script script) {
  return new QString(QLocale::scriptToCode(script));
}

//  Script QLocale::codeToScript(QStringView scriptCode)
extern "C" Q_DECL_EXPORT
QLocale::Script ritual_ZN7QLocale12codeToScriptE11QStringView(
    const QString *scriptCode) {
  return QLocale::codeToScript(QStringView(*scriptCode));
}

//  QString QLocale::languageToString(Language language)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale16languageToStringENS_8LanguageE(
    QLocale::Language language) {
  return new QString(QLocale::languageToString(language));
}

//  QString QLocale::territoryToString(Territory territory)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale17territoryToStringENS_7CountryE(
    QLocale::Territory territory) {
  return new QString(QLocale::territoryToString(territory));
}

//  QString QLocale::countryToString(Country country)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale15countryToStringENS_7CountryE(
    QLocale::Country country) {
  return new QString(QLocale::countryToString(country));
}

//  QString QLocale::scriptToString(Script script)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QLocale14scriptToStringENS_6ScriptE(
    QLocale::Script script) {
  return new QString(QLocale::scriptToString(script));
}

//  void QLocale::setDefault(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLocale10setDefaultERKS_(const QLocale *locale) {
  QLocale::setDefault(*locale);
}

//  QLocale QLocale::c()
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocale1cEv() {
  return new QLocale(QLocale::c());
}

//  QLocale QLocale::system()
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZN7QLocale6systemEv() {
  return new QLocale(QLocale::system());
}

//  QList<QLocale> QLocale::matchingLocales(QLocale::Language language,
//      QLocale::Script script, QLocale::Territory territory)
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_ZN7QLocale15matchingLocalesENS_8LanguageENS_6ScriptENS_7CountryE(
    QLocale::Language language,
    QLocale::Script script,
    QLocale::Territory territory) {
  return new QList<QLocale>(
      QLocale::matchingLocales(
          language,
          script,
          territory));
}

//  void QLocale::setNumberOptions(NumberOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QLocale16setNumberOptionsE6QFlagsINS_12NumberOptionEE(
    QLocale *self,
    int options) {
  self->setNumberOptions(QFlags<QLocale::NumberOption>::fromInt(options));
}

//  NumberOptions QLocale::numberOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QLocale13numberOptionsEv(const QLocale *self) {
  return static_cast<int>(self->numberOptions().toInt());
}

//  QString QLocale::quoteString(const QString &str, QuotationStyle style)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale11quoteStringERK7QStringNS_14QuotationStyleE(
    const QLocale *self,
    const QString *str,
    QLocale::QuotationStyle style) {
  return new QString(self->quoteString(*str, style));
}

//  QString QLocale::quoteString(QStringView str, QuotationStyle style) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale11quoteStringE11QStringViewNS_14QuotationStyleE(
    const QLocale *self,
    const QString *str,
    QLocale::QuotationStyle style) {
  return new QString(self->quoteString(QStringView(*str), style));
}

//  QString QLocale::createSeparatedList(const QStringList &strl) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QLocale19createSeparatedListERK5QListI7QStringE(
    const QLocale *self,
    const QList<QString> *strl) {
  return new QString(self->createSeparatedList(*strl));
}

//  bool QLocale::equals(const QLocale &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QLocale6equalsERKS_(
    const QLocale *self,
    const QLocale *other) {
  return self->equals(*other);
}

//  bool operator==(const QLocale &lhs, const QLocale &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QLocaleS1_(const QLocale *lhs, const QLocale *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QLocale &lhs, const QLocale &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QLocaleS1_(const QLocale *lhs, const QLocale *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QLocale>::QList()
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_list_make_QLocale() {
  return new QList<QLocale>();
}

//  void QList<QLocale>::append(const QLocale &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLocale(QList<QLocale> *self, const QLocale *element) {
  self->append(*element);
}

//  qsizetype QList<QLocale>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLocale(const QList<QLocale> *self) {
  return self->size();
}

//  const QLocale &QList<QLocale>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLocale *ritual_list_at_QLocale(
    const QList<QLocale> *self,
    long long index) {
  return new QLocale(self->at(index));
}

//  QList<QLocale>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLocale(QList<QLocale> *self) {
  delete self;
}
