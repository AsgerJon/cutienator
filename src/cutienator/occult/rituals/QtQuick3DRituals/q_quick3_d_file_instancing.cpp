//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DFileInstancing that Python can take functions over in. Every QQuick3DFileInstancing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DFileInstancingCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DFileInstancingCall1)(const void *, int *);
typedef void (*CuteQQuick3DFileInstancingCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DFileInstancingCall3)(const void *, int *);
typedef void (*CuteQQuick3DFileInstancingCall4)(const void *, int *);
typedef void (*CuteQQuick3DFileInstancingCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DFileInstancingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DFileInstancingCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DFileInstancingCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DFileInstancingCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DFileInstancingCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DFileInstancingCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DFileInstancingCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DFileInstancing : public QQuick3DFileInstancing {
public:
  using QQuick3DFileInstancing::QQuick3DFileInstancing;
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
  //      *QQuick3DInstancing::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DFileInstancingCall0 call = reinterpret_cast<CuteQQuick3DFileInstancingCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DInstancing::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DFileInstancingCall1 call = reinterpret_cast<CuteQQuick3DFileInstancingCall1>(taken[1]);
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
      CuteQQuick3DFileInstancingCall2 call = reinterpret_cast<CuteQQuick3DFileInstancingCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DFileInstancingCall3 call = reinterpret_cast<CuteQQuick3DFileInstancingCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DFileInstancingCall4 call = reinterpret_cast<CuteQQuick3DFileInstancingCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DFileInstancingCall5 call = reinterpret_cast<CuteQQuick3DFileInstancingCall5>(taken[5]);
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
      CuteQQuick3DFileInstancingCall6 call = reinterpret_cast<CuteQQuick3DFileInstancingCall6>(taken[6]);
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
      CuteQQuick3DFileInstancingCall7 call = reinterpret_cast<CuteQQuick3DFileInstancingCall7>(taken[7]);
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
      CuteQQuick3DFileInstancingCall8 call = reinterpret_cast<CuteQQuick3DFileInstancingCall8>(taken[8]);
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
      CuteQQuick3DFileInstancingCall9 call = reinterpret_cast<CuteQQuick3DFileInstancingCall9>(taken[9]);
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
      CuteQQuick3DFileInstancingCall10 call = reinterpret_cast<CuteQQuick3DFileInstancingCall10>(taken[10]);
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
      CuteQQuick3DFileInstancingCall11 call = reinterpret_cast<CuteQQuick3DFileInstancingCall11>(taken[11]);
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
      CuteQQuick3DFileInstancingCall12 call = reinterpret_cast<CuteQQuick3DFileInstancingCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DFileInstancing::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DFileInstancing10metaObjectEv(
    const QQuick3DFileInstancing *self) {
  return self->metaObject();
}

//  void *QQuick3DFileInstancing::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DFileInstancing11qt_metacastEPKc(
    QQuick3DFileInstancing *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DFileInstancing::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DFileInstancing11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DFileInstancing *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DFileInstancing::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DFileInstancing2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DFileInstancing::tr(s, c, n));
}

//  QQuick3DFileInstancing::QQuick3DFileInstancing(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DFileInstancing *ritual_ZN22QQuick3DFileInstancingC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DFileInstancing(parent);
}

//  QQuick3DFileInstancing::~QQuick3DFileInstancing()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DFileInstancingD1Ev(QQuick3DFileInstancing *self) {
  delete self;
}

//  const QUrl &QQuick3DFileInstancing::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuick3DFileInstancing6sourceEv(
    const QQuick3DFileInstancing *self) {
  return new QUrl(self->source());
}

//  void QQuick3DFileInstancing::setSource(const QUrl &newSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DFileInstancing9setSourceERK4QUrl(
    QQuick3DFileInstancing *self,
    const QUrl *newSource) {
  self->setSource(*newSource);
}

//  bool QQuick3DFileInstancing::loadFromBinaryFile(const QString &filename)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuick3DFileInstancing18loadFromBinaryFileERK7QString(
    QQuick3DFileInstancing *self,
    const QString *filename) {
  return self->loadFromBinaryFile(*filename);
}

//  bool QQuick3DFileInstancing::loadFromXmlFile(const QString &filename)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuick3DFileInstancing15loadFromXmlFileERK7QString(
    QQuick3DFileInstancing *self,
    const QString *filename) {
  return self->loadFromXmlFile(*filename);
}

//  int QQuick3DFileInstancing::writeToBinaryFile(QIODevice *out)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DFileInstancing17writeToBinaryFileEP9QIODevice(
    QQuick3DFileInstancing *self,
    QIODevice *out) {
  return self->writeToBinaryFile(out);
}

//  int QQuick3DFileInstancing::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DFileInstancing13instanceCountEv(
    const QQuick3DFileInstancing *self) {
  return self->instanceCount();
}

//  void QQuick3DFileInstancing::instanceCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DFileInstancing20instanceCountChangedEv(
    QQuick3DFileInstancing *self) {
  self->instanceCountChanged();
}

//  void QQuick3DFileInstancing::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DFileInstancing13sourceChangedEv(
    QQuick3DFileInstancing *self) {
  self->sourceChanged();
}

//  QByteArray QQuick3DFileInstancing::getInstanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QQuick3DFileInstancing17getInstanceBufferEPi(
    QQuick3DFileInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

//  bool QQuick3DFileInstancing::loadFromFile(const QUrl &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuick3DFileInstancing12loadFromFileERK4QUrl(
    QQuick3DFileInstancing *self,
    const QUrl *source) {
  return self->loadFromFile(*source);
}

//  a Python function taken by a CuteQQuick3DFileInstancing, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DFileInstancing(
    QQuick3DFileInstancing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DFileInstancing *>(self)->take(key, call);
}
