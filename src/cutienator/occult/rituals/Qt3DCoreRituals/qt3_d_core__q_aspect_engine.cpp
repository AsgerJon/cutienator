//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qaspectengine.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qaspectengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QList>

//  A Qt3DCore::QAspectEngine that Python can take functions over in. Every Qt3DCore::QAspectEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAspectEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAspectEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAspectEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAspectEngine : public Qt3DCore::QAspectEngine {
public:
  using Qt3DCore::QAspectEngine::QAspectEngine;
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
      CuteQt3DCore_QAspectEngineCall0 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall0>(taken[0]);
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
      CuteQt3DCore_QAspectEngineCall1 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall1>(taken[1]);
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
      CuteQt3DCore_QAspectEngineCall2 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall2>(taken[2]);
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
      CuteQt3DCore_QAspectEngineCall3 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall3>(taken[3]);
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
      CuteQt3DCore_QAspectEngineCall4 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall4>(taken[4]);
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
      CuteQt3DCore_QAspectEngineCall5 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall5>(taken[5]);
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
      CuteQt3DCore_QAspectEngineCall6 call = reinterpret_cast<CuteQt3DCore_QAspectEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAspectEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore13QAspectEngine10metaObjectEv(
    const Qt3DCore::QAspectEngine *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QAspectEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore13QAspectEngine11qt_metacastEPKc(
    Qt3DCore::QAspectEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QAspectEngine::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore13QAspectEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QAspectEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QAspectEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore13QAspectEngine2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAspectEngine::tr(s, c, n));
}

//  Qt3DCore::QAspectEngine::QAspectEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine *ritual_ZN8Qt3DCore13QAspectEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_QAspectEngine(parent);
}

//  Qt3DCore::QAspectEngine::~QAspectEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngineD1Ev(Qt3DCore::QAspectEngine *self) {
  delete self;
}

//  void Qt3DCore::QAspectEngine::setRootEntity(QEntityPtr root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine13setRootEntityE14QSharedPointerINS_7QEntityEE(
    Qt3DCore::QAspectEngine *self,
    const Qt3DCore::QEntityPtr *root) {
  self->setRootEntity(*root);
}

//  QEntityPtr Qt3DCore::QAspectEngine::rootEntity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntityPtr *ritual_ZNK8Qt3DCore13QAspectEngine10rootEntityEv(
    const Qt3DCore::QAspectEngine *self) {
  return new Qt3DCore::QEntityPtr(self->rootEntity());
}

//  void Qt3DCore::QAspectEngine::setRunMode(RunMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine10setRunModeENS0_7RunModeE(
    Qt3DCore::QAspectEngine *self,
    Qt3DCore::QAspectEngine::RunMode mode) {
  self->setRunMode(mode);
}

//  RunMode Qt3DCore::QAspectEngine::runMode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine::RunMode ritual_ZNK8Qt3DCore13QAspectEngine7runModeEv(
    const Qt3DCore::QAspectEngine *self) {
  return self->runMode();
}

//  void Qt3DCore::QAspectEngine::registerAspect(QAbstractAspect *aspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine14registerAspectEPNS_15QAbstractAspectE(
    Qt3DCore::QAspectEngine *self,
    Qt3DCore::QAbstractAspect *aspect) {
  self->registerAspect(aspect);
}

//  void Qt3DCore::QAspectEngine::registerAspect(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine14registerAspectERK7QString(
    Qt3DCore::QAspectEngine *self,
    const QString *name) {
  self->registerAspect(*name);
}

//  void Qt3DCore::QAspectEngine::unregisterAspect(QAbstractAspect *aspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine16unregisterAspectEPNS_15QAbstractAspectE(
    Qt3DCore::QAspectEngine *self,
    Qt3DCore::QAbstractAspect *aspect) {
  self->unregisterAspect(aspect);
}

//  void Qt3DCore::QAspectEngine::unregisterAspect(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine16unregisterAspectERK7QString(
    Qt3DCore::QAspectEngine *self,
    const QString *name) {
  self->unregisterAspect(*name);
}

//  QList<QAbstractAspect *> Qt3DCore::QAspectEngine::aspects() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QAbstractAspect *> *ritual_ZNK8Qt3DCore13QAspectEngine7aspectsEv(
    const Qt3DCore::QAspectEngine *self) {
  return new QList<Qt3DCore::QAbstractAspect *>(self->aspects());
}

//  QAbstractAspect *Qt3DCore::QAspectEngine::aspect(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspect *ritual_ZNK8Qt3DCore13QAspectEngine6aspectERK7QString(
    const Qt3DCore::QAspectEngine *self,
    const QString *name) {
  return self->aspect(*name);
}

//  QVariant Qt3DCore::QAspectEngine::executeCommand(const QString &command)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore13QAspectEngine14executeCommandERK7QString(
    Qt3DCore::QAspectEngine *self,
    const QString *command) {
  return new QVariant(self->executeCommand(*command));
}

//  void Qt3DCore::QAspectEngine::processFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore13QAspectEngine12processFrameEv(
    Qt3DCore::QAspectEngine *self) {
  self->processFrame();
}

//  QNode *Qt3DCore::QAspectEngine::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore13QAspectEngine10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QAspectEngine *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  QList<QNode *> Qt3DCore::QAspectEngine::lookupNodes(const QList<QNodeId>
//      &ids) const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNode *> *ritual_ZNK8Qt3DCore13QAspectEngine11lookupNodesERK5QListINS_7QNodeIdEE(
    const Qt3DCore::QAspectEngine *self,
    const QList<Qt3DCore::QNodeId> *ids) {
  return new QList<Qt3DCore::QNode *>(self->lookupNodes(*ids));
}

//  QAspectEnginePrivate *Qt3DCore::QAspectEngine::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEnginePrivate *ritual_ZN8Qt3DCore13QAspectEngine6d_funcEv(
    Qt3DCore::QAspectEngine *self) {
  return self->d_func();
}

//  const QAspectEnginePrivate *Qt3DCore::QAspectEngine::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAspectEnginePrivate *ritual_ZNK8Qt3DCore13QAspectEngine6d_funcEv(
    const Qt3DCore::QAspectEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QAspectEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectEngine(
    Qt3DCore::QAspectEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectEngine *>(self)->take(key, call);
}

//  a Qt3DCore::QEntityPtr a ritual of Qt3DCore::QAspectEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAspectEngine__Qt3DCore_QEntityPtr(
    Qt3DCore::QEntityPtr *self) {
  delete self;
}

//  a QList<Qt3DCore::QAbstractAspect *> a ritual of Qt3DCore::QAspectEngine
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAspectEngine__QList_Qt3DCore_QAbstractAspect(
    QList<Qt3DCore::QAbstractAspect *> *self) {
  delete self;
}

//  a QList<Qt3DCore::QNode *> a ritual of Qt3DCore::QAspectEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAspectEngine__QList_Qt3DCore_QNode(
    QList<Qt3DCore::QNode *> *self) {
  delete self;
}
