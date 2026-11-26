//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/qvoice.h, Qt 6.12.0. Changes made here are lost.
#include <QtTextToSpeech/qvoice.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QVoice::QVoice()
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceC1Ev() {
  return new QVoice();
}

//  QVoice::~QVoice()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QVoiceD1Ev(QVoice *self) {
  delete self;
}

//  QVoice::QVoice(const QVoice &other)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceC1ERKS_(const QVoice *other) {
  return new QVoice(*other);
}

//  QVoice &QVoice::operator=(const QVoice &other)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceaSERKS_(QVoice *self, const QVoice *other) {
  return &(self->operator=(*other));
}

//  QVoice::QVoice(QVoice &&other)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceC1EOS_(QVoice *other) {
  return new QVoice(std::move(*other));
}

//  QVoice &QVoice::operator=(QVoice &&other)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceaSEOS_(QVoice *self, QVoice *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QVoice::swap(QVoice &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QVoice4swapERS_(QVoice *self, QVoice *other) {
  self->swap(*other);
}

//  bool operator==(const QVoice &lhs, const QVoice &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QVoiceS1_(const QVoice *lhs, const QVoice *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QVoice &lhs, const QVoice &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QVoiceS1_(const QVoice *lhs, const QVoice *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &str, const QVoice &voice)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK6QVoice(
    QDataStream *str,
    const QVoice *voice) {
  return &(operator<<(*str, *voice));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &str, QVoice &voice)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR6QVoice(
    QDataStream *str,
    QVoice *voice) {
  return &(operator>>(*str, *voice));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QString QVoice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QVoice4nameEv(const QVoice *self) {
  return new QString(self->name());
}

//  QLocale QVoice::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK6QVoice6localeEv(const QVoice *self) {
  return new QLocale(self->locale());
}

//  Gender QVoice::gender() const
extern "C" Q_DECL_EXPORT
QVoice::Gender ritual_ZNK6QVoice6genderEv(const QVoice *self) {
  return self->gender();
}

//  Age QVoice::age() const
extern "C" Q_DECL_EXPORT
QVoice::Age ritual_ZNK6QVoice3ageEv(const QVoice *self) {
  return self->age();
}

//  QLocale::Language QVoice::language() const
extern "C" Q_DECL_EXPORT
QLocale::Language ritual_ZNK6QVoice8languageEv(const QVoice *self) {
  return self->language();
}

//  QString QVoice::genderName(QVoice::Gender gender)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QVoice10genderNameENS_6GenderE(QVoice::Gender gender) {
  return new QString(QVoice::genderName(gender));
}

//  QString QVoice::ageName(QVoice::Age age)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QVoice7ageNameENS_3AgeE(QVoice::Age age) {
  return new QString(QVoice::ageName(age));
}

//  QVoice::QVoice(const QString &name, const QLocale &loc, Gender gender,
//      Age age, const QVariant &data)
extern "C" Q_DECL_EXPORT
QVoice *ritual_ZN6QVoiceC1ERK7QStringRK7QLocaleNS_6GenderENS_3AgeERK8QVariant(
    const QString *name,
    const QLocale *loc,
    QVoice::Gender gender,
    QVoice::Age age,
    const QVariant *data) {
  return new QVoice(*name, *loc, gender, age, *data);
}

//  bool QVoice::isEqual(const QVoice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QVoice7isEqualERKS_(
    const QVoice *self,
    const QVoice *other) {
  return self->isEqual(*other);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &QVoice::writeTo(QDataStream &a0) const
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZNK6QVoice7writeToER11QDataStream(
    const QVoice *self,
    QDataStream *a0) {
  return &(self->writeTo(*a0));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &QVoice::readFrom(QDataStream &a0)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN6QVoice8readFromER11QDataStream(
    QVoice *self,
    QDataStream *a0) {
  return &(self->readFrom(*a0));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QVariant QVoice::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK6QVoice4dataEv(const QVoice *self) {
  return new QVariant(self->data());
}

//  QDebug operator<<(QDebug a0, const QVoice &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK6QVoice(const QDebug *a0, const QVoice *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  QList<QVoice>::QList()
extern "C" Q_DECL_EXPORT
QList<QVoice> *ritual_list_make_QVoice() {
  return new QList<QVoice>();
}

//  void QList<QVoice>::append(const QVoice &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QVoice(QList<QVoice> *self, const QVoice *element) {
  self->append(*element);
}

//  qsizetype QList<QVoice>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QVoice(const QList<QVoice> *self) {
  return self->size();
}

//  const QVoice &QList<QVoice>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QVoice *ritual_list_at_QVoice(const QList<QVoice> *self, long long index) {
  return new QVoice(self->at(index));
}

//  QList<QVoice>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QVoice(QList<QVoice> *self) {
  delete self;
}
