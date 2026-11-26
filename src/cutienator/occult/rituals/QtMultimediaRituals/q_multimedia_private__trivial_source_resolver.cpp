//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_source_resolver_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_source_resolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  QMultimediaPrivate::TrivialSourceResolver::~TrivialSourceResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMultimediaPrivate21TrivialSourceResolverD1Ev(
    QMultimediaPrivate::TrivialSourceResolver *self) {
  delete self;
}

//  QUrl QMultimediaPrivate::TrivialSourceResolver::resolve(QUrl a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QMultimediaPrivate21TrivialSourceResolver7resolveE4QUrl(
    const QMultimediaPrivate::TrivialSourceResolver *self,
    const QUrl *a0) {
  return new QUrl(self->resolve(*a0));
}
