//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DSpati
//  alAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudioroom_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qtquick3daudioglobal_p.h>
#include <QtQuick3DSpatialAudio/QtQuick3DSpatialAudio>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudioroom_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3daudioroom_p.h"
#include <QtQuick3DSpatialAudio/private/qquick3daudioengine_p.h>
#include <QtSpatialAudio/qaudioroom.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 45, as _ZN17QQuick3DAudioRoomD1Ev
inline QQuick3DAudioRoom::~QQuick3DAudioRoom()
{
    delete m_room;
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 58, as _ZN17QQuick3DAudioRoom13setDimensionsE9QVector3D
inline void QQuick3DAudioRoom::setDimensions(QVector3D dim)
{
    m_room->setDimensions(dim);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 63, as _ZNK17QQuick3DAudioRoom10dimensionsEv
inline QVector3D QQuick3DAudioRoom::dimensions() const
{
    return m_room->dimensions();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 123, as _ZN17QQuick3DAudioRoom15setLeftMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setLeftMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::LeftWall, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 128, as _ZNK17QQuick3DAudioRoom12leftMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::leftMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::LeftWall));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 133, as _ZN17QQuick3DAudioRoom16setRightMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setRightMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::RightWall, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 138, as _ZNK17QQuick3DAudioRoom13rightMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::rightMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::RightWall));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 143, as _ZN17QQuick3DAudioRoom16setFrontMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setFrontMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::FrontWall, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 148, as _ZNK17QQuick3DAudioRoom13frontMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::frontMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::FrontWall));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 153, as _ZN17QQuick3DAudioRoom15setBackMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setBackMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::BackWall, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 158, as _ZNK17QQuick3DAudioRoom12backMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::backMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::BackWall));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 163, as _ZN17QQuick3DAudioRoom16setFloorMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setFloorMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::Floor, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 168, as _ZNK17QQuick3DAudioRoom13floorMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::floorMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::Floor));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 173, as _ZN17QQuick3DAudioRoom18setCeilingMaterialENS_8MaterialE
inline void QQuick3DAudioRoom::setCeilingMaterial(Material material)
{
    m_room->setWallMaterial(QAudioRoom::Ceiling, QAudioRoom::Material(material));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 178, as _ZNK17QQuick3DAudioRoom15ceilingMaterialEv
inline QQuick3DAudioRoom::Material QQuick3DAudioRoom::ceilingMaterial() const
{
    return Material(m_room->wallMaterial(QAudioRoom::Ceiling));
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 193, as _ZN17QQuick3DAudioRoom17setReflectionGainEf
inline void QQuick3DAudioRoom::setReflectionGain(float factor)
{
    m_room->setReflectionGain(factor);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 198, as _ZNK17QQuick3DAudioRoom14reflectionGainEv
inline float QQuick3DAudioRoom::reflectionGain() const
{
    return m_room->reflectionGain();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 213, as _ZN17QQuick3DAudioRoom13setReverbGainEf
inline void QQuick3DAudioRoom::setReverbGain(float factor)
{
    m_room->setReverbGain(factor);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 218, as _ZNK17QQuick3DAudioRoom10reverbGainEv
inline float QQuick3DAudioRoom::reverbGain() const
{
    return m_room->reverbGain();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 232, as _ZN17QQuick3DAudioRoom13setReverbTimeEf
inline void QQuick3DAudioRoom::setReverbTime(float factor)
{
    m_room->setReverbTime(factor);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 237, as _ZNK17QQuick3DAudioRoom10reverbTimeEv
inline float QQuick3DAudioRoom::reverbTime() const
{
    return m_room->reverbTime();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 251, as _ZN17QQuick3DAudioRoom19setReverbBrightnessEf
inline void QQuick3DAudioRoom::setReverbBrightness(float factor)
{
    m_room->setReverbBrightness(factor);
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 256, as _ZNK17QQuick3DAudioRoom16reverbBrightnessEv
inline float QQuick3DAudioRoom::reverbBrightness() const
{
    return m_room->reverbBrightness();
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 261, as _ZN17QQuick3DAudioRoom14updatePositionEv
inline void QQuick3DAudioRoom::updatePosition()
{
    m_room->setPosition(scenePosition());
}

//  from ../qtmultimedia/src/spatialaudioquick3d/qquick3daudioroom.cpp, line 266, as _ZN17QQuick3DAudioRoom14updateRotationEv
inline void QQuick3DAudioRoom::updateRotation()
{
    m_room->setRotation(sceneRotation());
}
//  -----------------------------------------------------------------------

//  A QQuick3DAudioRoom that Python can take functions over in. Every QQuick3DAudioRoom
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DAudioRoomCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall3)(const void *, int *);
typedef void * (*CuteQQuick3DAudioRoomCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DAudioRoomCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DAudioRoomCall6)(const void *, int *);
typedef void (*CuteQQuick3DAudioRoomCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAudioRoomCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DAudioRoomCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DAudioRoomCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DAudioRoom : public QQuick3DAudioRoom {
public:
  using QQuick3DAudioRoom::QQuick3DAudioRoom;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
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

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall0 call = reinterpret_cast<CuteQQuick3DAudioRoomCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall1 call = reinterpret_cast<CuteQQuick3DAudioRoomCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall2 call = reinterpret_cast<CuteQQuick3DAudioRoomCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall3 call = reinterpret_cast<CuteQQuick3DAudioRoomCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall4 call = reinterpret_cast<CuteQQuick3DAudioRoomCall4>(taken[4]);
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
      CuteQQuick3DAudioRoomCall5 call = reinterpret_cast<CuteQQuick3DAudioRoomCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall6 call = reinterpret_cast<CuteQQuick3DAudioRoomCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DAudioRoomCall7 call = reinterpret_cast<CuteQQuick3DAudioRoomCall7>(taken[7]);
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
      CuteQQuick3DAudioRoomCall8 call = reinterpret_cast<CuteQQuick3DAudioRoomCall8>(taken[8]);
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
      CuteQQuick3DAudioRoomCall9 call = reinterpret_cast<CuteQQuick3DAudioRoomCall9>(taken[9]);
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
      CuteQQuick3DAudioRoomCall10 call = reinterpret_cast<CuteQQuick3DAudioRoomCall10>(taken[10]);
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
      CuteQQuick3DAudioRoomCall11 call = reinterpret_cast<CuteQQuick3DAudioRoomCall11>(taken[11]);
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
      CuteQQuick3DAudioRoomCall12 call = reinterpret_cast<CuteQQuick3DAudioRoomCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DAudioRoom::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuick3DAudioRoom10metaObjectEv(
    const QQuick3DAudioRoom *self) {
  return self->metaObject();
}

//  QQuick3DAudioRoom::~QQuick3DAudioRoom()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoomD1Ev(QQuick3DAudioRoom *self) {
  delete self;
}

//  void QQuick3DAudioRoom::setDimensions(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom13setDimensionsE9QVector3D(
    QQuick3DAudioRoom *self,
    const QVector3D *pos) {
  self->setDimensions(*pos);
}

//  QVector3D QQuick3DAudioRoom::dimensions() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QQuick3DAudioRoom10dimensionsEv(
    const QQuick3DAudioRoom *self) {
  return new QVector3D(self->dimensions());
}

//  void QQuick3DAudioRoom::setLeftMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom15setLeftMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setLeftMaterial(material);
}

//  Material QQuick3DAudioRoom::leftMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom12leftMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->leftMaterial();
}

//  void QQuick3DAudioRoom::setRightMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom16setRightMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setRightMaterial(material);
}

//  Material QQuick3DAudioRoom::rightMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom13rightMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->rightMaterial();
}

//  void QQuick3DAudioRoom::setFrontMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom16setFrontMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setFrontMaterial(material);
}

//  Material QQuick3DAudioRoom::frontMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom13frontMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->frontMaterial();
}

//  void QQuick3DAudioRoom::setBackMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom15setBackMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setBackMaterial(material);
}

//  Material QQuick3DAudioRoom::backMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom12backMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->backMaterial();
}

