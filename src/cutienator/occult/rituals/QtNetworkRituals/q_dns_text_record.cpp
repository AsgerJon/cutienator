//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QDnsTextRecord::QDnsTextRecord()
extern "C" Q_DECL_EXPORT
QDnsTextRecord *ritual_ZN14QDnsTextRecordC1Ev() {
  return new QDnsTextRecord();
}

//  QDnsTextRecord::QDnsTextRecord(const QDnsTextRecord &other)
extern "C" Q_DECL_EXPORT
QDnsTextRecord *ritual_ZN14QDnsTextRecordC1ERKS_(
    const QDnsTextRecord *other) {
  return new QDnsTextRecord(*other);
}

//  QDnsTextRecord::~QDnsTextRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDnsTextRecordD1Ev(QDnsTextRecord *self) {
  delete self;
}

//  QString QDnsTextRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDnsTextRecord4nameEv(const QDnsTextRecord *self) {
  return new QString(self->name());
}

//  quint32 QDnsTextRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QDnsTextRecord10timeToLiveEv(
    const QDnsTextRecord *self) {
  return self->timeToLive();
}

//  QList<QByteArray> QDnsTextRecord::values() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK14QDnsTextRecord6valuesEv(
    const QDnsTextRecord *self) {
  return new QList<QByteArray>(self->values());
}

//  QList<QDnsTextRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsTextRecord> *ritual_list_make_QDnsTextRecord() {
  return new QList<QDnsTextRecord>();
}

//  void QList<QDnsTextRecord>::append(const QDnsTextRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsTextRecord(
    QList<QDnsTextRecord> *self,
    const QDnsTextRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsTextRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsTextRecord(
    const QList<QDnsTextRecord> *self) {
  return self->size();
}

//  const QDnsTextRecord &QList<QDnsTextRecord>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDnsTextRecord *ritual_list_at_QDnsTextRecord(
    const QList<QDnsTextRecord> *self,
    long long index) {
  return new QDnsTextRecord(self->at(index));
}

//  QList<QDnsTextRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsTextRecord(QList<QDnsTextRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
