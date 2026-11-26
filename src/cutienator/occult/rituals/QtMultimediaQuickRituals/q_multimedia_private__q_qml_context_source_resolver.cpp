//  Written by dev_tooling.RitualGenerator from the records of QtMultimediaQu
//  ick/6.12.0/QtMultimediaQuick/private/qqmlcontext_source_resolver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qqmlcontext_source_resolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  QMultimediaPrivate::QQmlContextSourceResolver::QQmlContextSourceResolver(
//      QObject *objectForContext)
extern "C" Q_DECL_EXPORT
QMultimediaPrivate::QQmlContextSourceResolver *ritual_ZN18QMultimediaPrivate25QQmlContextSourceResolverC1EP7QObject(
    QObject *objectForContext) {
  return new QMultimediaPrivate::QQmlContextSourceResolver(objectForContext);
}

//  QUrl QMultimediaPrivate::QQmlContextSourceResolver::resolve(QUrl a0)
//      const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QMultimediaPrivate25QQmlContextSourceResolver7resolveE4QUrl(
    const QMultimediaPrivate::QQmlContextSourceResolver *self,
    const QUrl *a0) {
  return new QUrl(self->resolve(*a0));
}

//  QMultimediaPrivate::QQmlContextSourceResolver::~QQmlContextSourceResolver
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMultimediaPrivate25QQmlContextSourceResolverD1Ev(
    QMultimediaPrivate::QQmlContextSourceResolver *self) {
  delete self;
}
