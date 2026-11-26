//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QDnsMailExchangeRecord::QDnsMailExchangeRecord()
extern "C" Q_DECL_EXPORT
QDnsMailExchangeRecord *ritual_ZN22QDnsMailExchangeRecordC1Ev() {
  return new QDnsMailExchangeRecord();
}

//  QDnsMailExchangeRecord::QDnsMailExchangeRecord(const
//      QDnsMailExchangeRecord &other)
extern "C" Q_DECL_EXPORT
QDnsMailExchangeRecord *ritual_ZN22QDnsMailExchangeRecordC1ERKS_(
    const QDnsMailExchangeRecord *other) {
  return new QDnsMailExchangeRecord(*other);
}

//  QDnsMailExchangeRecord
//      &QDnsMailExchangeRecord::operator=(QDnsMailExchangeRecord &&other)
extern "C" Q_DECL_EXPORT
QDnsMailExchangeRecord *ritual_ZN22QDnsMailExchangeRecordaSEOS_(
    QDnsMailExchangeRecord *self,
    QDnsMailExchangeRecord *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDnsMailExchangeRecord &QDnsMailExchangeRecord::operator=(const
//      QDnsMailExchangeRecord &other)
extern "C" Q_DECL_EXPORT
QDnsMailExchangeRecord *ritual_ZN22QDnsMailExchangeRecordaSERKS_(
    QDnsMailExchangeRecord *self,
    const QDnsMailExchangeRecord *other) {
  return &(self->operator=(*other));
}

//  QDnsMailExchangeRecord::~QDnsMailExchangeRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDnsMailExchangeRecordD1Ev(QDnsMailExchangeRecord *self) {
  delete self;
}

//  void QDnsMailExchangeRecord::swap(QDnsMailExchangeRecord &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDnsMailExchangeRecord4swapERS_(
    QDnsMailExchangeRecord *self,
    QDnsMailExchangeRecord *other) {
  self->swap(*other);
}

//  QString QDnsMailExchangeRecord::exchange() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDnsMailExchangeRecord8exchangeEv(
    const QDnsMailExchangeRecord *self) {
  return new QString(self->exchange());
}

//  QString QDnsMailExchangeRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDnsMailExchangeRecord4nameEv(
    const QDnsMailExchangeRecord *self) {
  return new QString(self->name());
}

//  quint16 QDnsMailExchangeRecord::preference() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK22QDnsMailExchangeRecord10preferenceEv(
    const QDnsMailExchangeRecord *self) {
  return self->preference();
}

//  quint32 QDnsMailExchangeRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK22QDnsMailExchangeRecord10timeToLiveEv(
    const QDnsMailExchangeRecord *self) {
  return self->timeToLive();
}

//  QList<QDnsMailExchangeRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsMailExchangeRecord> *ritual_list_make_QDnsMailExchangeRecord() {
  return new QList<QDnsMailExchangeRecord>();
}

//  void QList<QDnsMailExchangeRecord>::append(const QDnsMailExchangeRecord
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsMailExchangeRecord(
    QList<QDnsMailExchangeRecord> *self,
    const QDnsMailExchangeRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsMailExchangeRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsMailExchangeRecord(
    const QList<QDnsMailExchangeRecord> *self) {
  return self->size();
}

//  const QDnsMailExchangeRecord &QList<QDnsMailExchangeRecord>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QDnsMailExchangeRecord *ritual_list_at_QDnsMailExchangeRecord(
    const QList<QDnsMailExchangeRecord> *self,
    long long index) {
  return new QDnsMailExchangeRecord(self->at(index));
}

//  QList<QDnsMailExchangeRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsMailExchangeRecord(
    QList<QDnsMailExchangeRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
