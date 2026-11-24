//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DLoader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DLoader : QQuick3DLoader {
  using QQuick3DLoader::componentComplete;
};

//  A QQuick3DLoader that Python can take functions over in. Every QQuick3DLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DLoaderCall0)(const void *, int *);
typedef void (*CuteQQuick3DLoaderCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLoaderCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLoaderCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DLoaderCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DLoaderCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DLoaderCall6)(const void *, int *);
typedef void (*CuteQQuick3DLoaderCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DLoaderCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DLoaderCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLoaderCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLoaderCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLoaderCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DLoader : public QQuick3DLoader {
public:
  using QQuick3DLoader::QQuick3DLoader;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
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
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DLoader::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DLoaderCall0 call = reinterpret_cast<CuteQQuick3DLoaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DLoader::componentComplete();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DLoaderCall1 call = reinterpret_cast<CuteQQuick3DLoaderCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DLoaderCall2 call = reinterpret_cast<CuteQQuick3DLoaderCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DLoaderCall3 call = reinterpret_cast<CuteQQuick3DLoaderCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DLoaderCall4 call = reinterpret_cast<CuteQQuick3DLoaderCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DLoaderCall5 call = reinterpret_cast<CuteQQuick3DLoaderCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DLoaderCall6 call = reinterpret_cast<CuteQQuick3DLoaderCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DLoaderCall7 call = reinterpret_cast<CuteQQuick3DLoaderCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DLoaderCall8 call = reinterpret_cast<CuteQQuick3DLoaderCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DLoaderCall9 call = reinterpret_cast<CuteQQuick3DLoaderCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DLoaderCall10 call = reinterpret_cast<CuteQQuick3DLoaderCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DLoaderCall11 call = reinterpret_cast<CuteQQuick3DLoaderCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DLoaderCall12 call = reinterpret_cast<CuteQQuick3DLoaderCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuick3DLoader10metaObjectEv(
    const QQuick3DLoader *self) {
  return self->metaObject();
}

//  QString QQuick3DLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuick3DLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DLoader::tr(s, c, n));
}

//  QQuick3DLoader::QQuick3DLoader(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DLoader *ritual_ZN14QQuick3DLoaderC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DLoader(parent);
}

//  QQuick3DLoader::~QQuick3DLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoaderD1Ev(QQuick3DLoader *self) {
  delete self;
}

//  bool QQuick3DLoader::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DLoader6activeEv(const QQuick3DLoader *self) {
  return self->active();
}

//  void QQuick3DLoader::setActive(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader9setActiveEb(
    QQuick3DLoader *self,
    bool newVal) {
  self->setActive(newVal);
}

//  void QQuick3DLoader::setSource(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader9setSourceEP14QQmlV4Function(
    QQuick3DLoader *self,
    QQmlV4FunctionPtr a0) {
  self->setSource(a0);
}

//  QUrl QQuick3DLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QQuick3DLoader6sourceEv(const QQuick3DLoader *self) {
  return new QUrl(self->source());
}

//  void QQuick3DLoader::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader9setSourceERK4QUrl(
    QQuick3DLoader *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  QQmlComponent *QQuick3DLoader::sourceComponent() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuick3DLoader15sourceComponentEv(
    const QQuick3DLoader *self) {
  return self->sourceComponent();
}

//  void QQuick3DLoader::setSourceComponent(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader18setSourceComponentEP13QQmlComponent(
    QQuick3DLoader *self,
    QQmlComponent *a0) {
  self->setSourceComponent(a0);
}

//  void QQuick3DLoader::resetSourceComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader20resetSourceComponentEv(
    QQuick3DLoader *self) {
  self->resetSourceComponent();
}

//  Status QQuick3DLoader::status() const
extern "C" Q_DECL_EXPORT
QQuick3DLoader::Status ritual_ZNK14QQuick3DLoader6statusEv(
    const QQuick3DLoader *self) {
  return self->status();
}

//  qreal QQuick3DLoader::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuick3DLoader8progressEv(const QQuick3DLoader *self) {
  return self->progress();
}

//  bool QQuick3DLoader::asynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuick3DLoader12asynchronousEv(const QQuick3DLoader *self) {
  return self->asynchronous();
}

//  void QQuick3DLoader::setAsynchronous(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader15setAsynchronousEb(
    QQuick3DLoader *self,
    bool a) {
  self->setAsynchronous(a);
}

//  QObject *QQuick3DLoader::item() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK14QQuick3DLoader4itemEv(const QQuick3DLoader *self) {
  return self->item();
}

//  void QQuick3DLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader17componentCompleteEv(QQuick3DLoader *self) {
  self->componentComplete();
}

//  void QQuick3DLoader::sourceLoaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader12sourceLoadedEv(QQuick3DLoader *self) {
  self->sourceLoaded();
}

//  void QQuick3DLoader::setSource(const QUrl &sourceUrl, bool needsClear)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader9setSourceERK4QUrlb(
    QQuick3DLoader *self,
    const QUrl *sourceUrl,
    bool needsClear) {
  self->setSource(*sourceUrl, needsClear);
}

//  void QQuick3DLoader::loadFromSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader14loadFromSourceEv(QQuick3DLoader *self) {
  self->loadFromSource();
}

//  void QQuick3DLoader::loadFromSourceComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader23loadFromSourceComponentEv(
    QQuick3DLoader *self) {
  self->loadFromSourceComponent();
}

//  void QQuick3DLoader::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader5clearEv(QQuick3DLoader *self) {
  self->clear();
}

//  void QQuick3DLoader::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader4loadEv(QQuick3DLoader *self) {
  self->load();
}

//  void QQuick3DLoader::incubatorStateChanged(QQmlIncubator::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader21incubatorStateChangedEN13QQmlIncubator6StatusE(
    QQuick3DLoader *self,
    QQmlIncubator::Status status) {
  self->incubatorStateChanged(status);
}

//  void QQuick3DLoader::setInitialState(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader15setInitialStateEP7QObject(
    QQuick3DLoader *self,
    QObject *obj) {
  self->setInitialState(obj);
}

//  void QQuick3DLoader::disposeInitialPropertyValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader28disposeInitialPropertyValuesEv(
    QQuick3DLoader *self) {
  self->disposeInitialPropertyValues();
}

//  QUrl QQuick3DLoader::resolveSourceUrl(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN14QQuick3DLoader16resolveSourceUrlEP14QQmlV4Function(
    QQmlV4FunctionPtr args) {
  return new QUrl(QQuick3DLoader::resolveSourceUrl(args));
}

//  QV4::ReturnedValue
//      QQuick3DLoader::extractInitialPropertyValues(QQmlV4FunctionPtr args,
//      bool *error)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN14QQuick3DLoader28extractInitialPropertyValuesEP14QQmlV4FunctionPb(
    QQuick3DLoader *self,
    QQmlV4FunctionPtr args,
    bool *error) {
  return self->extractInitialPropertyValues(args, error);
}

//  void QQuick3DLoader::createComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuick3DLoader15createComponentEv(QQuick3DLoader *self) {
  self->createComponent();
}

//  a Python function taken by a CuteQQuick3DLoader, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DLoader(
    QQuick3DLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DLoader *>(self)->take(key, call);
}

//  void QQuick3DLoader::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuick3DLoader17componentCompleteEv(
    QQuick3DLoader *self) {
  static_cast<OwnQQuick3DLoader *>(self)->OwnQQuick3DLoader::componentComplete();
}
