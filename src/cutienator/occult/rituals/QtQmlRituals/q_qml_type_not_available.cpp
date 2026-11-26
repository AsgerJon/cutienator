//  Written by dev_tooling.RitualGenerator from the records of QtQml/qqml.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQmlTypeNotAvailable' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqml.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQml__QQmlTypeNotAvailable.cpp, line 1, as moc:QQmlTypeNotAvailable
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QQmlTypeNotAvailableE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlTypeNotAvailable::qt_create_metaobjectdata<qt_meta_tag_ZN20QQmlTypeNotAvailableE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlTypeNotAvailable",
        "QML.Element",
        "TypeNotAvailable",
        "QML.AddedInVersion",
        "527",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "Type not available."
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
    });
    return QtMocHelpers::metaObjectData<QQmlTypeNotAvailable, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQmlTypeNotAvailable::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlTypeNotAvailableE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlTypeNotAvailableE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QQmlTypeNotAvailableE_t>.metaTypes,
    nullptr
} };

void QQmlTypeNotAvailable::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlTypeNotAvailable *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQmlTypeNotAvailable::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlTypeNotAvailable::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQmlTypeNotAvailableE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQmlTypeNotAvailable::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlTypeNotAvailable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlTypeNotAvailable10metaObjectEv(
    const QQmlTypeNotAvailable *self) {
  return self->metaObject();
}

//  void *QQmlTypeNotAvailable::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQmlTypeNotAvailable11qt_metacastEPKc(
    QQmlTypeNotAvailable *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTypeNotAvailable::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQmlTypeNotAvailable11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTypeNotAvailable *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlTypeNotAvailable::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlTypeNotAvailable2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTypeNotAvailable::tr(s, c, n));
}

//  void QQmlTypeNotAvailable::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeNotAvailable24qt_qmlMarker_uncreatableEv(
    QQmlTypeNotAvailable *self) {
  self->qt_qmlMarker_uncreatable();
}
