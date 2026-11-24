//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickframebufferobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(opengl) || QT_CONFIG(opengles2) || QT_CONFIG(opengles3)
#include <QtQuick/qquickframebufferobject.h>
#include <QtCore/qsize.h>
#include <cstring>

//  Only a class built on QQuickFramebufferObject::Renderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFramebufferObject_Renderer : QQuickFramebufferObject::Renderer {
  using QQuickFramebufferObject::Renderer::createFramebufferObject;
  using QQuickFramebufferObject::Renderer::synchronize;
};

//  A QQuickFramebufferObject::Renderer that Python can take functions over in. Every QQuickFramebufferObject::Renderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFramebufferObject_RendererCall0)(const void *, int *);
typedef void * (*CuteQQuickFramebufferObject_RendererCall1)(const void *, const QSize *, int *);
typedef void (*CuteQQuickFramebufferObject_RendererCall2)(const void *, QQuickFramebufferObject *, int *);
class CuteQQuickFramebufferObject_Renderer : public QQuickFramebufferObject::Renderer {
public:
  using QQuickFramebufferObject::Renderer::Renderer;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQuickFramebufferObject8Renderer6renderEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuickFramebufferObject8Renderer23createFramebufferObjectERK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuickFramebufferObject8Renderer11synchronizeEPS_")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QQuickFramebufferObject::Renderer::render()
  void render() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFramebufferObject_RendererCall0 call = reinterpret_cast<CuteQQuickFramebufferObject_RendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QOpenGLFramebufferObject
  //      *QQuickFramebufferObject::Renderer::createFramebufferObject(const
  //      QSize &size)
  QOpenGLFramebufferObject *createFramebufferObject(
      const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFramebufferObject_RendererCall1 call = reinterpret_cast<CuteQQuickFramebufferObject_RendererCall1>(taken[1]);
      void * given = call(this, &size, &handled);
      if (handled) return static_cast<QOpenGLFramebufferObject *>(given);
    }
    return QQuickFramebufferObject::Renderer::createFramebufferObject(size);
  }

  //  void QQuickFramebufferObject::Renderer::synchronize(QQuickFramebuffer
  //      Object *a0)
  void synchronize(QQuickFramebufferObject *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFramebufferObject_RendererCall2 call = reinterpret_cast<CuteQQuickFramebufferObject_RendererCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickFramebufferObject::Renderer::synchronize(a0);
  }
};

//  QQuickFramebufferObject::Renderer::~Renderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject8RendererD1Ev(
    QQuickFramebufferObject::Renderer *self) {
  delete self;
}

//  void QQuickFramebufferObject::Renderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject8Renderer6renderEv(
    QQuickFramebufferObject::Renderer *self) {
  self->render();
}

//  QOpenGLFramebufferObject
//      *QQuickFramebufferObject::Renderer::createFramebufferObject(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZN23QQuickFramebufferObject8Renderer23createFramebufferObjectERK5QSize(
    QQuickFramebufferObject::Renderer *self,
    const QSize *size) {
  return self->createFramebufferObject(*size);
}

//  void
//      QQuickFramebufferObject::Renderer::synchronize(QQuickFramebufferObjec
//      t *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject8Renderer11synchronizeEPS_(
    QQuickFramebufferObject::Renderer *self,
    QQuickFramebufferObject *a0) {
  self->synchronize(a0);
}

//  QOpenGLFramebufferObject
//      *QQuickFramebufferObject::Renderer::framebufferObject() const
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_ZNK23QQuickFramebufferObject8Renderer17framebufferObjectEv(
    const QQuickFramebufferObject::Renderer *self) {
  return self->framebufferObject();
}

//  void QQuickFramebufferObject::Renderer::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject8Renderer6updateEv(
    QQuickFramebufferObject::Renderer *self) {
  self->update();
}

//  void QQuickFramebufferObject::Renderer::invalidateFramebufferObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickFramebufferObject8Renderer27invalidateFramebufferObjectEv(
    QQuickFramebufferObject::Renderer *self) {
  self->invalidateFramebufferObject();
}

//  a Python function taken by a CuteQQuickFramebufferObject_Renderer, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFramebufferObject_Renderer(
    QQuickFramebufferObject::Renderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFramebufferObject_Renderer *>(self)->take(key, call);
}

//  QOpenGLFramebufferObject
//      *QQuickFramebufferObject::Renderer::createFramebufferObject(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
QOpenGLFramebufferObject *ritual_own_ZN23QQuickFramebufferObject8Renderer23createFramebufferObjectERK5QSize(
    QQuickFramebufferObject::Renderer *self,
    const QSize *size) {
  return static_cast<OwnQQuickFramebufferObject_Renderer *>(self)->OwnQQuickFramebufferObject_Renderer::createFramebufferObject(
      *size);
}

//  void
//      QQuickFramebufferObject::Renderer::synchronize(QQuickFramebufferObjec
//      t *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickFramebufferObject8Renderer11synchronizeEPS_(
    QQuickFramebufferObject::Renderer *self,
    QQuickFramebufferObject *a0) {
  static_cast<OwnQQuickFramebufferObject_Renderer *>(self)->OwnQQuickFramebufferObject_Renderer::synchronize(
      a0);
}

#endif  // QT_CONFIG(opengl) || QT_CONFIG(opengles2) || QT_CONFIG(opengles3)
