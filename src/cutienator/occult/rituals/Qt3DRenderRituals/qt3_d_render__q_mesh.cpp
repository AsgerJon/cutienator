//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qmesh.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qmesh.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QMesh that Python can take functions over in. Every Qt3DRender::QMesh
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMeshCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMeshCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMeshCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMeshCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMeshCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMeshCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMeshCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QMesh : public Qt3DRender::QMesh {
public:
  using Qt3DRender::QMesh::QMesh;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall0 call = reinterpret_cast<CuteQt3DRender_QMeshCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall1 call = reinterpret_cast<CuteQt3DRender_QMeshCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall2 call = reinterpret_cast<CuteQt3DRender_QMeshCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall3 call = reinterpret_cast<CuteQt3DRender_QMeshCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall4 call = reinterpret_cast<CuteQt3DRender_QMeshCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall5 call = reinterpret_cast<CuteQt3DRender_QMeshCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_QMeshCall6 call = reinterpret_cast<CuteQt3DRender_QMeshCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender5QMesh10metaObjectEv(
    const Qt3DRender::QMesh *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender5QMesh11qt_metacastEPKc(
    Qt3DRender::QMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QMesh::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender5QMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender5QMesh2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QMesh::tr(s, c, n));
}

//  Qt3DRender::QMesh::QMesh(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMesh *ritual_ZN10Qt3DRender5QMeshC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMesh(parent);
}

//  Qt3DRender::QMesh::~QMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMeshD1Ev(Qt3DRender::QMesh *self) {
  delete self;
}

//  QUrl Qt3DRender::QMesh::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender5QMesh6sourceEv(const Qt3DRender::QMesh *self) {
  return new QUrl(self->source());
}

//  QString Qt3DRender::QMesh::meshName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender5QMesh8meshNameEv(
    const Qt3DRender::QMesh *self) {
  return new QString(self->meshName());
}

//  Status Qt3DRender::QMesh::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QMesh::Status ritual_ZNK10Qt3DRender5QMesh6statusEv(
    const Qt3DRender::QMesh *self) {
  return self->status();
}

//  void Qt3DRender::QMesh::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMesh9setSourceERK4QUrl(
    Qt3DRender::QMesh *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void Qt3DRender::QMesh::setMeshName(const QString &meshName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMesh11setMeshNameERK7QString(
    Qt3DRender::QMesh *self,
    const QString *meshName) {
  self->setMeshName(*meshName);
}

//  void Qt3DRender::QMesh::sourceChanged(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMesh13sourceChangedERK4QUrl(
    Qt3DRender::QMesh *self,
    const QUrl *source) {
  self->sourceChanged(*source);
}

//  void Qt3DRender::QMesh::meshNameChanged(const QString &meshName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMesh15meshNameChangedERK7QString(
    Qt3DRender::QMesh *self,
    const QString *meshName) {
  self->meshNameChanged(*meshName);
}

//  void Qt3DRender::QMesh::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5QMesh13statusChangedENS0_6StatusE(
    Qt3DRender::QMesh *self,
    Qt3DRender::QMesh::Status status) {
  self->statusChanged(status);
}

//  Qt3DRender::QMesh::QMesh(QMeshPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMesh *ritual_ZN10Qt3DRender5QMeshC1ERNS_12QMeshPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QMeshPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMesh(*dd, parent);
}

//  QMeshPrivate *Qt3DRender::QMesh::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMeshPrivate *ritual_ZN10Qt3DRender5QMesh6d_funcEv(
    Qt3DRender::QMesh *self) {
  return self->d_func();
}

//  const QMeshPrivate *Qt3DRender::QMesh::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QMeshPrivate *ritual_ZNK10Qt3DRender5QMesh6d_funcEv(
    const Qt3DRender::QMesh *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QMesh, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QMesh(
    Qt3DRender::QMesh *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QMesh *>(self)->take(key, call);
}
