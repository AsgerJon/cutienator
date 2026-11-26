//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringview.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QUtf8StringView>
#include <QtCore/QStringView>
#include <string_view>

//  qsizetype QStringView::lengthHelperPointer(const QChar *str)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN11QStringView19lengthHelperPointerEPK5QChar(
    const QChar *str) {
  return QStringView::lengthHelperPointer(str);
}

//  const storage_type *QStringView::castHelper(const storage_type *str)
extern "C" Q_DECL_EXPORT
const QStringView::storage_type *ritual_ZN11QStringView10castHelperEPKDs(
    const QStringView::storage_type *str) {
  return QStringView::castHelper(str);
}

//  QStringView::QStringView()
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1Ev() {
  return new QStringView();
}

//  QStringView::QStringView(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1EDn() {
  return new QStringView(nullptr);
}

//  QString QStringView::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView8toStringEv(const QStringView *self) {
  return new QString(self->toString());
}

//  qsizetype QStringView::maxSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN11QStringView7maxSizeEv() {
  return QStringView::maxSize();
}

//  qsizetype QStringView::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView4sizeEv(const QStringView *self) {
  return self->size();
}

//  const_pointer QStringView::data() const
extern "C" Q_DECL_EXPORT
QStringView::const_pointer ritual_ZNK11QStringView4dataEv(
    const QStringView *self) {
  return self->data();
}

//  const_pointer QStringView::constData() const
extern "C" Q_DECL_EXPORT
QStringView::const_pointer ritual_ZNK11QStringView9constDataEv(
    const QStringView *self) {
  return self->constData();
}

//  const storage_type *QStringView::utf16() const
extern "C" Q_DECL_EXPORT
const QStringView::storage_type *ritual_ZNK11QStringView5utf16Ev(
    const QStringView *self) {
  return self->utf16();
}

//  QChar QStringView::operator[](qsizetype n) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringViewixEx(const QStringView *self, qsizetype n) {
  return new QChar(self->operator[](n));
}

//  QByteArray QStringView::toLatin1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QStringView8toLatin1Ev(const QStringView *self) {
  return new QByteArray(self->toLatin1());
}

//  QByteArray QStringView::toUtf8() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QStringView6toUtf8Ev(const QStringView *self) {
  return new QByteArray(self->toUtf8());
}

//  QByteArray QStringView::toLocal8Bit() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QStringView11toLocal8BitEv(const QStringView *self) {
  return new QByteArray(self->toLocal8Bit());
}

//  QList<uint> QStringView::toUcs4() const
extern "C" Q_DECL_EXPORT
QList<uint> *ritual_ZNK11QStringView6toUcs4Ev(const QStringView *self) {
  return new QList<uint>(self->toUcs4());
}

//  QChar QStringView::at(qsizetype n) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringView2atEx(const QStringView *self, qsizetype n) {
  return new QChar(self->at(n));
}

//  QStringView QStringView::mid(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView3midExx(
    const QStringView *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->mid(pos, n).toString());
}

//  QStringView QStringView::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView4leftEx(
    const QStringView *self,
    qsizetype n) {
  return new QString(self->left(n).toString());
}

//  QStringView QStringView::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView5rightEx(
    const QStringView *self,
    qsizetype n) {
  return new QString(self->right(n).toString());
}

//  QStringView QStringView::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView5firstEx(
    const QStringView *self,
    qsizetype n) {
  return new QString(self->first(n).toString());
}

//  QStringView QStringView::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView4lastEx(
    const QStringView *self,
    qsizetype n) {
  return new QString(self->last(n).toString());
}

//  QStringView QStringView::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView6slicedEx(
    const QStringView *self,
    qsizetype pos) {
  return new QString(self->sliced(pos).toString());
}

//  QStringView QStringView::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView6slicedExx(
    const QStringView *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->sliced(pos, n).toString());
}

//  QStringView QStringView::chopped(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView7choppedEx(
    const QStringView *self,
    qsizetype n) {
  return new QString(self->chopped(n).toString());
}

//  void QStringView::truncate(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStringView8truncateEx(QStringView *self, qsizetype n) {
  self->truncate(n);
}

//  void QStringView::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStringView4chopEx(QStringView *self, qsizetype n) {
  self->chop(n);
}

