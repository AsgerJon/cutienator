//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QXmlStreamEntityResolver that Python can take functions over in. Every QXmlStreamEntityResolver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQXmlStreamEntityResolverCall0)(const void *, const QString *, int *);
class CuteQXmlStreamEntityResolver : public QXmlStreamEntityResolver {
public:
  using QXmlStreamEntityResolver::QXmlStreamEntityResolver;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QString QXmlStreamEntityResolver::resolveUndeclaredEntity(const
  //      QString &name)
  QString resolveUndeclaredEntity(const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlStreamEntityResolverCall0 call = reinterpret_cast<CuteQXmlStreamEntityResolverCall0>(taken[0]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QXmlStreamEntityResolver::resolveUndeclaredEntity(name);
  }
};

//  QXmlStreamEntityResolver::QXmlStreamEntityResolver()
extern "C" Q_DECL_EXPORT
QXmlStreamEntityResolver *ritual_ZN24QXmlStreamEntityResolverC1Ev() {
  return new CuteQXmlStreamEntityResolver();
}

//  QXmlStreamEntityResolver::~QXmlStreamEntityResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QXmlStreamEntityResolverD1Ev(
    QXmlStreamEntityResolver *self) {
  delete self;
}

//  QString QXmlStreamEntityResolver::resolveEntity(const QString &publicId,
//      const QString &systemId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QXmlStreamEntityResolver13resolveEntityERK7QStringS2_(
    QXmlStreamEntityResolver *self,
    const QString *publicId,
    const QString *systemId) {
  return new QString(self->resolveEntity(*publicId, *systemId));
}

//  QString QXmlStreamEntityResolver::resolveUndeclaredEntity(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QString(
    QXmlStreamEntityResolver *self,
    const QString *name) {
  return new QString(self->resolveUndeclaredEntity(*name));
}

//  a Python function taken by a CuteQXmlStreamEntityResolver, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlStreamEntityResolver(
    QXmlStreamEntityResolver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlStreamEntityResolver *>(self)->take(key, call);
}

//  QString QXmlStreamEntityResolver::resolveUndeclaredEntity(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QString(
    QXmlStreamEntityResolver *self,
    const QString *name) {
  return new QString(
      self->QXmlStreamEntityResolver::resolveUndeclaredEntity(
          *name));
}
