//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QNativeInterface::Private::QEGLIntegration that Python can take functions over in. Every QNativeInterface::Private::QEGLIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl)
typedef void * (*CuteQNativeInterface_Private_QEGLIntegrationCall0)(const void *, EGLContext, EGLDisplay, QOpenGLContext *, int *);
#endif  // QT_CONFIG(egl)
#endif  // !defined(QT_NO_OPENGL)
class CuteQNativeInterface_Private_QEGLIntegration : public QNativeInterface::Private::QEGLIntegration {
public:
  using QNativeInterface::Private::QEGLIntegration::QEGLIntegration;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl)
    if (!std::strcmp(key, "_ZNK16QNativeInterface7Private15QEGLIntegration19createOpenGLContextEPvS2_P14QOpenGLContext")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(egl)
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
#if QT_CONFIG(egl)
  //  QOpenGLContext *QNativeInterface::Private::QEGLIntegration::createOpe
  //      nGLContext(EGLContext context, EGLDisplay display, QOpenGLContext
  //      *shareContext) const
  QOpenGLContext *createOpenGLContext(
      EGLContext context,
      EGLDisplay display,
      QOpenGLContext *shareContext) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QEGLIntegrationCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QEGLIntegrationCall0>(taken[0]);
      void * given = call(this, context, display, shareContext, &handled);
      if (handled) return static_cast<QOpenGLContext *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(egl)
#endif  // !defined(QT_NO_OPENGL)
};

//  QNativeInterface::Private::QEGLIntegration::~QEGLIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QEGLIntegrationD1Ev(
    QNativeInterface::Private::QEGLIntegration *self) {
  delete self;
}

//  QNativeInterface::Private::QEGLIntegration::QEGLIntegration()
extern "C" Q_DECL_EXPORT
QNativeInterface::Private::QEGLIntegration *ritual_ZN16QNativeInterface7Private15QEGLIntegrationC1Ev() {
  return new CuteQNativeInterface_Private_QEGLIntegration();
}

//  QOpenGLContext *QNativeInterface::Private::QEGLIntegration::createOpenGLC
//      ontext(EGLContext context, EGLDisplay display, QOpenGLContext
//      *shareContext) const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK16QNativeInterface7Private15QEGLIntegration19createOpenGLContextEPvS2_P14QOpenGLContext(
    const QNativeInterface::Private::QEGLIntegration *self,
    EGLContext context,
    EGLDisplay display,
    QOpenGLContext *shareContext) {
  return self->createOpenGLContext(context, display, shareContext);
}

//  a Python function taken by a
//      CuteQNativeInterface_Private_QEGLIntegration, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QEGLIntegration(
    QNativeInterface::Private::QEGLIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QEGLIntegration *>(self)->take(key, call);
}

#endif  // QT_CONFIG(egl)
#endif  // !defined(QT_NO_OPENGL)
