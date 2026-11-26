//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickDayOfWeekModel' is
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
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
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
#include <QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 11, as local:qquickdayofweekmodel.cpp:QQuickDayOfWeekModelPrivate
class QQuickDayOfWeekModelPrivate : public QAbstractItemModelPrivate
{
    Q_DECLARE_PUBLIC(QQuickDayOfWeekModel)

public:
    QLocale locale;
};

//  from QtQuickTemplates2__QQuickDayOfWeekModel.cpp, line 1, as moc:QQuickDayOfWeekModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QQuickDayOfWeekModelE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickDayOfWeekModel::qt_create_metaobjectdata<qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickDayOfWeekModel",
        "localeChanged",
        "",
        "dayAt",
        "index",
        "locale",
        "count"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'localeChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Method 'dayAt'
        QtMocHelpers::MethodData<int(int) const>(3, 2, QMC::AccessPublic, QMetaType::Int, {{
            { QMetaType::Int, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'locale'
        QtMocHelpers::PropertyData<QLocale>(5, QMetaType::QLocale, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'count'
        QtMocHelpers::PropertyData<int>(6, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Constant | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickDayOfWeekModel, qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickDayOfWeekModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractListModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>.metaTypes,
    nullptr
} };

void QQuickDayOfWeekModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickDayOfWeekModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->localeChanged(); break;
        case 1: { int _r = _t->dayAt((*reinterpret_cast<std::add_pointer_t<int>>(_a[1])));
            if (_a[0]) *reinterpret_cast<int*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickDayOfWeekModel::*)()>(_a, &QQuickDayOfWeekModel::localeChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QLocale*>(_v) = _t->locale(); break;
        case 1: *reinterpret_cast<int*>(_v) = _t->rowCount(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setLocale(*reinterpret_cast<QLocale*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickDayOfWeekModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickDayOfWeekModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQuickDayOfWeekModelE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractListModel::qt_metacast(_clname);
}

int QQuickDayOfWeekModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractListModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
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
void QQuickDayOfWeekModel::localeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 30, as _ZN20QQuickDayOfWeekModel9setLocaleERK7QLocale
inline void QQuickDayOfWeekModel::setLocale(const QLocale &locale)
{
    Q_D(QQuickDayOfWeekModel);
    if (d->locale != locale) {
        d->locale = locale;
        emit localeChanged();
        emit dataChanged(index(0, 0), index(6, 0));
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 51, as _ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi
inline QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role) const
{
    Q_D(const QQuickDayOfWeekModel);
    if (index.isValid() && index.row() < 7) {
        int day = dayAt(index.row());
        switch (role) {
        case DayRole:
            return day;
        case LongNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::LongFormat);
        case ShortNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::ShortFormat);
        case NarrowNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::NarrowFormat);
        default:
            break;
        }
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 40, as _ZNK20QQuickDayOfWeekModel5dayAtEi
inline int QQuickDayOfWeekModel::dayAt(int index) const
{
    Q_D(const QQuickDayOfWeekModel);
    int day = d->locale.firstDayOfWeek() + index;
    if (day > 7)
        day -= 7;
    if (day == 7)
        day = 0; // Qt::Sunday = 7, but Sunday is 0 in JS Date
    return day;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 24, as _ZNK20QQuickDayOfWeekModel6localeEv
inline QLocale QQuickDayOfWeekModel::locale() const
{
    Q_D(const QQuickDayOfWeekModel);
    return d->locale;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 72, as _ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex
inline int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 7;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 79, as _ZNK20QQuickDayOfWeekModel9roleNamesEv
inline QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[DayRole] = QByteArrayLiteral("day");
    roles[LongNameRole] = QByteArrayLiteral("longName");
    roles[ShortNameRole] = QByteArrayLiteral("shortName");
    roles[NarrowNameRole] = QByteArrayLiteral("narrowName");
    return roles;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 19, as _ZN20QQuickDayOfWeekModelC1EP7QObject
inline QQuickDayOfWeekModel::QQuickDayOfWeekModel(QObject *parent) :
    QAbstractListModel(*(new QQuickDayOfWeekModelPrivate), parent)
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDayOfWeekModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickDayOfWeekModel10metaObjectEv(
    const QQuickDayOfWeekModel *self) {
  return self->metaObject();
}

//  void *QQuickDayOfWeekModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickDayOfWeekModel11qt_metacastEPKc(
    QQuickDayOfWeekModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDayOfWeekModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickDayOfWeekModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDayOfWeekModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDayOfWeekModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickDayOfWeekModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDayOfWeekModel::tr(s, c, n));
}

//  QQuickDayOfWeekModel::QQuickDayOfWeekModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDayOfWeekModel *ritual_ZN20QQuickDayOfWeekModelC1EP7QObject(
    QObject *parent) {
  return new QQuickDayOfWeekModel(parent);
}

//  QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK20QQuickDayOfWeekModel9roleNamesEv(
    const QQuickDayOfWeekModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickDayOfWeekModel::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickDayOfWeekModel13localeChangedEv(
    QQuickDayOfWeekModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDayOfWeekModel")) {
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

//  QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickDayOfWeekModelPrivate *ritual_ZN20QQuickDayOfWeekModel6d_funcEv(
    QQuickDayOfWeekModel *self) {
  return self->d_func();
}

//  const QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDayOfWeekModelPrivate *ritual_ZNK20QQuickDayOfWeekModel6d_funcEv(
    const QQuickDayOfWeekModel *self) {
  return self->d_func();
}

//  QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickDayOfWeekModel::data(*index, role));
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->QQuickDayOfWeekModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
