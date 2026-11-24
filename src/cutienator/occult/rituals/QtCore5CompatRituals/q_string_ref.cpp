//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qstringref.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qstringref.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qchar.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QStringRef::QStringRef()
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZN10QStringRefC1Ev() {
  return new QStringRef();
}

//  QStringRef::QStringRef(const QString *string, qsizetype position,
//      qsizetype size)
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZN10QStringRefC1EPK7QStringxx(
    const QString *string,
    qsizetype position,
    qsizetype size) {
  return new QStringRef(string, position, size);
}

//  QStringRef::QStringRef(const QString *string)
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZN10QStringRefC1EPK7QString(const QString *string) {
  return new QStringRef(string);
}

//  const QString *QStringRef::string() const
extern "C" Q_DECL_EXPORT
const QString *ritual_ZNK10QStringRef6stringEv(const QStringRef *self) {
  return self->string();
}

//  int QStringRef::position() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef8positionEv(const QStringRef *self) {
  return self->position();
}

//  int QStringRef::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef4sizeEv(const QStringRef *self) {
  return self->size();
}

//  int QStringRef::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef5countEv(const QStringRef *self) {
  return self->count();
}

//  int QStringRef::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef6lengthEv(const QStringRef *self) {
  return self->length();
}

//  int QStringRef::indexOf(const QString &str, int from, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7indexOfERK7QStringiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*str, from, cs);
}

//  int QStringRef::indexOf(const QStringRef &str, int from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7indexOfERKS_iN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*str, from, cs);
}

//  int QStringRef::indexOf(QStringView s, int from, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7indexOfE11QStringViewiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    int from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(QStringView(*s), from, cs);
}

//  int QStringRef::indexOf(QChar ch, int from, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7indexOfE5QChariN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *ch,
    int from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*ch, from, cs);
}

//  int QStringRef::indexOf(QLatin1String str, int from, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7indexOfE13QLatin1StringiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*str, from, cs);
}

//  int QStringRef::lastIndexOf(const QStringRef &str, int from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef11lastIndexOfERKS_iN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*str, from, cs);
}

//  int QStringRef::lastIndexOf(const QString &str, int from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef11lastIndexOfERK7QStringiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*str, from, cs);
}

//  int QStringRef::lastIndexOf(QChar ch, int from, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef11lastIndexOfE5QChariN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *ch,
    int from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*ch, from, cs);
}

//  int QStringRef::lastIndexOf(QLatin1String str, int from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef11lastIndexOfE13QLatin1StringiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *str,
    int from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*str, from, cs);
}

//  int QStringRef::lastIndexOf(QStringView s, int from, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef11lastIndexOfE11QStringViewiN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    int from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), from, cs);
}

//  bool QStringRef::contains(const QString &str, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8containsERK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *str,
    Qt::CaseSensitivity cs) {
  return self->contains(*str, cs);
}

//  bool QStringRef::contains(const QStringRef &str, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8containsERKS_N2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *str,
    Qt::CaseSensitivity cs) {
  return self->contains(*str, cs);
}

//  bool QStringRef::contains(QChar ch, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8containsE5QCharN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *ch,
    Qt::CaseSensitivity cs) {
  return self->contains(*ch, cs);
}

//  bool QStringRef::contains(QLatin1String str, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8containsE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *str,
    Qt::CaseSensitivity cs) {
  return self->contains(*str, cs);
}

//  bool QStringRef::contains(QStringView str, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8containsE11QStringViewN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *str,
    Qt::CaseSensitivity cs) {
  return self->contains(QStringView(*str), cs);
}

//  int QStringRef::count(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef5countERK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->count(*s, cs);
}

//  int QStringRef::count(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef5countE5QCharN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->count(*c, cs);
}

//  int QStringRef::count(const QStringRef &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef5countERKS_N2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *s,
    Qt::CaseSensitivity cs) {
  return self->count(*s, cs);
}

//  QList<QStringRef> QStringRef::split(const QString &sep, Qt::SplitBehavior
//      behavior, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QStringRef> *ritual_ZNK10QStringRef5splitERK7QString6QFlagsIN2Qt18SplitBehaviorFlagsEENS4_15CaseSensitivityE(
    const QStringRef *self,
    const QString *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QStringRef>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

