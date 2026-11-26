//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'DeclarativeCategoryAxis'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtChartsQml/private/declarativecategoryaxis_p.h>
#include <QtCore/QDebug>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtChartsQml__DeclarativeCategoryAxis.cpp, line 1, as moc:DeclarativeCategoryAxis
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23DeclarativeCategoryAxisE_t {};
} // unnamed namespace

template <> constexpr inline auto DeclarativeCategoryAxis::qt_create_metaobjectdata<qt_meta_tag_ZN23DeclarativeCategoryAxisE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "DeclarativeCategoryAxis",
        "DefaultProperty",
        "axisChildren",
        "QML.Element",
        "CategoryAxis",
        "QML.AddedInVersion",
        "257",
        "QML.ExtraVersion",
        "512",
        "labelsPositionChanged",
        "",
        "AxisLabelsPosition",
        "position",
        "append",
        "label",
        "categoryEndValue",
        "remove",
        "replace",
        "oldLabel",
        "newLabel",
        "QQmlListProperty<QObject>",
        "labelsPosition",
        "AxisLabelsPositionCenter",
        "AxisLabelsPositionOnValue"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'labelsPositionChanged'
        QtMocHelpers::RevisionedSignalData<void(enum AxisLabelsPosition)>(9, 10, QMC::AccessPublic, 0x201, QMetaType::Void, {{
            { 0x80000000 | 11, 12 },
        }}),
        // Slot 'append'
        QtMocHelpers::SlotData<void(const QString &, qreal)>(13, 10, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 14 }, { QMetaType::QReal, 15 },
        }}),
        // Slot 'remove'
        QtMocHelpers::SlotData<void(const QString &)>(16, 10, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 14 },
        }}),
        // Slot 'replace'
        QtMocHelpers::SlotData<void(const QString &, const QString &)>(17, 10, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 18 }, { QMetaType::QString, 19 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'axisChildren'
        QtMocHelpers::PropertyData<QQmlListProperty<QObject>>(2, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'labelsPosition'
        QtMocHelpers::PropertyData<enum AxisLabelsPosition>(21, 0x80000000 | 11, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 0, 0x201),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'AxisLabelsPosition'
        QtMocHelpers::EnumData<enum AxisLabelsPosition>(11, 11, QMC::EnumFlags{}).add({
            {   22, AxisLabelsPosition::AxisLabelsPositionCenter },
            {   23, AxisLabelsPosition::AxisLabelsPositionOnValue },
        }),
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
    });
    return QtMocHelpers::metaObjectData<DeclarativeCategoryAxis, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject DeclarativeCategoryAxis::staticMetaObject = { {
    QMetaObject::SuperData::link<QCategoryAxis::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23DeclarativeCategoryAxisE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23DeclarativeCategoryAxisE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23DeclarativeCategoryAxisE_t>.metaTypes,
    nullptr
} };

