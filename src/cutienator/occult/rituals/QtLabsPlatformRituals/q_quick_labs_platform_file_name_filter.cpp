//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickLabsPlatformFileNameFilter' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 4 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/qlist.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 586, as local:qquicklabsplatformfiledialog.cpp:extractName
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractName(const QString &filter)
{
    return filter.left(filter.indexOf(QLatin1Char('(')) - 1);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 591, as local:qquicklabsplatformfiledialog.cpp:extractExtension
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractExtension(QStringView filter)
{
    return filter.mid(filter.indexOf(QLatin1Char('.')) + 1).toString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 596, as local:qquicklabsplatformfiledialog.cpp:extractExtensions
#if QT_DEPRECATED_SINCE(6, 9)
static QStringList extractExtensions(QStringView filter)
{
    QStringList extensions;
    const int from = filter.indexOf(QLatin1Char('('));
    const int to = filter.lastIndexOf(QLatin1Char(')')) - 1;
    if (from >= 0 && from < to) {
        const QStringView ref = filter.mid(from + 1, to - from);
        const QList<QStringView> exts = ref.split(QLatin1Char(' '), Qt::SkipEmptyParts);
        for (const QStringView &ref : exts)
            extensions += extractExtension(ref);
    }

    return extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from QtLabsPlatform__QQuickLabsPlatformFileNameFilter.cpp, line 1, as moc:QQuickLabsPlatformFileNameFilter
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickLabsPlatformFileNameFilter::qt_create_metaobjectdata<qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickLabsPlatformFileNameFilter",
        "QML.Element",
        "anonymous",
        "QML.AddedInVersion",
        "256",
        "indexChanged",
        "",
        "index",
        "nameChanged",
        "name",
        "extensionsChanged",
        "extensions"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'indexChanged'
        QtMocHelpers::SignalData<void(int)>(5, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 7 },
        }}),
        // Signal 'nameChanged'
        QtMocHelpers::SignalData<void(const QString &)>(8, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 9 },
        }}),
        // Signal 'extensionsChanged'
        QtMocHelpers::SignalData<void(const QStringList &)>(10, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QStringList, 11 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'index'
        QtMocHelpers::PropertyData<int>(7, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'name'
        QtMocHelpers::PropertyData<QString>(9, QMetaType::QString, QMC::DefaultPropertyFlags | QMC::Final, 1),
        // property 'extensions'
        QtMocHelpers::PropertyData<QStringList>(11, QMetaType::QStringList, QMC::DefaultPropertyFlags | QMC::Final, 2),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickLabsPlatformFileNameFilter, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickLabsPlatformFileNameFilter::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t>.metaTypes,
    nullptr
} };

