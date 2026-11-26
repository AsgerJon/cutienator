//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qsurface3dseries_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSurface3DSeriesPrivate'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qsurface3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qsurface3dseries_p.h>
#include <QtDataVisualization/private/surface3dcontroller_p.h>
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

//  from QtDataVisualization__QSurface3DSeriesPrivate.cpp, line 1, as moc:QSurface3DSeriesPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QSurface3DSeriesPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSurface3DSeriesPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSurface3DSeriesPrivate, qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSurface3DSeriesPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DSeriesPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>.metaTypes,
    nullptr
} };

void QSurface3DSeriesPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSurface3DSeriesPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QSurface3DSeriesPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSurface3DSeriesPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QSurface3DSeriesPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DSeriesPrivate::qt_metacast(_clname);
}

int QSurface3DSeriesPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DSeriesPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 437, as _ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataTypeSurface);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit qptr()->dataProxyChanged(static_cast<QSurfaceDataProxy *>(proxy));
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 476, as _ZN23QSurface3DSeriesPrivate15createItemLabelEv
inline void QSurface3DSeriesPrivate::createItemLabel()
{
    static const QString xTitleTag(QStringLiteral("@xTitle"));
    static const QString yTitleTag(QStringLiteral("@yTitle"));
    static const QString zTitleTag(QStringLiteral("@zTitle"));
    static const QString xLabelTag(QStringLiteral("@xLabel"));
    static const QString yLabelTag(QStringLiteral("@yLabel"));
    static const QString zLabelTag(QStringLiteral("@zLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedPoint == QSurface3DSeries::invalidSelectionPosition()) {
        m_itemLabel = QString();
        return;
    }

    QValue3DAxis *axisX = static_cast<QValue3DAxis *>(m_controller->axisX());
    QValue3DAxis *axisY = static_cast<QValue3DAxis *>(m_controller->axisY());
    QValue3DAxis *axisZ = static_cast<QValue3DAxis *>(m_controller->axisZ());
    QVector3D selectedPosition = qptr()->dataProxy()->itemAt(m_selectedPoint)->position();

    m_itemLabel = m_itemLabelFormat;

    m_itemLabel.replace(xTitleTag, axisX->title());
    m_itemLabel.replace(yTitleTag, axisY->title());
    m_itemLabel.replace(zTitleTag, axisZ->title());

    if (m_itemLabel.contains(xLabelTag)) {
        QString valueLabelText = axisX->formatter()->stringForValue(
                    qreal(selectedPosition.x()), axisX->labelFormat());
        m_itemLabel.replace(xLabelTag, valueLabelText);
    }
    if (m_itemLabel.contains(yLabelTag)) {
        QString valueLabelText = axisY->formatter()->stringForValue(
                    qreal(selectedPosition.y()), axisY->labelFormat());
        m_itemLabel.replace(yLabelTag, valueLabelText);
    }
    if (m_itemLabel.contains(zLabelTag)) {
        QString valueLabelText = axisZ->formatter()->stringForValue(
                    qreal(selectedPosition.z()), axisZ->labelFormat());
        m_itemLabel.replace(zLabelTag, valueLabelText);
    }
    m_itemLabel.replace(seriesNameTag, m_name);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 446, as _ZN23QSurface3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController
inline void QSurface3DSeriesPrivate::connectControllerAndProxy(Abstract3DController *newController)
{
    QSurfaceDataProxy *surfaceDataProxy = static_cast<QSurfaceDataProxy *>(m_dataProxy);

    if (m_controller && surfaceDataProxy) {
        //Disconnect old controller/old proxy
        QObject::disconnect(surfaceDataProxy, 0, m_controller, 0);
        QObject::disconnect(q_ptr, 0, m_controller, 0);
    }

    if (newController && surfaceDataProxy) {
        Surface3DController *controller = static_cast<Surface3DController *>(newController);

        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::arrayReset, controller,
                         &Surface3DController::handleArrayReset);
        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::rowsAdded, controller,
                         &Surface3DController::handleRowsAdded);
        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::rowsChanged, controller,
                         &Surface3DController::handleRowsChanged);
        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::rowsRemoved, controller,
                         &Surface3DController::handleRowsRemoved);
        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::rowsInserted, controller,
                         &Surface3DController::handleRowsInserted);
        QObject::connect(surfaceDataProxy, &QSurfaceDataProxy::itemChanged, controller,
                         &Surface3DController::handleItemChanged);
        QObject::connect(qptr(), &QSurface3DSeries::dataProxyChanged, controller,
                         &Surface3DController::handleArrayReset);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 428, as _ZN23QSurface3DSeriesPrivateD0Ev
