//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickEnterKeyAttached'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 4 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickEnterKeyAttached.cpp, line 1, as moc:QQuickEnterKeyAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickEnterKeyAttached::qt_create_metaobjectdata<qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickEnterKeyAttached",
        "QML.Element",
        "EnterKey",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "EnterKey is only available via attached properties",
        "QML.AddedInVersion",
        "518",
        "QML.Attached",
        "typeChanged",
        "",
        "type",
        "Qt::EnterKeyType"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'typeChanged'
        QtMocHelpers::SignalData<void()>(10, 11, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'type'
        QtMocHelpers::PropertyData<Qt::EnterKeyType>(12, 0x80000000 | 13, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 0),
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
    return QtMocHelpers::metaObjectData<QQuickEnterKeyAttached, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickEnterKeyAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t>.metaTypes,
    nullptr
} };

void QQuickEnterKeyAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickEnterKeyAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->typeChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickEnterKeyAttached::*)()>(_a, &QQuickEnterKeyAttached::typeChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<Qt::EnterKeyType*>(_v) = _t->type(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setType(*reinterpret_cast<Qt::EnterKeyType*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickEnterKeyAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickEnterKeyAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickEnterKeyAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickEnterKeyAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QQuickEnterKeyAttached::typeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1644, as _ZN22QQuickEnterKeyAttachedC1EP7QObject
inline QQuickEnterKeyAttached::QQuickEnterKeyAttached(QObject *parent)
    : QObject(parent), itemPrivate(nullptr), keyType(Qt::EnterKeyDefault)
{
    if (QQuickItem *item = qobject_cast<QQuickItem*>(parent)) {
        itemPrivate = QQuickItemPrivate::get(item);
        itemPrivate->extra.value().enterKeyAttached = this;
    } else
        qmlWarning(parent) << tr("EnterKey attached property only works with Items");
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1659, as _ZNK22QQuickEnterKeyAttached4typeEv
inline Qt::EnterKeyType QQuickEnterKeyAttached::type() const
{
    return keyType;
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1664, as _ZN22QQuickEnterKeyAttached7setTypeEN2Qt12EnterKeyTypeE
inline void QQuickEnterKeyAttached::setType(Qt::EnterKeyType type)
{
    if (keyType != type) {
        keyType = type;
#if QT_CONFIG(im)
        if (itemPrivate && itemPrivate->activeFocus)
            QGuiApplication::inputMethod()->update(Qt::ImEnterKeyType);
#endif
        typeChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 1654, as _ZN22QQuickEnterKeyAttached21qmlAttachedPropertiesEP7QObject
inline QQuickEnterKeyAttached *QQuickEnterKeyAttached::qmlAttachedProperties(QObject *object)
{
    return new QQuickEnterKeyAttached(object);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickEnterKeyAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickEnterKeyAttached10metaObjectEv(
    const QQuickEnterKeyAttached *self) {
  return self->metaObject();
}

//  void *QQuickEnterKeyAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickEnterKeyAttached11qt_metacastEPKc(
    QQuickEnterKeyAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickEnterKeyAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickEnterKeyAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickEnterKeyAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickEnterKeyAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickEnterKeyAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickEnterKeyAttached::tr(s, c, n));
}

//  void QQuickEnterKeyAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickEnterKeyAttached24qt_qmlMarker_uncreatableEv(
    QQuickEnterKeyAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickEnterKeyAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickEnterKeyAttached21qt_qmlMarker_attachedEv(
    QQuickEnterKeyAttached *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickEnterKeyAttached::QQuickEnterKeyAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickEnterKeyAttached *ritual_ZN22QQuickEnterKeyAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickEnterKeyAttached(parent);
}

//  Qt::EnterKeyType QQuickEnterKeyAttached::type() const
extern "C" Q_DECL_EXPORT
Qt::EnterKeyType ritual_ZNK22QQuickEnterKeyAttached4typeEv(
    const QQuickEnterKeyAttached *self) {
  return self->type();
}

//  void QQuickEnterKeyAttached::setType(Qt::EnterKeyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickEnterKeyAttached7setTypeEN2Qt12EnterKeyTypeE(
    QQuickEnterKeyAttached *self,
    Qt::EnterKeyType type) {
  self->setType(type);
}

//  QQuickEnterKeyAttached
//      *QQuickEnterKeyAttached::qmlAttachedProperties(QObject *a0)
extern "C" Q_DECL_EXPORT
QQuickEnterKeyAttached *ritual_ZN22QQuickEnterKeyAttached21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickEnterKeyAttached::qmlAttachedProperties(a0);
}

//  void QQuickEnterKeyAttached::typeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickEnterKeyAttached11typeChangedEv(
    QQuickEnterKeyAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickEnterKeyAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "typeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "typeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
