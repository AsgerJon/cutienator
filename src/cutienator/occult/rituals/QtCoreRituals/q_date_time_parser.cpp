//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcalendar.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlocale.h>
#include <QtCore/qtimezone.h>
#include <cstring>
#include <QtCore/QDateTime>
#include <QtCore/QStringView>

//  Only a class built on QDateTimeParser may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDateTimeParser : QDateTimeParser {
  using QDateTimeParser::getMinimum;
  using QDateTimeParser::getMaximum;
  using QDateTimeParser::cursorPosition;
  using QDateTimeParser::locale;
};

//  A QDateTimeParser that Python can take functions over in. Every QDateTimeParser
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(datetimeparser)
typedef QString * (*CuteQDateTimeParserCall0)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QDateTime * (*CuteQDateTimeParserCall1)(const void *, const QTimeZone *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QDateTime * (*CuteQDateTimeParserCall2)(const void *, const QTimeZone *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef int (*CuteQDateTimeParserCall3)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QLocale * (*CuteQDateTimeParserCall4)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
class CuteQDateTimeParser : public QDateTimeParser {
public:
  using QDateTimeParser::QDateTimeParser;
  CuteQDateTimeParser(const QDateTimeParser & other) : QDateTimeParser(other) {}
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser11displayTextEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser10getMinimumERK9QTimeZone")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser10getMaximumERK9QTimeZone")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser14cursorPositionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser6localeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
    return false;
  }

#if QT_CONFIG(datetimeparser)
  //  QString QDateTimeParser::displayText() const
  QString displayText() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeParserCall0 call = reinterpret_cast<CuteQDateTimeParserCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDateTimeParser::displayText();
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QDateTime QDateTimeParser::getMinimum(const QTimeZone &zone) const
  QDateTime getMinimum(const QTimeZone &zone) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeParserCall1 call = reinterpret_cast<CuteQDateTimeParserCall1>(taken[1]);
      const QDateTime * given = call(this, &zone, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeParser::getMinimum(zone);
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QDateTime QDateTimeParser::getMaximum(const QTimeZone &zone) const
  QDateTime getMaximum(const QTimeZone &zone) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateTimeParserCall2 call = reinterpret_cast<CuteQDateTimeParserCall2>(taken[2]);
      const QDateTime * given = call(this, &zone, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeParser::getMaximum(zone);
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  int QDateTimeParser::cursorPosition() const
  int cursorPosition() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateTimeParserCall3 call = reinterpret_cast<CuteQDateTimeParserCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeParser::cursorPosition();
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QLocale QDateTimeParser::locale() const
  QLocale locale() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateTimeParserCall4 call = reinterpret_cast<CuteQDateTimeParserCall4>(taken[4]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeParser::locale();
  }
#endif  // QT_CONFIG(datetimeparser)
};

//  QDateTimeParser::QDateTimeParser(QMetaType::Type t, Context ctx,
//      QCalendar cal)
extern "C" Q_DECL_EXPORT
QDateTimeParser *ritual_ZN15QDateTimeParserC1EN9QMetaType4TypeENS_7ContextE9QCalendar(
    QMetaType::Type t,
    QDateTimeParser::Context ctx,
    const QCalendar *cal) {
  return new CuteQDateTimeParser(t, ctx, *cal);
}

//  QDateTimeParser::~QDateTimeParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDateTimeParserD1Ev(QDateTimeParser *self) {
  delete self;
}

//  StateNode QDateTimeParser::parse(const QString &input, int position,
//      const QDateTime &defaultValue, bool fixup) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::StateNode *ritual_ZNK15QDateTimeParser5parseERK7QStringiRK9QDateTimeb(
    const QDateTimeParser *self,
    const QString *input,
    int position,
    const QDateTime *defaultValue,
    bool fixup) {
  return new QDateTimeParser::StateNode(
      self->parse(
          *input,
          position,
          *defaultValue,
          fixup));
}

//  bool QDateTimeParser::fromString(const QString &text, QDate *date, QTime
//      *time, int baseYear) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser10fromStringERK7QStringP5QDateP5QTimei(
    const QDateTimeParser *self,
    const QString *text,
    QDate *date,
    QTime *time,
    int baseYear) {
  return self->fromString(*text, date, time, baseYear);
}

