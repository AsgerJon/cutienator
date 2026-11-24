//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qcompare.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

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

//  QList<QCborValue> QCborMap::keys() const
extern "C" Q_DECL_EXPORT
QList<QCborValue> *ritual_ZNK8QCborMap4keysEv(const QCborMap *self) {
  return new QList<QCborValue>(self->keys());
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

//  QCborMap QCborMap::fromVariantMap(const QVariantMap &map)
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMap14fromVariantMapERK4QMapI7QString8QVariantE(
    const QMap<QString, QVariant> *map) {
  return new QCborMap(QCborMap::fromVariantMap(*map));
}

//  QCborMap QCborMap::fromVariantHash(const QVariantHash &hash)
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMap15fromVariantHashERK5QHashI7QString8QVariantE(
    const QHash<QString, QVariant> *hash) {
  return new QCborMap(QCborMap::fromVariantHash(*hash));
}

//  QCborMap QCborMap::fromJsonObject(const QJsonObject &o)
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZN8QCborMap14fromJsonObjectERK11QJsonObject(
    const QJsonObject *o) {
  return new QCborMap(QCborMap::fromJsonObject(*o));
}

//  QVariantMap QCborMap::toVariantMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK8QCborMap12toVariantMapEv(
    const QCborMap *self) {
  return new QMap<QString, QVariant>(self->toVariantMap());
}

//  QVariantHash QCborMap::toVariantHash() const
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZNK8QCborMap13toVariantHashEv(
    const QCborMap *self) {
  return new QHash<QString, QVariant>(self->toVariantHash());
}

//  QJsonObject QCborMap::toJsonObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK8QCborMap12toJsonObjectEv(const QCborMap *self) {
  return new QJsonObject(self->toJsonObject());
}

//  void QCborMap::detach(qsizetype reserve)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QCborMap6detachEx(QCborMap *self, qsizetype reserve) {
  self->detach(reserve);
}

//  bool operator==(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborMap &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8QCborMapS1_(const QCborMap *lhs, const QCborMap *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool QCborMap::comparesEqual_helper(const QCborMap &lhs, const QCborValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QCborMap20comparesEqual_helperERKS_RK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return QCborMap::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QCborMap::compareThreeWay_helper(const QCborMap &lhs,
//      const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN8QCborMap22compareThreeWay_helperERKS_RK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return new Qt::strong_ordering(
      QCborMap::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborMap &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8QCborMapRK10QCborValue(
    const QCborMap *lhs,
    const QCborValue *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValue &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QCborValueRK8QCborMap(
    const QCborValue *lhs,
    const QCborMap *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool QCborMap::comparesEqual_helper(const QCborMap &lhs,
//      QCborValueConstRef rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QCborMap20comparesEqual_helperERKS_18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return QCborMap::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering QCborMap::compareThreeWay_helper(const QCborMap &lhs,
//      QCborValueConstRef rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN8QCborMap22compareThreeWay_helperERKS_18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return new Qt::strong_ordering(
      QCborMap::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborMap &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK8QCborMapRK18QCborValueConstRef(
    const QCborMap *lhs,
    const QCborValueConstRef *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValueConstRef &lhs, const QCborMap &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK18QCborValueConstRefRK8QCborMap(
    const QCborValueConstRef *lhs,
    const QCborMap *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QList<QCborMap>::QList()
extern "C" Q_DECL_EXPORT
QList<QCborMap> *ritual_list_make_QCborMap() {
  return new QList<QCborMap>();
}

//  void QList<QCborMap>::append(const QCborMap &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCborMap(
    QList<QCborMap> *self,
    const QCborMap *element) {
  self->append(*element);
}

//  qsizetype QList<QCborMap>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCborMap(const QList<QCborMap> *self) {
  return self->size();
}

//  const QCborMap &QList<QCborMap>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_list_at_QCborMap(
    const QList<QCborMap> *self,
    long long index) {
  return new QCborMap(self->at(index));
}

//  QList<QCborMap>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCborMap(QList<QCborMap> *self) {
  delete self;
}