//  QList<QStringRef> QStringRef::split(QChar sep, Qt::SplitBehavior
//      behavior, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QStringRef> *ritual_ZNK10QStringRef5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFlagsEENS2_15CaseSensitivityE(
    const QStringRef *self,
    const QChar *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QStringRef>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

//  QStringRef QStringRef::left(int n) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef4leftEi(const QStringRef *self, int n) {
  return new QStringRef(self->left(n));
}

//  QStringRef QStringRef::right(int n) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef5rightEi(const QStringRef *self, int n) {
  return new QStringRef(self->right(n));
}

//  QStringRef QStringRef::mid(int pos, int n) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef3midEii(
    const QStringRef *self,
    int pos,
    int n) {
  return new QStringRef(self->mid(pos, n));
}

//  QStringRef QStringRef::chopped(int n) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef7choppedEi(const QStringRef *self, int n) {
  return new QStringRef(self->chopped(n));
}

//  void QStringRef::truncate(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStringRef8truncateEi(QStringRef *self, int pos) {
  self->truncate(pos);
}

//  void QStringRef::chop(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStringRef4chopEi(QStringRef *self, int n) {
  self->chop(n);
}

//  bool QStringRef::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef13isRightToLeftEv(const QStringRef *self) {
  return self->isRightToLeft();
}

//  bool QStringRef::startsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef10startsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(QStringView(*s), cs);
}

//  bool QStringRef::startsWith(QLatin1String s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef10startsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QStringRef::startsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef10startsWithE5QCharN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*c, cs);
}

//  bool QStringRef::startsWith(const QString &s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef10startsWithERK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QStringRef::startsWith(const QStringRef &c, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef10startsWithERKS_N2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *c,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*c, cs);
}

//  bool QStringRef::endsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8endsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(QStringView(*s), cs);
}

//  bool QStringRef::endsWith(QLatin1String s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8endsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QStringRef::endsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8endsWithE5QCharN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*c, cs);
}

//  bool QStringRef::endsWith(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8endsWithERK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QStringRef::endsWith(const QStringRef &c, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef8endsWithERKS_N2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *c,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*c, cs);
}

//  QStringView QStringRef::operator QStringView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QStringRefcv11QStringViewEv(const QStringRef *self) {
  return new QString(self->operator QStringView().toString());
}

#if defined(QSTRINGVIEW_REFUSES_QSTRINGREF)
//  QAnyStringView QStringRef::operator QAnyStringView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QStringRefcv14QAnyStringViewEv(const QStringRef *self) {
  return new QString(self->operator QAnyStringView().toString());
}
#endif  // defined(QSTRINGVIEW_REFUSES_QSTRINGREF)

//  const QChar *QStringRef::unicode() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK10QStringRef7unicodeEv(const QStringRef *self) {
  return self->unicode();
}

//  const QChar *QStringRef::data() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK10QStringRef4dataEv(const QStringRef *self) {
  return self->data();
}

//  const QChar *QStringRef::constData() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK10QStringRef9constDataEv(const QStringRef *self) {
  return self->constData();
}

//  const_iterator QStringRef::begin() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef5beginEv(
    const QStringRef *self) {
  return self->begin();
}

//  const_iterator QStringRef::cbegin() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef6cbeginEv(
    const QStringRef *self) {
  return self->cbegin();
}

//  const_iterator QStringRef::constBegin() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef10constBeginEv(
    const QStringRef *self) {
  return self->constBegin();
}

//  const_iterator QStringRef::end() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef3endEv(
    const QStringRef *self) {
  return self->end();
}

//  const_iterator QStringRef::cend() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef4cendEv(
    const QStringRef *self) {
  return self->cend();
}

//  const_iterator QStringRef::constEnd() const
extern "C" Q_DECL_EXPORT
QStringRef::const_iterator ritual_ZNK10QStringRef8constEndEv(
    const QStringRef *self) {
  return self->constEnd();
}

//  QByteArray QStringRef::toLatin1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QStringRef8toLatin1Ev(const QStringRef *self) {
  return new QByteArray(self->toLatin1());
}

//  QByteArray QStringRef::toUtf8() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QStringRef6toUtf8Ev(const QStringRef *self) {
  return new QByteArray(self->toUtf8());
}

