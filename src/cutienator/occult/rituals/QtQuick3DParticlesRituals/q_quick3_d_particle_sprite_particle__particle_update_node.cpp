//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h>
#include <QtQuick3DParticles/private/qquick3dparticleemitter_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3dparticles/qquick3dparticlespriteparticle.cpp, line 354, as _ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNode17updateSpatialNodeEP21QSSGRenderGraphObject
inline QSSGRenderGraphObject *QQuick3DParticleSpriteParticle::ParticleUpdateNode::updateSpatialNode(QSSGRenderGraphObject *node)
{
    if (m_particle) {
        node = m_particle->updateParticleNode(this, node);
        QQuick3DNode::updateSpatialNode(node);
        Q_QUICK3D_PROFILE_ASSIGN_ID_SG(m_particle, node);
        auto particles = static_cast<QSSGRenderParticles *>(node);

        if (m_particle->m_featureLevel == QQuick3DParticleSpriteParticle::Animated || m_particle->m_featureLevel == QQuick3DParticleSpriteParticle::AnimatedVLight)
            m_particle->updateAnimatedParticleBuffer(this, particles);
        else
            m_particle->updateParticleBuffer(this, particles);

        m_nodeDirty = false;
    }
    return node;
}
//  -----------------------------------------------------------------------

//  A QQuick3DParticleSpriteParticle::ParticleUpdateNode that Python can take functions over in. Every QQuick3DParticleSpriteParticle::ParticleUpdateNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall4)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall6)(const void *, int *);
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleSpriteParticle_ParticleUpdateNode : public QQuick3DParticleSpriteParticle::ParticleUpdateNode {
public:
  using QQuick3DParticleSpriteParticle::ParticleUpdateNode::ParticleUpdateNode;
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
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  QSSGRenderGraphObject *QQuick3DParticleSpriteParticle::ParticleUpdate
  //      Node::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall0 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DParticleSpriteParticle::ParticleUpdateNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall1 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall1>(taken[1]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall2 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall2>(taken[2]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall3 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall4 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall5 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall6 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall7 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall7>(taken[7]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall8 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall8>(taken[8]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall9 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall9>(taken[9]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall10 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall10>(taken[10]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall11 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall11>(taken[11]);
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
      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall12 call = reinterpret_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNodeCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QQuick3DParticleSpriteParticle::ParticleUpdateNode::ParticleUpdateNode(QQ
//      uick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSpriteParticle::ParticleUpdateNode *ritual_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNodeC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleSpriteParticle_ParticleUpdateNode(parent);
}

//  QSSGRenderGraphObject *QQuick3DParticleSpriteParticle::ParticleUpdateNode
//      ::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNode17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleSpriteParticle::ParticleUpdateNode *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  a Python function taken by a
//      CuteQQuick3DParticleSpriteParticle_ParticleUpdateNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleSpriteParticle_ParticleUpdateNode(
    QQuick3DParticleSpriteParticle::ParticleUpdateNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleSpriteParticle_ParticleUpdateNode *>(self)->take(key, call);
}

//  QSSGRenderGraphObject *QQuick3DParticleSpriteParticle::ParticleUpdateNode
//      ::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNode17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DParticleSpriteParticle::ParticleUpdateNode *self,
    QSSGRenderGraphObject *node) {
  return self->QQuick3DParticleSpriteParticle::ParticleUpdateNode::updateSpatialNode(
      node);
}
