//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QNativeInterface::Private::QGLXIntegration that Python can take functions over in. Every QNativeInterface::Private::QGLXIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin)
typedef void * (*CuteQNativeInterface_Private_QGLXIntegrationCall0)(const void *, GLXContext, void *, QOpenGLContext *, int *);
#endif  // QT_CONFIG(xcb_glx_plugin)
#endif  // !defined(QT_NO_OPENGL)
class CuteQNativeInterface_Private_QGLXIntegration : public QNativeInterface::Private::QGLXIntegration {
public:
  using QNativeInterface::Private::QGLXIntegration::QGLXIntegration;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin)
    if (!std::strcmp(key, "_ZNK16QNativeInterface7Private15QGLXIntegration19createOpenGLContextEP15__GLXcontextRecPvP14QOpenGLContext")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb_glx_plugin)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(xcb_glx_plugin)
  //  QOpenGLContext *QNativeInterface::Private::QGLXIntegration::createOpe
  //      nGLContext(GLXContext context, void *visualInfo, QOpenGLContext
  //      *shareContext) const
  QOpenGLContext *createOpenGLContext(
      GLXContext context,
      void *visualInfo,
      QOpenGLContext *shareContext) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QGLXIntegrationCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QGLXIntegrationCall0>(taken[0]);
      void * given = call(this, context, visualInfo, shareContext, &handled);
      if (handled) return static_cast<QOpenGLContext *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(xcb_glx_plugin)
#endif  // !defined(QT_NO_OPENGL)
};

//  QNativeInterface::Private::QGLXIntegration::~QGLXIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QGLXIntegrationD1Ev(
    QNativeInterface::Private::QGLXIntegration *self) {
  delete self;
}

//  QNativeInterface::Private::QGLXIntegration::QGLXIntegration()
extern "C" Q_DECL_EXPORT
QNativeInterface::Private::QGLXIntegration *ritual_ZN16QNativeInterface7Private15QGLXIntegrationC1Ev() {
  return new CuteQNativeInterface_Private_QGLXIntegration();
}

//  QOpenGLContext *QNativeInterface::Private::QGLXIntegration::createOpenGLC
//      ontext(GLXContext context, void *visualInfo, QOpenGLContext
//      *shareContext) const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK16QNativeInterface7Private15QGLXIntegration19createOpenGLContextEP15__GLXcontextRecPvP14QOpenGLContext(
    const QNativeInterface::Private::QGLXIntegration *self,
    GLXContext context,
    void *visualInfo,
    QOpenGLContext *shareContext) {
  return self->createOpenGLContext(context, visualInfo, shareContext);
}

//  a Python function taken by a
//      CuteQNativeInterface_Private_QGLXIntegration, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QGLXIntegration(
    QNativeInterface::Private::QGLXIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QGLXIntegration *>(self)->take(key, call);
}

#endif  // QT_CONFIG(xcb_glx_plugin)
#endif  // !defined(QT_NO_OPENGL)
