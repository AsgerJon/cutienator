//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefmessage.h>
#include <QtNfc/qndefrecord.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QNdefMessage::QNdefMessage()
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN12QNdefMessageC1Ev() {
  return new QNdefMessage();
}

//  QNdefMessage::QNdefMessage(const QNdefRecord &record)
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN12QNdefMessageC1ERK11QNdefRecord(
    const QNdefRecord *record) {
  return new QNdefMessage(*record);
}

//  QNdefMessage::QNdefMessage(const QNdefMessage &message)
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN12QNdefMessageC1ERKS_(const QNdefMessage *message) {
  return new QNdefMessage(*message);
}

//  QNdefMessage::QNdefMessage(const QList<QNdefRecord> &records)
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN12QNdefMessageC1ERK5QListI11QNdefRecordE(
    const QList<QNdefRecord> *records) {
  return new QNdefMessage(*records);
}

//  bool QNdefMessage::operator==(const QNdefMessage &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QNdefMessageeqERKS_(
    const QNdefMessage *self,
    const QNdefMessage *other) {
  return self->operator==(*other);
}

//  QByteArray QNdefMessage::toByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QNdefMessage11toByteArrayEv(
    const QNdefMessage *self) {
  return new QByteArray(self->toByteArray());
}

//  QNdefMessage QNdefMessage::fromByteArray(const QByteArray &message)
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_ZN12QNdefMessage13fromByteArrayERK10QByteArray(
    const QByteArray *message) {
  return new QNdefMessage(QNdefMessage::fromByteArray(*message));
}

//  QNdefMessage::~QNdefMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNdefMessageD1Ev(QNdefMessage *self) {
  delete self;
}

//  QList<QNdefMessage>::QList()
extern "C" Q_DECL_EXPORT
QList<QNdefMessage> *ritual_list_make_QNdefMessage() {
  return new QList<QNdefMessage>();
}

//  void QList<QNdefMessage>::append(const QNdefMessage &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNdefMessage(
    QList<QNdefMessage> *self,
    const QNdefMessage *element) {
  self->append(*element);
}

//  qsizetype QList<QNdefMessage>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNdefMessage(const QList<QNdefMessage> *self) {
  return self->size();
}

//  const QNdefMessage &QList<QNdefMessage>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNdefMessage *ritual_list_at_QNdefMessage(
    const QList<QNdefMessage> *self,
    long long index) {
  return new QNdefMessage(self->at(index));
}

//  QList<QNdefMessage>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNdefMessage(QList<QNdefMessage> *self) {
  delete self;
}