//  QStringView QStringView::trimmed() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStringView7trimmedEv(const QStringView *self) {
  return new QString(self->trimmed().toString());
}

//  QStringView &QStringView::slice(qsizetype pos)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringView5sliceEx(
    QStringView *self,
    qsizetype pos) {
  return &(self->slice(pos));
}

//  QStringView &QStringView::slice(qsizetype pos, qsizetype n)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringView5sliceExx(
    QStringView *self,
    qsizetype pos,
    qsizetype n) {
  return &(self->slice(pos, n));
}

//  int QStringView::compare(QStringView other, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView7compareES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *other,
    Qt::CaseSensitivity cs) {
  return self->compare(QStringView(*other), cs);
}

//  int QStringView::compare(QLatin1StringView other, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView7compareE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *other,
    Qt::CaseSensitivity cs) {
  return self->compare(*other, cs);
}

//  int QStringView::compare(QUtf8StringView other, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView7compareE20QBasicUtf8StringViewILb0EEN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QUtf8StringView *other,
    Qt::CaseSensitivity cs) {
  return self->compare(*other, cs);
}

//  int QStringView::compare(QChar c) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView7compareE5QChar(
    const QStringView *self,
    const QChar *c) {
  return self->compare(*c);
}

//  int QStringView::compare(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView7compareE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->compare(*c, cs);
}

//  int QStringView::localeAwareCompare(QStringView other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView18localeAwareCompareES_(
    const QStringView *self,
    const QString *other) {
  return self->localeAwareCompare(QStringView(*other));
}

//  bool QStringView::startsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView10startsWithES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(QStringView(*s), cs);
}

//  bool QStringView::startsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView10startsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QStringView::startsWith(QChar c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView10startsWithE5QChar(
    const QStringView *self,
    const QChar *c) {
  return self->startsWith(*c);
}

//  bool QStringView::startsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView10startsWithE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*c, cs);
}

//  bool QStringView::endsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8endsWithES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(QStringView(*s), cs);
}

//  bool QStringView::endsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8endsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QStringView::endsWith(QChar c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8endsWithE5QChar(
    const QStringView *self,
    const QChar *c) {
  return self->endsWith(*c);
}

//  bool QStringView::endsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8endsWithE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*c, cs);
}

//  qsizetype QStringView::indexOf(QChar c, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView7indexOfE5QCharxN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*c, from, cs);
}

//  qsizetype QStringView::indexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView7indexOfES_xN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(QStringView(*s), from, cs);
}

//  qsizetype QStringView::indexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView7indexOfE13QLatin1StringxN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*s, from, cs);
}

//  bool QStringView::contains(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8containsE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->contains(*c, cs);
}

//  bool QStringView::contains(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8containsES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->contains(QStringView(*s), cs);
}

//  bool QStringView::contains(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8containsE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->contains(*s, cs);
}

//  qsizetype QStringView::count(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView5countE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->count(*c, cs);
}

//  qsizetype QStringView::count(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView5countES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->count(QStringView(*s), cs);
}

//  qsizetype QStringView::count(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView5countE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->count(*s, cs);
}

//  qsizetype QStringView::lastIndexOf(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfE5QCharN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, cs);
}

//  qsizetype QStringView::lastIndexOf(QChar c, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfE5QCharxN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, from, cs);
}

//  qsizetype QStringView::lastIndexOf(QStringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfES_N2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), cs);
}

//  qsizetype QStringView::lastIndexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfES_xN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), from, cs);
}

//  qsizetype QStringView::lastIndexOf(QLatin1StringView s,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfE13QLatin1StringN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, cs);
}

//  qsizetype QStringView::lastIndexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfE13QLatin1StringxN2Qt15CaseSensitivityE(
    const QStringView *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, from, cs);
}

