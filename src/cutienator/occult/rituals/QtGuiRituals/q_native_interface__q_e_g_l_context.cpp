//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
#include <QtGui/qopenglcontext.h>
#include <cstring>

//  A QNativeInterface::QEGLContext that Python can take functions over in. Every QNativeInterface::QEGLContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_QEGLContextCall0)(const void *, int *);
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
class CuteQNativeInterface_QEGLContext : public QNativeInterface::QEGLContext {
public:
  using QNativeInterface::QEGLContext::QEGLContext;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface11QEGLContext17invalidateContextEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
  //  void QNativeInterface::QEGLContext::invalidateContext()
  void invalidateContext() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QEGLContextCall0 call = reinterpret_cast<CuteQNativeInterface_QEGLContextCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
};

//  QNativeInterface::QEGLContext::~QEGLContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface11QEGLContextD1Ev(
    QNativeInterface::QEGLContext *self) {
  delete self;
}

//  void QNativeInterface::QEGLContext::invalidateContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface11QEGLContext17invalidateContextEv(
    QNativeInterface::QEGLContext *self) {
  self->invalidateContext();
}

//  a Python function taken by a CuteQNativeInterface_QEGLContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QEGLContext(
    QNativeInterface::QEGLContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QEGLContext *>(self)->take(key, call);
}

#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
