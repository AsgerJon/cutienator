//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QDBusVariant::QDBusVariant()
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN12QDBusVariantC1Ev() {
  return new QDBusVariant();
}

//  QDBusVariant::QDBusVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN12QDBusVariantC1ERK8QVariant(
    const QVariant *variant) {
  return new QDBusVariant(*variant);
}

//  void QDBusVariant::setVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusVariant10setVariantERK8QVariant(
    QDBusVariant *self,
    const QVariant *variant) {
  self->setVariant(*variant);
}

//  QVariant QDBusVariant::variant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QDBusVariant7variantEv(const QDBusVariant *self) {
  return new QVariant(self->variant());
}

//  QDBusVariant::~QDBusVariant()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusVariantD1Ev(QDBusVariant *self) {
  delete self;
}

//  QMap<QString, QDBusVariant>: QMap<QString, QDBusVariant>()
extern "C" Q_DECL_EXPORT
QMap<QString, QDBusVariant> *ritual_map_make_QMap_QString_QDBusVariant() {
  return new QMap<QString, QDBusVariant>();
}

//  QMap<QString, QDBusVariant>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_QString_QDBusVariant(
    QMap<QString, QDBusVariant> *self,
    const QString *key,
    const QDBusVariant *value) {
  self->insert(*key, *value);
}

//  QMap<QString, QDBusVariant>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_QString_QDBusVariant(
    const QMap<QString, QDBusVariant> *self) {
  return self->size();
}

//  QMap<QString, QDBusVariant>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QMap_QString_QDBusVariant(
    const QMap<QString, QDBusVariant> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QMap<QString, QDBusVariant>: the value at a place
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_map_value_QMap_QString_QDBusVariant(
    const QMap<QString, QDBusVariant> *self,
    long long index) {
  return new QDBusVariant(*std::next(self->constBegin(), index));
}

//  QMap<QString, QDBusVariant>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_QString_QDBusVariant(
    const QMap<QString, QDBusVariant> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QMap<QString, QDBusVariant>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_map_get_QMap_QString_QDBusVariant(
    const QMap<QString, QDBusVariant> *self,
    const QString *key) {
  return new QDBusVariant(self->value(*key));
}

//  QMap<QString, QDBusVariant>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_QString_QDBusVariant(
    QMap<QString, QDBusVariant> *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
