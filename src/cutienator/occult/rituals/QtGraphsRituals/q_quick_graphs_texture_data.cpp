//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphstexturedata_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickGraphsTextureData'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphstexturedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/commonutils_p.h>
#include <QtGraphs/private/qquickgraphstexturedata_p.h>
#include <QtGraphs/private/qgraphsglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__QQuickGraphsTextureData.cpp, line 1, as moc:QQuickGraphsTextureData
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QQuickGraphsTextureDataE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickGraphsTextureData::qt_create_metaobjectdata<qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickGraphsTextureData"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickGraphsTextureData, qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickGraphsTextureData::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuick3DTextureData::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>.metaTypes,
    nullptr
} };

void QQuickGraphsTextureData::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickGraphsTextureData *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickGraphsTextureData::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickGraphsTextureData::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuickGraphsTextureDataE_t>.strings))
        return static_cast<void*>(this);
    return QQuick3DTextureData::qt_metacast(_clname);
}

int QQuickGraphsTextureData::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuick3DTextureData::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs3d/qml/qquickgraphstexturedata.cpp, line 24, as _ZN23QQuickGraphsTextureDataC1Ev
inline QQuickGraphsTextureData::QQuickGraphsTextureData() {}

//  from ../qtgraphs/src/graphs3d/qml/qquickgraphstexturedata.cpp, line 26, as _ZN23QQuickGraphsTextureDataD1Ev
inline QQuickGraphsTextureData::~QQuickGraphsTextureData() {}

//  from ../qtgraphs/src/graphs3d/qml/qquickgraphstexturedata.cpp, line 71, as _ZN23QQuickGraphsTextureData17linearInterpolateE6QColorS0_f
inline QColor QQuickGraphsTextureData::linearInterpolate(QColor startColor, QColor endColor, float value)
{
    QColor output;

    output.setRedF(startColor.redF() + (value * (endColor.redF() - startColor.redF())));
    output.setGreenF(startColor.greenF() + (value * (endColor.greenF() - startColor.greenF())));
    output.setBlueF(startColor.blueF() + (value * (endColor.blueF() - startColor.blueF())));
    output.setAlphaF(startColor.alphaF() + (value * (endColor.alphaF() - startColor.alphaF())));

    return output;
}
//  -----------------------------------------------------------------------

//  A QQuickGraphsTextureData that Python can take functions over in. Every QQuickGraphsTextureData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickGraphsTextureDataCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuickGraphsTextureDataCall1)(const void *, int *);
typedef void (*CuteQQuickGraphsTextureDataCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuickGraphsTextureDataCall3)(const void *, int *);
typedef void (*CuteQQuickGraphsTextureDataCall4)(const void *, int *);
typedef void (*CuteQQuickGraphsTextureDataCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsTextureDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsTextureDataCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsTextureDataCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsTextureDataCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsTextureDataCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsTextureDataCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsTextureDataCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsTextureData : public QQuickGraphsTextureData {
public:
  using QQuickGraphsTextureData::QQuickGraphsTextureData;
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
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall0 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTextureData::updateSpatialNode(node);
  }

  //  void QQuick3DTextureData::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall1 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DTextureData::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall2 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall3 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall4 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall5 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall6 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall7 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall8 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall9 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall10 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall11 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickGraphsTextureDataCall12 call = reinterpret_cast<CuteQQuickGraphsTextureDataCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsTextureData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickGraphsTextureData10metaObjectEv(
    const QQuickGraphsTextureData *self) {
  return self->metaObject();
}

//  void *QQuickGraphsTextureData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickGraphsTextureData11qt_metacastEPKc(
    QQuickGraphsTextureData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphsTextureData::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickGraphsTextureData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphsTextureData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphsTextureData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickGraphsTextureData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsTextureData::tr(s, c, n));
}

//  QQuickGraphsTextureData::QQuickGraphsTextureData()
extern "C" Q_DECL_EXPORT
QQuickGraphsTextureData *ritual_ZN23QQuickGraphsTextureDataC1Ev() {
  return new CuteQQuickGraphsTextureData();
}

//  QQuickGraphsTextureData::~QQuickGraphsTextureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGraphsTextureDataD1Ev(QQuickGraphsTextureData *self) {
  delete self;
}

//  QColor QQuickGraphsTextureData::linearInterpolate(QColor startColor,
//      QColor endColor, float value)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN23QQuickGraphsTextureData17linearInterpolateE6QColorS0_f(
    QQuickGraphsTextureData *self,
    const QColor *startColor,
    const QColor *endColor,
    float value) {
  return new QColor(self->linearInterpolate(*startColor, *endColor, value));
}

//  a Python function taken by a CuteQQuickGraphsTextureData, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsTextureData(
    QQuickGraphsTextureData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsTextureData *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
