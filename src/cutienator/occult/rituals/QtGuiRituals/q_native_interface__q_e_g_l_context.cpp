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
typedef void * (*CuteQNativeInterface_QEGLContextCall0)(const void *, int *);
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QEGLContextCall1)(const void *, int *);
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QEGLContextCall2)(const void *, int *);
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_QEGLContextCall3)(const void *, int *);
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
class CuteQNativeInterface_QEGLContext : public QNativeInterface::QEGLContext {
public:
  using QNativeInterface::QEGLContext::QEGLContext;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface11QEGLContext13nativeContextEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface11QEGLContext6configEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface11QEGLContext7displayEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface11QEGLContext17invalidateContextEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
  //  EGLContext QNativeInterface::QEGLContext::nativeContext() const
  EGLContext nativeContext() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QEGLContextCall0 call = reinterpret_cast<CuteQNativeInterface_QEGLContextCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<EGLContext>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
  //  EGLConfig QNativeInterface::QEGLContext::config() const
  EGLConfig config() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_QEGLContextCall1 call = reinterpret_cast<CuteQNativeInterface_QEGLContextCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<EGLConfig>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
  //  EGLDisplay QNativeInterface::QEGLContext::display() const
  EGLDisplay display() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeInterface_QEGLContextCall2 call = reinterpret_cast<CuteQNativeInterface_QEGLContextCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<EGLDisplay>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(egl) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl) || defined(Q_QDOC)
  //  void QNativeInterface::QEGLContext::invalidateContext()
  void invalidateContext() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeInterface_QEGLContextCall3 call = reinterpret_cast<CuteQNativeInterface_QEGLContextCall3>(taken[3]);
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

//  QNativeInterface::QEGLContext::QEGLContext()
extern "C" Q_DECL_EXPORT
QNativeInterface::QEGLContext *ritual_ZN16QNativeInterface11QEGLContextC1Ev() {
  return new CuteQNativeInterface_QEGLContext();
}

//  QOpenGLContext *QNativeInterface::QEGLContext::fromNative(EGLContext
//      context, EGLDisplay display, QOpenGLContext *shareContext)
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN16QNativeInterface11QEGLContext10fromNativeEPvS1_P14QOpenGLContext(
    EGLContext context,
    EGLDisplay display,
    QOpenGLContext *shareContext) {
  return QNativeInterface::QEGLContext::fromNative(
      context,
      display,
      shareContext);
}

//  EGLContext QNativeInterface::QEGLContext::nativeContext() const
extern "C" Q_DECL_EXPORT
EGLContext ritual_ZNK16QNativeInterface11QEGLContext13nativeContextEv(
    const QNativeInterface::QEGLContext *self) {
  return self->nativeContext();
}

//  EGLConfig QNativeInterface::QEGLContext::config() const
extern "C" Q_DECL_EXPORT
EGLConfig ritual_ZNK16QNativeInterface11QEGLContext6configEv(
    const QNativeInterface::QEGLContext *self) {
  return self->config();
}

//  EGLDisplay QNativeInterface::QEGLContext::display() const
extern "C" Q_DECL_EXPORT
EGLDisplay ritual_ZNK16QNativeInterface11QEGLContext7displayEv(
    const QNativeInterface::QEGLContext *self) {
  return self->display();
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
