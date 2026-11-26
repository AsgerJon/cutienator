//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_locale)
#if QT_CONFIG(qml_locale)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmllocale_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qtimezone.h>
#include <QtCore/private/qlocale_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmllocale.cpp, line 503, as local:qqmllocale.cpp:qtDayToQmlDay
static QQmlLocale::DayOfWeek qtDayToQmlDay(Qt::DayOfWeek day)
{
    return day == Qt::Sunday ? QQmlLocale::DayOfWeek::Sunday : QQmlLocale::DayOfWeek(day);
}

//  from ../qtdeclarative/src/qml/qml/qqmllocale.cpp, line 437, as _ZNK19QQmlLocaleValueType17formattedDataSizeEP14QQmlV4Function
inline void QQmlLocaleValueType::formattedDataSize(QQmlV4FunctionPtr args) const
{
    QV4::Scope scope(args->v4engine());
    const auto doThrow = [&](const QString &message) {
        args->setReturnValue(scope.engine->throwError(message));
    };

    const int argc = args->length();

    if (argc < 1 || argc > 3) {
        doThrow(QString::fromLatin1(
                        "Locale: formattedDataSize(): Expected 1-3 arguments, but received %1")
                        .arg(argc));
        return;
    }

    QV4::ScopedValue arg0(scope, (*args)[0]);
    bool mismatched0 = false;
    if (!arg0->isNumber()) {
        // ### Qt7: Throw an exception here, so that we don't have to handle mismatched0 below.
        qWarning() << "Locale: formattedDataSize(): Invalid argument ('bytes' should be a number)";
        if (argc == 1) {
            args->setReturnValue(
                    scope.engine->newString(locale.formattedDataSize(qint64(arg0->toInteger())))
                            ->asReturnedValue());
            return;
        }

        mismatched0 = true;
    }

    // Anything can be coerced to a number, for better or worse ...
    Q_ASSERT(argc >= 2);

    QV4::ScopedValue arg1(scope, (*args)[1]);
    if (!arg1->isInteger()) {
        doThrow(QLatin1String(
                "Locale: formattedDataSize(): Invalid argument ('precision' must be an int)"));
        return;
    }

    if (mismatched0) {
        if (argc == 2) {
            const QString result = locale.formattedDataSize(
                    qint64(arg0->toInteger()), arg1->integerValue());
            args->setReturnValue(scope.engine->newString(result)->asReturnedValue());
            return;
        }

        QV4::ScopedValue arg2(scope, (*args)[2]);
        if (arg2->isNumber()) {
            const QString result = locale.formattedDataSize(
                    qint64(arg0->toInteger()), arg1->integerValue(),
                    QLocale::DataSizeFormats(arg2->integerValue()));
            args->setReturnValue(scope.engine->newString(result)->asReturnedValue());
            return;
        }
    }

    Q_ASSERT(argc == 3);
    Q_ASSERT(!QV4::ScopedValue(scope, (*args)[2])->isNumber());

    doThrow(QLatin1String(
            "Locale: formattedDataSize(): Invalid argument ('format' must be DataSizeFormat)"));
}

//  from ../qtdeclarative/src/qml/qml/qqmllocale.cpp, line 508, as _ZNK19QQmlLocaleValueType14firstDayOfWeekEv
inline QQmlLocale::DayOfWeek QQmlLocaleValueType::firstDayOfWeek() const
{
    return qtDayToQmlDay(locale.firstDayOfWeek());
}
//  -----------------------------------------------------------------------