#if QT_CONFIG(regularexpression)
//  qsizetype QStringView::indexOf(const QRegularExpression &re, qsizetype
//      from, QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView7indexOfERK18QRegularExpressionxP23QRegularExpressionMatch(
    const QStringView *self,
    const QRegularExpression *re,
    qsizetype from,
    QRegularExpressionMatch *rmatch) {
  return self->indexOf(*re, from, rmatch);
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  qsizetype QStringView::lastIndexOf(const QRegularExpression &re,
//      qsizetype from, QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfERK18QRegularExpressionxP23QRegularExpressionMatch(
    const QStringView *self,
    const QRegularExpression *re,
    qsizetype from,
    QRegularExpressionMatch *rmatch) {
  return self->lastIndexOf(*re, from, rmatch);
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  bool QStringView::contains(const QRegularExpression &re,
//      QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView8containsERK18QRegularExpressionP23QRegularExpressionMatch(
    const QStringView *self,
    const QRegularExpression *re,
    QRegularExpressionMatch *rmatch) {
  return self->contains(*re, rmatch);
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  qsizetype QStringView::count(const QRegularExpression &re) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView5countERK18QRegularExpression(
    const QStringView *self,
    const QRegularExpression *re) {
  return self->count(*re);
}
#endif  // QT_CONFIG(regularexpression)

//  bool QStringView::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView13isRightToLeftEv(const QStringView *self) {
  return self->isRightToLeft();
}

//  bool QStringView::isValidUtf16() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView12isValidUtf16Ev(const QStringView *self) {
  return self->isValidUtf16();
}

//  bool QStringView::isUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView7isUpperEv(const QStringView *self) {
  return self->isUpper();
}

//  bool QStringView::isLower() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView7isLowerEv(const QStringView *self) {
  return self->isLower();
}

//  short QStringView::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK11QStringView7toShortEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QStringView::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK11QStringView8toUShortEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QStringView::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView5toIntEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toInt(ok, base);
}

//  uint QStringView::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11QStringView6toUIntEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toUInt(ok, base);
}

//  long QStringView::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK11QStringView6toLongEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toLong(ok, base);
}

//  ulong QStringView::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK11QStringView7toULongEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QStringView::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK11QStringView10toLongLongEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QStringView::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK11QStringView11toULongLongEPbi(
    const QStringView *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QStringView::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QStringView7toFloatEPb(const QStringView *self, bool *ok) {
  return self->toFloat(ok);
}

//  double QStringView::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK11QStringView8toDoubleEPb(
    const QStringView *self,
    bool *ok) {
  return self->toDouble(ok);
}

//  qsizetype QStringView::toWCharArray(wchar_t *array) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView12toWCharArrayEPw(
    const QStringView *self,
    wchar_t *array) {
  return self->toWCharArray(array);
}

//  QList<QStringView> QStringView::split(QStringView sep, Qt::SplitBehavior
//      behavior, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QStringView> *ritual_ZNK11QStringView5splitES_6QFlagsIN2Qt18SplitBehaviorFlagsEENS1_15CaseSensitivityE(
    const QStringView *self,
    const QString *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QStringView>(
      self->split(
          QStringView(*sep),
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

//  QList<QStringView> QStringView::split(QChar sep, Qt::SplitBehavior
//      behavior, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QStringView> *ritual_ZNK11QStringView5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFlagsEENS2_15CaseSensitivityE(
    const QStringView *self,
    const QChar *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QStringView>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

#if QT_CONFIG(regularexpression)
//  QList<QStringView> QStringView::split(const QRegularExpression &sep,
//      Qt::SplitBehavior behavior) const
extern "C" Q_DECL_EXPORT
QList<QStringView> *ritual_ZNK11QStringView5splitERK18QRegularExpression6QFlagsIN2Qt18SplitBehaviorFlagsEE(
    const QStringView *self,
    const QRegularExpression *sep,
    int behavior) {
  return new QList<QStringView>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior)));
}
#endif  // QT_CONFIG(regularexpression)

//  bool operator==(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator==(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator!=(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator!=(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator<(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator<(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator>(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator>(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator<=(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator<=(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator>=(const QStringView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QStringViewS1_(const QString *lhs, const QString *rhs) {
  return operator>=(QStringView(*lhs), QStringView(*rhs));
}

//  bool operator==(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator==(QStringView(*lhs), *rhs);
}

//  bool operator!=(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator!=(QStringView(*lhs), *rhs);
}

//  bool operator<(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator<(QStringView(*lhs), *rhs);
}

//  bool operator>(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator>(QStringView(*lhs), *rhs);
}

