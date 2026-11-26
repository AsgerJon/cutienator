//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickWeekNumberModel' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 12, as local:qquickweeknumbermodel.cpp:QQuickWeekNumberModelPrivate
class QQuickWeekNumberModelPrivate : public QAbstractItemModelPrivate
{
    Q_DECLARE_PUBLIC(QQuickWeekNumberModel)

public:
    QQuickWeekNumberModelPrivate() : month(-1), year(-1), weekNumbers{}
    {
        QDate date = QDate::currentDate();
        init(date.month(), date.year(), locale);
        month = date.month();
        year = date.year();
    }

    void init(int month, int year, const QLocale &locale = QLocale());
    static QDate calculateFirst(int month, int year, const QLocale &locale);

    int month;
    int year;
    QLocale locale;
    int weekNumbers[6];
};

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 34, as local:qquickweeknumbermodel.cpp:QQuickWeekNumberModelPrivate::init
inline void QQuickWeekNumberModelPrivate::init(int m, int y, const QLocale &l)
{
    Q_Q(QQuickWeekNumberModel);
    if (m == month && y == year && l.firstDayOfWeek() == locale.firstDayOfWeek())
        return;

    // The actual first (1st) day of the month.
    QDate firstDayOfMonthDate(y, m, 1);
    int difference = ((firstDayOfMonthDate.dayOfWeek() - l.firstDayOfWeek()) + 7) % 7;
    // The first day to display should never be the 1st of the month, as we want some days from
    // the previous month to be visible.
    if (difference == 0)
        difference += 7;

    for (int i = 0; i < 6; ++i)
        weekNumbers[i] = firstDayOfMonthDate.addDays(i * 7 - difference).weekNumber();

    if (q) // null at construction
        emit q->dataChanged(q->index(0, 0), q->index(5, 0));
}