//  bool QDateTimeParser::fromString(const QString &text, QDateTime
//      *datetime, int baseYear) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser10fromStringERK7QStringP9QDateTimei(
    const QDateTimeParser *self,
    const QString *text,
    QDateTime *datetime,
    int baseYear) {
  return self->fromString(*text, datetime, baseYear);
}

//  bool QDateTimeParser::parseFormat(QStringView format)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDateTimeParser11parseFormatE11QStringView(
    QDateTimeParser *self,
    const QString *format) {
  return self->parseFormat(QStringView(*format));
}

//  FieldInfo QDateTimeParser::fieldInfo(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser9fieldInfoEi(
    const QDateTimeParser *self,
    int index) {
  return static_cast<int>(self->fieldInfo(index).toInt());
}

//  void QDateTimeParser::setDefaultLocale(const QLocale &loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDateTimeParser16setDefaultLocaleERK7QLocale(
    QDateTimeParser *self,
    const QLocale *loc) {
  self->setDefaultLocale(*loc);
}

//  QString QDateTimeParser::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11displayTextEv(
    const QDateTimeParser *self) {
  return new QString(self->displayText());
}

//  void QDateTimeParser::setCalendar(QCalendar calendar)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDateTimeParser11setCalendarE9QCalendar(
    QDateTimeParser *self,
    const QCalendar *calendar) {
  self->setCalendar(*calendar);
}

//  int QDateTimeParser::sectionMaxSize(Section s, int count) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser14sectionMaxSizeENS_7SectionEi(
    const QDateTimeParser *self,
    QDateTimeParser::Section s,
    int count) {
  return self->sectionMaxSize(s, count);
}

//  QString QDateTimeParser::sectionText(const QString &text, int
//      sectionIndex, int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11sectionTextERK7QStringii(
    const QDateTimeParser *self,
    const QString *text,
    int sectionIndex,
    int index) {
  return new QString(self->sectionText(*text, sectionIndex, index));
}

//  StateNode QDateTimeParser::scanString(const QDateTime &defaultValue, bool
//      fixup) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::StateNode *ritual_ZNK15QDateTimeParser10scanStringERK9QDateTimeb(
    const QDateTimeParser *self,
    const QDateTime *defaultValue,
    bool fixup) {
  return new QDateTimeParser::StateNode(
      self->scanString(
          *defaultValue,
          fixup));
}

//  ParsedSection QDateTimeParser::parseSection(const QDateTime
//      &currentValue, int sectionIndex, int offset) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::ParsedSection *ritual_ZNK15QDateTimeParser12parseSectionERK9QDateTimeii(
    const QDateTimeParser *self,
    const QDateTime *currentValue,
    int sectionIndex,
    int offset) {
  return new QDateTimeParser::ParsedSection(
      self->parseSection(
          *currentValue,
          sectionIndex,
          offset));
}

//  int QDateTimeParser::findMonth(QStringView str, int monthstart, int
//      sectionIndex, int year, QString *monthName, int *used) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser9findMonthE11QStringViewiiiP7QStringPi(
    const QDateTimeParser *self,
    const QString *str,
    int monthstart,
    int sectionIndex,
    int year,
    QString *monthName,
    int *used) {
  return self->findMonth(
      QStringView(*str),
      monthstart,
      sectionIndex,
      year,
      monthName,
      used);
}

//  int QDateTimeParser::findDay(QStringView str, int intDaystart, int
//      sectionIndex, QString *dayName, int *used) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser7findDayE11QStringViewiiP7QStringPi(
    const QDateTimeParser *self,
    const QString *str,
    int intDaystart,
    int sectionIndex,
    QString *dayName,
    int *used) {
  return self->findDay(
      QStringView(*str),
      intDaystart,
      sectionIndex,
      dayName,
      used);
}

//  ParsedSection QDateTimeParser::findUtcOffset(QStringView str, int mode)
//      const
extern "C" Q_DECL_EXPORT
QDateTimeParser::ParsedSection *ritual_ZNK15QDateTimeParser13findUtcOffsetE11QStringViewi(
    const QDateTimeParser *self,
    const QString *str,
    int mode) {
  return new QDateTimeParser::ParsedSection(
      self->findUtcOffset(
          QStringView(*str),
          mode));
}

//  ParsedSection QDateTimeParser::findTimeZoneName(QStringView str, const
//      QDateTime &when) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::ParsedSection *ritual_ZNK15QDateTimeParser16findTimeZoneNameE11QStringViewRK9QDateTime(
    const QDateTimeParser *self,
    const QString *str,
    const QDateTime *when) {
  return new QDateTimeParser::ParsedSection(
      self->findTimeZoneName(
          QStringView(*str),
          *when));
}

