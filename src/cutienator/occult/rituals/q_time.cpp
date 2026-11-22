//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QTime::QTime()
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTimeC1Ev() {
  return new QTime();
}

//  QTime::QTime(int h, int m, int s, int ms)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTimeC1Eiiii(int h, int m, int s, int ms) {
  return new QTime(h, m, s, ms);
}

//  bool QTime::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QTime6isNullEv(const QTime *self) {
  return self->isNull();
}

//  bool QTime::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QTime7isValidEv(const QTime *self) {
  return self->isValid();
}

//  int QTime::hour() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime4hourEv(const QTime *self) {
  return self->hour();
}

//  int QTime::minute() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime6minuteEv(const QTime *self) {
  return self->minute();
}

//  int QTime::second() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime6secondEv(const QTime *self) {
  return self->second();
}

//  int QTime::msec() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime4msecEv(const QTime *self) {
  return self->msec();
}

//  QString QTime::toString(Qt::DateFormat f) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QTime8toStringEN2Qt10DateFormatE(
    const QTime *self,
    Qt::DateFormat f) {
  return new QString(self->toString(f));
}

//  QString QTime::toString(const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QTime8toStringERK7QString(
    const QTime *self,
    const QString *format) {
  return new QString(self->toString(*format));
}

//  QString QTime::toString(QStringView format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QTime8toStringE11QStringView(
    const QTime *self,
    const QString *format) {
  return new QString(self->toString(QStringView(*format)));
}

//  bool QTime::setHMS(int h, int m, int s, int ms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QTime6setHMSEiiii(QTime *self, int h, int m, int s, int ms) {
  return self->setHMS(h, m, s, ms);
}

//  QTime QTime::addSecs(int secs) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK5QTime7addSecsEi(const QTime *self, int secs) {
  return new QTime(self->addSecs(secs));
}

//  int QTime::secsTo(QTime t) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime6secsToES_(const QTime *self, const QTime *t) {
  return self->secsTo(*t);
}

//  QTime QTime::addMSecs(int ms) const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK5QTime8addMSecsEi(const QTime *self, int ms) {
  return new QTime(self->addMSecs(ms));
}

//  int QTime::msecsTo(QTime t) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime7msecsToES_(const QTime *self, const QTime *t) {
  return self->msecsTo(*t);
}

//  QTime QTime::fromMSecsSinceStartOfDay(int msecs)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime24fromMSecsSinceStartOfDayEi(int msecs) {
  return new QTime(QTime::fromMSecsSinceStartOfDay(msecs));
}

//  int QTime::msecsSinceStartOfDay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QTime20msecsSinceStartOfDayEv(const QTime *self) {
  return self->msecsSinceStartOfDay();
}

//  QTime QTime::currentTime()
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime11currentTimeEv() {
  return new QTime(QTime::currentTime());
}

//  QTime QTime::fromString(QStringView string, Qt::DateFormat format)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime10fromStringE11QStringViewN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QTime(QTime::fromString(QStringView(*string), format));
}

//  QTime QTime::fromString(QStringView string, QStringView format)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime10fromStringE11QStringViewS0_(
    const QString *string,
    const QString *format) {
  return new QTime(
      QTime::fromString(
          QStringView(*string),
          QStringView(*format)));
}

//  QTime QTime::fromString(const QString &string, QStringView format)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime10fromStringERK7QString11QStringView(
    const QString *string,
    const QString *format) {
  return new QTime(QTime::fromString(*string, QStringView(*format)));
}

//  QTime QTime::fromString(const QString &string, Qt::DateFormat format)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime10fromStringERK7QStringN2Qt10DateFormatE(
    const QString *string,
    Qt::DateFormat format) {
  return new QTime(QTime::fromString(*string, format));
}

//  QTime QTime::fromString(const QString &string, const QString &format)
extern "C" Q_DECL_EXPORT
QTime *ritual_ZN5QTime10fromStringERK7QStringS2_(
    const QString *string,
    const QString *format) {
  return new QTime(QTime::fromString(*string, *format));
}

//  bool QTime::isValid(int h, int m, int s, int ms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QTime7isValidEiiii(int h, int m, int s, int ms) {
  return QTime::isValid(h, m, s, ms);
}

//  bool operator==(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QTime &lhs, const QTime &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QTimeS1_(const QTime *lhs, const QTime *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QTime::~QTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QTimeD1Ev(QTime *self) {
  delete self;
}
