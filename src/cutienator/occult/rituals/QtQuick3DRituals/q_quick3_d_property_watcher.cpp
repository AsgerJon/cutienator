//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuick3DPropertyWatcher'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick3D/private/qquick3dshaderutils_p.h>
#include <QtCore/qfile.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include <QtQuick3D/private/qquick3dviewport_p.h>
#include <QtQuick3D/private/qquick3dcustommaterial_p.h>
#include <QtQuick3D/private/qquick3deffect_p.h>
#include <QtQuick3D/qquick3dtextureproviderextension.h>
#include <QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#include <QtQuick3D/ssg/qquick3dextensionhelpers.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderimage_p.h>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick3D__QQuick3DPropertyWatcher.cpp, line 1, as moc:QQuick3DPropertyWatcher
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuick3DPropertyWatcher::qt_create_metaobjectdata<qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuick3DPropertyWatcher",
        "onValuePropertyChanged",
        "",
        "onPointerPropertyChanged"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'onValuePropertyChanged'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'onPointerPropertyChanged'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuick3DPropertyWatcher, qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuick3DPropertyWatcher::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>.metaTypes,
    nullptr
} };

void QQuick3DPropertyWatcher::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuick3DPropertyWatcher *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->onValuePropertyChanged(); break;
        case 1: _t->onPointerPropertyChanged(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QQuick3DPropertyWatcher::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuick3DPropertyWatcher::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQuick3DPropertyWatcherE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuick3DPropertyWatcher::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtquick3d/src/quick3d/qquick3dshaderutils.cpp, line 2000, as _ZN23QQuick3DPropertyWatcher22onValuePropertyChangedEv
inline void QQuick3DPropertyWatcher::onValuePropertyChanged()
{
    m_tracker->m_dirtyProperties.push_back(m_property.propertyIndex());
    m_tracker->markTrackedPropertyDirty(m_property, QQuick3DPropertyChangedTracker::DirtyPropertyHint::Value);
}

//  from ../qtquick3d/src/quick3d/qquick3dshaderutils.cpp, line 2006, as _ZN23QQuick3DPropertyWatcher24onPointerPropertyChangedEv
inline void QQuick3DPropertyWatcher::onPointerPropertyChanged()
{
    m_tracker->m_dirtyProperties.push_back(m_property.propertyIndex());
    m_tracker->markTrackedPropertyDirty(m_property, QQuick3DPropertyChangedTracker::DirtyPropertyHint::Reference);;
}

//  from ../qtquick3d/src/quick3d/qquick3dshaderutils.cpp, line 1967, as _ZN23QQuick3DPropertyWatcherC1EP30QQuick3DPropertyChangedTracker13QMetaProperty
inline QQuick3DPropertyWatcher::QQuick3DPropertyWatcher(QQuick3DPropertyChangedTracker *tracker, QMetaProperty property)
    : m_tracker(tracker)
    , m_property(property)
{
    Q_ASSERT(tracker != nullptr);
    Q_ASSERT(property.isValid() && property.hasNotifySignal());

    // Ensure that the watcher is on the watched object's thread if it's not already there.
    // If not, the watcher will be created on the render thread and the notify connections
    // will be queued to the render thread, which is not what we want
    // (as can end-up concurrently mutating the dirty lists).
    if (thread() != tracker->m_owner->thread())
        moveToThread(tracker->m_owner->thread());

    const bool isPointerType = (property.metaType().flags().testFlag(QMetaType::IsPointer));

    if (!isPointerType) {
        // Value change notification
        const auto idx = staticMetaObject.indexOfSlot("onValuePropertyChanged()");
        if (QSSG_GUARD_X(idx != -1, "Method not found!")) {
            auto onPropertyChangedMethod = staticMetaObject.method(idx);
            connect(m_tracker->m_owner, property.notifySignal(), this, onPropertyChangedMethod);
        }
    } else {
        // Pointer value change notification
        const auto idx = staticMetaObject.indexOfSlot("onPointerPropertyChanged()");
        if (QSSG_GUARD_X(idx != -1, "Method not found!")) {
            auto onPointerPropertyChangedMethod = staticMetaObject.method(idx);
            connect(m_tracker->m_owner, property.notifySignal(), this, onPointerPropertyChangedMethod);
        }
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DPropertyWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DPropertyWatcher10metaObjectEv(
    const QQuick3DPropertyWatcher *self) {
  return self->metaObject();
}

//  void *QQuick3DPropertyWatcher::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DPropertyWatcher11qt_metacastEPKc(
    QQuick3DPropertyWatcher *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DPropertyWatcher::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DPropertyWatcher11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DPropertyWatcher *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DPropertyWatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DPropertyWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DPropertyWatcher::tr(s, c, n));
}

//  QQuick3DPropertyWatcher::QQuick3DPropertyWatcher(QQuick3DPropertyChangedT
//      racker *tracker, QMetaProperty property)
extern "C" Q_DECL_EXPORT
QQuick3DPropertyWatcher *ritual_ZN23QQuick3DPropertyWatcherC1EP30QQuick3DPropertyChangedTracker13QMetaProperty(
    QQuick3DPropertyChangedTracker *tracker,
    const QMetaProperty *property) {
  return new QQuick3DPropertyWatcher(tracker, *property);
}

//  void QQuick3DPropertyWatcher::onValuePropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher22onValuePropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DPropertyWatcher")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onValuePropertyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onValuePropertyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DPropertyWatcher::onPointerPropertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DPropertyWatcher24onPointerPropertyChangedEv(
    QQuick3DPropertyWatcher *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DPropertyWatcher")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onPointerPropertyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onPointerPropertyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
