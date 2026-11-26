//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'DeclarativePieSeries' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qpieslice.h>
#include <QtCore/qlist.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtChartsQml/private/declarativepieseries_p.h>
#include <QtCharts/QPieSlice>
#include <QtCharts/QVPieModelMapper>
#include <QtCharts/QHPieModelMapper>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtChartsQml__DeclarativePieSeries.cpp, line 1, as moc:DeclarativePieSeries
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20DeclarativePieSeriesE_t {};
} // unnamed namespace

template <> constexpr inline auto DeclarativePieSeries::qt_create_metaobjectdata<qt_meta_tag_ZN20DeclarativePieSeriesE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "DeclarativePieSeries",
        "DefaultProperty",
        "seriesChildren",
        "QML.Element",
        "PieSeries",
        "QML.AddedInVersion",
        "256",
        "QML.ExtraVersion",
        "512",
        "sliceAdded",
        "",
        "QPieSlice*",
        "slice",
        "sliceRemoved",
        "handleAdded",
        "QList<QPieSlice*>",
        "slices",
        "handleRemoved",
        "at",
        "index",
        "find",
        "label",
        "append",
        "DeclarativePieSlice*",
        "value",
        "remove",
        "clear",
        "QQmlListProperty<QObject>"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'sliceAdded'
        QtMocHelpers::SignalData<void(QPieSlice *)>(9, 10, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 11, 12 },
        }}),
        // Signal 'sliceRemoved'
        QtMocHelpers::SignalData<void(QPieSlice *)>(13, 10, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 11, 12 },
        }}),
        // Slot 'handleAdded'
        QtMocHelpers::SlotData<void(const QList<QPieSlice*> &)>(14, 10, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 },
        }}),
        // Slot 'handleRemoved'
        QtMocHelpers::SlotData<void(const QList<QPieSlice*> &)>(17, 10, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 },
        }}),
        // Method 'at'
        QtMocHelpers::MethodData<QPieSlice *(int)>(18, 10, QMC::AccessPublic, 0x80000000 | 11, {{
            { QMetaType::Int, 19 },
        }}),
        // Method 'find'
        QtMocHelpers::MethodData<QPieSlice *(QString)>(20, 10, QMC::AccessPublic, 0x80000000 | 11, {{
            { QMetaType::QString, 21 },
        }}),
        // Method 'append'
        QtMocHelpers::MethodData<DeclarativePieSlice *(QString, qreal)>(22, 10, QMC::AccessPublic, 0x80000000 | 23, {{
            { QMetaType::QString, 21 }, { QMetaType::QReal, 24 },
        }}),
        // Method 'remove'
        QtMocHelpers::MethodData<bool(QPieSlice *)>(25, 10, QMC::AccessPublic, QMetaType::Bool, {{
            { 0x80000000 | 11, 12 },
        }}),
        // Method 'clear'
        QtMocHelpers::MethodData<void()>(26, 10, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'seriesChildren'
        QtMocHelpers::PropertyData<QQmlListProperty<QObject>>(2, 0x80000000 | 27, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
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
    return QtMocHelpers::metaObjectData<DeclarativePieSeries, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject DeclarativePieSeries::staticMetaObject = { {
    QMetaObject::SuperData::link<QPieSeries::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20DeclarativePieSeriesE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20DeclarativePieSeriesE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20DeclarativePieSeriesE_t>.metaTypes,
    nullptr
} };

void DeclarativePieSeries::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<DeclarativePieSeries *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->sliceAdded((*reinterpret_cast<std::add_pointer_t<QPieSlice*>>(_a[1]))); break;
        case 1: _t->sliceRemoved((*reinterpret_cast<std::add_pointer_t<QPieSlice*>>(_a[1]))); break;
        case 2: _t->handleAdded((*reinterpret_cast<std::add_pointer_t<QList<QPieSlice*>>>(_a[1]))); break;
        case 3: _t->handleRemoved((*reinterpret_cast<std::add_pointer_t<QList<QPieSlice*>>>(_a[1]))); break;
        case 4: { QPieSlice* _r = _t->at((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QPieSlice**>(_a[0]) = std::move(_r); }  break;
        case 5: { QPieSlice* _r = _t->find((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QPieSlice**>(_a[0]) = std::move(_r); }  break;
        case 6: { DeclarativePieSlice* _r = _t->append((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<qreal>>(_a[2])));
            if (_a[0]) *reinterpret_cast<DeclarativePieSlice**>(_a[0]) = std::move(_r); }  break;
        case 7: { bool _r = _t->remove((*reinterpret_cast<std::add_pointer_t<QPieSlice*>>(_a[1])));
            if (_a[0]) *reinterpret_cast<bool*>(_a[0]) = std::move(_r); }  break;
        case 8: _t->clear(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QPieSlice* >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QPieSlice* >(); break;
            }
            break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QList<QPieSlice*> >(); break;
            }
            break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QList<QPieSlice*> >(); break;
            }
            break;
        case 7:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QPieSlice* >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (DeclarativePieSeries::*)(QPieSlice * )>(_a, &DeclarativePieSeries::sliceAdded, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (DeclarativePieSeries::*)(QPieSlice * )>(_a, &DeclarativePieSeries::sliceRemoved, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQmlListProperty<QObject>*>(_v) = _t->seriesChildren(); break;
        default: break;
        }
    }
}

const QMetaObject *DeclarativePieSeries::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *DeclarativePieSeries::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20DeclarativePieSeriesE_t>.strings))
        return static_cast<void*>(this);
    if (!strcmp(_clname, "QQmlParserStatus"))
        return static_cast< QQmlParserStatus*>(this);
    if (!strcmp(_clname, "org.qt-project.Qt.QQmlParserStatus"))
        return static_cast< QQmlParserStatus*>(this);
    return QPieSeries::qt_metacast(_clname);
}

