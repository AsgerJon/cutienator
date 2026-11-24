//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QmlIR::ScriptDirectivesCollector that Python can take functions over in. Every QmlIR::ScriptDirectivesCollector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQmlIR_ScriptDirectivesCollectorCall0)(const void *, int *);
typedef void (*CuteQmlIR_ScriptDirectivesCollectorCall1)(const void *, const QString *, const QString *, int, int, int *);
typedef void (*CuteQmlIR_ScriptDirectivesCollectorCall2)(const void *, const QString *, const QString *, const QString *, int, int, int *);
class CuteQmlIR_ScriptDirectivesCollector : public QmlIR::ScriptDirectivesCollector {
public:
  using QmlIR::ScriptDirectivesCollector::ScriptDirectivesCollector;
  CuteQmlIR_ScriptDirectivesCollector(const QmlIR::ScriptDirectivesCollector &other) : QmlIR::ScriptDirectivesCollector(other) {}
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

  //  void QmlIR::ScriptDirectivesCollector::pragmaLibrary()
  void pragmaLibrary() override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlIR_ScriptDirectivesCollectorCall0 call = reinterpret_cast<CuteQmlIR_ScriptDirectivesCollectorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QmlIR::ScriptDirectivesCollector::pragmaLibrary();
  }

  //  void QmlIR::ScriptDirectivesCollector::importFile(const QString
  //      &jsfile, const QString &module, int lineNumber, int column)
  void importFile(
      const QString &jsfile,
      const QString &module,
      int lineNumber,
      int column) override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlIR_ScriptDirectivesCollectorCall1 call = reinterpret_cast<CuteQmlIR_ScriptDirectivesCollectorCall1>(taken[1]);
      call(this, &jsfile, &module, lineNumber, column, &handled);
      if (handled) return;
    }
    QmlIR::ScriptDirectivesCollector::importFile(jsfile, module, lineNumber, column);
  }

  //  void QmlIR::ScriptDirectivesCollector::importModule(const QString
  //      &uri, const QString &version, const QString &module, int
  //      lineNumber, int column)
  void importModule(
      const QString &uri,
      const QString &version,
      const QString &module,
      int lineNumber,
      int column) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlIR_ScriptDirectivesCollectorCall2 call = reinterpret_cast<CuteQmlIR_ScriptDirectivesCollectorCall2>(taken[2]);
      call(this, &uri, &version, &module, lineNumber, column, &handled);
      if (handled) return;
    }
    QmlIR::ScriptDirectivesCollector::importModule(uri, version, module, lineNumber, column);
  }
};

//  QmlIR::ScriptDirectivesCollector::~ScriptDirectivesCollector()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR25ScriptDirectivesCollectorD1Ev(
    QmlIR::ScriptDirectivesCollector *self) {
  delete self;
}

//  a Python function taken by a CuteQmlIR_ScriptDirectivesCollector, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlIR_ScriptDirectivesCollector(
    QmlIR::ScriptDirectivesCollector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlIR_ScriptDirectivesCollector *>(self)->take(key, call);
}

//  void QmlIR::ScriptDirectivesCollector::pragmaLibrary()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR25ScriptDirectivesCollector13pragmaLibraryEv(
    QmlIR::ScriptDirectivesCollector *self) {
  self->QmlIR::ScriptDirectivesCollector::pragmaLibrary();
}

//  void QmlIR::ScriptDirectivesCollector::importFile(const QString &jsfile,
//      const QString &module, int lineNumber, int column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR25ScriptDirectivesCollector10importFileERK7QStringS3_ii(
    QmlIR::ScriptDirectivesCollector *self,
    const QString *jsfile,
    const QString *module,
    int lineNumber,
    int column) {
  self->QmlIR::ScriptDirectivesCollector::importFile(
      *jsfile,
      *module,
      lineNumber,
      column);
}

//  void QmlIR::ScriptDirectivesCollector::importModule(const QString &uri,
//      const QString &version, const QString &module, int lineNumber, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR25ScriptDirectivesCollector12importModuleERK7QStringS3_S3_ii(
    QmlIR::ScriptDirectivesCollector *self,
    const QString *uri,
    const QString *version,
    const QString *module,
    int lineNumber,
    int column) {
  self->QmlIR::ScriptDirectivesCollector::importModule(
      *uri,
      *version,
      *module,
      lineNumber,
      column);
}
