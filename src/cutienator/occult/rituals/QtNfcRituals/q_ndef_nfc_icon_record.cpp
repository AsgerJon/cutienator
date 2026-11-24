//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefnfcsmartposterrecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefnfcsmartposterrecord.h>
#include <QtNfc/qndefrecord.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QNdefNfcIconRecord::QNdefNfcIconRecord()
extern "C" Q_DECL_EXPORT
QNdefNfcIconRecord *ritual_ZN18QNdefNfcIconRecordC1Ev() {
  return new QNdefNfcIconRecord();
}

//  QNdefNfcIconRecord::QNdefNfcIconRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefNfcIconRecord *ritual_ZN18QNdefNfcIconRecordC1ERK11QNdefRecord(
    const QNdefRecord *other) {
  return new QNdefNfcIconRecord(*other);
}

//  void QNdefNfcIconRecord::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcIconRecord7setDataERK10QByteArray(
    QNdefNfcIconRecord *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  QByteArray QNdefNfcIconRecord::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QNdefNfcIconRecord4dataEv(
    const QNdefNfcIconRecord *self) {
  return new QByteArray(self->data());
}

//  QNdefNfcIconRecord::~QNdefNfcIconRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefNfcIconRecordD1Ev(QNdefNfcIconRecord *self) {
  delete self;
}

//  QList<QNdefNfcIconRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QNdefNfcIconRecord> *ritual_list_make_QNdefNfcIconRecord() {
  return new QList<QNdefNfcIconRecord>();
}

//  void QList<QNdefNfcIconRecord>::append(const QNdefNfcIconRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNdefNfcIconRecord(
    QList<QNdefNfcIconRecord> *self,
    const QNdefNfcIconRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QNdefNfcIconRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNdefNfcIconRecord(
    const QList<QNdefNfcIconRecord> *self) {
  return self->size();
}

//  const QNdefNfcIconRecord &QList<QNdefNfcIconRecord>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QNdefNfcIconRecord *ritual_list_at_QNdefNfcIconRecord(
    const QList<QNdefNfcIconRecord> *self,
    long long index) {
  return new QNdefNfcIconRecord(self->at(index));
}

//  QList<QNdefNfcIconRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNdefNfcIconRecord(QList<QNdefNfcIconRecord> *self) {
  delete self;
}