//  void QQmlLocaleValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLocaleValueType22qt_qmlMarker_anonymousEv(
    QQmlLocaleValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlLocaleValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLocaleValueType20qt_qmlMarker_foreignEv(
    QQmlLocaleValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlLocaleValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLocaleValueType21qt_qmlMarker_extendedEv(
    QQmlLocaleValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlLocaleValueType::QQmlLocaleValueType(const QString &name)
extern "C" Q_DECL_EXPORT
QQmlLocaleValueType *ritual_ZN19QQmlLocaleValueTypeC1ERK7QString(
    const QString *name) {
  return new QQmlLocaleValueType(*name);
}

//  QString QQmlLocaleValueType::currencySymbol(QLocale::CurrencySymbolFormat
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType14currencySymbolEN7QLocale20CurrencySymbolFormatE(
    const QQmlLocaleValueType *self,
    QLocale::CurrencySymbolFormat format) {
  return new QString(self->currencySymbol(format));
}

//  QString QQmlLocaleValueType::dateTimeFormat(QLocale::FormatType format)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType14dateTimeFormatEN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    QLocale::FormatType format) {
  return new QString(self->dateTimeFormat(format));
}

//  QString QQmlLocaleValueType::timeFormat(QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType10timeFormatEN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    QLocale::FormatType format) {
  return new QString(self->timeFormat(format));
}

//  QString QQmlLocaleValueType::dateFormat(QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType10dateFormatEN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    QLocale::FormatType format) {
  return new QString(self->dateFormat(format));
}

//  QString QQmlLocaleValueType::monthName(int index, QLocale::FormatType
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType9monthNameEiN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    int index,
    QLocale::FormatType format) {
  return new QString(self->monthName(index, format));
}

//  QString QQmlLocaleValueType::standaloneMonthName(int index,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType19standaloneMonthNameEiN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    int index,
    QLocale::FormatType format) {
  return new QString(self->standaloneMonthName(index, format));
}

//  QString QQmlLocaleValueType::dayName(int index, QLocale::FormatType
//      format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType7dayNameEiN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    int index,
    QLocale::FormatType format) {
  return new QString(self->dayName(index, format));
}

//  QString QQmlLocaleValueType::standaloneDayName(int index,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType17standaloneDayNameEiN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    int index,
    QLocale::FormatType format) {
  return new QString(self->standaloneDayName(index, format));
}

//  void QQmlLocaleValueType::formattedDataSize(QQmlV4FunctionPtr args) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlLocaleValueType17formattedDataSizeEP14QQmlV4Function(
    const QQmlLocaleValueType *self,
    QQmlV4FunctionPtr args) {
  self->formattedDataSize(args);
}

//  QString QQmlLocaleValueType::formattedDataSize(double bytes, int
//      precision, QLocale::DataSizeFormats format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType17formattedDataSizeEdi6QFlagsIN7QLocale14DataSizeFormatEE(
    const QQmlLocaleValueType *self,
    double bytes,
    int precision,
    int format) {
  return new QString(
      self->formattedDataSize(
          bytes,
          precision,
          QFlags<QLocale::DataSizeFormat>::fromInt(format)));
}

//  QString QQmlLocaleValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->toString());
}

//  QString QQmlLocaleValueType::toString(int i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringEi(
    const QQmlLocaleValueType *self,
    int i) {
  return new QString(self->toString(i));
}

//  QString QQmlLocaleValueType::toString(double f) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringEd(
    const QQmlLocaleValueType *self,
    double f) {
  return new QString(self->toString(f));
}

//  QString QQmlLocaleValueType::toString(double f, const QString &format,
//      int precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringEdRK7QStringi(
    const QQmlLocaleValueType *self,
    double f,
    const QString *format,
    int precision) {
  return new QString(self->toString(f, *format, precision));
}

//  QString QQmlLocaleValueType::toString(const QDateTime &dateTime, const
//      QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringERK9QDateTimeRK7QString(
    const QQmlLocaleValueType *self,
    const QDateTime *dateTime,
    const QString *format) {
  return new QString(self->toString(*dateTime, *format));
}

//  QString QQmlLocaleValueType::toString(const QDateTime &dateTime,
//      QLocale::FormatType format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType8toStringERK9QDateTimeN7QLocale10FormatTypeE(
    const QQmlLocaleValueType *self,
    const QDateTime *dateTime,
    QLocale::FormatType format) {
  return new QString(self->toString(*dateTime, format));
}

