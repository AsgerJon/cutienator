//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qtremoteobjectglobal.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo()
extern "C" Q_DECL_EXPORT
QRemoteObjectSourceLocationInfo *ritual_ZN31QRemoteObjectSourceLocationInfoC1Ev() {
  return new QRemoteObjectSourceLocationInfo();
}

//  QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo(const
//      QString &typeName_, const QUrl &hostUrl_)
extern "C" Q_DECL_EXPORT
QRemoteObjectSourceLocationInfo *ritual_ZN31QRemoteObjectSourceLocationInfoC1ERK7QStringRK4QUrl(
    const QString *typeName_,
    const QUrl *hostUrl_) {
  return new QRemoteObjectSourceLocationInfo(*typeName_, *hostUrl_);
}

//  bool QRemoteObjectSourceLocationInfo::operator==(const
//      QRemoteObjectSourceLocationInfo &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QRemoteObjectSourceLocationInfoeqERKS_(
    const QRemoteObjectSourceLocationInfo *self,
    const QRemoteObjectSourceLocationInfo *other) {
  return self->operator==(*other);
}

//  bool QRemoteObjectSourceLocationInfo::operator!=(const
//      QRemoteObjectSourceLocationInfo &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QRemoteObjectSourceLocationInfoneERKS_(
    const QRemoteObjectSourceLocationInfo *self,
    const QRemoteObjectSourceLocationInfo *other) {
  return self->operator!=(*other);
}

//  QRemoteObjectSourceLocationInfo::~QRemoteObjectSourceLocationInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QRemoteObjectSourceLocationInfoD1Ev(
    QRemoteObjectSourceLocationInfo *self) {
  delete self;
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: QHash<QString,
//      QRemoteObjectSourceLocationInfo>()
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_map_make_QHash_QString_QRemoteObjectSourceLocationInfo() {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>();
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: insert(const Key &key,
//      const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QRemoteObjectSourceLocationInfo(
    QHash<QString, QRemoteObjectSourceLocationInfo> *self,
    const QString *key,
    const QRemoteObjectSourceLocationInfo *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QRemoteObjectSourceLocationInfo(
    const QHash<QString, QRemoteObjectSourceLocationInfo> *self) {
  return self->size();
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QRemoteObjectSourceLocationInfo(
    const QHash<QString, QRemoteObjectSourceLocationInfo> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: the value at a place
extern "C" Q_DECL_EXPORT
QRemoteObjectSourceLocationInfo *ritual_map_value_QHash_QString_QRemoteObjectSourceLocationInfo(
    const QHash<QString, QRemoteObjectSourceLocationInfo> *self,
    long long index) {
  return new QRemoteObjectSourceLocationInfo(*std::next(self->constBegin(), index));
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: contains(const Key &key)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QRemoteObjectSourceLocationInfo(
    const QHash<QString, QRemoteObjectSourceLocationInfo> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: value(const Key &key)
//      const
extern "C" Q_DECL_EXPORT
QRemoteObjectSourceLocationInfo *ritual_map_get_QHash_QString_QRemoteObjectSourceLocationInfo(
    const QHash<QString, QRemoteObjectSourceLocationInfo> *self,
    const QString *key) {
  return new QRemoteObjectSourceLocationInfo(self->value(*key));
}

//  QHash<QString, QRemoteObjectSourceLocationInfo>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QRemoteObjectSourceLocationInfo(
    QHash<QString, QRemoteObjectSourceLocationInfo> *self) {
  delete self;
}
