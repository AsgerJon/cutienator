//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickLayoutMirroringAttached' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  4 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickrendercontrol.h>
#include <QtQml/qjsengine.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickscreen_p.h>
#include <QtQuick/private/qquicksafearea_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qpen.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickaccessibleattached_p.h>
#include <QtQuick/private/qquickattachedpropertypropagator_p.h>
#include <QtQuick/private/qquickhoverhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtCore/private/qdebug_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#if QT_CONFIG(cursor)
# include <QtGui/qcursor.h>
#endif
#if QT_CONFIG(accessibility)
# include <QtGui/private/qaccessiblecache_p.h>
#endif
#include <QtCore/qpointer.h>
#include <algorithm>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickLayoutMirroringAttached.cpp, line 1, as moc:QQuickLayoutMirroringAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickLayoutMirroringAttached::qt_create_metaobjectdata<qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickLayoutMirroringAttached",
        "QML.Element",
        "LayoutMirroring",
        "QML.AddedInVersion",
        "512",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "LayoutMirroring is only available via attached properties.",
        "QML.Attached",
        "enabledChanged",
        "",
        "childrenInheritChanged",
        "enabled",
        "childrenInherit"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'enabledChanged'
        QtMocHelpers::SignalData<void()>(10, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'childrenInheritChanged'
        QtMocHelpers::SignalData<void()>(12, 11, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'enabled'
        QtMocHelpers::PropertyData<bool>(13, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::Resettable | QMC::StdCppSet | QMC::Final, 0),
        // property 'childrenInherit'
        QtMocHelpers::PropertyData<bool>(14, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
            {    9,    0 },
    });
    return QtMocHelpers::metaObjectData<QQuickLayoutMirroringAttached, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickLayoutMirroringAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t>.metaTypes,
    nullptr
} };

void QQuickLayoutMirroringAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickLayoutMirroringAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->enabledChanged(); break;
        case 1: _t->childrenInheritChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickLayoutMirroringAttached::*)()>(_a, &QQuickLayoutMirroringAttached::enabledChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickLayoutMirroringAttached::*)()>(_a, &QQuickLayoutMirroringAttached::childrenInheritChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->enabled(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->childrenInherit(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setEnabled(*reinterpret_cast<bool*>(_v)); break;
        case 1: _t->setChildrenInherit(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
    if (_c == QMetaObject::ResetProperty) {
        switch (_id) {
        case 0: _t->resetEnabled(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickLayoutMirroringAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickLayoutMirroringAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickLayoutMirroringAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickLayoutMirroringAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QQuickLayoutMirroringAttached::enabledChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickLayoutMirroringAttached::childrenInheritChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1491, as _ZN29QQuickLayoutMirroringAttachedC1EP7QObject
inline QQuickLayoutMirroringAttached::QQuickLayoutMirroringAttached(QObject *parent) : QObject(parent), itemPrivate(nullptr)
{
    if (QQuickItem *item = qobject_cast<QQuickItem *>(parent))
        itemPrivate = QQuickItemPrivate::get(item);
    else if (QQuickWindow *window = qobject_cast<QQuickWindow *>(parent))
        itemPrivate = QQuickItemPrivate::get(window->contentItem());

    if (itemPrivate)
        itemPrivate->extra.value().layoutDirectionAttached = this;
    else
        qmlWarning(parent) << tr("LayoutMirroring attached property only works with Items and Windows");
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1509, as _ZNK29QQuickLayoutMirroringAttached7enabledEv
inline bool QQuickLayoutMirroringAttached::enabled() const
{
    return itemPrivate ? itemPrivate->effectiveLayoutMirror : false;
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1514, as _ZN29QQuickLayoutMirroringAttached10setEnabledEb
inline void QQuickLayoutMirroringAttached::setEnabled(bool enabled)
{
    if (!itemPrivate)
        return;

    itemPrivate->isMirrorImplicit = false;
    if (enabled != itemPrivate->effectiveLayoutMirror) {
        itemPrivate->setLayoutMirror(enabled);
        if (itemPrivate->inheritMirrorFromItem)
             itemPrivate->resolveLayoutMirror();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1527, as _ZN29QQuickLayoutMirroringAttached12resetEnabledEv
inline void QQuickLayoutMirroringAttached::resetEnabled()
{
    if (itemPrivate && !itemPrivate->isMirrorImplicit) {
        itemPrivate->isMirrorImplicit = true;
        itemPrivate->resolveLayoutMirror();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1535, as _ZNK29QQuickLayoutMirroringAttached15childrenInheritEv
inline bool QQuickLayoutMirroringAttached::childrenInherit() const
{
    return itemPrivate ? itemPrivate->inheritMirrorFromItem : false;
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1540, as _ZN29QQuickLayoutMirroringAttached18setChildrenInheritEb
inline void QQuickLayoutMirroringAttached::setChildrenInherit(bool childrenInherit) {
    if (itemPrivate && childrenInherit != itemPrivate->inheritMirrorFromItem) {
        itemPrivate->inheritMirrorFromItem = childrenInherit;
        itemPrivate->resolveLayoutMirror();
        childrenInheritChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1504, as _ZN29QQuickLayoutMirroringAttached21qmlAttachedPropertiesEP7QObject
inline QQuickLayoutMirroringAttached * QQuickLayoutMirroringAttached::qmlAttachedProperties(QObject *object)
{
    return new QQuickLayoutMirroringAttached(object);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLayoutMirroringAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickLayoutMirroringAttached10metaObjectEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->metaObject();
}

//  void *QQuickLayoutMirroringAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickLayoutMirroringAttached11qt_metacastEPKc(
    QQuickLayoutMirroringAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLayoutMirroringAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickLayoutMirroringAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLayoutMirroringAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickLayoutMirroringAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickLayoutMirroringAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLayoutMirroringAttached::tr(s, c, n));
}

//  void QQuickLayoutMirroringAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached24qt_qmlMarker_uncreatableEv(
    QQuickLayoutMirroringAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickLayoutMirroringAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached21qt_qmlMarker_attachedEv(
    QQuickLayoutMirroringAttached *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickLayoutMirroringAttached::QQuickLayoutMirroringAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickLayoutMirroringAttached *ritual_ZN29QQuickLayoutMirroringAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickLayoutMirroringAttached(parent);
}

//  bool QQuickLayoutMirroringAttached::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickLayoutMirroringAttached7enabledEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->enabled();
}

//  void QQuickLayoutMirroringAttached::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached10setEnabledEb(
    QQuickLayoutMirroringAttached *self,
    bool a0) {
  self->setEnabled(a0);
}

//  void QQuickLayoutMirroringAttached::resetEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached12resetEnabledEv(
    QQuickLayoutMirroringAttached *self) {
  self->resetEnabled();
}

//  bool QQuickLayoutMirroringAttached::childrenInherit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickLayoutMirroringAttached15childrenInheritEv(
    const QQuickLayoutMirroringAttached *self) {
  return self->childrenInherit();
}

//  void QQuickLayoutMirroringAttached::setChildrenInherit(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached18setChildrenInheritEb(
    QQuickLayoutMirroringAttached *self,
    bool a0) {
  self->setChildrenInherit(a0);
}

//  QQuickLayoutMirroringAttached
//      *QQuickLayoutMirroringAttached::qmlAttachedProperties(QObject *a0)
extern "C" Q_DECL_EXPORT
QQuickLayoutMirroringAttached *ritual_ZN29QQuickLayoutMirroringAttached21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickLayoutMirroringAttached::qmlAttachedProperties(a0);
}

//  void QQuickLayoutMirroringAttached::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached14enabledChangedEv(
    QQuickLayoutMirroringAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutMirroringAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutMirroringAttached::childrenInheritChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLayoutMirroringAttached22childrenInheritChangedEv(
    QQuickLayoutMirroringAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutMirroringAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "childrenInheritChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "childrenInheritChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
