//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QDeclarativeGeoMapPainterPath' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from QtLocation__QDeclarativeGeoMapPainterPath.cpp, line 1, as moc:QDeclarativeGeoMapPainterPath
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t {};
} // unnamed namespace

template <> constexpr inline auto QDeclarativeGeoMapPainterPath::qt_create_metaobjectdata<qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QDeclarativeGeoMapPainterPath"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QDeclarativeGeoMapPainterPath, qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QDeclarativeGeoMapPainterPath::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickCurve::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>.metaTypes,
    nullptr
} };

void QDeclarativeGeoMapPainterPath::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QDeclarativeGeoMapPainterPath *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QDeclarativeGeoMapPainterPath::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QDeclarativeGeoMapPainterPath::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QDeclarativeGeoMapPainterPathE_t>.strings))
        return static_cast<void*>(this);
    return QQuickCurve::qt_metacast(_clname);
}

int QDeclarativeGeoMapPainterPath::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickCurve::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *QDeclarativeGeoMapPainterPath::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativeGeoMapPainterPath10metaObjectEv(
    const QDeclarativeGeoMapPainterPath *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoMapPainterPath::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QDeclarativeGeoMapPainterPath11qt_metacastEPKc(
    QDeclarativeGeoMapPainterPath *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoMapPainterPath::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QDeclarativeGeoMapPainterPath11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoMapPainterPath *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoMapPainterPath::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDeclarativeGeoMapPainterPath2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoMapPainterPath::tr(s, c, n));
}

//  QDeclarativeGeoMapPainterPath::QDeclarativeGeoMapPainterPath(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapPainterPath *ritual_ZN29QDeclarativeGeoMapPainterPathC1EP7QObject(
    QObject *parent) {
  return new QDeclarativeGeoMapPainterPath(parent);
}

//  QPainterPath QDeclarativeGeoMapPainterPath::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK29QDeclarativeGeoMapPainterPath4pathEv(
    const QDeclarativeGeoMapPainterPath *self) {
  return new QPainterPath(self->path());
}

//  void QDeclarativeGeoMapPainterPath::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeGeoMapPainterPath7setPathERK12QPainterPath(
    QDeclarativeGeoMapPainterPath *self,
    const QPainterPath *path) {
  self->setPath(*path);
}

//  void QDeclarativeGeoMapPainterPath::addToPath(QPainterPath &path, const
//      QQuickPathData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeGeoMapPainterPath9addToPathER12QPainterPathRK14QQuickPathData(
    QDeclarativeGeoMapPainterPath *self,
    QPainterPath *path,
    const QQuickPathData *a1) {
  self->addToPath(*path, *a1);
}