//  ParsedSection QDateTimeParser::findTimeZone(QStringView str, const
//      QDateTime &when, int maxVal, int minVal, int mode) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::ParsedSection *ritual_ZNK15QDateTimeParser12findTimeZoneE11QStringViewRK9QDateTimeiii(
    const QDateTimeParser *self,
    const QString *str,
    const QDateTime *when,
    int maxVal,
    int minVal,
    int mode) {
  return new QDateTimeParser::ParsedSection(
      self->findTimeZone(
          QStringView(*str),
          *when,
          maxVal,
          minVal,
          mode));
}

//  AmPmFinder QDateTimeParser::findAmPm(QString &str, int index, int *used)
//      const
extern "C" Q_DECL_EXPORT
QDateTimeParser::AmPmFinder ritual_ZNK15QDateTimeParser8findAmPmER7QStringiPi(
    const QDateTimeParser *self,
    QString *str,
    int index,
    int *used) {
  return self->findAmPm(*str, index, used);
}

//  bool QDateTimeParser::potentialValue(QStringView str, int min, int max,
//      int index, const QDateTime &currentValue, int insert) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser14potentialValueE11QStringViewiiiRK9QDateTimei(
    const QDateTimeParser *self,
    const QString *str,
    int min,
    int max,
    int index,
    const QDateTime *currentValue,
    int insert) {
  return self->potentialValue(
      QStringView(*str),
      min,
      max,
      index,
      *currentValue,
      insert);
}

//  bool QDateTimeParser::potentialValue(const QString &str, int min, int
//      max, int index, const QDateTime &currentValue, int insert) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser14potentialValueERK7QStringiiiRK9QDateTimei(
    const QDateTimeParser *self,
    const QString *str,
    int min,
    int max,
    int index,
    const QDateTime *currentValue,
    int insert) {
  return self->potentialValue(*str, min, max, index, *currentValue, insert);
}

//  QString QDateTimeParser::getAmPmText(AmPm ap, Case cs) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11getAmPmTextENS_4AmPmENS_4CaseE(
    const QDateTimeParser *self,
    QDateTimeParser::AmPm ap,
    QDateTimeParser::Case cs) {
  return new QString(self->getAmPmText(ap, cs));
}

//  QDateTime QDateTimeParser::baseDate(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QDateTimeParser8baseDateERK9QTimeZone(
    const QDateTimeParser *self,
    const QTimeZone *zone) {
  return new QDateTime(self->baseDate(*zone));
}

//  int QDateTimeParser::sectionSize(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser11sectionSizeEi(
    const QDateTimeParser *self,
    int index) {
  return self->sectionSize(index);
}

//  int QDateTimeParser::sectionMaxSize(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser14sectionMaxSizeEi(
    const QDateTimeParser *self,
    int index) {
  return self->sectionMaxSize(index);
}

//  int QDateTimeParser::sectionPos(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser10sectionPosEi(
    const QDateTimeParser *self,
    int index) {
  return self->sectionPos(index);
}

//  int QDateTimeParser::sectionPos(SectionNode sn) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser10sectionPosENS_11SectionNodeE(
    const QDateTimeParser *self,
    const QDateTimeParser::SectionNode *sn) {
  return self->sectionPos(*sn);
}

//  const SectionNode &QDateTimeParser::sectionNode(int index) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::SectionNode *ritual_ZNK15QDateTimeParser11sectionNodeEi(
    const QDateTimeParser *self,
    int index) {
  return new QDateTimeParser::SectionNode(self->sectionNode(index));
}

//  Section QDateTimeParser::sectionType(int index) const
extern "C" Q_DECL_EXPORT
QDateTimeParser::Section ritual_ZNK15QDateTimeParser11sectionTypeEi(
    const QDateTimeParser *self,
    int index) {
  return self->sectionType(index);
}

//  QString QDateTimeParser::sectionText(int sectionIndex) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11sectionTextEi(
    const QDateTimeParser *self,
    int sectionIndex) {
  return new QString(self->sectionText(sectionIndex));
}

//  int QDateTimeParser::getDigit(const QDateTime &dt, int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser8getDigitERK9QDateTimei(
    const QDateTimeParser *self,
    const QDateTime *dt,
    int index) {
  return self->getDigit(*dt, index);
}

