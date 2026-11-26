//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 1. Kept as it is
//  when the generator runs again.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlEntityResolver that Python can take functions over in. Every QXmlEntityResolver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQXmlEntityResolverCall0)(const void *, int *);
class CuteQXmlEntityResolver : public QXmlEntityResolver {
public:
  using QXmlEntityResolver::QXmlEntityResolver;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QXmlEntityResolver11errorStringEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QString QXmlEntityResolver::errorString() const
  QString errorString() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlEntityResolverCall0 call = reinterpret_cast<CuteQXmlEntityResolverCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QXmlEntityResolver::~QXmlEntityResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QXmlEntityResolverD1Ev(QXmlEntityResolver *self) {
  delete self;
}

//  QString QXmlEntityResolver::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QXmlEntityResolver11errorStringEv(
    const QXmlEntityResolver *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQXmlEntityResolver, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlEntityResolver(
    QXmlEntityResolver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlEntityResolver *>(self)->take(key, call);
}

//  bool QXmlEntityResolver::resolveEntity(const QString &publicId, const
//      QString &systemId, QXmlInputSource *&ret)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QXmlEntityResolver13resolveEntityERK7QStringS2_RP15QXmlInputSource(
    QXmlEntityResolver *self,
    const QString *publicId,
    const QString *systemId,
    QXmlInputSource **ret) {
  return self->resolveEntity(*publicId, *systemId, *ret);
}
