//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qlist.h>

//  QDnsHostAddressRecord::QDnsHostAddressRecord()
extern "C" Q_DECL_EXPORT
QDnsHostAddressRecord *ritual_ZN21QDnsHostAddressRecordC1Ev() {
  return new QDnsHostAddressRecord();
}

//  QDnsHostAddressRecord::QDnsHostAddressRecord(const QDnsHostAddressRecord
//      &other)
extern "C" Q_DECL_EXPORT
QDnsHostAddressRecord *ritual_ZN21QDnsHostAddressRecordC1ERKS_(
    const QDnsHostAddressRecord *other) {
  return new QDnsHostAddressRecord(*other);
}

//  QDnsHostAddressRecord::~QDnsHostAddressRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDnsHostAddressRecordD1Ev(QDnsHostAddressRecord *self) {
  delete self;
}

//  QString QDnsHostAddressRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QDnsHostAddressRecord4nameEv(
    const QDnsHostAddressRecord *self) {
  return new QString(self->name());
}

//  quint32 QDnsHostAddressRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK21QDnsHostAddressRecord10timeToLiveEv(
    const QDnsHostAddressRecord *self) {
  return self->timeToLive();
}

//  QHostAddress QDnsHostAddressRecord::value() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK21QDnsHostAddressRecord5valueEv(
    const QDnsHostAddressRecord *self) {
  return new QHostAddress(self->value());
}

//  QList<QDnsHostAddressRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsHostAddressRecord> *ritual_list_make_QDnsHostAddressRecord() {
  return new QList<QDnsHostAddressRecord>();
}

//  void QList<QDnsHostAddressRecord>::append(const QDnsHostAddressRecord
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsHostAddressRecord(
    QList<QDnsHostAddressRecord> *self,
    const QDnsHostAddressRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsHostAddressRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsHostAddressRecord(
    const QList<QDnsHostAddressRecord> *self) {
  return self->size();
}

//  const QDnsHostAddressRecord &QList<QDnsHostAddressRecord>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QDnsHostAddressRecord *ritual_list_at_QDnsHostAddressRecord(
    const QList<QDnsHostAddressRecord> *self,
    long long index) {
  return new QDnsHostAddressRecord(self->at(index));
}

//  QList<QDnsHostAddressRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsHostAddressRecord(
    QList<QDnsHostAddressRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
