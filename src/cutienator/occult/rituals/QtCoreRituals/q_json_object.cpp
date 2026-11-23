//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QJsonObject::QJsonObject()
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN11QJsonObjectC1Ev() {
  return new QJsonObject();
}

//  QJsonObject::~QJsonObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObjectD1Ev(QJsonObject *self) {
  delete self;
}

//  QJsonObject::QJsonObject(const QJsonObject &other)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN11QJsonObjectC1ERKS_(const QJsonObject *other) {
  return new QJsonObject(*other);
}

//  QJsonObject QJsonObject::fromVariantMap(const QVariantMap &map)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN11QJsonObject14fromVariantMapERK4QMapI7QString8QVariantE(
    const QMap<QString, QVariant> *map) {
  return new QJsonObject(QJsonObject::fromVariantMap(*map));
}

//  QVariantMap QJsonObject::toVariantMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK11QJsonObject12toVariantMapEv(
    const QJsonObject *self) {
  return new QMap<QString, QVariant>(self->toVariantMap());
}

//  QJsonObject QJsonObject::fromVariantHash(const QVariantHash &map)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN11QJsonObject15fromVariantHashERK5QHashI7QString8QVariantE(
    const QHash<QString, QVariant> *map) {
  return new QJsonObject(QJsonObject::fromVariantHash(*map));
}

//  QVariantHash QJsonObject::toVariantHash() const
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZNK11QJsonObject13toVariantHashEv(
    const QJsonObject *self) {
  return new QHash<QString, QVariant>(self->toVariantHash());
}

//  QStringList QJsonObject::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QJsonObject4keysEv(const QJsonObject *self) {
  return new QList<QString>(self->keys());
}

//  qsizetype QJsonObject::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QJsonObject4sizeEv(const QJsonObject *self) {
  return self->size();
}

//  qsizetype QJsonObject::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QJsonObject5countEv(const QJsonObject *self) {
  return self->count();
}

//  qsizetype QJsonObject::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QJsonObject6lengthEv(const QJsonObject *self) {
  return self->length();
}

//  bool QJsonObject::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QJsonObject7isEmptyEv(const QJsonObject *self) {
  return self->isEmpty();
}

//  QJsonValue QJsonObject::value(const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObject5valueERK7QString(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->value(*key));
}

//  QJsonValue QJsonObject::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObjectixERK7QString(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->operator[](*key));
}

//  QJsonValueRef QJsonObject::operator[](const QString &key)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN11QJsonObjectixERK7QString(
    QJsonObject *self,
    const QString *key) {
  return new QJsonValueRef(self->operator[](*key));
}

//  QJsonValue QJsonObject::value(QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObject5valueE11QStringView(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->value(QStringView(*key)));
}

//  QJsonValue QJsonObject::value(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObject5valueE13QLatin1String(
    const QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonValue(self->value(*key));
}

//  QJsonValue QJsonObject::operator[](QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObjectixE11QStringView(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->operator[](QStringView(*key)));
}

//  QJsonValue QJsonObject::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObjectixE13QLatin1String(
    const QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonValue(self->operator[](*key));
}

//  QJsonValueRef QJsonObject::operator[](QStringView key)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN11QJsonObjectixE11QStringView(
    QJsonObject *self,
    const QString *key) {
  return new QJsonValueRef(self->operator[](QStringView(*key)));
}

//  QJsonValueRef QJsonObject::operator[](QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN11QJsonObjectixE13QLatin1String(
    QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonValueRef(self->operator[](*key));
}

//  void QJsonObject::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject6removeERK7QString(
    QJsonObject *self,
    const QString *key) {
  self->remove(*key);
}

//  QJsonValue QJsonObject::take(const QString &key)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN11QJsonObject4takeERK7QString(
    QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->take(*key));
}

//  bool QJsonObject::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QJsonObject8containsERK7QString(
    const QJsonObject *self,
    const QString *key) {
  return self->contains(*key);
}

//  void QJsonObject::remove(QStringView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject6removeE11QStringView(
    QJsonObject *self,
    const QString *key) {
  self->remove(QStringView(*key));
}

//  void QJsonObject::remove(QLatin1StringView key)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject6removeE13QLatin1String(
    QJsonObject *self,
    const QLatin1String *key) {
  self->remove(*key);
}

//  QJsonValue QJsonObject::take(QStringView key)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN11QJsonObject4takeE11QStringView(
    QJsonObject *self,
    const QString *key) {
  return new QJsonValue(self->take(QStringView(*key)));
}

//  QJsonValue QJsonObject::take(QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN11QJsonObject4takeE13QLatin1String(
    QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonValue(self->take(*key));
}

//  bool QJsonObject::contains(QStringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QJsonObject8containsE11QStringView(
    const QJsonObject *self,
    const QString *key) {
  return self->contains(QStringView(*key));
}

//  bool QJsonObject::contains(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QJsonObject8containsE13QLatin1String(
    const QJsonObject *self,
    const QLatin1String *key) {
  return self->contains(*key);
}

//  iterator QJsonObject::begin()
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject5beginEv(QJsonObject *self) {
  return new QJsonObject::iterator(self->begin());
}

//  const_iterator QJsonObject::begin() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject5beginEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->begin());
}

//  const_iterator QJsonObject::cbegin() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject6cbeginEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->cbegin());
}

//  const_iterator QJsonObject::constBegin() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject10constBeginEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->constBegin());
}

//  iterator QJsonObject::end()
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject3endEv(QJsonObject *self) {
  return new QJsonObject::iterator(self->end());
}

