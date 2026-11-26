//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdebug.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 19. Kept as it is when the generator
//  runs again.
#include <QtCore/qdebug.h>
#include <QtCore/qcompare.h>
#include <QtCore/qchar.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qtextstream.h>
#include <QtCore/QUtf8StringView>
#include <chrono>

//  void QDebug::putUcs4(uint ucs4)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug7putUcs4Ej(QDebug *self, uint ucs4) {
  self->putUcs4(ucs4);
}

//  void QDebug::putString(const QChar *begin, size_t length)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug9putStringEPK5QCharm(
    QDebug *self,
    const QChar *begin,
    size_t length) {
  self->putString(begin, length);
}

//  void QDebug::putByteArray(const char *begin, size_t length, Latin1Content
//      content)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug12putByteArrayEPKcmNS_13Latin1ContentE(
    QDebug *self,
    const char *begin,
    size_t length,
    QDebug::Latin1Content content) {
  self->putByteArray(begin, length, content);
}

//  void QDebug::putTimeUnit(qint64 num, qint64 den)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug11putTimeUnitExx(QDebug *self, qint64 num, qint64 den) {
  self->putTimeUnit(num, den);
}

//  void QDebug::putInt128(const void *i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug9putInt128EPKv(QDebug *self, const void *i) {
  self->putInt128(i);
}

//  void QDebug::putUInt128(const void *i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug10putUInt128EPKv(QDebug *self, const void *i) {
  self->putUInt128(i);
}

//  void QDebug::putQtOrdering(QtOrderingPrivate::QtOrderingTypeFlag flags,
//      Qt::partial_ordering order)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug13putQtOrderingE6QFlagsIN17QtOrderingPrivate14QtOrderingTypeEEN2Qt16partial_orderingE(
    QDebug *self,
    int flags,
    const Qt::partial_ordering *order) {
  self->putQtOrdering(
      QFlags<QtOrderingPrivate::QtOrderingType>::fromInt(flags),
      *order);
}

//  QDebug::QDebug(QIODevice *device)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP9QIODevice(QIODevice *device) {
  return new QDebug(device);
}

//  QDebug::QDebug(QString *string)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP7QString(QString *string) {
  return new QDebug(string);
}

//  QDebug::QDebug(QByteArray *bytes)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EP10QByteArray(QByteArray *bytes) {
  return new QDebug(bytes);
}

//  QDebug::QDebug(QtMsgType t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1E9QtMsgType(QtMsgType t) {
  return new QDebug(t);
}

//  QDebug::QDebug(const QDebug &o)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1ERKS_(const QDebug *o) {
  return new QDebug(*o);
}

//  QDebug::QDebug(QDebug &&other)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugC1EOS_(QDebug *other) {
  return new QDebug(std::move(*other));
}

//  QDebug &QDebug::operator=(const QDebug &other)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugaSERKS_(QDebug *self, const QDebug *other) {
  return &(self->operator=(*other));
}

//  QDebug &QDebug::operator=(QDebug &&other)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebugaSEOS_(QDebug *self, QDebug *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDebug::~QDebug()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebugD1Ev(QDebug *self) {
  delete self;
}

//  void QDebug::swap(QDebug &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug4swapERS_(QDebug *self, QDebug *other) {
  self->swap(*other);
}

//  QDebug &QDebug::resetFormat()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug11resetFormatEv(QDebug *self) {
  return &(self->resetFormat());
}

//  QDebug &QDebug::space()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug5spaceEv(QDebug *self) {
  return &(self->space());
}

//  QDebug &QDebug::nospace()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug7nospaceEv(QDebug *self) {
  return &(self->nospace());
}

//  QDebug &QDebug::maybeSpace()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug10maybeSpaceEv(QDebug *self) {
  return &(self->maybeSpace());
}

//  QDebug &QDebug::verbosity(int verbosityLevel)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug9verbosityEi(QDebug *self, int verbosityLevel) {
  return &(self->verbosity(verbosityLevel));
}

//  int QDebug::verbosity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QDebug9verbosityEv(const QDebug *self) {
  return self->verbosity();
}

//  void QDebug::setVerbosity(int verbosityLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug12setVerbosityEi(QDebug *self, int verbosityLevel) {
  self->setVerbosity(verbosityLevel);
}

//  bool QDebug::autoInsertSpaces() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QDebug16autoInsertSpacesEv(const QDebug *self) {
  return self->autoInsertSpaces();
}

//  void QDebug::setAutoInsertSpaces(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug19setAutoInsertSpacesEb(QDebug *self, bool b) {
  self->setAutoInsertSpaces(b);
}

