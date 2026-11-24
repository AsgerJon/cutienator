//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QDnsServiceRecord::QDnsServiceRecord()
extern "C" Q_DECL_EXPORT
QDnsServiceRecord *ritual_ZN17QDnsServiceRecordC1Ev() {
  return new QDnsServiceRecord();
}

//  QDnsServiceRecord::QDnsServiceRecord(const QDnsServiceRecord &other)
extern "C" Q_DECL_EXPORT
QDnsServiceRecord *ritual_ZN17QDnsServiceRecordC1ERKS_(
    const QDnsServiceRecord *other) {
  return new QDnsServiceRecord(*other);
}

//  QDnsServiceRecord::~QDnsServiceRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDnsServiceRecordD1Ev(QDnsServiceRecord *self) {
  delete self;
}

//  QString QDnsServiceRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDnsServiceRecord4nameEv(
    const QDnsServiceRecord *self) {
  return new QString(self->name());
}

//  quint16 QDnsServiceRecord::port() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK17QDnsServiceRecord4portEv(const QDnsServiceRecord *self) {
  return self->port();
}

//  quint16 QDnsServiceRecord::priority() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK17QDnsServiceRecord8priorityEv(
    const QDnsServiceRecord *self) {
  return self->priority();
}

//  QString QDnsServiceRecord::target() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDnsServiceRecord6targetEv(
    const QDnsServiceRecord *self) {
  return new QString(self->target());
}

//  quint32 QDnsServiceRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK17QDnsServiceRecord10timeToLiveEv(
    const QDnsServiceRecord *self) {
  return self->timeToLive();
}

//  quint16 QDnsServiceRecord::weight() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK17QDnsServiceRecord6weightEv(
    const QDnsServiceRecord *self) {
  return self->weight();
}

//  QList<QDnsServiceRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsServiceRecord> *ritual_list_make_QDnsServiceRecord() {
  return new QList<QDnsServiceRecord>();
}

//  void QList<QDnsServiceRecord>::append(const QDnsServiceRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsServiceRecord(
    QList<QDnsServiceRecord> *self,
    const QDnsServiceRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsServiceRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsServiceRecord(
    const QList<QDnsServiceRecord> *self) {
  return self->size();
}

//  const QDnsServiceRecord &QList<QDnsServiceRecord>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDnsServiceRecord *ritual_list_at_QDnsServiceRecord(
    const QList<QDnsServiceRecord> *self,
    long long index) {
  return new QDnsServiceRecord(self->at(index));
}

//  QList<QDnsServiceRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsServiceRecord(QList<QDnsServiceRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
