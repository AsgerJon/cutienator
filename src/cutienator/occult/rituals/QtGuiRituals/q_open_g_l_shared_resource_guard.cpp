//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qopenglcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QOpenGLSharedResourceGuard may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOpenGLSharedResourceGuard : QOpenGLSharedResourceGuard {
  using QOpenGLSharedResourceGuard::invalidateResource;
  using QOpenGLSharedResourceGuard::freeResource;
};

//  A QOpenGLSharedResourceGuard that Python can take functions over in. Every QOpenGLSharedResourceGuard
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLSharedResourceGuardCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLSharedResourceGuardCall1)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLSharedResourceGuard : public QOpenGLSharedResourceGuard {
public:
  using QOpenGLSharedResourceGuard::QOpenGLSharedResourceGuard;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource18invalidateResourceEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLSharedResourceGuard::invalidateResource()
  void invalidateResource() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLSharedResourceGuardCall0 call = reinterpret_cast<CuteQOpenGLSharedResourceGuardCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLSharedResourceGuard::invalidateResource();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLSharedResourceGuard::freeResource(QOpenGLContext
  //      *context)
  void freeResource(QOpenGLContext *context) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLSharedResourceGuardCall1 call = reinterpret_cast<CuteQOpenGLSharedResourceGuardCall1>(taken[1]);
      call(this, context, &handled);
      if (handled) return;
    }
    QOpenGLSharedResourceGuard::freeResource(context);
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLSharedResourceGuard::QOpenGLSharedResourceGuard(QOpenGLContext
//      *context, GLuint id, FreeResourceFunc func)
extern "C" Q_DECL_EXPORT
QOpenGLSharedResourceGuard *ritual_ZN26QOpenGLSharedResourceGuardC1EP14QOpenGLContextjPFvP16QOpenGLFunctionsjE(
    QOpenGLContext *context,
    GLuint id,
    void *func) {
  return new CuteQOpenGLSharedResourceGuard(
      context,
      id,
      reinterpret_cast<QOpenGLSharedResourceGuard::FreeResourceFunc>(func));
}

//  QOpenGLSharedResourceGuard::~QOpenGLSharedResourceGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLSharedResourceGuardD1Ev(
    QOpenGLSharedResourceGuard *self) {
  delete self;
}

//  GLuint QOpenGLSharedResourceGuard::id() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK26QOpenGLSharedResourceGuard2idEv(
    const QOpenGLSharedResourceGuard *self) {
  return self->id();
}

//  void QOpenGLSharedResourceGuard::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLSharedResourceGuard18invalidateResourceEv(
    QOpenGLSharedResourceGuard *self) {
  self->invalidateResource();
}

//  void QOpenGLSharedResourceGuard::freeResource(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpenGLSharedResourceGuard12freeResourceEP14QOpenGLContext(
    QOpenGLSharedResourceGuard *self,
    QOpenGLContext *context) {
  self->freeResource(context);
}

//  a Python function taken by a CuteQOpenGLSharedResourceGuard, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLSharedResourceGuard(
    QOpenGLSharedResourceGuard *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLSharedResourceGuard *>(self)->take(key, call);
}

//  void QOpenGLSharedResourceGuard::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QOpenGLSharedResourceGuard18invalidateResourceEv(
    QOpenGLSharedResourceGuard *self) {
  static_cast<OwnQOpenGLSharedResourceGuard *>(self)->OwnQOpenGLSharedResourceGuard::invalidateResource();
}

//  void QOpenGLSharedResourceGuard::freeResource(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QOpenGLSharedResourceGuard12freeResourceEP14QOpenGLContext(
    QOpenGLSharedResourceGuard *self,
    QOpenGLContext *context) {
  static_cast<OwnQOpenGLSharedResourceGuard *>(self)->OwnQOpenGLSharedResourceGuard::freeResource(
      context);
}

#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
