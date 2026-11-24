//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpenGLCompositorWindow that Python can take functions over in. Every QOpenGLCompositorWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQOpenGLCompositorWindowCall0)(const void *, int *);
typedef void * (*CuteQOpenGLCompositorWindowCall1)(const void *, int *);
typedef void (*CuteQOpenGLCompositorWindowCall2)(const void *, int *);
typedef void (*CuteQOpenGLCompositorWindowCall3)(const void *, int *);
typedef void (*CuteQOpenGLCompositorWindowCall4)(const void *, QOpenGLCompositorBackingStore *, int *);
typedef void * (*CuteQOpenGLCompositorWindowCall5)(const void *, int *);
class CuteQOpenGLCompositorWindow : public QOpenGLCompositorWindow {
public:
  using QOpenGLCompositorWindow::QOpenGLCompositorWindow;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QOpenGLCompositorWindow12sourceWindowEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QOpenGLCompositorWindow8texturesEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QOpenGLCompositorWindow16beginCompositingEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QOpenGLCompositorWindow14endCompositingEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QOpenGLCompositorWindow15setBackingStoreEP29QOpenGLCompositorBackingStore")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QOpenGLCompositorWindow12backingStoreEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QWindow *QOpenGLCompositorWindow::sourceWindow() const
  QWindow *sourceWindow() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall0 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return {};
  }

  //  const QPlatformTextureList *QOpenGLCompositorWindow::textures() const
  const QPlatformTextureList *textures() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall1 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QPlatformTextureList *>(given);
    }
    return {};
  }

  //  void QOpenGLCompositorWindow::beginCompositing()
  void beginCompositing() override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall2 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLCompositorWindow::beginCompositing();
  }

  //  void QOpenGLCompositorWindow::endCompositing()
  void endCompositing() override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall3 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QOpenGLCompositorWindow::endCompositing();
  }

  //  void QOpenGLCompositorWindow::setBackingStore(QOpenGLCompositorBackin
  //      gStore *backingStore)
  void setBackingStore(
      QOpenGLCompositorBackingStore *backingStore) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall4 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall4>(taken[4]);
      call(this, backingStore, &handled);
      if (handled) return;
    }
  }

  //  QOpenGLCompositorBackingStore
  //      *QOpenGLCompositorWindow::backingStore() const
  QOpenGLCompositorBackingStore *backingStore() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLCompositorWindowCall5 call = reinterpret_cast<CuteQOpenGLCompositorWindowCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QOpenGLCompositorBackingStore *>(given);
    }
    return {};
  }
};

//  QOpenGLCompositorWindow::~QOpenGLCompositorWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLCompositorWindowD1Ev(QOpenGLCompositorWindow *self) {
  delete self;
}

//  QWindow *QOpenGLCompositorWindow::sourceWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK23QOpenGLCompositorWindow12sourceWindowEv(
    const QOpenGLCompositorWindow *self) {
  return self->sourceWindow();
}

//  const QPlatformTextureList *QOpenGLCompositorWindow::textures() const
extern "C" Q_DECL_EXPORT
const QPlatformTextureList *ritual_ZNK23QOpenGLCompositorWindow8texturesEv(
    const QOpenGLCompositorWindow *self) {
  return self->textures();
}

//  void QOpenGLCompositorWindow::beginCompositing()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLCompositorWindow16beginCompositingEv(
    QOpenGLCompositorWindow *self) {
  self->beginCompositing();
}

//  void QOpenGLCompositorWindow::endCompositing()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLCompositorWindow14endCompositingEv(
    QOpenGLCompositorWindow *self) {
  self->endCompositing();
}

//  void
//      QOpenGLCompositorWindow::setBackingStore(QOpenGLCompositorBackingStor
//      e *backingStore)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOpenGLCompositorWindow15setBackingStoreEP29QOpenGLCompositorBackingStore(
    QOpenGLCompositorWindow *self,
    QOpenGLCompositorBackingStore *backingStore) {
  self->setBackingStore(backingStore);
}

//  QOpenGLCompositorBackingStore *QOpenGLCompositorWindow::backingStore()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLCompositorBackingStore *ritual_ZNK23QOpenGLCompositorWindow12backingStoreEv(
    const QOpenGLCompositorWindow *self) {
  return self->backingStore();
}

//  a Python function taken by a CuteQOpenGLCompositorWindow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLCompositorWindow(
    QOpenGLCompositorWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLCompositorWindow *>(self)->take(key, call);
}

//  void QOpenGLCompositorWindow::beginCompositing()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QOpenGLCompositorWindow16beginCompositingEv(
    QOpenGLCompositorWindow *self) {
  self->QOpenGLCompositorWindow::beginCompositing();
}

//  void QOpenGLCompositorWindow::endCompositing()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QOpenGLCompositorWindow14endCompositingEv(
    QOpenGLCompositorWindow *self) {
  self->QOpenGLCompositorWindow::endCompositing();
}

//  QList<QOpenGLCompositorWindow *>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpenGLCompositorWindow *> *ritual_list_make_QOpenGLCompositorWindow_ptr() {
  return new QList<QOpenGLCompositorWindow *>();
}

//  void QList<QOpenGLCompositorWindow *>::append(const
//      QOpenGLCompositorWindow * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpenGLCompositorWindow_ptr(
    QList<QOpenGLCompositorWindow *> *self,
    QOpenGLCompositorWindow *element) {
  self->append(element);
}

//  qsizetype QList<QOpenGLCompositorWindow *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpenGLCompositorWindow_ptr(
    const QList<QOpenGLCompositorWindow *> *self) {
  return self->size();
}

//  const QOpenGLCompositorWindow * &QList<QOpenGLCompositorWindow
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpenGLCompositorWindow *ritual_list_at_QOpenGLCompositorWindow_ptr(
    const QList<QOpenGLCompositorWindow *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QOpenGLCompositorWindow *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpenGLCompositorWindow_ptr(
    QList<QOpenGLCompositorWindow *> *self) {
  delete self;
}
