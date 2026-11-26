//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dbars_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'Q3DBarsPrivate' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dbars_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/q3dbars_p.h>
#include <QtDataVisualization/qabstract3dgraph.h>
#include <QtDataVisualization/private/qabstract3dgraph_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#include <QtDataVisualization/private/qabstract3dinputhandler_p.h>
#include <QtDataVisualization/private/q3dscene_p.h>
#include <QtDataVisualization/qutils.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QGuiApplication>
#include <QtGui/QOpenGLContext>
#include <QtOpenGL/QOpenGLPaintDevice>
#include <QtGui/QPainter>
#include <QtOpenGL/QOpenGLFramebufferObject>
#include <QtGui/QOffscreenSurface>
#if defined(Q_OS_MACOS)
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__Q3DBarsPrivate.cpp, line 1, as moc:Q3DBarsPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN14Q3DBarsPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto Q3DBarsPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN14Q3DBarsPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Q3DBarsPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Q3DBarsPrivate, qt_meta_tag_ZN14Q3DBarsPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Q3DBarsPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DGraphPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14Q3DBarsPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14Q3DBarsPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN14Q3DBarsPrivateE_t>.metaTypes,
    nullptr
} };

void Q3DBarsPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Q3DBarsPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *Q3DBarsPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Q3DBarsPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14Q3DBarsPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DGraphPrivate::qt_metacast(_clname);
}

int Q3DBarsPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DGraphPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 457, as _ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
{
    emit qptr()->columnAxisChanged(static_cast<QCategory3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 462, as _ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
{
    emit qptr()->valueAxisChanged(static_cast<QValue3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 467, as _ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis
inline void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
{
    emit qptr()->rowAxisChanged(static_cast<QCategory3DAxis *>(axis));
}

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1046, as _ZN23QAbstract3DGraphPrivateD2Ev
inline QAbstract3DGraphPrivate::~QAbstract3DGraphPrivate()
{
    if (m_offscreenSurface) {
        m_offscreenSurface->destroy();
        delete m_offscreenSurface;
    }
    if (m_context) {
        if (!m_context->makeCurrent(q_ptr))
            m_context->doneCurrent();
    }

    delete m_visualController;
}

//  from ../qtdatavis3d/src/datavisualization/engine/qabstract3dgraph.cpp, line 1035, as _ZN23QAbstract3DGraphPrivateC2EP16QAbstract3DGraph
inline QAbstract3DGraphPrivate::QAbstract3DGraphPrivate(QAbstract3DGraph *q)
    : QObject(0),
      q_ptr(q),
      m_updatePending(false),
      m_visualController(0),
      m_devicePixelRatio(1.f),
      m_offscreenSurface(0),
      m_initialized(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 447, as _ZN14Q3DBarsPrivateC1EP7Q3DBars
inline Q3DBarsPrivate::Q3DBarsPrivate(Q3DBars *q)
    : QAbstract3DGraphPrivate(q),
      m_shared(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 453, as _ZN14Q3DBarsPrivateD1Ev
inline Q3DBarsPrivate::~Q3DBarsPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/q3dbars.cpp, line 472, as _ZN14Q3DBarsPrivate4qptrEv
inline Q3DBars *Q3DBarsPrivate::qptr()
{
    return static_cast<Q3DBars *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A Q3DBarsPrivate that Python can take functions over in. Every Q3DBarsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQ3DBarsPrivateCall0)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DBarsPrivateCall1)(const void *, QAbstract3DAxis *, int *);
typedef void (*CuteQ3DBarsPrivateCall2)(const void *, QAbstract3DAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DBarsPrivate : public Q3DBarsPrivate {
public:
  using Q3DBarsPrivate::Q3DBarsPrivate;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisXChangedEP15QAbstract3DAxis")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisYChangedEP15QAbstract3DAxis")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstract3DGraphPrivate18handleAxisZChangedEP15QAbstract3DAxis")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
  void handleAxisXChanged(QAbstract3DAxis *axis) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall0 call = reinterpret_cast<CuteQ3DBarsPrivateCall0>(taken[0]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisXChanged(axis);
  }

  //  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
  void handleAxisYChanged(QAbstract3DAxis *axis) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall1 call = reinterpret_cast<CuteQ3DBarsPrivateCall1>(taken[1]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisYChanged(axis);
  }

  //  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
  void handleAxisZChanged(QAbstract3DAxis *axis) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall2 call = reinterpret_cast<CuteQ3DBarsPrivateCall2>(taken[2]);
      call(this, axis, &handled);
      if (handled) return;
    }
    Q3DBarsPrivate::handleAxisZChanged(axis);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall3 call = reinterpret_cast<CuteQ3DBarsPrivateCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall4 call = reinterpret_cast<CuteQ3DBarsPrivateCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall5 call = reinterpret_cast<CuteQ3DBarsPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall6 call = reinterpret_cast<CuteQ3DBarsPrivateCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall7 call = reinterpret_cast<CuteQ3DBarsPrivateCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall8 call = reinterpret_cast<CuteQ3DBarsPrivateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQ3DBarsPrivateCall9 call = reinterpret_cast<CuteQ3DBarsPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DBarsPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14Q3DBarsPrivate10metaObjectEv(
    const Q3DBarsPrivate *self) {
  return self->metaObject();
}

//  void *Q3DBarsPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14Q3DBarsPrivate11qt_metacastEPKc(
    Q3DBarsPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DBarsPrivate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14Q3DBarsPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DBarsPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DBarsPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14Q3DBarsPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DBarsPrivate::tr(s, c, n));
}

//  Q3DBarsPrivate::Q3DBarsPrivate(Q3DBars *q)
extern "C" Q_DECL_EXPORT
Q3DBarsPrivate *ritual_ZN14Q3DBarsPrivateC1EP7Q3DBars(Q3DBars *q) {
  return new CuteQ3DBarsPrivate(q);
}

//  Q3DBarsPrivate::~Q3DBarsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivateD1Ev(Q3DBarsPrivate *self) {
  delete self;
}

//  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}

//  Q3DBars *Q3DBarsPrivate::qptr()
extern "C" Q_DECL_EXPORT
Q3DBars *ritual_ZN14Q3DBarsPrivate4qptrEv(Q3DBarsPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQ3DBarsPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DBarsPrivate(
    Q3DBarsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DBarsPrivate *>(self)->take(key, call);
}

//  void Q3DBarsPrivate::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisXChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisXChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisYChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisYChanged(axis);
}

//  void Q3DBarsPrivate::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Q3DBarsPrivate18handleAxisZChangedEP15QAbstract3DAxis(
    Q3DBarsPrivate *self,
    QAbstract3DAxis *axis) {
  self->Q3DBarsPrivate::handleAxisZChanged(axis);
}