int DeclarativePieSeries::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QPieSeries::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
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
void DeclarativePieSeries::sliceAdded(QPieSlice * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void DeclarativePieSeries::sliceRemoved(QPieSlice * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 55, as _ZN20DeclarativePieSeries10classBeginEv
inline void DeclarativePieSeries::classBegin()
{
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 127, as _ZN20DeclarativePieSeries11handleAddedERK5QListIP9QPieSliceE
inline void DeclarativePieSeries::handleAdded(const QList<QPieSlice *> &slices)
{
    for (auto *slice : slices)
        emit sliceAdded(slice);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 133, as _ZN20DeclarativePieSeries13handleRemovedERK5QListIP9QPieSliceE
inline void DeclarativePieSeries::handleRemoved(const QList<QPieSlice *> &slices)
{
    for (auto *slice : slices)
        emit sliceRemoved(slice);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 59, as _ZN20DeclarativePieSeries17componentCompleteEv
inline void DeclarativePieSeries::componentComplete()
{
    const auto childlist = children();
    for (QObject *child : childlist) {
        if (qobject_cast<QPieSlice *>(child)) {
            QPieSeries::append(qobject_cast<QPieSlice *>(child));
        } else if (qobject_cast<QVPieModelMapper *>(child)) {
            QVPieModelMapper *mapper = qobject_cast<QVPieModelMapper *>(child);
            mapper->setSeries(this);
        } else if (qobject_cast<QHPieModelMapper *>(child)) {
            QHPieModelMapper *mapper = qobject_cast<QHPieModelMapper *>(child);
            mapper->setSeries(this);
        }
    }
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 122, as _ZN20DeclarativePieSeries5clearEv
inline void DeclarativePieSeries::clear()
{
    QPieSeries::clear();
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 48, as _ZN20DeclarativePieSeriesC1EP10QQuickItem
inline DeclarativePieSeries::DeclarativePieSeries(QQuickItem *parent) :
    QPieSeries(parent)
{
    connect(this, SIGNAL(added(QList<QPieSlice*>)), this, SLOT(handleAdded(QList<QPieSlice*>)));
    connect(this, SIGNAL(removed(QList<QPieSlice*>)), this, SLOT(handleRemoved(QList<QPieSlice*>)));
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 75, as _ZN20DeclarativePieSeries14seriesChildrenEv
inline QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()
{
    return QQmlListProperty<QObject>(this, 0, &DeclarativePieSeries::appendSeriesChildren ,0,0,0);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 87, as _ZN20DeclarativePieSeries2atEi
inline QPieSlice *DeclarativePieSeries::at(int index)
{
    const QList<QPieSlice *> sliceList = slices();
    if (index >= 0 && index < sliceList.size())
        return sliceList.at(index);

    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 96, as _ZN20DeclarativePieSeries4findE7QString
inline QPieSlice *DeclarativePieSeries::find(QString label)
{
    const QList<QPieSlice *> sliceList = slices();
    for (auto *slice : sliceList) {
        if (slice->label() == label)
            return slice;
    }
    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 106, as _ZN20DeclarativePieSeries6appendE7QStringd
inline DeclarativePieSlice *DeclarativePieSeries::append(QString label, qreal value)
{
    DeclarativePieSlice *slice = new DeclarativePieSlice(this);
    slice->setLabel(label);
    slice->setValue(value);
    if (QPieSeries::append(slice))
        return slice;
    delete slice;
    return 0;
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 117, as _ZN20DeclarativePieSeries6removeEP9QPieSlice
inline bool DeclarativePieSeries::remove(QPieSlice *slice)
{
    return QPieSeries::remove(slice);
}

//  from ../qtcharts/src/chartsqml2/declarativepieseries.cpp, line 80, as _ZN20DeclarativePieSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_
inline void DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject> * list, QObject *element)
{
    // Empty implementation; the children are parsed in componentComplete instead
    Q_UNUSED(list);
    Q_UNUSED(element);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativePieSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20DeclarativePieSeries10metaObjectEv(
    const DeclarativePieSeries *self) {
  return self->metaObject();
}

//  void *DeclarativePieSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20DeclarativePieSeries11qt_metacastEPKc(
    DeclarativePieSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativePieSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20DeclarativePieSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativePieSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativePieSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20DeclarativePieSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativePieSeries::tr(s, c, n));
}

//  DeclarativePieSeries::DeclarativePieSeries(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
DeclarativePieSeries *ritual_ZN20DeclarativePieSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new DeclarativePieSeries(parent);
}

//  QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20DeclarativePieSeries14seriesChildrenEv(
    DeclarativePieSeries *self) {
  return new QQmlListProperty<QObject>(self->seriesChildren());
}

//  QPieSlice *DeclarativePieSeries::at(int index)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN20DeclarativePieSeries2atEi(
    DeclarativePieSeries *self,
    int index) {
  return self->at(index);
}

//  QPieSlice *DeclarativePieSeries::find(QString label)
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN20DeclarativePieSeries4findE7QString(
    DeclarativePieSeries *self,
    const QString *label) {
  return self->find(*label);
}

//  DeclarativePieSlice *DeclarativePieSeries::append(QString label, qreal
//      value)
extern "C" Q_DECL_EXPORT
DeclarativePieSlice *ritual_ZN20DeclarativePieSeries6appendE7QStringd(
    DeclarativePieSeries *self,
    const QString *label,
    qreal value) {
  return self->append(*label, value);
}

//  bool DeclarativePieSeries::remove(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20DeclarativePieSeries6removeEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  return self->remove(slice);
}

//  void DeclarativePieSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries5clearEv(DeclarativePieSeries *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries10classBeginEv(
    DeclarativePieSeries *self) {
  self->classBegin();
}

//  void DeclarativePieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries17componentCompleteEv(
    DeclarativePieSeries *self) {
  self->componentComplete();
}

//  void DeclarativePieSeries::sliceAdded(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries10sliceAddedEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sliceAdded(QPieSlice *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sliceAdded(QPieSlice *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&slice)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::sliceRemoved(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries12sliceRemovedEP9QPieSlice(
    DeclarativePieSeries *self,
    QPieSlice *slice) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sliceRemoved(QPieSlice *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sliceRemoved(QPieSlice *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&slice)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::handleAdded(const QList<QPieSlice *> &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries11handleAddedERK5QListIP9QPieSliceE(
    DeclarativePieSeries *self,
    const QList<QPieSlice *> *slices) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleAdded(const QList<QPieSlice *> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleAdded(const QList<QPieSlice *> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(slices)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::handleRemoved(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries13handleRemovedERK5QListIP9QPieSliceE(
    DeclarativePieSeries *self,
    const QList<QPieSlice *> *slices) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativePieSeries")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleRemoved(const QList<QPieSlice *> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleRemoved(const QList<QPieSlice *> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(slices)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject>
//      *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativePieSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativePieSeries::appendSeriesChildren(list, element);
}

//  DeclarativePieSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativePieSeries_QQmlParserStatus(
    DeclarativePieSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativePieSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativePieSeries10classBeginEv(
    DeclarativePieSeries *self) {
  self->DeclarativePieSeries::classBegin();
}

//  void DeclarativePieSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20DeclarativePieSeries17componentCompleteEv(
    DeclarativePieSeries *self) {
  self->DeclarativePieSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativePieSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativePieSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_pie_chart)