void DeclarativeCategoryAxis::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<DeclarativeCategoryAxis *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->labelsPositionChanged((*reinterpret_cast<std::add_pointer_t<enum AxisLabelsPosition>>(_a[1]))); break;
        case 1: _t->append((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<qreal>>(_a[2]))); break;
        case 2: _t->remove((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1]))); break;
        case 3: _t->replace((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (DeclarativeCategoryAxis::*)(AxisLabelsPosition )>(_a, &DeclarativeCategoryAxis::labelsPositionChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQmlListProperty<QObject>*>(_v) = _t->axisChildren(); break;
        case 1: *reinterpret_cast<enum AxisLabelsPosition*>(_v) = _t->labelsPosition(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setLabelsPosition(*reinterpret_cast<enum AxisLabelsPosition*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *DeclarativeCategoryAxis::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *DeclarativeCategoryAxis::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23DeclarativeCategoryAxisE_t>.strings))
        return static_cast<void*>(this);
    if (!strcmp(_clname, "QQmlParserStatus"))
        return static_cast< QQmlParserStatus*>(this);
    if (!strcmp(_clname, "org.qt-project.Qt.QQmlParserStatus"))
        return static_cast< QQmlParserStatus*>(this);
    return QCategoryAxis::qt_metacast(_clname);
}

int DeclarativeCategoryAxis::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QCategoryAxis::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
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
void DeclarativeCategoryAxis::labelsPositionChanged(AxisLabelsPosition _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 57, as _ZN23DeclarativeCategoryAxis10classBeginEv
inline void DeclarativeCategoryAxis::classBegin()
{
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 61, as _ZN23DeclarativeCategoryAxis17componentCompleteEv
inline void DeclarativeCategoryAxis::componentComplete()
{
    QList<QPair<QString, qreal> > ranges;
    const auto childlist = children();
    for (QObject *child : childlist) {
        if (qobject_cast<DeclarativeCategoryRange *>(child)) {
            DeclarativeCategoryRange *range = qobject_cast<DeclarativeCategoryRange *>(child);
            ranges.append(QPair<QString, qreal>(range->label(), range->endValue()));
        }
    }

    // Sort and append the range objects according to end value
    std::sort(ranges.begin(), ranges.end(), endValueLessThan);
    for (int i(0); i < ranges.size(); i++)
        append(ranges.at(i).first, ranges.at(i).second);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 88, as _ZN23DeclarativeCategoryAxis6appendERK7QStringd
inline void DeclarativeCategoryAxis::append(const QString &label, qreal categoryEndValue)
{
    QCategoryAxis::append(label, categoryEndValue);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 93, as _ZN23DeclarativeCategoryAxis6removeERK7QString
inline void DeclarativeCategoryAxis::remove(const QString &label)
{
    QCategoryAxis::remove(label);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 98, as _ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_
inline void DeclarativeCategoryAxis::replace(const QString &oldLabel, const QString &newLabel)
{
    QCategoryAxis::replaceLabel(oldLabel, newLabel);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 51, as _ZN23DeclarativeCategoryAxisC1EP7QObject
inline DeclarativeCategoryAxis::DeclarativeCategoryAxis(QObject *parent) :
    QCategoryAxis(parent),
    m_labelsPosition(AxisLabelsPositionCenter)
{
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 83, as _ZN23DeclarativeCategoryAxis12axisChildrenEv
inline QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()
{
    return QQmlListProperty<QObject>(this, 0, &DeclarativeCategoryAxis::appendAxisChildren ,0,0,0);
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 110, as _ZNK23DeclarativeCategoryAxis14labelsPositionEv
inline DeclarativeCategoryAxis::AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
{
    return (DeclarativeCategoryAxis::AxisLabelsPosition) QCategoryAxis::labelsPosition();
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 115, as _ZN23DeclarativeCategoryAxis17setLabelsPositionENS_18AxisLabelsPositionE
inline void DeclarativeCategoryAxis::setLabelsPosition(AxisLabelsPosition position)
{
    if (position != m_labelsPosition) {
        QCategoryAxis::setLabelsPosition((QCategoryAxis::AxisLabelsPosition)position);
        emit labelsPositionChanged(position);
    }
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 78, as _ZN23DeclarativeCategoryAxis16endValueLessThanERKSt4pairI7QStringdES4_
inline bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString, qreal> &value1, const QPair<QString, qreal> &value2)
{
    return value1.second < value2.second;
}

//  from ../qtcharts/src/chartsqml2/declarativecategoryaxis.cpp, line 103, as _ZN23DeclarativeCategoryAxis18appendAxisChildrenEP16QQmlListPropertyI7QObjectEPS1_
inline void DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject> *list, QObject *element)
{
    // Empty implementation; the children are parsed in componentComplete instead
    Q_UNUSED(list);
    Q_UNUSED(element);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *DeclarativeCategoryAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23DeclarativeCategoryAxis10metaObjectEv(
    const DeclarativeCategoryAxis *self) {
  return self->metaObject();
}

//  void *DeclarativeCategoryAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23DeclarativeCategoryAxis11qt_metacastEPKc(
    DeclarativeCategoryAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23DeclarativeCategoryAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeCategoryAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeCategoryAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23DeclarativeCategoryAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeCategoryAxis::tr(s, c, n));
}

//  DeclarativeCategoryAxis::DeclarativeCategoryAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeCategoryAxis *ritual_ZN23DeclarativeCategoryAxisC1EP7QObject(
    QObject *parent) {
  return new DeclarativeCategoryAxis(parent);
}

//  QQmlListProperty<QObject> DeclarativeCategoryAxis::axisChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN23DeclarativeCategoryAxis12axisChildrenEv(
    DeclarativeCategoryAxis *self) {
  return new QQmlListProperty<QObject>(self->axisChildren());
}

//  void DeclarativeCategoryAxis::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis10classBeginEv(
    DeclarativeCategoryAxis *self) {
  self->classBegin();
}

//  void DeclarativeCategoryAxis::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis17componentCompleteEv(
    DeclarativeCategoryAxis *self) {
  self->componentComplete();
}

//  AxisLabelsPosition DeclarativeCategoryAxis::labelsPosition() const
extern "C" Q_DECL_EXPORT
DeclarativeCategoryAxis::AxisLabelsPosition ritual_ZNK23DeclarativeCategoryAxis14labelsPositionEv(
    const DeclarativeCategoryAxis *self) {
  return self->labelsPosition();
}

//  void DeclarativeCategoryAxis::setLabelsPosition(AxisLabelsPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis17setLabelsPositionENS_18AxisLabelsPositionE(
    DeclarativeCategoryAxis *self,
    DeclarativeCategoryAxis::AxisLabelsPosition position) {
  self->setLabelsPosition(position);
}

//  void DeclarativeCategoryAxis::labelsPositionChanged(AxisLabelsPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis21labelsPositionChangedENS_18AxisLabelsPositionE(
    DeclarativeCategoryAxis *self,
    DeclarativeCategoryAxis::AxisLabelsPosition position) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "labelsPositionChanged(AxisLabelsPosition)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "labelsPositionChanged(AxisLabelsPosition)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&position)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::append(const QString &label, qreal
//      categoryEndValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6appendERK7QStringd(
    DeclarativeCategoryAxis *self,
    const QString *label,
    qreal categoryEndValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "append(const QString &,qreal)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "append(const QString &,qreal)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(label)),
      const_cast<void *>(static_cast<const void *>(&categoryEndValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::remove(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis6removeERK7QString(
    DeclarativeCategoryAxis *self,
    const QString *label) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remove(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remove(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(label)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DeclarativeCategoryAxis::replace(const QString &oldLabel, const
//      QString &newLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis7replaceERK7QStringS2_(
    DeclarativeCategoryAxis *self,
    const QString *oldLabel,
    const QString *newLabel) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DeclarativeCategoryAxis")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "replace(const QString &,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "replace(const QString &,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(oldLabel)),
      const_cast<void *>(static_cast<const void *>(newLabel)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool DeclarativeCategoryAxis::endValueLessThan(const QPair<QString,
//      qreal> &value1, const QPair<QString, qreal> &value2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23DeclarativeCategoryAxis16endValueLessThanERKSt4pairI7QStringdES4_(
    const QPair<QString, qreal> *value1,
    const QPair<QString, qreal> *value2) {
  return DeclarativeCategoryAxis::endValueLessThan(*value1, *value2);
}

//  void
//      DeclarativeCategoryAxis::appendAxisChildren(QQmlListProperty<QObject>
//      *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeCategoryAxis18appendAxisChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeCategoryAxis::appendAxisChildren(list, element);
}

//  DeclarativeCategoryAxis as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeCategoryAxis_QQmlParserStatus(
    DeclarativeCategoryAxis *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void DeclarativeCategoryAxis::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeCategoryAxis10classBeginEv(
    DeclarativeCategoryAxis *self) {
  self->DeclarativeCategoryAxis::classBegin();
}

//  void DeclarativeCategoryAxis::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeCategoryAxis17componentCompleteEv(
    DeclarativeCategoryAxis *self) {
  self->DeclarativeCategoryAxis::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeCategoryAxis gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeCategoryAxis__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
