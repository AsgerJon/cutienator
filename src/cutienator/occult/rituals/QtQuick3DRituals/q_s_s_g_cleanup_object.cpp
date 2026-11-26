//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QSSGCleanupObject' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <memory>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3D/private/qquick3dscenemanager_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3D/private/qquick3dviewport_p.h>
#include <QtQuick3D/private/qquick3dmodel_p.h>
#include <QtQuick/QQuickWindow>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermodel_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderimage_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderroot_p.h>
#include <QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick3D/qquick3drenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3D__QSSGCleanupObject.cpp, line 1, as moc:QSSGCleanupObject
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QSSGCleanupObjectE_t {};
} // unnamed namespace

template <> constexpr inline auto QSSGCleanupObject::qt_create_metaobjectdata<qt_meta_tag_ZN17QSSGCleanupObjectE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QSSGCleanupObject",
        "cleanupResources",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Method 'cleanupResources'
        QtMocHelpers::MethodData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QSSGCleanupObject, qt_meta_tag_ZN17QSSGCleanupObjectE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QSSGCleanupObject::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QSSGCleanupObjectE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QSSGCleanupObjectE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QSSGCleanupObjectE_t>.metaTypes,
    nullptr
} };

void QSSGCleanupObject::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QSSGCleanupObject *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->cleanupResources(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QSSGCleanupObject::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QSSGCleanupObject::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QSSGCleanupObjectE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QSSGCleanupObject::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
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

//  from ../qtquick3d/src/quick3d/qquick3dscenemanager.cpp, line 51, as _ZN17QSSGCleanupObject16cleanupResourcesEv
inline void QSSGCleanupObject::cleanupResources()
{
    m_rci->renderer()->cleanupResources(m_resourceCleanupQueue);
    deleteLater();
}

//  from ../qtquick3d/src/quick3d/qquick3dscenemanager.cpp, line 46, as _ZN17QSSGCleanupObjectD0Ev
inline QSSGCleanupObject::~QSSGCleanupObject()
{
    QSSG_CHECK(QSSG_DEBUG_COND(m_resourceCleanupQueue.isEmpty()));
}

//  from ../qtquick3d/src/quick3d/qquick3dscenemanager.cpp, line 30, as _ZN17QSSGCleanupObjectC1ESt10shared_ptrI26QSSGRenderContextInterfaceE5QListIP21QSSGRenderGraphObjectEP12QQuickWindow
inline QSSGCleanupObject::QSSGCleanupObject(std::shared_ptr<QSSGRenderContextInterface> rci, QList<QSSGRenderGraphObject *> resourceCleanupQueue, QQuickWindow *window)
    : QObject(window)
    , m_rci(rci)
    , m_window(window)
    , m_resourceCleanupQueue(resourceCleanupQueue)
{
    Q_ASSERT(window != nullptr && rci); // We need a window and a rci for this!

    if (QSGRenderContext *rc = QQuickWindowPrivate::get(window)->context) {
        connect(rc, &QSGRenderContext::releaseCachedResourcesRequested, this, &QSSGCleanupObject::cleanupResources, Qt::DirectConnection);
        connect(rc, &QSGRenderContext::invalidated, this, &QSSGCleanupObject::cleanupResources, Qt::DirectConnection);
    } else {
        qWarning() << "No QSGRenderContext, cannot cleanup resources!";
    }
}
//  -----------------------------------------------------------------------

//  A QSSGCleanupObject that Python can take functions over in. Every QSSGCleanupObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGCleanupObjectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGCleanupObjectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGCleanupObjectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGCleanupObjectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGCleanupObjectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGCleanupObjectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGCleanupObjectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSSGCleanupObject : public QSSGCleanupObject {
public:
  using QSSGCleanupObject::QSSGCleanupObject;
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
      CuteQSSGCleanupObjectCall0 call = reinterpret_cast<CuteQSSGCleanupObjectCall0>(taken[0]);
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
      CuteQSSGCleanupObjectCall1 call = reinterpret_cast<CuteQSSGCleanupObjectCall1>(taken[1]);
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
      CuteQSSGCleanupObjectCall2 call = reinterpret_cast<CuteQSSGCleanupObjectCall2>(taken[2]);
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
      CuteQSSGCleanupObjectCall3 call = reinterpret_cast<CuteQSSGCleanupObjectCall3>(taken[3]);
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
      CuteQSSGCleanupObjectCall4 call = reinterpret_cast<CuteQSSGCleanupObjectCall4>(taken[4]);
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
      CuteQSSGCleanupObjectCall5 call = reinterpret_cast<CuteQSSGCleanupObjectCall5>(taken[5]);
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
      CuteQSSGCleanupObjectCall6 call = reinterpret_cast<CuteQSSGCleanupObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSSGCleanupObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QSSGCleanupObject10metaObjectEv(
    const QSSGCleanupObject *self) {
  return self->metaObject();
}

//  void *QSSGCleanupObject::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QSSGCleanupObject11qt_metacastEPKc(
    QSSGCleanupObject *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSSGCleanupObject::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QSSGCleanupObject11qt_metacallEN11QMetaObject4CallEiPPv(
    QSSGCleanupObject *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSSGCleanupObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSSGCleanupObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSSGCleanupObject::tr(s, c, n));
}

//  QSSGCleanupObject::QSSGCleanupObject(std::shared_ptr<QSSGRenderContextInt
//      erface> rci, QList<QSSGRenderGraphObject *> resourceCleanupQueue,
//      QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSSGCleanupObject *ritual_ZN17QSSGCleanupObjectC1ESt10shared_ptrI26QSSGRenderContextInterfaceE5QListIP21QSSGRenderGraphObjectEP12QQuickWindow(
    const std::shared_ptr<QSSGRenderContextInterface> *rci,
    const QList<QSSGRenderGraphObject *> *resourceCleanupQueue,
    QQuickWindow *window) {
  return new CuteQSSGCleanupObject(*rci, *resourceCleanupQueue, window);
}

//  QSSGCleanupObject::~QSSGCleanupObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGCleanupObjectD1Ev(QSSGCleanupObject *self) {
  delete self;
}

//  void QSSGCleanupObject::cleanupResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGCleanupObject16cleanupResourcesEv(
    QSSGCleanupObject *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSSGCleanupObject")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cleanupResources()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cleanupResources()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQSSGCleanupObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGCleanupObject(
    QSSGCleanupObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGCleanupObject *>(self)->take(key, call);
}
