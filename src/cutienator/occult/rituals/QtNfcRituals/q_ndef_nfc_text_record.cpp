//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefnfctextrecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefnfctextrecord.h>
#include <QtNfc/qndefrecord.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

#if !defined(Q_QDOC)
//  QNdefNfcTextRecord::QNdefNfcTextRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcTextRecord *ritual_ZN18QNdefNfcTextRecordC1Ev() {
  return new QNdefNfcTextRecord();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QNdefNfcTextRecord::QNdefNfcTextRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcTextRecord *ritual_ZN18QNdefNfcTextRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcTextRecord(*other);
}
#endif  // !defined(Q_QDOC)

//  QString QNdefNfcTextRecord::locale() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QNdefNfcTextRecord6localeEv(
    const QNdefNfcTextRecord *self) {
  return new QString(self->locale());
}

//  void QNdefNfcTextRecord::setLocale(const QString &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTextRecord9setLocaleERK7QString(
    QNdefNfcTextRecord *self,
    const QString *locale) {
  self->setLocale(*locale);
}

//  QString QNdefNfcTextRecord::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QNdefNfcTextRecord4textEv(
    const QNdefNfcTextRecord *self) {
  return new QString(self->text());
}

//  void QNdefNfcTextRecord::setText(const QString text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTextRecord7setTextE7QString(
    QNdefNfcTextRecord *self,
    const QString *text) {
  self->setText(*text);
}

//  Encoding QNdefNfcTextRecord::encoding() const
extern "C" Q_DECL_EXPORT
QNdefNfcTextRecord::Encoding ritual_ZNK18QNdefNfcTextRecord8encodingEv(
    const QNdefNfcTextRecord *self) {
  return self->encoding();
}

//  void QNdefNfcTextRecord::setEncoding(Encoding encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTextRecord11setEncodingENS_8EncodingE(
    QNdefNfcTextRecord *self,
    QNdefNfcTextRecord::Encoding encoding) {
  self->setEncoding(encoding);
}

//  QNdefNfcTextRecord::~QNdefNfcTextRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcTextRecordD1Ev(QNdefNfcTextRecord *self) {
  delete self;
}

//  QList<QNdefNfcTextRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QNdefNfcTextRecord> *ritual_list_make_QNdefNfcTextRecord() {
  return new QList<QNdefNfcTextRecord>();
}

//  void QList<QNdefNfcTextRecord>::append(const QNdefNfcTextRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNdefNfcTextRecord(
    QList<QNdefNfcTextRecord> *self,
    const QNdefNfcTextRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QNdefNfcTextRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNdefNfcTextRecord(
    const QList<QNdefNfcTextRecord> *self) {
  return self->size();
}

//  const QNdefNfcTextRecord &QList<QNdefNfcTextRecord>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QNdefNfcTextRecord *ritual_list_at_QNdefNfcTextRecord(
    const QList<QNdefNfcTextRecord> *self,
    long long index) {
  return new QNdefNfcTextRecord(self->at(index));
}

//  QList<QNdefNfcTextRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNdefNfcTextRecord(QList<QNdefNfcTextRecord> *self) {
  delete self;
}
