//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qitemmodelsurfacedataproxy_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QItemModelSurfaceDataProxyPrivate' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 3 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qitemmodelsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qsurfacedataproxy_p.h>
#include <QtDataVisualization/private/qsurface3dseries_p.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#include <QtDataVisualization/private/qitemmodelsurfacedataproxy_p.h>
#include <QtDataVisualization/private/surfaceitemmodelhandler_p.h>
#include <QtDataVisualization/private/surfaceitemmodelhandler_p.h>
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

//  from QtDataVisualization__QItemModelSurfaceDataProxyPrivate.cpp, line 1, as moc:QItemModelSurfaceDataProxyPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QItemModelSurfaceDataProxyPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QItemModelSurfaceDataProxyPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QItemModelSurfaceDataProxyPrivate, qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QItemModelSurfaceDataProxyPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QSurfaceDataProxyPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>.metaTypes,
    nullptr
} };

void QItemModelSurfaceDataProxyPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QItemModelSurfaceDataProxyPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QItemModelSurfaceDataProxyPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QItemModelSurfaceDataProxyPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN33QItemModelSurfaceDataProxyPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QSurfaceDataProxyPrivate::qt_metacast(_clname);
}

int QItemModelSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSurfaceDataProxyPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 636, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit qptr()->seriesChanged(surfaceSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelsurfacedataproxy.cpp, line 1043, as _ZN33QItemModelSurfaceDataProxyPrivateD0Ev
inline QItemModelSurfaceDataProxyPrivate::~QItemModelSurfaceDataProxyPrivate()
{
    delete m_itemModelHandler;
}

//  from ../qtdatavis3d/src/datavisualization/data/surfaceitemmodelhandler.cpp, line 8, as _ZN23SurfaceItemModelHandlerC1EP26QItemModelSurfaceDataProxyP7QObject
inline SurfaceItemModelHandler::SurfaceItemModelHandler(QItemModelSurfaceDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent),
      m_proxy(proxy),
      m_proxyArray(0),
      m_xPosRole(noRoleIndex),
      m_yPosRole(noRoleIndex),
      m_zPosRole(noRoleIndex),
      m_haveXPosPattern(false),
      m_haveYPosPattern(false),
      m_haveZPosPattern(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 394, as _ZN24QSurfaceDataProxyPrivateC2EP17QSurfaceDataProxy
inline QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate(QSurfaceDataProxy *q)
    : QAbstractDataProxyPrivate(q, QAbstractDataProxy::DataTypeSurface),
      m_dataArray(new QSurfaceDataArray)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 400, as _ZN24QSurfaceDataProxyPrivateD2Ev
inline QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
{
    clearArray();
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 628, as _ZN24QSurfaceDataProxyPrivate10clearArrayEv
inline void QSurfaceDataProxyPrivate::clearArray()
{
    for (int i = 0; i < m_dataArray->size(); i++)
        clearRow(i);
    m_dataArray->clear();
    delete m_dataArray;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 500, as _ZN24QSurfaceDataProxyPrivate4qptrEv
inline QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QSurfaceDataProxy *>(q_ptr);
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

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 620, as _ZN24QSurfaceDataProxyPrivate8clearRowEi
inline void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
{
    if (m_dataArray->at(rowIndex)) {
        delete m_dataArray->at(rowIndex);
        (*m_dataArray)[rowIndex] = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelsurfacedataproxy.cpp, line 1033, as _ZN33QItemModelSurfaceDataProxyPrivateC1EP26QItemModelSurfaceDataProxy
inline QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPrivate(QItemModelSurfaceDataProxy *q)
    : QSurfaceDataProxyPrivate(q),
      m_itemModelHandler(new SurfaceItemModelHandler(q)),
      m_useModelCategories(false),
      m_autoRowCategories(true),
      m_autoColumnCategories(true),
      m_multiMatchBehavior(QItemModelSurfaceDataProxy::MMBLast)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelsurfacedataproxy.cpp, line 1053, as _ZN33QItemModelSurfaceDataProxyPrivate23connectItemModelHandlerEv
inline void QItemModelSurfaceDataProxyPrivate::connectItemModelHandler()
{
    QObject::connect(m_itemModelHandler, &SurfaceItemModelHandler::itemModelChanged,
                     qptr(), &QItemModelSurfaceDataProxy::itemModelChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::rowRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::columnRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::xPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::yPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::zPosRoleChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::rowCategoriesChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::columnCategoriesChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::useModelCategoriesChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::autoRowCategoriesChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::autoColumnCategoriesChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::rowRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::columnRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::xPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::yPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::zPosRolePatternChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::rowRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::columnRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::xPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::yPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::zPosRoleReplaceChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
    QObject::connect(qptr(), &QItemModelSurfaceDataProxy::multiMatchBehaviorChanged,
                     m_itemModelHandler, &AbstractItemModelHandler::handleMappingChanged);
}

//  from ../qtdatavis3d/src/datavisualization/data/qitemmodelsurfacedataproxy.cpp, line 1048, as _ZN33QItemModelSurfaceDataProxyPrivate4qptrEv
inline QItemModelSurfaceDataProxy *QItemModelSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QItemModelSurfaceDataProxy *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QItemModelSurfaceDataProxyPrivate that Python can take functions over in. Every QItemModelSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelSurfaceDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemModelSurfaceDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemModelSurfaceDataProxyPrivate : public QItemModelSurfaceDataProxyPrivate {
public:
  using QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPrivate;
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

  //  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemModelSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemModelSurfaceDataProxyPrivateCall1 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall1>(taken[1]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall2 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall2>(taken[2]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall3 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall3>(taken[3]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall4 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall4>(taken[4]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall5 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall5>(taken[5]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall6 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall6>(taken[6]);
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
      CuteQItemModelSurfaceDataProxyPrivateCall7 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemModelSurfaceDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QItemModelSurfaceDataProxyPrivate10metaObjectEv(
    const QItemModelSurfaceDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QItemModelSurfaceDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QItemModelSurfaceDataProxyPrivate11qt_metacastEPKc(
    QItemModelSurfaceDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QItemModelSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QItemModelSurfaceDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QItemModelSurfaceDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QItemModelSurfaceDataProxyPrivate::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QItemModelSurfaceDataProxyPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemModelSurfaceDataProxyPrivate::tr(s, c, n));
}

//  QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPrivate(QIte
//      mModelSurfaceDataProxy *q)
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxyPrivate *ritual_ZN33QItemModelSurfaceDataProxyPrivateC1EP26QItemModelSurfaceDataProxy(
    QItemModelSurfaceDataProxy *q) {
  return new CuteQItemModelSurfaceDataProxyPrivate(q);
}

//  QItemModelSurfaceDataProxyPrivate::~QItemModelSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelSurfaceDataProxyPrivateD1Ev(
    QItemModelSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QItemModelSurfaceDataProxyPrivate::connectItemModelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelSurfaceDataProxyPrivate23connectItemModelHandlerEv(
    QItemModelSurfaceDataProxyPrivate *self) {
  self->connectItemModelHandler();
}

//  QItemModelSurfaceDataProxy *QItemModelSurfaceDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN33QItemModelSurfaceDataProxyPrivate4qptrEv(
    QItemModelSurfaceDataProxyPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQItemModelSurfaceDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelSurfaceDataProxyPrivate(
    QItemModelSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelSurfaceDataProxyPrivate *>(self)->take(key, call);
}