//  QByteArray QStringRef::toLocal8Bit() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QStringRef11toLocal8BitEv(const QStringRef *self) {
  return new QByteArray(self->toLocal8Bit());
}

//  void QStringRef::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStringRef5clearEv(QStringRef *self) {
  self->clear();
}

//  QString QStringRef::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QStringRef8toStringEv(const QStringRef *self) {
  return new QString(self->toString());
}

//  bool QStringRef::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef7isEmptyEv(const QStringRef *self) {
  return self->isEmpty();
}

//  bool QStringRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRef6isNullEv(const QStringRef *self) {
  return self->isNull();
}

//  QStringRef QStringRef::appendTo(QString *string) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef8appendToEP7QString(
    const QStringRef *self,
    QString *string) {
  return new QStringRef(self->appendTo(string));
}

//  const QChar QStringRef::at(int i) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK10QStringRef2atEi(const QStringRef *self, int i) {
  return new QChar(self->at(i));
}

//  QChar QStringRef::operator[](int i) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK10QStringRefixEi(const QStringRef *self, int i) {
  return new QChar(self->operator[](i));
}

//  QChar QStringRef::front() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK10QStringRef5frontEv(const QStringRef *self) {
  return new QChar(self->front());
}

//  QChar QStringRef::back() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK10QStringRef4backEv(const QStringRef *self) {
  return new QChar(self->back());
}

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator==(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefeqEPKc(const QStringRef *self, const char *s) {
  return self->operator==(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator!=(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefneEPKc(const QStringRef *self, const char *s) {
  return self->operator!=(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator<(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefltEPKc(const QStringRef *self, const char *s) {
  return self->operator<(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator<=(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefleEPKc(const QStringRef *self, const char *s) {
  return self->operator<=(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator>(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefgtEPKc(const QStringRef *self, const char *s) {
  return self->operator>(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool QStringRef::operator>=(const char *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStringRefgeEPKc(const QStringRef *self, const char *s) {
  return self->operator>=(s);
}
#endif

//  int QStringRef::compare(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7compareERK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->compare(*s, cs);
}

//  int QStringRef::compare(const QStringRef &s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7compareERKS_N2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QStringRef *s,
    Qt::CaseSensitivity cs) {
  return self->compare(*s, cs);
}

//  int QStringRef::compare(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7compareE5QCharN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->compare(*c, cs);
}

//  int QStringRef::compare(QLatin1String s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7compareE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->compare(*s, cs);
}

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  int QStringRef::compare(const QByteArray &s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef7compareERK10QByteArrayN2Qt15CaseSensitivityE(
    const QStringRef *self,
    const QByteArray *s,
    Qt::CaseSensitivity cs) {
  return self->compare(*s, cs);
}
#endif

//  int QStringRef::compare(const QStringRef &s1, const QString &s2,
//      Qt::CaseSensitivity a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef7compareERKS_RK7QStringN2Qt15CaseSensitivityE(
    const QStringRef *s1,
    const QString *s2,
    Qt::CaseSensitivity a2) {
  return QStringRef::compare(*s1, *s2, a2);
}

//  int QStringRef::compare(const QStringRef &s1, const QStringRef &s2,
//      Qt::CaseSensitivity a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef7compareERKS_S1_N2Qt15CaseSensitivityE(
    const QStringRef *s1,
    const QStringRef *s2,
    Qt::CaseSensitivity a2) {
  return QStringRef::compare(*s1, *s2, a2);
}

//  int QStringRef::compare(const QStringRef &s1, QLatin1String s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef7compareERKS_13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringRef *s1,
    const QLatin1String *s2,
    Qt::CaseSensitivity cs) {
  return QStringRef::compare(*s1, *s2, cs);
}

//  int QStringRef::localeAwareCompare(const QString &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef18localeAwareCompareERK7QString(
    const QStringRef *self,
    const QString *s) {
  return self->localeAwareCompare(*s);
}

//  int QStringRef::localeAwareCompare(const QStringRef &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef18localeAwareCompareERKS_(
    const QStringRef *self,
    const QStringRef *s) {
  return self->localeAwareCompare(*s);
}

//  int QStringRef::localeAwareCompare(const QStringRef &s1, const QString
//      &s2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef18localeAwareCompareERKS_RK7QString(
    const QStringRef *s1,
    const QString *s2) {
  return QStringRef::localeAwareCompare(*s1, *s2);
}

//  int QStringRef::localeAwareCompare(const QStringRef &s1, const QStringRef
//      &s2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef18localeAwareCompareERKS_S1_(
    const QStringRef *s1,
    const QStringRef *s2) {
  return QStringRef::localeAwareCompare(*s1, *s2);
}

//  QStringRef QStringRef::trimmed() const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_ZNK10QStringRef7trimmedEv(const QStringRef *self) {
  return new QStringRef(self->trimmed());
}

//  short QStringRef::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK10QStringRef7toShortEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QStringRef::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK10QStringRef8toUShortEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QStringRef::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QStringRef5toIntEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toInt(ok, base);
}

//  uint QStringRef::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10QStringRef6toUIntEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toUInt(ok, base);
}

//  long QStringRef::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK10QStringRef6toLongEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toLong(ok, base);
}

//  ulong QStringRef::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK10QStringRef7toULongEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QStringRef::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK10QStringRef10toLongLongEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QStringRef::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK10QStringRef11toULongLongEPbi(
    const QStringRef *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QStringRef::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QStringRef7toFloatEPb(const QStringRef *self, bool *ok) {
  return self->toFloat(ok);
}

//  double QStringRef::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QStringRef8toDoubleEPb(const QStringRef *self, bool *ok) {
  return self->toDouble(ok);
}

//  bool operator==(QChar a0, const QStringRef &a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq5QCharRK10QStringRef(const QChar *a0, const QStringRef *a1) {
  return operator==(*a0, *a1);
}

