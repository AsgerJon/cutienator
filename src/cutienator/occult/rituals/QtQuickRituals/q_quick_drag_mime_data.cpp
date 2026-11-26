//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickDragMimeData' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickDragMimeData.cpp, line 1, as moc:QQuickDragMimeData
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QQuickDragMimeDataE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickDragMimeData::qt_create_metaobjectdata<qt_meta_tag_ZN18QQuickDragMimeDataE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickDragMimeData"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickDragMimeData, qt_meta_tag_ZN18QQuickDragMimeDataE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickDragMimeData::staticMetaObject = { {
    QMetaObject::SuperData::link<QMimeData::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDragMimeDataE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDragMimeDataE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QQuickDragMimeDataE_t>.metaTypes,
    nullptr
} };

void QQuickDragMimeData::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickDragMimeData *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickDragMimeData::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickDragMimeData::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDragMimeDataE_t>.strings))
        return static_cast<void*>(this);
    return QMimeData::qt_metacast(_clname);
}

int QQuickDragMimeData::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMimeData::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDragMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickDragMimeData10metaObjectEv(
    const QQuickDragMimeData *self) {
  return self->metaObject();
}

//  void *QQuickDragMimeData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickDragMimeData11qt_metacastEPKc(
    QQuickDragMimeData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDragMimeData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDragMimeData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDragMimeData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDragMimeData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickDragMimeData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDragMimeData::tr(s, c, n));
}

//  QQuickDragMimeData::QQuickDragMimeData()
extern "C" Q_DECL_EXPORT
QQuickDragMimeData *ritual_ZN18QQuickDragMimeDataC1Ev() {
  return new QQuickDragMimeData();
}

//  QStringList QQuickDragMimeData::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QQuickDragMimeData4keysEv(
    const QQuickDragMimeData *self) {
  return new QList<QString>(self->keys());
}

//  QObject *QQuickDragMimeData::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQuickDragMimeData6sourceEv(
    const QQuickDragMimeData *self) {
  return self->source();
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
