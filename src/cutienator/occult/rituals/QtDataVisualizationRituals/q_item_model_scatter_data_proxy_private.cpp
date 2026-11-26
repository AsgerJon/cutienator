//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qitemmodelscatterdataproxy_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QItemModelScatterDataProxyPrivate' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 3 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qitemmodelscatterdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qscatterdataproxy_p.h>
#include <QtDataVisualization/private/qscatter3dseries_p.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#include <QtDataVisualization/private/qitemmodelscatterdataproxy_p.h>
#include <QtDataVisualization/private/scatteritemmodelhandler_p.h>
#include <QtDataVisualization/private/scatteritemmodelhandler_p.h>
#include <QtGui/qquaternion.h>
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#include <QtDataVisualization/private/abstractitemmodelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QItemModelScatterDataProxyPrivate.cpp, line 1, as moc:QItemModelScatterDataProxyPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QItemModelScatterDataProxyPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QItemModelScatterDataProxyPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QItemModelScatterDataProxyPrivate, qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QItemModelScatterDataProxyPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QScatterDataProxyPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>.metaTypes,
    nullptr
} };

void QItemModelScatterDataProxyPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QItemModelScatterDataProxyPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QItemModelScatterDataProxyPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QItemModelScatterDataProxyPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelScatterDataProxyPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QScatterDataProxyPrivate::qt_metacast(_clname);
}

int QItemModelScatterDataProxyPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QScatterDataProxyPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 416, as _ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QScatter3DSeries *scatterSeries = static_cast<QScatter3DSeries *>(series);
    emit qptr()->seriesChanged(scatterSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelscatterdataproxy.cpp, line 584, as _ZN33QItemModelScatterDataProxyPrivateD0Ev
inline QItemModelScatterDataProxyPrivate::~QItemModelScatterDataProxyPrivate()
{
    delete m_itemModelHandler;
}

//  from ../qtdatavis3d/src/datavisualization/data/scatteritemmodelhandler.cpp, line 10, as _ZN23ScatterItemModelHandlerC1EP26QItemModelScatterDataProxyP7QObject
inline ScatterItemModelHandler::ScatterItemModelHandler(QItemModelScatterDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent),
      m_proxy(proxy),
      m_proxyArray(0),
      m_xPosRole(noRoleIndex),
      m_yPosRole(noRoleIndex),
      m_zPosRole(noRoleIndex),
      m_rotationRole(noRoleIndex),
      m_haveXPosPattern(false),
      m_haveYPosPattern(false),
      m_haveZPosPattern(false),
      m_haveRotationPattern(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 281, as _ZN24QScatterDataProxyPrivateC2EP17QScatterDataProxy
inline QScatterDataProxyPrivate::QScatterDataProxyPrivate(QScatterDataProxy *q)
    : QAbstractDataProxyPrivate(q, QAbstractDataProxy::DataTypeScatter),
      m_dataArray(new QScatterDataArray)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 287, as _ZN24QScatterDataProxyPrivateD2Ev
inline QScatterDataProxyPrivate::~QScatterDataProxyPrivate()
{
    m_dataArray->clear();
    delete m_dataArray;
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 423, as _ZN24QScatterDataProxyPrivate4qptrEv
inline QScatterDataProxy *QScatterDataProxyPrivate::qptr()
{
    return static_cast<QScatterDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 97, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    q_ptr->setParent(series);
    m_series = series;
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 93, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 8, as _ZN24AbstractItemModelHandlerC2EP7QObject
inline AbstractItemModelHandler::AbstractItemModelHandler(QObject *parent)
    : QObject(parent),
      resolvePending(0),
      m_fullReset(true)
{
    m_resolveTimer.setSingleShot(true);
    QObject::connect(&m_resolveTimer, &QTimer::timeout,
                     this, &AbstractItemModelHandler::handlePendingResolve);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractitemmodelhandler.cpp, line 18, as _ZN24AbstractItemModelHandlerD2Ev
inline AbstractItemModelHandler::~AbstractItemModelHandler()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 84, as _ZN25QAbstractDataProxyPrivateC2EP18QAbstractDataProxyNS0_8DataTypeE
inline QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(QAbstractDataProxy *q,
                                                     QAbstractDataProxy::DataType type)
    : QObject(0),
      q_ptr(q),
      m_type(type),
      m_series(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelscatterdataproxy.cpp, line 578, as _ZN33QItemModelScatterDataProxyPrivateC1EP26QItemModelScatterDataProxy
inline QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPrivate(QItemModelScatterDataProxy *q)
    : QScatterDataProxyPrivate(q),
      m_itemModelHandler(new ScatterItemModelHandler(q))
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelscatterdataproxy.cpp, line 594, as _ZN33QItemModelScatterDataProxyPrivate23connectItemModelHandlerEv
inline void QItemModelScatterDataProxyPrivate::connectItemModelHandler()
{
    QObject::connect(m_itemModelHandler, &ScatterItemModelHandler::itemModelChanged,
                     qptr(), &QItemModelScatterDataProxy::itemModelChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::xPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::yPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::zPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::rotationRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::xPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::yPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::zPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::rotationRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::xPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::yPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::zPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelScatterDataProxy::rotationRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelscatterdataproxy.cpp, line 589, as _ZN33QItemModelScatterDataProxyPrivate4qptrEv
inline QItemModelScatterDataProxy *QItemModelScatterDataProxyPrivate::qptr()
{
    return static_cast<QItemModelScatterDataProxy *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QItemModelScatterDataProxyPrivate that Python can take functions over in. Every QItemModelScatterDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQItemModelScatterDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelScatterDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelScatterDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelScatterDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemModelScatterDataProxyPrivate : public QItemModelScatterDataProxyPrivate {
public:
  using QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall0 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QScatterDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall1 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall2 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall3 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall4 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall5 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall6 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall7 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemModelScatterDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QItemModelScatterDataProxyPrivate10metaObjectEv(
    const QItemModelScatterDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QItemModelScatterDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QItemModelScatterDataProxyPrivate11qt_metacastEPKc(
    QItemModelScatterDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QItemModelScatterDataProxyPrivate::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QItemModelScatterDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QItemModelScatterDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QItemModelScatterDataProxyPrivate::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QItemModelScatterDataProxyPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemModelScatterDataProxyPrivate::tr(s, c, n));
}

//  QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPrivate(QIte
//      mModelScatterDataProxy *q)
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxyPrivate *ritual_ZN33QItemModelScatterDataProxyPrivateC1EP26QItemModelScatterDataProxy(
    QItemModelScatterDataProxy *q) {
  return new CuteQItemModelScatterDataProxyPrivate(q);
}

//  QItemModelScatterDataProxyPrivate::~QItemModelScatterDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelScatterDataProxyPrivateD1Ev(
    QItemModelScatterDataProxyPrivate *self) {
  delete self;
}

//  void QItemModelScatterDataProxyPrivate::connectItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelScatterDataProxyPrivate23connectItemModelHandlerEv(
    QItemModelScatterDataProxyPrivate *self) {
  self->connectItemModelHandler();
}

//  QItemModelScatterDataProxy *QItemModelScatterDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN33QItemModelScatterDataProxyPrivate4qptrEv(
    QItemModelScatterDataProxyPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQItemModelScatterDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelScatterDataProxyPrivate(
    QItemModelScatterDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelScatterDataProxyPrivate *>(self)->take(key, call);
}
