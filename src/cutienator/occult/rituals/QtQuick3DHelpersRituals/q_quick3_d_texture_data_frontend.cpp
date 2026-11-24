//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/qquick3dtexturedatafrontend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dtexturedatafrontend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DTextureDataFrontend that Python can take functions over in. Every QQuick3DTextureDataFrontend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DTextureDataFrontendCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DTextureDataFrontendCall1)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataFrontendCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DTextureDataFrontendCall3)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataFrontendCall4)(const void *, int *);
typedef void (*CuteQQuick3DTextureDataFrontendCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureDataFrontendCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DTextureDataFrontendCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataFrontendCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataFrontendCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataFrontendCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataFrontendCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DTextureDataFrontendCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DTextureDataFrontend : public QQuick3DTextureDataFrontend {
public:
  using QQuick3DTextureDataFrontend::QQuick3DTextureDataFrontend;
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
      CuteQQuick3DTextureDataFrontendCall0 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTextureData::updateSpatialNode(node);
  }

  //  void QQuick3DTextureData::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DTextureDataFrontendCall1 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall1>(taken[1]);
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
      CuteQQuick3DTextureDataFrontendCall2 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DTextureDataFrontendCall3 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DTextureDataFrontendCall4 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DTextureDataFrontendCall5 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall5>(taken[5]);
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
      CuteQQuick3DTextureDataFrontendCall6 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall6>(taken[6]);
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
      CuteQQuick3DTextureDataFrontendCall7 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall7>(taken[7]);
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
      CuteQQuick3DTextureDataFrontendCall8 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall8>(taken[8]);
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
      CuteQQuick3DTextureDataFrontendCall9 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall9>(taken[9]);
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
      CuteQQuick3DTextureDataFrontendCall10 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall10>(taken[10]);
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
      CuteQQuick3DTextureDataFrontendCall11 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall11>(taken[11]);
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
      CuteQQuick3DTextureDataFrontendCall12 call = reinterpret_cast<CuteQQuick3DTextureDataFrontendCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DTextureDataFrontend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuick3DTextureDataFrontend10metaObjectEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->metaObject();
}

//  QString QQuick3DTextureDataFrontend::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuick3DTextureDataFrontend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DTextureDataFrontend::tr(s, c, n));
}

//  QQuick3DTextureDataFrontend::QQuick3DTextureDataFrontend()
extern "C" Q_DECL_EXPORT
QQuick3DTextureDataFrontend *ritual_ZN27QQuick3DTextureDataFrontendC1Ev() {
  return new CuteQQuick3DTextureDataFrontend();
}

//  QQuick3DTextureData::Format QQuick3DTextureDataFrontend::format() const
extern "C" Q_DECL_EXPORT
QQuick3DTextureData::Format ritual_ZNK27QQuick3DTextureDataFrontend6formatEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->format();
}

//  int QQuick3DTextureDataFrontend::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuick3DTextureDataFrontend5depthEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->depth();
}

//  void QQuick3DTextureDataFrontend::setDepth(int newDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DTextureDataFrontend8setDepthEi(
    QQuick3DTextureDataFrontend *self,
    int newDepth) {
  self->setDepth(newDepth);
}

//  bool QQuick3DTextureDataFrontend::hasTransparency() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuick3DTextureDataFrontend15hasTransparencyEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->hasTransparency();
}

//  void QQuick3DTextureDataFrontend::setHasTransparency(bool
//      newHasTransparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DTextureDataFrontend18setHasTransparencyEb(
    QQuick3DTextureDataFrontend *self,
    bool newHasTransparency) {
  self->setHasTransparency(newHasTransparency);
}

//  QByteArray QQuick3DTextureDataFrontend::textureData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QQuick3DTextureDataFrontend11textureDataEv(
    const QQuick3DTextureDataFrontend *self) {
  return new QByteArray(self->textureData());
}

//  void QQuick3DTextureDataFrontend::setTextureData(const QByteArray
//      &newTextureData)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DTextureDataFrontend14setTextureDataERK10QByteArray(
    QQuick3DTextureDataFrontend *self,
    const QByteArray *newTextureData) {
  self->setTextureData(*newTextureData);
}

//  int QQuick3DTextureDataFrontend::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuick3DTextureDataFrontend5widthEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->width();
}

//  void QQuick3DTextureDataFrontend::setWidth(int newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DTextureDataFrontend8setWidthEi(
    QQuick3DTextureDataFrontend *self,
    int newWidth) {
  self->setWidth(newWidth);
}

//  int QQuick3DTextureDataFrontend::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuick3DTextureDataFrontend6heightEv(
    const QQuick3DTextureDataFrontend *self) {
  return self->height();
}

//  void QQuick3DTextureDataFrontend::setHeight(int newHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DTextureDataFrontend9setHeightEi(
    QQuick3DTextureDataFrontend *self,
    int newHeight) {
  self->setHeight(newHeight);
}

//  a Python function taken by a CuteQQuick3DTextureDataFrontend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTextureDataFrontend(
    QQuick3DTextureDataFrontend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTextureDataFrontend *>(self)->take(key, call);
}