//  void QQuick3DAudioRoom::setFloorMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom16setFloorMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setFloorMaterial(material);
}

//  Material QQuick3DAudioRoom::floorMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom13floorMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->floorMaterial();
}

//  void QQuick3DAudioRoom::setCeilingMaterial(Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom18setCeilingMaterialENS_8MaterialE(
    QQuick3DAudioRoom *self,
    QQuick3DAudioRoom::Material material) {
  self->setCeilingMaterial(material);
}

//  Material QQuick3DAudioRoom::ceilingMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DAudioRoom::Material ritual_ZNK17QQuick3DAudioRoom15ceilingMaterialEv(
    const QQuick3DAudioRoom *self) {
  return self->ceilingMaterial();
}

//  void QQuick3DAudioRoom::setReflectionGain(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom17setReflectionGainEf(
    QQuick3DAudioRoom *self,
    float factor) {
  self->setReflectionGain(factor);
}

//  float QQuick3DAudioRoom::reflectionGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DAudioRoom14reflectionGainEv(
    const QQuick3DAudioRoom *self) {
  return self->reflectionGain();
}

//  void QQuick3DAudioRoom::setReverbGain(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom13setReverbGainEf(
    QQuick3DAudioRoom *self,
    float factor) {
  self->setReverbGain(factor);
}

//  float QQuick3DAudioRoom::reverbGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DAudioRoom10reverbGainEv(
    const QQuick3DAudioRoom *self) {
  return self->reverbGain();
}

//  void QQuick3DAudioRoom::setReverbTime(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom13setReverbTimeEf(
    QQuick3DAudioRoom *self,
    float factor) {
  self->setReverbTime(factor);
}

//  float QQuick3DAudioRoom::reverbTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DAudioRoom10reverbTimeEv(
    const QQuick3DAudioRoom *self) {
  return self->reverbTime();
}

//  void QQuick3DAudioRoom::setReverbBrightness(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom19setReverbBrightnessEf(
    QQuick3DAudioRoom *self,
    float factor) {
  self->setReverbBrightness(factor);
}

//  float QQuick3DAudioRoom::reverbBrightness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QQuick3DAudioRoom16reverbBrightnessEv(
    const QQuick3DAudioRoom *self) {
  return self->reverbBrightness();
}

//  void QQuick3DAudioRoom::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom14updatePositionEv(
    QQuick3DAudioRoom *self) {
  self->updatePosition();
}

//  void QQuick3DAudioRoom::updateRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DAudioRoom14updateRotationEv(
    QQuick3DAudioRoom *self) {
  self->updateRotation();
}

//  a Python function taken by a CuteQQuick3DAudioRoom, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DAudioRoom(
    QQuick3DAudioRoom *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DAudioRoom *>(self)->take(key, call);
}