//  const_iterator QJsonObject::end() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject3endEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->end());
}

//  const_iterator QJsonObject::cend() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject4cendEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->cend());
}

//  const_iterator QJsonObject::constEnd() const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject8constEndEv(
    const QJsonObject *self) {
  return new QJsonObject::const_iterator(self->constEnd());
}

//  iterator QJsonObject::erase(iterator it)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject5eraseENS_8iteratorE(
    QJsonObject *self,
    const QJsonObject::iterator *it) {
  return new QJsonObject::iterator(self->erase(*it));
}

//  iterator QJsonObject::find(const QString &key)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject4findERK7QString(
    QJsonObject *self,
    const QString *key) {
  return new QJsonObject::iterator(self->find(*key));
}

//  const_iterator QJsonObject::find(const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject4findERK7QString(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonObject::const_iterator(self->find(*key));
}

//  const_iterator QJsonObject::constFind(const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject9constFindERK7QString(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonObject::const_iterator(self->constFind(*key));
}

//  iterator QJsonObject::insert(const QString &key, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject6insertERK7QStringRK10QJsonValue(
    QJsonObject *self,
    const QString *key,
    const QJsonValue *value) {
  return new QJsonObject::iterator(self->insert(*key, *value));
}

//  iterator QJsonObject::find(QStringView key)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject4findE11QStringView(
    QJsonObject *self,
    const QString *key) {
  return new QJsonObject::iterator(self->find(QStringView(*key)));
}

//  iterator QJsonObject::find(QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject4findE13QLatin1String(
    QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonObject::iterator(self->find(*key));
}

//  const_iterator QJsonObject::find(QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject4findE11QStringView(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonObject::const_iterator(self->find(QStringView(*key)));
}

//  const_iterator QJsonObject::find(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject4findE13QLatin1String(
    const QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonObject::const_iterator(self->find(*key));
}

//  const_iterator QJsonObject::constFind(QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject9constFindE11QStringView(
    const QJsonObject *self,
    const QString *key) {
  return new QJsonObject::const_iterator(self->constFind(QStringView(*key)));
}

//  const_iterator QJsonObject::constFind(QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonObject::const_iterator *ritual_ZNK11QJsonObject9constFindE13QLatin1String(
    const QJsonObject *self,
    const QLatin1String *key) {
  return new QJsonObject::const_iterator(self->constFind(*key));
}

//  iterator QJsonObject::insert(QStringView key, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject6insertE11QStringViewRK10QJsonValue(
    QJsonObject *self,
    const QString *key,
    const QJsonValue *value) {
  return new QJsonObject::iterator(self->insert(QStringView(*key), *value));
}

//  iterator QJsonObject::insert(QLatin1StringView key, const QJsonValue
//      &value)
extern "C" Q_DECL_EXPORT
QJsonObject::iterator *ritual_ZN11QJsonObject6insertE13QLatin1StringRK10QJsonValue(
    QJsonObject *self,
    const QLatin1String *key,
    const QJsonValue *value) {
  return new QJsonObject::iterator(self->insert(*key, *value));
}

//  bool QJsonObject::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QJsonObject5emptyEv(const QJsonObject *self) {
  return self->empty();
}

//  bool operator==(const QJsonObject &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QJsonObjectS1_(
    const QJsonObject *lhs,
    const QJsonObject *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonObject &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QJsonObjectS1_(
    const QJsonObject *lhs,
    const QJsonObject *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonObject &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QJsonObjectRK10QJsonValue(
    const QJsonObject *lhs,
    const QJsonValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonObject &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QJsonObjectRK10QJsonValue(
    const QJsonObject *lhs,
    const QJsonValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonValue &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonValueRK11QJsonObject(
    const QJsonValue *lhs,
    const QJsonObject *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValue &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonValueRK11QJsonObject(
    const QJsonValue *lhs,
    const QJsonObject *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonObject &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QJsonObjectRK18QJsonValueConstRef(
    const QJsonObject *lhs,
    const QJsonValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonObject &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QJsonObjectRK18QJsonValueConstRef(
    const QJsonObject *lhs,
    const QJsonValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonValueConstRef &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QJsonValueConstRefRK11QJsonObject(
    const QJsonValueConstRef *lhs,
    const QJsonObject *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValueConstRef &lhs, const QJsonObject &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QJsonValueConstRefRK11QJsonObject(
    const QJsonValueConstRef *lhs,
    const QJsonObject *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QDebug operator<<(QDebug a0, const QJsonObject &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK11QJsonObject(
    const QDebug *a0,
    const QJsonObject *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  bool QJsonObject::detach(qsizetype reserve)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QJsonObject6detachEx(QJsonObject *self, qsizetype reserve) {
  return self->detach(reserve);
}

//  QString QJsonObject::keyAt(qsizetype i) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QJsonObject5keyAtEx(
    const QJsonObject *self,
    qsizetype i) {
  return new QString(self->keyAt(i));
}

//  QJsonValue QJsonObject::valueAt(qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK11QJsonObject7valueAtEx(
    const QJsonObject *self,
    qsizetype i) {
  return new QJsonValue(self->valueAt(i));
}

//  void QJsonObject::setValueAt(qsizetype i, const QJsonValue &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject10setValueAtExRK10QJsonValue(
    QJsonObject *self,
    qsizetype i,
    const QJsonValue *val) {
  self->setValueAt(i, *val);
}

//  void QJsonObject::removeAt(qsizetype i)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QJsonObject8removeAtEx(QJsonObject *self, qsizetype i) {
  self->removeAt(i);
}
