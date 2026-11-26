//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QAbstractScrollAreaFilter' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from QtWidgets__QAbstractScrollAreaFilter.cpp, line 1, as moc:QAbstractScrollAreaFilter
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t {};
} // unnamed namespace

template <> constexpr inline auto QAbstractScrollAreaFilter::qt_create_metaobjectdata<qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QAbstractScrollAreaFilter"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QAbstractScrollAreaFilter, qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QAbstractScrollAreaFilter::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>.metaTypes,
    nullptr
} };

void QAbstractScrollAreaFilter::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QAbstractScrollAreaFilter *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QAbstractScrollAreaFilter::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QAbstractScrollAreaFilter::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QAbstractScrollAreaFilterE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QAbstractScrollAreaFilter::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractScrollAreaFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractScrollAreaFilter10metaObjectEv(
    const QAbstractScrollAreaFilter *self) {
  return self->metaObject();
}

//  void *QAbstractScrollAreaFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QAbstractScrollAreaFilter11qt_metacastEPKc(
    QAbstractScrollAreaFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractScrollAreaFilter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QAbstractScrollAreaFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractScrollAreaFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractScrollAreaFilter::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QAbstractScrollAreaFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractScrollAreaFilter::tr(s, c, n));
}

//  QAbstractScrollAreaFilter::QAbstractScrollAreaFilter(QAbstractScrollAreaP
//      rivate *p)
extern "C" Q_DECL_EXPORT
QAbstractScrollAreaFilter *ritual_ZN25QAbstractScrollAreaFilterC1EP26QAbstractScrollAreaPrivate(
    QAbstractScrollAreaPrivate *p) {
  return new QAbstractScrollAreaFilter(p);
}

//  bool QAbstractScrollAreaFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractScrollAreaFilter11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollAreaFilter *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  bool QAbstractScrollAreaFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QAbstractScrollAreaFilter11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollAreaFilter *self,
    QObject *o,
    QEvent *e) {
  return self->QAbstractScrollAreaFilter::eventFilter(o, e);
}

#endif  // QT_CONFIG(scrollarea)
