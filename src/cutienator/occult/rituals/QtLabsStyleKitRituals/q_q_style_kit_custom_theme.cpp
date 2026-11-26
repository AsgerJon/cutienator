//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQStyleKitCustomTheme' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 4 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKit/private/qqstylekitcustomtheme_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQStyleKitCustomTheme.cpp, line 1, as moc:QQStyleKitCustomTheme
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN21QQStyleKitCustomThemeE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitCustomTheme::qt_create_metaobjectdata<qt_meta_tag_ZN21QQStyleKitCustomThemeE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitCustomTheme",
        "QML.Element",
        "CustomTheme",
        "nameChanged",
        "",
        "themeChanged",
        "name",
        "theme",
        "QQmlComponent*"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'nameChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'themeChanged'
        QtMocHelpers::SignalData<void()>(5, 4, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'name'
        QtMocHelpers::PropertyData<QString>(6, QMetaType::QString, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'theme'
        QtMocHelpers::PropertyData<QQmlComponent*>(7, 0x80000000 | 8, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQStyleKitCustomTheme, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQStyleKitCustomTheme::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQStyleKitCustomThemeE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQStyleKitCustomThemeE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN21QQStyleKitCustomThemeE_t>.metaTypes,
    nullptr
} };

void QQStyleKitCustomTheme::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitCustomTheme *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->nameChanged(); break;
        case 1: _t->themeChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitCustomTheme::*)()>(_a, &QQStyleKitCustomTheme::nameChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitCustomTheme::*)()>(_a, &QQStyleKitCustomTheme::themeChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QString*>(_v) = _t->name(); break;
        case 1: *reinterpret_cast<QQmlComponent**>(_v) = _t->theme(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setName(*reinterpret_cast<QString*>(_v)); break;
        case 1: _t->setTheme(*reinterpret_cast<QQmlComponent**>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitCustomTheme::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitCustomTheme::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQStyleKitCustomThemeE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQStyleKitCustomTheme::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
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
void QQStyleKitCustomTheme::nameChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQStyleKitCustomTheme::themeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 57, as _ZN21QQStyleKitCustomThemeC1EP7QObject
inline QQStyleKitCustomTheme::QQStyleKitCustomTheme(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 62, as _ZNK21QQStyleKitCustomTheme4nameEv
inline QString QQStyleKitCustomTheme::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 67, as _ZN21QQStyleKitCustomTheme7setNameERK7QString
inline void QQStyleKitCustomTheme::setName(const QString &newName)
{
    if (m_name == newName)
        return;
    m_name = newName;
    emit nameChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 75, as _ZNK21QQStyleKitCustomTheme5themeEv
inline QQmlComponent *QQStyleKitCustomTheme::theme() const
{
    return m_theme;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcustomtheme.cpp, line 80, as _ZN21QQStyleKitCustomTheme8setThemeEP13QQmlComponent
inline void QQStyleKitCustomTheme::setTheme(QQmlComponent *newTheme)
{
    if (m_theme == newTheme)
        return;
    m_theme = newTheme;
    emit themeChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitCustomTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQStyleKitCustomTheme10metaObjectEv(
    const QQStyleKitCustomTheme *self) {
  return self->metaObject();
}

//  void *QQStyleKitCustomTheme::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQStyleKitCustomTheme11qt_metacastEPKc(
    QQStyleKitCustomTheme *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitCustomTheme::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQStyleKitCustomTheme11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitCustomTheme *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitCustomTheme::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQStyleKitCustomTheme2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitCustomTheme::tr(s, c, n));
}

//  QQStyleKitCustomTheme::QQStyleKitCustomTheme(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitCustomTheme *ritual_ZN21QQStyleKitCustomThemeC1EP7QObject(
    QObject *parent) {
  return new QQStyleKitCustomTheme(parent);
}

//  QString QQStyleKitCustomTheme::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQStyleKitCustomTheme4nameEv(
    const QQStyleKitCustomTheme *self) {
  return new QString(self->name());
}

//  void QQStyleKitCustomTheme::setName(const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme7setNameERK7QString(
    QQStyleKitCustomTheme *self,
    const QString *newName) {
  self->setName(*newName);
}

//  QQmlComponent *QQStyleKitCustomTheme::theme() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQStyleKitCustomTheme5themeEv(
    const QQStyleKitCustomTheme *self) {
  return self->theme();
}

//  void QQStyleKitCustomTheme::setTheme(QQmlComponent *newTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme8setThemeEP13QQmlComponent(
    QQStyleKitCustomTheme *self,
    QQmlComponent *newTheme) {
  self->setTheme(newTheme);
}

//  void QQStyleKitCustomTheme::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme11nameChangedEv(
    QQStyleKitCustomTheme *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitCustomTheme")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nameChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nameChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitCustomTheme::themeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQStyleKitCustomTheme12themeChangedEv(
    QQStyleKitCustomTheme *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitCustomTheme")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "themeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "themeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QList<QQStyleKitCustomTheme *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQStyleKitCustomTheme *> *ritual_list_make_QQStyleKitCustomTheme_ptr() {
  return new QList<QQStyleKitCustomTheme *>();
}

//  void QList<QQStyleKitCustomTheme *>::append(const QQStyleKitCustomTheme *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQStyleKitCustomTheme_ptr(
    QList<QQStyleKitCustomTheme *> *self,
    QQStyleKitCustomTheme *element) {
  self->append(element);
}

//  qsizetype QList<QQStyleKitCustomTheme *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQStyleKitCustomTheme_ptr(
    const QList<QQStyleKitCustomTheme *> *self) {
  return self->size();
}

//  const QQStyleKitCustomTheme * &QList<QQStyleKitCustomTheme
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQStyleKitCustomTheme *ritual_list_at_QQStyleKitCustomTheme_ptr(
    const QList<QQStyleKitCustomTheme *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQStyleKitCustomTheme *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQStyleKitCustomTheme_ptr(
    QList<QQStyleKitCustomTheme *> *self) {
  delete self;
}
