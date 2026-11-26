//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfu
//  sionbusyindicator_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickFusionBusyIndicator' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2FusionStyleImpl/QtQuickControls2FusionStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfusionbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickControls2FusionStyleImpl/private/qquickfusionbusyindicator_p.h>
#include <QtGui/qpainter.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickControls2FusionStyleImpl__QQuickFusionBusyIndicator.cpp, line 1, as moc:QQuickFusionBusyIndicator
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickFusionBusyIndicator::qt_create_metaobjectdata<qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickFusionBusyIndicator",
        "QML.Element",
        "BusyIndicatorImpl",
        "QML.AddedInVersion",
        "515",
        "color",
        "QColor",
        "running"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'color'
        QtMocHelpers::PropertyData<QColor>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final),
        // property 'running'
        QtMocHelpers::PropertyData<bool>(7, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickFusionBusyIndicator, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickFusionBusyIndicator::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickPaintedItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t>.metaTypes,
    nullptr
} };

void QQuickFusionBusyIndicator::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickFusionBusyIndicator *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QColor*>(_v) = _t->color(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->isRunning(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setColor(*reinterpret_cast<QColor*>(_v)); break;
        case 1: _t->setRunning(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickFusionBusyIndicator::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickFusionBusyIndicator::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickFusionBusyIndicatorE_t>.strings))
        return static_cast<void*>(this);
    return QQuickPaintedItem::qt_metacast(_clname);
}

int QQuickFusionBusyIndicator::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 74, as _ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickFusionBusyIndicator::itemChange(ItemChange change, const ItemChangeData &data)
{
    QQuickPaintedItem::itemChange(change, data);

    switch (change) {
    case ItemOpacityHasChanged:
        // If running is set to false and then true within a short period (QTBUG-85860), our
        // OpacityAnimator cancels the 1 => 0 animation (which was for running being set to false),
        // setting opacity to 0 and hence visible to false. This happens _after_ setRunning(true)
        // was called, because the properties were set synchronously but the animation is
        // asynchronous. To account for this situation, we only hide ourselves if we're not running.
        if (qFuzzyIsNull(data.realValue) && !m_running)
            setVisible(false);
        break;
    case ItemVisibleHasChanged:
        update();
        break;
    default:
        break;
    }
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 46, as _ZN25QQuickFusionBusyIndicator5paintEP8QPainter
inline void QQuickFusionBusyIndicator::paint(QPainter *painter)
{
    const qreal w = width();
    const qreal h = height();
    if (w <= 0 || h <= 0 || !isRunning())
        return;

    const qreal sz = qMin(w, h);
    const qreal dx = (w - sz) / 2;
    const qreal dy = (h - sz) / 2;
    const int hpw = qRound(qMax(qreal(1), sz / 14)) & -1;
    const int pw = 2 * hpw;
    const QRectF bounds(dx + hpw, dy + hpw, sz - pw - 1, sz - pw - 1);

    QConicalGradient gradient;
    gradient.setCenter(QPointF(dx + sz / 2, dy + sz / 2));
    gradient.setColorAt(0, m_color);
    gradient.setColorAt(0.1, m_color);
    gradient.setColorAt(1, Qt::transparent);

    painter->translate(0.5, 0.5);
    painter->setRenderHint(QPainter::Antialiasing, true);
    painter->setPen(QPen(gradient, pw, Qt::SolidLine));
    painter->drawArc(bounds, 0, 360 * 16);
    painter->setPen(QPen(m_color, pw, Qt::SolidLine, Qt::RoundCap));
    painter->drawArc(bounds, 0, 20 * 16);
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 11, as _ZN25QQuickFusionBusyIndicatorC1EP10QQuickItem
inline QQuickFusionBusyIndicator::QQuickFusionBusyIndicator(QQuickItem *parent)
    : QQuickPaintedItem(parent)
{
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 16, as _ZNK25QQuickFusionBusyIndicator5colorEv
inline QColor QQuickFusionBusyIndicator::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 21, as _ZN25QQuickFusionBusyIndicator8setColorERK6QColor
inline void QQuickFusionBusyIndicator::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 30, as _ZNK25QQuickFusionBusyIndicator9isRunningEv
inline bool QQuickFusionBusyIndicator::isRunning() const
{
    return isVisible();
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 35, as _ZN25QQuickFusionBusyIndicator10setRunningEb
inline void QQuickFusionBusyIndicator::setRunning(bool running)
{
    m_running = running;

    if (m_running) {
        setVisible(true);
        update();
    }
    // Don't set visible to false if not running, because we use an opacity animation (in QML) to hide ourselves.
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickFusionBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFusionBusyIndicator : QQuickFusionBusyIndicator {
  using QQuickFusionBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickFusionBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickFusionBusyIndicator10metaObjectEv(
    const QQuickFusionBusyIndicator *self) {
  return self->metaObject();
}

//  void *QQuickFusionBusyIndicator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickFusionBusyIndicator11qt_metacastEPKc(
    QQuickFusionBusyIndicator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFusionBusyIndicator::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickFusionBusyIndicator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFusionBusyIndicator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFusionBusyIndicator::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickFusionBusyIndicator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFusionBusyIndicator::tr(s, c, n));
}

//  QQuickFusionBusyIndicator::QQuickFusionBusyIndicator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFusionBusyIndicator *ritual_ZN25QQuickFusionBusyIndicatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFusionBusyIndicator(parent);
}

//  QColor QQuickFusionBusyIndicator::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickFusionBusyIndicator5colorEv(
    const QQuickFusionBusyIndicator *self) {
  return new QColor(self->color());
}

//  void QQuickFusionBusyIndicator::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator8setColorERK6QColor(
    QQuickFusionBusyIndicator *self,
    const QColor *color) {
  self->setColor(*color);
}

//  bool QQuickFusionBusyIndicator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickFusionBusyIndicator9isRunningEv(
    const QQuickFusionBusyIndicator *self) {
  return self->isRunning();
}

//  void QQuickFusionBusyIndicator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator10setRunningEb(
    QQuickFusionBusyIndicator *self,
    bool running) {
  self->setRunning(running);
}

//  void QQuickFusionBusyIndicator::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator5paintEP8QPainter(
    QQuickFusionBusyIndicator *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFusionBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFusionBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickFusionBusyIndicator::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFusionBusyIndicator5paintEP8QPainter(
    QQuickFusionBusyIndicator *self,
    QPainter *painter) {
  self->QQuickFusionBusyIndicator::paint(painter);
}

//  void QQuickFusionBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFusionBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickFusionBusyIndicator *>(self)->OwnQQuickFusionBusyIndicator::itemChange(
      change,
      *data);
}
