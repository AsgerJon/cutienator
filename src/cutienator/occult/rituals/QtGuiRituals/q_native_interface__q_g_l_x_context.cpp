//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#include <QtGui/qopenglcontext.h>
#include <cstring>

//  A QNativeInterface::QGLXContext that Python can take functions over in. Every QNativeInterface::QGLXContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QGLXContextCall0)(const void *, int *);
#endif  // QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
class CuteQNativeInterface_QGLXContext : public QNativeInterface::QGLXContext {
public:
  using QNativeInterface::QGLXContext::QGLXContext;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface11QGLXContext13nativeContextEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
  //  GLXContext QNativeInterface::QGLXContext::nativeContext() const
  GLXContext nativeContext() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QGLXContextCall0 call = reinterpret_cast<CuteQNativeInterface_QGLXContextCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<GLXContext>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
};

//  QNativeInterface::QGLXContext::~QGLXContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface11QGLXContextD1Ev(
    QNativeInterface::QGLXContext *self) {
  delete self;
}

//  QNativeInterface::QGLXContext::QGLXContext()
extern "C" Q_DECL_EXPORT
QNativeInterface::QGLXContext *ritual_ZN16QNativeInterface11QGLXContextC1Ev() {
  return new CuteQNativeInterface_QGLXContext();
}

//  QOpenGLContext *QNativeInterface::QGLXContext::fromNative(GLXContext
//      configBasedContext, QOpenGLContext *shareContext)
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN16QNativeInterface11QGLXContext10fromNativeEP15__GLXcontextRecP14QOpenGLContext(
    GLXContext configBasedContext,
    QOpenGLContext *shareContext) {
  return QNativeInterface::QGLXContext::fromNative(
      configBasedContext,
      shareContext);
}

//  QOpenGLContext *QNativeInterface::QGLXContext::fromNative(GLXContext
//      visualBasedContext, void *visualInfo, QOpenGLContext *shareContext)
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN16QNativeInterface11QGLXContext10fromNativeEP15__GLXcontextRecPvP14QOpenGLContext(
    GLXContext visualBasedContext,
    void *visualInfo,
    QOpenGLContext *shareContext) {
  return QNativeInterface::QGLXContext::fromNative(
      visualBasedContext,
      visualInfo,
      shareContext);
}

//  GLXContext QNativeInterface::QGLXContext::nativeContext() const
extern "C" Q_DECL_EXPORT
GLXContext ritual_ZNK16QNativeInterface11QGLXContext13nativeContextEv(
    const QNativeInterface::QGLXContext *self) {
  return self->nativeContext();
}

//  a Python function taken by a CuteQNativeInterface_QGLXContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QGLXContext(
    QNativeInterface::QGLXContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QGLXContext *>(self)->take(key, call);
}

#endif  // QT_CONFIG(xcb_glx_plugin) || defined(Q_QDOC)
#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