//  bool QDebug::quoteStrings() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QDebug12quoteStringsEv(const QDebug *self) {
  return self->quoteStrings();
}

//  void QDebug::setQuoteStrings(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug15setQuoteStringsEb(QDebug *self, bool b) {
  self->setQuoteStrings(b);
}

//  QDebug &QDebug::quote()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug5quoteEv(QDebug *self) {
  return &(self->quote());
}

//  QDebug &QDebug::noquote()
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug7noquoteEv(QDebug *self) {
  return &(self->noquote());
}

//  QDebug &QDebug::maybeQuote(char c)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug10maybeQuoteEc(QDebug *self, char c) {
  return &(self->maybeQuote(c));
}

//  QDebug &QDebug::operator<<(QChar t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE5QChar(QDebug *self, const QChar *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(bool t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEb(QDebug *self, bool t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(char t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEc(QDebug *self, char t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(short t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEs(QDebug *self, short t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(unsigned short t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEt(QDebug *self, unsigned short t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(char16_t t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEDs(QDebug *self, char16_t t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(char32_t t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEDi(QDebug *self, char32_t t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(int t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEi(QDebug *self, int t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(unsigned int t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEj(QDebug *self, unsigned int t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(long t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEl(QDebug *self, long t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(unsigned long t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEm(QDebug *self, unsigned long t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(qint64 t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEx(QDebug *self, qint64 t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(quint64 t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEy(QDebug *self, quint64 t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(qfloat16 t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE8qfloat16(QDebug *self, const qfloat16 *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(float t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEf(QDebug *self, float t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(double t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEd(QDebug *self, double t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(const char *t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEPKc(QDebug *self, const char *t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(const char16_t *t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEPKDs(QDebug *self, const char16_t *t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(const QString &t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsERK7QString(QDebug *self, const QString *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(QStringView s)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE11QStringView(QDebug *self, const QString *s) {
  return &(self->operator<<(QStringView(*s)));
}

//  QDebug &QDebug::operator<<(QUtf8StringView s)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE20QBasicUtf8StringViewILb0EE(
    QDebug *self,
    const QUtf8StringView *s) {
  return &(self->operator<<(*s));
}

//  QDebug &QDebug::operator<<(QLatin1StringView t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE13QLatin1String(
    QDebug *self,
    const QLatin1String *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(const QByteArray &t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsERK10QByteArray(
    QDebug *self,
    const QByteArray *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(QByteArrayView t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE14QByteArrayView(
    QDebug *self,
    const QByteArrayView *t) {
  return &(self->operator<<(*t));
}

//  QDebug &QDebug::operator<<(const void *t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEPKv(QDebug *self, const void *t) {
  return &(self->operator<<(t));
}

//  QDebug &QDebug::operator<<(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEDn(QDebug *self) {
  return &(self->operator<<(nullptr));
}

//  QDebug &QDebug::operator<<(std::nullopt_t a0)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsESt9nullopt_t(
    QDebug *self,
    const std::nullopt_t *a0) {
  return &(self->operator<<(*a0));
}

//  QDebug &QDebug::operator<<(QTextStreamFunction f)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsEPFR11QTextStreamS1_E(QDebug *self, void *f) {
  return &(self->operator<<(reinterpret_cast<QTextStreamFunction>(f)));
}

//  QDebug &QDebug::operator<<(QTextStreamManipulator m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsE22QTextStreamManipulator(
    QDebug *self,
    const QTextStreamManipulator *m) {
  return &(self->operator<<(*m));
}

//  QString QDebug::toStringImpl(StreamTypeErased s, const void *obj)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug12toStringImplEPFvRS_PKvES2_(
    void *s,
    const void *obj) {
  return new QString(
      QDebug::toStringImpl(
          reinterpret_cast<QDebug::StreamTypeErased>(s),
          obj));
}

//  QByteArray QDebug::toBytesImpl(StreamTypeErased s, const void *obj)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug11toBytesImplEPFvRS_PKvES2_(
    void *s,
    const void *obj) {
  return new QByteArray(
      QDebug::toBytesImpl(
          reinterpret_cast<QDebug::StreamTypeErased>(s),
          obj));
}

//  QDebug &QDebug::putTupleLikeImplImpl(const char *ns, const char *what,
//      size_t n, StreamTypeErased *ops, const void **data)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebug20putTupleLikeImplImplEPKcS1_mPPFvRS_PKvEPS4_(
    QDebug *self,
    const char *ns,
    const char *what,
    size_t n,
    QDebug::StreamTypeErased *ops,
    const void **data) {
  return &(self->putTupleLikeImplImpl(ns, what, n, ops, data));
}

