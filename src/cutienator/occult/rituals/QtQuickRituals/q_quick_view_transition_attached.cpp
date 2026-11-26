//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickViewTransitionAttached' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  3 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/QList>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickitemviewtransition_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQuick/private/qquicktransitionmanager_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickViewTransitionAttached.cpp, line 1, as moc:QQuickViewTransitionAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickViewTransitionAttached::qt_create_metaobjectdata<qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickViewTransitionAttached",
        "QML.Element",
        "ViewTransition",
        "QML.AddedInVersion",
        "512",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "ViewTransition is only available via attached properties.",
        "QML.Attached",
        "indexChanged",
        "",
        "itemChanged",
        "destinationChanged",
        "targetIndexesChanged",
        "targetItemsChanged",
        "index",
        "item",
        "QQuickItem*",
        "destination",
        "QPointF",
        "targetIndexes",
        "QList<int>",
        "targetItems",
        "QQmlListProperty<QObject>"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'indexChanged'
        QtMocHelpers::SignalData<void()>(10, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'itemChanged'
        QtMocHelpers::SignalData<void()>(12, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'destinationChanged'
        QtMocHelpers::SignalData<void()>(13, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'targetIndexesChanged'
        QtMocHelpers::SignalData<void()>(14, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'targetItemsChanged'
        QtMocHelpers::SignalData<void()>(15, 11, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'index'
        QtMocHelpers::PropertyData<int>(16, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Final, 0),
        // property 'item'
        QtMocHelpers::PropertyData<QQuickItem*>(17, 0x80000000 | 18, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
        // property 'destination'
        QtMocHelpers::PropertyData<QPointF>(19, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 2),
        // property 'targetIndexes'
        QtMocHelpers::PropertyData<QList<int>>(21, 0x80000000 | 22, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 3),
        // property 'targetItems'
        QtMocHelpers::PropertyData<QQmlListProperty<QObject>>(23, 0x80000000 | 24, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 4),
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
    return QtMocHelpers::metaObjectData<QQuickViewTransitionAttached, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickViewTransitionAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t>.metaTypes,
    nullptr
} };

void QQuickViewTransitionAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickViewTransitionAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->indexChanged(); break;
        case 1: _t->itemChanged(); break;
        case 2: _t->destinationChanged(); break;
        case 3: _t->targetIndexesChanged(); break;
        case 4: _t->targetItemsChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickViewTransitionAttached::*)()>(_a, &QQuickViewTransitionAttached::indexChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickViewTransitionAttached::*)()>(_a, &QQuickViewTransitionAttached::itemChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickViewTransitionAttached::*)()>(_a, &QQuickViewTransitionAttached::destinationChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickViewTransitionAttached::*)()>(_a, &QQuickViewTransitionAttached::targetIndexesChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickViewTransitionAttached::*)()>(_a, &QQuickViewTransitionAttached::targetItemsChanged, 4))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 3:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QList<int> >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<int*>(_v) = _t->index(); break;
        case 1: *reinterpret_cast<QQuickItem**>(_v) = _t->item(); break;
        case 2: *reinterpret_cast<QPointF*>(_v) = _t->destination(); break;
        case 3: *reinterpret_cast<QList<int>*>(_v) = _t->targetIndexes(); break;
        case 4: *reinterpret_cast<QQmlListProperty<QObject>*>(_v) = _t->targetItems(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickViewTransitionAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickViewTransitionAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickViewTransitionAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickViewTransitionAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 5;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void QQuickViewTransitionAttached::indexChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickViewTransitionAttached::itemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuickViewTransitionAttached::destinationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQuickViewTransitionAttached::targetIndexesChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQuickViewTransitionAttached::targetItemsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickitemviewtransition.cpp, line 557, as _ZN28QQuickViewTransitionAttachedC1EP7QObject
inline QQuickViewTransitionAttached::QQuickViewTransitionAttached(QObject *parent)
    : QObject(parent), m_index(-1)
{
}

//  from ../qtdeclarative/src/quick/items/qquickitemviewtransition.cpp, line 933, as _ZN28QQuickViewTransitionAttached11targetItemsEv
inline QQmlListProperty<QObject> QQuickViewTransitionAttached::targetItems()
{
    return QQmlListProperty<QObject>(this, &m_targetItems);
}

//  from ../qtdeclarative/src/quick/items/qquickitemviewtransition.cpp, line 938, as _ZN28QQuickViewTransitionAttached21qmlAttachedPropertiesEP7QObject
inline QQuickViewTransitionAttached *QQuickViewTransitionAttached::qmlAttachedProperties(QObject *obj)
{
    return new QQuickViewTransitionAttached(obj);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickViewTransitionAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickViewTransitionAttached10metaObjectEv(
    const QQuickViewTransitionAttached *self) {
  return self->metaObject();
}

//  void *QQuickViewTransitionAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickViewTransitionAttached11qt_metacastEPKc(
    QQuickViewTransitionAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickViewTransitionAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickViewTransitionAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickViewTransitionAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickViewTransitionAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickViewTransitionAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickViewTransitionAttached::tr(s, c, n));
}

//  void QQuickViewTransitionAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached24qt_qmlMarker_uncreatableEv(
    QQuickViewTransitionAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickViewTransitionAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached21qt_qmlMarker_attachedEv(
    QQuickViewTransitionAttached *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickViewTransitionAttached::QQuickViewTransitionAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickViewTransitionAttached *ritual_ZN28QQuickViewTransitionAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickViewTransitionAttached(parent);
}

//  int QQuickViewTransitionAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickViewTransitionAttached5indexEv(
    const QQuickViewTransitionAttached *self) {
  return self->index();
}

//  QQuickItem *QQuickViewTransitionAttached::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK28QQuickViewTransitionAttached4itemEv(
    const QQuickViewTransitionAttached *self) {
  return self->item();
}

//  QPointF QQuickViewTransitionAttached::destination() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QQuickViewTransitionAttached11destinationEv(
    const QQuickViewTransitionAttached *self) {
  return new QPointF(self->destination());
}

//  QList<int> QQuickViewTransitionAttached::targetIndexes() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK28QQuickViewTransitionAttached13targetIndexesEv(
    const QQuickViewTransitionAttached *self) {
  return new QList<int>(self->targetIndexes());
}

//  QQmlListProperty<QObject> QQuickViewTransitionAttached::targetItems()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN28QQuickViewTransitionAttached11targetItemsEv(
    QQuickViewTransitionAttached *self) {
  return new QQmlListProperty<QObject>(self->targetItems());
}

//  QQuickViewTransitionAttached
//      *QQuickViewTransitionAttached::qmlAttachedProperties(QObject *a0)
extern "C" Q_DECL_EXPORT
QQuickViewTransitionAttached *ritual_ZN28QQuickViewTransitionAttached21qmlAttachedPropertiesEP7QObject(
    QObject *a0) {
  return QQuickViewTransitionAttached::qmlAttachedProperties(a0);
}

//  void QQuickViewTransitionAttached::indexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached12indexChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "indexChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "indexChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::itemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached11itemChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::destinationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached18destinationChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "destinationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "destinationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::targetIndexesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached20targetIndexesChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetIndexesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetIndexesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickViewTransitionAttached::targetItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickViewTransitionAttached18targetItemsChangedEv(
    QQuickViewTransitionAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickViewTransitionAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetItemsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetItemsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QList<int> a ritual of QQuickViewTransitionAttached gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickViewTransitionAttached__QList_int(QList<int> *self) {
  delete self;
}

//  a QQmlListProperty<QObject> a ritual of QQuickViewTransitionAttached gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickViewTransitionAttached__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_viewtransitions)
