//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceattribute.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceattribute.h>
#include <QtCore/qstring.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QPlaceAttribute::QPlaceAttribute()
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_ZN15QPlaceAttributeC1Ev() {
  return new QPlaceAttribute();
}

//  QPlaceAttribute::QPlaceAttribute(const QPlaceAttribute &other)
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_ZN15QPlaceAttributeC1ERKS_(
    const QPlaceAttribute *other) {
  return new QPlaceAttribute(*other);
}

//  QPlaceAttribute::~QPlaceAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlaceAttributeD1Ev(QPlaceAttribute *self) {
  delete self;
}

//  bool operator==(const QPlaceAttribute &lhs, const QPlaceAttribute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QPlaceAttributeS1_(
    const QPlaceAttribute *lhs,
    const QPlaceAttribute *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceAttribute &lhs, const QPlaceAttribute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QPlaceAttributeS1_(
    const QPlaceAttribute *lhs,
    const QPlaceAttribute *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceAttribute::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlaceAttribute5labelEv(const QPlaceAttribute *self) {
  return new QString(self->label());
}

//  void QPlaceAttribute::setLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlaceAttribute8setLabelERK7QString(
    QPlaceAttribute *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString QPlaceAttribute::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlaceAttribute4textEv(const QPlaceAttribute *self) {
  return new QString(self->text());
}

//  void QPlaceAttribute::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlaceAttribute7setTextERK7QString(
    QPlaceAttribute *self,
    const QString *text) {
  self->setText(*text);
}

//  bool QPlaceAttribute::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlaceAttribute7isEmptyEv(const QPlaceAttribute *self) {
  return self->isEmpty();
}

//  bool QPlaceAttribute::isEqual(const QPlaceAttribute &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlaceAttribute7isEqualERKS_(
    const QPlaceAttribute *self,
    const QPlaceAttribute *other) {
  return self->isEqual(*other);
}

//  QMap<QString, QPlaceAttribute>: QMap<QString, QPlaceAttribute>()
extern "C" Q_DECL_EXPORT
QMap<QString, QPlaceAttribute> *ritual_map_make_QMap_QString_QPlaceAttribute() {
  return new QMap<QString, QPlaceAttribute>();
}

//  QMap<QString, QPlaceAttribute>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_QString_QPlaceAttribute(
    QMap<QString, QPlaceAttribute> *self,
    const QString *key,
    const QPlaceAttribute *value) {
  self->insert(*key, *value);
}

//  QMap<QString, QPlaceAttribute>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_QString_QPlaceAttribute(
    const QMap<QString, QPlaceAttribute> *self) {
  return self->size();
}

//  QMap<QString, QPlaceAttribute>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QMap_QString_QPlaceAttribute(
    const QMap<QString, QPlaceAttribute> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QMap<QString, QPlaceAttribute>: the value at a place
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_map_value_QMap_QString_QPlaceAttribute(
    const QMap<QString, QPlaceAttribute> *self,
    long long index) {
  return new QPlaceAttribute(*std::next(self->constBegin(), index));
}

//  QMap<QString, QPlaceAttribute>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_QString_QPlaceAttribute(
    const QMap<QString, QPlaceAttribute> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QMap<QString, QPlaceAttribute>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_map_get_QMap_QString_QPlaceAttribute(
    const QMap<QString, QPlaceAttribute> *self,
    const QString *key) {
  return new QPlaceAttribute(self->value(*key));
}

//  QMap<QString, QPlaceAttribute>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_QString_QPlaceAttribute(
    QMap<QString, QPlaceAttribute> *self) {
  delete self;
}
