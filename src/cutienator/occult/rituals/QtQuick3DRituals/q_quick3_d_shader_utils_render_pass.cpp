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
#include <QtQml/QQmlListProperty>

//  A QQuick3DShaderUtilsRenderPass that Python can take functions over in. Every QQuick3DShaderUtilsRenderPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsRenderPassCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall1)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall3)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsRenderPass : public QQuick3DShaderUtilsRenderPass {
public:
  using QQuick3DShaderUtilsRenderPass::QQuick3DShaderUtilsRenderPass;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsRenderPass::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DShaderUtilsRenderPass10metaObjectEv(
    const QQuick3DShaderUtilsRenderPass *self) {
  return self->metaObject();
}

//  void *QQuick3DShaderUtilsRenderPass::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuick3DShaderUtilsRenderPass11qt_metacastEPKc(
    QQuick3DShaderUtilsRenderPass *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DShaderUtilsRenderPass::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuick3DShaderUtilsRenderPass11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DShaderUtilsRenderPass *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DShaderUtilsRenderPass::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuick3DShaderUtilsRenderPass2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsRenderPass::tr(s, c, n));
}

//  QQuick3DShaderUtilsRenderPass::QQuick3DShaderUtilsRenderPass()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPass *ritual_ZN29QQuick3DShaderUtilsRenderPassC1Ev() {
  return new CuteQQuick3DShaderUtilsRenderPass();
}

//  QQuick3DShaderUtilsRenderPass::~QQuick3DShaderUtilsRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPassD1Ev(
    QQuick3DShaderUtilsRenderPass *self) {
  delete self;
}

//  void QQuick3DShaderUtilsRenderPass::qmlAppendCommand(QQmlListProperty<QQu
//      ick3DShaderUtilsRenderCommand> *list,
//      QQuick3DShaderUtilsRenderCommand *command)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPass16qmlAppendCommandEP16QQmlListPropertyI32QQuick3DShaderUtilsRenderCommandEPS1_(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    QQuick3DShaderUtilsRenderCommand *command) {
  QQuick3DShaderUtilsRenderPass::qmlAppendCommand(list, command);
}

//  QQuick3DShaderUtilsRenderCommand *QQuick3DShaderUtilsRenderPass::qmlComma
//      ndAt(QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderCommand *ritual_ZN29QQuick3DShaderUtilsRenderPass12qmlCommandAtEP16QQmlListPropertyI32QQuick3DShaderUtilsRenderCommandEx(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    qsizetype index) {
  return QQuick3DShaderUtilsRenderPass::qmlCommandAt(list, index);
}

//  qsizetype QQuick3DShaderUtilsRenderPass::qmlCommandCount(QQmlListProperty
//      <QQuick3DShaderUtilsRenderCommand> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN29QQuick3DShaderUtilsRenderPass15qmlCommandCountEP16QQmlListPropertyI32QQuick3DShaderUtilsRenderCommandE(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list) {
  return QQuick3DShaderUtilsRenderPass::qmlCommandCount(list);
}

//  void QQuick3DShaderUtilsRenderPass::qmlCommandClear(QQmlListProperty<QQui
//      ck3DShaderUtilsRenderCommand> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPass15qmlCommandClearEP16QQmlListPropertyI32QQuick3DShaderUtilsRenderCommandE(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list) {
  QQuick3DShaderUtilsRenderPass::qmlCommandClear(list);
}

//  void QQuick3DShaderUtilsRenderPass::qmlAppendShader(QQmlListProperty<QQui
//      ck3DShaderUtilsShader> *list, QQuick3DShaderUtilsShader *shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPass15qmlAppendShaderEP16QQmlListPropertyI25QQuick3DShaderUtilsShaderEPS1_(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list,
    QQuick3DShaderUtilsShader *shader) {
  QQuick3DShaderUtilsRenderPass::qmlAppendShader(list, shader);
}

//  QQuick3DShaderUtilsShader *QQuick3DShaderUtilsRenderPass::qmlShaderAt(QQm
//      lListProperty<QQuick3DShaderUtilsShader> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsShader *ritual_ZN29QQuick3DShaderUtilsRenderPass11qmlShaderAtEP16QQmlListPropertyI25QQuick3DShaderUtilsShaderEx(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list,
    qsizetype index) {
  return QQuick3DShaderUtilsRenderPass::qmlShaderAt(list, index);
}

//  qsizetype QQuick3DShaderUtilsRenderPass::qmlShaderCount(QQmlListProperty<
//      QQuick3DShaderUtilsShader> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN29QQuick3DShaderUtilsRenderPass14qmlShaderCountEP16QQmlListPropertyI25QQuick3DShaderUtilsShaderE(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list) {
  return QQuick3DShaderUtilsRenderPass::qmlShaderCount(list);
}

//  void QQuick3DShaderUtilsRenderPass::qmlShaderClear(QQmlListProperty<QQuic
//      k3DShaderUtilsShader> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPass14qmlShaderClearEP16QQmlListPropertyI25QQuick3DShaderUtilsShaderE(
    QQmlListProperty<QQuick3DShaderUtilsShader> *list) {
  QQuick3DShaderUtilsRenderPass::qmlShaderClear(list);
}

//  QQmlListProperty<QQuick3DShaderUtilsRenderCommand>
//      QQuick3DShaderUtilsRenderPass::commands()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *ritual_ZN29QQuick3DShaderUtilsRenderPass8commandsEv(
    QQuick3DShaderUtilsRenderPass *self) {
  return new QQmlListProperty<QQuick3DShaderUtilsRenderCommand>(
      self->commands());
}

//  QQmlListProperty<QQuick3DShaderUtilsShader>
//      QQuick3DShaderUtilsRenderPass::shaders()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DShaderUtilsShader> *ritual_ZN29QQuick3DShaderUtilsRenderPass7shadersEv(
    QQuick3DShaderUtilsRenderPass *self) {
  return new QQmlListProperty<QQuick3DShaderUtilsShader>(self->shaders());
}

//  void QQuick3DShaderUtilsRenderPass::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DShaderUtilsRenderPass7changedEv(
    QQuick3DShaderUtilsRenderPass *self) {
  self->changed();
}

//  a Python function taken by a CuteQQuick3DShaderUtilsRenderPass, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsRenderPass(
    QQuick3DShaderUtilsRenderPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsRenderPass *>(self)->take(key, call);
}

//  a QQmlListProperty<QQuick3DShaderUtilsRenderCommand> a ritual of
//      QQuick3DShaderUtilsRenderPass gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DShaderUtilsRenderPass__QQmlListProperty_QQuick3DShaderUtilsRenderCommand(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *self) {
  delete self;
}

//  a QQmlListProperty<QQuick3DShaderUtilsShader> a ritual of
//      QQuick3DShaderUtilsRenderPass gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DShaderUtilsRenderPass__QQmlListProperty_QQuick3DShaderUtilsShader(
    QQmlListProperty<QQuick3DShaderUtilsShader> *self) {
  delete self;
}