//  from QtQuickTemplates2__QQuickWeekNumberModel.cpp, line 1, as moc:QQuickWeekNumberModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN21QQuickWeekNumberModelE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickWeekNumberModel::qt_create_metaobjectdata<qt_meta_tag_ZN21QQuickWeekNumberModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickWeekNumberModel",
        "monthChanged",
        "",
        "yearChanged",
        "localeChanged",
        "weekNumberAt",
        "index",
        "indexOf",
        "weekNumber",
        "month",
        "year",
        "locale",
        "count"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'monthChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'yearChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'localeChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Method 'weekNumberAt'
        QtMocHelpers::MethodData<int(int) const>(5, 2, QMC::AccessPublic, QMetaType::Int, {{
            { QMetaType::Int, 6 },
        }}),
        // Method 'indexOf'
        QtMocHelpers::MethodData<int(int) const>(7, 2, QMC::AccessPublic, QMetaType::Int, {{
            { QMetaType::Int, 8 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'month'
        QtMocHelpers::PropertyData<int>(9, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'year'
        QtMocHelpers::PropertyData<int>(10, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
        // property 'locale'
        QtMocHelpers::PropertyData<QLocale>(11, QMetaType::QLocale, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 2),
        // property 'count'
        QtMocHelpers::PropertyData<int>(12, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Constant | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickWeekNumberModel, qt_meta_tag_ZN21QQuickWeekNumberModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickWeekNumberModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractListModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickWeekNumberModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickWeekNumberModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN21QQuickWeekNumberModelE_t>.metaTypes,
    nullptr
} };

void QQuickWeekNumberModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickWeekNumberModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->monthChanged(); break;
        case 1: _t->yearChanged(); break;
        case 2: _t->localeChanged(); break;
        case 3: { int _r = _t->weekNumberAt((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])));
            if (_a[0]) *reinterpret_cast<int*>(_a[0]) = std::move(_r); }  break;
        case 4: { int _r = _t->indexOf((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])));
            if (_a[0]) *reinterpret_cast<int*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickWeekNumberModel::*)()>(_a, &QQuickWeekNumberModel::monthChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickWeekNumberModel::*)()>(_a, &QQuickWeekNumberModel::yearChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickWeekNumberModel::*)()>(_a, &QQuickWeekNumberModel::localeChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<int*>(_v) = _t->month(); break;
        case 1: *reinterpret_cast<int*>(_v) = _t->year(); break;
        case 2: *reinterpret_cast<QLocale*>(_v) = _t->locale(); break;
        case 3: *reinterpret_cast<int*>(_v) = _t->rowCount(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setMonth(*reinterpret_cast<int*>(_v)); break;
        case 1: _t->setYear(*reinterpret_cast<int*>(_v)); break;
        case 2: _t->setLocale(*reinterpret_cast<QLocale*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickWeekNumberModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickWeekNumberModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickWeekNumberModelE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractListModel::qt_metacast(_clname);
}

int QQuickWeekNumberModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractListModel::qt_metacall(_c, _id, _a);
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
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void QQuickWeekNumberModel::monthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickWeekNumberModel::yearChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuickWeekNumberModel::localeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 82, as _ZN21QQuickWeekNumberModel7setYearEi
inline void QQuickWeekNumberModel::setYear(int year)
{
    Q_D(QQuickWeekNumberModel);
    if (d->year != year) {
        d->init(d->month, year, d->locale);
        d->year = year;
        emit yearChanged();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 66, as _ZN21QQuickWeekNumberModel8setMonthEi
inline void QQuickWeekNumberModel::setMonth(int month)
{
    Q_D(QQuickWeekNumberModel);
    if (d->month != month) {
        d->init(month, d->year, d->locale);
        d->month = month;
        emit monthChanged();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 98, as _ZN21QQuickWeekNumberModel9setLocaleERK7QLocale
inline void QQuickWeekNumberModel::setLocale(const QLocale &locale)
{
    Q_D(QQuickWeekNumberModel);
    if (d->locale != locale) {
        d->init(d->month, d->year, locale);
        d->locale = locale;
        emit localeChanged();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 108, as _ZNK21QQuickWeekNumberModel12weekNumberAtEi
inline int QQuickWeekNumberModel::weekNumberAt(int index) const
{
    Q_D(const QQuickWeekNumberModel);
    if (index < 0 || index > 5)
        return -1;
    return d->weekNumbers[index];
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 124, as _ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi
inline QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role) const
{
    if (role == WeekNumberRole) {
        int weekNumber = weekNumberAt(index.row());
        if (weekNumber != -1)
            return weekNumber;
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 76, as _ZNK21QQuickWeekNumberModel4yearEv
inline int QQuickWeekNumberModel::year() const
{
    Q_D(const QQuickWeekNumberModel);
    return d->year;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 60, as _ZNK21QQuickWeekNumberModel5monthEv
inline int QQuickWeekNumberModel::month() const
{
    Q_D(const QQuickWeekNumberModel);
    return d->month;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 92, as _ZNK21QQuickWeekNumberModel6localeEv
inline QLocale QQuickWeekNumberModel::locale() const
{
    Q_D(const QQuickWeekNumberModel);
    return d->locale;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 116, as _ZNK21QQuickWeekNumberModel7indexOfEi
inline int QQuickWeekNumberModel::indexOf(int weekNumber) const
{
    Q_D(const QQuickWeekNumberModel);
    if (weekNumber < d->weekNumbers[0] || weekNumber > d->weekNumbers[5])
        return -1;
    return weekNumber - d->weekNumbers[0];
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 134, as _ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex
inline int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 6;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 141, as _ZNK21QQuickWeekNumberModel9roleNamesEv
inline QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[WeekNumberRole] = QByteArrayLiteral("weekNumber");
    return roles;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 55, as _ZN21QQuickWeekNumberModelC1EP7QObject
inline QQuickWeekNumberModel::QQuickWeekNumberModel(QObject *parent) :
    QAbstractListModel(*(new QQuickWeekNumberModelPrivate), parent)
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickWeekNumberModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWeekNumberModel10metaObjectEv(
    const QQuickWeekNumberModel *self) {
  return self->metaObject();
}

//  void *QQuickWeekNumberModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickWeekNumberModel11qt_metacastEPKc(
    QQuickWeekNumberModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWeekNumberModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickWeekNumberModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWeekNumberModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWeekNumberModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickWeekNumberModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWeekNumberModel::tr(s, c, n));
}

//  QQuickWeekNumberModel::QQuickWeekNumberModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWeekNumberModel *ritual_ZN21QQuickWeekNumberModelC1EP7QObject(
    QObject *parent) {
  return new QQuickWeekNumberModel(parent);
}

//  QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK21QQuickWeekNumberModel9roleNamesEv(
    const QQuickWeekNumberModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi(
    const QQuickWeekNumberModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickWeekNumberModel::monthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel12monthChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "monthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "monthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickWeekNumberModel::yearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel11yearChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yearChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yearChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickWeekNumberModel::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel13localeChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "localeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "localeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickWeekNumberModelPrivate *ritual_ZN21QQuickWeekNumberModel6d_funcEv(
    QQuickWeekNumberModel *self) {
  return self->d_func();
}

//  const QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWeekNumberModelPrivate *ritual_ZNK21QQuickWeekNumberModel6d_funcEv(
    const QQuickWeekNumberModel *self) {
  return self->d_func();
}

//  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi(
    const QQuickWeekNumberModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickWeekNumberModel::data(*index, role));
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->QQuickWeekNumberModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
