//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickPositionerAttached'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 5 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickpositioners_p.h>
#include <QtQuick/private/qquickpositioners_p_p.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qcoreapplication.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickPositionerAttached.cpp, line 1, as moc:QQuickPositionerAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24QQuickPositionerAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickPositionerAttached::qt_create_metaobjectdata<qt_meta_tag_ZN24QQuickPositionerAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickPositionerAttached",
        "indexChanged",
        "",
        "isFirstItemChanged",
        "isLastItemChanged",
        "index",
        "isFirstItem",
        "isLastItem"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'indexChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'isFirstItemChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'isLastItemChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'index'
        QtMocHelpers::PropertyData<int>(5, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Final, 0),
        // property 'isFirstItem'
        QtMocHelpers::PropertyData<bool>(6, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 1),
        // property 'isLastItem'
        QtMocHelpers::PropertyData<bool>(7, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 2),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickPositionerAttached, qt_meta_tag_ZN24QQuickPositionerAttachedE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickPositionerAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QQuickPositionerAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QQuickPositionerAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24QQuickPositionerAttachedE_t>.metaTypes,
    nullptr
} };

void QQuickPositionerAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickPositionerAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->indexChanged(); break;
        case 1: _t->isFirstItemChanged(); break;
        case 2: _t->isLastItemChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickPositionerAttached::*)()>(_a, &QQuickPositionerAttached::indexChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickPositionerAttached::*)()>(_a, &QQuickPositionerAttached::isFirstItemChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickPositionerAttached::*)()>(_a, &QQuickPositionerAttached::isLastItemChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<int*>(_v) = _t->index(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->isFirstItem(); break;
        case 2: *reinterpret_cast<bool*>(_v) = _t->isLastItem(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickPositionerAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickPositionerAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QQuickPositionerAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickPositionerAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QQuickPositionerAttached::indexChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickPositionerAttached::isFirstItemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuickPositionerAttached::isLastItemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 738, as _ZN24QQuickPositionerAttachedC1EP7QObject
inline QQuickPositionerAttached::QQuickPositionerAttached(QObject *parent) : QObject(parent), m_index(-1), m_isFirstItem(false), m_isLastItem(false)
{
    QQuickItem *attachedItem = qobject_cast<QQuickItem *>(parent);
    if (attachedItem) {
        QQuickBasePositioner *positioner = qobject_cast<QQuickBasePositioner *>(attachedItem->parent());
        if (positioner) {
            positioner->updateAttachedProperties(this, attachedItem);
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 755, as _ZN24QQuickPositionerAttached8setIndexEi
inline void QQuickPositionerAttached::setIndex(int index)
{
    if (m_index == index)
        return;
    m_index = index;
    emit indexChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 770, as _ZN24QQuickPositionerAttached14setIsFirstItemEb
inline void QQuickPositionerAttached::setIsFirstItem(bool isFirstItem)
{
    if (m_isFirstItem == isFirstItem)
        return;
    m_isFirstItem = isFirstItem;
    emit isFirstItemChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 778, as _ZN24QQuickPositionerAttached13setIsLastItemEb
inline void QQuickPositionerAttached::setIsLastItem(bool isLastItem)
{
    if (m_isLastItem == isLastItem)
        return;
    m_isLastItem = isLastItem;
    emit isLastItemChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickPositionerAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickPositionerAttached10metaObjectEv(
    const QQuickPositionerAttached *self) {
  return self->metaObject();
}

//  void *QQuickPositionerAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickPositionerAttached11qt_metacastEPKc(
    QQuickPositionerAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPositionerAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickPositionerAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPositionerAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPositionerAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickPositionerAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPositionerAttached::tr(s, c, n));
}

//  QQuickPositionerAttached::QQuickPositionerAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPositionerAttached *ritual_ZN24QQuickPositionerAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickPositionerAttached(parent);
}

//  int QQuickPositionerAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickPositionerAttached5indexEv(
    const QQuickPositionerAttached *self) {
  return self->index();
}

//  void QQuickPositionerAttached::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached8setIndexEi(
    QQuickPositionerAttached *self,
    int index) {
  self->setIndex(index);
}

//  bool QQuickPositionerAttached::isFirstItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPositionerAttached11isFirstItemEv(
    const QQuickPositionerAttached *self) {
  return self->isFirstItem();
}

//  void QQuickPositionerAttached::setIsFirstItem(bool isFirstItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached14setIsFirstItemEb(
    QQuickPositionerAttached *self,
    bool isFirstItem) {
  self->setIsFirstItem(isFirstItem);
}

//  bool QQuickPositionerAttached::isLastItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickPositionerAttached10isLastItemEv(
    const QQuickPositionerAttached *self) {
  return self->isLastItem();
}

//  void QQuickPositionerAttached::setIsLastItem(bool isLastItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached13setIsLastItemEb(
    QQuickPositionerAttached *self,
    bool isLastItem) {
  self->setIsLastItem(isLastItem);
}

//  void QQuickPositionerAttached::indexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached12indexChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
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

//  void QQuickPositionerAttached::isFirstItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached18isFirstItemChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isFirstItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isFirstItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickPositionerAttached::isLastItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickPositionerAttached17isLastItemChangedEv(
    QQuickPositionerAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPositionerAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isLastItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isLastItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)
