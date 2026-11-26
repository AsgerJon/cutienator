//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickLabsPlatformStandardPaths' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 3 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 4)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h>
#if QT_DEPRECATED_SINCE(6, 4)
#include <QtQml/qqmlengine.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 37, as local:qquicklabsplatformstandardpaths.cpp:toUrlList
#if QT_DEPRECATED_SINCE(6, 4)
static QList<QUrl> toUrlList(const QStringList &paths)
{
    QList<QUrl> urls;
    urls.reserve(paths.size());
    for (const QString &path : paths)
        urls += QUrl::fromLocalFile(path);
    return urls;
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from QtLabsPlatform__QQuickLabsPlatformStandardPaths.cpp, line 1, as moc:QQuickLabsPlatformStandardPaths
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickLabsPlatformStandardPaths::qt_create_metaobjectdata<qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickLabsPlatformStandardPaths",
        "QML.Singleton",
        "true",
        "QML.Element",
        "StandardPaths",
        "QML.AddedInVersion",
        "256",
        "QML.Extended",
        "QStandardPaths",
        "QML.ExtensionIsNamespace",
        "displayName",
        "",
        "QStandardPaths::StandardLocation",
        "type",
        "findExecutable",
        "QUrl",
        "executableName",
        "paths",
        "locate",
        "fileName",
        "QStandardPaths::LocateOptions",
        "options",
        "locateAll",
        "QList<QUrl>",
        "setTestModeEnabled",
        "testMode",
        "standardLocations",
        "writableLocation"
    };

    QtMocHelpers::UintData qt_methods {
        // Method 'displayName'
        QtMocHelpers::MethodData<QString(QStandardPaths::StandardLocation)>(10, 11, QMC::AccessPublic, QMetaType::QString, {{
            { 0x80000000 | 12, 13 },
        }}),
        // Method 'findExecutable'
        QtMocHelpers::MethodData<QUrl(const QString &, const QStringList &)>(14, 11, QMC::AccessPublic, 0x80000000 | 15, {{
            { QMetaType::QString, 16 }, { QMetaType::QStringList, 17 },
        }}),
        // Method 'findExecutable'
        QtMocHelpers::MethodData<QUrl(const QString &)>(14, 11, QMC::AccessPublic | QMC::MethodCloned, 0x80000000 | 15, {{
            { QMetaType::QString, 16 },
        }}),
        // Method 'locate'
        QtMocHelpers::MethodData<QUrl(QStandardPaths::StandardLocation, const QString &, QStandardPaths::LocateOptions)>(18, 11, QMC::AccessPublic, 0x80000000 | 15, {{
            { 0x80000000 | 12, 13 }, { QMetaType::QString, 19 }, { 0x80000000 | 20, 21 },
        }}),
        // Method 'locate'
        QtMocHelpers::MethodData<QUrl(QStandardPaths::StandardLocation, const QString &)>(18, 11, QMC::AccessPublic | QMC::MethodCloned, 0x80000000 | 15, {{
            { 0x80000000 | 12, 13 }, { QMetaType::QString, 19 },
        }}),
        // Method 'locateAll'
        QtMocHelpers::MethodData<QList<QUrl>(QStandardPaths::StandardLocation, const QString &, QStandardPaths::LocateOptions)>(22, 11, QMC::AccessPublic, 0x80000000 | 23, {{
            { 0x80000000 | 12, 13 }, { QMetaType::QString, 19 }, { 0x80000000 | 20, 21 },
        }}),
        // Method 'locateAll'
        QtMocHelpers::MethodData<QList<QUrl>(QStandardPaths::StandardLocation, const QString &)>(22, 11, QMC::AccessPublic | QMC::MethodCloned, 0x80000000 | 23, {{
            { 0x80000000 | 12, 13 }, { QMetaType::QString, 19 },
        }}),
        // Method 'setTestModeEnabled'
        QtMocHelpers::MethodData<void(bool)>(24, 11, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 25 },
        }}),
        // Method 'standardLocations'
        QtMocHelpers::MethodData<QList<QUrl>(QStandardPaths::StandardLocation)>(26, 11, QMC::AccessPublic, 0x80000000 | 23, {{
            { 0x80000000 | 12, 13 },
        }}),
        // Method 'writableLocation'
        QtMocHelpers::MethodData<QUrl(QStandardPaths::StandardLocation)>(27, 11, QMC::AccessPublic, 0x80000000 | 15, {{
            { 0x80000000 | 12, 13 },
        }}),
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
            {    9,    2 },
    });
    return QtMocHelpers::metaObjectData<QQuickLabsPlatformStandardPaths, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickLabsPlatformStandardPaths::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t>.metaTypes,
    nullptr
} };

