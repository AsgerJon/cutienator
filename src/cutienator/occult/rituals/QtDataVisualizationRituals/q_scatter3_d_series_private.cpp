//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qscatter3dseries_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QScatter3DSeriesPrivate'
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
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qscatter3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qscatter3dseries_p.h>
#include <QtDataVisualization/private/scatter3dcontroller_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QScatter3DSeriesPrivate.cpp, line 1, as moc:QScatter3DSeriesPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QScatter3DSeriesPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QScatter3DSeriesPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QScatter3DSeriesPrivate, qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QScatter3DSeriesPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DSeriesPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>.metaTypes,
    nullptr
} };

void QScatter3DSeriesPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QScatter3DSeriesPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QScatter3DSeriesPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QScatter3DSeriesPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QScatter3DSeriesPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DSeriesPrivate::qt_metacast(_clname);
}

int QScatter3DSeriesPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DSeriesPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 273, as _ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataTypeScatter);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit qptr()->dataProxyChanged(static_cast<QScatterDataProxy *>(proxy));
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 309, as _ZN23QScatter3DSeriesPrivate15createItemLabelEv
inline void QScatter3DSeriesPrivate::createItemLabel()
{
    static const QString xTitleTag(QStringLiteral("@xTitle"));
    static const QString yTitleTag(QStringLiteral("@yTitle"));
    static const QString zTitleTag(QStringLiteral("@zTitle"));
    static const QString xLabelTag(QStringLiteral("@xLabel"));
    static const QString yLabelTag(QStringLiteral("@yLabel"));
    static const QString zLabelTag(QStringLiteral("@zLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedItem == QScatter3DSeries::invalidSelectionIndex()) {
        m_itemLabel = QString();
        return;
    }

    QValue3DAxis *axisX = static_cast<QValue3DAxis *>(m_controller->axisX());
    QValue3DAxis *axisY = static_cast<QValue3DAxis *>(m_controller->axisY());
    QValue3DAxis *axisZ = static_cast<QValue3DAxis *>(m_controller->axisZ());
    QVector3D selectedPosition = qptr()->dataProxy()->itemAt(m_selectedItem)->position();

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

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 282, as _ZN23QScatter3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController
inline void QScatter3DSeriesPrivate::connectControllerAndProxy(Abstract3DController *newController)
{
    QScatterDataProxy *scatterDataProxy = static_cast<QScatterDataProxy *>(m_dataProxy);

    if (m_controller && scatterDataProxy) {
        //Disconnect old controller/old proxy
        QObject::disconnect(scatterDataProxy, 0, m_controller, 0);
        QObject::disconnect(q_ptr, 0, m_controller, 0);
    }

    if (newController && scatterDataProxy) {
        Scatter3DController *controller = static_cast<Scatter3DController *>(newController);
        QObject::connect(scatterDataProxy, &QScatterDataProxy::arrayReset,
                         controller, &Scatter3DController::handleArrayReset);
        QObject::connect(scatterDataProxy, &QScatterDataProxy::itemsAdded,
                         controller, &Scatter3DController::handleItemsAdded);
        QObject::connect(scatterDataProxy, &QScatterDataProxy::itemsChanged,
                         controller, &Scatter3DController::handleItemsChanged);
        QObject::connect(scatterDataProxy, &QScatterDataProxy::itemsRemoved,
                         controller, &Scatter3DController::handleItemsRemoved);
        QObject::connect(scatterDataProxy, &QScatterDataProxy::itemsInserted,
                         controller, &Scatter3DController::handleItemsInserted);
        QObject::connect(qptr(), &QScatter3DSeries::dataProxyChanged,
                         controller, &Scatter3DController::handleArrayReset);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 264, as _ZN23QScatter3DSeriesPrivateD0Ev
inline QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()
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

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 255, as _ZN23QScatter3DSeriesPrivateC1EP16QScatter3DSeries
inline QScatter3DSeriesPrivate::QScatter3DSeriesPrivate(QScatter3DSeries *q)
    : QAbstract3DSeriesPrivate(q, QAbstract3DSeries::SeriesTypeScatter),
      m_selectedItem(Scatter3DController::invalidSelectionIndex()),
      m_itemSize(0.0f)
{
    m_itemLabelFormat = QStringLiteral("@xLabel, @yLabel, @zLabel");
    m_mesh = QAbstract3DSeries::MeshSphere;
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 353, as _ZN23QScatter3DSeriesPrivate15setSelectedItemEi
inline void QScatter3DSeriesPrivate::setSelectedItem(int index)
{
    if (index != m_selectedItem) {
        markItemLabelDirty();
        m_selectedItem = index;
        emit qptr()->selectedItemChanged(m_selectedItem);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 362, as _ZN23QScatter3DSeriesPrivate11setItemSizeEf
inline void QScatter3DSeriesPrivate::setItemSize(float size)
{
    m_itemSize = size;
    if (m_controller)
        m_controller->markSeriesVisualsDirty();
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatter3dseries.cpp, line 268, as _ZN23QScatter3DSeriesPrivate4qptrEv
inline QScatter3DSeries *QScatter3DSeriesPrivate::qptr()
{
    return static_cast<QScatter3DSeries *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QScatter3DSeriesPrivate that Python can take functions over in. Every QScatter3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScatter3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall1)(const void *, Abstract3DController *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall3)(const void *, Abstract3DController *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatter3DSeriesPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatter3DSeriesPrivateCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesPrivateCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesPrivateCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesPrivateCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesPrivateCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatter3DSeriesPrivate : public QScatter3DSeriesPrivate {
public:
  using QScatter3DSeriesPrivate::QScatter3DSeriesPrivate;
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

  //  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall0 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QScatter3DSeriesPrivate::connectControllerAndProxy(Abstract3DCon
  //      troller *newController)
  void connectControllerAndProxy(
      Abstract3DController *newController) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall1 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall1>(taken[1]);
      call(this, newController, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::connectControllerAndProxy(newController);
  }

  //  void QScatter3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall2 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setController(Abstract3DController
  //      *controller)
  void setController(Abstract3DController *controller) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall3 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall3>(taken[3]);
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
      CuteQScatter3DSeriesPrivateCall4 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall4>(taken[4]);
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
      CuteQScatter3DSeriesPrivateCall5 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall5>(taken[5]);
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
      CuteQScatter3DSeriesPrivateCall6 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall6>(taken[6]);
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
      CuteQScatter3DSeriesPrivateCall7 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall7>(taken[7]);
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
      CuteQScatter3DSeriesPrivateCall8 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall8>(taken[8]);
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
      CuteQScatter3DSeriesPrivateCall9 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall9>(taken[9]);
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
      CuteQScatter3DSeriesPrivateCall10 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatter3DSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QScatter3DSeriesPrivate10metaObjectEv(
    const QScatter3DSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QScatter3DSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QScatter3DSeriesPrivate11qt_metacastEPKc(
    QScatter3DSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScatter3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QScatter3DSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QScatter3DSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScatter3DSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QScatter3DSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScatter3DSeriesPrivate::tr(s, c, n));
}

//  QScatter3DSeriesPrivate::QScatter3DSeriesPrivate(QScatter3DSeries *q)
extern "C" Q_DECL_EXPORT
QScatter3DSeriesPrivate *ritual_ZN23QScatter3DSeriesPrivateC1EP16QScatter3DSeries(
    QScatter3DSeries *q) {
  return new CuteQScatter3DSeriesPrivate(q);
}

//  QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivateD1Ev(QScatter3DSeriesPrivate *self) {
  delete self;
}

//  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QScatter3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void
//      QScatter3DSeriesPrivate::connectControllerAndProxy(Abstract3DControll
//      er *newController)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QScatter3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->connectControllerAndProxy(newController);
}

//  void QScatter3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate15createItemLabelEv(
    QScatter3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QScatter3DSeriesPrivate::setSelectedItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate15setSelectedItemEi(
    QScatter3DSeriesPrivate *self,
    int index) {
  self->setSelectedItem(index);
}

//  void QScatter3DSeriesPrivate::setItemSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate11setItemSizeEf(
    QScatter3DSeriesPrivate *self,
    float size) {
  self->setItemSize(size);
}

//  QScatter3DSeries *QScatter3DSeriesPrivate::qptr()
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN23QScatter3DSeriesPrivate4qptrEv(
    QScatter3DSeriesPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQScatter3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatter3DSeriesPrivate(
    QScatter3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatter3DSeriesPrivate *>(self)->take(key, call);
}

//  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QScatter3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QScatter3DSeriesPrivate::setDataProxy(proxy);
}

//  void
//      QScatter3DSeriesPrivate::connectControllerAndProxy(Abstract3DControll
//      er *newController)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate25connectControllerAndProxyEP20Abstract3DController(
    QScatter3DSeriesPrivate *self,
    Abstract3DController *newController) {
  self->QScatter3DSeriesPrivate::connectControllerAndProxy(newController);
}

//  void QScatter3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate15createItemLabelEv(
    QScatter3DSeriesPrivate *self) {
  self->QScatter3DSeriesPrivate::createItemLabel();
}
