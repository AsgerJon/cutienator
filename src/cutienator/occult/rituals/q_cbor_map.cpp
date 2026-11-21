//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>

//  QCborMap::QCborMap()
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMapC1Ev() {
  return new QCborMap();
}

//  QCborMap::QCborMap(const QCborMap &other)
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMapC1ERKS_(const QCborMap *other) {
  return new QCborMap(*other);
}

//  QCborMap::~QCborMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMapD1Ev(QCborMap *self) {
  delete self;
}

//  QCborValue QCborMap::toCborValue() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap11toCborValueEv(const QCborMap *self) {
  return new QCborValue(self->toCborValue());
}

//  qsizetype QCborMap::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK8QCborMap4sizeEv(const QCborMap *self) {
  return self->size();
}

//  bool QCborMap::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap7isEmptyEv(const QCborMap *self) {
  return self->isEmpty();
}

//  void QCborMap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap5clearEv(QCborMap *self) {
  self->clear();
}

//  QCborValue QCborMap::value(qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap5valueEx(const QCborMap *self, qint64 key) {
  return new QCborValue(self->value(key));
}

//  QCborValue QCborMap::value(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap5valueE13QLatin1String(
    const QCborMap *self,
    const QLatin1String *key) {
  return new QCborValue(self->value(*key));
}

//  QCborValue QCborMap::value(const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap5valueERK7QString(
    const QCborMap *self,
    const QString *key) {
  return new QCborValue(self->value(*key));
}

//  QCborValue QCborMap::value(const QCborValue &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMap5valueERK10QCborValue(
    const QCborMap *self,
    const QCborValue *key) {
  return new QCborValue(self->value(*key));
}

//  const QCborValue QCborMap::operator[](qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMapixEx(const QCborMap *self, qint64 key) {
  return new QCborValue(self->operator[](key));
}

//  const QCborValue QCborMap::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMapixE13QLatin1String(
    const QCborMap *self,
    const QLatin1String *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborMap::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMapixERK7QString(
    const QCborMap *self,
    const QString *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborMap::operator[](const QCborValue &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK8QCborMapixERK10QCborValue(
    const QCborMap *self,
    const QCborValue *key) {
  return new QCborValue(self->operator[](*key));
}

//  QCborValueRef QCborMap::operator[](qint64 key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN8QCborMapixEx(QCborMap *self, qint64 key) {
  return new QCborValueRef(self->operator[](key));
}

//  QCborValueRef QCborMap::operator[](QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN8QCborMapixE13QLatin1String(
    QCborMap *self,
    const QLatin1String *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValueRef QCborMap::operator[](const QString &key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN8QCborMapixERK7QString(
    QCborMap *self,
    const QString *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValueRef QCborMap::operator[](const QCborValue &key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN8QCborMapixERK10QCborValue(
    QCborMap *self,
    const QCborValue *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValue QCborMap::take(qint64 key)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap4takeEx(QCborMap *self, qint64 key) {
  return new QCborValue(self->take(key));
}

//  QCborValue QCborMap::take(QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap4takeE13QLatin1String(
    QCborMap *self,
    const QLatin1String *key) {
  return new QCborValue(self->take(*key));
}

//  QCborValue QCborMap::take(const QString &key)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap4takeERK7QString(
    QCborMap *self,
    const QString *key) {
  return new QCborValue(self->take(*key));
}

//  QCborValue QCborMap::take(const QCborValue &key)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap4takeERK10QCborValue(
    QCborMap *self,
    const QCborValue *key) {
  return new QCborValue(self->take(*key));
}

//  void QCborMap::remove(qint64 key)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap6removeEx(QCborMap *self, qint64 key) {
  self->remove(key);
}

//  void QCborMap::remove(QLatin1StringView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap6removeE13QLatin1String(
    QCborMap *self,
    const QLatin1String *key) {
  self->remove(*key);
}

//  void QCborMap::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap6removeERK7QString(
    QCborMap *self,
    const QString *key) {
  self->remove(*key);
}

//  void QCborMap::remove(const QCborValue &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap6removeERK10QCborValue(
    QCborMap *self,
    const QCborValue *key) {
  self->remove(*key);
}

//  bool QCborMap::contains(qint64 key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap8containsEx(const QCborMap *self, qint64 key) {
  return self->contains(key);
}

//  bool QCborMap::contains(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap8containsE13QLatin1String(
    const QCborMap *self,
    const QLatin1String *key) {
  return self->contains(*key);
}

//  bool QCborMap::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap8containsERK7QString(
    const QCborMap *self,
    const QString *key) {
  return self->contains(*key);
}

//  bool QCborMap::contains(const QCborValue &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap8containsERK10QCborValue(
    const QCborMap *self,
    const QCborValue *key) {
  return self->contains(*key);
}

//  int QCborMap::compare(const QCborMap &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QCborMap7compareERKS_(
    const QCborMap *self,
    const QCborMap *other) {
  return self->compare(*other);
}

//  QCborValue QCborMap::extract(iterator it)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap7extractENS_8IteratorE(
    QCborMap *self,
    const QCborMap::Iterator *it) {
  return new QCborValue(self->extract(*it));
}

//  QCborValue QCborMap::extract(const_iterator it)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN8QCborMap7extractENS_13ConstIteratorE(
    QCborMap *self,
    const QCborMap::ConstIterator *it) {
  return new QCborValue(self->extract(*it));
}

//  bool QCborMap::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QCborMap5emptyEv(const QCborMap *self) {
  return self->empty();
}

//  QCborMap QCborMap::fromJsonObject(const QJsonObject &o)
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMap14fromJsonObjectERK11QJsonObject(
    const QJsonObject *o) {
  return new QCborMap(QCborMap::fromJsonObject(*o));
}

//  QJsonObject QCborMap::toJsonObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK8QCborMap12toJsonObjectEv(const QCborMap *self) {
  return new QJsonObject(self->toJsonObject());
}
