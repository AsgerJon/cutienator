//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/qquick3dquadtextureprovider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dquadtextureprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dquadtextureprovider_p.h"
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#include <ssg/qssgrenderextensions.h>
#include <ssg/qssgrenderhelpers.h>
#include <ssg/qssgrendercontextcore.h>
#include <ssg/qquick3dextensionhelpers.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 720, as _ZNK27QQuick3DQuadTextureProvider14fragmentShaderEv
inline QUrl QQuick3DQuadTextureProvider::fragmentShader() const
{
    return m_fragmentShader;
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 734, as _ZNK27QQuick3DQuadTextureProvider18fragmentShaderCodeEv
inline QString QQuick3DQuadTextureProvider::fragmentShaderCode() const
{
    return m_fragmentShaderCode;
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 749, as _ZNK27QQuick3DQuadTextureProvider5widthEv
inline int QQuick3DQuadTextureProvider::width() const
{
    return m_width;
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 764, as _ZNK27QQuick3DQuadTextureProvider6heightEv
inline int QQuick3DQuadTextureProvider::height() const
{
    return m_height;
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 779, as _ZNK27QQuick3DQuadTextureProvider6formatEv
inline QQuick3DTextureData::Format QQuick3DQuadTextureProvider::format() const
{
    return m_format;
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 707, as _ZN27QQuick3DQuadTextureProvider24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE
inline void QQuick3DQuadTextureProvider::markTrackedPropertyDirty(QMetaProperty property, DirtyPropertyHint hint)
{
    Q_UNUSED(property);
    Q_UNUSED(hint);
    markDirty(Dirty::TrackedProperty);
}

//  from ../qtquick3d/src/helpers/qquick3dquadtextureprovider.cpp, line 714, as _ZN27QQuick3DQuadTextureProvider9markDirtyENS_5DirtyE
inline void QQuick3DQuadTextureProvider::markDirty(Dirty v)
{
    m_dirtyFlag |= v;
    update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DQuadTextureProvider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DQuadTextureProvider : QQuick3DQuadTextureProvider {
  using QQuick3DQuadTextureProvider::markTrackedPropertyDirty;
};

//  A QQuick3DQuadTextureProvider that Python can take functions over in. Every QQuick3DQuadTextureProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DQuadTextureProviderCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DQuadTextureProviderCall1)(const void *, const QMetaProperty *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuadTextureProviderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall3)(const void *, int *);
typedef void (*CuteQQuick3DQuadTextureProviderCall4)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DQuadTextureProviderCall5)(const void *, int *);
typedef void (*CuteQQuick3DQuadTextureProviderCall6)(const void *, int *);
typedef void (*CuteQQuick3DQuadTextureProviderCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuadTextureProviderCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuadTextureProviderCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DQuadTextureProvider : public QQuick3DQuadTextureProvider {
public:
  using QQuick3DQuadTextureProvider::QQuick3DQuadTextureProvider;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuick3DPropertyChangedTracker24markTrackedPropertyDirtyE13QMetaPropertyNS_17DirtyPropertyHintE")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DQuadTextureProvider::updateSpatialNode(QSSGRenderGraphOb
  //      ject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall0 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DQuadTextureProvider::updateSpatialNode(node);
  }

  //  void
  //      QQuick3DQuadTextureProvider::markTrackedPropertyDirty(QMetaProper
  //      ty property, DirtyPropertyHint hint)
  void markTrackedPropertyDirty(
      QMetaProperty property,
      QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall1 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall1>(taken[1]);
      call(this, &property, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QQuick3DQuadTextureProvider::markTrackedPropertyDirty(property, hint);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuick3DTextureProviderExtension::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall2 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuick3DTextureProviderExtension::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall3 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall4 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall4>(taken[4]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall5 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall6 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall7 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall8 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall9 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall10 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall11 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall12 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DQuadTextureProviderCall13 call = reinterpret_cast<CuteQQuick3DQuadTextureProviderCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DQuadTextureProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuick3DQuadTextureProvider10metaObjectEv(
    const QQuick3DQuadTextureProvider *self) {
  return self->metaObject();
}

//  QUrl QQuick3DQuadTextureProvider::fragmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK27QQuick3DQuadTextureProvider14fragmentShaderEv(
    const QQuick3DQuadTextureProvider *self) {
  return new QUrl(self->fragmentShader());
}

//  QString QQuick3DQuadTextureProvider::fragmentShaderCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQuick3DQuadTextureProvider18fragmentShaderCodeEv(
    const QQuick3DQuadTextureProvider *self) {
  return new QString(self->fragmentShaderCode());
}

//  int QQuick3DQuadTextureProvider::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuick3DQuadTextureProvider5widthEv(
    const QQuick3DQuadTextureProvider *self) {
  return self->width();
}

//  int QQuick3DQuadTextureProvider::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuick3DQuadTextureProvider6heightEv(
    const QQuick3DQuadTextureProvider *self) {
  return self->height();
}

//  QQuick3DTextureData::Format QQuick3DQuadTextureProvider::format() const
extern "C" Q_DECL_EXPORT
QQuick3DTextureData::Format ritual_ZNK27QQuick3DQuadTextureProvider6formatEv(
    const QQuick3DQuadTextureProvider *self) {
  return self->format();
}

//  void QQuick3DQuadTextureProvider::markTrackedPropertyDirty(QMetaProperty
//      property, DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuadTextureProvider24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DQuadTextureProvider *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  self->markTrackedPropertyDirty(*property, hint);
}

//  void QQuick3DQuadTextureProvider::markDirty(Dirty v)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuadTextureProvider9markDirtyENS_5DirtyE(
    QQuick3DQuadTextureProvider *self,
    QQuick3DQuadTextureProvider::Dirty v) {
  self->markDirty(v);
}

//  QQuick3DQuadTextureProvider as the QQuick3DPropertyChangedTracker it is
//      built on
extern "C" Q_DECL_EXPORT
QQuick3DPropertyChangedTracker *ritual_cast_QQuick3DQuadTextureProvider_QQuick3DPropertyChangedTracker(
    QQuick3DQuadTextureProvider *self) {
  return static_cast<QQuick3DPropertyChangedTracker *>(self);
}

//  a Python function taken by a CuteQQuick3DQuadTextureProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DQuadTextureProvider(
    QQuick3DQuadTextureProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DQuadTextureProvider *>(self)->take(key, call);
}

//  void QQuick3DQuadTextureProvider::markTrackedPropertyDirty(QMetaProperty
//      property, DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuick3DQuadTextureProvider24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DQuadTextureProvider *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  static_cast<OwnQQuick3DQuadTextureProvider *>(self)->OwnQQuick3DQuadTextureProvider::markTrackedPropertyDirty(
      *property,
      hint);
}
