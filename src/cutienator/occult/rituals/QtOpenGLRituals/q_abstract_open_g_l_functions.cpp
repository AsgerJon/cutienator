//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglversionfunctions.h>
#include <cstring>

//  A QAbstractOpenGLFunctions that Python can take functions over in. Every QAbstractOpenGLFunctions
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef bool (*CuteQAbstractOpenGLFunctionsCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQAbstractOpenGLFunctions : public QAbstractOpenGLFunctions {
public:
  using QAbstractOpenGLFunctions::QAbstractOpenGLFunctions;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  bool QAbstractOpenGLFunctions::initializeOpenGLFunctions()
  bool initializeOpenGLFunctions() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractOpenGLFunctionsCall0 call = reinterpret_cast<CuteQAbstractOpenGLFunctionsCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractOpenGLFunctions::initializeOpenGLFunctions();
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QAbstractOpenGLFunctions::~QAbstractOpenGLFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractOpenGLFunctionsD1Ev(
    QAbstractOpenGLFunctions *self) {
  delete self;
}

//  bool QAbstractOpenGLFunctions::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv(
    QAbstractOpenGLFunctions *self) {
  return self->initializeOpenGLFunctions();
}

//  QAbstractOpenGLFunctionsPrivate *QAbstractOpenGLFunctions::d_func()
extern "C" Q_DECL_EXPORT
QAbstractOpenGLFunctionsPrivate *ritual_ZN24QAbstractOpenGLFunctions6d_funcEv(
    QAbstractOpenGLFunctions *self) {
  return self->d_func();
}

//  const QAbstractOpenGLFunctionsPrivate *QAbstractOpenGLFunctions::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractOpenGLFunctionsPrivate *ritual_ZNK24QAbstractOpenGLFunctions6d_funcEv(
    const QAbstractOpenGLFunctions *self) {
  return self->d_func();
}

//  QAbstractOpenGLFunctions::QAbstractOpenGLFunctions()
extern "C" Q_DECL_EXPORT
QAbstractOpenGLFunctions *ritual_ZN24QAbstractOpenGLFunctionsC1Ev() {
  return new CuteQAbstractOpenGLFunctions();
}

//  bool QAbstractOpenGLFunctions::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractOpenGLFunctions13isInitializedEv(
    const QAbstractOpenGLFunctions *self) {
  return self->isInitialized();
}

//  void QAbstractOpenGLFunctions::setOwningContext(const QOpenGLContext
//      *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractOpenGLFunctions16setOwningContextEPK14QOpenGLContext(
    QAbstractOpenGLFunctions *self,
    const QOpenGLContext *context) {
  self->setOwningContext(context);
}

//  QOpenGLContext *QAbstractOpenGLFunctions::owningContext() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK24QAbstractOpenGLFunctions13owningContextEv(
    const QAbstractOpenGLFunctions *self) {
  return self->owningContext();
}

//  a Python function taken by a CuteQAbstractOpenGLFunctions, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractOpenGLFunctions(
    QAbstractOpenGLFunctions *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractOpenGLFunctions *>(self)->take(key, call);
}

//  bool QAbstractOpenGLFunctions::initializeOpenGLFunctions()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv(
    QAbstractOpenGLFunctions *self) {
  return self->QAbstractOpenGLFunctions::initializeOpenGLFunctions();
}

#endif  // !defined(QT_NO_OPENGL)