//  bool operator<(QChar a0, const QStringRef &a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zlt5QCharRK10QStringRef(const QChar *a0, const QStringRef *a1) {
  return operator<(*a0, *a1);
}

//  bool operator>(QChar a0, const QStringRef &a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zgt5QCharRK10QStringRef(const QChar *a0, const QStringRef *a1) {
  return operator>(*a0, *a1);
}

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqPKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator==(s1, *s2);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZnePKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator!=(s1, *s2);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZltPKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator<(s1, *s2);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtPKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator>(s1, *s2);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZlePKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator<=(s1, *s2);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const char *s1, const QStringRef &s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZgePKcRK10QStringRef(const char *s1, const QStringRef *s2) {
  return operator>=(s1, *s2);
}
#endif

//  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
//      const QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef14compare_helperEPK5QCharxS2_xN2Qt15CaseSensitivityE(
    const QChar *data1,
    qsizetype length1,
    const QChar *data2,
    qsizetype length2,
    Qt::CaseSensitivity cs) {
  return QStringRef::compare_helper(data1, length1, data2, length2, cs);
}

//  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
//      const char *data2, qsizetype length2, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef14compare_helperEPK5QCharxPKcxN2Qt15CaseSensitivityE(
    const QChar *data1,
    qsizetype length1,
    const char *data2,
    qsizetype length2,
    Qt::CaseSensitivity cs) {
  return QStringRef::compare_helper(data1, length1, data2, length2, cs);
}

//  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
//      QLatin1String s2, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStringRef14compare_helperEPK5QCharx13QLatin1StringN2Qt15CaseSensitivityE(
    const QChar *data1,
    qsizetype length1,
    const QLatin1String *s2,
    Qt::CaseSensitivity cs) {
  return QStringRef::compare_helper(data1, length1, *s2, cs);
}

//  QStringRef::~QStringRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStringRefD1Ev(QStringRef *self) {
  delete self;
}

//  QList<QStringRef>::QList()
extern "C" Q_DECL_EXPORT
QList<QStringRef> *ritual_list_make_QStringRef() {
  return new QList<QStringRef>();
}

//  void QList<QStringRef>::append(const QStringRef &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QStringRef(
    QList<QStringRef> *self,
    const QStringRef *element) {
  self->append(*element);
}

//  qsizetype QList<QStringRef>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QStringRef(const QList<QStringRef> *self) {
  return self->size();
}

//  const QStringRef &QList<QStringRef>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QStringRef *ritual_list_at_QStringRef(
    const QList<QStringRef> *self,
    long long index) {
  return new QStringRef(self->at(index));
}

//  QList<QStringRef>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QStringRef(QList<QStringRef> *self) {
  delete self;
}
