//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QCustomSeriesData' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/QDataStream>
#include <QtGraphs/private/qcustomseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__QCustomSeriesData.cpp, line 1, as moc:QCustomSeriesData
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QCustomSeriesDataE_t {};
} // unnamed namespace

template <> constexpr inline auto QCustomSeriesData::qt_create_metaobjectdata<qt_meta_tag_ZN17QCustomSeriesDataE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QCustomSeriesData",
        "QML.Element",
        "CustomSeriesData",
        "QML.AddedInVersion",
        "1547",
        "data",
        "QVariantMap"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'data'
        QtMocHelpers::PropertyData<QVariantMap>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QCustomSeriesData, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QCustomSeriesData::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QCustomSeriesDataE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QCustomSeriesDataE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QCustomSeriesDataE_t>.metaTypes,
    nullptr
} };

void QCustomSeriesData::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QCustomSeriesData *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QVariantMap*>(_v) = _t->data(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setData(*reinterpret_cast<QVariantMap*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QCustomSeriesData::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QCustomSeriesData::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QCustomSeriesDataE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QCustomSeriesData::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/customchart/qcustomseriesdata.cpp, line 11, as _ZN17QCustomSeriesDataC1EP7QObject
inline QCustomSeriesData::QCustomSeriesData(QObject *parent)
    : QObject(parent)
{}

//  from ../qtgraphs/src/graphs2d/customchart/qcustomseriesdata.cpp, line 15, as _ZNK17QCustomSeriesData4dataEv
inline QVariantMap QCustomSeriesData::data() const
{
    return m_data;
}

//  from ../qtgraphs/src/graphs2d/customchart/qcustomseriesdata.cpp, line 20, as _ZN17QCustomSeriesData7setDataERK4QMapI7QString8QVariantE
inline void QCustomSeriesData::setData(const QVariantMap &newData)
{
    m_data = newData;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QCustomSeriesData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QCustomSeriesData10metaObjectEv(
    const QCustomSeriesData *self) {
  return self->metaObject();
}

//  void *QCustomSeriesData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QCustomSeriesData11qt_metacastEPKc(
    QCustomSeriesData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustomSeriesData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QCustomSeriesData11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustomSeriesData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustomSeriesData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QCustomSeriesData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustomSeriesData::tr(s, c, n));
}

//  QCustomSeriesData::QCustomSeriesData(QObject *parent)
extern "C" Q_DECL_EXPORT
QCustomSeriesData *ritual_ZN17QCustomSeriesDataC1EP7QObject(
    QObject *parent) {
  return new QCustomSeriesData(parent);
}

//  QVariantMap QCustomSeriesData::data() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK17QCustomSeriesData4dataEv(
    const QCustomSeriesData *self) {
  return new QMap<QString, QVariant>(self->data());
}

//  void QCustomSeriesData::setData(const QVariantMap &newData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCustomSeriesData7setDataERK4QMapI7QString8QVariantE(
    QCustomSeriesData *self,
    const QMap<QString, QVariant> *newData) {
  self->setData(*newData);
}

//  QList<QCustomSeriesData *>::QList()
extern "C" Q_DECL_EXPORT
QList<QCustomSeriesData *> *ritual_list_make_QCustomSeriesData_ptr() {
  return new QList<QCustomSeriesData *>();
}

//  void QList<QCustomSeriesData *>::append(const QCustomSeriesData * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCustomSeriesData_ptr(
    QList<QCustomSeriesData *> *self,
    QCustomSeriesData *element) {
  self->append(element);
}

//  qsizetype QList<QCustomSeriesData *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCustomSeriesData_ptr(
    const QList<QCustomSeriesData *> *self) {
  return self->size();
}

//  const QCustomSeriesData * &QList<QCustomSeriesData *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QCustomSeriesData *ritual_list_at_QCustomSeriesData_ptr(
    const QList<QCustomSeriesData *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QCustomSeriesData *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCustomSeriesData_ptr(
    QList<QCustomSeriesData *> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
