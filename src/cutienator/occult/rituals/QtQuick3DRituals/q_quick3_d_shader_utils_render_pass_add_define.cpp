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

//  A QQuick3DShaderUtilsRenderPassAddDefine that Python can take functions over in. Every QQuick3DShaderUtilsRenderPassAddDefine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall0)(const void *, int *);
typedef int (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall1)(const void *, int *);
typedef void * (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall2)(const void *, int, int *);
typedef void * (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall3)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall6)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall7)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassAddDefineCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsRenderPassAddDefine : public QQuick3DShaderUtilsRenderPassAddDefine {
public:
  using QQuick3DShaderUtilsRenderPassAddDefine::QQuick3DShaderUtilsRenderPassAddDefine;
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

  //  QSSGCommand *QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand()
  QSSGCommand *cloneCommand() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSSGCommand *>(given);
    }
    return QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand();
  }

  //  int QQuick3DShaderUtilsRenderCommand::bufferCount() const
  int bufferCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall1>(taken[1]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall2>(taken[2]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall3>(taken[3]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall4>(taken[4]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall8>(taken[8]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall9>(taken[9]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall10>(taken[10]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall11>(taken[11]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall12>(taken[12]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall13 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall13>(taken[13]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall14 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall14>(taken[14]);
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
      CuteQQuick3DShaderUtilsRenderPassAddDefineCall15 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassAddDefineCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsRenderPassAddDefine::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine10metaObjectEv(
    const QQuick3DShaderUtilsRenderPassAddDefine *self) {
  return self->metaObject();
}

//  QString QQuick3DShaderUtilsRenderPassAddDefine::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsRenderPassAddDefine::tr(s, c, n));
}

//  QQuick3DShaderUtilsRenderPassAddDefine::QQuick3DShaderUtilsRenderPassAddD
//      efine()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPassAddDefine *ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefineC1Ev() {
  return new CuteQQuick3DShaderUtilsRenderPassAddDefine();
}

//  QQuick3DShaderUtilsRenderPassAddDefine::~QQuick3DShaderUtilsRenderPassAdd
//      Define()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefineD1Ev(
    QQuick3DShaderUtilsRenderPassAddDefine *self) {
  delete self;
}

//  QSSGCommand *QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine12cloneCommandEv(
    QQuick3DShaderUtilsRenderPassAddDefine *self) {
  return self->cloneCommand();
}

//  QByteArray QQuick3DShaderUtilsRenderPassAddDefine::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine4nameEv(
    const QQuick3DShaderUtilsRenderPassAddDefine *self) {
  return new QByteArray(self->name());
}

//  void QQuick3DShaderUtilsRenderPassAddDefine::setName(const QByteArray
//      &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine7setNameERK10QByteArray(
    QQuick3DShaderUtilsRenderPassAddDefine *self,
    const QByteArray *newName) {
  self->setName(*newName);
}

//  int QQuick3DShaderUtilsRenderPassAddDefine::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK38QQuick3DShaderUtilsRenderPassAddDefine5valueEv(
    const QQuick3DShaderUtilsRenderPassAddDefine *self) {
  return self->value();
}

//  void QQuick3DShaderUtilsRenderPassAddDefine::setValue(int newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuick3DShaderUtilsRenderPassAddDefine8setValueEi(
    QQuick3DShaderUtilsRenderPassAddDefine *self,
    int newValue) {
  self->setValue(newValue);
}

//  a Python function taken by a CuteQQuick3DShaderUtilsRenderPassAddDefine,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsRenderPassAddDefine(
    QQuick3DShaderUtilsRenderPassAddDefine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsRenderPassAddDefine *>(self)->take(key, call);
}

//  QSSGCommand *QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_own_ZN38QQuick3DShaderUtilsRenderPassAddDefine12cloneCommandEv(
    QQuick3DShaderUtilsRenderPassAddDefine *self) {
  return self->QQuick3DShaderUtilsRenderPassAddDefine::cloneCommand();
}
