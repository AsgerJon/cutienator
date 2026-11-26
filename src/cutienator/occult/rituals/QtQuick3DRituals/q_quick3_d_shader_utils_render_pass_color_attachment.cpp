//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DShaderUtilsRenderPassColorAttachment that Python can take functions over in. Every QQuick3DShaderUtilsRenderPassColorAttachment
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall0)(const void *, int *);
typedef int (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall1)(const void *, int *);
typedef void * (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall2)(const void *, int, int *);
typedef void * (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall3)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall6)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall7)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsRenderPassColorAttachment : public QQuick3DShaderUtilsRenderPassColorAttachment {
public:
  using QQuick3DShaderUtilsRenderPassColorAttachment::QQuick3DShaderUtilsRenderPassColorAttachment;
  void *taken[16] = {};

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
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGCommand
  //      *QQuick3DShaderUtilsRenderPassColorAttachment::cloneCommand()
  QSSGCommand *cloneCommand() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSSGCommand *>(given);
    }
    return QQuick3DShaderUtilsRenderPassColorAttachment::cloneCommand();
  }

  //  int QQuick3DShaderUtilsRenderCommand::bufferCount() const
  int bufferCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall1>(taken[1]);
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
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall2>(taken[2]);
      void * given = call(this, idx, &handled);
      if (handled) return static_cast<QQuick3DShaderUtilsBuffer *>(given);
    }
    return QQuick3DShaderUtilsRenderCommand::bufferAt(idx);
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall3>(taken[3]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall13 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall14 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall15 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachmentCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QQuick3DShaderUtilsRenderPassColorAttachment::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK44QQuick3DShaderUtilsRenderPassColorAttachment10metaObjectEv(
    const QQuick3DShaderUtilsRenderPassColorAttachment *self) {
  return self->metaObject();
}

//  void *QQuick3DShaderUtilsRenderPassColorAttachment::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachment11qt_metacastEPKc(
    QQuick3DShaderUtilsRenderPassColorAttachment *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DShaderUtilsRenderPassColorAttachment::qt_metacall(QMetaObject
//      ::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachment11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DShaderUtilsRenderPassColorAttachment *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DShaderUtilsRenderPassColorAttachment::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachment2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QQuick3DShaderUtilsRenderPassColorAttachment::tr(
          s,
          c,
          n));
}

//  QQuick3DShaderUtilsRenderPassColorAttachment::QQuick3DShaderUtilsRenderPa
//      ssColorAttachment()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPassColorAttachment *ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachmentC1Ev() {
  return new CuteQQuick3DShaderUtilsRenderPassColorAttachment();
}

//  QQuick3DShaderUtilsRenderPassColorAttachment::~QQuick3DShaderUtilsRenderP
//      assColorAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachmentD1Ev(
    QQuick3DShaderUtilsRenderPassColorAttachment *self) {
  delete self;
}

//  QByteArray QQuick3DShaderUtilsRenderPassColorAttachment::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK44QQuick3DShaderUtilsRenderPassColorAttachment4nameEv(
    const QQuick3DShaderUtilsRenderPassColorAttachment *self) {
  return new QByteArray(self->name());
}

//  void QQuick3DShaderUtilsRenderPassColorAttachment::setName(const
//      QByteArray &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachment7setNameERK10QByteArray(
    QQuick3DShaderUtilsRenderPassColorAttachment *self,
    const QByteArray *newName) {
  self->setName(*newName);
}

//  QSSGCommand *QQuick3DShaderUtilsRenderPassColorAttachment::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN44QQuick3DShaderUtilsRenderPassColorAttachment12cloneCommandEv(
    QQuick3DShaderUtilsRenderPassColorAttachment *self) {
  return self->cloneCommand();
}

//  a Python function taken by a
//      CuteQQuick3DShaderUtilsRenderPassColorAttachment, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsRenderPassColorAttachment(
    QQuick3DShaderUtilsRenderPassColorAttachment *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsRenderPassColorAttachment *>(self)->take(key, call);
}

//  QSSGCommand *QQuick3DShaderUtilsRenderPassColorAttachment::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_own_ZN44QQuick3DShaderUtilsRenderPassColorAttachment12cloneCommandEv(
    QQuick3DShaderUtilsRenderPassColorAttachment *self) {
  return self->QQuick3DShaderUtilsRenderPassColorAttachment::cloneCommand();
}
