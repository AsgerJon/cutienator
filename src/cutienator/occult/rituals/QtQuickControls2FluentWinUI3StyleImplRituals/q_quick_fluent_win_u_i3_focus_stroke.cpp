//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/priv
//  ate/qquickfluentwinui3focusstroke_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickFluentWinUI3FocusStroke' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3styleimplglobal_p.h>
#include <QtQuickControls2FluentWinUI3StyleImpl/QtQuickControls2FluentWinUI3StyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusstroke_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusstroke_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickControls2FluentWinUI3StyleImpl__QQuickFluentWinUI3FocusStroke.cpp, line 1, as moc:QQuickFluentWinUI3FocusStroke
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickFluentWinUI3FocusStroke::qt_create_metaobjectdata<qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickFluentWinUI3FocusStroke",
        "QML.Element",
        "FocusStroke",
        "QML.AddedInVersion",
        "1544",
        "color",
        "QColor",
        "radius"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'color'
        QtMocHelpers::PropertyData<QColor>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final),
        // property 'radius'
        QtMocHelpers::PropertyData<int>(7, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickFluentWinUI3FocusStroke, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickFluentWinUI3FocusStroke::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickPaintedItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t>.metaTypes,
    nullptr
} };

void QQuickFluentWinUI3FocusStroke::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickFluentWinUI3FocusStroke *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QColor*>(_v) = _t->color(); break;
        case 1: *reinterpret_cast<int*>(_v) = _t->radius(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setColor(*reinterpret_cast<QColor*>(_v)); break;
        case 1: _t->setRadius(*reinterpret_cast<int*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickFluentWinUI3FocusStroke::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickFluentWinUI3FocusStroke::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickFluentWinUI3FocusStrokeE_t>.strings))
        return static_cast<void*>(this);
    return QQuickPaintedItem::qt_metacast(_clname);
}

int QQuickFluentWinUI3FocusStroke::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickPaintedItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 13, as _ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter
inline void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
{
    painter->setRenderHint(QPainter::Antialiasing);
    QPainterPath path;
    QRectF rect = boundingRect();
    path.moveTo(rect.left(), rect.top() + m_radius);
    path.lineTo(rect.left(), rect.bottom() - m_radius);
    path.arcTo(QRectF(rect.left(), rect.bottom() - 2 * m_radius, 2 * m_radius, 2 * m_radius), 180, 90);
    path.lineTo(rect.right() - m_radius, rect.bottom());
    path.arcTo(QRectF(rect.right() - 2 * m_radius, rect.bottom() - 2 * m_radius, 2 * m_radius, 2 * m_radius), 270, 90);
    path.lineTo(rect.right(), rect.top() + m_radius);
    path.lineTo(rect.right(), rect.top() + m_radius);
    path.lineTo(rect.right(), rect.top());
    path.lineTo(rect.left(), rect.top());
    painter->fillPath(path, m_color);
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 8, as _ZN29QQuickFluentWinUI3FocusStrokeC1EP10QQuickItem
inline QT_BEGIN_NAMESPACE
QQuickFluentWinUI3FocusStroke::QQuickFluentWinUI3FocusStroke(QQuickItem *parent)
    : QQuickPaintedItem(parent)
{
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 40, as _ZNK29QQuickFluentWinUI3FocusStroke6radiusEv
inline int QQuickFluentWinUI3FocusStroke::radius() const
{
    return m_radius;
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 44, as _ZN29QQuickFluentWinUI3FocusStroke9setRadiusEi
inline void QQuickFluentWinUI3FocusStroke::setRadius(int radius)
{
    if (m_radius == radius)
        return;
    m_radius = radius;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 29, as _ZNK29QQuickFluentWinUI3FocusStroke5colorEv
inline QColor QQuickFluentWinUI3FocusStroke::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 33, as _ZN29QQuickFluentWinUI3FocusStroke8setColorERK6QColor
inline void QQuickFluentWinUI3FocusStroke::setColor(const QColor &color)
{
    if (color == m_color)
        return;
    m_color = color;
    update();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickFluentWinUI3FocusStroke::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickFluentWinUI3FocusStroke10metaObjectEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return self->metaObject();
}

//  void *QQuickFluentWinUI3FocusStroke::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickFluentWinUI3FocusStroke11qt_metacastEPKc(
    QQuickFluentWinUI3FocusStroke *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFluentWinUI3FocusStroke::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickFluentWinUI3FocusStroke11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFluentWinUI3FocusStroke *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFluentWinUI3FocusStroke::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickFluentWinUI3FocusStroke2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFluentWinUI3FocusStroke::tr(s, c, n));
}

//  QQuickFluentWinUI3FocusStroke::QQuickFluentWinUI3FocusStroke(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFluentWinUI3FocusStroke *ritual_ZN29QQuickFluentWinUI3FocusStrokeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFluentWinUI3FocusStroke(parent);
}

//  int QQuickFluentWinUI3FocusStroke::radius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickFluentWinUI3FocusStroke6radiusEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return self->radius();
}

//  void QQuickFluentWinUI3FocusStroke::setRadius(int radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke9setRadiusEi(
    QQuickFluentWinUI3FocusStroke *self,
    int radius) {
  self->setRadius(radius);
}

//  QColor QQuickFluentWinUI3FocusStroke::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK29QQuickFluentWinUI3FocusStroke5colorEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return new QColor(self->color());
}

//  void QQuickFluentWinUI3FocusStroke::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke8setColorERK6QColor(
    QQuickFluentWinUI3FocusStroke *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter(
    QQuickFluentWinUI3FocusStroke *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter(
    QQuickFluentWinUI3FocusStroke *self,
    QPainter *painter) {
  self->QQuickFluentWinUI3FocusStroke::paint(painter);
}
