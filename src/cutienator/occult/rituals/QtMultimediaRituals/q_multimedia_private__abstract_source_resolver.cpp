//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_source_resolver_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmultimedia_source_resolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <cstring>

//  A QMultimediaPrivate::AbstractSourceResolver that Python can take functions over in. Every QMultimediaPrivate::AbstractSourceResolver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQMultimediaPrivate_AbstractSourceResolverCall0)(const void *, const QUrl *, int *);
class CuteQMultimediaPrivate_AbstractSourceResolver : public QMultimediaPrivate::AbstractSourceResolver {
public:
  using QMultimediaPrivate::AbstractSourceResolver::AbstractSourceResolver;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QMultimediaPrivate22AbstractSourceResolver7resolveE4QUrl")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QUrl QMultimediaPrivate::AbstractSourceResolver::resolve(QUrl a0)
  //      const
  QUrl resolve(QUrl a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMultimediaPrivate_AbstractSourceResolverCall0 call = reinterpret_cast<CuteQMultimediaPrivate_AbstractSourceResolverCall0>(taken[0]);
      const QUrl * given = call(this, &a0, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QMultimediaPrivate::AbstractSourceResolver::~AbstractSourceResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMultimediaPrivate22AbstractSourceResolverD1Ev(
    QMultimediaPrivate::AbstractSourceResolver *self) {
  delete self;
}

//  QUrl QMultimediaPrivate::AbstractSourceResolver::resolve(QUrl a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QMultimediaPrivate22AbstractSourceResolver7resolveE4QUrl(
    const QMultimediaPrivate::AbstractSourceResolver *self,
    const QUrl *a0) {
  return new QUrl(self->resolve(*a0));
}

//  a Python function taken by a
//      CuteQMultimediaPrivate_AbstractSourceResolver, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMultimediaPrivate_AbstractSourceResolver(
    QMultimediaPrivate::AbstractSourceResolver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMultimediaPrivate_AbstractSourceResolver *>(self)->take(key, call);
}