void QQuickLabsPlatformFileNameFilter::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickLabsPlatformFileNameFilter *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->indexChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 1: _t->nameChanged((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1]))); break;
        case 2: _t->extensionsChanged((*reinterpret_cast<std::add_pointer_t<QStringList>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickLabsPlatformFileNameFilter::*)(int )>(_a, &QQuickLabsPlatformFileNameFilter::indexChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickLabsPlatformFileNameFilter::*)(const QString & )>(_a, &QQuickLabsPlatformFileNameFilter::nameChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickLabsPlatformFileNameFilter::*)(const QStringList & )>(_a, &QQuickLabsPlatformFileNameFilter::extensionsChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<int*>(_v) = _t->index(); break;
        case 1: *reinterpret_cast<QString*>(_v) = _t->name(); break;
        case 2: *reinterpret_cast<QStringList*>(_v) = _t->extensions(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setIndex(*reinterpret_cast<int*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickLabsPlatformFileNameFilter::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickLabsPlatformFileNameFilter::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN32QQuickLabsPlatformFileNameFilterE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickLabsPlatformFileNameFilter::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
void QQuickLabsPlatformFileNameFilter::indexChanged(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QQuickLabsPlatformFileNameFilter::nameChanged(const QString & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void QQuickLabsPlatformFileNameFilter::extensionsChanged(const QStringList & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 547, as _ZN32QQuickLabsPlatformFileNameFilterC1EP7QObject
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter(QObject *parent)
    : QObject(parent), m_index(-1)
{
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 552, as _ZNK32QQuickLabsPlatformFileNameFilter5indexEv
#if QT_DEPRECATED_SINCE(6, 9)
inline int QQuickLabsPlatformFileNameFilter::index() const
{
    return m_index;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 557, as _ZN32QQuickLabsPlatformFileNameFilter8setIndexEi
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::setIndex(int index)
{
    if (m_index == index)
        return;

    m_index = index;
    emit indexChanged(index);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 566, as _ZNK32QQuickLabsPlatformFileNameFilter4nameEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::name() const
{
    return m_name;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 571, as _ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::extensions() const
{
    return m_extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 576, as _ZNK32QQuickLabsPlatformFileNameFilter7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QSharedPointer<QFileDialogOptions> QQuickLabsPlatformFileNameFilter::options() const
{
    return m_options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 581, as _ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::setOptions(const QSharedPointer<QFileDialogOptions> &options)
{
    m_options = options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 611, as _ZN32QQuickLabsPlatformFileNameFilter6updateERK7QString
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::update(const QString &filter)
{
    const QStringList filters = nameFilters();

    const int oldIndex = m_index;
    const QString oldName = m_name;
    const QStringList oldExtensions = m_extensions;

    m_index = filters.indexOf(filter);
    m_name = extractName(filter);
    m_extensions = extractExtensions(filter);

    if (oldIndex != m_index)
        emit indexChanged(m_index);
    if (oldName != m_name)
        emit nameChanged(m_name);
    if (oldExtensions != m_extensions)
        emit extensionsChanged(m_extensions);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 631, as _ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
{
    return m_options ? m_options->nameFilters() : QStringList();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 636, as _ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
{
    return m_options ? m_options->nameFilters().value(index) : QString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLabsPlatformFileNameFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickLabsPlatformFileNameFilter10metaObjectEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformFileNameFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickLabsPlatformFileNameFilter11qt_metacastEPKc(
    QQuickLabsPlatformFileNameFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformFileNameFilter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickLabsPlatformFileNameFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformFileNameFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickLabsPlatformFileNameFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLabsPlatformFileNameFilter::tr(s, c, n));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformFileNameFilter::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter22qt_qmlMarker_anonymousEv(
    QQuickLabsPlatformFileNameFilter *self) {
  self->qt_qmlMarker_anonymous();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter(QObjec
//      t *parent)
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformFileNameFilter *ritual_ZN32QQuickLabsPlatformFileNameFilterC1EP7QObject(
    QObject *parent) {
  return new QQuickLabsPlatformFileNameFilter(parent);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  int QQuickLabsPlatformFileNameFilter::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuickLabsPlatformFileNameFilter5indexEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->index();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileNameFilter::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter8setIndexEi(
    QQuickLabsPlatformFileNameFilter *self,
    int index) {
  self->setIndex(index);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter4nameEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QString(self->name());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->extensions());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QSharedPointer<QFileDialogOptions>
//      QQuickLabsPlatformFileNameFilter::options() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFileDialogOptions> *ritual_ZNK32QQuickLabsPlatformFileNameFilter7optionsEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QSharedPointer<QFileDialogOptions>(self->options());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileNameFilter::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QQuickLabsPlatformFileNameFilter *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileNameFilter::update(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter6updateERK7QString(
    QQuickLabsPlatformFileNameFilter *self,
    const QString *filter) {
  self->update(*filter);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformFileNameFilter::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter11nameChangedERK7QString(
    QQuickLabsPlatformFileNameFilter *self,
    const QString *name) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileNameFilter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nameChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nameChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(name)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileNameFilter::extensionsChanged(const
//      QStringList &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter17extensionsChangedERK5QListI7QStringE(
    QQuickLabsPlatformFileNameFilter *self,
    const QList<QString> *extensions) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileNameFilter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "extensionsChanged(const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "extensionsChanged(const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(extensions)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->nameFilters());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi(
    const QQuickLabsPlatformFileNameFilter *self,
    int index) {
  return new QString(self->nameFilter(index));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  a QSharedPointer<QFileDialogOptions> a ritual of
//      QQuickLabsPlatformFileNameFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickLabsPlatformFileNameFilter__QSharedPointer_QFileDialogOptions(
    QSharedPointer<QFileDialogOptions> *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 9)
