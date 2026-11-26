//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/qbar3dseries_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QBar3DSeriesPrivate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qbar3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qbar3dseries_p.h>
#include <QtDataVisualization/private/bars3dcontroller_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
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

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 236, as local:qbar3dseries.cpp:quaternionAngle
static inline float quaternionAngle(const QQuaternion &rotation)
{
    return qRadiansToDegrees(qAcos(rotation.scalar())) * 2.f;
}

//  from QtDataVisualization__QBar3DSeriesPrivate.cpp, line 1, as moc:QBar3DSeriesPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QBar3DSeriesPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QBar3DSeriesPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QBar3DSeriesPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QBar3DSeriesPrivate, qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QBar3DSeriesPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DSeriesPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>.metaTypes,
    nullptr
} };

void QBar3DSeriesPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QBar3DSeriesPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QBar3DSeriesPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QBar3DSeriesPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QBar3DSeriesPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DSeriesPrivate::qt_metacast(_clname);
}

int QBar3DSeriesPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DSeriesPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 329, as _ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataTypeBar);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit qptr()->dataProxyChanged(static_cast<QBarDataProxy *>(proxy));
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 373, as _ZN19QBar3DSeriesPrivate15createItemLabelEv
inline void QBar3DSeriesPrivate::createItemLabel()
{
    static const QString rowIndexTag(QStringLiteral("@rowIdx"));
    static const QString rowLabelTag(QStringLiteral("@rowLabel"));
    static const QString rowTitleTag(QStringLiteral("@rowTitle"));
    static const QString colIndexTag(QStringLiteral("@colIdx"));
    static const QString colLabelTag(QStringLiteral("@colLabel"));
    static const QString colTitleTag(QStringLiteral("@colTitle"));
    static const QString valueTitleTag(QStringLiteral("@valueTitle"));
    static const QString valueLabelTag(QStringLiteral("@valueLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedBar == QBar3DSeries::invalidSelectionPosition()) {
        m_itemLabel = QString();
        return;
    }

    QLocale locale(QLocale::c());
    if (m_controller)
        locale = m_controller->locale();

    QCategory3DAxis *categoryAxisZ = static_cast<QCategory3DAxis *>(m_controller->axisZ());
    QCategory3DAxis *categoryAxisX = static_cast<QCategory3DAxis *>(m_controller->axisX());
    QValue3DAxis *valueAxis = static_cast<QValue3DAxis *>(m_controller->axisY());
    qreal selectedBarValue = qreal(qptr()->dataProxy()->itemAt(m_selectedBar)->value());

    // Custom format expects printf format specifier. There is no tag for it.
    m_itemLabel = valueAxis->formatter()->stringForValue(selectedBarValue, m_itemLabelFormat);

    int selBarPosRow = m_selectedBar.x();
    int selBarPosCol = m_selectedBar.y();
    m_itemLabel.replace(rowIndexTag, locale.toString(selBarPosRow));
    if (categoryAxisZ->labels().size() > selBarPosRow)
        m_itemLabel.replace(rowLabelTag, categoryAxisZ->labels().at(selBarPosRow));
    else
        m_itemLabel.replace(rowLabelTag, QString());
    m_itemLabel.replace(rowTitleTag, categoryAxisZ->title());
    m_itemLabel.replace(colIndexTag, locale.toString(selBarPosCol));
    if (categoryAxisX->labels().size() > selBarPosCol)
        m_itemLabel.replace(colLabelTag, categoryAxisX->labels().at(selBarPosCol));
    else
        m_itemLabel.replace(colLabelTag, QString());
    m_itemLabel.replace(colTitleTag, categoryAxisX->title());
    m_itemLabel.replace(valueTitleTag, valueAxis->title());

    if (m_itemLabel.contains(valueLabelTag)) {
        QString valueLabelText = valueAxis->formatter()->stringForValue(selectedBarValue,
                                                                        valueAxis->labelFormat());
        m_itemLabel.replace(valueLabelTag, valueLabelText);
    }

    m_itemLabel.replace(seriesNameTag, m_name);
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 338, as _ZN19QBar3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController
inline void QBar3DSeriesPrivate::connectControllerAndProxy(Abstract3DController *newController)
{
    QBarDataProxy *barDataProxy = static_cast<QBarDataProxy *>(m_dataProxy);

    if (m_controller && barDataProxy) {
        // Disconnect old controller/old proxy
        QObject::disconnect(barDataProxy, 0, m_controller, 0);
        QObject::disconnect(q_ptr, 0, m_controller, 0);
    }

    if (newController && barDataProxy) {
        Bars3DController *controller = static_cast<Bars3DController *>(newController);
        QObject::connect(barDataProxy, &QBarDataProxy::arrayReset, controller,
                         &Bars3DController::handleArrayReset);
        QObject::connect(barDataProxy, &QBarDataProxy::rowsAdded, controller,
                         &Bars3DController::handleRowsAdded);
        QObject::connect(barDataProxy, &QBarDataProxy::rowsChanged, controller,
                         &Bars3DController::handleRowsChanged);
        QObject::connect(barDataProxy, &QBarDataProxy::rowsRemoved, controller,
                         &Bars3DController::handleRowsRemoved);
        QObject::connect(barDataProxy, &QBarDataProxy::rowsInserted, controller,
                         &Bars3DController::handleRowsInserted);
        QObject::connect(barDataProxy, &QBarDataProxy::itemChanged, controller,
                         &Bars3DController::handleItemChanged);
        QObject::connect(barDataProxy, &QBarDataProxy::rowLabelsChanged, controller,
                         &Bars3DController::handleDataRowLabelsChanged);
        QObject::connect(barDataProxy, &QBarDataProxy::columnLabelsChanged, controller,
                         &Bars3DController::handleDataColumnLabelsChanged);
        QObject::connect(qptr(), &QBar3DSeries::dataProxyChanged, controller,
                         &Bars3DController::handleArrayReset);
        QObject::connect(qptr(), &QBar3DSeries::rowColorsChanged, controller,
                         &Bars3DController::handleRowColorsChanged);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 320, as _ZN19QBar3DSeriesPrivateD0Ev
inline QBar3DSeriesPrivate::~QBar3DSeriesPrivate()
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

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 312, as _ZN19QBar3DSeriesPrivateC1EP12QBar3DSeries
inline QBar3DSeriesPrivate::QBar3DSeriesPrivate(QBar3DSeries *q)
    : QAbstract3DSeriesPrivate(q, QAbstract3DSeries::SeriesTypeBar),
      m_selectedBar(Bars3DController::invalidSelectionPosition())
{
    m_itemLabelFormat = QStringLiteral("@valueLabel");
    m_mesh = QAbstract3DSeries::MeshBevelBar;
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 427, as _ZN19QBar3DSeriesPrivate25handleMeshRotationChangedERK11QQuaternion
inline void QBar3DSeriesPrivate::handleMeshRotationChanged(const QQuaternion &rotation)
{
    emit qptr()->meshAngleChanged(quaternionAngle(rotation));
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 432, as _ZN19QBar3DSeriesPrivate14setSelectedBarERK6QPoint
inline void QBar3DSeriesPrivate::setSelectedBar(const QPoint &position)
{
    if (position != m_selectedBar) {
        markItemLabelDirty();
        m_selectedBar = position;
        emit qptr()->selectedBarChanged(m_selectedBar);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 441, as _ZN19QBar3DSeriesPrivate14connectSignalsEv
inline void QBar3DSeriesPrivate::connectSignals()
{
    QObject::connect(q_ptr, &QAbstract3DSeries::meshRotationChanged, this,
                     &QBar3DSeriesPrivate::handleMeshRotationChanged);
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 447, as _ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE
inline void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
{
    if (m_rowColors != colors) {
        m_rowColors = colors;
        emit qptr()->rowColorsChanged(m_rowColors);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qbar3dseries.cpp, line 324, as _ZN19QBar3DSeriesPrivate4qptrEv
inline QBar3DSeries *QBar3DSeriesPrivate::qptr()
{
    return static_cast<QBar3DSeries *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QBar3DSeriesPrivate that Python can take functions over in. Every QBar3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBar3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall1)(const void *, Abstract3DController *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall3)(const void *, Abstract3DController *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBar3DSeriesPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBar3DSeriesPrivateCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesPrivateCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesPrivateCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesPrivateCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBar3DSeriesPrivate : public QBar3DSeriesPrivate {
public:
  using QBar3DSeriesPrivate::QBar3DSeriesPrivate;
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

  //  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall0 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void
  //      QBar3DSeriesPrivate::connectControllerAndProxy(Abstract3DControll
  //      er *newController)
  void connectControllerAndProxy(
      Abstract3DController *newController) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall1 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall1>(taken[1]);
      call(this, newController, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::connectControllerAndProxy(newController);
  }

  //  void QBar3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall2 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setController(Abstract3DController
  //      *controller)
  void setController(Abstract3DController *controller) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall3 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall3>(taken[3]);
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
      CuteQBar3DSeriesPrivateCall4 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall4>(taken[4]);
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
      CuteQBar3DSeriesPrivateCall5 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall5>(taken[5]);
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
      CuteQBar3DSeriesPrivateCall6 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall6>(taken[6]);
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
      CuteQBar3DSeriesPrivateCall7 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall7>(taken[7]);
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
      CuteQBar3DSeriesPrivateCall8 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall8>(taken[8]);
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
      CuteQBar3DSeriesPrivateCall9 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall9>(taken[9]);
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
      CuteQBar3DSeriesPrivateCall10 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBar3DSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QBar3DSeriesPrivate10metaObjectEv(
    const QBar3DSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QBar3DSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QBar3DSeriesPrivate11qt_metacastEPKc(
    QBar3DSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBar3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QBar3DSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBar3DSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBar3DSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QBar3DSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBar3DSeriesPrivate::tr(s, c, n));
}

//  QBar3DSeriesPrivate::QBar3DSeriesPrivate(QBar3DSeries *q)
extern "C" Q_DECL_EXPORT
QBar3DSeriesPrivate *ritual_ZN19QBar3DSeriesPrivateC1EP12QBar3DSeries(
    QBar3DSeries *q) {
  return new CuteQBar3DSeriesPrivate(q);
}

//  QBar3DSeriesPrivate::~QBar3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivateD1Ev(QBar3DSeriesPrivate *self) {
  delete self;
}

//  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QBar3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QBar3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
//      *newController)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QBar3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->connectControllerAndProxy(newController);
}

//  void QBar3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate15createItemLabelEv(
    QBar3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QBar3DSeriesPrivate::handleMeshRotationChanged(const QQuaternion
//      &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate25handleMeshRotationChangedERK11QQuaternion(
    QBar3DSeriesPrivate *self,
    const QQuaternion *rotation) {
  self->handleMeshRotationChanged(*rotation);
}

//  void QBar3DSeriesPrivate::setSelectedBar(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate14setSelectedBarERK6QPoint(
    QBar3DSeriesPrivate *self,
    const QPoint *position) {
  self->setSelectedBar(*position);
}

//  void QBar3DSeriesPrivate::connectSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate14connectSignalsEv(
    QBar3DSeriesPrivate *self) {
  self->connectSignals();
}

//  void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE(
    QBar3DSeriesPrivate *self,
    const QList<QColor> *colors) {
  self->setRowColors(*colors);
}

//  QBar3DSeries *QBar3DSeriesPrivate::qptr()
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN19QBar3DSeriesPrivate4qptrEv(
    QBar3DSeriesPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQBar3DSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBar3DSeriesPrivate(
    QBar3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBar3DSeriesPrivate *>(self)->take(key, call);
}

//  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QBar3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QBar3DSeriesPrivate::setDataProxy(proxy);
}

//  void QBar3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
//      *newController)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QBar3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->QBar3DSeriesPrivate::connectControllerAndProxy(newController);
}

//  void QBar3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate15createItemLabelEv(
    QBar3DSeriesPrivate *self) {
  self->QBar3DSeriesPrivate::createItemLabel();
}
