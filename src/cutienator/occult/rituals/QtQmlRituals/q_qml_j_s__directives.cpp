//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QQmlJS::Directives that Python can take functions over in. Every QQmlJS::Directives
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_DirectivesCall0)(const void *, int *);
typedef void (*CuteQQmlJS_DirectivesCall1)(const void *, const QString *, const QString *, int, int, int *);
typedef void (*CuteQQmlJS_DirectivesCall2)(const void *, const QString *, const QString *, const QString *, int, int, int *);
class CuteQQmlJS_Directives : public QQmlJS::Directives {
public:
  using QQmlJS::Directives::Directives;
  CuteQQmlJS_Directives(const QQmlJS::Directives &other) : QQmlJS::Directives(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS10Directives13pragmaLibraryEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_ii")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::Directives::pragmaLibrary()
  void pragmaLibrary() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_DirectivesCall0 call = reinterpret_cast<CuteQQmlJS_DirectivesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJS::Directives::pragmaLibrary();
  }

  //  void QQmlJS::Directives::importFile(const QString &jsfile, const
  //      QString &module, int line, int column)
  void importFile(
      const QString &jsfile,
      const QString &module,
      int line,
      int column) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_DirectivesCall1 call = reinterpret_cast<CuteQQmlJS_DirectivesCall1>(taken[1]);
      call(this, &jsfile, &module, line, column, &handled);
      if (handled) return;
    }
    QQmlJS::Directives::importFile(jsfile, module, line, column);
  }

  //  void QQmlJS::Directives::importModule(const QString &uri, const
  //      QString &version, const QString &module, int line, int column)
  void importModule(
      const QString &uri,
      const QString &version,
      const QString &module,
      int line,
      int column) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_DirectivesCall2 call = reinterpret_cast<CuteQQmlJS_DirectivesCall2>(taken[2]);
      call(this, &uri, &version, &module, line, column, &handled);
      if (handled) return;
    }
    QQmlJS::Directives::importModule(uri, version, module, line, column);
  }
};

//  QQmlJS::Directives::~Directives()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10DirectivesD1Ev(QQmlJS::Directives *self) {
  delete self;
}

//  void QQmlJS::Directives::pragmaLibrary()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10Directives13pragmaLibraryEv(
    QQmlJS::Directives *self) {
  self->pragmaLibrary();
}

//  void QQmlJS::Directives::importFile(const QString &jsfile, const QString
//      &module, int line, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii(
    QQmlJS::Directives *self,
    const QString *jsfile,
    const QString *module,
    int line,
    int column) {
  self->importFile(*jsfile, *module, line, column);
}

//  void QQmlJS::Directives::importModule(const QString &uri, const QString
//      &version, const QString &module, int line, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_ii(
    QQmlJS::Directives *self,
    const QString *uri,
    const QString *version,
    const QString *module,
    int line,
    int column) {
  self->importModule(*uri, *version, *module, line, column);
}

//  a Python function taken by a CuteQQmlJS_Directives, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_Directives(
    QQmlJS::Directives *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_Directives *>(self)->take(key, call);
}

//  void QQmlJS::Directives::pragmaLibrary()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS10Directives13pragmaLibraryEv(
    QQmlJS::Directives *self) {
  self->QQmlJS::Directives::pragmaLibrary();
}

//  void QQmlJS::Directives::importFile(const QString &jsfile, const QString
//      &module, int line, int column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii(
    QQmlJS::Directives *self,
    const QString *jsfile,
    const QString *module,
    int line,
    int column) {
  self->QQmlJS::Directives::importFile(*jsfile, *module, line, column);
}

//  void QQmlJS::Directives::importModule(const QString &uri, const QString
//      &version, const QString &module, int line, int column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_ii(
    QQmlJS::Directives *self,
    const QString *uri,
    const QString *version,
    const QString *module,
    int line,
    int column) {
  self->QQmlJS::Directives::importModule(
      *uri,
      *version,
      *module,
      line,
      column);
}