//  bool QDateTimeParser::setDigit(QDateTime &t, int index, int newval) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser8setDigitER9QDateTimeii(
    const QDateTimeParser *self,
    QDateTime *t,
    int index,
    int newval) {
  return self->setDigit(*t, index, newval);
}

//  int QDateTimeParser::absoluteMax(int index, const QDateTime &value) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser11absoluteMaxEiRK9QDateTime(
    const QDateTimeParser *self,
    int index,
    const QDateTime *value) {
  return self->absoluteMax(index, *value);
}

//  int QDateTimeParser::absoluteMin(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser11absoluteMinEi(
    const QDateTimeParser *self,
    int index) {
  return self->absoluteMin(index);
}

//  bool QDateTimeParser::skipToNextSection(int section, const QDateTime
//      &current, QStringView sectionText) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser17skipToNextSectionEiRK9QDateTime11QStringView(
    const QDateTimeParser *self,
    int section,
    const QDateTime *current,
    const QString *sectionText) {
  return self->skipToNextSection(
      section,
      *current,
      QStringView(*sectionText));
}

//  bool QDateTimeParser::skipToNextSection(int section, const QDateTime
//      &current, const QString &sectionText) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDateTimeParser17skipToNextSectionEiRK9QDateTimeRK7QString(
    const QDateTimeParser *self,
    int section,
    const QDateTime *current,
    const QString *sectionText) {
  return self->skipToNextSection(section, *current, *sectionText);
}

//  QString QDateTimeParser::stateName(State s) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser9stateNameENS_5StateE(
    const QDateTimeParser *self,
    QDateTimeParser::State s) {
  return new QString(self->stateName(s));
}

//  QDateTime QDateTimeParser::getMinimum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QDateTimeParser10getMinimumERK9QTimeZone(
    const QDateTimeParser *self,
    const QTimeZone *zone) {
  return new QDateTime(self->getMinimum(*zone));
}

//  QDateTime QDateTimeParser::getMaximum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QDateTimeParser10getMaximumERK9QTimeZone(
    const QDateTimeParser *self,
    const QTimeZone *zone) {
  return new QDateTime(self->getMaximum(*zone));
}

//  int QDateTimeParser::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser14cursorPositionEv(
    const QDateTimeParser *self) {
  return self->cursorPosition();
}

//  QLocale QDateTimeParser::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK15QDateTimeParser6localeEv(const QDateTimeParser *self) {
  return new QLocale(self->locale());
}

//  a Python function taken by a CuteQDateTimeParser, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeParser(
    QDateTimeParser *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeParser *>(self)->take(key, call);
}

//  QString QDateTimeParser::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QDateTimeParser11displayTextEv(
    const QDateTimeParser *self) {
  return new QString(self->QDateTimeParser::displayText());
}

//  QDateTime QDateTimeParser::getMinimum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_own_ZNK15QDateTimeParser10getMinimumERK9QTimeZone(
    const QDateTimeParser *self,
    const QTimeZone *zone) {
  return new QDateTime(
      static_cast<const OwnQDateTimeParser *>(self)->OwnQDateTimeParser::getMinimum(
          *zone));
}

//  QDateTime QDateTimeParser::getMaximum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_own_ZNK15QDateTimeParser10getMaximumERK9QTimeZone(
    const QDateTimeParser *self,
    const QTimeZone *zone) {
  return new QDateTime(
      static_cast<const OwnQDateTimeParser *>(self)->OwnQDateTimeParser::getMaximum(
          *zone));
}

//  int QDateTimeParser::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QDateTimeParser14cursorPositionEv(
    const QDateTimeParser *self) {
  return static_cast<const OwnQDateTimeParser *>(self)->OwnQDateTimeParser::cursorPosition();
}

//  QLocale QDateTimeParser::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_own_ZNK15QDateTimeParser6localeEv(
    const QDateTimeParser *self) {
  return new QLocale(
      static_cast<const OwnQDateTimeParser *>(self)->OwnQDateTimeParser::locale());
}

//  a QDateTimeParser::ParsedSection a ritual of QDateTimeParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDateTimeParser__QDateTimeParser_ParsedSection(
    QDateTimeParser::ParsedSection *self) {
  delete self;
}

#endif  // QT_CONFIG(datetimeparser)
#endif  // QT_CONFIG(datetimeparser)