//  QString QQmlLocaleValueType::createSeparatedList(const QStringList &list)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType19createSeparatedListERK5QListI7QStringE(
    const QQmlLocaleValueType *self,
    const QList<QString> *list) {
  return new QString(self->createSeparatedList(*list));
}

//  QQmlLocale::DayOfWeek QQmlLocaleValueType::firstDayOfWeek() const
extern "C" Q_DECL_EXPORT
QQmlLocale::DayOfWeek ritual_ZNK19QQmlLocaleValueType14firstDayOfWeekEv(
    const QQmlLocaleValueType *self) {
  return self->firstDayOfWeek();
}

//  QLocale::MeasurementSystem QQmlLocaleValueType::measurementSystem() const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK19QQmlLocaleValueType17measurementSystemEv(
    const QQmlLocaleValueType *self) {
  return self->measurementSystem();
}

//  Qt::LayoutDirection QQmlLocaleValueType::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK19QQmlLocaleValueType13textDirectionEv(
    const QQmlLocaleValueType *self) {
  return self->textDirection();
}

//  QStringList QQmlLocaleValueType::uiLanguages() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QQmlLocaleValueType11uiLanguagesEv(
    const QQmlLocaleValueType *self) {
  return new QList<QString>(self->uiLanguages());
}

//  QString QQmlLocaleValueType::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType4nameEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->name());
}

//  QString QQmlLocaleValueType::nativeLanguageName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType18nativeLanguageNameEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->nativeLanguageName());
}

#if QT_DEPRECATED_SINCE(6, 6)
//  QString QQmlLocaleValueType::nativeCountryName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType17nativeCountryNameEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->nativeCountryName());
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  QString QQmlLocaleValueType::nativeTerritoryName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType19nativeTerritoryNameEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->nativeTerritoryName());
}

//  QString QQmlLocaleValueType::decimalPoint() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType12decimalPointEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->decimalPoint());
}

//  QString QQmlLocaleValueType::groupSeparator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType14groupSeparatorEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->groupSeparator());
}

//  QString QQmlLocaleValueType::percent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType7percentEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->percent());
}

//  QString QQmlLocaleValueType::zeroDigit() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType9zeroDigitEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->zeroDigit());
}

//  QString QQmlLocaleValueType::negativeSign() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType12negativeSignEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->negativeSign());
}

//  QString QQmlLocaleValueType::positiveSign() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType12positiveSignEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->positiveSign());
}

//  QString QQmlLocaleValueType::exponential() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType11exponentialEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->exponential());
}

//  QString QQmlLocaleValueType::amText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType6amTextEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->amText());
}

//  QString QQmlLocaleValueType::pmText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlLocaleValueType6pmTextEv(
    const QQmlLocaleValueType *self) {
  return new QString(self->pmText());
}

//  QLocale::NumberOptions QQmlLocaleValueType::numberOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQmlLocaleValueType13numberOptionsEv(
    const QQmlLocaleValueType *self) {
  return static_cast<int>(self->numberOptions().toInt());
}

//  void QQmlLocaleValueType::setNumberOptions(const QLocale::NumberOptions
//      &numberOptions)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLocaleValueType16setNumberOptionsERK6QFlagsIN7QLocale12NumberOptionEE(
    QQmlLocaleValueType *self,
    const QLocale::NumberOptions *numberOptions) {
  self->setNumberOptions(*numberOptions);
}

//  QQmlLocaleValueType::~QQmlLocaleValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlLocaleValueTypeD1Ev(QQmlLocaleValueType *self) {
  delete self;
}

//  a QList<QQmlLocale::DayOfWeek> a ritual of QQmlLocaleValueType gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlLocaleValueType__QList_QQmlLocale_DayOfWeek(
    QList<QQmlLocale::DayOfWeek> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_locale)
#endif  // QT_CONFIG(qml_locale)
