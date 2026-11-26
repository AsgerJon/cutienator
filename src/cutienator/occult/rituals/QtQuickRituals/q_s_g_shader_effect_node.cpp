//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGShaderEffectNode that Python can take functions over in. Every QSGShaderEffectNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQSGShaderEffectNodeCall0)(const void *, bool, int *);
typedef void (*CuteQSGShaderEffectNodeCall1)(const void *, QSGShaderEffectNode::SyncData *, int *);
typedef void (*CuteQSGShaderEffectNodeCall2)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGShaderEffectNodeCall3)(const void *, int *);
typedef void (*CuteQSGShaderEffectNodeCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGShaderEffectNodeCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGShaderEffectNodeCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGShaderEffectNodeCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGShaderEffectNodeCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGShaderEffectNodeCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGShaderEffectNodeCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGShaderEffectNodeCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGShaderEffectNode : public QSGShaderEffectNode {
public:
  using QSGShaderEffectNode::QSGShaderEffectNode;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGShaderEffectNode30updateNormalizedTextureSubRectEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGShaderEffectNode12syncMaterialEPNS_8SyncDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QRectF QSGShaderEffectNode::updateNormalizedTextureSubRect(bool
  //      supportsAtlasTextures)
  QRectF updateNormalizedTextureSubRect(
      bool supportsAtlasTextures) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall0 call = reinterpret_cast<CuteQSGShaderEffectNodeCall0>(taken[0]);
      const QRectF * given = call(this, supportsAtlasTextures, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGShaderEffectNode::syncMaterial(SyncData *syncData)
  void syncMaterial(QSGShaderEffectNode::SyncData *syncData) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall1 call = reinterpret_cast<CuteQSGShaderEffectNodeCall1>(taken[1]);
      call(this, syncData, &handled);
      if (handled) return;
    }
  }

  //  void QSGShaderEffectNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall2 call = reinterpret_cast<CuteQSGShaderEffectNodeCall2>(taken[2]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGShaderEffectNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall3 call = reinterpret_cast<CuteQSGShaderEffectNodeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall4 call = reinterpret_cast<CuteQSGShaderEffectNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall5 call = reinterpret_cast<CuteQSGShaderEffectNodeCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall6 call = reinterpret_cast<CuteQSGShaderEffectNodeCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall7 call = reinterpret_cast<CuteQSGShaderEffectNodeCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall8 call = reinterpret_cast<CuteQSGShaderEffectNodeCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall9 call = reinterpret_cast<CuteQSGShaderEffectNodeCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall10 call = reinterpret_cast<CuteQSGShaderEffectNodeCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGShaderEffectNodeCall11 call = reinterpret_cast<CuteQSGShaderEffectNodeCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGShaderEffectNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QSGShaderEffectNode10metaObjectEv(
    const QSGShaderEffectNode *self) {
  return self->metaObject();
}

//  void *QSGShaderEffectNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QSGShaderEffectNode11qt_metacastEPKc(
    QSGShaderEffectNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGShaderEffectNode::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QSGShaderEffectNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGShaderEffectNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGShaderEffectNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QSGShaderEffectNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGShaderEffectNode::tr(s, c, n));
}

//  QSGShaderEffectNode::~QSGShaderEffectNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGShaderEffectNodeD1Ev(QSGShaderEffectNode *self) {
  delete self;
}

//  QRectF QSGShaderEffectNode::updateNormalizedTextureSubRect(bool
//      supportsAtlasTextures)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN19QSGShaderEffectNode30updateNormalizedTextureSubRectEb(
    QSGShaderEffectNode *self,
    bool supportsAtlasTextures) {
  return new QRectF(
      self->updateNormalizedTextureSubRect(
          supportsAtlasTextures));
}

//  void QSGShaderEffectNode::syncMaterial(SyncData *syncData)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGShaderEffectNode12syncMaterialEPNS_8SyncDataE(
    QSGShaderEffectNode *self,
    QSGShaderEffectNode::SyncData *syncData) {
  self->syncMaterial(syncData);
}

//  void QSGShaderEffectNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGShaderEffectNode6acceptEP16QSGNodeVisitorEx(
    QSGShaderEffectNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  void QSGShaderEffectNode::textureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGShaderEffectNode14textureChangedEv(
    QSGShaderEffectNode *self) {
  self->textureChanged();
}

//  QSGShaderEffectNode as the QSGVisitableNode it is built on
extern "C" Q_DECL_EXPORT
QSGVisitableNode *ritual_cast_QSGShaderEffectNode_QSGVisitableNode(
    QSGShaderEffectNode *self) {
  return static_cast<QSGVisitableNode *>(self);
}

//  a Python function taken by a CuteQSGShaderEffectNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGShaderEffectNode(
    QSGShaderEffectNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGShaderEffectNode *>(self)->take(key, call);
}

//  void QSGShaderEffectNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGShaderEffectNode6acceptEP16QSGNodeVisitorEx(
    QSGShaderEffectNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGShaderEffectNode::accept(visitor);
}
