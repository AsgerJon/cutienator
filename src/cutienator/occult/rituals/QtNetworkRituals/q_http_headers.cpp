//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QHttpHeaders::QHttpHeaders()
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZN12QHttpHeadersC1Ev() {
  return new QHttpHeaders();
}

//  QHttpHeaders::~QHttpHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeadersD1Ev(QHttpHeaders *self) {
  delete self;
}

//  QHttpHeaders::QHttpHeaders(const QHttpHeaders &other)
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZN12QHttpHeadersC1ERKS_(const QHttpHeaders *other) {
  return new QHttpHeaders(*other);
}

//  bool QHttpHeaders::append(QAnyStringView name, QAnyStringView value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders6appendE14QAnyStringViewS0_(
    QHttpHeaders *self,
    const QString *name,
    const QString *value) {
  return self->append(QAnyStringView(*name), QAnyStringView(*value));
}

//  bool QHttpHeaders::append(WellKnownHeader name, QAnyStringView value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders6appendENS_15WellKnownHeaderE14QAnyStringView(
    QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name,
    const QString *value) {
  return self->append(name, QAnyStringView(*value));
}

//  bool QHttpHeaders::insert(qsizetype i, QAnyStringView name,
//      QAnyStringView value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders6insertEx14QAnyStringViewS0_(
    QHttpHeaders *self,
    qsizetype i,
    const QString *name,
    const QString *value) {
  return self->insert(i, QAnyStringView(*name), QAnyStringView(*value));
}

//  bool QHttpHeaders::insert(qsizetype i, WellKnownHeader name,
//      QAnyStringView value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders6insertExNS_15WellKnownHeaderE14QAnyStringView(
    QHttpHeaders *self,
    qsizetype i,
    QHttpHeaders::WellKnownHeader name,
    const QString *value) {
  return self->insert(i, name, QAnyStringView(*value));
}

//  bool QHttpHeaders::replace(qsizetype i, QAnyStringView name,
//      QAnyStringView newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders7replaceEx14QAnyStringViewS0_(
    QHttpHeaders *self,
    qsizetype i,
    const QString *name,
    const QString *newValue) {
  return self->replace(i, QAnyStringView(*name), QAnyStringView(*newValue));
}

//  bool QHttpHeaders::replace(qsizetype i, WellKnownHeader name,
//      QAnyStringView newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders7replaceExNS_15WellKnownHeaderE14QAnyStringView(
    QHttpHeaders *self,
    qsizetype i,
    QHttpHeaders::WellKnownHeader name,
    const QString *newValue) {
  return self->replace(i, name, QAnyStringView(*newValue));
}

//  bool QHttpHeaders::replaceOrAppend(QAnyStringView name, QAnyStringView
//      newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders15replaceOrAppendE14QAnyStringViewS0_(
    QHttpHeaders *self,
    const QString *name,
    const QString *newValue) {
  return self->replaceOrAppend(
      QAnyStringView(*name),
      QAnyStringView(*newValue));
}

//  bool QHttpHeaders::replaceOrAppend(WellKnownHeader name, QAnyStringView
//      newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttpHeaders15replaceOrAppendENS_15WellKnownHeaderE14QAnyStringView(
    QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name,
    const QString *newValue) {
  return self->replaceOrAppend(name, QAnyStringView(*newValue));
}

//  bool QHttpHeaders::contains(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttpHeaders8containsE14QAnyStringView(
    const QHttpHeaders *self,
    const QString *name) {
  return self->contains(QAnyStringView(*name));
}

//  bool QHttpHeaders::contains(WellKnownHeader name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttpHeaders8containsENS_15WellKnownHeaderE(
    const QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name) {
  return self->contains(name);
}

//  void QHttpHeaders::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders5clearEv(QHttpHeaders *self) {
  self->clear();
}

//  void QHttpHeaders::removeAll(QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders9removeAllE14QAnyStringView(
    QHttpHeaders *self,
    const QString *name) {
  self->removeAll(QAnyStringView(*name));
}

//  void QHttpHeaders::removeAll(WellKnownHeader name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders9removeAllENS_15WellKnownHeaderE(
    QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name) {
  self->removeAll(name);
}

//  void QHttpHeaders::removeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders8removeAtEx(QHttpHeaders *self, qsizetype i) {
  self->removeAt(i);
}

