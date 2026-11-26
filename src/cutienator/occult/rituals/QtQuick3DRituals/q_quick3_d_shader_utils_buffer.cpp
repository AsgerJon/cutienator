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

//  A QQuick3DShaderUtilsBuffer that Python can take functions over in. Every QQuick3DShaderUtilsBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsBufferCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsBufferCall1)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsBufferCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsBufferCall3)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsBufferCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsBufferCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsBufferCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsBufferCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsBufferCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsBufferCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsBufferCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsBufferCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsBufferCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsBuffer : public QQuick3DShaderUtilsBuffer {
public:
  using QQuick3DShaderUtilsBuffer::QQuick3DShaderUtilsBuffer;
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
      CuteQQuick3DShaderUtilsBufferCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsBufferCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall1>(taken[1]);
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
      CuteQQuick3DShaderUtilsBufferCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsBufferCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsBufferCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsBufferCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall5>(taken[5]);
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
      CuteQQuick3DShaderUtilsBufferCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall6>(taken[6]);
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
      CuteQQuick3DShaderUtilsBufferCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall7>(taken[7]);
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
      CuteQQuick3DShaderUtilsBufferCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall8>(taken[8]);
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
      CuteQQuick3DShaderUtilsBufferCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall9>(taken[9]);
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
      CuteQQuick3DShaderUtilsBufferCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall10>(taken[10]);
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
      CuteQQuick3DShaderUtilsBufferCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall11>(taken[11]);
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
      CuteQQuick3DShaderUtilsBufferCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsBufferCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsBuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuick3DShaderUtilsBuffer10metaObjectEv(
    const QQuick3DShaderUtilsBuffer *self) {
  return self->metaObject();
}

//  void *QQuick3DShaderUtilsBuffer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuick3DShaderUtilsBuffer11qt_metacastEPKc(
    QQuick3DShaderUtilsBuffer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DShaderUtilsBuffer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuick3DShaderUtilsBuffer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DShaderUtilsBuffer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DShaderUtilsBuffer::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuick3DShaderUtilsBuffer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsBuffer::tr(s, c, n));
}

//  QQuick3DShaderUtilsBuffer::QQuick3DShaderUtilsBuffer()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer *ritual_ZN25QQuick3DShaderUtilsBufferC1Ev() {
  return new CuteQQuick3DShaderUtilsBuffer();
}

//  QQuick3DShaderUtilsBuffer::~QQuick3DShaderUtilsBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBufferD1Ev(
    QQuick3DShaderUtilsBuffer *self) {
  delete self;
}

//  TextureFilterOperation
//      QQuick3DShaderUtilsBuffer::textureFilterOperation() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer::TextureFilterOperation ritual_ZNK25QQuick3DShaderUtilsBuffer22textureFilterOperationEv(
    const QQuick3DShaderUtilsBuffer *self) {
  return self->textureFilterOperation();
}

//  void QQuick3DShaderUtilsBuffer::setTextureFilterOperation(TextureFilterOp
//      eration op)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBuffer25setTextureFilterOperationENS_22TextureFilterOperationE(
    QQuick3DShaderUtilsBuffer *self,
    QQuick3DShaderUtilsBuffer::TextureFilterOperation op) {
  self->setTextureFilterOperation(op);
}

//  TextureCoordOperation QQuick3DShaderUtilsBuffer::textureCoordOperation()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer::TextureCoordOperation ritual_ZNK25QQuick3DShaderUtilsBuffer21textureCoordOperationEv(
    const QQuick3DShaderUtilsBuffer *self) {
  return self->textureCoordOperation();
}

//  void
//      QQuick3DShaderUtilsBuffer::setTextureCoordOperation(TextureCoordOpera
//      tion texCoordOp)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBuffer24setTextureCoordOperationENS_21TextureCoordOperationE(
    QQuick3DShaderUtilsBuffer *self,
    QQuick3DShaderUtilsBuffer::TextureCoordOperation texCoordOp) {
  self->setTextureCoordOperation(texCoordOp);
}

//  QSSGCommand *QQuick3DShaderUtilsBuffer::cloneCommand()
extern "C" Q_DECL_EXPORT
QSSGCommand *ritual_ZN25QQuick3DShaderUtilsBuffer12cloneCommandEv(
    QQuick3DShaderUtilsBuffer *self) {
  return self->cloneCommand();
}

//  TextureFormat QQuick3DShaderUtilsBuffer::format() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer::TextureFormat ritual_ZNK25QQuick3DShaderUtilsBuffer6formatEv(
    const QQuick3DShaderUtilsBuffer *self) {
  return self->format();
}

//  void QQuick3DShaderUtilsBuffer::setFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBuffer9setFormatENS_13TextureFormatE(
    QQuick3DShaderUtilsBuffer *self,
    QQuick3DShaderUtilsBuffer::TextureFormat format) {
  self->setFormat(format);
}

//  AllocateBufferFlagValues QQuick3DShaderUtilsBuffer::bufferFlags() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer::AllocateBufferFlagValues ritual_ZNK25QQuick3DShaderUtilsBuffer11bufferFlagsEv(
    const QQuick3DShaderUtilsBuffer *self) {
  return self->bufferFlags();
}

//  void QQuick3DShaderUtilsBuffer::setBufferFlags(AllocateBufferFlagValues
//      flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBuffer14setBufferFlagsENS_24AllocateBufferFlagValuesE(
    QQuick3DShaderUtilsBuffer *self,
    QQuick3DShaderUtilsBuffer::AllocateBufferFlagValues flag) {
  self->setBufferFlags(flag);
}

//  QSSGRenderTextureFormat::Format QQuick3DShaderUtilsBuffer::mapTextureForm
//      at(QQuick3DShaderUtilsBuffer::TextureFormat fmt)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat::Format ritual_ZN25QQuick3DShaderUtilsBuffer16mapTextureFormatENS_13TextureFormatE(
    QQuick3DShaderUtilsBuffer::TextureFormat fmt) {
  return QQuick3DShaderUtilsBuffer::mapTextureFormat(fmt);
}

//  QQuick3DShaderUtilsBuffer::TextureFormat QQuick3DShaderUtilsBuffer::mapRe
//      nderTextureFormat(QSSGRenderTextureFormat::Format fmt)
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsBuffer::TextureFormat ritual_ZN25QQuick3DShaderUtilsBuffer22mapRenderTextureFormatEN23QSSGRenderTextureFormat6FormatE(
    QSSGRenderTextureFormat::Format fmt) {
  return QQuick3DShaderUtilsBuffer::mapRenderTextureFormat(fmt);
}

//  void QQuick3DShaderUtilsBuffer::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DShaderUtilsBuffer7changedEv(
    QQuick3DShaderUtilsBuffer *self) {
  self->changed();
}

//  a Python function taken by a CuteQQuick3DShaderUtilsBuffer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsBuffer(
    QQuick3DShaderUtilsBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsBuffer *>(self)->take(key, call);
}
