//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datestring)
#if QT_CONFIG(datestring)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/QTime>
#include <QtCore/QStringView>

//  QTimePattern::QTimePattern(const QList<Field> &fs)
extern "C" Q_DECL_EXPORT
QTimePattern *ritual_ZN12QTimePatternC1ERK5QListIN17QtTemporalPattern13TemporalFieldEE(
    const QList<QTimePattern::Field> *fs) {
  return new QTimePattern(*fs);
}

//  QtTemporalPattern::SupportType QTimePattern::timeSupport() const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::SupportType ritual_ZNK12QTimePattern11timeSupportEv(
    const QTimePattern *self) {
  return self->timeSupport();
}

//  bool QTimePattern::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTimePattern7isValidEv(const QTimePattern *self) {
  return self->isValid();
}

//  void QTimePattern::setLocale(const QLocale &loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTimePattern9setLocaleERK7QLocale(
    QTimePattern *self,
    const QLocale *loc) {
  self->setLocale(*loc);
}

//  const QLocale &QTimePattern::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK12QTimePattern6localeEv(const QTimePattern *self) {
  return new QLocale(self->locale());
}

//  QtTemporalPattern::ParseResult<QTime> QTimePattern::parse(QStringView
//      text, QTime defaults) const
extern "C" Q_DECL_EXPORT
QtTemporalPattern::ParseResult<QTime> *ritual_ZNK12QTimePattern5parseE11QStringView5QTime(
    const QTimePattern *self,
    const QString *text,
    const QTime *defaults) {
  return new QtTemporalPattern::ParseResult<QTime>(
      self->parse(
          QStringView(*text),
          *defaults));
}

//  QString QTimePattern::serialize(const QTime &time) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QTimePattern9serializeERK5QTime(
    const QTimePattern *self,
    const QTime *time) {
  return new QString(self->serialize(*time));
}

//  QTimePattern QTimePattern::fromQtFormat(QStringView format)
extern "C" Q_DECL_EXPORT
QTimePattern *ritual_ZN12QTimePattern12fromQtFormatE11QStringView(
    const QString *format) {
  return new QTimePattern(QTimePattern::fromQtFormat(QStringView(*format)));
}

//  QTimePattern QTimePattern::forLocale(const QLocale &locale,
//      QLocale::FormatType format)
extern "C" Q_DECL_EXPORT
QTimePattern *ritual_ZN12QTimePattern9forLocaleERK7QLocaleNS0_10FormatTypeE(
    const QLocale *locale,
    QLocale::FormatType format) {
  return new QTimePattern(QTimePattern::forLocale(*locale, format));
}

//  QTimePattern::~QTimePattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTimePatternD1Ev(QTimePattern *self) {
  delete self;
}

//  a QtTemporalPattern::ParseResult<QTime> a ritual of QTimePattern gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimePattern__QtTemporalPattern_ParseResult_QTime(
    QtTemporalPattern::ParseResult<QTime> *self) {
  delete self;
}

#endif  // QT_CONFIG(datestring)
#endif  // QT_CONFIG(datestring)
