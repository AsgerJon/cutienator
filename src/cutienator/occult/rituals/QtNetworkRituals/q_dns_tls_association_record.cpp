//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dnslookup)
#if QT_CONFIG(dnslookup)
#include <QtNetwork/qdnslookup.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QDnsTlsAssociationRecord::QDnsTlsAssociationRecord()
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_ZN24QDnsTlsAssociationRecordC1Ev() {
  return new QDnsTlsAssociationRecord();
}

//  QDnsTlsAssociationRecord::QDnsTlsAssociationRecord(const
//      QDnsTlsAssociationRecord &other)
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_ZN24QDnsTlsAssociationRecordC1ERKS_(
    const QDnsTlsAssociationRecord *other) {
  return new QDnsTlsAssociationRecord(*other);
}

//  QDnsTlsAssociationRecord::QDnsTlsAssociationRecord(QDnsTlsAssociationReco
//      rd &&other)
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_ZN24QDnsTlsAssociationRecordC1EOS_(
    QDnsTlsAssociationRecord *other) {
  return new QDnsTlsAssociationRecord(std::move(*other));
}

//  QDnsTlsAssociationRecord
//      &QDnsTlsAssociationRecord::operator=(QDnsTlsAssociationRecord
//      &&other)
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_ZN24QDnsTlsAssociationRecordaSEOS_(
    QDnsTlsAssociationRecord *self,
    QDnsTlsAssociationRecord *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDnsTlsAssociationRecord &QDnsTlsAssociationRecord::operator=(const
//      QDnsTlsAssociationRecord &other)
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_ZN24QDnsTlsAssociationRecordaSERKS_(
    QDnsTlsAssociationRecord *self,
    const QDnsTlsAssociationRecord *other) {
  return &(self->operator=(*other));
}

//  QDnsTlsAssociationRecord::~QDnsTlsAssociationRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDnsTlsAssociationRecordD1Ev(
    QDnsTlsAssociationRecord *self) {
  delete self;
}

//  void QDnsTlsAssociationRecord::swap(QDnsTlsAssociationRecord &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDnsTlsAssociationRecord4swapERS_(
    QDnsTlsAssociationRecord *self,
    QDnsTlsAssociationRecord *other) {
  self->swap(*other);
}

//  QString QDnsTlsAssociationRecord::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QDnsTlsAssociationRecord4nameEv(
    const QDnsTlsAssociationRecord *self) {
  return new QString(self->name());
}

//  quint32 QDnsTlsAssociationRecord::timeToLive() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QDnsTlsAssociationRecord10timeToLiveEv(
    const QDnsTlsAssociationRecord *self) {
  return self->timeToLive();
}

//  CertificateUsage QDnsTlsAssociationRecord::usage() const
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord::CertificateUsage ritual_ZNK24QDnsTlsAssociationRecord5usageEv(
    const QDnsTlsAssociationRecord *self) {
  return self->usage();
}

//  Selector QDnsTlsAssociationRecord::selector() const
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord::Selector ritual_ZNK24QDnsTlsAssociationRecord8selectorEv(
    const QDnsTlsAssociationRecord *self) {
  return self->selector();
}

//  MatchingType QDnsTlsAssociationRecord::matchType() const
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord::MatchingType ritual_ZNK24QDnsTlsAssociationRecord9matchTypeEv(
    const QDnsTlsAssociationRecord *self) {
  return self->matchType();
}

//  QByteArray QDnsTlsAssociationRecord::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QDnsTlsAssociationRecord5valueEv(
    const QDnsTlsAssociationRecord *self) {
  return new QByteArray(self->value());
}

//  QList<QDnsTlsAssociationRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QDnsTlsAssociationRecord> *ritual_list_make_QDnsTlsAssociationRecord() {
  return new QList<QDnsTlsAssociationRecord>();
}

//  void QList<QDnsTlsAssociationRecord>::append(const
//      QDnsTlsAssociationRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDnsTlsAssociationRecord(
    QList<QDnsTlsAssociationRecord> *self,
    const QDnsTlsAssociationRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QDnsTlsAssociationRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDnsTlsAssociationRecord(
    const QList<QDnsTlsAssociationRecord> *self) {
  return self->size();
}

//  const QDnsTlsAssociationRecord
//      &QList<QDnsTlsAssociationRecord>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDnsTlsAssociationRecord *ritual_list_at_QDnsTlsAssociationRecord(
    const QList<QDnsTlsAssociationRecord> *self,
    long long index) {
  return new QDnsTlsAssociationRecord(self->at(index));
}

//  QList<QDnsTlsAssociationRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDnsTlsAssociationRecord(
    QList<QDnsTlsAssociationRecord> *self) {
  delete self;
}

#endif  // QT_CONFIG(dnslookup)
#endif  // QT_CONFIG(dnslookup)
