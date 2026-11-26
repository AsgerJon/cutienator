//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuahistorydata.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuahistorydata.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuadatavalue.h>
#include <QtCore/qlist.h>

//  QOpcUaHistoryData::QOpcUaHistoryData()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryData *ritual_ZN17QOpcUaHistoryDataC1Ev() {
  return new QOpcUaHistoryData();
}

//  QOpcUaHistoryData::QOpcUaHistoryData(const QString &nodeId)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryData *ritual_ZN17QOpcUaHistoryDataC1ERK7QString(
    const QString *nodeId) {
  return new QOpcUaHistoryData(*nodeId);
}

//  QOpcUaHistoryData::QOpcUaHistoryData(const QOpcUaHistoryData &other)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryData *ritual_ZN17QOpcUaHistoryDataC1ERKS_(
    const QOpcUaHistoryData *other) {
  return new QOpcUaHistoryData(*other);
}

//  QOpcUaHistoryData::~QOpcUaHistoryData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaHistoryDataD1Ev(QOpcUaHistoryData *self) {
  delete self;
}

//  void QOpcUaHistoryData::swap(QOpcUaHistoryData &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaHistoryData4swapERS_(
    QOpcUaHistoryData *self,
    QOpcUaHistoryData *other) {
  self->swap(*other);
}

//  QOpcUa::UaStatusCode QOpcUaHistoryData::statusCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK17QOpcUaHistoryData10statusCodeEv(
    const QOpcUaHistoryData *self) {
  return self->statusCode();
}

//  void QOpcUaHistoryData::setStatusCode(QOpcUa::UaStatusCode statusCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaHistoryData13setStatusCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaHistoryData *self,
    QOpcUa::UaStatusCode statusCode) {
  self->setStatusCode(statusCode);
}

//  QList<QOpcUaDataValue> QOpcUaHistoryData::result() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaDataValue> *ritual_ZNK17QOpcUaHistoryData6resultEv(
    const QOpcUaHistoryData *self) {
  return new QList<QOpcUaDataValue>(self->result());
}

//  int QOpcUaHistoryData::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QOpcUaHistoryData5countEv(const QOpcUaHistoryData *self) {
  return self->count();
}

//  void QOpcUaHistoryData::addValue(const QOpcUaDataValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaHistoryData8addValueERK15QOpcUaDataValue(
    QOpcUaHistoryData *self,
    const QOpcUaDataValue *value) {
  self->addValue(*value);
}

//  QString QOpcUaHistoryData::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QOpcUaHistoryData6nodeIdEv(
    const QOpcUaHistoryData *self) {
  return new QString(self->nodeId());
}

//  void QOpcUaHistoryData::setNodeId(const QString &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpcUaHistoryData9setNodeIdERK7QString(
    QOpcUaHistoryData *self,
    const QString *nodeId) {
  self->setNodeId(*nodeId);
}

//  QOpcUaHistoryData &QOpcUaHistoryData::operator=(const QOpcUaHistoryData
//      &other)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryData *ritual_ZN17QOpcUaHistoryDataaSERKS_(
    QOpcUaHistoryData *self,
    const QOpcUaHistoryData *other) {
  return &(self->operator=(*other));
}

//  QList<QOpcUaHistoryData>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaHistoryData> *ritual_list_make_QOpcUaHistoryData() {
  return new QList<QOpcUaHistoryData>();
}

//  void QList<QOpcUaHistoryData>::append(const QOpcUaHistoryData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaHistoryData(
    QList<QOpcUaHistoryData> *self,
    const QOpcUaHistoryData *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaHistoryData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaHistoryData(
    const QList<QOpcUaHistoryData> *self) {
  return self->size();
}

//  const QOpcUaHistoryData &QList<QOpcUaHistoryData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaHistoryData *ritual_list_at_QOpcUaHistoryData(
    const QList<QOpcUaHistoryData> *self,
    long long index) {
  return new QOpcUaHistoryData(self->at(index));
}

//  QList<QOpcUaHistoryData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaHistoryData(QList<QOpcUaHistoryData> *self) {
  delete self;
}