//  bool operator<=(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator<=(QStringView(*lhs), *rhs);
}

//  bool operator>=(const QStringView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QStringViewRK5QChar(
    const QString *lhs,
    const QChar *rhs) {
  return operator>=(QStringView(*lhs), *rhs);
}

//  bool operator==(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator==(*lhs, QStringView(*rhs));
}

//  bool operator!=(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator!=(*lhs, QStringView(*rhs));
}

//  bool operator<(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator<(*lhs, QStringView(*rhs));
}

//  bool operator>(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator>(*lhs, QStringView(*rhs));
}

//  bool operator<=(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator<=(*lhs, QStringView(*rhs));
}

//  bool operator>=(const QChar &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRK11QStringView(
    const QChar *lhs,
    const QString *rhs) {
  return operator>=(*lhs, QStringView(*rhs));
}

//  const_iterator QStringView::begin() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView5beginEv(
    const QStringView *self) {
  return self->begin();
}

//  const_iterator QStringView::end() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView3endEv(
    const QStringView *self) {
  return self->end();
}

//  const_iterator QStringView::cbegin() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView6cbeginEv(
    const QStringView *self) {
  return self->cbegin();
}

//  const_iterator QStringView::cend() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView4cendEv(
    const QStringView *self) {
  return self->cend();
}

//  const_reverse_iterator QStringView::rbegin() const
extern "C" Q_DECL_EXPORT
QStringView::const_reverse_iterator *ritual_ZNK11QStringView6rbeginEv(
    const QStringView *self) {
  return new QStringView::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QStringView::rend() const
extern "C" Q_DECL_EXPORT
QStringView::const_reverse_iterator *ritual_ZNK11QStringView4rendEv(
    const QStringView *self) {
  return new QStringView::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QStringView::crbegin() const
extern "C" Q_DECL_EXPORT
QStringView::const_reverse_iterator *ritual_ZNK11QStringView7crbeginEv(
    const QStringView *self) {
  return new QStringView::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QStringView::crend() const
extern "C" Q_DECL_EXPORT
QStringView::const_reverse_iterator *ritual_ZNK11QStringView5crendEv(
    const QStringView *self) {
  return new QStringView::const_reverse_iterator(self->crend());
}

//  bool QStringView::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView5emptyEv(const QStringView *self) {
  return self->empty();
}

//  QChar QStringView::front() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringView5frontEv(const QStringView *self) {
  return new QChar(self->front());
}

//  QChar QStringView::back() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringView4backEv(const QStringView *self) {
  return new QChar(self->back());
}

//  std::u16string_view QStringView::operator basic_string_view() const
extern "C" Q_DECL_EXPORT
std::u16string_view *ritual_ZNK11QStringViewcvSt17basic_string_viewIDsSt11char_traitsIDsEEEv(
    const QStringView *self) {
  return new std::u16string_view(self->operator std::u16string_view());
}

//  qsizetype QStringView::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView8max_sizeEv(const QStringView *self) {
  return self->max_size();
}

//  const_iterator QStringView::constBegin() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView10constBeginEv(
    const QStringView *self) {
  return self->constBegin();
}

//  const_iterator QStringView::constEnd() const
extern "C" Q_DECL_EXPORT
QStringView::const_iterator ritual_ZNK11QStringView8constEndEv(
    const QStringView *self) {
  return self->constEnd();
}

//  bool QStringView::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView6isNullEv(const QStringView *self) {
  return self->isNull();
}

//  bool QStringView::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStringView7isEmptyEv(const QStringView *self) {
  return self->isEmpty();
}

//  qsizetype QStringView::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView6lengthEv(const QStringView *self) {
  return self->length();
}

//  QChar QStringView::first() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringView5firstEv(const QStringView *self) {
  return new QChar(self->first());
}

//  QChar QStringView::last() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStringView4lastEv(const QStringView *self) {
  return new QChar(self->last());
}

//  void QStringView::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QStringView6verifyExx(
    const QStringView *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  int QStringView::compare_single_char_helper(int diff) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStringView26compare_single_char_helperEi(
    const QStringView *self,
    int diff) {
  return self->compare_single_char_helper(diff);
}

