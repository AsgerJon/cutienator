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
#include <QtCore/qlist.h>
#include <cstring>

//  A QOpenGLSharedResource that Python can take functions over in. Every QOpenGLSharedResource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLSharedResourceCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQOpenGLSharedResourceCall1)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQOpenGLSharedResource : public QOpenGLSharedResource {
public:
  using QOpenGLSharedResource::QOpenGLSharedResource;
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
  //  void QOpenGLSharedResource::invalidateResource()
  void invalidateResource() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLSharedResourceCall0 call = reinterpret_cast<CuteQOpenGLSharedResourceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QOpenGLSharedResource::freeResource(QOpenGLContext *context)
  void freeResource(QOpenGLContext *context) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLSharedResourceCall1 call = reinterpret_cast<CuteQOpenGLSharedResourceCall1>(taken[1]);
      call(this, context, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QOpenGLSharedResource::~QOpenGLSharedResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLSharedResourceD1Ev(QOpenGLSharedResource *self) {
  delete self;
}

//  QOpenGLContextGroup *QOpenGLSharedResource::group() const
extern "C" Q_DECL_EXPORT
QOpenGLContextGroup *ritual_ZNK21QOpenGLSharedResource5groupEv(
    const QOpenGLSharedResource *self) {
  return self->group();
}

//  void QOpenGLSharedResource::free()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLSharedResource4freeEv(QOpenGLSharedResource *self) {
  self->free();
}

//  void QOpenGLSharedResource::invalidateResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLSharedResource18invalidateResourceEv(
    QOpenGLSharedResource *self) {
  self->invalidateResource();
}

//  void QOpenGLSharedResource::freeResource(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext(
    QOpenGLSharedResource *self,
    QOpenGLContext *context) {
  self->freeResource(context);
}

//  a Python function taken by a CuteQOpenGLSharedResource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLSharedResource(
    QOpenGLSharedResource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLSharedResource *>(self)->take(key, call);
}

//  QList<QOpenGLSharedResource *>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpenGLSharedResource *> *ritual_list_make_QOpenGLSharedResource_ptr() {
  return new QList<QOpenGLSharedResource *>();
}

//  void QList<QOpenGLSharedResource *>::append(const QOpenGLSharedResource *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpenGLSharedResource_ptr(
    QList<QOpenGLSharedResource *> *self,
    QOpenGLSharedResource *element) {
  self->append(element);
}

//  qsizetype QList<QOpenGLSharedResource *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpenGLSharedResource_ptr(
    const QList<QOpenGLSharedResource *> *self) {
  return self->size();
}

//  const QOpenGLSharedResource * &QList<QOpenGLSharedResource
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpenGLSharedResource *ritual_list_at_QOpenGLSharedResource_ptr(
    const QList<QOpenGLSharedResource *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QOpenGLSharedResource *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpenGLSharedResource_ptr(
    QList<QOpenGLSharedResource *> *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
