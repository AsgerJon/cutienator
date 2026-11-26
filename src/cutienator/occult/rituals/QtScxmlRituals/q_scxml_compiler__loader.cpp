//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlcompiler.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlcompiler.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QScxmlCompiler::Loader that Python can take functions over in. Every QScxmlCompiler::Loader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QByteArray * (*CuteQScxmlCompiler_LoaderCall0)(const void *, const QString *, const QString *, QStringList *, int *);
class CuteQScxmlCompiler_Loader : public QScxmlCompiler::Loader {
public:
  using QScxmlCompiler::Loader::Loader;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QScxmlCompiler6Loader4loadERK7QStringS3_P5QListIS1_E")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QByteArray QScxmlCompiler::Loader::load(const QString &name, const
  //      QString &baseDir, QStringList *errors)
  QByteArray load(
      const QString &name,
      const QString &baseDir,
      QStringList *errors) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlCompiler_LoaderCall0 call = reinterpret_cast<CuteQScxmlCompiler_LoaderCall0>(taken[0]);
      const QByteArray * given = call(this, &name, &baseDir, errors, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QScxmlCompiler::Loader::Loader()
extern "C" Q_DECL_EXPORT
QScxmlCompiler::Loader *ritual_ZN14QScxmlCompiler6LoaderC1Ev() {
  return new CuteQScxmlCompiler_Loader();
}

//  QScxmlCompiler::Loader::~Loader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlCompiler6LoaderD1Ev(QScxmlCompiler::Loader *self) {
  delete self;
}

//  QByteArray QScxmlCompiler::Loader::load(const QString &name, const
//      QString &baseDir, QStringList *errors)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QScxmlCompiler6Loader4loadERK7QStringS3_P5QListIS1_E(
    QScxmlCompiler::Loader *self,
    const QString *name,
    const QString *baseDir,
    QStringList *errors) {
  return new QByteArray(self->load(*name, *baseDir, errors));
}

//  a Python function taken by a CuteQScxmlCompiler_Loader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlCompiler_Loader(
    QScxmlCompiler::Loader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlCompiler_Loader *>(self)->take(key, call);
}
