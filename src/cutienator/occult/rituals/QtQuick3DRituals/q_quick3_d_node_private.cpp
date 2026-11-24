//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p.h>
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dnode_p.h"
#include "qquick3dnode_p_p.h"
#include <QtQuick3DRuntimeRender/private/qssgrendernode_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtMath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dnode.cpp, line 412, as _ZNK19QQuick3DNodePrivate19localRotationMatrixEv
inline QMatrix4x4 QQuick3DNodePrivate::localRotationMatrix() const
{
    return QMatrix4x4(m_rotation.toRotationMatrix());
}

//  from ../qtquick3d/src/quick3d/qquick3dnode.cpp, line 417, as _ZNK19QQuick3DNodePrivate19sceneRotationMatrixEv
inline QMatrix4x4 QQuick3DNodePrivate::sceneRotationMatrix() const
{
    Q_Q(const QQuick3DNode);

    if (m_sceneTransformDirty) {
        // Ensure m_hasInheritedUniformScale is up to date
        const_cast<QQuick3DNodePrivate *>(this)->calculateGlobalVariables();
    }

    if (m_hasInheritedUniformScale) {
        // When we know that every node up to the root have a uniform scale, we can extract the
        // rotation directly from the sceneTransform(). This is optimizing, since we reuse that
        // matrix for more than just calculating the sceneRotation.
        QMatrix4x4 rotationMatrix = q->sceneTransform();
        QSSGUtils::mat44::normalize(rotationMatrix);
        return rotationMatrix;
    }

    // When we have an ancestor that has a non-uniform scale, we cannot extract
    // the rotation from the sceneMatrix directly. Instead, we need to calculate
    // it separately, which is slightly more costly.
    const QMatrix4x4 parentRotationMatrix = QQuick3DNodePrivate::get(q->parentNode())->sceneRotationMatrix();
    return parentRotationMatrix * localRotationMatrix();
}
//  -----------------------------------------------------------------------

//  A QQuick3DNodePrivate that Python can take functions over in. Every QQuick3DNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DNodePrivateCall0)(const void *, int *);
class CuteQQuick3DNodePrivate : public QQuick3DNodePrivate {
public:
  using QQuick3DNodePrivate::QQuick3DNodePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuick3DObjectPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuick3DObjectPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DNodePrivateCall0 call = reinterpret_cast<CuteQQuick3DNodePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObjectPrivate::updatePolish();
  }
};

//  QQuick3DNode *QQuick3DNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN19QQuick3DNodePrivate6q_funcEv(
    QQuick3DNodePrivate *self) {
  return self->q_func();
}

//  const QQuick3DNode *QQuick3DNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuick3DNode *ritual_ZNK19QQuick3DNodePrivate6q_funcEv(
    const QQuick3DNodePrivate *self) {
  return self->q_func();
}

//  QQuick3DNodePrivate::QQuick3DNodePrivate(QQuick3DObjectPrivate::Type t,
//      QQuick3DContentLayer::LayerFlag layerFlag)
extern "C" Q_DECL_EXPORT
QQuick3DNodePrivate *ritual_ZN19QQuick3DNodePrivateC1EN21QSSGRenderGraphObject4TypeEN20QQuick3DContentLayer9LayerFlagE(
    QQuick3DObjectPrivate::Type t,
    QQuick3DContentLayer::LayerFlag layerFlag) {
  return new CuteQQuick3DNodePrivate(t, layerFlag);
}

//  QQuick3DNodePrivate::~QQuick3DNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivateD1Ev(QQuick3DNodePrivate *self) {
  delete self;
}

//  void QQuick3DNodePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate4initEv(QQuick3DNodePrivate *self) {
  self->init();
}

//  void QQuick3DNodePrivate::calculateGlobalVariables()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate24calculateGlobalVariablesEv(
    QQuick3DNodePrivate *self) {
  self->calculateGlobalVariables();
}

//  void QQuick3DNodePrivate::markSceneTransformDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate23markSceneTransformDirtyEv(
    QQuick3DNodePrivate *self) {
  self->markSceneTransformDirty();
}

//  QMatrix4x4 QQuick3DNodePrivate::localRotationMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QQuick3DNodePrivate19localRotationMatrixEv(
    const QQuick3DNodePrivate *self) {
  return new QMatrix4x4(self->localRotationMatrix());
}

//  QMatrix4x4 QQuick3DNodePrivate::sceneRotationMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QQuick3DNodePrivate19sceneRotationMatrixEv(
    const QQuick3DNodePrivate *self) {
  return new QMatrix4x4(self->sceneRotationMatrix());
}

//  void QQuick3DNodePrivate::emitChangesToSceneTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate27emitChangesToSceneTransformEv(
    QQuick3DNodePrivate *self) {
  self->emitChangesToSceneTransform();
}

//  bool QQuick3DNodePrivate::isSceneTransformRelatedSignal(const QMetaMethod
//      &signal) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DNodePrivate29isSceneTransformRelatedSignalERK11QMetaMethod(
    const QQuick3DNodePrivate *self,
    const QMetaMethod *signal) {
  return self->isSceneTransformRelatedSignal(*signal);
}

//  bool QQuick3DNodePrivate::isDirectionRelatedSignal(const QMetaMethod
//      &signal) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DNodePrivate24isDirectionRelatedSignalERK11QMetaMethod(
    const QQuick3DNodePrivate *self,
    const QMetaMethod *signal) {
  return self->isDirectionRelatedSignal(*signal);
}

//  void QQuick3DNodePrivate::setIsHiddenInEditor(bool isHidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate19setIsHiddenInEditorEb(
    QQuick3DNodePrivate *self,
    bool isHidden) {
  self->setIsHiddenInEditor(isHidden);
}

//  QQuick3DNodePrivate *QQuick3DNodePrivate::get(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
QQuick3DNodePrivate *ritual_ZN19QQuick3DNodePrivate3getEP12QQuick3DNode(
    QQuick3DNode *node) {
  return QQuick3DNodePrivate::get(node);
}

//  void QQuick3DNodePrivate::setLocalTransform(const QMatrix4x4 &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DNodePrivate17setLocalTransformERK10QMatrix4x4(
    QQuick3DNodePrivate *self,
    const QMatrix4x4 *transform) {
  self->setLocalTransform(*transform);
}

//  a Python function taken by a CuteQQuick3DNodePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DNodePrivate(
    QQuick3DNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DNodePrivate *>(self)->take(key, call);
}
