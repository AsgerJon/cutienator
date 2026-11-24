//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qabstract3dseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 665, as _ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy && proxy != m_dataProxy && !proxy->d_ptr->series());

    delete m_dataProxy;
    m_dataProxy = proxy;

    proxy->d_ptr->setSeries(q_ptr); // also sets parent

    if (m_controller) {
        connectControllerAndProxy(m_controller);
        m_controller->markDataDirty();
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 680, as _ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController
inline void QAbstract3DSeriesPrivate::setController(Abstract3DController *controller)
{
    connectControllerAndProxy(controller);
    m_controller = controller;
    q_ptr->setParent(controller);
    markItemLabelDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 660, as _ZNK24QAbstract3DSeriesPrivate9dataProxyEv
inline QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy() const
{
    return m_dataProxy;
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 688, as _ZN24QAbstract3DSeriesPrivate18setItemLabelFormatERK7QString
inline void QAbstract3DSeriesPrivate::setItemLabelFormat(const QString &format)
{
    m_itemLabelFormat = format;
    markItemLabelDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 694, as _ZN24QAbstract3DSeriesPrivate10setVisibleEb
inline void QAbstract3DSeriesPrivate::setVisible(bool visible)
{
    m_visible = visible;
    markItemLabelDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 700, as _ZN24QAbstract3DSeriesPrivate7setMeshEN17QAbstract3DSeries4MeshE
inline void QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)
{
    m_mesh = mesh;
    m_changeTracker.meshChanged = true;
    if (m_controller) {
        m_controller->markSeriesVisualsDirty();

        if (m_controller->optimizationHints().testFlag(QAbstract3DGraph::OptimizationStatic))
            m_controller->markDataDirty();
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 712, as _ZN24QAbstract3DSeriesPrivate13setMeshSmoothEb
inline void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)
{
    m_meshSmooth = enable;
    m_changeTracker.meshSmoothChanged = true;
    if (m_controller) {
        m_controller->markSeriesVisualsDirty();

        if (m_controller->optimizationHints().testFlag(QAbstract3DGraph::OptimizationStatic))
            m_controller->markDataDirty();
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 724, as _ZN24QAbstract3DSeriesPrivate15setMeshRotationERK11QQuaternion
inline void QAbstract3DSeriesPrivate::setMeshRotation(const QQuaternion &rotation)
{
    m_meshRotation = rotation;
    m_changeTracker.meshRotationChanged = true;
    if (m_controller) {
        m_controller->markSeriesVisualsDirty();

        if (m_controller->optimizationHints().testFlag(QAbstract3DGraph::OptimizationStatic))
            m_controller->markDataDirty();
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 736, as _ZN24QAbstract3DSeriesPrivate18setUserDefinedMeshERK7QString
inline void QAbstract3DSeriesPrivate::setUserDefinedMesh(const QString &meshFile)
{
    m_userDefinedMesh = meshFile;
    m_changeTracker.userDefinedMeshChanged = true;
    if (m_controller) {
        m_controller->markSeriesVisualsDirty();

        if (m_controller->optimizationHints().testFlag(QAbstract3DGraph::OptimizationStatic))
            m_controller->markDataDirty();
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 748, as _ZN24QAbstract3DSeriesPrivate13setColorStyleEN8Q3DTheme10ColorStyleE
inline void QAbstract3DSeriesPrivate::setColorStyle(Q3DTheme::ColorStyle style)
{
    m_colorStyle = style;
    m_changeTracker.colorStyleChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 756, as _ZN24QAbstract3DSeriesPrivate12setBaseColorERK6QColor
inline void QAbstract3DSeriesPrivate::setBaseColor(const QColor &color)
{
    m_baseColor = color;
    m_changeTracker.baseColorChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 764, as _ZN24QAbstract3DSeriesPrivate15setBaseGradientERK15QLinearGradient
inline void QAbstract3DSeriesPrivate::setBaseGradient(const QLinearGradient &gradient)
{
    m_baseGradient = gradient;
    m_changeTracker.baseGradientChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 772, as _ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorERK6QColor
inline void QAbstract3DSeriesPrivate::setSingleHighlightColor(const QColor &color)
{
    m_singleHighlightColor = color;
    m_changeTracker.singleHighlightColorChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 780, as _ZN24QAbstract3DSeriesPrivate26setSingleHighlightGradientERK15QLinearGradient
inline void QAbstract3DSeriesPrivate::setSingleHighlightGradient(const QLinearGradient &gradient)
{
    m_singleHighlightGradient = gradient;
    m_changeTracker.singleHighlightGradientChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 788, as _ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorERK6QColor
inline void QAbstract3DSeriesPrivate::setMultiHighlightColor(const QColor &color)
{
    m_multiHighlightColor = color;
    m_changeTracker.multiHighlightColorChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 796, as _ZN24QAbstract3DSeriesPrivate25setMultiHighlightGradientERK15QLinearGradient
inline void QAbstract3DSeriesPrivate::setMultiHighlightGradient(const QLinearGradient &gradient)
{
    m_multiHighlightGradient = gradient;
    m_changeTracker.multiHighlightGradientChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 804, as _ZN24QAbstract3DSeriesPrivate7setNameERK7QString
inline void QAbstract3DSeriesPrivate::setName(const QString &name)
{
    m_name = name;
    markItemLabelDirty();
    m_changeTracker.nameChanged = true;
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 848, as _ZN24QAbstract3DSeriesPrivate9itemLabelEv
inline QString QAbstract3DSeriesPrivate::itemLabel()
{
    if (m_itemLabelDirty) {
        QString oldLabel = m_itemLabel;
        if (m_controller && m_visible)
            createItemLabel();
        else
            m_itemLabel = QString();
        m_itemLabelDirty = false;

        if (oldLabel != m_itemLabel)
            emit q_ptr->itemLabelChanged(m_itemLabel);
    }

    return m_itemLabel;
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 865, as _ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv
inline void QAbstract3DSeriesPrivate::markItemLabelDirty()
{
    m_itemLabelDirty = true;
    m_changeTracker.itemLabelChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 873, as _ZN24QAbstract3DSeriesPrivate19setItemLabelVisibleEb
inline void QAbstract3DSeriesPrivate::setItemLabelVisible(bool visible)
{
    m_itemLabelVisible = visible;
    markItemLabelDirty();
    m_changeTracker.itemLabelVisibilityChanged = true;
}
//  -----------------------------------------------------------------------

//  A QAbstract3DSeriesPrivate that Python can take functions over in. Every QAbstract3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstract3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall1)(const void *, Abstract3DController *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall2)(const void *, Abstract3DController *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DSeriesPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DSeriesPrivateCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesPrivateCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesPrivateCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesPrivateCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DSeriesPrivate : public QAbstract3DSeriesPrivate {
public:
  using QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate15createItemLabelEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy
  //      *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall0 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QAbstract3DSeriesPrivate::setController(Abstract3DController
  //      *controller)
  void setController(Abstract3DController *controller) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall1 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall1>(taken[1]);
      call(this, controller, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setController(controller);
  }

  //  void QAbstract3DSeriesPrivate::connectControllerAndProxy(Abstract3DCo
  //      ntroller *newController)
  void connectControllerAndProxy(
      Abstract3DController *newController) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall2 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall2>(taken[2]);
      call(this, newController, &handled);
      if (handled) return;
    }
  }

  //  void QAbstract3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall3 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall4 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall5 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall6 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall7 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall8 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall9 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall10 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QAbstract3DSeriesPrivate10metaObjectEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->metaObject();
}

//  QAbstract3DSeriesPrivate::~QAbstract3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivateD1Ev(
    QAbstract3DSeriesPrivate *self) {
  delete self;
}

//  QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy() const
extern "C" Q_DECL_EXPORT
QAbstractDataProxy *ritual_ZNK24QAbstract3DSeriesPrivate9dataProxyEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->dataProxy();
}

//  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QAbstract3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QAbstract3DSeriesPrivate::setController(Abstract3DController
//      *controller)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController(
    QAbstract3DSeriesPrivate *self,
    Abstract3DController *controller) {
  self->setController(controller);
}

//  void
//      QAbstract3DSeriesPrivate::connectControllerAndProxy(Abstract3DControl
//      ler *newController)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QAbstract3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->connectControllerAndProxy(newController);
}

//  void QAbstract3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15createItemLabelEv(
    QAbstract3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QAbstract3DSeriesPrivate::setItemLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18setItemLabelFormatERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *format) {
  self->setItemLabelFormat(*format);
}

//  void QAbstract3DSeriesPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate10setVisibleEb(
    QAbstract3DSeriesPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate7setMeshEN17QAbstract3DSeries4MeshE(
    QAbstract3DSeriesPrivate *self,
    QAbstract3DSeries::Mesh mesh) {
  self->setMesh(mesh);
}

//  void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate13setMeshSmoothEb(
    QAbstract3DSeriesPrivate *self,
    bool enable) {
  self->setMeshSmooth(enable);
}

//  void QAbstract3DSeriesPrivate::setMeshRotation(const QQuaternion
//      &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15setMeshRotationERK11QQuaternion(
    QAbstract3DSeriesPrivate *self,
    const QQuaternion *rotation) {
  self->setMeshRotation(*rotation);
}

//  void QAbstract3DSeriesPrivate::setUserDefinedMesh(const QString
//      &meshFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18setUserDefinedMeshERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *meshFile) {
  self->setUserDefinedMesh(*meshFile);
}

//  void QAbstract3DSeriesPrivate::setColorStyle(Q3DTheme::ColorStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate13setColorStyleEN8Q3DTheme10ColorStyleE(
    QAbstract3DSeriesPrivate *self,
    Q3DTheme::ColorStyle style) {
  self->setColorStyle(style);
}

//  void QAbstract3DSeriesPrivate::setBaseColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate12setBaseColorERK6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setBaseColor(*color);
}

//  void QAbstract3DSeriesPrivate::setBaseGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15setBaseGradientERK15QLinearGradient(
    QAbstract3DSeriesPrivate *self,
    const QLinearGradient *gradient) {
  self->setBaseGradient(*gradient);
}

//  void QAbstract3DSeriesPrivate::setSingleHighlightColor(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorERK6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setSingleHighlightColor(*color);
}

//  void QAbstract3DSeriesPrivate::setSingleHighlightGradient(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate26setSingleHighlightGradientERK15QLinearGradient(
    QAbstract3DSeriesPrivate *self,
    const QLinearGradient *gradient) {
  self->setSingleHighlightGradient(*gradient);
}

//  void QAbstract3DSeriesPrivate::setMultiHighlightColor(const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorERK6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setMultiHighlightColor(*color);
}

//  void QAbstract3DSeriesPrivate::setMultiHighlightGradient(const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate25setMultiHighlightGradientERK15QLinearGradient(
    QAbstract3DSeriesPrivate *self,
    const QLinearGradient *gradient) {
  self->setMultiHighlightGradient(*gradient);
}

//  void QAbstract3DSeriesPrivate::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate7setNameERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QAbstract3DSeriesPrivate::itemLabel()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QAbstract3DSeriesPrivate9itemLabelEv(
    QAbstract3DSeriesPrivate *self) {
  return new QString(self->itemLabel());
}

//  void QAbstract3DSeriesPrivate::markItemLabelDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv(
    QAbstract3DSeriesPrivate *self) {
  self->markItemLabelDirty();
}

//  bool QAbstract3DSeriesPrivate::itemLabelDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstract3DSeriesPrivate14itemLabelDirtyEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->itemLabelDirty();
}

//  void QAbstract3DSeriesPrivate::setItemLabelVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate19setItemLabelVisibleEb(
    QAbstract3DSeriesPrivate *self,
    bool visible) {
  self->setItemLabelVisible(visible);
}

//  a Python function taken by a CuteQAbstract3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DSeriesPrivate(
    QAbstract3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DSeriesPrivate *>(self)->take(key, call);
}

//  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QAbstract3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QAbstract3DSeriesPrivate::setDataProxy(proxy);
}

//  void QAbstract3DSeriesPrivate::setController(Abstract3DController
//      *controller)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController(
    QAbstract3DSeriesPrivate *self,
    Abstract3DController *controller) {
  self->QAbstract3DSeriesPrivate::setController(controller);
}