void QQuickLabsPlatformStandardPaths::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickLabsPlatformStandardPaths *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { QString _r = _t->displayName((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QString*>(_a[0]) = std::move(_r); }  break;
        case 1: { QUrl _r = _t->findExecutable((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QStringList>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QUrl*>(_a[0]) = std::move(_r); }  break;
        case 2: { QUrl _r = _t->findExecutable((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QUrl*>(_a[0]) = std::move(_r); }  break;
        case 3: { QUrl _r = _t->locate((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QStandardPaths::LocateOptions>>(_a[3])));
            if (_a[0]) *reinterpret_cast<QUrl*>(_a[0]) = std::move(_r); }  break;
        case 4: { QUrl _r = _t->locate((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QUrl*>(_a[0]) = std::move(_r); }  break;
        case 5: { QList<QUrl> _r = _t->locateAll((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QStandardPaths::LocateOptions>>(_a[3])));
            if (_a[0]) *reinterpret_cast<QList<QUrl>*>(_a[0]) = std::move(_r); }  break;
        case 6: { QList<QUrl> _r = _t->locateAll((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QList<QUrl>*>(_a[0]) = std::move(_r); }  break;
        case 7: _t->setTestModeEnabled((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 8: { QList<QUrl> _r = _t->standardLocations((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QList<QUrl>*>(_a[0]) = std::move(_r); }  break;
        case 9: { QUrl _r = _t->writableLocation((*reinterpret_cast<std::add_pointer_t<QStandardPaths::StandardLocation>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QUrl*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
}

const QMetaObject *QQuickLabsPlatformStandardPaths::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickLabsPlatformStandardPaths::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQuickLabsPlatformStandardPathsE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickLabsPlatformStandardPaths::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 10;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 124, as _ZN31QQuickLabsPlatformStandardPaths17standardLocationsEN14QStandardPaths16StandardLocationE
#if QT_DEPRECATED_SINCE(6, 4)
inline QList<QUrl> QQuickLabsPlatformStandardPaths::standardLocations(QStandardPaths::StandardLocation type)
{
    return toUrlList(QStandardPaths::standardLocations(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 46, as _ZN31QQuickLabsPlatformStandardPathsC1EP7QObject
#if QT_DEPRECATED_SINCE(6, 4)
inline QQuickLabsPlatformStandardPaths::QQuickLabsPlatformStandardPaths(QObject *parent)
    : QObject(parent)
{
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 51, as _ZN31QQuickLabsPlatformStandardPaths6createEP10QQmlEngineP9QJSEngine
#if QT_DEPRECATED_SINCE(6, 4)
inline QObject *QQuickLabsPlatformStandardPaths::create(QQmlEngine *engine, QJSEngine *scriptEngine)
{
    Q_UNUSED(scriptEngine);
    return new QQuickLabsPlatformStandardPaths(engine);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 64, as _ZN31QQuickLabsPlatformStandardPaths11displayNameEN14QStandardPaths16StandardLocationE
#if QT_DEPRECATED_SINCE(6, 4)
inline QString QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::StandardLocation type)
{
    return QStandardPaths::displayName(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 76, as _ZN31QQuickLabsPlatformStandardPaths14findExecutableERK7QStringRK5QListIS0_E
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::findExecutable(const QString &executableName, const QStringList &paths)
{
    return QUrl::fromLocalFile(QStandardPaths::findExecutable(executableName, paths));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 88, as _ZN31QQuickLabsPlatformStandardPaths6locateEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::locate(QStandardPaths::StandardLocation type, const QString &fileName, QStandardPaths::LocateOptions options)
{
    return QUrl::fromLocalFile(QStandardPaths::locate(type, fileName, options));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 100, as _ZN31QQuickLabsPlatformStandardPaths9locateAllEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE
#if QT_DEPRECATED_SINCE(6, 4)
inline QList<QUrl> QQuickLabsPlatformStandardPaths::locateAll(QStandardPaths::StandardLocation type, const QString &fileName, QStandardPaths::LocateOptions options)
{
    return toUrlList(QStandardPaths::locateAll(type, fileName, options));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 112, as _ZN31QQuickLabsPlatformStandardPaths18setTestModeEnabledEb
#if QT_DEPRECATED_SINCE(6, 4)
inline void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool testMode)
{
    QStandardPaths::setTestModeEnabled(testMode);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformstandardpaths.cpp, line 136, as _ZN31QQuickLabsPlatformStandardPaths16writableLocationEN14QStandardPaths16StandardLocationE
#if QT_DEPRECATED_SINCE(6, 4)
inline QUrl QQuickLabsPlatformStandardPaths::writableLocation(QStandardPaths::StandardLocation type)
{
    return QUrl::fromLocalFile(QStandardPaths::writableLocation(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLabsPlatformStandardPaths::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformStandardPaths10metaObjectEv(
    const QQuickLabsPlatformStandardPaths *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformStandardPaths::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickLabsPlatformStandardPaths11qt_metacastEPKc(
    QQuickLabsPlatformStandardPaths *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformStandardPaths::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickLabsPlatformStandardPaths11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformStandardPaths *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QString QQuickLabsPlatformStandardPaths::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickLabsPlatformStandardPaths2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLabsPlatformStandardPaths::tr(s, c, n));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  void QQuickLabsPlatformStandardPaths::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths22qt_qmlMarker_singletonEv(
    QQuickLabsPlatformStandardPaths *self) {
  self->qt_qmlMarker_singleton();
}

//  const QMetaObject
//      *QQuickLabsPlatformStandardPaths::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN31QQuickLabsPlatformStandardPaths20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformStandardPaths::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformStandardPaths::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformStandardPaths *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QQuickLabsPlatformStandardPaths::QQuickLabsPlatformStandardPaths(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformStandardPaths *ritual_ZN31QQuickLabsPlatformStandardPathsC1EP7QObject(
    QObject *parent) {
  return new QQuickLabsPlatformStandardPaths(parent);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QObject *QQuickLabsPlatformStandardPaths::create(QQmlEngine *engine,
//      QJSEngine *scriptEngine)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN31QQuickLabsPlatformStandardPaths6createEP10QQmlEngineP9QJSEngine(
    QQmlEngine *engine,
    QJSEngine *scriptEngine) {
  return QQuickLabsPlatformStandardPaths::create(engine, scriptEngine);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QString QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::Stan
//      dardLocation type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickLabsPlatformStandardPaths11displayNameEN14QStandardPaths16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QString(QQuickLabsPlatformStandardPaths::displayName(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl QQuickLabsPlatformStandardPaths::findExecutable(const QString
//      &executableName, const QStringList &paths)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths14findExecutableERK7QStringRK5QListIS0_E(
    const QString *executableName,
    const QList<QString> *paths) {
  return new QUrl(
      QQuickLabsPlatformStandardPaths::findExecutable(
          *executableName,
          *paths));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl
//      QQuickLabsPlatformStandardPaths::locate(QStandardPaths::StandardLocat
//      ion type, const QString &fileName, QStandardPaths::LocateOptions
//      options)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths6locateEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE(
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QUrl(
      QQuickLabsPlatformStandardPaths::locate(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QList<QUrl> QQuickLabsPlatformStandardPaths::locateAll(QStandardPaths::St
//      andardLocation type, const QString &fileName,
//      QStandardPaths::LocateOptions options)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN31QQuickLabsPlatformStandardPaths9locateAllEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE(
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QList<QUrl>(
      QQuickLabsPlatformStandardPaths::locateAll(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool testMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformStandardPaths18setTestModeEnabledEb(
    bool testMode) {
  QQuickLabsPlatformStandardPaths::setTestModeEnabled(testMode);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#if QT_DEPRECATED_SINCE(6, 4)
//  QUrl QQuickLabsPlatformStandardPaths::writableLocation(QStandardPaths::St
//      andardLocation type)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN31QQuickLabsPlatformStandardPaths16writableLocationEN14QStandardPaths16StandardLocationE(
    QStandardPaths::StandardLocation type) {
  return new QUrl(QQuickLabsPlatformStandardPaths::writableLocation(type));
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

#endif  // QT_DEPRECATED_SINCE(6, 4)
