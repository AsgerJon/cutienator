//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QQmlJSMetaEnum::QQmlJSMetaEnum()
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_ZN14QQmlJSMetaEnumC1Ev() {
  return new QQmlJSMetaEnum();
}

//  QQmlJSMetaEnum::QQmlJSMetaEnum(QString name)
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_ZN14QQmlJSMetaEnumC1E7QString(const QString *name) {
  return new QQmlJSMetaEnum(*name);
}

//  bool QQmlJSMetaEnum::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum7isValidEv(const QQmlJSMetaEnum *self) {
  return self->isValid();
}

//  QString QQmlJSMetaEnum::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlJSMetaEnum4nameEv(const QQmlJSMetaEnum *self) {
  return new QString(self->name());
}

//  void QQmlJSMetaEnum::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum7setNameERK7QString(
    QQmlJSMetaEnum *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QQmlJSMetaEnum::alias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlJSMetaEnum5aliasEv(const QQmlJSMetaEnum *self) {
  return new QString(self->alias());
}

//  void QQmlJSMetaEnum::setAlias(const QString &alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum8setAliasERK7QString(
    QQmlJSMetaEnum *self,
    const QString *alias) {
  self->setAlias(*alias);
}

//  bool QQmlJSMetaEnum::isFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum6isFlagEv(const QQmlJSMetaEnum *self) {
  return self->isFlag();
}

//  void QQmlJSMetaEnum::setIsFlag(bool isFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum9setIsFlagEb(
    QQmlJSMetaEnum *self,
    bool isFlag) {
  self->setIsFlag(isFlag);
}

//  bool QQmlJSMetaEnum::isScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum8isScopedEv(const QQmlJSMetaEnum *self) {
  return self->isScoped();
}

//  void QQmlJSMetaEnum::setIsScoped(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum11setIsScopedEb(QQmlJSMetaEnum *self, bool v) {
  self->setIsScoped(v);
}

//  bool QQmlJSMetaEnum::isQml() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum5isQmlEv(const QQmlJSMetaEnum *self) {
  return self->isQml();
}

//  void QQmlJSMetaEnum::setIsQml(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum8setIsQmlEb(QQmlJSMetaEnum *self, bool v) {
  self->setIsQml(v);
}

//  void QQmlJSMetaEnum::addKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum6addKeyERK7QString(
    QQmlJSMetaEnum *self,
    const QString *key) {
  self->addKey(*key);
}

//  QStringList QQmlJSMetaEnum::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlJSMetaEnum4keysEv(
    const QQmlJSMetaEnum *self) {
  return new QList<QString>(self->keys());
}

//  void QQmlJSMetaEnum::addValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum8addValueEi(QQmlJSMetaEnum *self, int value) {
  self->addValue(value);
}

//  bool QQmlJSMetaEnum::hasValues() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum9hasValuesEv(const QQmlJSMetaEnum *self) {
  return self->hasValues();
}

//  int QQmlJSMetaEnum::value(const QString &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlJSMetaEnum5valueERK7QString(
    const QQmlJSMetaEnum *self,
    const QString *key) {
  return self->value(*key);
}

//  bool QQmlJSMetaEnum::hasKey(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSMetaEnum6hasKeyERK7QString(
    const QQmlJSMetaEnum *self,
    const QString *key) {
  return self->hasKey(*key);
}

//  QString QQmlJSMetaEnum::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlJSMetaEnum8typeNameEv(const QQmlJSMetaEnum *self) {
  return new QString(self->typeName());
}

//  void QQmlJSMetaEnum::setTypeName(const QString &typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum11setTypeNameERK7QString(
    QQmlJSMetaEnum *self,
    const QString *typeName) {
  self->setTypeName(*typeName);
}

//  int QQmlJSMetaEnum::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlJSMetaEnum10lineNumberEv(const QQmlJSMetaEnum *self) {
  return self->lineNumber();
}

//  void QQmlJSMetaEnum::setLineNumber(int lineNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnum13setLineNumberEi(
    QQmlJSMetaEnum *self,
    int lineNumber) {
  self->setLineNumber(lineNumber);
}

//  bool operator==(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QQmlJSMetaEnumS1_(
    const QQmlJSMetaEnum *a,
    const QQmlJSMetaEnum *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QQmlJSMetaEnumS1_(
    const QQmlJSMetaEnum *a,
    const QQmlJSMetaEnum *b) {
  return operator!=(*a, *b);
}

//  QQmlJSMetaEnum::~QQmlJSMetaEnum()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSMetaEnumD1Ev(QQmlJSMetaEnum *self) {
  delete self;
}

//  QHash<QString, QQmlJSMetaEnum>: QHash<QString, QQmlJSMetaEnum>()
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaEnum> *ritual_map_make_QHash_QString_QQmlJSMetaEnum() {
  return new QHash<QString, QQmlJSMetaEnum>();
}

//  QHash<QString, QQmlJSMetaEnum>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QQmlJSMetaEnum(
    QHash<QString, QQmlJSMetaEnum> *self,
    const QString *key,
    const QQmlJSMetaEnum *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QQmlJSMetaEnum>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QQmlJSMetaEnum(
    const QHash<QString, QQmlJSMetaEnum> *self) {
  return self->size();
}

//  QHash<QString, QQmlJSMetaEnum>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QQmlJSMetaEnum(
    const QHash<QString, QQmlJSMetaEnum> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QQmlJSMetaEnum>: the value at a place
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_map_value_QHash_QString_QQmlJSMetaEnum(
    const QHash<QString, QQmlJSMetaEnum> *self,
    long long index) {
  return new QQmlJSMetaEnum(*std::next(self->constBegin(), index));
}

//  QHash<QString, QQmlJSMetaEnum>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QQmlJSMetaEnum(
    const QHash<QString, QQmlJSMetaEnum> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QQmlJSMetaEnum>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_map_get_QHash_QString_QQmlJSMetaEnum(
    const QHash<QString, QQmlJSMetaEnum> *self,
    const QString *key) {
  return new QQmlJSMetaEnum(self->value(*key));
}

//  QHash<QString, QQmlJSMetaEnum>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QQmlJSMetaEnum(
    QHash<QString, QQmlJSMetaEnum> *self) {
  delete self;
}
