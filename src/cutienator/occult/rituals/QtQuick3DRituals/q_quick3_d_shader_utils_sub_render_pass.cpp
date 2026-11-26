//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DShaderUtilsSubRenderPass that Python can take functions over in. Every QQuick3DShaderUtilsSubRenderPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsSubRenderPassCall0)(const void *, int *);
typedef int (*CuteQQuick3DShaderUtilsSubRenderPassCall1)(const void *, int *);
typedef void * (*CuteQQuick3DShaderUtilsSubRenderPassCall2)(const void *, int, int *);
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall3)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall5)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsSubRenderPassCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsSubRenderPassCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsSubRenderPassCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsSubRenderPass : public QQuick3DShaderUtilsSubRenderPass {
public:
  using QQuick3DShaderUtilsSubRenderPass::QQuick3DShaderUtilsSubRenderPass;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QQuick3DShaderUtilsRenderCommand12cloneCommandEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QQuick3DShaderUtilsRenderCommand11bufferCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QQuick3DShaderUtilsRenderCommand8bufferAtEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGCommand *QQuick3DShaderUtilsSubRenderPass::cloneCommand()
  QSSGCommand *cloneCommand() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSSGCommand *>(given);
    }
    return QQuick3DShaderUtilsSubRenderPass::cloneCommand();
  }

  //  int QQuick3DShaderUtilsRenderCommand::bufferCount() const
  int bufferCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DShaderUtilsRenderCommand::bufferCount();
  }

  //  QQuick3DShaderUtilsBuffer
  //      *QQuick3DShaderUtilsRenderCommand::bufferAt(int idx) const
  QQuick3DShaderUtilsBuffer *bufferAt(int idx) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall2>(taken[2]);
      void * given = call(this, idx, &handled);
      if (handled) return static_cast<QQuick3DShaderUtilsBuffer *>(given);
    }
    return QQuick3DShaderUtilsRenderCommand::bufferAt(idx);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsSubRenderPassCall13 call = reinterpret_cast<CuteQQuick3DShaderUtilsSubRenderPassCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsSubRenderPass::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuick3DShaderUtilsSubRenderPass10metaObjectEv(
    const QQuick3DShaderUtilsSubRenderPass *self) {
  return self->metaObject();
}

//  void *QQuick3DShaderUtilsSubRenderPass::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuick3DShaderUtilsSubRenderPass11qt_metacastEPKc(
    QQuick3DShaderUtilsSubRenderPass *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DShaderUtilsSubRenderPass::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuick3DShaderUtilsSubRenderPass11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DShaderUtilsSubRenderPass *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DShaderUtilsSubRenderPass::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuick3DShaderUtilsSubRenderPass2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsSubRenderPass::tr(s, c, n));
}

//  QQuick3DShaderUtilsSubRenderPass::QQuick3DShaderUtilsSubRenderPass()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsSubRenderPass *ritual_ZN32QQuick3DShaderUtilsSubRenderPassC1Ev() {
  return new CuteQQuick3DShaderUtilsSubRenderPass();
}

//  QQuick3DShaderUtilsSubRenderPass::~QQuick3DShaderUtilsSubRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DShaderUtilsSubRenderPassD1Ev(
    QQuick3DShaderUtilsSubRenderPass *self) {
  delete self;
}

//  QQuick3DRenderPass *QQuick3DShaderUtilsSubRenderPass::renderPass() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPass *ritual_ZNK32QQuick3DShaderUtilsSubRenderPass10renderPassEv(
    const QQuick3DShaderUtilsSubRenderPass *self) {
  return self->renderPass();
}

//  void QQuick3DShaderUtilsSubRenderPass::setRenderPass(QQuick3DRenderPass
//      *newRenderPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DShaderUtilsSubRenderPass13setRenderPassEP18QQuick3DRenderPass(
    QQuick3DShaderUtilsSubRenderPass *self,
    QQuick3DRenderPass *newRenderPass) {
  self->setRenderPass(newRenderPass);
}

//  QSSGCommand *QQuick3DShaderUtilsSubRenderPass::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN32QQuick3DShaderUtilsSubRenderPass12cloneCommandEv(
    QQuick3DShaderUtilsSubRenderPass *self) {
  return self->cloneCommand();
}

//  void QQuick3DShaderUtilsSubRenderPass::renderPassChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DShaderUtilsSubRenderPass17renderPassChangedEv(
    QQuick3DShaderUtilsSubRenderPass *self) {
  self->renderPassChanged();
}

//  QSSGRenderGraphObject *QQuick3DShaderUtilsSubRenderPass::updateSpatialNod
//      e(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN32QQuick3DShaderUtilsSubRenderPass17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DShaderUtilsSubRenderPass *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DShaderUtilsSubRenderPass::itemChange(ItemChange change,
//      const ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DShaderUtilsSubRenderPass10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DShaderUtilsSubRenderPass *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void
//      QQuick3DShaderUtilsSubRenderPass::updateSceneManager(QQuick3DSceneMan
//      ager *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuick3DShaderUtilsSubRenderPass18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DShaderUtilsSubRenderPass *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  a Python function taken by a CuteQQuick3DShaderUtilsSubRenderPass, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsSubRenderPass(
    QQuick3DShaderUtilsSubRenderPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsSubRenderPass *>(self)->take(key, call);
}

//  QSSGCommand *QQuick3DShaderUtilsSubRenderPass::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_own_ZN32QQuick3DShaderUtilsSubRenderPass12cloneCommandEv(
    QQuick3DShaderUtilsSubRenderPass *self) {
  return self->QQuick3DShaderUtilsSubRenderPass::cloneCommand();
}
