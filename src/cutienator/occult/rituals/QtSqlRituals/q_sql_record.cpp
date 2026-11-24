//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlrecord.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlrecord.h>
#include <QtCore/qvariant.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlfield.h>

//  QSqlRecord::QSqlRecord()
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZN10QSqlRecordC1Ev() {
  return new QSqlRecord();
}

//  QSqlRecord::QSqlRecord(const QSqlRecord &other)
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZN10QSqlRecordC1ERKS_(const QSqlRecord *other) {
  return new QSqlRecord(*other);
}

//  QSqlRecord::~QSqlRecord()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecordD1Ev(QSqlRecord *self) {
  delete self;
}

//  bool QSqlRecord::operator==(const QSqlRecord &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecordeqERKS_(
    const QSqlRecord *self,
    const QSqlRecord *other) {
  return self->operator==(*other);
}

//  bool QSqlRecord::operator!=(const QSqlRecord &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecordneERKS_(
    const QSqlRecord *self,
    const QSqlRecord *other) {
  return self->operator!=(*other);
}

//  QVariant QSqlRecord::value(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlRecord5valueEi(const QSqlRecord *self, int i) {
  return new QVariant(self->value(i));
}

//  QVariant QSqlRecord::value(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QSqlRecord5valueE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return new QVariant(self->value(QAnyStringView(*name)));
}

//  void QSqlRecord::setValue(int i, const QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord8setValueEiRK8QVariant(
    QSqlRecord *self,
    int i,
    const QVariant *val) {
  self->setValue(i, *val);
}

//  void QSqlRecord::setValue(QAnyStringView name, const QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord8setValueE14QAnyStringViewRK8QVariant(
    QSqlRecord *self,
    const QString *name,
    const QVariant *val) {
  self->setValue(QAnyStringView(*name), *val);
}

//  void QSqlRecord::setNull(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord7setNullEi(QSqlRecord *self, int i) {
  self->setNull(i);
}

//  void QSqlRecord::setNull(QAnyStringView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord7setNullE14QAnyStringView(
    QSqlRecord *self,
    const QString *name) {
  self->setNull(QAnyStringView(*name));
}

//  bool QSqlRecord::isNull(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord6isNullEi(const QSqlRecord *self, int i) {
  return self->isNull(i);
}

//  bool QSqlRecord::isNull(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord6isNullE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return self->isNull(QAnyStringView(*name));
}

//  int QSqlRecord::indexOf(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlRecord7indexOfE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return self->indexOf(QAnyStringView(*name));
}

//  QString QSqlRecord::fieldName(int i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSqlRecord9fieldNameEi(const QSqlRecord *self, int i) {
  return new QString(self->fieldName(i));
}

//  QSqlField QSqlRecord::field(int i) const
extern "C" Q_DECL_EXPORT
QSqlField *ritual_ZNK10QSqlRecord5fieldEi(const QSqlRecord *self, int i) {
  return new QSqlField(self->field(i));
}

//  QSqlField QSqlRecord::field(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QSqlField *ritual_ZNK10QSqlRecord5fieldE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return new QSqlField(self->field(QAnyStringView(*name)));
}

//  bool QSqlRecord::isGenerated(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord11isGeneratedEi(const QSqlRecord *self, int i) {
  return self->isGenerated(i);
}

//  bool QSqlRecord::isGenerated(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord11isGeneratedE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return self->isGenerated(QAnyStringView(*name));
}

//  void QSqlRecord::setGenerated(QAnyStringView name, bool generated)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord12setGeneratedE14QAnyStringViewb(
    QSqlRecord *self,
    const QString *name,
    bool generated) {
  self->setGenerated(QAnyStringView(*name), generated);
}

//  void QSqlRecord::setGenerated(int i, bool generated)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord12setGeneratedEib(
    QSqlRecord *self,
    int i,
    bool generated) {
  self->setGenerated(i, generated);
}

//  void QSqlRecord::append(const QSqlField &field)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord6appendERK9QSqlField(
    QSqlRecord *self,
    const QSqlField *field) {
  self->append(*field);
}

//  void QSqlRecord::replace(int pos, const QSqlField &field)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord7replaceEiRK9QSqlField(
    QSqlRecord *self,
    int pos,
    const QSqlField *field) {
  self->replace(pos, *field);
}

//  void QSqlRecord::insert(int pos, const QSqlField &field)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord6insertEiRK9QSqlField(
    QSqlRecord *self,
    int pos,
    const QSqlField *field) {
  self->insert(pos, *field);
}

//  void QSqlRecord::remove(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord6removeEi(QSqlRecord *self, int pos) {
  self->remove(pos);
}

//  bool QSqlRecord::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord7isEmptyEv(const QSqlRecord *self) {
  return self->isEmpty();
}

//  bool QSqlRecord::contains(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSqlRecord8containsE14QAnyStringView(
    const QSqlRecord *self,
    const QString *name) {
  return self->contains(QAnyStringView(*name));
}

//  void QSqlRecord::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord5clearEv(QSqlRecord *self) {
  self->clear();
}

//  void QSqlRecord::clearValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord11clearValuesEv(QSqlRecord *self) {
  self->clearValues();
}

//  int QSqlRecord::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSqlRecord5countEv(const QSqlRecord *self) {
  return self->count();
}

//  QSqlRecord QSqlRecord::keyValues(const QSqlRecord &keyFields) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK10QSqlRecord9keyValuesERKS_(
    const QSqlRecord *self,
    const QSqlRecord *keyFields) {
  return new QSqlRecord(self->keyValues(*keyFields));
}

//  void QSqlRecord::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSqlRecord6detachEv(QSqlRecord *self) {
  self->detach();
}
