//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dtexturedata.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dtexturedata.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DTextureData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DTextureData : QQuick3DTextureData {
  using QQuick3DTextureData::updateSpatialNode;
  using QQuick3DTextureData::markAllDirty;
};

//  A QQuick3DTextureData that Python can take functions over in. Every QQuick3DTextureData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DTextureDataCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DTextureDataCall1)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DTextureDataCall3)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataCall4)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureDataCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DTextureData : public QQuick3DTextureData {
public:
  using QQuick3DTextureData::QQuick3DTextureData;
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
  //      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall0 call = reinterpret_cast<CuteQQuick3DTextureDataCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTextureData::updateSpatialNode(node);
  }

  //  void QQuick3DTextureData::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall1 call = reinterpret_cast<CuteQQuick3DTextureDataCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DTextureData::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall2 call = reinterpret_cast<CuteQQuick3DTextureDataCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall3 call = reinterpret_cast<CuteQQuick3DTextureDataCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall4 call = reinterpret_cast<CuteQQuick3DTextureDataCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DTextureDataCall5 call = reinterpret_cast<CuteQQuick3DTextureDataCall5>(taken[5]);
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
      CuteQQuick3DTextureDataCall6 call = reinterpret_cast<CuteQQuick3DTextureDataCall6>(taken[6]);
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
      CuteQQuick3DTextureDataCall7 call = reinterpret_cast<CuteQQuick3DTextureDataCall7>(taken[7]);
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
      CuteQQuick3DTextureDataCall8 call = reinterpret_cast<CuteQQuick3DTextureDataCall8>(taken[8]);
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
      CuteQQuick3DTextureDataCall9 call = reinterpret_cast<CuteQQuick3DTextureDataCall9>(taken[9]);
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
      CuteQQuick3DTextureDataCall10 call = reinterpret_cast<CuteQQuick3DTextureDataCall10>(taken[10]);
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
      CuteQQuick3DTextureDataCall11 call = reinterpret_cast<CuteQQuick3DTextureDataCall11>(taken[11]);
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
      CuteQQuick3DTextureDataCall12 call = reinterpret_cast<CuteQQuick3DTextureDataCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DTextureData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DTextureData10metaObjectEv(
    const QQuick3DTextureData *self) {
  return self->metaObject();
}

//  void *QQuick3DTextureData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DTextureData11qt_metacastEPKc(
    QQuick3DTextureData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DTextureData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DTextureData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DTextureData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DTextureData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DTextureData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DTextureData::tr(s, c, n));
}

//  QQuick3DTextureDataPrivate *QQuick3DTextureData::d_func()
extern "C" Q_DECL_EXPORT
QQuick3DTextureDataPrivate *ritual_ZN19QQuick3DTextureData6d_funcEv(
    QQuick3DTextureData *self) {
  return self->d_func();
}

//  const QQuick3DTextureDataPrivate *QQuick3DTextureData::d_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DTextureDataPrivate *ritual_ZNK19QQuick3DTextureData6d_funcEv(
    const QQuick3DTextureData *self) {
  return self->d_func();
}

//  void QQuick3DTextureData::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData24qt_qmlMarker_uncreatableEv(
    QQuick3DTextureData *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DTextureData::QQuick3DTextureData(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DTextureData *ritual_ZN19QQuick3DTextureDataC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DTextureData(parent);
}

//  QQuick3DTextureData::~QQuick3DTextureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureDataD1Ev(QQuick3DTextureData *self) {
  delete self;
}

//  const QByteArray QQuick3DTextureData::textureData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QQuick3DTextureData11textureDataEv(
    const QQuick3DTextureData *self) {
  return new QByteArray(self->textureData());
}

//  void QQuick3DTextureData::setTextureData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData14setTextureDataERK10QByteArray(
    QQuick3DTextureData *self,
    const QByteArray *data) {
  self->setTextureData(*data);
}

//  QSize QQuick3DTextureData::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QQuick3DTextureData4sizeEv(
    const QQuick3DTextureData *self) {
  return new QSize(self->size());
}

//  void QQuick3DTextureData::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData7setSizeERK5QSize(
    QQuick3DTextureData *self,
    const QSize *size) {
  self->setSize(*size);
}

//  int QQuick3DTextureData::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DTextureData5depthEv(
    const QQuick3DTextureData *self) {
  return self->depth();
}

//  void QQuick3DTextureData::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData8setDepthEi(
    QQuick3DTextureData *self,
    int depth) {
  self->setDepth(depth);
}

//  Format QQuick3DTextureData::format() const
extern "C" Q_DECL_EXPORT
QQuick3DTextureData::Format ritual_ZNK19QQuick3DTextureData6formatEv(
    const QQuick3DTextureData *self) {
  return self->format();
}

//  void QQuick3DTextureData::setFormat(Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData9setFormatENS_6FormatE(
    QQuick3DTextureData *self,
    QQuick3DTextureData::Format format) {
  self->setFormat(format);
}

//  bool QQuick3DTextureData::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DTextureData15hasTransparencyEv(
    const QQuick3DTextureData *self) {
  return self->hasTransparency();
}

//  void QQuick3DTextureData::setHasTransparency(bool hasTransparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData18setHasTransparencyEb(
    QQuick3DTextureData *self,
    bool hasTransparency) {
  self->setHasTransparency(hasTransparency);
}

//  void QQuick3DTextureData::textureDataNodeDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData20textureDataNodeDirtyEv(
    QQuick3DTextureData *self) {
  self->textureDataNodeDirty();
}

//  QSSGRenderGraphObject
//      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN19QQuick3DTextureData17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTextureData *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DTextureData::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DTextureData12markAllDirtyEv(
    QQuick3DTextureData *self) {
  self->markAllDirty();
}

//  a Python function taken by a CuteQQuick3DTextureData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTextureData(
    QQuick3DTextureData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTextureData *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN19QQuick3DTextureData17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DTextureData *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DTextureData *>(self)->OwnQQuick3DTextureData::updateSpatialNode(
      node);
}

//  void QQuick3DTextureData::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuick3DTextureData12markAllDirtyEv(
    QQuick3DTextureData *self) {
  static_cast<OwnQQuick3DTextureData *>(self)->OwnQQuick3DTextureData::markAllDirty();
}
