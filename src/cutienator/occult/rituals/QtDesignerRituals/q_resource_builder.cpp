//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/resourcebuilder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/resourcebuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qdir.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QResourceBuilder that Python can take functions over in. Every QResourceBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQResourceBuilderCall0)(const void *, const QDir *, const DomProperty *, int *);
typedef const QVariant * (*CuteQResourceBuilderCall1)(const void *, const QVariant *, int *);
typedef void * (*CuteQResourceBuilderCall2)(const void *, const QDir *, const QVariant *, int *);
typedef bool (*CuteQResourceBuilderCall3)(const void *, const DomProperty *, int *);
typedef bool (*CuteQResourceBuilderCall4)(const void *, const QVariant *, int *);
class CuteQResourceBuilder : public QResourceBuilder {
public:
  using QResourceBuilder::QResourceBuilder;
  CuteQResourceBuilder(const QResourceBuilder & other) : QResourceBuilder(other) {}
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomProperty")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QResourceBuilder13toNativeValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProperty")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QResourceBuilder14isResourceTypeERK8QVariant")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QVariant QResourceBuilder::loadResource(const QDir &workingDirectory,
  //      const DomProperty *property) const
  QVariant loadResource(
      const QDir &workingDirectory,
      const DomProperty *property) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQResourceBuilderCall0 call = reinterpret_cast<CuteQResourceBuilderCall0>(taken[0]);
      const QVariant * given = call(this, &workingDirectory, property, &handled);
      if (handled && given) return *given;
    }
    return QResourceBuilder::loadResource(workingDirectory, property);
  }

  //  QVariant QResourceBuilder::toNativeValue(const QVariant &value) const
  QVariant toNativeValue(const QVariant &value) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQResourceBuilderCall1 call = reinterpret_cast<CuteQResourceBuilderCall1>(taken[1]);
      const QVariant * given = call(this, &value, &handled);
      if (handled && given) return *given;
    }
    return QResourceBuilder::toNativeValue(value);
  }

  //  DomProperty *QResourceBuilder::saveResource(const QDir
  //      &workingDirectory, const QVariant &value) const
  DomProperty *saveResource(
      const QDir &workingDirectory,
      const QVariant &value) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQResourceBuilderCall2 call = reinterpret_cast<CuteQResourceBuilderCall2>(taken[2]);
      void * given = call(this, &workingDirectory, &value, &handled);
      if (handled) return static_cast<DomProperty *>(given);
    }
    return QResourceBuilder::saveResource(workingDirectory, value);
  }

  //  bool QResourceBuilder::isResourceProperty(const DomProperty *p) const
  bool isResourceProperty(const DomProperty *p) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQResourceBuilderCall3 call = reinterpret_cast<CuteQResourceBuilderCall3>(taken[3]);
      bool given = call(this, p, &handled);
      if (handled) return given;
    }
    return QResourceBuilder::isResourceProperty(p);
  }

  //  bool QResourceBuilder::isResourceType(const QVariant &value) const
  bool isResourceType(const QVariant &value) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQResourceBuilderCall4 call = reinterpret_cast<CuteQResourceBuilderCall4>(taken[4]);
      bool given = call(this, &value, &handled);
      if (handled) return given;
    }
    return QResourceBuilder::isResourceType(value);
  }
};

//  QResourceBuilder::QResourceBuilder()
extern "C" Q_DECL_EXPORT
QResourceBuilder *ritual_ZN16QResourceBuilderC1Ev() {
  return new CuteQResourceBuilder();
}

//  QResourceBuilder::~QResourceBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QResourceBuilderD1Ev(QResourceBuilder *self) {
  delete self;
}

//  const QStringList &QResourceBuilder::themeIconNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QResourceBuilder14themeIconNamesEv() {
  return new QList<QString>(QResourceBuilder::themeIconNames());
}

//  int QResourceBuilder::themeIconIndex(QStringView name)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QResourceBuilder14themeIconIndexE11QStringView(
    const QString *name) {
  return QResourceBuilder::themeIconIndex(QStringView(*name));
}

//  QString QResourceBuilder::fullyQualifiedThemeIconName(int i)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QResourceBuilder27fullyQualifiedThemeIconNameEi(int i) {
  return new QString(QResourceBuilder::fullyQualifiedThemeIconName(i));
}

//  QVariant QResourceBuilder::loadResource(const QDir &workingDirectory,
//      const DomProperty *property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomProperty(
    const QResourceBuilder *self,
    const QDir *workingDirectory,
    const DomProperty *property) {
  return new QVariant(self->loadResource(*workingDirectory, property));
}

//  QVariant QResourceBuilder::toNativeValue(const QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QResourceBuilder13toNativeValueERK8QVariant(
    const QResourceBuilder *self,
    const QVariant *value) {
  return new QVariant(self->toNativeValue(*value));
}

//  DomProperty *QResourceBuilder::saveResource(const QDir &workingDirectory,
//      const QVariant &value) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVariant(
    const QResourceBuilder *self,
    const QDir *workingDirectory,
    const QVariant *value) {
  return self->saveResource(*workingDirectory, *value);
}

//  bool QResourceBuilder::isResourceProperty(const DomProperty *p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProperty(
    const QResourceBuilder *self,
    const DomProperty *p) {
  return self->isResourceProperty(p);
}

//  bool QResourceBuilder::isResourceType(const QVariant &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QResourceBuilder14isResourceTypeERK8QVariant(
    const QResourceBuilder *self,
    const QVariant *value) {
  return self->isResourceType(*value);
}

//  int QResourceBuilder::iconStateFlags(const DomResourceIcon *resIcon)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QResourceBuilder14iconStateFlagsEPK15DomResourceIcon(
    const DomResourceIcon *resIcon) {
  return QResourceBuilder::iconStateFlags(resIcon);
}

//  a Python function taken by a CuteQResourceBuilder, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QResourceBuilder(
    QResourceBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQResourceBuilder *>(self)->take(key, call);
}

//  QVariant QResourceBuilder::loadResource(const QDir &workingDirectory,
//      const DomProperty *property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomProperty(
    const QResourceBuilder *self,
    const QDir *workingDirectory,
    const DomProperty *property) {
  return new QVariant(
      self->QResourceBuilder::loadResource(
          *workingDirectory,
          property));
}

//  QVariant QResourceBuilder::toNativeValue(const QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QResourceBuilder13toNativeValueERK8QVariant(
    const QResourceBuilder *self,
    const QVariant *value) {
  return new QVariant(self->QResourceBuilder::toNativeValue(*value));
}

//  DomProperty *QResourceBuilder::saveResource(const QDir &workingDirectory,
//      const QVariant &value) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_own_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVariant(
    const QResourceBuilder *self,
    const QDir *workingDirectory,
    const QVariant *value) {
  return self->QResourceBuilder::saveResource(*workingDirectory, *value);
}

//  bool QResourceBuilder::isResourceProperty(const DomProperty *p) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProperty(
    const QResourceBuilder *self,
    const DomProperty *p) {
  return self->QResourceBuilder::isResourceProperty(p);
}

//  bool QResourceBuilder::isResourceType(const QVariant &value) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QResourceBuilder14isResourceTypeERK8QVariant(
    const QResourceBuilder *self,
    const QVariant *value) {
  return self->QResourceBuilder::isResourceType(*value);
}
