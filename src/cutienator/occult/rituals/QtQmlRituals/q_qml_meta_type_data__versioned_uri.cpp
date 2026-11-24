//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>

//  QQmlMetaTypeData::VersionedUri::VersionedUri()
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData::VersionedUri *ritual_ZN16QQmlMetaTypeData12VersionedUriC1Ev() {
  return new QQmlMetaTypeData::VersionedUri();
}

//  QQmlMetaTypeData::VersionedUri::VersionedUri(const QString &uri,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData::VersionedUri *ritual_ZN16QQmlMetaTypeData12VersionedUriC1ERK7QString13QTypeRevision(
    const QString *uri,
    const QTypeRevision *version) {
  return new QQmlMetaTypeData::VersionedUri(*uri, *version);
}

//  bool operator==(const VersionedUri &a, const VersionedUri &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN16QQmlMetaTypeData12VersionedUriES2_(
    const QQmlMetaTypeData::VersionedUri *a,
    const QQmlMetaTypeData::VersionedUri *b) {
  return operator==(*a, *b);
}

//  bool operator<(const QQmlMetaTypeData::VersionedUri &a, const
//      QQmlMetaTypeData::VersionedUri &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN16QQmlMetaTypeData12VersionedUriES2_(
    const QQmlMetaTypeData::VersionedUri *a,
    const QQmlMetaTypeData::VersionedUri *b) {
  return operator<(*a, *b);
}

//  QQmlMetaTypeData::VersionedUri::~VersionedUri()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData12VersionedUriD1Ev(
    QQmlMetaTypeData::VersionedUri *self) {
  delete self;
}