//  bool QStringView::equal_helper(QStringView sv, const char *data,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QStringView12equal_helperES_PKcx(
    const QString *sv,
    const char *data,
    qsizetype len) {
  return QStringView::equal_helper(QStringView(*sv), data, len);
}

//  int QStringView::compare_helper(QStringView sv, const char *data,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QStringView14compare_helperES_PKcx(
    const QString *sv,
    const char *data,
    qsizetype len) {
  return QStringView::compare_helper(QStringView(*sv), data, len);
}

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator==(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator!=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator<(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator>(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator<=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QStringView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QStringViewRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator>=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator==(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator!=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator<(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator>(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator<=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QByteArrayView &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRK11QStringView(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator>=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator==(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator!=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator<(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator>(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator<=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QStringView &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QStringViewRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator>=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator==(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator!=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator<(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator>(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator<=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QByteArray &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QByteArrayRK11QStringView(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator>=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator==(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator!=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator<(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator>(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator<=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QStringView &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QStringViewRKPKc(
    const QString *lhs,
    const char *const *rhs) {
  return operator>=(QStringView(*lhs), *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator==(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator!=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator<(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator>(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator<=(*lhs, QStringView(*rhs));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const char *const &lhs, const QStringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKPKcRK11QStringView(
    const char *const *lhs,
    const QString *rhs) {
  return operator>=(*lhs, QStringView(*rhs));
}
#endif

//  QStringView::~QStringView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStringViewD1Ev(QStringView *self) {
  delete self;
}

//  QList<QStringView>::QList()
extern "C" Q_DECL_EXPORT
QList<QStringView> *ritual_list_make_QStringView() {
  return new QList<QStringView>();
}

//  void QList<QStringView>::append(const QStringView &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QStringView(
    QList<QStringView> *self,
    const QStringView *element) {
  self->append(*element);
}

//  qsizetype QList<QStringView>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QStringView(const QList<QStringView> *self) {
  return self->size();
}

//  const QStringView &QList<QStringView>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QStringView *ritual_list_at_QStringView(
    const QList<QStringView> *self,
    long long index) {
  return new QStringView(self->at(index));
}

//  QList<QStringView>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QStringView(QList<QStringView> *self) {
  delete self;
}

//  a QList<uint> a ritual of QStringView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringView__QList_uint(QList<uint> *self) {
  delete self;
}

//  a QStringView::const_reverse_iterator a ritual of QStringView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringView__QStringView_const_reverse_iterator(
    QStringView::const_reverse_iterator *self) {
  delete self;
}

//  a std::u16string_view a ritual of QStringView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStringView__std_u16string_view(std::u16string_view *self) {
  delete self;
}

//  QStringView::QStringView<char16_t>(const char16_t *str, qsizetype len)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1IDsLb1EEEPKT_x(
    const char16_t *str,
    qsizetype len) {
  return new QStringView(str, len);
}

//  QStringView::QStringView<char16_t>(const char16_t *f,
//      const char16_t *l)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1IDsLb1EEEPKT_S3_(
    const char16_t *f,
    const char16_t *l) {
  return new QStringView(f, l);
}

//  QStringView::QStringView<const char16_t *>(const char16_t *const
//      &str)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1IPKDsLb1EEERKT_(
    const char16_t *str) {
  return new QStringView(str);
}

//  QStringView::QStringView<QString>(const QString &str)
extern "C" Q_DECL_EXPORT
QStringView *ritual_ZN11QStringViewC1I7QStringLb1EEERKT_(
    const QString *str) {
  return new QStringView(*str);
}

#if QT_CONFIG(regularexpression)
//  qsizetype QStringView::lastIndexOf<QRegularExpressionMatch>(
//      const QRegularExpression &re, QRegularExpressionMatch *rmatch)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QStringView11lastIndexOfI23QRegularExpressionMatchLb0EEExRK18QRegularExpressionPT_(
    const QStringView *self,
    const QRegularExpression *re,
    QRegularExpressionMatch *rmatch) {
  return self->lastIndexOf<QRegularExpressionMatch>(*re, rmatch);
}
#endif  // QT_CONFIG(regularexpression)