//  QByteArrayView QHttpHeaders::value(QAnyStringView name, QByteArrayView
//      defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK12QHttpHeaders5valueE14QAnyStringView14QByteArrayView(
    const QHttpHeaders *self,
    const QString *name,
    const QByteArrayView *defaultValue) {
  return new QByteArrayView(
      self->value(
          QAnyStringView(*name),
          *defaultValue));
}

//  QByteArrayView QHttpHeaders::value(WellKnownHeader name, QByteArrayView
//      defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK12QHttpHeaders5valueENS_15WellKnownHeaderE14QByteArrayView(
    const QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name,
    const QByteArrayView *defaultValue) {
  return new QByteArrayView(self->value(name, *defaultValue));
}

//  QList<QByteArray> QHttpHeaders::values(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12QHttpHeaders6valuesE14QAnyStringView(
    const QHttpHeaders *self,
    const QString *name) {
  return new QList<QByteArray>(self->values(QAnyStringView(*name)));
}

//  QList<QByteArray> QHttpHeaders::values(WellKnownHeader name) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12QHttpHeaders6valuesENS_15WellKnownHeaderE(
    const QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name) {
  return new QList<QByteArray>(self->values(name));
}

//  QByteArrayView QHttpHeaders::valueAt(qsizetype i) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK12QHttpHeaders7valueAtEx(
    const QHttpHeaders *self,
    qsizetype i) {
  return new QByteArrayView(self->valueAt(i));
}

//  QLatin1StringView QHttpHeaders::nameAt(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK12QHttpHeaders6nameAtEx(
    const QHttpHeaders *self,
    qsizetype i) {
  return new QLatin1String(self->nameAt(i));
}

//  QByteArray QHttpHeaders::combinedValue(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QHttpHeaders13combinedValueE14QAnyStringView(
    const QHttpHeaders *self,
    const QString *name) {
  return new QByteArray(self->combinedValue(QAnyStringView(*name)));
}

//  QByteArray QHttpHeaders::combinedValue(WellKnownHeader name) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QHttpHeaders13combinedValueENS_15WellKnownHeaderE(
    const QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name) {
  return new QByteArray(self->combinedValue(name));
}

//  void QHttpHeaders::setDateTimeValue(QAnyStringView name, const QDateTime
//      &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders16setDateTimeValueE14QAnyStringViewRK9QDateTime(
    QHttpHeaders *self,
    const QString *name,
    const QDateTime *dateTime) {
  self->setDateTimeValue(QAnyStringView(*name), *dateTime);
}

//  void QHttpHeaders::setDateTimeValue(WellKnownHeader name, const QDateTime
//      &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders16setDateTimeValueENS_15WellKnownHeaderERK9QDateTime(
    QHttpHeaders *self,
    QHttpHeaders::WellKnownHeader name,
    const QDateTime *dateTime) {
  self->setDateTimeValue(name, *dateTime);
}

//  void QHttpHeaders::setRangeValues(const QHttpHeaderRangeSet &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders14setRangeValuesERK19QHttpHeaderRangeSet(
    QHttpHeaders *self,
    const QHttpHeaderRangeSet *ranges) {
  self->setRangeValues(*ranges);
}

//  qsizetype QHttpHeaders::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QHttpHeaders4sizeEv(const QHttpHeaders *self) {
  return self->size();
}

//  void QHttpHeaders::reserve(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttpHeaders7reserveEx(QHttpHeaders *self, qsizetype size) {
  self->reserve(size);
}

//  bool QHttpHeaders::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttpHeaders7isEmptyEv(const QHttpHeaders *self) {
  return self->isEmpty();
}

//  QByteArrayView QHttpHeaders::wellKnownHeaderName(WellKnownHeader name)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN12QHttpHeaders19wellKnownHeaderNameENS_15WellKnownHeaderE(
    QHttpHeaders::WellKnownHeader name) {
  return new QByteArrayView(QHttpHeaders::wellKnownHeaderName(name));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QHttpHeaders &headers)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK12QHttpHeaders(
    const QDebug *debug,
    const QHttpHeaders *headers) {
  return new QDebug(operator<<(*debug, *headers));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  void QHttpHeaders::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QHttpHeaders6verifyExx(
    const QHttpHeaders *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}
