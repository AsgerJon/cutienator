//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qndefrecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qndefrecord.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QNdefRecord::QNdefRecord()
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_ZN11QNdefRecordC1Ev() {
  return new QNdefRecord();
}

//  QNdefRecord::~QNdefRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecordD1Ev(QNdefRecord *self) {
  delete self;
}

//  QNdefRecord::QNdefRecord(const QNdefRecord &other)
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_ZN11QNdefRecordC1ERKS_(const QNdefRecord *other) {
  return new QNdefRecord(*other);
}

//  void QNdefRecord::setTypeNameFormat(TypeNameFormat typeNameFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecord17setTypeNameFormatENS_14TypeNameFormatE(
    QNdefRecord *self,
    QNdefRecord::TypeNameFormat typeNameFormat) {
  self->setTypeNameFormat(typeNameFormat);
}

//  TypeNameFormat QNdefRecord::typeNameFormat() const
extern "C" Q_DECL_EXPORT
QNdefRecord::TypeNameFormat ritual_ZNK11QNdefRecord14typeNameFormatEv(
    const QNdefRecord *self) {
  return self->typeNameFormat();
}

//  void QNdefRecord::setType(const QByteArray &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecord7setTypeERK10QByteArray(
    QNdefRecord *self,
    const QByteArray *type) {
  self->setType(*type);
}

//  QByteArray QNdefRecord::type() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QNdefRecord4typeEv(const QNdefRecord *self) {
  return new QByteArray(self->type());
}

//  void QNdefRecord::setId(const QByteArray &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecord5setIdERK10QByteArray(
    QNdefRecord *self,
    const QByteArray *id) {
  self->setId(*id);
}

//  QByteArray QNdefRecord::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QNdefRecord2idEv(const QNdefRecord *self) {
  return new QByteArray(self->id());
}

//  void QNdefRecord::setPayload(const QByteArray &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecord10setPayloadERK10QByteArray(
    QNdefRecord *self,
    const QByteArray *payload) {
  self->setPayload(*payload);
}

//  QByteArray QNdefRecord::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QNdefRecord7payloadEv(const QNdefRecord *self) {
  return new QByteArray(self->payload());
}

//  bool QNdefRecord::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QNdefRecord7isEmptyEv(const QNdefRecord *self) {
  return self->isEmpty();
}

//  bool QNdefRecord::operator==(const QNdefRecord &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QNdefRecordeqERKS_(
    const QNdefRecord *self,
    const QNdefRecord *other) {
  return self->operator==(*other);
}

//  bool QNdefRecord::operator!=(const QNdefRecord &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QNdefRecordneERKS_(
    const QNdefRecord *self,
    const QNdefRecord *other) {
  return self->operator!=(*other);
}

//  void QNdefRecord::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QNdefRecord5clearEv(QNdefRecord *self) {
  self->clear();
}

//  QNdefRecord::QNdefRecord(const QNdefRecord &other, TypeNameFormat
//      typeNameFormat, const QByteArray &type)
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_ZN11QNdefRecordC1ERKS_NS_14TypeNameFormatERK10QByteArray(
    const QNdefRecord *other,
    QNdefRecord::TypeNameFormat typeNameFormat,
    const QByteArray *type) {
  return new QNdefRecord(*other, typeNameFormat, *type);
}

//  QNdefRecord::QNdefRecord(const QNdefRecord &other, TypeNameFormat
//      typeNameFormat)
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_ZN11QNdefRecordC1ERKS_NS_14TypeNameFormatE(
    const QNdefRecord *other,
    QNdefRecord::TypeNameFormat typeNameFormat) {
  return new QNdefRecord(*other, typeNameFormat);
}

//  QNdefRecord::QNdefRecord(TypeNameFormat typeNameFormat, const QByteArray
//      &type)
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_ZN11QNdefRecordC1ENS_14TypeNameFormatERK10QByteArray(
    QNdefRecord::TypeNameFormat typeNameFormat,
    const QByteArray *type) {
  return new QNdefRecord(typeNameFormat, *type);
}

//  QList<QNdefRecord>::QList()
extern "C" Q_DECL_EXPORT
QList<QNdefRecord> *ritual_list_make_QNdefRecord() {
  return new QList<QNdefRecord>();
}

//  void QList<QNdefRecord>::append(const QNdefRecord &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNdefRecord(
    QList<QNdefRecord> *self,
    const QNdefRecord *element) {
  self->append(*element);
}

//  qsizetype QList<QNdefRecord>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNdefRecord(const QList<QNdefRecord> *self) {
  return self->size();
}

//  const QNdefRecord &QList<QNdefRecord>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNdefRecord *ritual_list_at_QNdefRecord(
    const QList<QNdefRecord> *self,
    long long index) {
  return new QNdefRecord(self->at(index));
}

//  QList<QNdefRecord>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNdefRecord(QList<QNdefRecord> *self) {
  delete self;
}