//  static QString QDebug::toString<int>(const int &object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug8toStringIiEE7QStringRKT_(const int *object) {
  return new QString(QDebug::toString(*object));
}

//  static QString QDebug::toString<double>(const double &object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug8toStringIdEE7QStringRKT_(const double *object) {
  return new QString(QDebug::toString(*object));
}

//  static QString QDebug::toString<bool>(const bool &object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug8toStringIbEE7QStringRKT_(const bool *object) {
  return new QString(QDebug::toString(*object));
}

//  static QString QDebug::toString<QString>(const QString &object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug8toStringI7QStringEES1_RKT_(const QString *object) {
  return new QString(QDebug::toString(*object));
}

//  static QString QDebug::toString<QByteArray>(const QByteArray &object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QDebug8toStringI10QByteArrayEE7QStringRKT_(const QByteArray *object) {
  return new QString(QDebug::toString(*object));
}

//  static QByteArray QDebug::toBytes<int>(const int &object)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug7toBytesIiEE10QByteArrayRKT_(const int *object) {
  return new QByteArray(QDebug::toBytes(*object));
}

//  static QByteArray QDebug::toBytes<double>(const double &object)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug7toBytesIdEE10QByteArrayRKT_(const double *object) {
  return new QByteArray(QDebug::toBytes(*object));
}

//  static QByteArray QDebug::toBytes<bool>(const bool &object)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug7toBytesIbEE10QByteArrayRKT_(const bool *object) {
  return new QByteArray(QDebug::toBytes(*object));
}

//  static QByteArray QDebug::toBytes<QString>(const QString &object)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug7toBytesI7QStringEE10QByteArrayRKT_(const QString *object) {
  return new QByteArray(QDebug::toBytes(*object));
}

//  static QByteArray QDebug::toBytes<QByteArray>(const QByteArray &object)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN6QDebug7toBytesI10QByteArrayEES1_RKT_(const QByteArray *object) {
  return new QByteArray(QDebug::toBytes(*object));
}

//  static void QDebug::streamTypeErased<int>(QDebug &d, const void *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug16streamTypeErasedIiEEvRS_PKv(QDebug *d, const void *obj) {
  QDebug::streamTypeErased<int>(*d, obj);
}

//  static void QDebug::streamTypeErased<double>(QDebug &d, const void *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug16streamTypeErasedIdEEvRS_PKv(QDebug *d, const void *obj) {
  QDebug::streamTypeErased<double>(*d, obj);
}

//  static void QDebug::streamTypeErased<bool>(QDebug &d, const void *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug16streamTypeErasedIbEEvRS_PKv(QDebug *d, const void *obj) {
  QDebug::streamTypeErased<bool>(*d, obj);
}

//  static void QDebug::streamTypeErased<QString>(QDebug &d, const void *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug16streamTypeErasedI7QStringEEvRS_PKv(QDebug *d, const void *obj) {
  QDebug::streamTypeErased<QString>(*d, obj);
}

//  static void QDebug::streamTypeErased<QByteArray>(QDebug &d, const void *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QDebug16streamTypeErasedI10QByteArrayEEvRS_PKv(QDebug *d, const void *obj) {
  QDebug::streamTypeErased<QByteArray>(*d, obj);
}

//  QDebug &QDebug::operator<<<long, std::ratio<1l, 1000l> >(
//      std::chrono::duration<long, std::ratio<1l, 1000l> > duration)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QDebuglsIlSt5ratioILl1ELl1000EEEERS_NSt6chrono8durationIT_T0_EE(QDebug *self, long long duration) {
  return &(*self << std::chrono::milliseconds(duration));
}

//  QDebug operator<<<Qt::partial_ordering, true>(QDebug debug, Qt::partial_ordering t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZlsIN2Qt16partial_orderingELb1EE6QDebugS2_T_(QDebug *self, const Qt::partial_ordering *t) {
  return new QDebug(*self << *t);
}

//  QDebug operator<<<Qt::weak_ordering, true>(QDebug debug, Qt::weak_ordering t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZlsIN2Qt13weak_orderingELb1EE6QDebugS2_T_(QDebug *self, const Qt::weak_ordering *t) {
  return new QDebug(*self << *t);
}

//  QDebug operator<<<Qt::strong_ordering, true>(QDebug debug, Qt::strong_ordering t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZlsIN2Qt15strong_orderingELb1EE6QDebugS2_T_(QDebug *self, const Qt::strong_ordering *t) {
  return new QDebug(*self << *t);
}
