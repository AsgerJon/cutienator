//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertyresolver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlPropertyResolver::QQmlPropertyResolver(const
//      QQmlPropertyCache::ConstPtr &cache)
extern "C" Q_DECL_EXPORT
QQmlPropertyResolver *ritual_ZN20QQmlPropertyResolverC1ERKN17QQmlPropertyCache8ConstPtrE(
    const QQmlPropertyCache::ConstPtr *cache) {
  return new QQmlPropertyResolver(*cache);
}

//  const QQmlPropertyData *QQmlPropertyResolver::property(int index) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK20QQmlPropertyResolver8propertyEi(
    const QQmlPropertyResolver *self,
    int index) {
  return self->property(index);
}

//  const QQmlPropertyData *QQmlPropertyResolver::property(const QString
//      &name, bool *notInRevision, RevisionCheck check) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK20QQmlPropertyResolver8propertyERK7QStringPbNS_13RevisionCheckE(
    const QQmlPropertyResolver *self,
    const QString *name,
    bool *notInRevision,
    QQmlPropertyResolver::RevisionCheck check) {
  return self->property(*name, notInRevision, check);
}

//  const QQmlPropertyData *QQmlPropertyResolver::signal(const QString &name,
//      bool *notInRevision, RevisionCheck check) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK20QQmlPropertyResolver6signalERK7QStringPbNS_13RevisionCheckE(
    const QQmlPropertyResolver *self,
    const QString *name,
    bool *notInRevision,
    QQmlPropertyResolver::RevisionCheck check) {
  return self->signal(*name, notInRevision, check);
}

//  QQmlPropertyResolver::~QQmlPropertyResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlPropertyResolverD1Ev(QQmlPropertyResolver *self) {
  delete self;
}
