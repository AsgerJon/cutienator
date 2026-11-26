//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandivisurfaceintegration_p.
//  h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtWayland::IviSurfaceIntegration' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandivisurfaceintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWaylandCompositor/private/qwaylandivisurfaceintegration_p.h>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/QWaylandIviSurface>
#include <QtWaylandCompositor/QWaylandQuickShellSurfaceItem>
#include <QtWaylandCompositor/QWaylandSeat>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWaylandCompositor__QtWayland_IviSurfaceIntegration.cpp, line 1, as moc:QtWayland::IviSurfaceIntegration
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t {};
} // unnamed namespace

template <> constexpr inline auto QtWayland::IviSurfaceIntegration::qt_create_metaobjectdata<qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtWayland::IviSurfaceIntegration",
        "handleIviSurfaceDestroyed",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'handleIviSurfaceDestroyed'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<IviSurfaceIntegration, qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtWayland::IviSurfaceIntegration::staticMetaObject = { {
    QMetaObject::SuperData::link<QWaylandQuickShellIntegration::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>.metaTypes,
    nullptr
} };

void QtWayland::IviSurfaceIntegration::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<IviSurfaceIntegration *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->handleIviSurfaceDestroyed(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QtWayland::IviSurfaceIntegration::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtWayland::IviSurfaceIntegration::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9QtWayland21IviSurfaceIntegrationE_t>.strings))
        return static_cast<void*>(this);
    return QWaylandQuickShellIntegration::qt_metacast(_clname);
}

int QtWayland::IviSurfaceIntegration::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWaylandQuickShellIntegration::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtwayland/src/compositor/extensions/qwaylandivisurfaceintegration.cpp, line 30, as _ZN9QtWayland21IviSurfaceIntegration25handleIviSurfaceDestroyedEv
namespace QtWayland {
inline void IviSurfaceIntegration::handleIviSurfaceDestroyed()
{
    m_shellSurface = nullptr;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandivisurfaceintegration.cpp, line 25, as _ZN9QtWayland21IviSurfaceIntegrationD0Ev
namespace QtWayland {
inline IviSurfaceIntegration::~IviSurfaceIntegration()
{
    m_item->setSurface(nullptr);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandivisurfaceintegration.cpp, line 16, as _ZN9QtWayland21IviSurfaceIntegrationC1EP29QWaylandQuickShellSurfaceItem
namespace QtWayland {
inline IviSurfaceIntegration::IviSurfaceIntegration(QWaylandQuickShellSurfaceItem *item)
    : QWaylandQuickShellIntegration(item)
    , m_item(item)
    , m_shellSurface(qobject_cast<QWaylandIviSurface *>(item->shellSurface()))
{
    m_item->setSurface(m_shellSurface->surface());
    connect(m_shellSurface, &QWaylandIviSurface::destroyed, this, &IviSurfaceIntegration::handleIviSurfaceDestroyed);
}
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  A QtWayland::IviSurfaceIntegration that Python can take functions over in. Every QtWayland::IviSurfaceIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_IviSurfaceIntegrationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_IviSurfaceIntegrationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_IviSurfaceIntegrationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_IviSurfaceIntegrationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_IviSurfaceIntegrationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_IviSurfaceIntegrationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_IviSurfaceIntegrationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_IviSurfaceIntegration : public QtWayland::IviSurfaceIntegration {
public:
  using QtWayland::IviSurfaceIntegration::IviSurfaceIntegration;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall0 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall1 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall2 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall3 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall4 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall5 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWayland_IviSurfaceIntegrationCall6 call = reinterpret_cast<CuteQtWayland_IviSurfaceIntegrationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::IviSurfaceIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland21IviSurfaceIntegration10metaObjectEv(
    const QtWayland::IviSurfaceIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::IviSurfaceIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland21IviSurfaceIntegration11qt_metacastEPKc(
    QtWayland::IviSurfaceIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::IviSurfaceIntegration::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland21IviSurfaceIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::IviSurfaceIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::IviSurfaceIntegration::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland21IviSurfaceIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::IviSurfaceIntegration::tr(s, c, n));
}

//  QtWayland::IviSurfaceIntegration::IviSurfaceIntegration(QWaylandQuickShel
//      lSurfaceItem *item)
extern "C" Q_DECL_EXPORT
QtWayland::IviSurfaceIntegration *ritual_ZN9QtWayland21IviSurfaceIntegrationC1EP29QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *item) {
  return new CuteQtWayland_IviSurfaceIntegration(item);
}

//  QtWayland::IviSurfaceIntegration::~IviSurfaceIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland21IviSurfaceIntegrationD1Ev(
    QtWayland::IviSurfaceIntegration *self) {
  delete self;
}

//  void QtWayland::IviSurfaceIntegration::handleIviSurfaceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland21IviSurfaceIntegration25handleIviSurfaceDestroyedEv(
    QtWayland::IviSurfaceIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::IviSurfaceIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleIviSurfaceDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleIviSurfaceDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQtWayland_IviSurfaceIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_IviSurfaceIntegration(
    QtWayland::IviSurfaceIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_IviSurfaceIntegration *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
