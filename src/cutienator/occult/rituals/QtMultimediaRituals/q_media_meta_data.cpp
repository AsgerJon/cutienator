//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediametadata.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediametadata.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qlist.h>

//  QVariant QMediaMetaData::value(Key k) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QMediaMetaData5valueENS_3KeyE(
    const QMediaMetaData *self,
    QMediaMetaData::Key k) {
  return new QVariant(self->value(k));
}

//  void QMediaMetaData::insert(Key k, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaMetaData6insertENS_3KeyERK8QVariant(
    QMediaMetaData *self,
    QMediaMetaData::Key k,
    const QVariant *value) {
  self->insert(k, *value);
}

//  void QMediaMetaData::remove(Key k)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaMetaData6removeENS_3KeyE(
    QMediaMetaData *self,
    QMediaMetaData::Key k) {
  self->remove(k);
}

//  void QMediaMetaData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaMetaData5clearEv(QMediaMetaData *self) {
  self->clear();
}

//  bool QMediaMetaData::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMediaMetaData7isEmptyEv(const QMediaMetaData *self) {
  return self->isEmpty();
}

//  QString QMediaMetaData::stringValue(Key k) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QMediaMetaData11stringValueENS_3KeyE(
    const QMediaMetaData *self,
    QMediaMetaData::Key k) {
  return new QString(self->stringValue(k));
}

//  QString QMediaMetaData::metaDataKeyToString(Key k)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QMediaMetaData19metaDataKeyToStringENS_3KeyE(
    QMediaMetaData::Key k) {
  return new QString(QMediaMetaData::metaDataKeyToString(k));
}

//  QDebug operator<<(QDebug a0, const QMediaMetaData &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK14QMediaMetaData(
    const QDebug *a0,
    const QMediaMetaData *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  bool operator==(const QMediaMetaData &a, const QMediaMetaData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QMediaMetaDataS1_(
    const QMediaMetaData *a,
    const QMediaMetaData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QMediaMetaData &a, const QMediaMetaData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QMediaMetaDataS1_(
    const QMediaMetaData *a,
    const QMediaMetaData *b) {
  return operator!=(*a, *b);
}

//  QMetaType QMediaMetaData::keyType(Key key)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN14QMediaMetaData7keyTypeENS_3KeyE(
    QMediaMetaData::Key key) {
  return new QMetaType(QMediaMetaData::keyType(key));
}

//  QMediaMetaData::~QMediaMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMediaMetaDataD1Ev(QMediaMetaData *self) {
  delete self;
}

//  QList<QMediaMetaData>::QList()
extern "C" Q_DECL_EXPORT
QList<QMediaMetaData> *ritual_list_make_QMediaMetaData() {
  return new QList<QMediaMetaData>();
}

//  void QList<QMediaMetaData>::append(const QMediaMetaData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMediaMetaData(
    QList<QMediaMetaData> *self,
    const QMediaMetaData *element) {
  self->append(*element);
}

//  qsizetype QList<QMediaMetaData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMediaMetaData(
    const QList<QMediaMetaData> *self) {
  return self->size();
}

//  const QMediaMetaData &QList<QMediaMetaData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMediaMetaData *ritual_list_at_QMediaMetaData(
    const QList<QMediaMetaData> *self,
    long long index) {
  return new QMediaMetaData(self->at(index));
}

//  QList<QMediaMetaData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMediaMetaData(QList<QMediaMetaData> *self) {
  delete self;
}
