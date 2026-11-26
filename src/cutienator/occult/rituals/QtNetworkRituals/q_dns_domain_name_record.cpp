//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QDnsDomainNameRecord::QDnsDomainNameRecord()
extern "C" Q_DECL_EXPORT
QDnsDomainNameRecord *ritual_ZN20QDnsDomainNameRecordC1Ev() {
  return new QDnsDomainNameRecord();
}

//  QDnsDomainNameRecord::QDnsDomainNameRecord(const QDnsDomainNameRecord
//      &other)
extern "C" Q_DECL_EXPORT
QDnsDomainNameRecord *ritual_ZN20QDnsDomainNameRecordC1ERKS_(
    const QDnsDomainNameRecord *other) {
  return new QDnsDomainNameRecord(*other);
}

//  QDnsDomainNameRecord
//      &QDnsDomainNameRecord::operator=(QDnsDomainNameRecord &&other)
extern "C" Q_DECL_EXPORT
QDnsDomainNameRecord *ritual_ZN20QDnsDomainNameRecordaSEOS_(
    QDnsDomainNameRecord *self,
    QDnsDomainNameRecord *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDnsDomainNameRecord &QDnsDomainNameRecord::operator=(const
//      QDnsDomainNameRecord &other)
extern "C" Q_DECL_EXPORT
QDnsDomainNameRecord *ritual_ZN20QDnsDomainNameRecordaSERKS_(
    QDnsDomainNameRecord *self,
    const QDnsDomainNameRecord *other) {
  return &(self->operator=(*other));
}

//  QDnsDomainNameRecord::~QDnsDomainNameRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDnsDomainNameRecordD1Ev(QDnsDomainNameRecord *self) {
  delete self;
}

//  void QDnsDomainNameRecord::swap(QDnsDomainNameRecord &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDnsDomainNameRecord4swapERS_(
    QDnsDomainNameRecord *self,
    QDnsDomainNameRecord *other) {
  self->swap(*other);
}

//  QString QDnsDomainNameRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDnsDomainNameRecord4nameEv(
    const QDnsDomainNameRecord *self) {
  return new QString(self->name());
}

//  quint32 QDnsDomainNameRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QDnsDomainNameRecord10timeToLiveEv(
    const QDnsDomainNameRecord *self) {
  return self->timeToLive();
}

//  QString QDnsDomainNameRecord::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDnsDomainNameRecord5valueEv(
    const QDnsDomainNameRecord *self) {
  return new QString(self->value());
}

//  QList<QDnsDomainNameRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsDomainNameRecord> *ritual_list_make_QDnsDomainNameRecord() {
  return new QList<QDnsDomainNameRecord>();
}

//  void QList<QDnsDomainNameRecord>::append(const QDnsDomainNameRecord
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsDomainNameRecord(
    QList<QDnsDomainNameRecord> *self,
    const QDnsDomainNameRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsDomainNameRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsDomainNameRecord(
    const QList<QDnsDomainNameRecord> *self) {
  return self->size();
}

//  const QDnsDomainNameRecord &QList<QDnsDomainNameRecord>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QDnsDomainNameRecord *ritual_list_at_QDnsDomainNameRecord(
    const QList<QDnsDomainNameRecord> *self,
    long long index) {
  return new QDnsDomainNameRecord(self->at(index));
}

//  QList<QDnsDomainNameRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsDomainNameRecord(
    QList<QDnsDomainNameRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