inline QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 680, as _ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController
inline void QAbstract3DSeriesPrivate::setController(Abstract3DController *controller)
{
    connectControllerAndProxy(controller);
    m_controller = controller;
    q_ptr->setParent(controller);
    markItemLabelDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 637, as _ZN24QAbstract3DSeriesPrivateC2EP17QAbstract3DSeriesNS0_10SeriesTypeE
inline QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(QAbstract3DSeries *q,
                                                   QAbstract3DSeries::SeriesType type)
    : QObject(0),
      q_ptr(q),
      m_type(type),
      m_dataProxy(0),
      m_visible(true),
      m_controller(0),
      m_mesh(QAbstract3DSeries::MeshCube),
      m_meshSmooth(false),
      m_colorStyle(Q3DTheme::ColorStyleUniform),
      m_baseColor(Qt::black),
      m_singleHighlightColor(Qt::black),
      m_multiHighlightColor(Qt::black),
      m_itemLabelDirty(true),
      m_itemLabelVisible(true)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 656, as _ZN24QAbstract3DSeriesPrivateD2Ev
inline QAbstract3DSeriesPrivate::~QAbstract3DSeriesPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstract3dseries.cpp, line 865, as _ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv
inline void QAbstract3DSeriesPrivate::markItemLabelDirty()
{
    m_itemLabelDirty = true;
    m_changeTracker.itemLabelChanged = true;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

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

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 417, as _ZN23QSurface3DSeriesPrivateC1EP16QSurface3DSeries
inline QSurface3DSeriesPrivate::QSurface3DSeriesPrivate(QSurface3DSeries *q)
    : QAbstract3DSeriesPrivate(q, QAbstract3DSeries::SeriesTypeSurface),
      m_selectedPoint(Surface3DController::invalidSelectionPosition()),
      m_flatShadingEnabled(true),
      m_drawMode(QSurface3DSeries::DrawSurfaceAndWireframe),
      m_wireframeColor(Qt::black)
{
    m_itemLabelFormat = QStringLiteral("@xLabel, @yLabel, @zLabel");
    m_mesh = QAbstract3DSeries::MeshSphere;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 520, as _ZN23QSurface3DSeriesPrivate16setSelectedPointERK6QPoint
inline void QSurface3DSeriesPrivate::setSelectedPoint(const QPoint &position)
{
    if (position != m_selectedPoint) {
        markItemLabelDirty();
        m_selectedPoint = position;
        emit qptr()->selectedPointChanged(m_selectedPoint);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 529, as _ZN23QSurface3DSeriesPrivate21setFlatShadingEnabledEb
inline void QSurface3DSeriesPrivate::setFlatShadingEnabled(bool enabled)
{
    m_flatShadingEnabled = enabled;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 536, as _ZN23QSurface3DSeriesPrivate11setDrawModeE6QFlagsIN16QSurface3DSeries8DrawFlagEE
inline void QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags mode)
{
    if (mode.testFlag(QSurface3DSeries::DrawWireframe)
            || mode.testFlag(QSurface3DSeries::DrawSurface)) {
        m_drawMode = mode;
        if (m_controller)
            m_controller->markSeriesVisualsDirty();
    } else {
        qWarning("You may not clear all draw flags. Mode not changed.");
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 548, as _ZN23QSurface3DSeriesPrivate10setTextureERK6QImage
inline void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
{
    m_texture = texture;
    if (static_cast<Surface3DController *>(m_controller))
        static_cast<Surface3DController *>(m_controller)->updateSurfaceTexture(qptr());
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 555, as _ZN23QSurface3DSeriesPrivate17setWireframeColorERK6QColor
inline void QSurface3DSeriesPrivate::setWireframeColor(const QColor &color)
{
    m_wireframeColor = color;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurface3dseries.cpp, line 432, as _ZN23QSurface3DSeriesPrivate4qptrEv
inline QSurface3DSeries *QSurface3DSeriesPrivate::qptr()
{
    return static_cast<QSurface3DSeries *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QSurface3DSeriesPrivate that Python can take functions over in. Every QSurface3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSurface3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall1)(const void *, Abstract3DController *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall3)(const void *, Abstract3DController *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurface3DSeriesPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurface3DSeriesPrivateCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesPrivateCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesPrivateCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurface3DSeriesPrivateCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurface3DSeriesPrivate : public QSurface3DSeriesPrivate {
public:
  using QSurface3DSeriesPrivate::QSurface3DSeriesPrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate15createItemLabelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate13setControllerEP20Abstract3DController")) {
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

  //  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall0 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QSurface3DSeriesPrivate::connectControllerAndProxy(Abstract3DCon
  //      troller *newController)
  void connectControllerAndProxy(
      Abstract3DController *newController) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall1 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall1>(taken[1]);
      call(this, newController, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::connectControllerAndProxy(newController);
  }

  //  void QSurface3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall2 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setController(Abstract3DController
  //      *controller)
  void setController(Abstract3DController *controller) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall3 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall3>(taken[3]);
      call(this, controller, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setController(controller);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall4 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall4>(taken[4]);
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
      CuteQSurface3DSeriesPrivateCall5 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall5>(taken[5]);
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
      CuteQSurface3DSeriesPrivateCall6 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall6>(taken[6]);
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
      CuteQSurface3DSeriesPrivateCall7 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall7>(taken[7]);
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
      CuteQSurface3DSeriesPrivateCall8 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall8>(taken[8]);
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
      CuteQSurface3DSeriesPrivateCall9 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall9>(taken[9]);
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
      CuteQSurface3DSeriesPrivateCall10 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurface3DSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QSurface3DSeriesPrivate10metaObjectEv(
    const QSurface3DSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QSurface3DSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QSurface3DSeriesPrivate11qt_metacastEPKc(
    QSurface3DSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSurface3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QSurface3DSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QSurface3DSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSurface3DSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QSurface3DSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurface3DSeriesPrivate::tr(s, c, n));
}

//  QSurface3DSeriesPrivate::QSurface3DSeriesPrivate(QSurface3DSeries *q)
extern "C" Q_DECL_EXPORT
QSurface3DSeriesPrivate *ritual_ZN23QSurface3DSeriesPrivateC1EP16QSurface3DSeries(
    QSurface3DSeries *q) {
  return new CuteQSurface3DSeriesPrivate(q);
}

//  QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivateD1Ev(QSurface3DSeriesPrivate *self) {
  delete self;
}

//  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QSurface3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void
//      QSurface3DSeriesPrivate::connectControllerAndProxy(Abstract3DControll
//      er *newController)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QSurface3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->connectControllerAndProxy(newController);
}

//  void QSurface3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate15createItemLabelEv(
    QSurface3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QSurface3DSeriesPrivate::setSelectedPoint(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate16setSelectedPointERK6QPoint(
    QSurface3DSeriesPrivate *self,
    const QPoint *position) {
  self->setSelectedPoint(*position);
}

//  void QSurface3DSeriesPrivate::setFlatShadingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate21setFlatShadingEnabledEb(
    QSurface3DSeriesPrivate *self,
    bool enabled) {
  self->setFlatShadingEnabled(enabled);
}

//  void QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate11setDrawModeE6QFlagsIN16QSurface3DSeries8DrawFlagEE(
    QSurface3DSeriesPrivate *self,
    int mode) {
  self->setDrawMode(QFlags<QSurface3DSeries::DrawFlag>::fromInt(mode));
}

//  void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10setTextureERK6QImage(
    QSurface3DSeriesPrivate *self,
    const QImage *texture) {
  self->setTexture(*texture);
}

//  void QSurface3DSeriesPrivate::setWireframeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate17setWireframeColorERK6QColor(
    QSurface3DSeriesPrivate *self,
    const QColor *color) {
  self->setWireframeColor(*color);
}

//  QSurface3DSeries *QSurface3DSeriesPrivate::qptr()
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZN23QSurface3DSeriesPrivate4qptrEv(
    QSurface3DSeriesPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQSurface3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurface3DSeriesPrivate(
    QSurface3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurface3DSeriesPrivate *>(self)->take(key, call);
}

//  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QSurface3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QSurface3DSeriesPrivate::setDataProxy(proxy);
}

//  void
//      QSurface3DSeriesPrivate::connectControllerAndProxy(Abstract3DControll
//      er *newController)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QSurface3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->QSurface3DSeriesPrivate::connectControllerAndProxy(newController);
}

//  void QSurface3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate15createItemLabelEv(
    QSurface3DSeriesPrivate *self) {
  self->QSurface3DSeriesPrivate::createItemLabel();
}
